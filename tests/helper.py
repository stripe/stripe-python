from __future__ import absolute_import, division, print_function

import os
import sys
import unittest2

from distutils.version import StrictVersion

import stripe
from stripe.six.moves.urllib.request import urlopen
from stripe.six.moves.urllib.error import HTTPError

from tests.request_mock import RequestMock


MOCK_MINIMUM_VERSION = '0.16.1'
MOCK_PORT = os.environ.get('STRIPE_MOCK_PORT', 12111)


try:
    resp = urlopen('http://localhost:%s/' % MOCK_PORT)
    info = resp.info()
except HTTPError as e:
    info = e.info()
except Exception:
    sys.exit("Couldn't reach stripe-mock at `localhost:%s`. Is "
             "it running? Please see README for setup instructions." %
             MOCK_PORT)

version = info.get('Stripe-Mock-Version')
if version != 'master' \
        and StrictVersion(version) < StrictVersion(MOCK_MINIMUM_VERSION):
    sys.exit("Your version of stripe-mock (%s) is too old. The minimum "
             "version to run this test suite is %s. Please "
             "see its repository for upgrade instructions." %
             (version, MOCK_MINIMUM_VERSION))


class StripeTestCase(unittest2.TestCase):
    def setUp(self):
        super(StripeTestCase, self).setUp()

        stripe.orig_attrs = {
            'api_base': stripe.api_base,
            'api_key': stripe.api_key,
            'client_id': stripe.client_id,
            'default_http_client': stripe.default_http_client,
        }
        stripe.api_base = 'http://localhost:%s' % MOCK_PORT
        stripe.api_key = 'sk_test_123'
        stripe.client_id = 'ca_123'

        self.client = stripe.http_client.new_default_http_client()
        stripe.default_http_client = self.client

        self.request_mock = RequestMock()
        self.request_mock.start()

    def tearDown(self):
        super(StripeTestCase, self).tearDown()

        self.request_mock.stop()

        self.client.close()

        stripe.api_base = stripe.orig_attrs['api_base']
        stripe.api_key = stripe.orig_attrs['api_key']
        stripe.client_id = stripe.orig_attrs['client_id']
        stripe.default_http_client = stripe.orig_attrs['default_http_client']

    def stub_request(self, *args, **kwargs):
        return self.request_mock.stub_request(*args, **kwargs)

    def assert_requested(self, *args, **kwargs):
        return self.request_mock.assert_requested(*args, **kwargs)

    def assert_no_request(self):
        return self.request_mock.assert_no_request()
