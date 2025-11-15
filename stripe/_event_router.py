from dataclasses import dataclass
from typing_extensions import TYPE_CHECKING

from typing import TypeVar, Callable

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
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_canceled_event import (
        V2PaymentsOffSessionPaymentCanceledEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_created_event import (
        V2PaymentsOffSessionPaymentCreatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_failed_event import (
        V2PaymentsOffSessionPaymentFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_requires_capture_event import (
        V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_succeeded_event import (
        V2PaymentsOffSessionPaymentSucceededEventNotification,
    )
    # event-notification-types: The end of the section generated from our OpenAPI spec

# internal type to represent any EventNotification subclass
EventNotificationChild = TypeVar(
    "EventNotificationChild", bound="EventNotification"
)


@dataclass
class UnhandledEventInfo:
    """
    A pile of information about to help user code respond to unhandled events.
    """

    known_event_type: bool


OnUnhandledHandler = Callable[
    [EventNotification, "StripeClient", UnhandledEventInfo], None
]


class EventRouter:
    def __init__(
        self,
        client: "StripeClient",
        webhook_secret: str,
        on_unhandled_handler: OnUnhandledHandler,
    ) -> None:
        self._registered_handlers = {}
        self._client = client
        self._webhook_secret = webhook_secret
        self._on_unhandled_handler = on_unhandled_handler
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
            else:
                self._on_unhandled_handler(
                    event_notif,
                    self._client,
                    UnhandledEventInfo(
                        known_event_type=isinstance(
                            event_notif, UnknownEventNotification
                        )
                    ),
                )

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

    def on_V2CoreAccountClosedEventNotification(
        self,
        func: "Callable[[V2CoreAccountClosedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountClosedEvent` (`v2.core.account.closed`) event notification.
        """
        self._register(
            "v2.core.account.closed",
            func,
        )

    def on_V2CoreAccountCreatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountCreatedEvent` (`v2.core.account.created`) event notification.
        """
        self._register(
            "v2.core.account.created",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.customer].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.customer].capability_status_updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationCustomerUpdatedEvent` (`v2.core.account[configuration.customer].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.customer].updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.merchant].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.merchant].capability_status_updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationMerchantUpdatedEvent` (`v2.core.account[configuration.merchant].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.merchant].updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.recipient].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.recipient].capability_status_updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationRecipientUpdatedEvent` (`v2.core.account[configuration.recipient].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.recipient].updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.storer].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.storer].capability_status_updated",
            func,
        )

    def on_V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` (`v2.core.account[configuration.storer].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.storer].updated",
            func,
        )

    def on_V2CoreAccountIncludingDefaultsUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingDefaultsUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingDefaultsUpdatedEvent` (`v2.core.account[defaults].updated`) event notification.
        """
        self._register(
            "v2.core.account[defaults].updated",
            func,
        )

    def on_V2CoreAccountIncludingIdentityUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingIdentityUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingIdentityUpdatedEvent` (`v2.core.account[identity].updated`) event notification.
        """
        self._register(
            "v2.core.account[identity].updated",
            func,
        )

    def on_V2CoreAccountIncludingRequirementsUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountIncludingRequirementsUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountIncludingRequirementsUpdatedEvent` (`v2.core.account[requirements].updated`) event notification.
        """
        self._register(
            "v2.core.account[requirements].updated",
            func,
        )

    def on_V2CoreAccountLinkReturnedEventNotification(
        self,
        func: "Callable[[V2CoreAccountLinkReturnedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountLinkReturnedEvent` (`v2.core.account_link.returned`) event notification.
        """
        self._register(
            "v2.core.account_link.returned",
            func,
        )

    def on_V2CoreAccountPersonCreatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountPersonCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountPersonCreatedEvent` (`v2.core.account_person.created`) event notification.
        """
        self._register(
            "v2.core.account_person.created",
            func,
        )

    def on_V2CoreAccountPersonDeletedEventNotification(
        self,
        func: "Callable[[V2CoreAccountPersonDeletedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountPersonDeletedEvent` (`v2.core.account_person.deleted`) event notification.
        """
        self._register(
            "v2.core.account_person.deleted",
            func,
        )

    def on_V2CoreAccountPersonUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountPersonUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountPersonUpdatedEvent` (`v2.core.account_person.updated`) event notification.
        """
        self._register(
            "v2.core.account_person.updated",
            func,
        )

    def on_V2CoreAccountUpdatedEventNotification(
        self,
        func: "Callable[[V2CoreAccountUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2CoreAccountUpdatedEvent` (`v2.core.account.updated`) event notification.
        """
        self._register(
            "v2.core.account.updated",
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

    def on_V2MoneyManagementAdjustmentCreatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementAdjustmentCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementAdjustmentCreatedEvent` (`v2.money_management.adjustment.created`) event notification.
        """
        self._register(
            "v2.money_management.adjustment.created",
            func,
        )

    def on_V2MoneyManagementFinancialAccountCreatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementFinancialAccountCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementFinancialAccountCreatedEvent` (`v2.money_management.financial_account.created`) event notification.
        """
        self._register(
            "v2.money_management.financial_account.created",
            func,
        )

    def on_V2MoneyManagementFinancialAccountUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementFinancialAccountUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementFinancialAccountUpdatedEvent` (`v2.money_management.financial_account.updated`) event notification.
        """
        self._register(
            "v2.money_management.financial_account.updated",
            func,
        )

    def on_V2MoneyManagementFinancialAddressActivatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementFinancialAddressActivatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementFinancialAddressActivatedEvent` (`v2.money_management.financial_address.activated`) event notification.
        """
        self._register(
            "v2.money_management.financial_address.activated",
            func,
        )

    def on_V2MoneyManagementFinancialAddressFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementFinancialAddressFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementFinancialAddressFailedEvent` (`v2.money_management.financial_address.failed`) event notification.
        """
        self._register(
            "v2.money_management.financial_address.failed",
            func,
        )

    def on_V2MoneyManagementInboundTransferAvailableEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferAvailableEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferAvailableEvent` (`v2.money_management.inbound_transfer.available`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.available",
            func,
        )

    def on_V2MoneyManagementInboundTransferBankDebitFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferBankDebitFailedEvent` (`v2.money_management.inbound_transfer.bank_debit_failed`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_failed",
            func,
        )

    def on_V2MoneyManagementInboundTransferBankDebitProcessingEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitProcessingEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferBankDebitProcessingEvent` (`v2.money_management.inbound_transfer.bank_debit_processing`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_processing",
            func,
        )

    def on_V2MoneyManagementInboundTransferBankDebitQueuedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitQueuedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferBankDebitQueuedEvent` (`v2.money_management.inbound_transfer.bank_debit_queued`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_queued",
            func,
        )

    def on_V2MoneyManagementInboundTransferBankDebitReturnedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitReturnedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferBankDebitReturnedEvent` (`v2.money_management.inbound_transfer.bank_debit_returned`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_returned",
            func,
        )

    def on_V2MoneyManagementInboundTransferBankDebitSucceededEventNotification(
        self,
        func: "Callable[[V2MoneyManagementInboundTransferBankDebitSucceededEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementInboundTransferBankDebitSucceededEvent` (`v2.money_management.inbound_transfer.bank_debit_succeeded`) event notification.
        """
        self._register(
            "v2.money_management.inbound_transfer.bank_debit_succeeded",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentCanceledEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentCanceledEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentCanceledEvent` (`v2.money_management.outbound_payment.canceled`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.canceled",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentCreatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentCreatedEvent` (`v2.money_management.outbound_payment.created`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.created",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentFailedEvent` (`v2.money_management.outbound_payment.failed`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.failed",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentPostedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentPostedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentPostedEvent` (`v2.money_management.outbound_payment.posted`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.posted",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentReturnedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentReturnedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentReturnedEvent` (`v2.money_management.outbound_payment.returned`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.returned",
            func,
        )

    def on_V2MoneyManagementOutboundPaymentUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundPaymentUpdatedEvent` (`v2.money_management.outbound_payment.updated`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.updated",
            func,
        )

    def on_V2MoneyManagementOutboundTransferCanceledEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferCanceledEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferCanceledEvent` (`v2.money_management.outbound_transfer.canceled`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.canceled",
            func,
        )

    def on_V2MoneyManagementOutboundTransferCreatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferCreatedEvent` (`v2.money_management.outbound_transfer.created`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.created",
            func,
        )

    def on_V2MoneyManagementOutboundTransferFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferFailedEvent` (`v2.money_management.outbound_transfer.failed`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.failed",
            func,
        )

    def on_V2MoneyManagementOutboundTransferPostedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferPostedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferPostedEvent` (`v2.money_management.outbound_transfer.posted`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.posted",
            func,
        )

    def on_V2MoneyManagementOutboundTransferReturnedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferReturnedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferReturnedEvent` (`v2.money_management.outbound_transfer.returned`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.returned",
            func,
        )

    def on_V2MoneyManagementOutboundTransferUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementOutboundTransferUpdatedEvent` (`v2.money_management.outbound_transfer.updated`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.updated",
            func,
        )

    def on_V2MoneyManagementPayoutMethodUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementPayoutMethodUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementPayoutMethodUpdatedEvent` (`v2.money_management.payout_method.updated`) event notification.
        """
        self._register(
            "v2.money_management.payout_method.updated",
            func,
        )

    def on_V2MoneyManagementReceivedCreditAvailableEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditAvailableEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedCreditAvailableEvent` (`v2.money_management.received_credit.available`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.available",
            func,
        )

    def on_V2MoneyManagementReceivedCreditFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedCreditFailedEvent` (`v2.money_management.received_credit.failed`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.failed",
            func,
        )

    def on_V2MoneyManagementReceivedCreditReturnedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditReturnedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedCreditReturnedEvent` (`v2.money_management.received_credit.returned`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.returned",
            func,
        )

    def on_V2MoneyManagementReceivedCreditSucceededEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedCreditSucceededEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedCreditSucceededEvent` (`v2.money_management.received_credit.succeeded`) event notification.
        """
        self._register(
            "v2.money_management.received_credit.succeeded",
            func,
        )

    def on_V2MoneyManagementReceivedDebitCanceledEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitCanceledEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedDebitCanceledEvent` (`v2.money_management.received_debit.canceled`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.canceled",
            func,
        )

    def on_V2MoneyManagementReceivedDebitFailedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedDebitFailedEvent` (`v2.money_management.received_debit.failed`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.failed",
            func,
        )

    def on_V2MoneyManagementReceivedDebitPendingEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitPendingEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedDebitPendingEvent` (`v2.money_management.received_debit.pending`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.pending",
            func,
        )

    def on_V2MoneyManagementReceivedDebitSucceededEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitSucceededEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedDebitSucceededEvent` (`v2.money_management.received_debit.succeeded`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.succeeded",
            func,
        )

    def on_V2MoneyManagementReceivedDebitUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementReceivedDebitUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementReceivedDebitUpdatedEvent` (`v2.money_management.received_debit.updated`) event notification.
        """
        self._register(
            "v2.money_management.received_debit.updated",
            func,
        )

    def on_V2MoneyManagementTransactionCreatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementTransactionCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementTransactionCreatedEvent` (`v2.money_management.transaction.created`) event notification.
        """
        self._register(
            "v2.money_management.transaction.created",
            func,
        )

    def on_V2MoneyManagementTransactionUpdatedEventNotification(
        self,
        func: "Callable[[V2MoneyManagementTransactionUpdatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2MoneyManagementTransactionUpdatedEvent` (`v2.money_management.transaction.updated`) event notification.
        """
        self._register(
            "v2.money_management.transaction.updated",
            func,
        )

    def on_V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent` (`v2.payments.off_session_payment.authorization_attempt_failed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.authorization_attempt_failed",
            func,
        )

    def on_V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent` (`v2.payments.off_session_payment.authorization_attempt_started`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.authorization_attempt_started",
            func,
        )

    def on_V2PaymentsOffSessionPaymentCanceledEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentCanceledEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentCanceledEvent` (`v2.payments.off_session_payment.canceled`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.canceled",
            func,
        )

    def on_V2PaymentsOffSessionPaymentCreatedEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentCreatedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentCreatedEvent` (`v2.payments.off_session_payment.created`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.created",
            func,
        )

    def on_V2PaymentsOffSessionPaymentFailedEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentFailedEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentFailedEvent` (`v2.payments.off_session_payment.failed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.failed",
            func,
        )

    def on_V2PaymentsOffSessionPaymentRequiresCaptureEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentRequiresCaptureEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentRequiresCaptureEvent` (`v2.payments.off_session_payment.requires_capture`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.requires_capture",
            func,
        )

    def on_V2PaymentsOffSessionPaymentSucceededEventNotification(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentSucceededEventNotification, StripeClient], None]",
    ) -> None:
        """
        Registers a handler for the `V2PaymentsOffSessionPaymentSucceededEvent` (`v2.payments.off_session_payment.succeeded`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.succeeded",
            func,
        )

    # event-handler-methods: The end of the section generated from our OpenAPI spec
