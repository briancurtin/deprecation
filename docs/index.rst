.. deprecation documentation master file, created by
   sphinx-quickstart on Fri Jan 13 16:03:40 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

``deprecation``
===============

``deprecation`` is a library that enables automated deprecations. It offers
the :func:`~deprecation.deprecated` decorator to wrap functions, providing
proper warnings both in documentation and via Python's :mod:`warnings` system,
as well as the :func:`deprecation.fail_if_not_removed` decorator for test
methods to ensure that deprecated code is eventually removed.

See `API Documentation`_ to jump straight into the options. See the
:doc:`sample` page for an example of ``deprecation``'s effect on a module's
Sphinx `autodoc <http://www.sphinx-doc.org/en/master/ext/autodoc.html>`_
generated documentation.

Installation
============

 ::

    pip install deprecation

Using ``@deprecated``
=====================

To mark a function or method as deprecated, wrap it in the
:func:`~deprecation.deprecated` decorator. This does several things for you:

1. The docstring of the wrapped function will have details appended
   to it from the arguments you set on :func:`~deprecation.deprecated`.
   This takes care of telling your users not only that the function
   is deprecated, but can also tell them when it's going away and
   what they can do in the meantime.
2. In conjunction with the :func:`~deprecation.fail_if_not_removed`
   decorator it removes the need for any sort of manual tracking of
   when a sufficiently deprecated piece of code should be removed
   from the codebase. It causes tests to fail when they contain
   code which should be removed.

 ::

    import deprecation

    @deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                            current_version=__version__,
                            details="Use the bar function instead")
    def foo():
        """Do some stuff"""
        return 1

Now look at the docs. If you you generate API documentation from your source
like the :doc:`sample` does, you'll see that the a sentence has been
appended to a deprecated function's docstring to include information about
when the function is deprecated, when it'll be removed, and what you can do
instead. For example, run ``help(foo)`` and this is what you'll get:

 ::

    Help on function foo in module example:

    foo()
        Do some stuff

        *Deprecated in 1.0, to be removed in 2.0. Use the bar function instead*

You can pass varying amounts of detail to this decorator, but note that
in most cases it removes the ability to use
:func:`~deprecation.fail_if_not_removed`. See the `API Documentation`_
for full details.

Using ``@fail_if_not_removed``
==============================

Once you've marked code for deprecation via :func:`~deprecation.deprecated`,
you can sit back and relax as most of the work has been done for you.
Assuming you've provided sufficient detail to the decorator, you now just
wait for your tests to tell you it's time to delete the code in question.

If you wrap test methods which use your now deprecated code in
:func:`~deprecation.fail_if_not_removed`, the test will fail with a message
notifying you that you should remove this code.

 ::

    @deprecation.fail_if_not_removed
    def test_won(self):
        self.assertEqual(1, won())

Looking at the :doc:`sample` docs, we can see that this function would
fail the tests at version 2.0, when it should be removed. The following
shows what test output will look like for a failure.

 ::

    AssertionError: <function Tests.test_won at 0x10af33268> uses a function
    that should be removed: who is unsupported as of 2.0. Use the ``one``
    function instead

API Documentation
=================

.. automodule:: deprecation
   :members:
