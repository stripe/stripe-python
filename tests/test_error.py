# -*- coding: utf-8 -*-


import json
import pickle

import pytest

from stripe._error import (
    APIConnectionError,
    APIError,
    AuthenticationError,
    CardError,
    IdempotencyError,
    InvalidRequestError,
    PermissionError,
    RateLimitError,
    SignatureVerificationError,
    StripeError,
    StripeErrorWithParamCode,
    TemporarySessionExpiredError,
)


def assert_error_round_trips(err):
    json_args = json.loads(json.dumps(err.args))
    round_tripped_errors = (
        pickle.loads(pickle.dumps(err)),
        type(err)(*json_args),
    )

    for round_tripped in round_tripped_errors:
        assert type(round_tripped) is type(err)
        assert round_tripped.args == err.args
        assert vars(round_tripped) == vars(err)


class TestStripeError(object):
    def test_formatting(self):
        err = StripeError("öre")
        assert str(err) == "öre"

    def test_formatting_with_request_id(self):
        err = StripeError("öre", headers={"request-id": "123"})
        assert str(err) == "Request 123: öre"

    def test_formatting_with_none(self):
        err = StripeError(None, headers={"request-id": "123"})
        assert str(err) == "Request 123: <empty message>"

    def test_formatting_with_message_none_and_request_id_none(self):
        err = StripeError(None)
        assert str(err) == "<empty message>"

    def test_repr(self):
        err = StripeError("öre", headers={"request-id": "123"})
        assert (
            repr(err) == "StripeError(message='öre', http_status=None, "
            "request_id='123')"
        )

    def test_error_string_body(self):
        http_body = '{"error": {"code": "some_error"}}'
        err = StripeError(
            "message", http_body=http_body, json_body=json.loads(http_body)
        )
        assert err.http_body is not None
        assert err.http_body == json.dumps(err.json_body)

    def test_error_bytes_body(self):
        http_body = '{"error": {"code": "some_error"}}'.encode("utf-8")
        err = StripeError(
            "message", http_body=http_body, json_body=json.loads(http_body)
        )
        assert err.http_body is not None
        assert err.http_body == json.dumps(err.json_body)

    def test_error_object(self):
        err = StripeError(
            "message", json_body={"error": {"code": "some_error"}}
        )
        assert err.error is not None
        assert err.error.code == "some_error"
        assert err.error.charge is None

    def test_error_object_network_advice_code(self):
        err = StripeError(
            "message",
            json_body={
                "error": {
                    "type": "card_error",
                    "network_advice_code": "02",
                }
            },
        )
        assert err.error is not None
        assert err.error.network_advice_code == "02"

    def test_error_object_payment_intent(self):
        err = StripeError(
            "message",
            json_body={
                "error": {
                    "type": "card_error",
                    "payment_intent": {
                        "id": "pi_123",
                        "object": "payment_intent",
                        "amount": 1000,
                    },
                }
            },
        )
        assert err.error is not None
        assert err.error.payment_intent is not None
        assert err.error.payment_intent.id == "pi_123"
        assert err.error.payment_intent.amount == 1000

    def test_error_object_not_dict(self):
        err = StripeError("message", json_body={"error": "not a dict"})
        assert err.error is None


class TestStripeErrorWithParamCode(object):
    def test_repr(self):
        err = CardError(
            "öre",
            param="cparam",
            code="ccode",
            http_status=403,
            headers={"request-id": "123"},
        )
        assert (
            repr(err)
            == "CardError(message='öre', param='cparam', code='ccode', "
            "http_status=403, request_id='123')"
        )


class TestApiConnectionError(object):
    def test_default_no_retry(self):
        err = APIConnectionError("msg")
        assert err.should_retry is False

        err = APIConnectionError("msg", should_retry=True)
        assert err.should_retry


@pytest.mark.parametrize(
    "error_class",
    [
        StripeError,
        APIError,
        AuthenticationError,
        IdempotencyError,
        PermissionError,
        RateLimitError,
        StripeErrorWithParamCode,
        TemporarySessionExpiredError,
    ],
)
def test_stripe_error_round_trips(error_class):
    err = error_class(
        message="message",
        http_body=b"body",
        http_status=400,
        json_body={"error": {"code": "error_code"}},
        headers={"request-id": "req_123"},
        code="error_code",
    )

    assert_error_round_trips(err)


@pytest.mark.parametrize(
    "err",
    [
        APIConnectionError(
            "message",
            b"body",
            400,
            {"error": {"code": "error_code"}},
            {"request-id": "req_123"},
            "error_code",
            True,
        ),
        CardError(
            "message",
            "param",
            "error_code",
            b"body",
            402,
            {"error": {"code": "error_code"}},
            {"request-id": "req_123"},
        ),
        InvalidRequestError(
            message="message",
            param="param",
            code="error_code",
            http_body=b"body",
            http_status=400,
            json_body={"error": {"code": "error_code"}},
            headers={"request-id": "req_123"},
        ),
        SignatureVerificationError("message", "signature", b"body"),
    ],
)
def test_stripe_error_with_custom_constructor_round_trips(err):
    assert_error_round_trips(err)
