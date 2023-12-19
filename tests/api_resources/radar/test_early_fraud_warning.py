import stripe


TEST_RESOURCE_ID = "issfr_123"


class TestEarlyFraudWarning(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.radar.EarlyFraudWarning.list()
        http_client_mock.assert_requested(
            "get", path="/v1/radar/early_fraud_warnings"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.radar.EarlyFraudWarning)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.radar.EarlyFraudWarning.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/radar/early_fraud_warnings/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.radar.EarlyFraudWarning)
