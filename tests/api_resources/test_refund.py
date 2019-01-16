from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "re_123"


class TestRefund(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Refund.list()
        request_mock.assert_requested("get", "/v1/refunds")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Refund)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)

    def test_is_creatable(self, request_mock):
        resource = stripe.Refund.create(charge="ch_123")
        request_mock.assert_requested("post", "/v1/refunds")
        assert isinstance(resource, stripe.Refund)

    def test_is_saveable(self, request_mock):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Refund.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/refunds/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Refund)
