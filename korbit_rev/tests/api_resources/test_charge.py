import stripe


TEST_RESOURCE_ID = "ch_123"


class TestCharge(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Charge.list()
        http_client_mock.assert_requested("get", path="/v1/charges")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Charge)

    def test_is_searchable(self, http_client_mock):
        resources = stripe.Charge.search(query='currency:"USD"')
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges/search",
            query_string='query=currency:"USD"',
        )
        assert resources.total_count == 1
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Charge)

        cnt = 0
        for c in resources.auto_paging_iter():
            assert isinstance(c, stripe.Charge)
            cnt += 1

        assert cnt == 1

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/charges/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Charge.create(
            amount=100, currency="usd", source="tok_123"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges",
            post_data="amount=100&currency=usd&source=tok_123",
        )
        assert isinstance(resource, stripe.Charge)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Charge)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Charge.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Charge)

    def test_can_capture(self, http_client_mock):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.capture()
        http_client_mock.assert_requested(
            "post", path="/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    def test_can_capture_classmethod(self, http_client_mock):
        resource = stripe.Charge.capture(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/charges/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Charge)

    def test_can_mark_as_fraudulent(self, http_client_mock):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_fraudulent()
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/%s" % charge.id,
            post_data="fraud_details[user_report]=fraudulent",
        )
        assert isinstance(resource, stripe.Charge)

    def test_can_mark_as_safe(self, http_client_mock):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_safe()
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/%s" % charge.id,
            post_data="fraud_details[user_report]=safe",
        )
        assert isinstance(resource, stripe.Charge)
