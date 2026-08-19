# -*- coding: utf-8 -*-
from dataclasses import dataclass
from typing_extensions import TYPE_CHECKING

from typing import TypeVar, Callable, List

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


FallbackCallback = Callable[
    [EventNotification, "StripeClient", UnhandledNotificationDetails], None
]
"""
This function is called when no other callback is registered for a given event notification type.
"""


class _BaseEventNotificationHandler:
    """
    Shared internal registration and dispatch machinery for the two user-facing event handlers.
    """

    def __init__(
        self,
        client: "StripeClient",
        fallback_callback: FallbackCallback,
    ) -> None:
        self._registered_handlers = {}
        self._client = client
        self.fallback_callback = fallback_callback
        # once this is true, adding additional handlers results in an error
        self._has_handled_events = False

    def _dispatch(self, event_notif: "EventNotification"):
        # Create a new client with the event's context.
        # This is thread-safe since we're not modifying the original client.
        # The new client reuses the HTTP client to avoid TLS handshake overhead.
        client_with_event_context = self._client.with_stripe_context(
            event_notif.context
        )

        if event_notif.type in self._registered_handlers:
            self._registered_handlers[event_notif.type](
                event_notif, client_with_event_context
            )
        else:
            self.fallback_callback(
                event_notif,
                client_with_event_context,
                UnhandledNotificationDetails(
                    is_known_event_type=not isinstance(
                        event_notif, UnknownEventNotification
                    )
                ),
            )

    def _register(
        self,
        event_type: str,
        func: "Callable[[EventNotificationChild, StripeClient], None]",
    ) -> None:
        if self._has_handled_events:
            raise RuntimeError(
                "Cannot register new event handlers after .handle() has been called. This is indicative of a bug."
            )
        if event_type in self._registered_handlers:
            raise ValueError(
                f'Handler for event type "{event_type}" already registered.'
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
        func: "Callable[[V1BillingMeterErrorReportTriggeredEventNotification, StripeClient], None]",
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
        func: "Callable[[V1BillingMeterNoMeterFoundEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CommerceProductCatalogImportsFailedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CommerceProductCatalogImportsProcessingEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CommerceProductCatalogImportsSucceededEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountClosedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountCreatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingDefaultsUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingIdentityUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountIncludingRequirementsUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountLinkReturnedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountPersonCreatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountPersonDeletedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountPersonUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreAccountUpdatedEventNotification, StripeClient], None]",
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
        func: "Callable[[V2CoreEventDestinationPingEventNotification, StripeClient], None]",
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


class StripeEventNotificationHandler(_BaseEventNotificationHandler):
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
    _BaseEventNotificationHandler
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
