from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'txn_123'


class TestBalanceTransaction(object):
    def test_is_listable(self, request_mock):
        resources = stripe.BalanceTransaction.list()
        request_mock.assert_requested(
            'get',
            '/v1/balance/history',
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.BalanceTransaction)
