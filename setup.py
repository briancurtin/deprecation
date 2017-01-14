from setuptools import setup

AUTHOR = "Brian Curtin"
EMAIL = "brian@python.org"


setup(name="deprecation",
      description="A library to handle automated deprecations",
      license="Apache 2",
      url="https://deprecation.readthedocs.io/",
      version="1.0",
      author=AUTHOR,
      author_email=EMAIL,
      maintainer=AUTHOR,
      maintainer_email=EMAIL,
      keywords=["deprecation"],
      long_description=open("README.rst").read(),
      py_modules=["deprecation"],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"]
      )
