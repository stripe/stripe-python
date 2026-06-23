# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

from stripe import (
    DEFAULT_API_BASE,
    DEFAULT_CONNECT_API_BASE,
    DEFAULT_UPLOAD_API_BASE,
    DEFAULT_METER_EVENTS_API_BASE,
)

from stripe._api_mode import ApiMode
from stripe._error import AuthenticationError
from stripe._request_options import extract_options_from_dict
from stripe._requestor_options import RequestorOptions, BaseAddresses
from stripe._client_options import _ClientOptions
from stripe._http_client import (
    new_default_http_client,
    new_http_client_async_fallback,
)
from stripe._api_version import _ApiVersion
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import _convert_to_stripe_object, get_api_mode
from stripe._webhook import Webhook, WebhookSignature
from stripe._event import Event
from stripe.v2.core._event import EventNotification

from typing import Any, Dict, Optional, Union, cast
from typing_extensions import TYPE_CHECKING, deprecated

if TYPE_CHECKING:
    from stripe._stripe_context import StripeContext
    from stripe._http_client import HTTPClient

# Non-generated services
from stripe._oauth_service import OAuthService

from stripe._v1_services import V1Services
from stripe._v2_services import V2Services

# service-types: The beginning of the section generated from our OpenAPI spec
if TYPE_CHECKING:
    pass
# service-types: The end of the section generated from our OpenAPI spec

if TYPE_CHECKING:
    from stripe.events._event_classes import ALL_EVENT_NOTIFICATIONS


class StripeClient(object):
    def __init__(
        self,
        api_key: str,
        *,
        stripe_account: Optional[str] = None,
        stripe_context: "Optional[Union[str, StripeContext]]" = None,
        stripe_version: Optional[str] = None,
        base_addresses: Optional[BaseAddresses] = None,
        client_id: Optional[str] = None,
        verify_ssl_certs: bool = True,
        proxy: Optional[str] = None,
        max_network_retries: Optional[int] = None,
        http_client: Optional["HTTPClient"] = None,
    ):
        # The types forbid this, but let's give users without types a friendly error.
        if api_key is None:  # pyright: ignore[reportUnnecessaryComparison]
            raise AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"client = stripe.StripeClient(<API-KEY>)"). You can '
                "generate API keys from the Stripe web interface. "
                "See https://stripe.com/api for details, or email "
                "support@stripe.com if you have any questions."
            )

        if http_client and (proxy or verify_ssl_certs is not True):
            raise ValueError(
                "You cannot specify `proxy` or `verify_ssl_certs` when passing "
                "in a custom `http_client`. Please set these values on your "
                "custom `http_client` instead."
            )

        # Default to stripe.DEFAULT_API_BASE, stripe.DEFAULT_CONNECT_API_BASE,
        # and stripe.DEFAULT_UPLOAD_API_BASE if not set in base_addresses.
        base_addresses = {
            "api": DEFAULT_API_BASE,
            "connect": DEFAULT_CONNECT_API_BASE,
            "files": DEFAULT_UPLOAD_API_BASE,
            "meter_events": DEFAULT_METER_EVENTS_API_BASE,
            **(base_addresses or {}),
        }

        requestor_options = RequestorOptions(
            api_key=api_key,
            stripe_account=stripe_account,
            stripe_context=stripe_context,
            stripe_version=stripe_version or _ApiVersion.CURRENT,
            base_addresses=base_addresses,
            max_network_retries=max_network_retries,
        )

        if http_client is None:
            http_client = new_default_http_client(
                async_fallback_client=new_http_client_async_fallback(
                    proxy=proxy, verify_ssl_certs=verify_ssl_certs
                ),
                proxy=proxy,
                verify_ssl_certs=verify_ssl_certs,
            )

        from stripe._api_requestor import _APIRequestor

        self._requestor = _APIRequestor(
            options=requestor_options,
            client=http_client,
        )

        self._options = _ClientOptions(
            client_id=client_id,
            proxy=proxy,
            verify_ssl_certs=verify_ssl_certs,
        )

        self.oauth = OAuthService(self._requestor, self._options)

        # top-level services: The beginning of the section generated from our OpenAPI spec
        # top-level services: The end of the section generated from our OpenAPI spec

    def parse_event_notification(
        self,
        raw: Union[bytes, str, bytearray],
        sig_header: str,
        secret: str,
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> "ALL_EVENT_NOTIFICATIONS":
        """
        This should be your main method for interacting with `EventNotifications`. It's the V2 equivalent of `construct_event()`, but with better typing support.

        It returns a union representing all known `EventNotification` classes. They have a `type` property that can be used for narrowing, which will get you very specific type support. If parsing an event the SDK isn't familiar with, it'll instead return `UnknownEventNotification`. That's not reflected in the return type of the function (because it messes up type narrowing) but is otherwise intended.
        """
        payload = (
            cast(Union[bytes, bytearray], raw).decode("utf-8")
            if hasattr(raw, "decode")
            else cast(str, raw)
        )

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        # TODO(DEVSDK-2968): Remove once Custom Events are sent with the correct type.
        # Rewrite the type in the JSON payload BEFORE from_json so the type
        # registry resolves the correct EventNotification subclass.
        parsed = json.loads(payload)
        evt_type = parsed.get("type", "")
        related = parsed.get("related_object") or {}
        related_type = related.get("type")
        if (
            isinstance(evt_type, str)
            and evt_type.startswith("v2.extend.objects.object_record")
            and isinstance(related_type, str)
        ):
            parsed["type"] = evt_type.replace(
                "v2.extend.objects.object_record", related_type, 1
            )
            payload = json.dumps(parsed)

        event_notification = cast(
            "ALL_EVENT_NOTIFICATIONS",
            EventNotification.from_json(payload, self),
        )

        return event_notification

    def construct_event(
        self,
        payload: Union[bytes, str],
        sig_header: str,
        secret: str,
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> Event:
        if hasattr(payload, "decode"):
            payload = cast(bytes, payload).decode("utf-8")

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        data = json.loads(payload, object_pairs_hook=OrderedDict)
        event = Event._construct_from(
            values=data,
            requestor=self._requestor,
            api_mode="V1",
        )
        if event.object == "v2.core.event":  # type: ignore
            raise ValueError(
                "You passed a thin event notification to StripeClient.construct_event, which expects a webhook payload. Use StripeClient.parse_event_notification instead."
            )

        return event

    def raw_request(self, method_: str, url_: str, **params):
        params = params.copy()
        options, params = extract_options_from_dict(params)
        api_mode = get_api_mode(url_)
        base_address = params.pop("base", "api")

        # we manually pass usage in event internals, so use those if available
        usage = params.pop("usage", ["raw_request"])

        rbody, rcode, rheaders = self._requestor.request_raw(
            method_,
            url_,
            params=params,
            options=options,
            base_address=base_address,
            api_mode=api_mode,
            usage=usage,
        )

        return self._requestor._interpret_response(
            rbody, rcode, rheaders, api_mode
        )

    async def raw_request_async(self, method_: str, url_: str, **params):
        params = params.copy()
        options, params = extract_options_from_dict(params)
        api_mode = get_api_mode(url_)
        base_address = params.pop("base", "api")

        rbody, rcode, rheaders = await self._requestor.request_raw_async(
            method_,
            url_,
            params=params,
            options=options,
            base_address=base_address,
            api_mode=api_mode,
            usage=["raw_request"],
        )

        return self._requestor._interpret_response(
            rbody, rcode, rheaders, api_mode
        )

    def deserialize(
        self,
        resp: Union[StripeResponse, Dict[str, Any]],
        params: Optional[Dict[str, Any]] = None,
        *,
        api_mode: ApiMode,
    ) -> StripeObject:
        """
        Used to translate the result of a `raw_request` into a StripeObject.
        """
        return _convert_to_stripe_object(
            resp=resp,
            params=params,
            requestor=self._requestor,
            api_mode=api_mode,
        )

    # deprecated v1 services: The beginning of the section generated from our OpenAPI spec
    # deprecated v1 services: The end of the section generated from our OpenAPI spec
