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


def extract_from_cloud_provider_envelope(
    payload: Union[bytes, str],
):
    """
    Internal helper to extract the inner type from a cloud provider envelope (regardless of what's in there)
    """
    if isinstance(payload, bytes):
        payload = payload.decode("utf-8")

    data = json.loads(payload, object_pairs_hook=OrderedDict)

    # could add as many checks as we want here, but we'll start simple
    if "detail" in data:
        # AWS
        # https://docs.stripe.com/event-destinations/eventbridge#event-structure
        inner = data["detail"]
    elif "specversion" in data:
        # Azure
        # https://docs.stripe.com/event-destinations/eventgrid#event-structure
        inner = data["data"]
    elif isinstance(data.get("id"), str) and data["id"].startswith("evt_"):
        raise ValueError(
            "It looks like you passed a Stripe Event directly. Use construct_event instead to parse a webhook payload with signature verification."
        )
    else:
        raise ValueError(
            "Unrecognized cloud event format. The payload must be an AWS EventBridge or Azure Event Grid event envelope."
        )

    return inner


class Webhook(object):
    DEFAULT_TOLERANCE = 300

    @staticmethod
    def construct_event(
        payload,
        sig_header,
        secret,
        tolerance=DEFAULT_TOLERANCE,
        api_key=None,
        api_requestor: Optional[_APIRequestor] = None,
    ):
        if hasattr(payload, "decode"):
            payload = payload.decode("utf-8")

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        data = json.loads(payload, object_pairs_hook=OrderedDict)
        return build_v1_event(
            data,
            api_requestor
            or _APIRequestor._global_with_options(
                api_key=api_key or stripe.api_key
            ),
        )


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
