# -*- coding: utf-8 -*-


import json

from stripe._error import StripeError, CardError, APIConnectionError


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
