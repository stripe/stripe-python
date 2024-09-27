from __future__ import absolute_import, division, print_function

import json

import pytest

import stripe
from stripe import error
from tests.http_client_mock import HTTPClientMock


class TestV2Error(object):
    @pytest.fixture(scope="function")
    def stripe_client(self, http_client_mock):
        return stripe.StripeClient(
            api_key="keyinfo_test_123",
            http_client=http_client_mock.get_mock_http_client(),
        )

    def test_raises_v2_error(
        self,
        stripe_client: stripe.StripeClient,
        http_client_mock: HTTPClientMock,
    ):
        method = "get"
        path = "/v2/core/events/evt_123"

        error_response = {
            "error": {
                "type": "temporary_session_expired",
                "code": "session_bad",
                "message": "you messed up",
            }
        }
        http_client_mock.stub_request(
            method,
            path=path,
            rbody=json.dumps(error_response),
            rcode=400,
            rheaders={},
        )

        try:
            stripe_client.v2.core.events.retrieve("evt_123")
        except error.TemporarySessionExpiredError as e:
            assert e.code == "session_bad"
            assert e.error.code == "session_bad"
            assert e.error.message == "you messed up"
        else:
            assert False, "Should have raised a TemporarySessionExpiredError"

        http_client_mock.assert_requested(
            method,
            path=path,
            api_key="keyinfo_test_123",
        )

    @pytest.mark.skip("python doesn't have any errors with invalid params yet")
    def test_raises_v2_error_with_field(
        self,
        stripe_client: stripe.StripeClient,
        http_client_mock: HTTPClientMock,
    ):
        method = "post"
        path = "/v2/payment_methods/us_bank_accounts"

        error_response = {
            "error": {
                "type": "invalid_payment_method",
                "code": "invalid_us_bank_account",
                "message": "bank account is invalid",
                "invalid_param": "routing_number",
            }
        }
        http_client_mock.stub_request(
            method,
            path=path,
            rbody=json.dumps(error_response),
            rcode=400,
            rheaders={},
        )

        try:
            stripe_client.v2.payment_methods.us_bank_accounts.create(
                params={"account_number": "123", "routing_number": "456"}
            )
        except error.InvalidPaymentMethodError as e:
            assert e.invalid_param == "routing_number"
            assert e.error.code == "invalid_us_bank_account"
            assert e.error.message == "bank account is invalid"
        else:
            assert False, "Should have raised a InvalidUsBankAccountError"

        http_client_mock.assert_requested(
            method,
            path=path,
            api_key="keyinfo_test_123",
        )

    def test_falls_back_to_v1_error(
        self,
        stripe_client: stripe.StripeClient,
        http_client_mock: HTTPClientMock,
    ):
        method = "post"
        path = "/v2/billing/meter_events"

        error_response = {
            "error": {
                "code": "invalid_request",
                "message": "your request is invalid",
                "param": "invalid_param",
            }
        }
        http_client_mock.stub_request(
            method,
            path=path,
            rbody=json.dumps(error_response),
            rcode=400,
            rheaders={"request-id": "123"},
        )

        try:
            stripe_client.v2.billing.meter_events.create(
                {"event_name": "asdf", "payload": {}}
            )
        except error.InvalidRequestError as e:
            assert e.param == "invalid_param"
            assert repr(e) == (
                "InvalidRequestError(message='your request is invalid', "
                "param='invalid_param', code='invalid_request', "
                "http_status=400, request_id='123')"
            )
        else:
            assert False, "Should have raised a InvalidRequestError"

        http_client_mock.assert_requested(
            method,
            path=path,
            api_key="keyinfo_test_123",
        )
