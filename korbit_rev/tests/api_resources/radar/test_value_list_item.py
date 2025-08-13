import stripe


TEST_RESOURCE_ID = "rsli_123"


class TestValueListItem(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.radar.ValueListItem.list(value_list="rsl_123")
        http_client_mock.assert_requested(
            "get", path="/v1/radar/value_list_items"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.radar.ValueListItem)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.radar.ValueListItem.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.radar.ValueListItem)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.radar.ValueListItem.create(
            value_list="rsl_123", value="value"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_list_items",
            post_data="value_list=rsl_123&value=value",
        )
        assert isinstance(resource, stripe.radar.ValueListItem)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.radar.ValueListItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.radar.ValueListItem.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/radar/value_list_items/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
