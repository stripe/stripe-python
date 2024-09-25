from __future__ import absolute_import, division, print_function

import datetime

import stripe

from tests.test_api_requestor import GMT1


class TestRawRequest(object):
    ENCODE_INPUTS = {
        "type": "standard",
        "int": 123,
        "datetime": datetime.datetime(2013, 1, 1, second=1, tzinfo=GMT1()),
    }
    POST_REL_URL = "/v1/accounts"
    GET_REL_URL = "/v1/accounts/acct_123"
    POST_REL_URL_V2 = "/v2/billing/meter_event_session"
    GET_REL_URL_V2 = "/v2/accounts/acct_123"

    def test_form_request_get(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.GET_REL_URL,
            rbody='{"id": "acct_123", "object": "account"}',
            rcode=200,
            rheaders={},
        )

        resp = stripe.raw_request("get", self.GET_REL_URL)
        http_client_mock.assert_requested("get", path=self.GET_REL_URL)

        deserialized = stripe.deserialize(resp, api_mode="V1")
        assert isinstance(deserialized, stripe.Account)

    def test_form_request_post(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path=self.POST_REL_URL,
            rbody='{"id": "acct_123", "object": "account"}',
            rcode=200,
            rheaders={},
        )

        expectation = "type=standard&int=123&datetime=1356994801"

        resp = stripe.raw_request(
            "post", self.POST_REL_URL, **self.ENCODE_INPUTS
        )

        http_client_mock.assert_requested(
            "post",
            path=self.POST_REL_URL,
            content_type="application/x-www-form-urlencoded",
            post_data=expectation,
        )

        deserialized = stripe.deserialize(resp, api_mode="V1")
        assert isinstance(deserialized, stripe.Account)

    def test_preview_request_post(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path=self.POST_REL_URL_V2,
            rbody='{"id": "bmes_123", "object": "billing.meter_event_session"}',
            rcode=200,
            rheaders={},
        )

        params = dict({}, **self.ENCODE_INPUTS)
        expectation = (
            '{"type": "standard", "int": 123, "datetime": 1356994801}'
        )

        resp = stripe.raw_request("post", self.POST_REL_URL_V2, **params)

        http_client_mock.assert_requested(
            "post",
            path=self.POST_REL_URL_V2,
            content_type="application/json",
            post_data=expectation,
            is_json=True,
        )

        deserialized = stripe.deserialize(resp, api_mode="V2")
        assert isinstance(deserialized, stripe.v2.billing.MeterEventSession)

    def test_form_request_with_extra_headers(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.GET_REL_URL,
            rbody='{"id": "acct_123", "object": "account"}',
            rcode=200,
            rheaders={},
        )

        extra_headers = {"foo": "bar", "Stripe-Account": "acct_123"}
        params = {"headers": extra_headers}

        stripe.raw_request("get", self.GET_REL_URL, **params)

        http_client_mock.assert_requested(
            "get",
            path=self.GET_REL_URL,
            extra_headers=extra_headers,
        )

    def test_preview_request_default_api_version(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path=self.GET_REL_URL_V2,
            rbody='{"id": "acct_123", "object": "account"}',
            rcode=200,
            rheaders={},
        )
        params = {}

        stripe.raw_request("get", self.GET_REL_URL_V2, **params)

        http_client_mock.assert_requested(
            "get",
            path=self.GET_REL_URL_V2,
            stripe_version=stripe.preview_api_version,
        )

    def test_preview_request_overridden_api_version(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path=self.POST_REL_URL_V2,
            rbody='{"id": "acct_123", "object": "account"}',
            rcode=200,
            rheaders={},
        )
        stripe_version_override = "2023-05-15.preview"
        params = {
            "stripe_version": stripe_version_override,
        }

        stripe.raw_request("post", self.POST_REL_URL_V2, **params)

        http_client_mock.assert_requested(
            "post",
            path=self.POST_REL_URL_V2,
            content_type="application/json",
            stripe_version=stripe_version_override,
            post_data="{}",
            is_json=True,
        )
