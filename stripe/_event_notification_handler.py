"""
We use a combination of generics and inheritance to construct 4 handler classes with perfect type information while reusing as much code as we can.
Each handler has the methods/signatures that will actually work:

|       | verified                            | unverified                                             |
| ----- | ----------------------------------- | ------------------------------------------------------ |
| sync  | StripeEventNotificationHandler      | StripeEventNotificationHandlerWithoutVerification      |
| async | AsyncStripeEventNotificationHandler | AsyncStripeEventNotificationHandlerWithoutVerification |

A pair of generic variables gives us the following class hierarchy (names edited for brevity):

- _BaseHandler(Generic[CallbackReturn, PreHandleReturn])
    - _SyncHandler(_BaseHandler[None, bool])
        - StripeHandler(_SyncHandler)
        - StripeHandlerWithoutVerification(_SyncHandler)
    - _AsyncHandler(_BaseHandler[None, bool])
        - AsyncStripeHandler(_AsyncHandler)
        - AsyncStripeHandlerWithoutVerification(_AsyncHandler)

Each defines `handle` and `register` methods corresponding to the types it expects
"""

from dataclasses import dataclass
from typing_extensions import TYPE_CHECKING, Awaitable

from typing import (
    Callable,
    Generic,
    List,
    Optional,
    TypeVar,
)

# Import at runtime for isinstance check and type annotations
from stripe.v2.core._event import EventNotification, UnknownEventNotification

if TYPE_CHECKING:
    from stripe._stripe_client import StripeClient

    # event-notification-types: The beginning of the section generated from our OpenAPI spec
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_failed_event import (
        V2CommerceProductCatalogImportsFailedEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_processing_event import (
        V2CommerceProductCatalogImportsProcessingEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_succeeded_event import (
        V2CommerceProductCatalogImportsSucceededEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event import (
        V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_future_requirements_updated_event import (
        V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_identity_updated_event import (
        V2CoreAccountIncludingIdentityUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_requirements_updated_event import (
        V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_link_returned_event import (
        V2CoreAccountLinkReturnedEventNotification,
    )
    from stripe.events._v2_core_account_person_created_event import (
        V2CoreAccountPersonCreatedEventNotification,
    )
    from stripe.events._v2_core_account_person_deleted_event import (
        V2CoreAccountPersonDeletedEventNotification,
    )
    from stripe.events._v2_core_account_person_updated_event import (
        V2CoreAccountPersonUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )
    # event-notification-types: The end of the section generated from our OpenAPI spec

# internal type to represent any EventNotification subclass
EventNotificationChild = TypeVar(
    "EventNotificationChild", bound="EventNotification"
)


@dataclass
class UnhandledNotificationDetails:
    """
    Information about an unhandled event notification to make it easier to respond (and potentially update your integration).
    """

    is_known_event_type: bool
    """
    If true, the unhandled event's type is known to the SDK (i.e., it was successfully deserialized into a specific `EventNotification` subclass).
    """


# The handler base class is generic over what its callbacks return, which lets us reuse base classes for both the sync and async handlers.
CallbackReturn = TypeVar("CallbackReturn")
PreHandleReturn = TypeVar("PreHandleReturn")

_FallbackCallback = Callable[
    [EventNotification, "StripeClient", UnhandledNotificationDetails],
    CallbackReturn,
]

_PreHandleCallback = Callable[
    [EventNotification, "StripeClient"], PreHandleReturn
]

FallbackCallback = _FallbackCallback[None]
"""
Called when no other callback is registered for a given event notification type.
"""

AsyncFallbackCallback = _FallbackCallback[Awaitable[None]]
"""
This async function is called when no other callback is registered for a given event notification type.
"""

PreHandleCallback = _PreHandleCallback[bool]
"""
Called before any of your callbacks are run. Useful for filtering.
"""

AsyncPreHandleCallback = _PreHandleCallback[Awaitable[bool]]
"""
This async function is called before any of your callbacks are run. Useful for filtering.
"""


class _BaseEventNotificationHandler(Generic[CallbackReturn, PreHandleReturn]):
    """
    Shared internal registration machinery for the user-facing event handlers.

    Holds everything that doesn't depend on whether callbacks are awaited; the
    sync and async subclasses below add only the dispatch loop itself.
    """

    def __init__(
        self,
        client: "StripeClient",
        fallback_callback: _FallbackCallback[CallbackReturn],
    ) -> None:
        self._registered_handlers = {}
        self._client = client
        self.fallback_callback = fallback_callback
        # once this is true, adding additional handlers results in an error
        self._has_handled_events = False
        self._pre_handle_callback: Optional[
            _PreHandleCallback[PreHandleReturn]
        ] = None

    def _assert_hasnt_handled(self) -> None:
        """
        Callbacks are expected to be registered on startup, so registering anything after handling an event indicates a bug.
        """
        if self._has_handled_events:
            raise RuntimeError(
                "Cannot register new callbacks after an event has been handled. This is indicative of a bug."
            )

    def pre_handle(
        self, func: _PreHandleCallback[PreHandleReturn]
    ) -> _PreHandleCallback[PreHandleReturn]:
        """
        Registers a function that will be run before any event-specific callbacks. A useful place to store event-agnostic logic, such as logging or checking for [duplicate event deliveries](https://docs.stripe.com/webhooks#handle-duplicate-events).

        Returning `True` causes handling to continue as normal; returning `False` returns from `.handle()` immediately, so neither the registered callback nor the fallback callback are called.
        """
        self._assert_hasnt_handled()
        if self._pre_handle_callback:
            raise ValueError("A pre_handle callback is already registered")

        self._pre_handle_callback = func
        return func

    def _callback_for(self, event_notif: "EventNotification"):
        """
        Returns the callback registered for this event's type, if any.
        """
        return self._registered_handlers.get(event_notif.type)

    def _unhandled_details(
        self, event_notif: "EventNotification"
    ) -> UnhandledNotificationDetails:
        return UnhandledNotificationDetails(
            is_known_event_type=not isinstance(
                event_notif, UnknownEventNotification
            )
        )

    def _register(
        self,
        event_type: str,
        func: "Callable[[EventNotificationChild, StripeClient], CallbackReturn]",
    ) -> None:
        self._assert_hasnt_handled()
        if event_type in self._registered_handlers:
            raise ValueError(
                f'Callback for event type "{event_type}" is already registered'
            )

        self._registered_handlers[event_type] = func

    @property
    def registered_event_types(self) -> List[str]:
        """
        Returns an alphabetized list of all event types that have registered handlers.
        """
        return sorted(self._registered_handlers.keys())

    # event-notification-registration-methods: The beginning of the section generated from our OpenAPI spec
    def on_v1_billing_meter_error_report_triggered(
        self,
        func: "Callable[[V1BillingMeterErrorReportTriggeredEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V1BillingMeterErrorReportTriggeredEvent` (`v1.billing.meter.error_report_triggered`) event notification.
        """
        self._register(
            "v1.billing.meter.error_report_triggered",
            func,
        )
        return func

    def on_v1_billing_meter_no_meter_found(
        self,
        func: "Callable[[V1BillingMeterNoMeterFoundEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V1BillingMeterNoMeterFoundEvent` (`v1.billing.meter.no_meter_found`) event notification.
        """
        self._register(
            "v1.billing.meter.no_meter_found",
            func,
        )
        return func

    def on_v2_commerce_product_catalog_imports_failed(
        self,
        func: "Callable[[V2CommerceProductCatalogImportsFailedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CommerceProductCatalogImportsFailedEvent` (`v2.commerce.product_catalog.imports.failed`) event notification.
        """
        self._register(
            "v2.commerce.product_catalog.imports.failed",
            func,
        )
        return func

    def on_v2_commerce_product_catalog_imports_processing(
        self,
        func: "Callable[[V2CommerceProductCatalogImportsProcessingEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CommerceProductCatalogImportsProcessingEvent` (`v2.commerce.product_catalog.imports.processing`) event notification.
        """
        self._register(
            "v2.commerce.product_catalog.imports.processing",
            func,
        )
        return func

    def on_v2_commerce_product_catalog_imports_succeeded(
        self,
        func: "Callable[[V2CommerceProductCatalogImportsSucceededEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CommerceProductCatalogImportsSucceededEvent` (`v2.commerce.product_catalog.imports.succeeded`) event notification.
        """
        self._register(
            "v2.commerce.product_catalog.imports.succeeded",
            func,
        )
        return func

    def on_v2_commerce_product_catalog_imports_succeeded_with_errors(
        self,
        func: "Callable[[V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CommerceProductCatalogImportsSucceededWithErrorsEvent` (`v2.commerce.product_catalog.imports.succeeded_with_errors`) event notification.
        """
        self._register(
            "v2.commerce.product_catalog.imports.succeeded_with_errors",
            func,
        )
        return func

    def on_v2_core_account_closed(
        self,
        func: "Callable[[V2CoreAccountClosedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountClosedEvent` (`v2.core.account.closed`) event notification.
        """
        self._register(
            "v2.core.account.closed",
            func,
        )
        return func

    def on_v2_core_account_created(
        self,
        func: "Callable[[V2CoreAccountCreatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountCreatedEvent` (`v2.core.account.created`) event notification.
        """
        self._register(
            "v2.core.account.created",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_customer_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.customer].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.customer].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_customer_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationCustomerUpdatedEvent` (`v2.core.account[configuration.customer].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.customer].updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_merchant_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.merchant].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.merchant].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_merchant_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationMerchantUpdatedEvent` (`v2.core.account[configuration.merchant].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.merchant].updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_recipient_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.recipient].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.recipient].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_recipient_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationRecipientUpdatedEvent` (`v2.core.account[configuration.recipient].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.recipient].updated",
            func,
        )
        return func

    def on_v2_core_account_including_defaults_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingDefaultsUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingDefaultsUpdatedEvent` (`v2.core.account[defaults].updated`) event notification.
        """
        self._register(
            "v2.core.account[defaults].updated",
            func,
        )
        return func

    def on_v2_core_account_including_future_requirements_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingFutureRequirementsUpdatedEvent` (`v2.core.account[future_requirements].updated`) event notification.
        """
        self._register(
            "v2.core.account[future_requirements].updated",
            func,
        )
        return func

    def on_v2_core_account_including_identity_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingIdentityUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingIdentityUpdatedEvent` (`v2.core.account[identity].updated`) event notification.
        """
        self._register(
            "v2.core.account[identity].updated",
            func,
        )
        return func

    def on_v2_core_account_including_requirements_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingRequirementsUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingRequirementsUpdatedEvent` (`v2.core.account[requirements].updated`) event notification.
        """
        self._register(
            "v2.core.account[requirements].updated",
            func,
        )
        return func

    def on_v2_core_account_link_returned(
        self,
        func: "Callable[[V2CoreAccountLinkReturnedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountLinkReturnedEvent` (`v2.core.account_link.returned`) event notification.
        """
        self._register(
            "v2.core.account_link.returned",
            func,
        )
        return func

    def on_v2_core_account_person_created(
        self,
        func: "Callable[[V2CoreAccountPersonCreatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountPersonCreatedEvent` (`v2.core.account_person.created`) event notification.
        """
        self._register(
            "v2.core.account_person.created",
            func,
        )
        return func

    def on_v2_core_account_person_deleted(
        self,
        func: "Callable[[V2CoreAccountPersonDeletedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountPersonDeletedEvent` (`v2.core.account_person.deleted`) event notification.
        """
        self._register(
            "v2.core.account_person.deleted",
            func,
        )
        return func

    def on_v2_core_account_person_updated(
        self,
        func: "Callable[[V2CoreAccountPersonUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountPersonUpdatedEvent` (`v2.core.account_person.updated`) event notification.
        """
        self._register(
            "v2.core.account_person.updated",
            func,
        )
        return func

    def on_v2_core_account_updated(
        self,
        func: "Callable[[V2CoreAccountUpdatedEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreAccountUpdatedEvent` (`v2.core.account.updated`) event notification.
        """
        self._register(
            "v2.core.account.updated",
            func,
        )
        return func

    def on_v2_core_event_destination_ping(
        self,
        func: "Callable[[V2CoreEventDestinationPingEventNotification, StripeClient], CallbackReturn]",
    ):
        """
        Registers a callback for the `V2CoreEventDestinationPingEvent` (`v2.core.event_destination.ping`) event notification.
        """
        self._register(
            "v2.core.event_destination.ping",
            func,
        )
        return func

    # event-notification-registration-methods: The end of the section generated from our OpenAPI spec


class _SyncEventNotificationHandler(_BaseEventNotificationHandler[None, bool]):
    """
    Adds synchronous dispatch. Shared by the verifying and non-verifying sync
    handlers, which differ only in how they parse the incoming payload.
    """

    def _dispatch(self, event_notif: "EventNotification") -> None:
        client = self._client.with_stripe_context(event_notif.context)

        if self._pre_handle_callback and not self._pre_handle_callback(
            event_notif, client
        ):
            return

        if callback := self._callback_for(event_notif):
            callback(event_notif, client)
        else:
            self.fallback_callback(
                event_notif, client, self._unhandled_details(event_notif)
            )


class _AsyncEventNotificationHandler(
    _BaseEventNotificationHandler[Awaitable[None], Awaitable[bool]]
):
    """
    Adds asynchronous dispatch. Only the callbacks are awaited: verifying a
    signature and parsing the payload are pure CPU work, so they stay
    synchronous even here.
    """

    async def _dispatch_async(self, event_notif: "EventNotification") -> None:
        client = self._client.with_stripe_context(event_notif.context)

        if self._pre_handle_callback and not await self._pre_handle_callback(
            event_notif, client
        ):
            return

        if callback := self._callback_for(event_notif):
            await callback(event_notif, client)
        else:
            await self.fallback_callback(
                event_notif, client, self._unhandled_details(event_notif)
            )


class StripeEventNotificationHandler(_SyncEventNotificationHandler):
    """
    An on-rails experience for handling Stripe event notifications. Define callbacks for individual event types and an instance of this class will be responsible for verifying and routing the event.
    """

    def __init__(
        self,
        client: "StripeClient",
        webhook_secret: str,
        fallback_callback: FallbackCallback,
    ) -> None:
        super().__init__(client, fallback_callback)
        if not webhook_secret:
            raise ValueError("webhook_secret must be a non-empty string")
        self._webhook_secret = webhook_secret

    def handle(self, webhook_body: str, sig_header: str):
        # set before parsing, so that even a failed parse locks out registration.
        # modification isn't thread-safe, but we expect callbacks to get registered synchronously at startup
        # making a race condition here unlikely
        self._has_handled_events = True

        event_notif = self._client.parse_event_notification(
            webhook_body, sig_header, self._webhook_secret
        )

        self._dispatch(event_notif)

    @staticmethod
    def without_verification(
        client: "StripeClient",
        fallback_callback: FallbackCallback,
    ) -> "StripeEventNotificationHandlerWithoutVerification":
        return StripeEventNotificationHandlerWithoutVerification(
            client, fallback_callback
        )


class StripeEventNotificationHandlerWithoutVerification(
    _SyncEventNotificationHandler
):
    """
    A variant of StripeEventNotificationHandler that parses events without verifying webhook signatures. Intended for pre-authenticated channels like AWS EventBridge, Azure Event Grid, or your own pre-authenticated queuing system.

    Prefer `StripeEventNotificationHandler.without_verification()` or `client.notification_handler_without_verification()` instead of constructing it directly.
    """

    def handle(self, webhook_body: str):
        self._has_handled_events = True

        event_notif = (
            self._client.parse_event_notification_without_verification(
                webhook_body
            )
        )

        self._dispatch(event_notif)


class AsyncStripeEventNotificationHandler(_AsyncEventNotificationHandler):
    """
    The async equivalent of `StripeEventNotificationHandler`, for use from async web frameworks. Register `async def` callbacks and await `.handle_async()`.
    """

    def __init__(
        self,
        client: "StripeClient",
        webhook_secret: str,
        fallback_callback: AsyncFallbackCallback,
    ) -> None:
        super().__init__(client, fallback_callback)
        if not webhook_secret:
            raise ValueError("webhook_secret must be a non-empty string")
        self._webhook_secret = webhook_secret

    async def handle_async(self, webhook_body: str, sig_header: str):
        self._has_handled_events = True

        event_notif = self._client.parse_event_notification(
            webhook_body, sig_header, self._webhook_secret
        )

        await self._dispatch_async(event_notif)

    @staticmethod
    def without_verification(
        client: "StripeClient",
        fallback_callback: AsyncFallbackCallback,
    ) -> "AsyncStripeEventNotificationHandlerWithoutVerification":
        return AsyncStripeEventNotificationHandlerWithoutVerification(
            client, fallback_callback
        )


class AsyncStripeEventNotificationHandlerWithoutVerification(
    _AsyncEventNotificationHandler
):
    """
    A variant of AsyncStripeEventNotificationHandler that parses events without verifying webhook signatures. Intended for pre-authenticated channels like AWS EventBridge, Azure Event Grid, or your own pre-authenticated queuing system.

    Prefer `AsyncStripeEventNotificationHandler.without_verification()` or `client.async_notification_handler_without_verification()` instead of constructing it directly.
    """

    async def handle_async(self, webhook_body: str):
        self._has_handled_events = True

        event_notif = (
            self._client.parse_event_notification_without_verification(
                webhook_body
            )
        )

        await self._dispatch_async(event_notif)
