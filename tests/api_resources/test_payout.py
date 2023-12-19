import stripe


TEST_RESOURCE_ID = "po_123"


class TestPayout(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Payout.list()
        http_client_mock.assert_requested("get", path="/v1/payouts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Payout)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/payouts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Payout.create(amount=100, currency="usd")
        http_client_mock.assert_requested(
            "post", path="/v1/payouts", post_data="amount=100&currency=usd"
        )
        assert isinstance(resource, stripe.Payout)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Payout.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_cancel(self, http_client_mock):
        payout = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource = payout.cancel()
        http_client_mock.assert_requested(
            "post", path="/v1/payouts/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.Payout.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payouts/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_reverse(self, http_client_mock):
        payout = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource = payout.reverse()
        http_client_mock.assert_requested(
            "post", path="/v1/payouts/%s/reverse" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_reverse_classmethod(self, http_client_mock):
        resource = stripe.Payout.reverse(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payouts/%s/reverse" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)
