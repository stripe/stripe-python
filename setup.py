import os
import sys
import warnings

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))


with open('LONG_DESCRIPTION.rst') as f:
    long_description = f.read()

version_contents = {}
with open(os.path.join('stripe', 'version.py')) as f:
    exec(f.read(), version_contents)

setup(
    name='stripe',
    version=version_contents['VERSION'],
    description='Python bindings for the Stripe API',
    long_description=long_description,
    author='Stripe',
    author_email='support@stripe.com',
    url='https://github.com/stripe/stripe-python',
    license='MIT',
    packages=['stripe', 'stripe.api_resources',
              'stripe.api_resources.abstract'],
    package_data={'stripe': ['data/ca-certificates.crt']},
    install_requires=[
        'requests >= 0.8.8',
    ],
    test_suite='tests',
    tests_require=['unittest2', 'mock'],
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
