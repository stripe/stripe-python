from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeResourceTest


class TransferTest(StripeResourceTest):

    def test_list_transfers(self):
        stripe.Transfer.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers',
            {}
        )

    def test_cancel_transfer(self):
        self.mock_response({
            'id': 'tr_cancel',
            'status': 'canceled',
        })

        transfer = stripe.Transfer(id='tr_cancel')

        self.assertTrue(transfer is transfer.cancel(idempotency_key='idem-foo'))
        self.assertEquals('canceled', transfer.status)
        self.assertEquals('tr_cancel', transfer.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_cancel/cancel',
            {},
            {'Idempotency-Key': 'idem-foo'}
        )


class TransferReversalsTests(StripeResourceTest):
    def test_create_reversal(self):
        stripe.Transfer.create_reversal(
            'tr_123',
            amount=100
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_123/reversals',
            {'amount': 100},
            None
        )

    def test_retrieve_reversal(self):
        stripe.Transfer.retrieve_reversal(
            'tr_123',
            'trr_123'
        )
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_123/reversals/trr_123',
            {},
            None
        )

    def test_modify_reversal(self):
        stripe.Transfer.modify_reversal(
            'tr_123',
            'trr_123',
            metadata={'foo': 'bar'}
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_123/reversals/trr_123',
            {'metadata': {'foo': 'bar'}},
            None
        )

    def test_list_reversals(self):
        stripe.Transfer.list_reversals(
            'tr_123'
        )
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_123/reversals',
            {},
            None
        )
