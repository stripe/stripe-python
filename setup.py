import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# The Requests package added a release in 2.14.0 that broke a whole bunch of
# people on old versions of pip and setuptools (< 18.0.0). Here we check to see
# whether we have a version that might be affected so that we can add a maximum
# version for Requests.
#
# This can probably removed after most people have moved to setuptools 18.0.0+.
#
# More context here: https://github.com/stripe/stripe-python/pull/311
old_setuptools_version = False
try:
    from distutils.version import StrictVersion
    import setuptools
    if StrictVersion(setuptools.__version__) < StrictVersion("18.0.0"):
        old_setuptools_version = True
except ImportError:
    pass

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

if sys.version_info < (2, 6):
    warnings.warn(
        'Python 2.5 is no longer officially supported by Stripe. '
        'If you have any questions, please file an issue on Github or '
        'contact us at support@stripe.com.',
        DeprecationWarning)
    install_requires.append('requests >= 0.8.8, < 0.10.1')
    install_requires.append('ssl')
elif old_setuptools_version:
    install_requires.append('requests >= 0.8.8, < 2.14.0')
else:
    install_requires.append('requests >= 0.8.8')


with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

# Don't import stripe module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stripe'))
from version import VERSION

# Get simplejson if we don't already have json
if sys.version_info < (3, 0):
    try:
        from util import json
    except ImportError:
        install_requires.append('simplejson')


setup(
    name='stripe',
    cmdclass={'build_py': build_py},
    version=VERSION,
    description='Stripe python bindings',
    long_description=long_description,
    author='Stripe',
    author_email='support@stripe.com',
    url='https://github.com/stripe/stripe-python',
    packages=['stripe', 'stripe.test', 'stripe.test.resources'],
    package_data={'stripe': ['data/ca-certificates.crt']},
    install_requires=install_requires,
    test_suite='stripe.test.all',
    tests_require=['unittest2', 'mock'],
    use_2to3=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
