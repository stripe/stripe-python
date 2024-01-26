from __future__ import absolute_import, division, print_function

import pytest
import stripe
from stripe._api_version import _ApiVersion


class TestPreview(object):
    def test_get(self, http_client_mock):
        expected_body = '{"id": "acc_123"}'
        http_client_mock.stub_request(
            "get",
            path="/v1/accounts/acc_123",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = stripe.preview.get("/v1/accounts/acc_123")

        http_client_mock.assert_requested(
            "get",
            api_base=stripe.api_base,
            path="/v1/accounts/acc_123",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
        )

        assert resp.body == expected_body

    def test_post(self, http_client_mock):
        expected_body = '{"id": "acc_123"}'
        http_client_mock.stub_request(
            "post",
            path="/v1/accounts",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = stripe.preview.post("/v1/accounts", arg="string")

        http_client_mock.assert_requested(
            "post",
            api_base=stripe.api_base,
            path="/v1/accounts",
            content_type="application/json",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
            post_data='{"arg": "string"}',
            is_json=True,
        )

        assert resp.body == expected_body

    def test_delete(self, http_client_mock):
        expected_body = '{"id": "acc_123"}'
        http_client_mock.stub_request(
            "delete",
            path="/v1/accounts/acc_123",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = stripe.preview.delete("/v1/accounts/acc_123")

        http_client_mock.assert_requested(
            "delete",
            api_base=stripe.api_base,
            path="/v1/accounts/acc_123",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
        )

        assert resp.body == expected_body

    @pytest.mark.anyio
    async def test_get_async(self, http_client_mock_async):
        expected_body = '{"id": "acc_123"}'
        http_client_mock_async.stub_request(
            "get",
            path="/v1/accounts/acc_123",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = await stripe.preview.get_async("/v1/accounts/acc_123")

        http_client_mock_async.assert_requested(
            "get",
            api_base=stripe.api_base,
            path="/v1/accounts/acc_123",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
        )

        assert resp.body == expected_body

    @pytest.mark.anyio
    async def test_post_async(self, http_client_mock_async):
        expected_body = '{"id": "acc_123"}'
        http_client_mock_async.stub_request(
            "post",
            path="/v1/accounts",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = await stripe.preview.post_async("/v1/accounts", arg="string")

        http_client_mock_async.assert_requested(
            "post",
            api_base=stripe.api_base,
            path="/v1/accounts",
            content_type="application/json",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
            post_data='{"arg": "string"}',
            is_json=True,
        )

        assert resp.body == expected_body

    @pytest.mark.anyio
    async def test_delete_async(self, http_client_mock_async):
        expected_body = '{"id": "acc_123"}'
        http_client_mock_async.stub_request(
            "delete",
            path="/v1/accounts/acc_123",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = await stripe.preview.delete_async("/v1/accounts/acc_123")

        http_client_mock_async.assert_requested(
            "delete",
            api_base=stripe.api_base,
            path="/v1/accounts/acc_123",
            stripe_version=_ApiVersion.PREVIEW,
            usage=["raw_request"],
        )

        assert resp.body == expected_body

    def test_override_default_options(self, http_client_mock):
        expected_body = '{"id": "acc_123"}'
        stripe_version_override = "2022-11-15"
        stripe_context = "acct_x"

        http_client_mock.stub_request(
            "post",
            path="/v1/accounts",
            rbody=expected_body,
            rcode=200,
            rheaders={},
        )

        resp = stripe.preview.post(
            "/v1/accounts",
            stripe_version=stripe_version_override,
            stripe_context=stripe_context,
        )

        http_client_mock.assert_requested(
            "post",
            api_base=stripe.api_base,
            path="/v1/accounts",
            content_type="application/json",
            stripe_version=stripe_version_override,
            stripe_context=stripe_context,
            usage=["raw_request"],
            post_data="{}",
            is_json=True,
        )

        assert resp.body == expected_body
