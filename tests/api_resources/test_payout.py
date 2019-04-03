from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "po_123"


class TestPayout(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Payout.list()
        request_mock.assert_requested("get", "/v1/payouts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Payout)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/payouts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_is_creatable(self, request_mock):
        resource = stripe.Payout.create(amount=100, currency="usd")
        request_mock.assert_requested("post", "/v1/payouts")
        assert isinstance(resource, stripe.Payout)

    def test_is_saveable(self, request_mock):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/payouts/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Payout.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/payouts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_cancel(self, request_mock):
        payout = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource = payout.cancel()
        request_mock.assert_requested(
            "post", "/v1/payouts/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)

    def test_can_cancel_classmethod(self, request_mock):
        resource = stripe.Payout.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payouts/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Payout)
