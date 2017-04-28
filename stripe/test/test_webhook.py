import time

import stripe
from stripe.test.helper import (
    StripeUnitTestCase, DUMMY_WEBHOOK_PAYLOAD, DUMMY_WEBHOOK_SECRET
)


class WebhookTests(StripeUnitTestCase):
    def test_construct_event(self):
        header = WebhookSignatureTests.generate_header()
        event = stripe.Webhook.construct_event(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET)
        self.assertTrue(isinstance(event, stripe.Event))

    def test_raise_on_json_error(self):
        payload = 'this is not valid JSON'
        header = WebhookSignatureTests.generate_header(payload=payload)
        with self.assertRaises(ValueError):
            stripe.Webhook.construct_event(
                payload, header, DUMMY_WEBHOOK_SECRET)

    def test_raise_on_invalid_header(self):
        header = 'bad_header'
        with self.assertRaises(stripe.error.SignatureVerificationError):
            stripe.Webhook.construct_event(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET)


class WebhookSignatureTests(StripeUnitTestCase):
    @staticmethod
    def generate_header(**kwargs):
        timestamp = kwargs.get('timestamp', int(time.time()))
        payload = kwargs.get('payload', DUMMY_WEBHOOK_PAYLOAD)
        secret = kwargs.get('secret', DUMMY_WEBHOOK_SECRET)
        scheme = kwargs.get('scheme', stripe.WebhookSignature.EXPECTED_SCHEME)
        signature = kwargs.get('signature', None)
        if signature is None:
            payload_to_sign = "%d.%s" % (timestamp, payload)
            signature = stripe.WebhookSignature._compute_signature(
                payload_to_sign, secret)
        header = "t=%d,%s=%s" % (timestamp, scheme, signature)
        return header

    def test_raise_on_malformed_header(self):
        header = "i'm not even a real signature header"
        with self.assertRaisesRegexp(
                stripe.error.SignatureVerificationError,
                "Unable to extract timestamp and signatures from header"):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET)

    def test_raise_on_no_signatures_with_expected_scheme(self):
        header = self.generate_header(scheme='v0')
        with self.assertRaisesRegexp(
                stripe.error.SignatureVerificationError,
                "No signatures found with expected scheme v1"):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET)

    def test_raise_on_no_valid_signatures_for_payload(self):
        header = self.generate_header(signature='bad_signature')
        with self.assertRaisesRegexp(
                stripe.error.SignatureVerificationError,
                "No signatures found matching the expected signature for "
                "payload"):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET)

    def test_raise_on_timestamp_outside_tolerance(self):
        header = self.generate_header(timestamp=int(time.time()) - 15)
        with self.assertRaisesRegexp(
                stripe.error.SignatureVerificationError,
                "Timestamp outside the tolerance zone"):
            stripe.WebhookSignature.verify_header(
                DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET,
                tolerance=10)

    def test_valid_header_and_signature(self):
        header = self.generate_header()
        self.assertTrue(stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET,
            tolerance=10))

    def test_header_contains_valid_signature(self):
        header = self.generate_header() + ",v1=bad_signature"
        self.assertTrue(stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET,
            tolerance=10))

    def test_timestamp_off_but_no_tolerance(self):
        header = self.generate_header(timestamp=12345)
        self.assertTrue(stripe.WebhookSignature.verify_header(
            DUMMY_WEBHOOK_PAYLOAD, header, DUMMY_WEBHOOK_SECRET))
