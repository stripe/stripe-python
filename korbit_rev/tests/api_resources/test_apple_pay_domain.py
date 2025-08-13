import stripe


TEST_RESOURCE_ID = "apwc_123"


class TestApplePayDomain(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.ApplePayDomain.list()
        http_client_mock.assert_requested("get", path="/v1/apple_pay/domains")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplePayDomain)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.ApplePayDomain.create(domain_name="test.com")
        http_client_mock.assert_requested("post", path="/v1/apple_pay/domains")
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.ApplePayDomain.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/apple_pay/domains/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
