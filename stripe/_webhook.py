import hmac
import json
import time
from collections import OrderedDict
from hashlib import sha256
from typing import Any, Dict, Optional, Union

# Used for global variables
import stripe  # noqa: IMP101
from stripe._event import Event
from stripe._util import secure_compare
from stripe._error import SignatureVerificationError
from stripe._api_requestor import _APIRequestor


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


def maybe_extract_from_cloud_provider_envelope(
    payload: Union[bytes, str],
):
    """
    Internal helper to extract the inner type from a cloud provider envelope (regardless of what's in there).
    If the payload is already a raw Stripe event (object is 'event' or 'v2.core.event'), returns the parsed dict as-is.
    """
    if isinstance(payload, bytes):
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
        "Unrecognized cloud event format. The payload must be an AWS EventBridge or Azure Event Grid event envelope."
    )


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload: Union[bytes, str],
        sig_header: str,
        secret: str,
        tolerance: int = DEFAULT_TOLERANCE,
        api_key: Optional[str] = None,
        api_requestor: Optional[_APIRequestor] = None,
    ):
        """Constructs a [snapshot event](https://docs.stripe.com/event-destinations#snapshot-payload) from an incoming webhook after verifying its authenticity. To work with a webhook that has already been verified (i.e. one from a cloud provider, an asynchronous queue, or during testing), see `construct_event_without_verification`."""
        if isinstance(payload, (bytes, bytearray)):
            payload = payload.decode("utf-8")

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
        payload: Union[bytes, str],
        api_requestor: Optional[_APIRequestor] = None,
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
        payload: Union[bytes, str],
        header: str,
        secret: str,
        tolerance=None,
    ):
        """Verifies the authenticity (and recency) of a webhook, throwing a `SignatureVerificationError` if there's a mismatch. Useful for quickly validating incoming webhooks before storing them for later processing (at which time you can use the `*_without_verification` methods for parsing)."""
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
