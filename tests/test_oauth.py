from __future__ import absolute_import, division, print_function

from stripe.six.moves.urllib.parse import parse_qs, urlparse

import stripe


class TestOAuth(object):
    def test_authorize_url(self, request_mock):
        url = stripe.OAuth.authorize_url(
            scope="read_write",
            state="csrf_token",
            stripe_user={
                "email": "test@example.com",
                "url": "https://example.com/profile/test",
                "country": "US",
            },
        )
        o = urlparse(url)
        params = parse_qs(o.query)

        url_express = stripe.OAuth.authorize_url(
            express=True, scope="read_write", state="csrf_token"
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

    def test_token(self, request_mock):
        request_mock.stub_request(
            "post",
            "/oauth/token",
            {
                "access_token": "sk_access_token",
                "scope": "read_only",
                "livemode": "false",
                "token_type": "bearer",
                "refresh_token": "sk_refresh_token",
                "stripe_user_id": "acct_test",
                "stripe_publishable_key": "pk_test",
            },
        )

        resp = stripe.OAuth.token(
            grant_type="authorization_code",
            code="this_is_an_authorization_code",
        )
        request_mock.assert_requested(
            "post",
            "/oauth/token",
            {
                "grant_type": "authorization_code",
                "code": "this_is_an_authorization_code",
            },
        )
        assert resp["access_token"] == "sk_access_token"

    def test_deauthorize(self, request_mock):
        request_mock.stub_request(
            "post",
            "/oauth/deauthorize",
            {"stripe_user_id": "acct_test_deauth"},
        )

        resp = stripe.OAuth.deauthorize(stripe_user_id="acct_test_deauth")
        request_mock.assert_requested(
            "post",
            "/oauth/deauthorize",
            {"client_id": "ca_123", "stripe_user_id": "acct_test_deauth"},
        )
        assert resp["stripe_user_id"] == "acct_test_deauth"
