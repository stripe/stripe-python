from typing_extensions import TYPE_CHECKING

from typing import TypeVar, Callable

if TYPE_CHECKING:
    from stripe._stripe_client import StripeClient
    from stripe.v2.core._event import (
        EventNotification,
        UnknownEventNotification,
    )

    # event-notification-types: The beginning of the section generated from our OpenAPI spec
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )
    # event-notification-types: The end of the section generated from our OpenAPI spec


EventNotificationChild = TypeVar(
    "EventNotificationChild", bound="EventNotification"
)

UNKNOWN_EVENT_TYPE_KEY = "__unknown_event_type"


class EventHandler:
    def __init__(self, client: "StripeClient", webhook_secret: str) -> None:
        self._registered_handlers = {}
        self._client = client
        self._webhook_secret = webhook_secret
        # once this is true, adding additional handlers results in an error
        self._has_handled_events = False

    def handle(self, webhook_body: str, sig_header: str):
        self._has_handled_events = True

        event_notif = self._client.parse_event_notification(
            webhook_body, sig_header, self._webhook_secret
        )

        # tie the client to the context of the event temporarily
        # there's probably a better way to do this
        original_context = self._client._requestor._options.stripe_context
        try:
            self._client._requestor._options.stripe_context = (
                event_notif.context
            )
            if event_notif.type in self._registered_handlers:
                self._registered_handlers[event_notif.type](
                    event_notif, self._client
                )
            # TODO: make sure this handles known-but-unregistered event types correctly; it should throw?
            # though, does that make migrations harder? Suddenly events are going to a new callback (potentially erroring) when they went to the catchall before
            # but in languages that care about types, the event won't come through as UnknownEventNotification, so we might have to do some casting??
            elif UNKNOWN_EVENT_TYPE_KEY in self._registered_handlers:
                self._registered_handlers[UNKNOWN_EVENT_TYPE_KEY](
                    event_notif, self._client
                )
            else:
                # TODO: raise here? open question `I`
                raise ValueError(
                    f'No handler registered for event of type "{event_notif.type}"'
                )
        finally:
            self._client._requestor._options.stripe_context = original_context

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

    def on_UnknownEventNotification(
        self, func: "Callable[[UnknownEventNotification, StripeClient], None]"
    ) -> None:
        """
        Registers a handler for unknown event notifications.
        """
        self._register(UNKNOWN_EVENT_TYPE_KEY, func)

    # event-handler-methods: The beginning of the section generated from our OpenAPI spec
    def on_V1BillingMeterErrorReportTriggeredEventNotification(
        self,
        func: "Callable[[V1BillingMeterErrorReportTriggeredEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V1BillingMeterErrorReportTriggeredEvent` (`v1.billing.meter.error_report_triggered`) event notification.
        """
        self._register(
            "v1.billing.meter.error_report_triggered",
            func,
        )

    def on_V1BillingMeterNoMeterFoundEventNotification(
        self,
        func: "Callable[[V1BillingMeterNoMeterFoundEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V1BillingMeterNoMeterFoundEvent` (`v1.billing.meter.no_meter_found`) event notification.
        """
        self._register(
            "v1.billing.meter.no_meter_found",
            func,
        )

    def on_V2CoreEventDestinationPingEventNotification(
        self,
        func: "Callable[[V2CoreEventDestinationPingEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreEventDestinationPingEvent` (`v2.core.event_destination.ping`) event notification.
        """
        self._register(
            "v2.core.event_destination.ping",
            func,
        )

    # event-handler-methods: The end of the section generated from our OpenAPI spec
