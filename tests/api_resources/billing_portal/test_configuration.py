import stripe


TEST_RESOURCE_ID = "bpc_123"


class TestConfiguration(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.billing_portal.Configuration.create(
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/tos",
            },
            features={
                "customer_update": {
                    "allowed_updates": ["address"],
                    "enabled": True,
                }
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/configurations",
            post_data="business_profile[privacy_policy_url]=https://example.com/privacy&business_profile[terms_of_service_url]=https://example.com/tos&features[customer_update][allowed_updates][0]=address&features[customer_update][enabled]=true",
        )
        assert isinstance(resource, stripe.billing_portal.Configuration)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.billing_portal.Configuration.retrieve(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/billing_portal/configurations/%s" % (TEST_RESOURCE_ID),
        )
        assert isinstance(resource, stripe.billing_portal.Configuration)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.billing_portal.Configuration.modify(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/configurations/%s" % (TEST_RESOURCE_ID),
        )
        assert isinstance(resource, stripe.billing_portal.Configuration)

    def test_is_listable(self, http_client_mock):
        resource = stripe.billing_portal.Configuration.list()
        http_client_mock.assert_requested(
            "get", path="/v1/billing_portal/configurations"
        )
        assert isinstance(
            resource.data[0], stripe.billing_portal.Configuration
        )
