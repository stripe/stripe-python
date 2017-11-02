from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class ApplicationFeeTest(StripeResourceTest):

    def test_list_application_fees(self):
        stripe.ApplicationFee.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees',
            {}
        )


class ApplicationFeeRefundsTests(StripeResourceTest):
    def test_create_refund(self):
        stripe.ApplicationFee.create_refund(
            'fee_123'
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/application_fees/fee_123/refunds',
            {},
            None
        )

    def test_retrieve_refund(self):
        stripe.ApplicationFee.retrieve_refund(
            'fee_123',
            'fr_123'
        )
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_123/refunds/fr_123',
            {},
            None
        )

    def test_modify_refund(self):
        stripe.ApplicationFee.modify_refund(
            'fee_123',
            'fr_123',
            metadata={'foo': 'bar'}
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/application_fees/fee_123/refunds/fr_123',
            {'metadata': {'foo': 'bar'}},
            None
        )

    def test_list_refunds(self):
        stripe.ApplicationFee.list_refunds(
            'fee_123'
        )
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_123/refunds',
            {},
            None
        )
