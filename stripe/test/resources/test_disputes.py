import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_DISPUTE, NOW
)


class DisputeTest(StripeResourceTest):

    def test_list_all_disputes(self):
        stripe.Dispute.list(created={'lt': NOW})

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/disputes',
            {
                'created': {'lt': NOW},
            }
        )

    def test_create_dispute(self):
        stripe.Dispute.create(idempotency_key='foo', **DUMMY_DISPUTE)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes',
            DUMMY_DISPUTE,
            {'Idempotency-Key': 'foo'},
        )

    def test_retrieve_dispute(self):
        stripe.Dispute.retrieve('dp_test_id')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/disputes/dp_test_id',
            {},
            None
        )

    def test_update_dispute(self):
        dispute = stripe.Dispute.construct_from({
            'id': 'dp_update_id',
            'evidence': {
                'product_description': 'description',
            },
        }, 'api_key')
        dispute.evidence['customer_name'] = 'customer'
        dispute.evidence['uncategorized_text'] = 'text'
        dispute.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes/dp_update_id',
            {'evidence': {
                'customer_name': 'customer',
                'uncategorized_text': 'text',
            }},
            None
        )

    def test_close_dispute(self):
        dispute = stripe.Dispute(id='dp_close_id')
        dispute.close(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes/dp_close_id/close',
            {},
            {'Idempotency-Key': 'foo'},
        )
