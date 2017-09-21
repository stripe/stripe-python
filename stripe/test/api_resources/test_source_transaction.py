import stripe
from stripe.test.helper import StripeResourceTest


class SourceTransactionTest(StripeResourceTest):
    def test_list_source_transactions(self):
        source = stripe.Source.construct_from({
            'id': 'src_test',
            'type': 'ach_credit'
        }, 'api_key')

        source.source_transactions()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/sources/src_test/source_transactions',
            {},
            None
        )
