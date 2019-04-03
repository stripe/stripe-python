from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "pi_123"


class TestPaymentIntent(object):
    def test_is_listable(self, request_mock):
        resources = stripe.PaymentIntent.list()
        request_mock.assert_requested("get", "/v1/payment_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentIntent)

    def test_is_retrievable(self, request_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/payment_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_creatable(self, request_mock):
        resource = stripe.PaymentIntent.create(
            amount="1234", currency="amount", payment_method_types=["card"]
        )
        request_mock.assert_requested("post", "/v1/payment_intents")
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_modifiable(self, request_mock):
        resource = stripe.PaymentIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_saveable(self, request_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post",
            "/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            {"metadata": {"key": "value"}},
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_cancel(self, request_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.cancel()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_cancel_classmethod(self, request_mock):
        resource = stripe.PaymentIntent.cancel(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_capture(self, request_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.capture()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_capture_classmethod(self, request_mock):
        resource = stripe.PaymentIntent.capture(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_confirm(self, request_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.confirm()
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_confirm_classmethod(self, request_mock):
        resource = stripe.PaymentIntent.confirm(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "post", "/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)
