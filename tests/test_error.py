# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from stripe import six, StripeError


class TestError(object):
    def test_formatting(self):
        err = StripeError(u'öre')
        if six.PY3:
            assert str(err) == u'öre'
        else:
            assert str(err) == '\xc3\xb6re'
            assert unicode(err) == u'öre'

    def test_formatting_with_request_id(self):
        err = StripeError(u'öre', headers={'request-id': '123'})
        if six.PY3:
            assert str(err) == u'Request 123: öre'
        else:
            assert str(err) == 'Request 123: \xc3\xb6re'
            assert unicode(err) == u'Request 123: öre'

    def test_formatting_with_none(self):
        err = StripeError(None, headers={'request-id': '123'})
        if six.PY3:
            assert str(err) == u'Request 123: <empty message>'
        else:
            assert str(err) == 'Request 123: <empty message>'
            assert unicode(err) == u'Request 123: <empty message>'
