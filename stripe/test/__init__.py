import unittest
import os
import stripe

from mock import patch, Mock

class StripeTestCase(unittest.TestCase):
    RESTORE_ATTRIBUTES = ('_httplib', 'api_version', 'api_key')
    REQUEST_LIBRARIES = ('requests', 'urlfetch', 'pycurl', 'urllib2')

    def setUp(self):
        super(StripeTestCase, self).setUp()

        self._stripe_original_attributes = {}

        for attr in self.RESTORE_ATTRIBUTES:
            self._stripe_original_attributes[attr] = getattr(stripe, attr)

        api_base = os.environ.get('STRIPE_API_BASE')
        if api_base:
            stripe.api_base = api_base
        stripe.api_key = os.environ.get('STRIPE_API_KEY', 'tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I')

    def tearDown(self):
        super(StripeTestCase, self).tearDown()

        for attr in self.RESTORE_ATTRIBUTES:
            setattr(stripe, attr, self._stripe_original_attributes[attr])


class StripeUnitTestCase(StripeTestCase):
    def setUp(self):
        super(StripeUnitTestCase, self).setUp()

        self.request_patchers = {}
        self.request_mocks = {}
        for lib in self.REQUEST_LIBRARIES:
            patcher = patch("stripe.%s" % lib)

            self.request_mocks[lib] = patcher.start()
            self.request_patchers[lib] = patcher

    def tearDown(self):
        super(StripeUnitTestCase, self).tearDown()

        for patcher in self.request_patchers.itervalues():
            patcher.stop()


class StripeApiTestCase(StripeUnitTestCase):
    def setUp(self):
        old_utf_8 = stripe.APIRequestor._utf8

        self.requestor_patcher = patch('stripe.APIRequestor')
        requestor_class_mock = self.requestor_patcher.start()
        self.requestor_mock = requestor_class_mock.return_value

        requestor_class_mock._utf8 = old_utf_8

    def tearDown(self):
        self.requestor_patcher.stop()

    def mock_response(self, res):
        self.requestor_mock.request = Mock(return_value=(res, 'reskey'))
