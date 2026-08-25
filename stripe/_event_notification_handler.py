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
from stripe._webhook import WebhookPayload

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
    from stripe.events._v2_core_account_including_configuration_money_manager_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_money_manager_updated_event import (
        V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEventNotification,
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
    from stripe.events._v2_core_batch_job_batch_failed_event import (
        V2CoreBatchJobBatchFailedEventNotification,
    )
    from stripe.events._v2_core_batch_job_canceled_event import (
        V2CoreBatchJobCanceledEventNotification,
    )
    from stripe.events._v2_core_batch_job_completed_event import (
        V2CoreBatchJobCompletedEventNotification,
    )
    from stripe.events._v2_core_batch_job_created_event import (
        V2CoreBatchJobCreatedEventNotification,
    )
    from stripe.events._v2_core_batch_job_ready_for_upload_event import (
        V2CoreBatchJobReadyForUploadEventNotification,
    )
    from stripe.events._v2_core_batch_job_timeout_event import (
        V2CoreBatchJobTimeoutEventNotification,
    )
    from stripe.events._v2_core_batch_job_updated_event import (
        V2CoreBatchJobUpdatedEventNotification,
    )
    from stripe.events._v2_core_batch_job_upload_timeout_event import (
        V2CoreBatchJobUploadTimeoutEventNotification,
    )
    from stripe.events._v2_core_batch_job_validating_event import (
        V2CoreBatchJobValidatingEventNotification,
    )
    from stripe.events._v2_core_batch_job_validation_failed_event import (
        V2CoreBatchJobValidationFailedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_data_reporting_query_run_created_event import (
        V2DataReportingQueryRunCreatedEventNotification,
    )
    from stripe.events._v2_data_reporting_query_run_failed_event import (
        V2DataReportingQueryRunFailedEventNotification,
    )
    from stripe.events._v2_data_reporting_query_run_succeeded_event import (
        V2DataReportingQueryRunSucceededEventNotification,
    )
    from stripe.events._v2_data_reporting_query_run_updated_event import (
        V2DataReportingQueryRunUpdatedEventNotification,
    )
    from stripe.events._v2_extend_workflow_run_failed_event import (
        V2ExtendWorkflowRunFailedEventNotification,
    )
    from stripe.events._v2_extend_workflow_run_started_event import (
        V2ExtendWorkflowRunStartedEventNotification,
    )
    from stripe.events._v2_extend_workflow_run_succeeded_event import (
        V2ExtendWorkflowRunSucceededEventNotification,
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
    from stripe.events._v2_money_management_outbound_payment_under_review_event import (
        V2MoneyManagementOutboundPaymentUnderReviewEventNotification,
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
    from stripe.events._v2_money_management_outbound_transfer_under_review_event import (
        V2MoneyManagementOutboundTransferUnderReviewEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_updated_event import (
        V2MoneyManagementOutboundTransferUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_created_event import (
        V2MoneyManagementPayoutMethodCreatedEventNotification,
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
    from stripe.events._v2_orchestrated_commerce_agreement_confirmed_event import (
        V2OrchestratedCommerceAgreementConfirmedEventNotification,
    )
    from stripe.events._v2_orchestrated_commerce_agreement_created_event import (
        V2OrchestratedCommerceAgreementCreatedEventNotification,
    )
    from stripe.events._v2_orchestrated_commerce_agreement_partially_confirmed_event import (
        V2OrchestratedCommerceAgreementPartiallyConfirmedEventNotification,
    )
    from stripe.events._v2_orchestrated_commerce_agreement_terminated_event import (
        V2OrchestratedCommerceAgreementTerminatedEventNotification,
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

    def on_v2_core_account_including_configuration_money_manager_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.money_manager].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.money_manager].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_money_manager_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEvent` (`v2.core.account[configuration.money_manager].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.money_manager].updated",
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

    def on_v2_core_batch_job_batch_failed(
        self,
        func: "Callable[[V2CoreBatchJobBatchFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobBatchFailedEvent` (`v2.core.batch_job.batch_failed`) event notification.
        """
        self._register(
            "v2.core.batch_job.batch_failed",
            func,
        )
        return func

    def on_v2_core_batch_job_canceled(
        self,
        func: "Callable[[V2CoreBatchJobCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobCanceledEvent` (`v2.core.batch_job.canceled`) event notification.
        """
        self._register(
            "v2.core.batch_job.canceled",
            func,
        )
        return func

    def on_v2_core_batch_job_completed(
        self,
        func: "Callable[[V2CoreBatchJobCompletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobCompletedEvent` (`v2.core.batch_job.completed`) event notification.
        """
        self._register(
            "v2.core.batch_job.completed",
            func,
        )
        return func

    def on_v2_core_batch_job_created(
        self,
        func: "Callable[[V2CoreBatchJobCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobCreatedEvent` (`v2.core.batch_job.created`) event notification.
        """
        self._register(
            "v2.core.batch_job.created",
            func,
        )
        return func

    def on_v2_core_batch_job_ready_for_upload(
        self,
        func: "Callable[[V2CoreBatchJobReadyForUploadEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobReadyForUploadEvent` (`v2.core.batch_job.ready_for_upload`) event notification.
        """
        self._register(
            "v2.core.batch_job.ready_for_upload",
            func,
        )
        return func

    def on_v2_core_batch_job_timeout(
        self,
        func: "Callable[[V2CoreBatchJobTimeoutEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobTimeoutEvent` (`v2.core.batch_job.timeout`) event notification.
        """
        self._register(
            "v2.core.batch_job.timeout",
            func,
        )
        return func

    def on_v2_core_batch_job_updated(
        self,
        func: "Callable[[V2CoreBatchJobUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobUpdatedEvent` (`v2.core.batch_job.updated`) event notification.
        """
        self._register(
            "v2.core.batch_job.updated",
            func,
        )
        return func

    def on_v2_core_batch_job_upload_timeout(
        self,
        func: "Callable[[V2CoreBatchJobUploadTimeoutEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobUploadTimeoutEvent` (`v2.core.batch_job.upload_timeout`) event notification.
        """
        self._register(
            "v2.core.batch_job.upload_timeout",
            func,
        )
        return func

    def on_v2_core_batch_job_validating(
        self,
        func: "Callable[[V2CoreBatchJobValidatingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobValidatingEvent` (`v2.core.batch_job.validating`) event notification.
        """
        self._register(
            "v2.core.batch_job.validating",
            func,
        )
        return func

    def on_v2_core_batch_job_validation_failed(
        self,
        func: "Callable[[V2CoreBatchJobValidationFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreBatchJobValidationFailedEvent` (`v2.core.batch_job.validation_failed`) event notification.
        """
        self._register(
            "v2.core.batch_job.validation_failed",
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

    def on_v2_data_reporting_query_run_created(
        self,
        func: "Callable[[V2DataReportingQueryRunCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2DataReportingQueryRunCreatedEvent` (`v2.data.reporting.query_run.created`) event notification.
        """
        self._register(
            "v2.data.reporting.query_run.created",
            func,
        )
        return func

    def on_v2_data_reporting_query_run_failed(
        self,
        func: "Callable[[V2DataReportingQueryRunFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2DataReportingQueryRunFailedEvent` (`v2.data.reporting.query_run.failed`) event notification.
        """
        self._register(
            "v2.data.reporting.query_run.failed",
            func,
        )
        return func

    def on_v2_data_reporting_query_run_succeeded(
        self,
        func: "Callable[[V2DataReportingQueryRunSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2DataReportingQueryRunSucceededEvent` (`v2.data.reporting.query_run.succeeded`) event notification.
        """
        self._register(
            "v2.data.reporting.query_run.succeeded",
            func,
        )
        return func

    def on_v2_data_reporting_query_run_updated(
        self,
        func: "Callable[[V2DataReportingQueryRunUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2DataReportingQueryRunUpdatedEvent` (`v2.data.reporting.query_run.updated`) event notification.
        """
        self._register(
            "v2.data.reporting.query_run.updated",
            func,
        )
        return func

    def on_v2_extend_workflow_run_failed(
        self,
        func: "Callable[[V2ExtendWorkflowRunFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ExtendWorkflowRunFailedEvent` (`v2.extend.workflow_run.failed`) event notification.
        """
        self._register(
            "v2.extend.workflow_run.failed",
            func,
        )
        return func

    def on_v2_extend_workflow_run_started(
        self,
        func: "Callable[[V2ExtendWorkflowRunStartedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ExtendWorkflowRunStartedEvent` (`v2.extend.workflow_run.started`) event notification.
        """
        self._register(
            "v2.extend.workflow_run.started",
            func,
        )
        return func

    def on_v2_extend_workflow_run_succeeded(
        self,
        func: "Callable[[V2ExtendWorkflowRunSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ExtendWorkflowRunSucceededEvent` (`v2.extend.workflow_run.succeeded`) event notification.
        """
        self._register(
            "v2.extend.workflow_run.succeeded",
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

    def on_v2_money_management_outbound_payment_under_review(
        self,
        func: "Callable[[V2MoneyManagementOutboundPaymentUnderReviewEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundPaymentUnderReviewEvent` (`v2.money_management.outbound_payment.under_review`) event notification.
        """
        self._register(
            "v2.money_management.outbound_payment.under_review",
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

    def on_v2_money_management_outbound_transfer_under_review(
        self,
        func: "Callable[[V2MoneyManagementOutboundTransferUnderReviewEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementOutboundTransferUnderReviewEvent` (`v2.money_management.outbound_transfer.under_review`) event notification.
        """
        self._register(
            "v2.money_management.outbound_transfer.under_review",
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

    def on_v2_money_management_payout_method_created(
        self,
        func: "Callable[[V2MoneyManagementPayoutMethodCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementPayoutMethodCreatedEvent` (`v2.money_management.payout_method.created`) event notification.
        """
        self._register(
            "v2.money_management.payout_method.created",
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

    def on_v2_orchestrated_commerce_agreement_confirmed(
        self,
        func: "Callable[[V2OrchestratedCommerceAgreementConfirmedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2OrchestratedCommerceAgreementConfirmedEvent` (`v2.orchestrated_commerce.agreement.confirmed`) event notification.
        """
        self._register(
            "v2.orchestrated_commerce.agreement.confirmed",
            func,
        )
        return func

    def on_v2_orchestrated_commerce_agreement_created(
        self,
        func: "Callable[[V2OrchestratedCommerceAgreementCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2OrchestratedCommerceAgreementCreatedEvent` (`v2.orchestrated_commerce.agreement.created`) event notification.
        """
        self._register(
            "v2.orchestrated_commerce.agreement.created",
            func,
        )
        return func

    def on_v2_orchestrated_commerce_agreement_partially_confirmed(
        self,
        func: "Callable[[V2OrchestratedCommerceAgreementPartiallyConfirmedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent` (`v2.orchestrated_commerce.agreement.partially_confirmed`) event notification.
        """
        self._register(
            "v2.orchestrated_commerce.agreement.partially_confirmed",
            func,
        )
        return func

    def on_v2_orchestrated_commerce_agreement_terminated(
        self,
        func: "Callable[[V2OrchestratedCommerceAgreementTerminatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2OrchestratedCommerceAgreementTerminatedEvent` (`v2.orchestrated_commerce.agreement.terminated`) event notification.
        """
        self._register(
            "v2.orchestrated_commerce.agreement.terminated",
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
        webhook_secret: Optional[str],
        fallback_callback: FallbackCallback,
    ) -> None:
        """`webhook_secret` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `ValueError` if a secret is not provided."""
        super().__init__(client, fallback_callback)
        if not webhook_secret:
            raise ValueError("webhook_secret must be a non-empty string")
        self._webhook_secret = webhook_secret

    def handle(self, webhook_body: WebhookPayload, sig_header: Optional[str]):
        """
        Process an incoming webhook, routing it to the correct registered callback (or your fallback).

        `sig_header` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if a signature is not provided.
        """
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

    def handle(self, webhook_body: WebhookPayload):
        """
        Process an incoming webhook, routing it to the correct registered callback (or your fallback) without signature verification.
        """
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
        webhook_secret: Optional[str],
        fallback_callback: AsyncFallbackCallback,
    ) -> None:
        """`webhook_secret` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `ValueError` if a secret is not provided."""
        super().__init__(client, fallback_callback)
        if not webhook_secret:
            raise ValueError("webhook_secret must be a non-empty string")
        self._webhook_secret = webhook_secret

    async def handle_async(
        self, webhook_body: WebhookPayload, sig_header: Optional[str]
    ):
        """
        Process an incoming webhook, routing it to the correct registered callback (or your fallback).

        `sig_header` is only marked as `Optional` so it plays nicely with the types commonly returned from web frameworks. This raises a `SignatureVerificationError` if a signature is not provided.
        """
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

    async def handle_async(self, webhook_body: WebhookPayload):
        """
        Process an incoming webhook, routing it to the correct registered callback (or your fallback) without signature verification.
        """
        self._has_handled_events = True

        event_notif = (
            self._client.parse_event_notification_without_verification(
                webhook_body
            )
        )

        await self._dispatch_async(event_notif)
