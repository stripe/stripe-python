import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

# Don't import stripe module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stripe'))
import importer
import version

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

requests = 'requests >= 0.8.8'
if sys.version_info < (2, 6):
  requests += ', < 0.10.1'
install_requires = [requests]

# Get simplejson if we don't already have json
try:
  importer.import_json()
except ImportError:
  install_requires.append('simplejson')

try:
  import json
  _json_loaded = hasattr(json, 'loads')
except ImportError:
  pass

setup(name='stripe',
      cmdclass = {'build_py': build_py},
      version=version.VERSION,
      description='Stripe python bindings',
      author='Stripe',
      author_email='support@stripe.com',
      url='https://stripe.com/',
      packages=['stripe','stripe.test'],
      package_data={'stripe' : ['data/ca-certificates.crt', '../VERSION']},
      install_requires=install_requires,
      test_suite='stripe.test',
)
