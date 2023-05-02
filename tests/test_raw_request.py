from __future__ import absolute_import, division, print_function

import stripe


class TestRawRequest(object):
    def test_form_request(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/accounts/acct_123",
            '{"id": "acct_123", "object": "account"}',
        )

        resp = stripe.raw_request("get", "/v1/accounts/acct_123")
        request_mock.assert_requested(
            "get", "/v1/accounts/acct_123", {}, None, "form"
        )

        assert resp.body == '{"id": "acct_123", "object": "account"}'

        deserialized = stripe.deserialize(resp)
        assert isinstance(deserialized, stripe.Account)

    def test_form_request_with_extra_headers(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/accounts/acct_123",
            '{"id": "acct_123", "object": "account"}',
        )

        resp = stripe.raw_request(
            "get",
            "/v1/accounts/acct_123",
            headers={"Stripe-Account": "acct_123"},
        )

        request_mock.assert_requested(
            "get",
            "/v1/accounts/acct_123",
            {},
            {"Stripe-Account": "acct_123"},
            "form",
        )

        assert resp.body == '{"id": "acct_123", "object": "account"}'
