from typing_extensions import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Callable
    from stripe._stripe_client import StripeClient

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


class EventHandler:
    def __init__(self, client: "StripeClient", webhook_secret: str) -> None:
        self._registered_handlers = {}
        self._client = client
        self._webhook_secret = webhook_secret

    def handle(self, webhook_body: str, sig_header: str):
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
            elif "__other" in self._registered_handlers:
                self._registered_handlers["__other"](event_notif, self._client)
            else:
                # TODO: raise here? open question `I`
                raise ValueError(
                    f'No handler registered for event of type "{event_notif.type}"'
                )
        finally:
            self._client._requestor._options.stripe_context = original_context

    # event-handler-methods: The beginning of the section generated from our OpenAPI spec
    def on_V1BillingMeterErrorReportTriggeredEventNotification(
        self,
        func: "Callable[[V1BillingMeterErrorReportTriggeredEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the V1BillingMeterErrorReportTriggeredEvent event notification.
        """
        if (
            "v1.billing.meter.error_report_triggered"
            in self._registered_handlers
        ):
            raise ValueError(
                'Handler for "v1.billing.meter.error_report_triggered" already registered.'
            )

        self._registered_handlers[
            "v1.billing.meter.error_report_triggered"
        ] = func

    def on_V1BillingMeterNoMeterFoundEventNotification(
        self,
        func: "Callable[[V1BillingMeterNoMeterFoundEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the V1BillingMeterNoMeterFoundEvent event notification.
        """
        if "v1.billing.meter.no_meter_found" in self._registered_handlers:
            raise ValueError(
                'Handler for "v1.billing.meter.no_meter_found" already registered.'
            )

        self._registered_handlers["v1.billing.meter.no_meter_found"] = func

    def on_V2CoreEventDestinationPingEventNotification(
        self,
        func: "Callable[[V2CoreEventDestinationPingEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the V2CoreEventDestinationPingEvent event notification.
        """
        if "v2.core.event_destination.ping" in self._registered_handlers:
            raise ValueError(
                'Handler for "v2.core.event_destination.ping" already registered.'
            )

        self._registered_handlers["v2.core.event_destination.ping"] = func

    # event-handler-methods: The end of the section generated from our OpenAPI spec
