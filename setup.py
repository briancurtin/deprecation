import io
from setuptools import setup

AUTHOR = "Brian Curtin"
EMAIL = "brian@python.org"


setup(name="deprecation",
      version="1.1",
      description="A library to handle automated deprecations",
      license="Apache 2",
      url="http://deprecation.readthedocs.io/",
      author=AUTHOR,
      author_email=EMAIL,
      maintainer=AUTHOR,
      maintainer_email=EMAIL,
      install_requires=["packaging"],
      keywords=["deprecation"],
      long_description=io.open("README.rst", encoding="utf-8").read(),
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
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules"]
      )
