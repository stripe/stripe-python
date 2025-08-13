import stripe


TEST_RESOURCE_ID = "pts_123"


class TestSession(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.billing_portal.Session.create(
            customer="cus_123", return_url="https://stripe.com/return"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/sessions",
            post_data="customer=cus_123&return_url=https://stripe.com/return",
        )
        assert isinstance(resource, stripe.billing_portal.Session)
