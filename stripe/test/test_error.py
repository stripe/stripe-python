# -*- coding: utf-8 -*-
import unittest2

from stripe import StripeError
from stripe.test.helper import StripeUnitTestCase


class StripeErrorTests(StripeUnitTestCase):

    def test_bytestring(self):
        err = StripeError('error')
        assert str(err) == 'error'

    def test_bytestring_with_request_id(self):
        err = StripeError('error', headers={'request-id': '123'})
        assert str(err) == 'Request 123: error'

    def test_unicode(self):
        err = StripeError(u'öre')
        assert unicode(err) == u'öre'

    def test_unicode_with_request_id(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        assert unicode(err) == u'Request 123: öre'


if __name__ == '__main__':
    unittest2.main()
