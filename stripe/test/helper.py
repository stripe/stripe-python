import datetime
import os
import random
import string
import sys
import unittest2

from mock import patch, Mock

import stripe

NOW = datetime.datetime.now()

DUMMY_CHARGE = {
    'amount': 100,
    'currency': 'usd',
    'source': 'tok_visa'
}

DUMMY_DISPUTE = {
    'status': 'needs_response',
    'currency': 'usd',
    'metadata': {}
}

DUMMY_PLAN = {
    'amount': 2000,
    'interval': 'month',
    'name': 'Amazing Gold Plan',
    'currency': 'usd',
    'id': ('stripe-test-gold-' +
           ''.join(random.choice(string.ascii_lowercase) for x in range(10)))
}

DUMMY_COUPON = {
    'percent_off': 25,
    'duration': 'repeating',
    'duration_in_months': 5,
    'metadata': {}
}

DUMMY_RECIPIENT = {
    'name': 'John Doe',
    'type': 'individual'
}

DUMMY_TRANSFER = {
    'amount': 400,
    'currency': 'usd',
    'recipient': 'self'
}

DUMMY_APPLE_PAY_DOMAIN = {
    'domain_name': 'test.com',
}

DUMMY_INVOICE_ITEM = {
    'amount': 456,
    'currency': 'usd',
}

SAMPLE_INVOICE = stripe.util.json.loads("""
{
  "amount_due": 1305,
  "attempt_count": 0,
  "attempted": true,
  "charge": "ch_wajkQ5aDTzFs5v",
  "closed": true,
  "customer": "cus_osllUe2f1BzrRT",
  "date": 1338238728,
  "discount": null,
  "ending_balance": 0,
  "id": "in_t9mHb2hpK7mml1",
  "livemode": false,
  "next_payment_attempt": null,
  "object": "invoice",
  "paid": true,
  "period_end": 1338238728,
  "period_start": 1338238716,
  "starting_balance": -8695,
  "subtotal": 10000,
  "total": 10000,
  "lines": {
    "invoiceitems": [],
    "prorations": [],
    "subscriptions": [
      {
        "plan": {
          "interval": "month",
          "object": "plan",
          "identifier": "expensive",
          "currency": "usd",
          "livemode": false,
          "amount": 10000,
          "name": "Expensive Plan",
          "trial_period_days": null,
          "id": "expensive"
        },
        "period": {
          "end": 1340917128,
          "start": 1338238728
        },
        "amount": 10000
      }
    ]
  }
}
""")

DUMMY_WEBHOOK_PAYLOAD = """{
  "id": "evt_test_webhook",
  "object": "event"
}"""

DUMMY_WEBHOOK_SECRET = 'whsec_test_secret'


class StripeTestCase(unittest2.TestCase):
    RESTORE_ATTRIBUTES = ('api_version', 'api_key', 'client_id')

    def setUp(self):
        super(StripeTestCase, self).setUp()

        self._stripe_original_attributes = {}

        for attr in self.RESTORE_ATTRIBUTES:
            self._stripe_original_attributes[attr] = getattr(stripe, attr)

        api_base = os.environ.get('STRIPE_API_BASE')
        if api_base:
            stripe.api_base = api_base
        stripe.api_key = os.environ.get(
            'STRIPE_API_KEY', 'tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I')
        stripe.api_version = os.environ.get(
            'STRIPE_API_VERSION', '2017-04-06')

    def tearDown(self):
        super(StripeTestCase, self).tearDown()

        for attr in self.RESTORE_ATTRIBUTES:
            setattr(stripe, attr, self._stripe_original_attributes[attr])


class StripeUnitTestCase(StripeTestCase):
    REQUEST_LIBRARIES = ['urlfetch', 'requests', 'pycurl']

    if sys.version_info >= (3, 0):
        REQUEST_LIBRARIES.append('urllib.request')
    else:
        REQUEST_LIBRARIES.append('urllib2')

    def setUp(self):
        super(StripeUnitTestCase, self).setUp()

        self.request_patchers = {}
        self.request_mocks = {}
        for lib in self.REQUEST_LIBRARIES:
            patcher = patch("stripe.http_client.%s" % (lib,))

            self.request_mocks[lib] = patcher.start()
            self.request_patchers[lib] = patcher

    def tearDown(self):
        super(StripeUnitTestCase, self).tearDown()

        for patcher in self.request_patchers.itervalues():
            patcher.stop()


class StripeApiTestCase(StripeTestCase):

    def setUp(self):
        super(StripeApiTestCase, self).setUp()

        self.requestor_patcher = patch('stripe.api_requestor.APIRequestor')
        requestor_class_mock = self.requestor_patcher.start()
        self.requestor_mock = requestor_class_mock.return_value

    def tearDown(self):
        super(StripeApiTestCase, self).tearDown()

        self.requestor_patcher.stop()

    def mock_response(self, res):
        self.requestor_mock.request = Mock(return_value=(res, 'reskey'))


class StripeResourceTest(StripeApiTestCase):

    def setUp(self):
        super(StripeResourceTest, self).setUp()
        self.mock_response({})


class MyResource(stripe.resource.APIResource):
    pass


class MySingleton(stripe.resource.SingletonAPIResource):
    pass


class MyListable(stripe.resource.ListableAPIResource):
    pass


class MyCreatable(stripe.resource.CreateableAPIResource):
    pass


class MyUpdateable(stripe.resource.UpdateableAPIResource):
    pass


class MyDeletable(stripe.resource.DeletableAPIResource):
    pass


class MyComposite(stripe.resource.ListableAPIResource,
                  stripe.resource.CreateableAPIResource,
                  stripe.resource.UpdateableAPIResource,
                  stripe.resource.DeletableAPIResource):
    pass
