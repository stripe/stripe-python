import stripe


TEST_RESOURCE_ID = "pm_123"


class TestPaymentMethod(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.PaymentMethod.list(customer="cus_123", type="card")
        http_client_mock.assert_requested("get", path="/v1/payment_methods")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PaymentMethod)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/payment_methods/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.PaymentMethod.create(
            type="card", card={"token": "tok_123"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods",
            post_data="type=card&card[token]=tok_123",
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.PaymentMethod.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_can_attach(self, http_client_mock):
        resource = stripe.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource = resource.attach(customer="cus_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/%s/attach" % TEST_RESOURCE_ID,
            post_data="customer=cus_123",
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_can_attach_classmethod(self, http_client_mock):
        resource = stripe.PaymentMethod.attach(
            TEST_RESOURCE_ID, customer="cus_123"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/%s/attach" % TEST_RESOURCE_ID,
            post_data="customer=cus_123",
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_can_detach(self, http_client_mock):
        resource = stripe.PaymentMethod.retrieve(TEST_RESOURCE_ID)
        resource = resource.detach()
        http_client_mock.assert_requested(
            "post", path="/v1/payment_methods/%s/detach" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentMethod)

    def test_can_detach_classmethod(self, http_client_mock):
        resource = stripe.PaymentMethod.detach(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/payment_methods/%s/detach" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PaymentMethod)
