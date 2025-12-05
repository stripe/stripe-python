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
    from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
        V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEventNotification,
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
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_money_management_adjustment_created_event import (
        V2MoneyManagementAdjustmentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_created_event import (
        V2MoneyManagementFinancialAccountCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_updated_event import (
        V2MoneyManagementFinancialAccountUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_activated_event import (
        V2MoneyManagementFinancialAddressActivatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_failed_event import (
        V2MoneyManagementFinancialAddressFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_available_event import (
        V2MoneyManagementInboundTransferAvailableEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
        V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
        V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
        V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
        V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
        V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_canceled_event import (
        V2MoneyManagementOutboundPaymentCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_created_event import (
        V2MoneyManagementOutboundPaymentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_failed_event import (
        V2MoneyManagementOutboundPaymentFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_posted_event import (
        V2MoneyManagementOutboundPaymentPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_returned_event import (
        V2MoneyManagementOutboundPaymentReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_updated_event import (
        V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
        V2MoneyManagementOutboundTransferCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_created_event import (
        V2MoneyManagementOutboundTransferCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_failed_event import (
        V2MoneyManagementOutboundTransferFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_posted_event import (
        V2MoneyManagementOutboundTransferPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_returned_event import (
        V2MoneyManagementOutboundTransferReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_updated_event import (
        V2MoneyManagementOutboundTransferUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_updated_event import (
        V2MoneyManagementPayoutMethodUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_available_event import (
        V2MoneyManagementReceivedCreditAvailableEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_failed_event import (
        V2MoneyManagementReceivedCreditFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_returned_event import (
        V2MoneyManagementReceivedCreditReturnedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_succeeded_event import (
        V2MoneyManagementReceivedCreditSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_canceled_event import (
        V2MoneyManagementReceivedDebitCanceledEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_failed_event import (
        V2MoneyManagementReceivedDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_pending_event import (
        V2MoneyManagementReceivedDebitPendingEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_succeeded_event import (
        V2MoneyManagementReceivedDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_updated_event import (
        V2MoneyManagementReceivedDebitUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEventNotification,
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


class StripeEventNotificationHandler:
    def __init__(
        self,
        client: "StripeClient",
        webhook_secret: str,
        fallback_callback: FallbackCallback,
    ) -> None:
        self._registered_handlers = {}
        self._client = client
        self._webhook_secret = webhook_secret
        self.fallback_callback = fallback_callback
        # once this is true, adding additional handlers results in an error
        self._has_handled_events = False

    def handle(self, webhook_body: str, sig_header: str):
        # isn't thread-safe, but we expect these to get registered synchronously at startup
        self._has_handled_events = True

        event_notif = self._client.parse_event_notification(
            webhook_body, sig_header, self._webhook_secret
        )

        # Create a new client with the event's context.
        # This is thread-safe since we're not modifying the original client.
        # The new client reuses the HTTP client to avoid TLS handshake overhead.
        client_with_event_context = self._client.with_context(
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

    def on_v2_core_account_including_configuration_storer_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.storer].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.storer].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_storer_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` (`v2.core.account[configuration.storer].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.storer].updated",
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

    def on_v2_core_health_event_generation_failure_resolved(
        self,
        func: "Callable[[V2CoreHealthEventGenerationFailureResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthEventGenerationFailureResolvedEvent` (`v2.core.health.event_generation_failure.resolved`) event notification.
        """
        self._register(
            "v2.core.health.event_generation_failure.resolved",
            func,
        )
        return func

    def on_v2_money_management_adjustment_created(
        self,
        func: "Callable[[V2MoneyManagementAdjustmentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementAdjustmentCreatedEvent` (`v2.money_management.adjustment.created`) event notification.
        """
        self._register(
            "v2.money_management.adjustment.created",
            func,
        )
        return func

    def on_v2_money_management_financial_account_created(
        self,
        func: "Callable[[V2MoneyManagementFinancialAccountCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementFinancialAccountCreatedEvent` (`v2.money_management.financial_account.created`) event notification.
        """
        self._register(
            "v2.money_management.financial_account.created",
            func,
        )
        return func

    def on_v2_money_management_financial_account_updated(
        self,
        func: "Callable[[V2MoneyManagementFinancialAccountUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementFinancialAccountUpdatedEvent` (`v2.money_management.financial_account.updated`) event notification.
        """
        self._register(
            "v2.money_management.financial_account.updated",
            func,
        )
        return func

    def on_v2_money_management_financial_address_activated(
        self,
        func: "Callable[[V2MoneyManagementFinancialAddressActivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementFinancialAddressActivatedEvent` (`v2.money_management.financial_address.activated`) event notification.
        """
        self._register(
            "v2.money_management.financial_address.activated",
            func,
        )
        return func

    def on_v2_money_management_financial_address_failed(
        self,
        func: "Callable[[V2MoneyManagementFinancialAddressFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementFinancialAddressFailedEvent` (`v2.money_management.financial_address.failed`) event notification.
        """
        self._register(
            "v2.money_management.financial_address.failed",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_available(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferAvailableEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferAvailableEvent` (`v2.money_management.inbound_transfer.available`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.available",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_bank_debit_failed(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferBankDebitFailedEvent` (`v2.money_management.inbound_transfer.bank_debit_failed`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_failed",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_bank_debit_processing(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitProcessingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferBankDebitProcessingEvent` (`v2.money_management.inbound_transfer.bank_debit_processing`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_processing",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_bank_debit_queued(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitQueuedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferBankDebitQueuedEvent` (`v2.money_management.inbound_transfer.bank_debit_queued`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_queued",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_bank_debit_returned(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitReturnedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferBankDebitReturnedEvent` (`v2.money_management.inbound_transfer.bank_debit_returned`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_returned",
            func,
        )
        return func

    def on_v2_money_management_inbound_transfer_bank_debit_succeeded(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementInboundTransferBankDebitSucceededEvent` (`v2.money_management.inbound_transfer.bank_debit_succeeded`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_succeeded",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_canceled(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentCanceledEvent` (`v2.money_management.outbound_payment.canceled`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.canceled",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_created(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentCreatedEvent` (`v2.money_management.outbound_payment.created`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.created",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_failed(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentFailedEvent` (`v2.money_management.outbound_payment.failed`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.failed",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_posted(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentPostedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentPostedEvent` (`v2.money_management.outbound_payment.posted`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.posted",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_returned(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentReturnedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentReturnedEvent` (`v2.money_management.outbound_payment.returned`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.returned",
            func,
        )
        return func

    def on_v2_money_management_outbound_payment_updated(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentUpdatedEvent` (`v2.money_management.outbound_payment.updated`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.updated",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_canceled(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferCanceledEvent` (`v2.money_management.outbound_transfer.canceled`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.canceled",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_created(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferCreatedEvent` (`v2.money_management.outbound_transfer.created`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.created",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_failed(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferFailedEvent` (`v2.money_management.outbound_transfer.failed`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.failed",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_posted(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferPostedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferPostedEvent` (`v2.money_management.outbound_transfer.posted`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.posted",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_returned(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferReturnedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferReturnedEvent` (`v2.money_management.outbound_transfer.returned`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.returned",
            func,
        )
        return func

    def on_v2_money_management_outbound_transfer_updated(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferUpdatedEvent` (`v2.money_management.outbound_transfer.updated`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.updated",
            func,
        )
        return func

    def on_v2_money_management_payout_method_updated(
        self,
        func: "Callable[[V2MoneyManagementPayoutMethodUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementPayoutMethodUpdatedEvent` (`v2.money_management.payout_method.updated`) event notification.
        """
        self._register(
            "v2.money_management.payout_method.updated",
            func,
        )
        return func

    def on_v2_money_management_received_credit_available(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditAvailableEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedCreditAvailableEvent` (`v2.money_management.received_credit.available`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.available",
            func,
        )
        return func

    def on_v2_money_management_received_credit_failed(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedCreditFailedEvent` (`v2.money_management.received_credit.failed`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.failed",
            func,
        )
        return func

    def on_v2_money_management_received_credit_returned(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditReturnedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedCreditReturnedEvent` (`v2.money_management.received_credit.returned`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.returned",
            func,
        )
        return func

    def on_v2_money_management_received_credit_succeeded(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedCreditSucceededEvent` (`v2.money_management.received_credit.succeeded`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.succeeded",
            func,
        )
        return func

    def on_v2_money_management_received_debit_canceled(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedDebitCanceledEvent` (`v2.money_management.received_debit.canceled`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.canceled",
            func,
        )
        return func

    def on_v2_money_management_received_debit_failed(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedDebitFailedEvent` (`v2.money_management.received_debit.failed`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.failed",
            func,
        )
        return func

    def on_v2_money_management_received_debit_pending(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitPendingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedDebitPendingEvent` (`v2.money_management.received_debit.pending`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.pending",
            func,
        )
        return func

    def on_v2_money_management_received_debit_succeeded(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedDebitSucceededEvent` (`v2.money_management.received_debit.succeeded`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.succeeded",
            func,
        )
        return func

    def on_v2_money_management_received_debit_updated(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementReceivedDebitUpdatedEvent` (`v2.money_management.received_debit.updated`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.updated",
            func,
        )
        return func

    def on_v2_money_management_transaction_created(
        self,
        func: "Callable[[V2MoneyManagementTransactionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementTransactionCreatedEvent` (`v2.money_management.transaction.created`) event notification.
        """
        self._register(
            "v2.money_management.transaction.created",
            func,
        )
        return func

    def on_v2_money_management_transaction_updated(
        self,
        func: "Callable[[V2MoneyManagementTransactionUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementTransactionUpdatedEvent` (`v2.money_management.transaction.updated`) event notification.
        """
        self._register(
            "v2.money_management.transaction.updated",
            func,
        )
        return func

    # event-notification-registration-methods: The end of the section generated from our OpenAPI spec
