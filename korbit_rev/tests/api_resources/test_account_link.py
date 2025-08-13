import stripe


class TestAccountLink(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.AccountLink.create(
            account="acct_123",
            refresh_url="https://stripe.com/failure",
            return_url="https://stripe.com/success",
            type="account_onboarding",
        )
        http_client_mock.assert_requested("post", path="/v1/account_links")
        assert isinstance(resource, stripe.AccountLink)
