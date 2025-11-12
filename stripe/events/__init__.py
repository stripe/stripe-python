# -*- coding: utf-8 -*-

from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import (
    UnknownEventNotification as UnknownEventNotification,
)


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.events._event_classes import (
        ALL_EVENT_NOTIFICATIONS as ALL_EVENT_NOTIFICATIONS,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEvent as V1BillingMeterErrorReportTriggeredEvent,
        V1BillingMeterErrorReportTriggeredEventNotification as V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEvent as V1BillingMeterNoMeterFoundEvent,
        V1BillingMeterNoMeterFoundEventNotification as V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEvent as V2CoreAccountClosedEvent,
        V2CoreAccountClosedEventNotification as V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEvent as V2CoreAccountCreatedEvent,
        V2CoreAccountCreatedEventNotification as V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
        V2CoreAccountIncludingConfigurationCustomerUpdatedEvent as V2CoreAccountIncludingConfigurationCustomerUpdatedEvent,
        V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification as V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
        V2CoreAccountIncludingConfigurationMerchantUpdatedEvent as V2CoreAccountIncludingConfigurationMerchantUpdatedEvent,
        V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification as V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
        V2CoreAccountIncludingConfigurationRecipientUpdatedEvent as V2CoreAccountIncludingConfigurationRecipientUpdatedEvent,
        V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification as V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent as V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent,
        V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification as V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
        V2CoreAccountIncludingConfigurationStorerUpdatedEvent as V2CoreAccountIncludingConfigurationStorerUpdatedEvent,
        V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification as V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEvent as V2CoreAccountIncludingDefaultsUpdatedEvent,
        V2CoreAccountIncludingDefaultsUpdatedEventNotification as V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_identity_updated_event import (
        V2CoreAccountIncludingIdentityUpdatedEvent as V2CoreAccountIncludingIdentityUpdatedEvent,
        V2CoreAccountIncludingIdentityUpdatedEventNotification as V2CoreAccountIncludingIdentityUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_requirements_updated_event import (
        V2CoreAccountIncludingRequirementsUpdatedEvent as V2CoreAccountIncludingRequirementsUpdatedEvent,
        V2CoreAccountIncludingRequirementsUpdatedEventNotification as V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_link_returned_event import (
        V2CoreAccountLinkReturnedEvent as V2CoreAccountLinkReturnedEvent,
        V2CoreAccountLinkReturnedEventNotification as V2CoreAccountLinkReturnedEventNotification,
    )
    from stripe.events._v2_core_account_person_created_event import (
        V2CoreAccountPersonCreatedEvent as V2CoreAccountPersonCreatedEvent,
        V2CoreAccountPersonCreatedEventNotification as V2CoreAccountPersonCreatedEventNotification,
    )
    from stripe.events._v2_core_account_person_deleted_event import (
        V2CoreAccountPersonDeletedEvent as V2CoreAccountPersonDeletedEvent,
        V2CoreAccountPersonDeletedEventNotification as V2CoreAccountPersonDeletedEventNotification,
    )
    from stripe.events._v2_core_account_person_updated_event import (
        V2CoreAccountPersonUpdatedEvent as V2CoreAccountPersonUpdatedEvent,
        V2CoreAccountPersonUpdatedEventNotification as V2CoreAccountPersonUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEvent as V2CoreAccountUpdatedEvent,
        V2CoreAccountUpdatedEventNotification as V2CoreAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEvent as V2CoreEventDestinationPingEvent,
        V2CoreEventDestinationPingEventNotification as V2CoreEventDestinationPingEventNotification,
    )
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEvent as V2CoreHealthEventGenerationFailureResolvedEvent,
        V2CoreHealthEventGenerationFailureResolvedEventNotification as V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_money_management_adjustment_created_event import (
        V2MoneyManagementAdjustmentCreatedEvent as V2MoneyManagementAdjustmentCreatedEvent,
        V2MoneyManagementAdjustmentCreatedEventNotification as V2MoneyManagementAdjustmentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_created_event import (
        V2MoneyManagementFinancialAccountCreatedEvent as V2MoneyManagementFinancialAccountCreatedEvent,
        V2MoneyManagementFinancialAccountCreatedEventNotification as V2MoneyManagementFinancialAccountCreatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_account_updated_event import (
        V2MoneyManagementFinancialAccountUpdatedEvent as V2MoneyManagementFinancialAccountUpdatedEvent,
        V2MoneyManagementFinancialAccountUpdatedEventNotification as V2MoneyManagementFinancialAccountUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_activated_event import (
        V2MoneyManagementFinancialAddressActivatedEvent as V2MoneyManagementFinancialAddressActivatedEvent,
        V2MoneyManagementFinancialAddressActivatedEventNotification as V2MoneyManagementFinancialAddressActivatedEventNotification,
    )
    from stripe.events._v2_money_management_financial_address_failed_event import (
        V2MoneyManagementFinancialAddressFailedEvent as V2MoneyManagementFinancialAddressFailedEvent,
        V2MoneyManagementFinancialAddressFailedEventNotification as V2MoneyManagementFinancialAddressFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_available_event import (
        V2MoneyManagementInboundTransferAvailableEvent as V2MoneyManagementInboundTransferAvailableEvent,
        V2MoneyManagementInboundTransferAvailableEventNotification as V2MoneyManagementInboundTransferAvailableEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
        V2MoneyManagementInboundTransferBankDebitFailedEvent as V2MoneyManagementInboundTransferBankDebitFailedEvent,
        V2MoneyManagementInboundTransferBankDebitFailedEventNotification as V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
        V2MoneyManagementInboundTransferBankDebitProcessingEvent as V2MoneyManagementInboundTransferBankDebitProcessingEvent,
        V2MoneyManagementInboundTransferBankDebitProcessingEventNotification as V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
        V2MoneyManagementInboundTransferBankDebitQueuedEvent as V2MoneyManagementInboundTransferBankDebitQueuedEvent,
        V2MoneyManagementInboundTransferBankDebitQueuedEventNotification as V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
        V2MoneyManagementInboundTransferBankDebitReturnedEvent as V2MoneyManagementInboundTransferBankDebitReturnedEvent,
        V2MoneyManagementInboundTransferBankDebitReturnedEventNotification as V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    )
    from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
        V2MoneyManagementInboundTransferBankDebitSucceededEvent as V2MoneyManagementInboundTransferBankDebitSucceededEvent,
        V2MoneyManagementInboundTransferBankDebitSucceededEventNotification as V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_canceled_event import (
        V2MoneyManagementOutboundPaymentCanceledEvent as V2MoneyManagementOutboundPaymentCanceledEvent,
        V2MoneyManagementOutboundPaymentCanceledEventNotification as V2MoneyManagementOutboundPaymentCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_created_event import (
        V2MoneyManagementOutboundPaymentCreatedEvent as V2MoneyManagementOutboundPaymentCreatedEvent,
        V2MoneyManagementOutboundPaymentCreatedEventNotification as V2MoneyManagementOutboundPaymentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_failed_event import (
        V2MoneyManagementOutboundPaymentFailedEvent as V2MoneyManagementOutboundPaymentFailedEvent,
        V2MoneyManagementOutboundPaymentFailedEventNotification as V2MoneyManagementOutboundPaymentFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_posted_event import (
        V2MoneyManagementOutboundPaymentPostedEvent as V2MoneyManagementOutboundPaymentPostedEvent,
        V2MoneyManagementOutboundPaymentPostedEventNotification as V2MoneyManagementOutboundPaymentPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_returned_event import (
        V2MoneyManagementOutboundPaymentReturnedEvent as V2MoneyManagementOutboundPaymentReturnedEvent,
        V2MoneyManagementOutboundPaymentReturnedEventNotification as V2MoneyManagementOutboundPaymentReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_updated_event import (
        V2MoneyManagementOutboundPaymentUpdatedEvent as V2MoneyManagementOutboundPaymentUpdatedEvent,
        V2MoneyManagementOutboundPaymentUpdatedEventNotification as V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
        V2MoneyManagementOutboundTransferCanceledEvent as V2MoneyManagementOutboundTransferCanceledEvent,
        V2MoneyManagementOutboundTransferCanceledEventNotification as V2MoneyManagementOutboundTransferCanceledEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_created_event import (
        V2MoneyManagementOutboundTransferCreatedEvent as V2MoneyManagementOutboundTransferCreatedEvent,
        V2MoneyManagementOutboundTransferCreatedEventNotification as V2MoneyManagementOutboundTransferCreatedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_failed_event import (
        V2MoneyManagementOutboundTransferFailedEvent as V2MoneyManagementOutboundTransferFailedEvent,
        V2MoneyManagementOutboundTransferFailedEventNotification as V2MoneyManagementOutboundTransferFailedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_posted_event import (
        V2MoneyManagementOutboundTransferPostedEvent as V2MoneyManagementOutboundTransferPostedEvent,
        V2MoneyManagementOutboundTransferPostedEventNotification as V2MoneyManagementOutboundTransferPostedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_returned_event import (
        V2MoneyManagementOutboundTransferReturnedEvent as V2MoneyManagementOutboundTransferReturnedEvent,
        V2MoneyManagementOutboundTransferReturnedEventNotification as V2MoneyManagementOutboundTransferReturnedEventNotification,
    )
    from stripe.events._v2_money_management_outbound_transfer_updated_event import (
        V2MoneyManagementOutboundTransferUpdatedEvent as V2MoneyManagementOutboundTransferUpdatedEvent,
        V2MoneyManagementOutboundTransferUpdatedEventNotification as V2MoneyManagementOutboundTransferUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_updated_event import (
        V2MoneyManagementPayoutMethodUpdatedEvent as V2MoneyManagementPayoutMethodUpdatedEvent,
        V2MoneyManagementPayoutMethodUpdatedEventNotification as V2MoneyManagementPayoutMethodUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_available_event import (
        V2MoneyManagementReceivedCreditAvailableEvent as V2MoneyManagementReceivedCreditAvailableEvent,
        V2MoneyManagementReceivedCreditAvailableEventNotification as V2MoneyManagementReceivedCreditAvailableEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_failed_event import (
        V2MoneyManagementReceivedCreditFailedEvent as V2MoneyManagementReceivedCreditFailedEvent,
        V2MoneyManagementReceivedCreditFailedEventNotification as V2MoneyManagementReceivedCreditFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_returned_event import (
        V2MoneyManagementReceivedCreditReturnedEvent as V2MoneyManagementReceivedCreditReturnedEvent,
        V2MoneyManagementReceivedCreditReturnedEventNotification as V2MoneyManagementReceivedCreditReturnedEventNotification,
    )
    from stripe.events._v2_money_management_received_credit_succeeded_event import (
        V2MoneyManagementReceivedCreditSucceededEvent as V2MoneyManagementReceivedCreditSucceededEvent,
        V2MoneyManagementReceivedCreditSucceededEventNotification as V2MoneyManagementReceivedCreditSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_canceled_event import (
        V2MoneyManagementReceivedDebitCanceledEvent as V2MoneyManagementReceivedDebitCanceledEvent,
        V2MoneyManagementReceivedDebitCanceledEventNotification as V2MoneyManagementReceivedDebitCanceledEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_failed_event import (
        V2MoneyManagementReceivedDebitFailedEvent as V2MoneyManagementReceivedDebitFailedEvent,
        V2MoneyManagementReceivedDebitFailedEventNotification as V2MoneyManagementReceivedDebitFailedEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_pending_event import (
        V2MoneyManagementReceivedDebitPendingEvent as V2MoneyManagementReceivedDebitPendingEvent,
        V2MoneyManagementReceivedDebitPendingEventNotification as V2MoneyManagementReceivedDebitPendingEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_succeeded_event import (
        V2MoneyManagementReceivedDebitSucceededEvent as V2MoneyManagementReceivedDebitSucceededEvent,
        V2MoneyManagementReceivedDebitSucceededEventNotification as V2MoneyManagementReceivedDebitSucceededEventNotification,
    )
    from stripe.events._v2_money_management_received_debit_updated_event import (
        V2MoneyManagementReceivedDebitUpdatedEvent as V2MoneyManagementReceivedDebitUpdatedEvent,
        V2MoneyManagementReceivedDebitUpdatedEventNotification as V2MoneyManagementReceivedDebitUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEvent as V2MoneyManagementTransactionCreatedEvent,
        V2MoneyManagementTransactionCreatedEventNotification as V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEvent as V2MoneyManagementTransactionUpdatedEvent,
        V2MoneyManagementTransactionUpdatedEventNotification as V2MoneyManagementTransactionUpdatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAttemptFailedEvent as V2PaymentsOffSessionPaymentAttemptFailedEvent,
        V2PaymentsOffSessionPaymentAttemptFailedEventNotification as V2PaymentsOffSessionPaymentAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_started_event import (
        V2PaymentsOffSessionPaymentAttemptStartedEvent as V2PaymentsOffSessionPaymentAttemptStartedEvent,
        V2PaymentsOffSessionPaymentAttemptStartedEventNotification as V2PaymentsOffSessionPaymentAttemptStartedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent as V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
        V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification as V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event import (
        V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent as V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
        V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification as V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_canceled_event import (
        V2PaymentsOffSessionPaymentCanceledEvent as V2PaymentsOffSessionPaymentCanceledEvent,
        V2PaymentsOffSessionPaymentCanceledEventNotification as V2PaymentsOffSessionPaymentCanceledEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_created_event import (
        V2PaymentsOffSessionPaymentCreatedEvent as V2PaymentsOffSessionPaymentCreatedEvent,
        V2PaymentsOffSessionPaymentCreatedEventNotification as V2PaymentsOffSessionPaymentCreatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_failed_event import (
        V2PaymentsOffSessionPaymentFailedEvent as V2PaymentsOffSessionPaymentFailedEvent,
        V2PaymentsOffSessionPaymentFailedEventNotification as V2PaymentsOffSessionPaymentFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_requires_capture_event import (
        V2PaymentsOffSessionPaymentRequiresCaptureEvent as V2PaymentsOffSessionPaymentRequiresCaptureEvent,
        V2PaymentsOffSessionPaymentRequiresCaptureEventNotification as V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_succeeded_event import (
        V2PaymentsOffSessionPaymentSucceededEvent as V2PaymentsOffSessionPaymentSucceededEvent,
        V2PaymentsOffSessionPaymentSucceededEventNotification as V2PaymentsOffSessionPaymentSucceededEventNotification,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ALL_EVENT_NOTIFICATIONS": ("stripe.events._event_classes", False),
    "V1BillingMeterErrorReportTriggeredEvent": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterErrorReportTriggeredEventNotification": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEvent": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V1BillingMeterNoMeterFoundEventNotification": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        False,
    ),
    "V2CoreAccountClosedEvent": (
        "stripe.events._v2_core_account_closed_event",
        False,
    ),
    "V2CoreAccountClosedEventNotification": (
        "stripe.events._v2_core_account_closed_event",
        False,
    ),
    "V2CoreAccountCreatedEvent": (
        "stripe.events._v2_core_account_created_event",
        False,
    ),
    "V2CoreAccountCreatedEventNotification": (
        "stripe.events._v2_core_account_created_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerUpdatedEvent": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        False,
    ),
    "V2CoreAccountIncludingDefaultsUpdatedEvent": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingIdentityUpdatedEvent": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        False,
    ),
    "V2CoreAccountIncludingIdentityUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        False,
    ),
    "V2CoreAccountIncludingRequirementsUpdatedEvent": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        False,
    ),
    "V2CoreAccountIncludingRequirementsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        False,
    ),
    "V2CoreAccountLinkReturnedEvent": (
        "stripe.events._v2_core_account_link_returned_event",
        False,
    ),
    "V2CoreAccountLinkReturnedEventNotification": (
        "stripe.events._v2_core_account_link_returned_event",
        False,
    ),
    "V2CoreAccountPersonCreatedEvent": (
        "stripe.events._v2_core_account_person_created_event",
        False,
    ),
    "V2CoreAccountPersonCreatedEventNotification": (
        "stripe.events._v2_core_account_person_created_event",
        False,
    ),
    "V2CoreAccountPersonDeletedEvent": (
        "stripe.events._v2_core_account_person_deleted_event",
        False,
    ),
    "V2CoreAccountPersonDeletedEventNotification": (
        "stripe.events._v2_core_account_person_deleted_event",
        False,
    ),
    "V2CoreAccountPersonUpdatedEvent": (
        "stripe.events._v2_core_account_person_updated_event",
        False,
    ),
    "V2CoreAccountPersonUpdatedEventNotification": (
        "stripe.events._v2_core_account_person_updated_event",
        False,
    ),
    "V2CoreAccountUpdatedEvent": (
        "stripe.events._v2_core_account_updated_event",
        False,
    ),
    "V2CoreAccountUpdatedEventNotification": (
        "stripe.events._v2_core_account_updated_event",
        False,
    ),
    "V2CoreEventDestinationPingEvent": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
    "V2CoreEventDestinationPingEventNotification": (
        "stripe.events._v2_core_event_destination_ping_event",
        False,
    ),
    "V2CoreHealthEventGenerationFailureResolvedEvent": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        False,
    ),
    "V2CoreHealthEventGenerationFailureResolvedEventNotification": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        False,
    ),
    "V2MoneyManagementAdjustmentCreatedEvent": (
        "stripe.events._v2_money_management_adjustment_created_event",
        False,
    ),
    "V2MoneyManagementAdjustmentCreatedEventNotification": (
        "stripe.events._v2_money_management_adjustment_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountCreatedEvent": (
        "stripe.events._v2_money_management_financial_account_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountCreatedEventNotification": (
        "stripe.events._v2_money_management_financial_account_created_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountUpdatedEvent": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        False,
    ),
    "V2MoneyManagementFinancialAccountUpdatedEventNotification": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressActivatedEvent": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressActivatedEventNotification": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressFailedEvent": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        False,
    ),
    "V2MoneyManagementFinancialAddressFailedEventNotification": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferAvailableEvent": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        False,
    ),
    "V2MoneyManagementInboundTransferAvailableEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitFailedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitFailedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitProcessingEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitQueuedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitReturnedEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitSucceededEvent": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCanceledEvent": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCanceledEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCreatedEvent": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentCreatedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentFailedEvent": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentFailedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentPostedEvent": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentPostedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentReturnedEvent": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentReturnedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentUpdatedEvent": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentUpdatedEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCanceledEvent": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCanceledEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCreatedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferCreatedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferFailedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferFailedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferPostedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferPostedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferReturnedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferReturnedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferUpdatedEvent": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        False,
    ),
    "V2MoneyManagementOutboundTransferUpdatedEventNotification": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodUpdatedEvent": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodUpdatedEventNotification": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditAvailableEvent": (
        "stripe.events._v2_money_management_received_credit_available_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditAvailableEventNotification": (
        "stripe.events._v2_money_management_received_credit_available_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditFailedEvent": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditFailedEventNotification": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditReturnedEvent": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditReturnedEventNotification": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditSucceededEvent": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedCreditSucceededEventNotification": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitCanceledEvent": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitCanceledEventNotification": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitFailedEvent": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitFailedEventNotification": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitPendingEvent": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitPendingEventNotification": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitSucceededEvent": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitSucceededEventNotification": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitUpdatedEvent": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        False,
    ),
    "V2MoneyManagementReceivedDebitUpdatedEventNotification": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        False,
    ),
    "V2MoneyManagementTransactionCreatedEvent": (
        "stripe.events._v2_money_management_transaction_created_event",
        False,
    ),
    "V2MoneyManagementTransactionCreatedEventNotification": (
        "stripe.events._v2_money_management_transaction_created_event",
        False,
    ),
    "V2MoneyManagementTransactionUpdatedEvent": (
        "stripe.events._v2_money_management_transaction_updated_event",
        False,
    ),
    "V2MoneyManagementTransactionUpdatedEventNotification": (
        "stripe.events._v2_money_management_transaction_updated_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptStartedEvent": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAttemptStartedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCanceledEvent": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCanceledEventNotification": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCreatedEvent": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentCreatedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentFailedEvent": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentFailedEventNotification": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentRequiresCaptureEvent": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentRequiresCaptureEventNotification": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentSucceededEvent": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        False,
    ),
    "V2PaymentsOffSessionPaymentSucceededEventNotification": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()

# The end of the section generated from our OpenAPI spec
