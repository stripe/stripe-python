import pytest

from urllib.parse import parse_qs, urlparse

import stripe
from stripe._stripe_client import StripeClient


class TestOAuth(object):
    @pytest.fixture
    def stripe_client(self, http_client_mock) -> StripeClient:
        return StripeClient(
            "sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
            client_id="ca_123",
        )

    def test_authorize_url(self, stripe_client: StripeClient):
        url = stripe_client.oauth.authorize_url(
            {
                "scope": "read_write",
                "state": "csrf_token",
                "stripe_user": {
                    "email": "test@example.com",
                    "url": "https://example.com/profile/test",
                    "country": "US",
                },
            }
        )
        o = urlparse(url)
        params = parse_qs(o.query)

        url_express = stripe_client.oauth.authorize_url(
            {"scope": "read_write", "state": "csrf_token"}, {"express": True}
        )
        o_express = urlparse(url_express)

        assert o.scheme == "https"
        assert o.netloc == "connect.stripe.com"
        assert o.path == "/oauth/authorize"
        assert o_express.path == "/express/oauth/authorize"

        assert params["client_id"] == ["ca_123"]
        assert params["scope"] == ["read_write"]
        assert params["stripe_user[email]"] == ["test@example.com"]
        assert params["stripe_user[url]"] == [
            "https://example.com/profile/test"
        ]
        assert params["stripe_user[country]"] == ["US"]

    def test_token(self, stripe_client: StripeClient, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/oauth/token",
            rbody='{"access_token":"sk_access_token","scope":"read_only","livemode":"false","token_type":"bearer","refresh_token":"sk_refresh_token","stripe_user_id":"acct_test","stripe_publishable_key":"pk_test"}',
        )

        resp = stripe_client.oauth.token(
            {
                "grant_type": "authorization_code",
                "code": "this_is_an_authorization_code",
            }
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.connect_api_base,
            path="/oauth/token",
            post_data="grant_type=authorization_code&code=this_is_an_authorization_code",
        )
        assert resp["access_token"] == "sk_access_token"

    def test_deauthorize(self, stripe_client: StripeClient, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/oauth/deauthorize",
            rbody='{"stripe_user_id":"acct_test_deauth"}',
        )

        resp = stripe_client.oauth.deauthorize(
            {
                "stripe_user_id": "acct_test_deauth",
            }
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.connect_api_base,
            path="/oauth/deauthorize",
            post_data="client_id=ca_123&stripe_user_id=acct_test_deauth",
        )
        assert resp["stripe_user_id"] == "acct_test_deauth"

    def test_uses_client_connect_api_base(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/oauth/token",
            rbody='{"access_token":"sk_access_token","scope":"read_only","livemode":"false","token_type":"bearer","refresh_token":"sk_refresh_token","stripe_user_id":"acct_test","stripe_publishable_key":"pk_test"}',
        )

        expected_api_base = "https://connect.example.com"
        client = stripe.StripeClient(
            "sk_test_123",
            base_addresses={"connect": expected_api_base},
            http_client=http_client_mock.get_mock_http_client(),
        )

        resp = client.oauth.token(
            {
                "grant_type": "authorization_code",
                "code": "ac_123456789",
            }
        )
        http_client_mock.assert_requested(
            "post",
            api_base=expected_api_base,
            path="/oauth/token",
        )
        assert resp["access_token"] == "sk_access_token"
