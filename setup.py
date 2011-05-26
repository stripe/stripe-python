from distutils.core import setup
import os, sys

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

setup(name='stripe',
      version='1.5.0',
      description='Stripe python bindings',
      author='Stripe',
      author_email='support@stripe.com',
      url='https://stripe.com/',
      packages=['stripe'],
      requires=['json', 'pycurl']
)
