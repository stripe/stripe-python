import stripe


TEST_RESOURCE_ID = "cn_123"


class TestCreditNote(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.CreditNote.list()
        http_client_mock.assert_requested("get", path="/v1/credit_notes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.CreditNote)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.CreditNote.create(
            amount=100, invoice="in_123", reason="duplicate"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes",
            post_data="amount=100&invoice=in_123&reason=duplicate",
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.CreditNote.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_can_preview(self, http_client_mock):
        resource = stripe.CreditNote.preview(invoice="in_123", amount=500)
        http_client_mock.assert_requested(
            "get",
            path="/v1/credit_notes/preview",
            query_string="amount=500&invoice=in_123",
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_can_void_credit_note(self, http_client_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource = resource.void_credit_note()
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes/%s/void" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_can_void_credit_note_classmethod(self, http_client_mock):
        resource = stripe.CreditNote.void_credit_note(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes/%s/void" % TEST_RESOURCE_ID,
            post_data="",
        )
        assert isinstance(resource, stripe.CreditNote)
