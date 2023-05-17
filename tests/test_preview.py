from __future__ import absolute_import, division, print_function

import pytest
import stripe
from stripe.api_version import _ApiVersion


class TestPreview(object):
    def set_body(self, body):
        self.mock_request.return_value = (body, 200, {})

    @pytest.fixture(autouse=True)
    def setup_stripe(self, mocker):
        orig_attrs = {
            "api_key": stripe.api_key,
            "default_http_client": stripe.default_http_client,
        }
        hc = mocker.Mock(stripe.default_http_client)
        hc.name = "mockclient"
        self.mock_request = mocker.Mock()
        hc.request_with_retries = self.mock_request
        stripe.default_http_client = hc
        stripe.api_key = "sk_test_123"
        yield
        stripe.default_http_client = orig_attrs["default_http_client"]
        stripe.api_key = orig_attrs["api_key"]

    def test_get(self, request_mock):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)
        resp = stripe.preview.get("/v2/accounts/acc_123")

        req = self.mock_request.mock_calls[0]
        method, abs_url, headers = req.args

        assert method == "get"
        assert "Content-Type" not in headers
        assert headers["Stripe-Version"] == _ApiVersion.PREVIEW
        assert headers["Stripe-Version"] == _ApiVersion.PREVIEW
        assert resp.body == expected_body

    def test_post(self, request_mock):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = stripe.preview.post("/v2/accounts", p1=1, p2="string")

        req = self.mock_request.mock_calls[0]
        method, abs_url, headers, post_data = req.args

        assert method == "post"
        assert headers["Content-Type"] == "application/json"
        assert headers["Stripe-Version"] == _ApiVersion.PREVIEW
        assert resp.body == expected_body

    def test_delete(self, request_mock):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = stripe.preview.delete("/v2/accounts/acc_123")

        req = self.mock_request.mock_calls[0]
        method, abs_url, headers = req.args

        assert method == "delete"
        assert "Content-Type" not in headers
        assert headers["Stripe-Version"] == _ApiVersion.PREVIEW
        assert resp.body == expected_body

    def test_override_default_options(self, request_mock):
        expected_body = '{"id": "acc_123"}'
        stripe_version_override = "2022-11-15"
        stripe_context = "acct_x"
        self.set_body(expected_body)

        resp = stripe.preview.post(
            "/v2/accounts",
            stripe_version=stripe_version_override,
            stripe_context=stripe_context,
        )

        req = self.mock_request.mock_calls[0]
        method, abs_url, headers, post_data = req.args

        assert method == "post"
        assert headers["Content-Type"] == "application/json"
        assert headers["Stripe-Version"] == stripe_version_override
        assert headers["Stripe-Context"] == stripe_context
        assert resp.body == expected_body
