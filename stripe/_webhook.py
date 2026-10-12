import hmac
import json
import time
from collections import OrderedDict
from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Dict, Optional, Union
from urllib.parse import quote

# Used for global variables
import stripe  # noqa: IMP101
from stripe._event import Event
from stripe._util import secure_compare
from stripe._error import SignatureVerificationError
from stripe._api_requestor import _APIRequestor

WebhookPayload = Union[str, bytes, bytearray]
"""
The raw body of an incoming webhook, as read off the request body.
Intentionally wide to work nicely with existing types from Django/Flask/FastAPI .
"""


@dataclass
class _DebugMetadata:
    secret: Optional[str] = None
    destination: Optional[str] = None
    payload: Optional[str] = None


def build_v1_event(values: Dict[str, Any], requestor: _APIRequestor) -> Event:
    """
    Internal helper for centralizing v1 event creation
    """
    if values.get("object") == "v2.core.event":
        raise ValueError(
            "You passed a thin event notification to a method that expects a webhook body. Use the corresponding parse_event_notification* method instead."
        )
    return Event._construct_from(
        values=values, requestor=requestor, api_mode="V1"
    )


def maybe_extract_from_cloud_provider_envelope(payload: WebhookPayload):
    """
    Internal helper to extract the inner type from a cloud provider envelope (regardless of what's in there).
    If the payload is already a raw Stripe event (object is 'event' or 'v2.core.event'), returns the parsed dict as-is.
    """
    if isinstance(payload, (bytes, bytearray)):
        payload = payload.decode("utf-8")

    data = json.loads(payload, object_pairs_hook=OrderedDict)

    # could add as many checks as we want here, but we'll start simple
    if detail := data.get("detail"):
        # AWS
        # https://docs.stripe.com/event-destinations/eventbridge#event-structure
        return detail
    elif "specversion" in data and (data_ := data.get("data")):
        # Azure
        # https://docs.stripe.com/event-destinations/eventgrid#event-structure
        return data_
    elif data.get("object") in ("event", "v2.core.event"):
        # Raw Stripe event passed directly: pass through as-is
        return data

    raise ValueError(
        "Unrecognized event format. The payload must be an AWS EventBridge/Azure Event Grid event envelope or a Stripe webhook (thin event notification or snapshot)."
    )


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload: WebhookPayload,
        sig_header: Optional[str],
        secret: Optional[str],
        tolerance: int = DEFAULT_TOLERANCE,
        api_key: Optional[str] = None,
        api_requestor: Optional[_APIRequestor] = None,
    ):
        """Constructs a [snapshot event](https://docs.stripe.com/event-destinations#snapshot-payload) from an incoming webhook after verifying its authenticity. To work with a webhook that has already been verified (i.e. one from a cloud provider, an asynchronous queue, or during testing), see `construct_event_without_verification`.

        `sig_header` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if a signature is not provided."""
        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        return build_v1_event(
            json.loads(payload, object_pairs_hook=OrderedDict),
            api_requestor
            or _APIRequestor._global_with_options(
                api_key=api_key or stripe.api_key
            ),
        )

    @staticmethod
    def construct_event_without_verification(
        payload: WebhookPayload, api_requestor: Optional[_APIRequestor] = None
    ):
        """Constructs a [snapshot event](https://docs.stripe.com/event-destinations#snapshot-payload) from an incoming webhook without first verifying its authenticity. Should be used after calling `WebhookSignature.verify_header(...)` or with input from a trusted source (such as [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge), or [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) payload). Or, to verify & construct in a single call, use `Webhook.construct_event(...)` instead."""
        return build_v1_event(
            maybe_extract_from_cloud_provider_envelope(payload),
            api_requestor
            or _APIRequestor._global_with_options(api_key=stripe.api_key),
        )


class WebhookSignature(object):
    EXPECTED_SCHEME = "v1"

    @staticmethod
    def _compute_signature(payload: str, secret: str) -> str:
        mac = hmac.new(
            secret.encode("utf-8"),
            msg=payload.encode("utf-8"),
            digestmod=sha256,
        )
        return mac.hexdigest()

    @staticmethod
    def _get_timestamp_and_signatures(header: str, scheme: str):
        list_items = [i.split("=", 2) for i in header.split(",")]
        timestamp = int([i[1] for i in list_items if i[0] == "t"][0])
        signatures = [i[1] for i in list_items if i[0] == scheme]
        return timestamp, signatures

    @classmethod
    def generate_signature_header(
        cls, payload: str, secret: str, timestamp=None
    ):
        """Compute the `Stripe-Signature` header for a given webhook body & secret. Useful for signing payloads in unit tests."""
        if timestamp is None:
            timestamp = int(time.time())
        scheme = cls.EXPECTED_SCHEME
        signed_payload = f"{timestamp}.{payload}"
        signature = cls._compute_signature(signed_payload, secret)
        return f"t={timestamp},{scheme}={signature}"

    @classmethod
    def verify_header(
        cls,
        payload: WebhookPayload,
        header: Optional[str],
        secret: Optional[str],
        tolerance=None,
    ):
        """Verifies the authenticity (and recency) of a webhook, throwing a `SignatureVerificationError` if there's a mismatch. Useful for quickly validating incoming webhooks before storing them for later processing (at which time you can use the `*_without_verification` methods for parsing).

        `sig_header` and `secret` are only marked as `Optional` so they play nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if either is missing."""
        # the signature is computed over the string form of the body, so binary
        # input has to be decoded before it's interpolated below
        if isinstance(payload, (bytes, bytearray)):
            payload = payload.decode("utf-8")

        if not header:
            raise SignatureVerificationError(
                "No Stripe-Signature header value was provided. Read it from the incoming request's headers and pass it in; if this webhook has already been verified (or came from a trusted source), use one of the `*_without_verification` methods instead.",
                header,
                payload,
            )
        if secret is None or secret.strip(" \t\r\n\f\v") == "":
            raise SignatureVerificationError(
                "No webhook secret value was provided. It should start with `whsec_`",
                header,
                payload,
            )

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
                cls._signature_error_message(header, str(payload), secret),
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

    @classmethod
    def _signature_error_message(
        cls, header: str, payload: str, secret: str
    ) -> str:
        """Build an HMAC-mismatch message using optional header metadata."""
        metadata = cls._signature_debug_metadata(header)

        # If metadata has an asterisk-masked secret, compare against its length and last four characters
        masked_secret = metadata.secret or ""
        secret_suffix = secret[-4:]
        if "*" in masked_secret and (
            len(secret) != len(masked_secret)
            or secret_suffix != masked_secret[-4:]
        ):
            dashboard_url = "https://dashboard.stripe.com/webhooks"
            if metadata.destination is not None:
                dashboard_url += "/" + quote(metadata.destination, safe="")
            return (
                "Webhook signature verification failed. This request may not "
                "have originated from Stripe.\n\n"
                f"The signing secret you provided is {len(secret)} characters "
                f"long and ends in `{secret_suffix}`. However, the signing "
                "secret for this destination is "
                f"{len(masked_secret)} characters long and looks like "
                f"`{masked_secret}`. Ensure you're using the signing secret "
                "for this destination, as shown on the Dashboard: "
                f"{dashboard_url}\n\n"
                "Learn more: https://docs.stripe.com/webhooks/signature"
            )

        # If metadata includes the truncated payload hash, compare with the payload passed in
        expected_hash = (metadata.payload or "").lower()
        if len(expected_hash) == 8 and all(
            character in "0123456789abcdef" for character in expected_hash
        ):
            actual_hash = sha256(payload.encode("utf-8")).hexdigest()[-8:]
            if expected_hash != actual_hash:
                return (
                    "Webhook signature verification failed.\n\n"
                    "The request body you passed to this function differs "
                    "from the request body sent by Stripe to this webhook "
                    "destination.\n"
                    "The SHA-256 hash of the body should end in "
                    f"`{expected_hash}`. However, the SHA-256 hash of the body "
                    f"you provided ends in `{actual_hash}`.\n\n"
                    "Make sure your code does not reformat or otherwise alter "
                    "the raw HTTP request body before passing it to this "
                    "function.\n\n"
                    "Learn more: https://docs.stripe.com/webhooks/signature"
                )

        # Fall back to the generic message if no debug metadata available
        return (
            "No signatures found matching the expected signature for payload"
        )

    @classmethod
    def _signature_debug_metadata(cls, header: str) -> _DebugMetadata:
        """Extract metadata from the stripe-signature header value to help debug verification failures."""
        # For each metadata key, extract the first value found in the header
        metadata: Dict[str, Optional[str]] = {}
        for item in header.split(","):
            key, separator, value = item.lstrip().partition("=")
            if (
                key in ("secret", "destination", "payload")
                and key not in metadata
            ):
                metadata[key] = (
                    cls._safe_metadata_value(value) if separator else None
                )
        return _DebugMetadata(
            metadata.get("secret"),
            metadata.get("destination"),
            metadata.get("payload"),
        )

    @staticmethod
    def _safe_metadata_value(value: str) -> Optional[str]:
        """Return a bounded UTF-8 metadata value, or None if unusable."""
        # Ignore overly long, potentially attacker-provided metadata values
        if len(value) > 100:
            return None
        try:
            value.encode("utf-8")
        except UnicodeEncodeError:
            return None
        return value.strip() or None
