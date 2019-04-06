from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "cn_123"


class TestCreditNote(object):
    def test_is_listable(self, request_mock):
        resources = stripe.CreditNote.list()
        request_mock.assert_requested("get", "/v1/credit_notes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.CreditNote)

    def test_is_retrievable(self, request_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_is_creatable(self, request_mock):
        resource = stripe.CreditNote.create(
            amount=100, invoice="in_123", reason="duplicate"
        )
        request_mock.assert_requested("post", "/v1/credit_notes")
        assert isinstance(resource, stripe.CreditNote)

    def test_is_saveable(self, request_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.CreditNote.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/credit_notes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_can_void_credit_note(self, request_mock):
        resource = stripe.CreditNote.retrieve(TEST_RESOURCE_ID)
        resource = resource.void_credit_note()
        request_mock.assert_requested(
            "post", "/v1/credit_notes/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CreditNote)

    def test_can_void_credit_note_classmethod(self, request_mock):
        resource = stripe.CreditNote.void_credit_note(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/credit_notes/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CreditNote)
