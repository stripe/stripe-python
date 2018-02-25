# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from stripe import six, error


class TestError(object):
    def test_formatting(self):
        err = error.StripeError(u'öre')
        assert six.text_type(err) == u'öre'
        if six.PY2:
            assert str(err) == '\xc3\xb6re'

    def test_formatting_with_request_id(self):
        err = error.StripeError(u'öre', headers={'request-id': '123'})
        assert six.text_type(err) == u'Request 123: öre'
        if six.PY2:
            assert str(err) == 'Request 123: \xc3\xb6re'

    def test_formatting_with_none(self):
        err = error.StripeError(None, headers={'request-id': '123'})
        assert six.text_type(err) == u'Request 123: <empty message>'
        if six.PY2:
            assert str(err) == 'Request 123: <empty message>'
