import stripe


TEST_RESOURCE_ID = "rdr_123"


class TestReader(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.terminal.Reader.create(
            registration_code="a-b-c", label="name"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers",
            post_data="label=name&registration_code=a-b-c",
        )
        assert isinstance(resource, stripe.terminal.Reader)

    def test_is_listable(self, http_client_mock):
        resources = stripe.terminal.Reader.list()
        http_client_mock.assert_requested("get", path="/v1/terminal/readers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.terminal.Reader)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.terminal.Reader.modify(
            TEST_RESOURCE_ID, label="new-name"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/%s" % TEST_RESOURCE_ID,
            post_data="label=new-name",
        )
        assert isinstance(resource, stripe.terminal.Reader)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.terminal.Reader)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.label = "new-name"
        reader = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/%s" % TEST_RESOURCE_ID,
            post_data="label=new-name",
        )
        assert isinstance(resource, stripe.terminal.Reader)
        assert resource is reader

    def test_is_deletable(self, http_client_mock):
        resource = stripe.terminal.Reader.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.terminal.Reader.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/terminal/readers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_present_payment_method(self, http_client_mock):
        resource = stripe.terminal.Reader.TestHelpers.present_payment_method(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/terminal/readers/%s/present_payment_method"
            % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.terminal.Reader)
