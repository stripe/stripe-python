import time

import pytest

import stripe
from stripe._error import SignatureVerificationError


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


def generate_header(**kwargs):
    return stripe.Webhook.generate_test_header_string(
        payload=kwargs.get("payload", DUMMY_WEBHOOK_PAYLOAD),
        secret=kwargs.get("secret", DUMMY_WEBHOOK_SECRET),
        timestamp=kwargs.get("timestamp"),
        scheme=kwargs.get("scheme"),
        signature=kwargs.get("signature"),
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
        assert "StripeClient.parse_event_notification" in str(e.value)


class TestWebhookSignature(object):
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
        header = generate_header(scheme="v0")
        with pytest.raises(
            SignatureVerificationError,
            match="No signatures found with expected scheme v1",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
            )

    def test_raise_on_no_valid_signatures_for_payload(self):
        header = generate_header(signature="bad_signature")
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

    def test_timestamp_off_but_no_tolerance(self):
        header = generate_header(timestamp=12345)
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
        )


class TestGenerateTestHeaderString(object):
    def test_uses_defaults_when_optional_args_omitted(self):
        before = int(time.time())
        header = stripe.Webhook.generate_test_header_string(
            payload=DUMMY_WEBHOOK_PAYLOAD, secret=DUMMY_WEBHOOK_SECRET
        )
        after = int(time.time())

        parts = dict(item.split("=", 1) for item in header.split(","))
        assert before <= int(parts["t"]) <= after
        assert "v1" in parts

    def test_header_verifies_round_trip(self):
        header = stripe.Webhook.generate_test_header_string(
            payload=DUMMY_WEBHOOK_PAYLOAD, secret=DUMMY_WEBHOOK_SECRET
        )
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD,
            header,
            DUMMY_WEBHOOK_SECRET,
            tolerance=10,
        )

    def test_honors_custom_timestamp_and_scheme(self):
        header = stripe.Webhook.generate_test_header_string(
            payload=DUMMY_WEBHOOK_PAYLOAD,
            secret=DUMMY_WEBHOOK_SECRET,
            timestamp=12345,
            scheme="v0",
        )
        assert header.startswith("t=12345,v0=")

    def test_uses_provided_signature_verbatim(self):
        header = stripe.Webhook.generate_test_header_string(
            payload=DUMMY_WEBHOOK_PAYLOAD,
            secret=DUMMY_WEBHOOK_SECRET,
            timestamp=12345,
            signature="deadbeef",
        )
        assert header == "t=12345,v1=deadbeef"

    def test_bad_secret_fails_verification(self):
        header = stripe.Webhook.generate_test_header_string(
            payload=DUMMY_WEBHOOK_PAYLOAD, secret="whsec_wrong"
        )
        with pytest.raises(SignatureVerificationError):
            stripe.WebhookSignature.verify_header(
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
