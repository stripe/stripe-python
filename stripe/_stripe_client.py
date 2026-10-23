# -*- coding: utf-8 -*-
import json

from stripe import (
    DEFAULT_API_BASE,
    DEFAULT_CONNECT_API_BASE,
    DEFAULT_UPLOAD_API_BASE,
    DEFAULT_METER_EVENTS_API_BASE,
)

from stripe._api_mode import ApiMode
from stripe._error import AuthenticationError
from stripe._event_notification_handler import (
    AsyncFallbackCallback,
    AsyncStripeEventNotificationHandler,
    AsyncStripeEventNotificationHandlerWithoutVerification,
    StripeEventNotificationHandler,
    StripeEventNotificationHandlerWithoutVerification,
    FallbackCallback,
)
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
from stripe._webhook import (
    Webhook,
    WebhookPayload,
    WebhookSignature,
    maybe_extract_from_cloud_provider_envelope,
)
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

    def construct_event(
        self,
        payload: WebhookPayload,
        sig_header: Optional[str],
        secret: Optional[str],
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> Event:
        """Constructs a [snapshot event](https://docs.stripe.com/event-destinations#snapshot-payload) from an incoming webhook after verifying its authenticity. To work with a webhook that has already been verified (i.e. one from a cloud provider, an asynchronous queue, or during testing), see `construct_event_without_verification`.

        `sig_header` and `secret` are only marked as `Optional` so they play nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if either is missing."""
        return Webhook.construct_event(
            payload,
            sig_header,
            secret,
            tolerance,
            api_requestor=self._requestor,
        )

    def construct_event_without_verification(
        self,
        payload: WebhookPayload,
    ) -> Event:
        """Constructs a [snapshot event](https://docs.stripe.com/event-destinations#snapshot-payload) from an incoming webhook without first verifying its authenticity. Should be used after calling `Webhook.verify_header(...)` or with input from a trusted source (such as [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge), or [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) payload). Or, to verify & construct in a single call, use `Webhook.construct_event(...)` instead."""
        return Webhook.construct_event_without_verification(
            payload, api_requestor=self._requestor
        )

    def parse_event_notification(
        self,
        raw: WebhookPayload,
        sig_header: Optional[str],
        secret: Optional[str],
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> "ALL_EVENT_NOTIFICATIONS":
        """Constructs a [thin event notification](https://docs.stripe.com/event-destinations#thin-payload) from an incoming webhook after verifying its authenticity. To work with a webhook that has already been verified (i.e. one from a cloud provider, an asynchronous queue, or during testing), see `parse_event_notification_without_verification`.

        `sig_header` and `secret` are only marked as `Optional` so they play nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if either is missing."""
        WebhookSignature.verify_header(raw, sig_header, secret, tolerance)

        # TODO(DEVSDK-2968): Remove once Custom Events are sent with the correct type.
        # Rewrite the type in the JSON raw payload BEFORE from_json so the type
        # registry resolves the correct EventNotification subclass.
        parsed = json.loads(raw)
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
            raw = json.dumps(parsed)

        event_notification = cast(
            "ALL_EVENT_NOTIFICATIONS",
            EventNotification.from_json(raw, self),
        )

        return event_notification

    def parse_event_notification_without_verification(
        self,
        payload: WebhookPayload,
    ) -> "ALL_EVENT_NOTIFICATIONS":
        """Constructs a [thin event notification](https://docs.stripe.com/event-destinations#thin-payload) from an incoming webhook without first verifying its authenticity. Should be used after calling `Webhook.verify_header(...)` or with input from a trusted source (such as [AWS EventBridge](https://docs.stripe.com/event-destinations/eventbridge), or [Azure Event Grid](https://docs.stripe.com/event-destinations/eventgrid) payload). Or, to verify & parse in a single call, use `parse_event_notification(...)` instead."""

        return cast(
            "ALL_EVENT_NOTIFICATIONS",
            EventNotification.from_json(
                maybe_extract_from_cloud_provider_envelope(payload), self
            ),
        )

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

    def with_stripe_context(
        self, stripe_context: "Optional[Union[str, StripeContext]]"
    ) -> "StripeClient":
        """
        Creates a new StripeClient with the same configuration as this client,
        but with a different stripe_context. This is useful for handling webhooks
        where each event may have its own context.

        The new client reuses the HTTP client from this client to avoid
        re-establishing TLS connections.
        """
        return StripeClient(
            api_key=self._requestor.api_key,  # type: ignore
            stripe_context=stripe_context,
            stripe_version=self._requestor._options.stripe_version,
            base_addresses=self._requestor._options.base_addresses,
            client_id=self._options.client_id,
            max_network_retries=self._requestor._options.max_network_retries,
            http_client=self._requestor._client,
        )

    def notification_handler(
        self,
        webhook_secret: Optional[str],
        fallback_callback: FallbackCallback,
    ) -> StripeEventNotificationHandler:
        """
        Returns an StripeEventNotificationHandler instance tied to this client.

        `webhook_secret` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `ValueError` if a secret is not provided.
        """
        return StripeEventNotificationHandler(
            self, webhook_secret, fallback_callback
        )

    def notification_handler_without_verification(
        self, fallback_callback: FallbackCallback
    ) -> StripeEventNotificationHandlerWithoutVerification:
        """
        A variant of StripeEventNotificationHandler that parses events without
        verifying webhook signatures. Intended for pre-authenticated channels
        like AWS EventBridge, Azure Event Grid, or your own queue system that
        verifies payloads before storage.
        """
        return StripeEventNotificationHandler.without_verification(
            self, fallback_callback
        )

    def async_notification_handler(
        self,
        webhook_secret: Optional[str],
        fallback_callback: AsyncFallbackCallback,
    ) -> AsyncStripeEventNotificationHandler:
        """
        Returns an AsyncStripeEventNotificationHandler instance tied to this client.
        Register `async def` callbacks on it and run them using `await handler.handle_async()`.

        `webhook_secret` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `ValueError` if a secret is not provided.
        """
        return AsyncStripeEventNotificationHandler(
            self, webhook_secret, fallback_callback
        )

    def async_notification_handler_without_verification(
        self, fallback_callback: AsyncFallbackCallback
    ) -> AsyncStripeEventNotificationHandlerWithoutVerification:
        """
        A variant of AsyncStripeEventNotificationHandler that parses events without
        verifying webhook signatures. Intended for pre-authenticated channels
        like AWS EventBridge, Azure Event Grid, or your own queue system that
        verifies payloads before storage.
        """
        return AsyncStripeEventNotificationHandler.without_verification(
            self, fallback_callback
        )

    # deprecated v1 services: The beginning of the section generated from our OpenAPI spec
    # deprecated v1 services: The end of the section generated from our OpenAPI spec
