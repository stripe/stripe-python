# -*- coding: utf-8 -*-
import sys

import unittest2

from stripe import StripeError
from stripe.test.helper import StripeUnitTestCase


class StripeErrorTests(StripeUnitTestCase):

    def test_formatting(self):
        err = StripeError(u'öre')
        if sys.version_info > (3, 0):
            assert str(err) == u'öre'
        else:
            assert str(err) == '\xc3\xb6re'
            assert unicode(err) == u'öre'

    def test_formatting_with_request_id(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        if sys.version_info > (3, 0):
            assert str(err) == u'Request 123: öre'
        else:
            assert str(err) == 'Request 123: \xc3\xb6re'
            assert unicode(err) == u'Request 123: öre'

    def test_formatting_with_none(self):
        err = StripeError(None, headers={'request-id': '123'})
        if sys.version_info > (3, 0):
            assert str(err) == u'Request 123: <empty message>'
        else:
            assert str(err) == 'Request 123: <empty message>'
            assert unicode(err) == u'Request 123: <empty message>'


if __name__ == '__main__':
    unittest2.main()
