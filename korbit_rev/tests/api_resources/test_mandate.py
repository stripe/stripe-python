import stripe


TEST_RESOURCE_ID = "mandate_123"


class TestMandateSchedule(object):
    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Mandate.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/mandates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Mandate)
