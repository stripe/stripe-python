import stripe


TEST_RESOURCE_ID = "usd"


class TestExchangeRate(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.ExchangeRate.list()
        http_client_mock.assert_requested("get", path="/v1/exchange_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ExchangeRate)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.ExchangeRate.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/exchange_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ExchangeRate)
