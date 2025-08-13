import stripe


TEST_RESOURCE_ID = "pi_123"


class TestPaymentIntent(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.PaymentIntent.list()
        http_client_mock.assert_requested("get", path="/v1/payment_intents")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentIntent)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/payment_intents/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.PaymentIntent.create(
            amount="1234", currency="amount", payment_method_types=["card"]
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents",
            post_data="amount=1234&currency=amount&payment_method_types[0]=card",
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.PaymentIntent.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)

        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_cancel(self, http_client_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.cancel()
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.PaymentIntent.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_capture(self, http_client_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.capture()
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_capture_classmethod(self, http_client_mock):
        resource = stripe.PaymentIntent.capture(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/capture" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_confirm(self, http_client_mock):
        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        resource.confirm()
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)

    def test_can_confirm_classmethod(self, http_client_mock):
        resource = stripe.PaymentIntent.confirm(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payment_intents/%s/confirm" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentIntent)
