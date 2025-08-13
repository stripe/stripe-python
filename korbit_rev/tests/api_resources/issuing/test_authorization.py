import stripe


TEST_RESOURCE_ID = "iauth_123"


class TestAuthorization(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.issuing.Authorization.list()
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/authorizations"
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Authorization)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.issuing.Authorization.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        authorization = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    def test_can_approve(self, http_client_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = resource.approve()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s/approve" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    def test_can_approve_classmethod(self, http_client_mock):
        resource = stripe.issuing.Authorization.approve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s/approve" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    def test_can_decline(self, http_client_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = resource.decline()
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s/decline" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    def test_can_decline_classmethod(self, http_client_mock):
        resource = stripe.issuing.Authorization.decline(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/%s/decline" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.issuing.Authorization)
