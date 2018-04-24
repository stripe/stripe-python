# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from stripe import six, StripeError
from tests.helper import StripeTestCase


class StripeErrorTests(StripeTestCase):

    def test_formatting(self):
        err = StripeError(u'öre')
        self.assertEqual(u'öre', six.text_type(err))
        if six.PY2:
            self.assertEqual('\xc3\xb6re', str(err))
        else:
            self.assertEqual(u'öre', str(err))

    def test_formatting_with_request_id(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        self.assertEqual(u'Request 123: öre', six.text_type(err))
        if six.PY2:
            self.assertEqual('Request 123: \xc3\xb6re', str(err))
        else:
            self.assertEqual(u'Request 123: öre', str(err))

    def test_formatting_with_none(self):
        err = StripeError(None, headers={'request-id': '123'})
        self.assertEqual(u'Request 123: <empty message>', six.text_type(err))
        if six.PY2:
            self.assertEqual('Request 123: <empty message>', str(err))
        else:
            self.assertEqual('Request 123: <empty message>', str(err))
