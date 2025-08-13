import stripe


TEST_RESOURCE_ID = "vs_123"


class TestVerificationSession(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.identity.VerificationSession.create(type="id_number")
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions",
            post_data="type=id_number",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)

    def test_is_listable(self, http_client_mock):
        resources = stripe.identity.VerificationSession.list()
        http_client_mock.assert_requested(
            "get", path="/v1/identity/verification_sessions"
        )
        assert isinstance(resources.data, list)
        assert isinstance(
            resources.data[0], stripe.identity.VerificationSession
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.identity.VerificationSession.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.identity.VerificationSession)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        resource.metadata["key"] = "value"
        verification_session = resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)
        assert resource is verification_session

    def test_can_cancel(self, http_client_mock):
        resource = stripe.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        verification_session = resource.cancel()
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s/cancel"
            % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)
        assert resource is verification_session

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.identity.VerificationSession.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s/cancel"
            % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)

    def test_can_redact(self, http_client_mock):
        resource = stripe.identity.VerificationSession.retrieve(
            TEST_RESOURCE_ID
        )
        verification_session = resource.redact()
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s/redact"
            % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)
        assert resource is verification_session

    def test_can_redact_classmethod(self, http_client_mock):
        resource = stripe.identity.VerificationSession.redact(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/%s/redact"
            % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.identity.VerificationSession)
