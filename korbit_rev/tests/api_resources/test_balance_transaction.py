import stripe


TEST_RESOURCE_ID = "txn_123"


class TestBalanceTransaction(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.BalanceTransaction.list()
        http_client_mock.assert_requested(
            "get", path="/v1/balance_transactions"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.BalanceTransaction)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.BalanceTransaction.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/balance_transactions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.BalanceTransaction)
