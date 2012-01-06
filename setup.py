import os
import sys
from distutils.core import setup

# Don't import stripe module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'stripe'))
import version

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

setup(name='stripe',
      version=version.VERSION,
      description='Stripe python bindings',
      author='Stripe',
      author_email='support@stripe.com',
      url='https://stripe.com/',
      packages=['stripe'],
      package_data={'stripe' : ['data/ca-certificates.crt', '../VERSION']},
      install_requires=['simplejson', 'requests']
)
