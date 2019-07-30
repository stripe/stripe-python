from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "txn_123"


class TestBalanceTransaction(object):
    def test_is_listable(self, request_mock):
        resources = stripe.BalanceTransaction.list()
        request_mock.assert_requested("get", "/v1/balance_transactions")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.BalanceTransaction)

    def test_is_retrievable(self, request_mock):
        resource = stripe.BalanceTransaction.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/balance_transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.BalanceTransaction)
