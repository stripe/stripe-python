import stripe


TEST_RESOURCE_ID = "apwc_123"


class TestApplePayDomain(object):
    def test_is_listable(self, request_mock):
        resources = stripe.ApplePayDomain.list()
        request_mock.assert_requested("get", "/v1/apple_pay/domains")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplePayDomain)

    def test_is_retrievable(self, request_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_creatable(self, request_mock):
        resource = stripe.ApplePayDomain.create(domain_name="test.com")
        request_mock.assert_requested("post", "/v1/apple_pay/domains")
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_deletable(self, request_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, request_mock):
        resource = stripe.ApplePayDomain.delete(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "delete", "/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
