import time
from hashlib import sha256

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

ASCII_WHITESPACE_WEBHOOK_SECRETS = [
    pytest.param(" ", id="space"),
    pytest.param("\t", id="tab"),
    pytest.param("\r", id="carriage-return"),
    pytest.param("\n", id="line-feed"),
    pytest.param("\f", id="form-feed"),
    pytest.param("\v", id="vertical-tab"),
    pytest.param(" \t\r\n\f\v", id="mixed"),
]


def generate_header(
    payload=DUMMY_WEBHOOK_PAYLOAD,
    secret=DUMMY_WEBHOOK_SECRET,
    timestamp=None,
    debug_metadata=None,
):
    """Thin wrapper around WebhookSignature.generate_signature_header for tests."""
    header = WebhookSignature.generate_signature_header(
        payload, secret, timestamp
    )
    for key, value in (debug_metadata or {}).items():
        if value is not None:
            header += f",{key}={value}"
    return header


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

    @pytest.mark.parametrize("secret", [None, ""])
    def test_raise_on_missing_secret(self, secret):
        header = generate_header()
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe.Webhook.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
            )

    @pytest.mark.parametrize("secret", ASCII_WHITESPACE_WEBHOOK_SECRETS)
    def test_raise_on_ascii_whitespace_secret(self, secret):
        header = generate_header(secret=secret)
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe.Webhook.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
            )

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

    @pytest.mark.parametrize("secret", [None, ""])
    def test_raise_on_missing_secret(self, secret):
        header = generate_header()
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
            )

    @pytest.mark.parametrize("secret", ASCII_WHITESPACE_WEBHOOK_SECRETS)
    def test_raise_on_ascii_whitespace_secret(self, secret):
        header = generate_header(secret=secret)
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
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

    def test_diagnose_secret_mismatch(self):
        dashboard_url_base = "https://dashboard.stripe.com/webhooks"
        cases = [
            # Secret and masket secret don't match; show URL with endpoint
            {
                "masked_secret": "whsec_******************1q84",
                "destination": "we_example",
                "url": dashboard_url_base + "/we_example",
            },
            # Missing and blank destinations use the bare Dashboard URL
            {
                "masked_secret": "whsec_******************1q84",
                "destination": "",
                "url": dashboard_url_base,
            },
            # Length mismatch
            {"masked_secret": "whsec_******************cret"},
            # An attacker-selected mask must not expose more than the last four characters
            {"masked_secret": "whsec_*bcdefghijklmnopqrstuvwxyZ"},
        ]
        for case in cases:
            secret = case.get("secret", DUMMY_WEBHOOK_SECRET)
            secret_suffix = case.get("secret_suffix", secret[-4:])
            masked_secret = case.get("masked_secret", "whsec_*******cret")
            url = case.get("url", dashboard_url_base)
            header = generate_header(
                secret="whsec_other_secret",
                debug_metadata={
                    "secret": masked_secret,
                    "destination": case.get("destination"),
                    "payload": "00000000",
                },
            )
            with pytest.raises(SignatureVerificationError) as error:
                WebhookSignature.verify_header(
                    DUMMY_WEBHOOK_PAYLOAD, header, secret
                )
            assert str(error.value) == (
                "Webhook signature verification failed. This request may not have originated from Stripe.\n\n"
                f"The signing secret you provided is {len(secret)} characters long and ends in `{secret_suffix}`. "
                f"However, the signing secret for this destination is {len(masked_secret)} characters long "
                f"and looks like `{masked_secret}`. Ensure you're using the signing secret for this "
                f"destination, as shown on the Dashboard: {url}\n\n"
                "Learn more: https://docs.stripe.com/webhooks/signature"
            )

    def test_diagnose_payload_mismatch(self):
        # User supplies the original body with an extra trailing space.
        payload = DUMMY_WEBHOOK_PAYLOAD + " "
        expected_hash = sha256(
            DUMMY_WEBHOOK_PAYLOAD.encode("utf-8")
        ).hexdigest()[-8:]
        actual_hash = sha256(payload.encode("utf-8")).hexdigest()[-8:]
        header = generate_header(
            debug_metadata={
                "secret": "whsec_*******cret",
                "payload": expected_hash.upper(),
            }
        )
        with pytest.raises(SignatureVerificationError) as error:
            WebhookSignature.verify_header(
                payload, header, DUMMY_WEBHOOK_SECRET
            )
        assert str(error.value) == (
            "Webhook signature verification failed.\n\n"
            "The request body you passed to this function differs from the request body sent by Stripe to this webhook destination.\n"
            f"The SHA-256 hash of the body should end in `{expected_hash}`. However, the SHA-256 hash of the body you provided ends in `{actual_hash}`.\n\n"
            "Make sure your code does not reformat or otherwise alter the raw HTTP request body before passing it to this function.\n\n"
            "Learn more: https://docs.stripe.com/webhooks/signature"
        )

    def test_matching_metadata_falls_back_to_generic_error(self):
        for masked_secret, secret in [
            ("whsec_*******cret", DUMMY_WEBHOOK_SECRET),
            # Prefixes and mask widths do not change the fixed four-character comparison.
            ("other_*******cret", DUMMY_WEBHOOK_SECRET),
            (
                "whsec_*bcdefghijklmnopqrstuvwxyz",
                "whsec_abcdefghijklmnopqrstuvwxyz",
            ),
            ("*", "*"),
        ]:
            header = generate_header(
                secret="whsec_other_secret",
                debug_metadata={"secret": masked_secret},
            )
            with pytest.raises(SignatureVerificationError) as error:
                WebhookSignature.verify_header(
                    DUMMY_WEBHOOK_PAYLOAD, header, secret
                )
            assert (
                str(error.value)
                == "No signatures found matching the expected signature for payload"
            )

    def test_invalid_secret_metadata_falls_back_to_generic_error(self):
        payload_hash = sha256(
            DUMMY_WEBHOOK_PAYLOAD.encode("utf-8")
        ).hexdigest()[-8:]
        for masked_secret in [
            "unmasked",
            "*" * 101,
            "*\ud800",
            # A blank first secret must not be replaced by a later value.
            ",secret=whsec_*******abcd",
        ]:
            header = generate_header(
                secret="whsec_other_secret",
                debug_metadata={
                    "secret": masked_secret,
                    "payload": payload_hash,
                },
            )
            with pytest.raises(SignatureVerificationError) as error:
                WebhookSignature.verify_header(
                    DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
                )
            assert (
                str(error.value)
                == "No signatures found matching the expected signature for payload"
            )

    def test_invalid_payload_metadata_falls_back_to_generic_error(self):
        for payload_hash in [
            "1234567",
            "123456789",
            "not-hex!",
            "a" * 101,
            "1234567\ud800",
            # A blank first hash must not be replaced by a later value.
            ",payload=00000000",
        ]:
            header = generate_header(
                secret="whsec_other_secret",
                debug_metadata={
                    "secret": "whsec_*******cret",
                    "payload": payload_hash,
                },
            )
            with pytest.raises(SignatureVerificationError) as error:
                WebhookSignature.verify_header(
                    DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET
                )
            assert (
                str(error.value)
                == "No signatures found matching the expected signature for payload"
            )

    def test_valid_signature_ignores_conflicting_metadata(self):
        header = generate_header(
            debug_metadata={
                "secret": "*abcd",
                "destination": "clidev_example",
                "payload": "00000000",
            }
        )
        assert WebhookSignature.verify_header(
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

    @pytest.mark.parametrize(
        "secret",
        [" \twhsec_test_secret\r\n", "\u00a0"],
        ids=["surrounding-whitespace", "non-ascii-whitespace"],
    )
    def test_preserves_nonblank_secret(self, secret):
        header = generate_header(secret=secret)
        assert stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, secret
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

    @pytest.mark.parametrize("secret", [None, ""])
    def test_raise_on_missing_secret(self, stripe_mock_stripe_client, secret):
        header = generate_header()
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe_mock_stripe_client.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
            )

    @pytest.mark.parametrize("secret", ASCII_WHITESPACE_WEBHOOK_SECRETS)
    def test_raise_on_ascii_whitespace_secret(
        self, stripe_mock_stripe_client, secret
    ):
        header = generate_header(secret=secret)
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe_mock_stripe_client.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, secret
            )

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
