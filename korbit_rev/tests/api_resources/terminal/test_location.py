import stripe


TEST_RESOURCE_ID = "loc_123"


class TestLocation(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.terminal.Location.create(
            display_name="name",
            address={
                "line1": "line1",
                "country": "US",
                "state": "CA",
                "postal_code": "12345",
                "city": "San Francisco",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/locations",
            post_data="display_name=name&address[city]=San+Francisco&address[country]=US&address[line1]=line1&address[postal_code]=12345&address[state]=CA",
        )
        assert isinstance(resource, stripe.terminal.Location)

    def test_is_listable(self, http_client_mock):
        resources = stripe.terminal.Location.list()
        http_client_mock.assert_requested("get", path="/v1/terminal/locations")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.terminal.Location)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.terminal.Location.modify(
            TEST_RESOURCE_ID, display_name="new-name"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/locations/%s" % TEST_RESOURCE_ID,
            post_data="display_name=new-name",
        )
        assert isinstance(resource, stripe.terminal.Location)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.terminal.Location.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.terminal.Location)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.terminal.Location.retrieve(TEST_RESOURCE_ID)
        resource.display_name = "new-name"
        location = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/locations/%s" % TEST_RESOURCE_ID,
            post_data="display_name=new-name",
        )
        assert isinstance(resource, stripe.terminal.Location)
        assert resource is location

    def test_is_deletable(self, http_client_mock):
        resource = stripe.terminal.Location.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.terminal.Location.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/terminal/locations/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
