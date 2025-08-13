import stripe


TEST_RESOURCE_ID = "evt_123"


class TestEvent(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Event.list()
        http_client_mock.assert_requested("get", path="/v1/events")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Event)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Event.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/events/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Event)
