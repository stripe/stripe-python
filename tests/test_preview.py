from __future__ import absolute_import, division, print_function

import pytest
import stripe
from stripe._api_version import _ApiVersion
from tests.test_api_requestor import APIHeaderMatcher
from mock import AsyncMock


class TestPreview(object):
    def set_body(self, body):
        self.mock_request.return_value = (body, 200, {})
        self.mock_request_async.return_value = (body, 200, {})

    @pytest.fixture(autouse=True)
    def setup_stripe(self, mocker):
        orig_attrs = {
            "api_key": stripe.api_key,
            "default_http_client": stripe.default_http_client,
            "default_http_client_async": stripe.default_http_client_async,
        }
        hc = mocker.Mock(stripe.default_http_client)
        hc_async = mocker.Mock(stripe.default_http_client_async)
        hc.name = "mockclient"
        self.mock_request = mocker.Mock()
        self.mock_request_async = AsyncMock()
        hc.request_with_retries = self.mock_request
        hc_async.request_with_retries_async = self.mock_request_async
        stripe.default_http_client = hc
        stripe.default_http_client_async = hc_async
        stripe.api_key = "sk_test_123"
        yield
        stripe.default_http_client = orig_attrs["default_http_client"]
        stripe.default_http_client_async = orig_attrs[
            "default_http_client_async"
        ]
        stripe.api_key = orig_attrs["api_key"]

    def test_get(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = stripe.preview.get("/v1/accounts/acc_123")

        self.mock_request.assert_called_with(
            "get",
            "%s/v1/accounts/acc_123" % stripe.api_base,
            APIHeaderMatcher(
                request_method="get",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            None,
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    def test_post(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = stripe.preview.post("/v1/accounts", arg="string")

        self.mock_request.assert_called_with(
            "post",
            "%s/v1/accounts" % stripe.api_base,
            APIHeaderMatcher(
                request_method="post",
                content_type="application/json",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            '{"arg": "string"}',
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    def test_delete(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = stripe.preview.delete("/v1/accounts/acc_123")

        self.mock_request.assert_called_with(
            "delete",
            "%s/v1/accounts/acc_123" % stripe.api_base,
            APIHeaderMatcher(
                request_method="delete",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            None,
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    @pytest.mark.asyncio
    async def test_get_async(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = await stripe.preview.get_async("/v1/accounts/acc_123")

        self.mock_request_async.assert_called_with(
            "get",
            "%s/v1/accounts/acc_123" % stripe.api_base,
            APIHeaderMatcher(
                request_method="get",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            None,
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    @pytest.mark.asyncio
    async def test_post_async(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = await stripe.preview.post_async("/v1/accounts", arg="string")

        self.mock_request_async.assert_called_with(
            "post",
            "%s/v1/accounts" % stripe.api_base,
            APIHeaderMatcher(
                request_method="post",
                content_type="application/json",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            '{"arg": "string"}',
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    @pytest.mark.asyncio
    async def test_delete_async(self):
        expected_body = '{"id": "acc_123"}'
        self.set_body(expected_body)

        resp = await stripe.preview.delete_async("/v1/accounts/acc_123")

        self.mock_request_async.assert_called_with(
            "delete",
            "%s/v1/accounts/acc_123" % stripe.api_base,
            APIHeaderMatcher(
                request_method="delete",
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
            ),
            None,
            _usage=["raw_request"],
        )

        assert resp.body == expected_body

    def test_override_default_options(self):
        expected_body = '{"id": "acc_123"}'
        stripe_version_override = "2022-11-15"
        stripe_context = "acct_x"
        self.set_body(expected_body)

        resp = stripe.preview.post(
            "/v1/accounts",
            stripe_version=stripe_version_override,
            stripe_context=stripe_context,
        )

        self.mock_request.assert_called_with(
            "post",
            "%s/v1/accounts" % stripe.api_base,
            APIHeaderMatcher(
                request_method="post",
                content_type="application/json",
                extra={
                    "Stripe-Context": stripe_context,
                    "Stripe-Version": stripe_version_override,
                },
            ),
            "{}",
            _usage=["raw_request"],
        )

        assert resp.body == expected_body
