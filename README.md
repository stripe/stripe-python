# Stripe Python bindings [![Build Status](https://travis-ci.org/stripe/stripe-python.svg?branch=master)](https://travis-ci.org/stripe/stripe-python)

## Installation

You don't need this source code unless you want to modify the
package. If you just want to use the Stripe Python bindings, you
should run:

    pip install --upgrade stripe

or

    easy_install --upgrade stripe

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead. If you're not using virtualenv,
you may have to prefix those commands with `sudo`. You can learn more
about virtualenv at http://www.virtualenv.org/

To install from source, run:

    python setup.py install

## Documentation

Please see https://stripe.com/docs/api/python for the most up-to-date documentation.

## Testing

We commit to being compatible with Python 2.6+, Python 3.1+ and PyPy.  We need to test against all of these environments to ensure compatibility.  Travis CI will automatically run our tests on push.  For local testing, we use [tox](http://tox.readthedocs.org/) to handle testing across environments.

### Setting up tox

In theory, you should be able to `pip install tox` and then simply run `tox` from the project root. In reality, Tox can take a bit of finagling to get working.

You'll need an interpreter installed for each of the versions of python we test (see the envlist in tox.ini).  You can find these releases [on the Python site](https://www.python.org/download/releases) and [at PyPy](http://pypy.org/download.html#installing).  If you're using OS X, it may be easier to get PyPy from Homebrew with `brew install pypy`.

You may choose not to go through the hassle of installing interpreters for every Python version we support.  It's useful to test at least one Python 2.x and one Python 3.x but can generally rely on Travis to find edge cases with other interpreters.  You can test a specific interpreter such as Python 2.7 with `tox -e py27`.

The system Python on OS X has been known to cause issues. You'll probably want to `brew install python` or equivalent.  If tox complains about `pkg_resources.DistributionNotFound` then some of your Python libraries are probably still linked to the system python installation.  To fix this for virtualenv you should `sudo pip uninstall virtualenv; pip install virtualenv`.

Note that PyCurl doesn't currently play nicely with our tox configuration.  Tox won't run any of the PyCurl related tests.

### Running specific tests

You can specify a module, TestCase or single test to run by passing it as an argument to tox.  For example, to run only the `test_save` test of the `UpdateableAPIResourceTests` case from the `test.resources` module on Python 2.7:

    tox -e py27 -- --test-suite stripe.test.resources.test_updateable.UpdateableAPIResourceTests.test_save

### Linting

We enforce linting on the code with flake8.  Install with `pip install flake8` and run with `flake8 stripe` from the project root.  Linting will also be run in Travis CI and for the Python 2.7 environment with Tox.  Note that linting will fail on code that has undergone 2to3 conversion for Python 3 support.
