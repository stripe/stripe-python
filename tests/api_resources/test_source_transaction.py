from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class SourceTransactionTest(StripeTestCase):
    def test_is_listable(self):
        source = stripe.Source.construct_from({
            'id': 'src_123',
            'object': 'source'
        }, stripe.api_key)
        source_transactions = source.source_transactions()
        self.assert_requested(
            'get',
            '/v1/sources/src_123/source_transactions'
        )
        self.assertIsInstance(source_transactions.data, list)
        self.assertIsInstance(source_transactions.data[0],
                              stripe.SourceTransaction)
