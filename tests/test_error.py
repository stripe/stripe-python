# -*- coding: utf-8 -*-


import json
from stripe import error


class TestStripeError(object):
    def test_formatting(self):
        err = error.StripeError("öre")
        assert str(err) == "öre"

    def test_formatting_with_request_id(self):
        err = error.StripeError("öre", headers={"request-id": "123"})
        assert str(err) == "Request 123: öre"

    def test_formatting_with_none(self):
        err = error.StripeError(None, headers={"request-id": "123"})
        assert str(err) == "Request 123: <empty message>"

    def test_formatting_with_message_none_and_request_id_none(self):
        err = error.StripeError(None)
        assert str(err) == "<empty message>"

    def test_repr(self):
        err = error.StripeError("öre", headers={"request-id": "123"})
        assert (
            repr(err) == "StripeError(message='öre', http_status=None, "
            "request_id='123')"
        )

    def test_error_string_body(self):
        http_body = '{"error": {"code": "some_error"}}'
        err = error.StripeError(
            "message", http_body=http_body, json_body=json.loads(http_body)
        )
        assert err.http_body is not None
        assert err.http_body == json.dumps(err.json_body)

    def test_error_bytes_body(self):
        http_body = '{"error": {"code": "some_error"}}'.encode("utf-8")
        err = error.StripeError(
            "message", http_body=http_body, json_body=json.loads(http_body)
        )
        assert err.http_body is not None
        assert err.http_body == json.dumps(err.json_body)

    def test_error_object(self):
        err = error.StripeError(
            "message", json_body={"error": {"code": "some_error"}}
        )
        assert err.error is not None
        assert err.error.code == "some_error"
        assert err.error.charge is None

    def test_error_object_not_dict(self):
        err = error.StripeError("message", json_body={"error": "not a dict"})
        assert err.error is None


class TestStripeErrorWithParamCode(object):
    def test_repr(self):
        err = error.CardError(
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
        err = error.APIConnectionError("msg")
        assert err.should_retry is False

        err = error.APIConnectionError("msg", should_retry=True)
        assert err.should_retry
