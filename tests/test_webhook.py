import time

import pytest

import stripe
from stripe._error import SignatureVerificationError
from stripe._webhook import WebhookSignature


DUMMY_WEBHOOK_PAYLOAD = """{
  "id": "evt_test_webhook",
  "object": "event",
  "data": { "object": { "id": "rdr_123", "object": "terminal.reader" } }
}"""

DUMMY_V2_WEBHOOK_PAYLOAD = """{
  "id": "evt_234",
  "object": "v2.core.event",
  "type": "v1.billing.meter.error_report_triggered",
  "livemode": true,
  "created": "2022-02-15T00:27:45.330Z"
}"""

DUMMY_WEBHOOK_SECRET = "whsec_test_secret"


def generate_header(
    payload=DUMMY_WEBHOOK_PAYLOAD, secret=DUMMY_WEBHOOK_SECRET, timestamp=None
):
    """Thin wrapper around WebhookSignature.generate_signature_header for tests."""
    return WebhookSignature.generate_signature_header(
        payload, secret, timestamp
    )


def _build_header_with_scheme(
    scheme,
    payload=DUMMY_WEBHOOK_PAYLOAD,
    secret=DUMMY_WEBHOOK_SECRET,
    timestamp=None,
):
    """Build a header with a custom scheme, for testing scheme-mismatch error paths."""
    if timestamp is None:
        timestamp = int(time.time())
    payload_to_sign = "%d.%s" % (timestamp, payload)
    signature = WebhookSignature._compute_signature(payload_to_sign, secret)
    return "t=%d,%s=%s" % (timestamp, scheme, signature)


def _build_header_with_signature(
    signature, payload=DUMMY_WEBHOOK_PAYLOAD, timestamp=None
):
    """Build a header with a pre-computed (possibly bad) signature, for testing signature-mismatch error paths."""
    if timestamp is None:
        timestamp = int(time.time())
    return "t=%d,%s=%s" % (
        timestamp,
        WebhookSignature.EXPECTED_SCHEME,
        signature,
    )


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
        with pytest.raises(SignatureVerificationError):
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
        header = generate_header()
        payload = bytes(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = stripe.Webhook.construct_event(
            payload, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_raise_on_v2_payload(self):
        header = generate_header(payload=DUMMY_V2_WEBHOOK_PAYLOAD)
        with pytest.raises(ValueError) as e:
            stripe.Webhook.construct_event(
                DUMMY_V2_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )
        assert "parse_event_notification" in str(e.value)


class TestWebhookSignature(object):
    @pytest.mark.parametrize("header", [None, ""])
    def test_raise_on_missing_header(self, header):
        with pytest.raises(
            SignatureVerificationError,
            match="No Stripe-Signature header value was provided",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    @pytest.mark.parametrize(
        "encode",
        [lambda p: p.encode("utf-8"), lambda p: bytearray(p, "utf-8")],
        ids=["bytes", "bytearray"],
    )
    def test_verifies_binary_payload(self, encode):
        header = generate_header()
        assert stripe.WebhookSignature.verify_header(
            encode(DUMMY_WEBHOOK_PAYLOAD), header, DUMMY_WEBHOOK_SECRET
        )

    def test_raise_on_malformed_header(self):
        header = "i'm not even a real signature header"
        with pytest.raises(
            SignatureVerificationError,
            match="Unable to extract timestamp and signatures from header",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_no_signatures_with_expected_scheme(self):
        header = _build_header_with_scheme("v0")
        with pytest.raises(
            SignatureVerificationError,
            match="No signatures found with expected scheme v1",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_no_valid_signatures_for_payload(self):
        header = _build_header_with_signature("bad_signature")
        with pytest.raises(
            SignatureVerificationError,
            match="No signatures found matching the expected signature for payload",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_timestamp_outside_tolerance(self):
        header = generate_header(timestamp=int(time.time()) - 15)
        with pytest.raises(
            SignatureVerificationError,
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

    def test_generate_signature_header(self):
        timestamp = 1234567890
        header = WebhookSignature.generate_signature_header(
            DUMMY_WEBHOOK_PAYLOAD, DUMMY_WEBHOOK_SECRET, timestamp
        )
        # Header must follow the format t=<timestamp>,v1=<hex_signature>
        assert header.startswith("t=%d,v1=" % timestamp)
        parts = dict(part.split("=", 1) for part in header.split(","))
        assert parts["t"] == str(timestamp)
        assert len(parts["v1"]) == 64  # SHA-256 hex digest is 64 chars
        # The generated header must pass verification (no tolerance since timestamp is old)
        assert WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )

    def test_timestamp_off_but_no_tolerance(self):
        header = generate_header(timestamp=12345)
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )


class TestStripeClientConstructEvent(object):
    def test_construct_event(self, stripe_mock_stripe_client):
        header = generate_header()
        event = stripe_mock_stripe_client.construct_event(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_raise_on_json_error(self, stripe_mock_stripe_client):
        payload = "this is not valid JSON"
        header = generate_header(payload=payload)
        with pytest.raises(ValueError):
            stripe_mock_stripe_client.construct_event(
                payload, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_invalid_header(self, stripe_mock_stripe_client):
        header = "bad_header"
        with pytest.raises(SignatureVerificationError):
            stripe_mock_stripe_client.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_construct_event_from_bytearray(self, stripe_mock_stripe_client):
        header = generate_header()
        payload = bytearray(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = stripe_mock_stripe_client.construct_event(
            payload, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_construct_event_from_bytes(self, stripe_mock_stripe_client):
        header = generate_header()
        payload = bytes(DUMMY_WEBHOOK_PAYLOAD, "utf-8")
        event = stripe_mock_stripe_client.construct_event(
            payload, header, DUMMY_WEBHOOK_SECRET
        )
        assert isinstance(event, stripe.Event)

    def test_raise_on_v2_payload(self, stripe_mock_stripe_client):
        header = generate_header(payload=DUMMY_V2_WEBHOOK_PAYLOAD)
        with pytest.raises(ValueError) as e:
            stripe_mock_stripe_client.construct_event(
                DUMMY_V2_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )
        assert "parse_event_notification" in str(e.value)

    def test_construct_event_inherits_requestor(self, http_client_mock):
        http_client_mock.stub_request("delete", "/v1/terminal/readers/rdr_123")

        client = stripe.StripeClient(
            "sk_test_777",
            stripe_account="acct_777",
            stripe_version="2222-22-22",
            http_client=http_client_mock.get_mock_http_client(),
        )
        header = generate_header()
        event = client.construct_event(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )
        assert event._requestor == client._requestor

        assert isinstance(event.data.object, stripe.terminal.Reader)
        event.data.object.delete()

        http_client_mock.assert_requested(
            "delete",
            path="/v1/terminal/readers/rdr_123",
            api_key="sk_test_777",
            stripe_account="acct_777",
            stripe_version="2222-22-22",
        )
