import hmac
import json
import time
from collections import OrderedDict
from hashlib import sha256
from typing import Optional

# Used for global variables
import stripe  # noqa: IMP101
from stripe._event import Event
from stripe._util import secure_compare
from stripe._error import SignatureVerificationError
from stripe._api_requestor import _APIRequestor


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload, sig_header, secret, tolerance=DEFAULT_TOLERANCE, api_key=None
    ):
        if hasattr(payload, "decode"):
            payload = payload.decode("utf-8")

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        data = json.loads(payload, object_pairs_hook=OrderedDict)
        event = Event._construct_from(
            values=data,
            requestor=_APIRequestor._global_with_options(
                api_key=api_key or stripe.api_key
            ),
            api_mode="V1",
        )

        if event.object == "v2.core.event":  # type: ignore
            raise ValueError(
                "You passed a thin event notification to Webhook.construct_event, which expects a webhook payload. Use StripeClient.parse_event_notification instead."
            )
        return event

    @staticmethod
    def generate_test_header_string(
        payload: str,
        secret: str,
        timestamp: Optional[int] = None,
        scheme: Optional[str] = None,
        signature: Optional[str] = None,
    ) -> str:
        """
        Generates a value for the `Stripe-Signature` header that can be used
        when testing code that calls `Webhook.construct_event` or
        `WebhookSignature.verify_header`. Mirrors `generateTestHeaderString`
        from stripe-node.

        Args:
            payload: The webhook payload to sign, as a string.
            secret: The webhook signing secret (`whsec_...`).
            timestamp: Unix timestamp to embed in the header. Defaults to
                the current time.
            scheme: Signature scheme. Defaults to
                `WebhookSignature.EXPECTED_SCHEME`.
            signature: Pre-computed signature to embed in the header. If
                omitted, a signature is computed from `payload` and `secret`.
        """
        if timestamp is None:
            timestamp = int(time.time())
        if scheme is None:
            scheme = WebhookSignature.EXPECTED_SCHEME
        if signature is None:
            signed_payload = "%d.%s" % (timestamp, payload)
            signature = WebhookSignature._compute_signature(
                signed_payload, secret
            )
        return "t=%d,%s=%s" % (timestamp, scheme, signature)


class WebhookSignature(object):
    EXPECTED_SCHEME = "v1"

    @staticmethod
    def _compute_signature(payload, secret):
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _get_timestamp_and_signatures(header, scheme):
        list_items = [i.split("=", 2) for i in header.split(",")]
        timestamp = int([i[1] for i in list_items if i[0] == "t"][0])
        signatures = [i[1] for i in list_items if i[0] == scheme]
        return timestamp, signatures

    @classmethod
    def verify_header(cls, payload, header, secret, tolerance=None):
        try:
            timestamp, signatures = cls._get_timestamp_and_signatures(
                header, cls.EXPECTED_SCHEME
            )
        except Exception:
            raise SignatureVerificationError(
                "Unable to extract timestamp and signatures from header",
                header,
                payload,
            )

        if not signatures:
            raise SignatureVerificationError(
                "No signatures found with expected scheme "
                "%s" % cls.EXPECTED_SCHEME,
                header,
                payload,
            )

        signed_payload = "%d.%s" % (timestamp, payload)
        expected_sig = cls._compute_signature(signed_payload, secret)
        if not any(secure_compare(expected_sig, s) for s in signatures):
            raise SignatureVerificationError(
                "No signatures found matching the expected signature for "
                "payload",
                header,
                payload,
            )

        if tolerance and timestamp < time.time() - tolerance:
            raise SignatureVerificationError(
                "Timestamp outside the tolerance zone (%d)" % timestamp,
                header,
                payload,
            )

        return True
