from __future__ import absolute_import, division, print_function

import time

import pytest

import stripe
from stripe import six


DUMMY_WEBHOOK_PAYLOAD = """{
  "id": "evt_test_webhook",
  "object": "event"
}"""

DUMMY_WEBHOOK_SECRET = "whsec_test_secret"


def generate_header(**kwargs):
    timestamp = kwargs.get("timestamp", int(time.time()))
    payload = kwargs.get("payload", DUMMY_WEBHOOK_PAYLOAD)
    secret = kwargs.get("secret", DUMMY_WEBHOOK_SECRET)
    scheme = kwargs.get("scheme", stripe.WebhookSignature.EXPECTED_SCHEME)
    signature = kwargs.get("signature", None)
    if signature is None:
        payload_to_sign = "%d.%s" % (timestamp, payload)
        signature = stripe.WebhookSignature._compute_signature(
            payload_to_sign, secret
        )
    header = "t=%d,%s=%s" % (timestamp, scheme, signature)
    return header


class TestWebhook(object):
    def test_construct_event(self):
        header = generate_header()
        event = stripe.Webhook.construct_event(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_raise_on_json_error(self):
        payload = "this is not valid JSON"
        header = generate_header(payload=payload)
        with pytest.raises(ValueError):
            stripe.Webhook.construct_event(
                payload, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_invalid_header(self):
        header = "bad_header"
        with pytest.raises(stripe.error.SignatureVerificationError):
            stripe.Webhook.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_construct_event_from_bytearray(self):
        header = generate_header()
        payload = bytearray(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = stripe.Webhook.construct_event(
            payload, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_construct_event_from_bytes(self):
        # This test is only applicable to Python 3 as `bytes` is not a symbol
        # in Python 2.
        if six.PY2:
            return

        header = generate_header()
        payload = bytes(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = stripe.Webhook.construct_event(
            payload, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)


class TestWebhookSignature(object):
    def test_raise_on_malformed_header(self):
        header = "i'm not even a real signature header"
        with pytest.raises(
            stripe.error.SignatureVerificationError,
            match="Unable to extract timestamp and signatures from header",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_no_signatures_with_expected_scheme(self):
        header = generate_header(scheme="v0")
        with pytest.raises(
            stripe.error.SignatureVerificationError,
            match="No signatures found with expected scheme v1",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_no_valid_signatures_for_payload(self):
        header = generate_header(signature="bad_signature")
        with pytest.raises(
            stripe.error.SignatureVerificationError,
            match="No signatures found matching the expected signature for payload",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_timestamp_outside_tolerance(self):
        header = generate_header(timestamp=int(time.time()) - 15)
        with pytest.raises(
            stripe.error.SignatureVerificationError,
            match="Timestamp outside the tolerance zone",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD,
                header,
                DUMMY_WEBHOOK_SECRET,
                tolerance=10,
            )

    def test_valid_header_and_signature(self):
        header = generate_header()
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET, tolerance=10
        )

    def test_header_contains_valid_signature(self):
        header = generate_header() + ",v1=bad_signature"
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET, tolerance=10
        )

    def test_timestamp_off_but_no_tolerance(self):
        header = generate_header(timestamp=12345)
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )
