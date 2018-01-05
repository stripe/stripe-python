import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

# Don't import stripe module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stripe'))
from version import VERSION

setup(
    name='stripe',
    version=VERSION,
    description='Stripe python bindings',
    long_description=long_description,
    author='Stripe',
    author_email='support@stripe.com',
    url='https://github.com/stripe/stripe-python',
    packages=['stripe', 'stripe.api_resources',
              'stripe.api_resources.abstract'],
    package_data={'stripe': ['data/ca-certificates.crt']},
    install_requires=install_requires,
    test_suite='tests',
    tests_require=['unittest2', 'mock'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
