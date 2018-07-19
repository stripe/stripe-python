from __future__ import absolute_import, division, print_function

import os
import sys
from distutils.version import StrictVersion

import pytest

import stripe
from stripe.six.moves.urllib.request import urlopen
from stripe.six.moves.urllib.error import HTTPError

from tests.request_mock import RequestMock


MOCK_MINIMUM_VERSION = '0.23.0'
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


@pytest.fixture(autouse=True)
def setup_stripe():
    orig_attrs = {
        'api_base': stripe.api_base,
        'api_key': stripe.api_key,
        'client_id': stripe.client_id,
        'default_http_client': stripe.default_http_client,
    }
    http_client = stripe.http_client.new_default_http_client()
    stripe.api_base = 'http://localhost:%s' % MOCK_PORT
    stripe.api_key = 'sk_test_123'
    stripe.client_id = 'ca_123'
    stripe.default_http_client = http_client
    yield
    http_client.close()
    stripe.api_base = orig_attrs['api_base']
    stripe.api_key = orig_attrs['api_key']
    stripe.client_id = orig_attrs['client_id']
    stripe.default_http_client = orig_attrs['default_http_client']


@pytest.fixture
def request_mock(mocker):
    return RequestMock(mocker)
