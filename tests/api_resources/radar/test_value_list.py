import stripe


TEST_RESOURCE_ID = "rsl_123"


class TestValueList(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.radar.ValueList.list()
        http_client_mock.assert_requested("get", path="/v1/radar/value_lists")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.radar.ValueList)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.radar.ValueList.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/radar/value_lists/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.radar.ValueList)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.radar.ValueList.create(alias="alias", name="name")
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_lists",
            post_data="alias=alias&name=name",
        )
        assert isinstance(resource, stripe.radar.ValueList)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.radar.ValueList.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_lists/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.radar.ValueList.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_lists/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.radar.ValueList)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.radar.ValueList.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/radar/value_lists/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.radar.ValueList.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/radar/value_lists/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
