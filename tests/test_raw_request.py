from __future__ import absolute_import, division, print_function

import json
import datetime
from collections import OrderedDict

import pytest

import stripe
from stripe.api_version import _ApiVersion

from tests.test_api_requestor import APIHeaderMatcher
from tests.test_api_requestor import GMT1


class TestRawRequest(object):
    ENCODE_INPUTS = {
        "type": "standard",
        "int": 123,
        "datetime": datetime.datetime(2013, 1, 1, second=1, tzinfo=GMT1()),
    }
    POST_REL_URL = "/v1/accounts"
    GET_REL_URL = "/v1/accounts/acct_123"
    POST_ABS_URL = stripe.api_base + POST_REL_URL
    GET_ABS_URL = stripe.api_base + GET_REL_URL

    @pytest.fixture(autouse=True)
    def setup_stripe(self, http_client):
        orig_attrs = {
            "api_key": stripe.api_key,
            "api_version": stripe.api_version,
            "default_http_client": stripe.default_http_client,
        }
        stripe.api_key = "sk_test_123"
        stripe.api_version = "2017-12-14"
        stripe.default_http_client = http_client
        yield
        stripe.api_key = orig_attrs["api_key"]
        stripe.api_version = orig_attrs["api_version"]
        stripe.default_http_client = orig_attrs["default_http_client"]

    def test_form_request_get(self, http_client, mock_response, check_call):
        mock_response('{"id": "acct_123", "object": "account"}', 200)

        params = {}

        resp = stripe.raw_request("get", self.GET_REL_URL, **params)

        check_call("get", abs_url=self.GET_ABS_URL)

        deserialized = stripe.deserialize(resp)
        assert isinstance(deserialized, stripe.Account)

    def test_form_request_post(self, http_client, mock_response, check_call):
        mock_response('{"id": "acct_123", "object": "account"}', 200)

        params = OrderedDict({"client": http_client}, **self.ENCODE_INPUTS)
        expectation = "type=standard&int=123&datetime=1356994801"

        resp = stripe.raw_request("post", self.POST_REL_URL, **params)

        check_call(
            "post",
            abs_url=self.POST_ABS_URL,
            headers=APIHeaderMatcher(
                content_type="application/x-www-form-urlencoded",
                request_method="post",
            ),
            post_data=expectation,
        )

        deserialized = stripe.deserialize(resp)
        assert isinstance(deserialized, stripe.Account)

    def test_preview_request_post(
        self, http_client, mock_response, check_call
    ):
        mock_response('{"id": "acct_123", "object": "account"}', 200)

        params = OrderedDict(
            {"client": http_client, "api_mode": "preview"},
            **self.ENCODE_INPUTS
        )
        expectation = (
            '{"type": "standard", "int": 123, "datetime": 1356994801}'
        )

        resp = stripe.raw_request("post", self.POST_REL_URL, **params)

        check_call(
            "post",
            abs_url=self.POST_ABS_URL,
            headers=APIHeaderMatcher(
                content_type="application/json",
                request_method="post",
            ),
            post_data=expectation,
        )

        deserialized = stripe.deserialize(resp)
        assert isinstance(deserialized, stripe.Account)

    def test_form_request_with_extra_headers(
        self, http_client, mock_response, check_call
    ):
        mock_response('{"id": "acct_123", "object": "account"}', 200)

        extraHeaders = {"foo": "bar", "Stripe-Account": "acct_123"}
        params = {"client": http_client, "headers": extraHeaders}

        stripe.raw_request("get", self.GET_REL_URL, **params)

        check_call(
            "get",
            abs_url=self.GET_ABS_URL,
            headers=APIHeaderMatcher(extra=extraHeaders, request_method="get"),
        )

    def test_preview_request_default_api_version(
        self, http_client, mock_response, check_call
    ):
        mock_response('{"id": "acct_123", "object": "account"}', 200)
        params = {"client": http_client, "api_mode": "preview"}

        stripe.raw_request("get", self.GET_REL_URL, **params)

        check_call(
            "get",
            abs_url=self.GET_ABS_URL,
            headers=APIHeaderMatcher(
                extra={"Stripe-Version": _ApiVersion.PREVIEW},
                request_method="get",
            ),
        )

    def test_preview_request_overridden_api_version(
        self, http_client, mock_response, check_call
    ):
        mock_response('{"id": "acct_123", "object": "account"}', 200)
        stripe_version_override = "2023-05-15.preview"
        params = {
            "client": http_client,
            "api_mode": "preview",
            "stripe_version": stripe_version_override,
        }

        stripe.raw_request("post", self.POST_REL_URL, **params)

        check_call(
            "post",
            abs_url=self.POST_ABS_URL,
            headers=APIHeaderMatcher(
                extra={"Stripe-Version": stripe_version_override},
                content_type="application/json",
                request_method="post",
            ),
            post_data=json.dumps({}),
        )
