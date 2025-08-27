# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
)
from stripe.events._v2_billing_cadence_billed_event import (
    V2BillingCadenceBilledEvent,
)
from stripe.events._v2_billing_cadence_canceled_event import (
    V2BillingCadenceCanceledEvent,
)
from stripe.events._v2_billing_cadence_created_event import (
    V2BillingCadenceCreatedEvent,
)
from stripe.events._v2_billing_cadence_errored_event import (
    V2BillingCadenceErroredEvent,
)
from stripe.events._v2_billing_license_fee_created_event import (
    V2BillingLicenseFeeCreatedEvent,
)
from stripe.events._v2_billing_license_fee_updated_event import (
    V2BillingLicenseFeeUpdatedEvent,
)
from stripe.events._v2_billing_license_fee_version_created_event import (
    V2BillingLicenseFeeVersionCreatedEvent,
)
from stripe.events._v2_billing_licensed_item_created_event import (
    V2BillingLicensedItemCreatedEvent,
)
from stripe.events._v2_billing_licensed_item_updated_event import (
    V2BillingLicensedItemUpdatedEvent,
)
from stripe.events._v2_billing_metered_item_created_event import (
    V2BillingMeteredItemCreatedEvent,
)
from stripe.events._v2_billing_metered_item_updated_event import (
    V2BillingMeteredItemUpdatedEvent,
)
from stripe.events._v2_billing_pricing_plan_created_event import (
    V2BillingPricingPlanCreatedEvent,
)
from stripe.events._v2_billing_pricing_plan_updated_event import (
    V2BillingPricingPlanUpdatedEvent,
)
from stripe.events._v2_billing_pricing_plan_component_created_event import (
    V2BillingPricingPlanComponentCreatedEvent,
)
from stripe.events._v2_billing_pricing_plan_component_updated_event import (
    V2BillingPricingPlanComponentUpdatedEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event import (
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_current_event import (
    V2BillingPricingPlanSubscriptionCollectionCurrentEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event import (
    V2BillingPricingPlanSubscriptionCollectionPastDueEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event import (
    V2BillingPricingPlanSubscriptionCollectionPausedEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event import (
    V2BillingPricingPlanSubscriptionCollectionUnpaidEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event import (
    V2BillingPricingPlanSubscriptionServicingActivatedEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event import (
    V2BillingPricingPlanSubscriptionServicingCanceledEvent,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event import (
    V2BillingPricingPlanSubscriptionServicingPausedEvent,
)
from stripe.events._v2_billing_pricing_plan_version_created_event import (
    V2BillingPricingPlanVersionCreatedEvent,
)
from stripe.events._v2_billing_rate_card_created_event import (
    V2BillingRateCardCreatedEvent,
)
from stripe.events._v2_billing_rate_card_updated_event import (
    V2BillingRateCardUpdatedEvent,
)
from stripe.events._v2_billing_rate_card_rate_created_event import (
    V2BillingRateCardRateCreatedEvent,
)
from stripe.events._v2_billing_rate_card_subscription_activated_event import (
    V2BillingRateCardSubscriptionActivatedEvent,
)
from stripe.events._v2_billing_rate_card_subscription_canceled_event import (
    V2BillingRateCardSubscriptionCanceledEvent,
)
from stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event import (
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent,
)
from stripe.events._v2_billing_rate_card_subscription_collection_current_event import (
    V2BillingRateCardSubscriptionCollectionCurrentEvent,
)
from stripe.events._v2_billing_rate_card_subscription_collection_past_due_event import (
    V2BillingRateCardSubscriptionCollectionPastDueEvent,
)
from stripe.events._v2_billing_rate_card_subscription_collection_paused_event import (
    V2BillingRateCardSubscriptionCollectionPausedEvent,
)
from stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event import (
    V2BillingRateCardSubscriptionCollectionUnpaidEvent,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_activated_event import (
    V2BillingRateCardSubscriptionServicingActivatedEvent,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event import (
    V2BillingRateCardSubscriptionServicingCanceledEvent,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_paused_event import (
    V2BillingRateCardSubscriptionServicingPausedEvent,
)
from stripe.events._v2_billing_rate_card_version_created_event import (
    V2BillingRateCardVersionCreatedEvent,
)
from stripe.events._v2_core_account_closed_event import (
    V2CoreAccountClosedEvent,
)
from stripe.events._v2_core_account_created_event import (
    V2CoreAccountCreatedEvent,
)
from stripe.events._v2_core_account_updated_event import (
    V2CoreAccountUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
    V2CoreAccountIncludingConfigurationCustomerUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
    V2CoreAccountIncludingConfigurationMerchantUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
    V2CoreAccountIncludingConfigurationRecipientUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent,
)
from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
    V2CoreAccountIncludingConfigurationStorerUpdatedEvent,
)
from stripe.events._v2_core_account_including_defaults_updated_event import (
    V2CoreAccountIncludingDefaultsUpdatedEvent,
)
from stripe.events._v2_core_account_including_identity_updated_event import (
    V2CoreAccountIncludingIdentityUpdatedEvent,
)
from stripe.events._v2_core_account_including_requirements_updated_event import (
    V2CoreAccountIncludingRequirementsUpdatedEvent,
)
from stripe.events._v2_core_account_link_returned_event import (
    V2CoreAccountLinkReturnedEvent,
)
from stripe.events._v2_core_account_person_created_event import (
    V2CoreAccountPersonCreatedEvent,
)
from stripe.events._v2_core_account_person_deleted_event import (
    V2CoreAccountPersonDeletedEvent,
)
from stripe.events._v2_core_account_person_updated_event import (
    V2CoreAccountPersonUpdatedEvent,
)
from stripe.events._v2_core_event_destination_ping_event import (
    V2CoreEventDestinationPingEvent,
)
from stripe.events._v2_core_health_api_error_firing_event import (
    V2CoreHealthApiErrorFiringEvent,
)
from stripe.events._v2_core_health_api_error_resolved_event import (
    V2CoreHealthApiErrorResolvedEvent,
)
from stripe.events._v2_core_health_api_latency_firing_event import (
    V2CoreHealthApiLatencyFiringEvent,
)
from stripe.events._v2_core_health_api_latency_resolved_event import (
    V2CoreHealthApiLatencyResolvedEvent,
)
from stripe.events._v2_core_health_authorization_rate_drop_firing_event import (
    V2CoreHealthAuthorizationRateDropFiringEvent,
)
from stripe.events._v2_core_health_authorization_rate_drop_resolved_event import (
    V2CoreHealthAuthorizationRateDropResolvedEvent,
)
from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
    V2CoreHealthEventGenerationFailureResolvedEvent,
)
from stripe.events._v2_core_health_fraud_rate_increased_event import (
    V2CoreHealthFraudRateIncreasedEvent,
)
from stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event import (
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent,
)
from stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event import (
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent,
)
from stripe.events._v2_core_health_payment_method_error_firing_event import (
    V2CoreHealthPaymentMethodErrorFiringEvent,
)
from stripe.events._v2_core_health_payment_method_error_resolved_event import (
    V2CoreHealthPaymentMethodErrorResolvedEvent,
)
from stripe.events._v2_core_health_traffic_volume_drop_firing_event import (
    V2CoreHealthTrafficVolumeDropFiringEvent,
)
from stripe.events._v2_core_health_traffic_volume_drop_resolved_event import (
    V2CoreHealthTrafficVolumeDropResolvedEvent,
)
from stripe.events._v2_core_health_webhook_latency_firing_event import (
    V2CoreHealthWebhookLatencyFiringEvent,
)
from stripe.events._v2_core_health_webhook_latency_resolved_event import (
    V2CoreHealthWebhookLatencyResolvedEvent,
)
from stripe.events._v2_money_management_adjustment_created_event import (
    V2MoneyManagementAdjustmentCreatedEvent,
)
from stripe.events._v2_money_management_financial_account_created_event import (
    V2MoneyManagementFinancialAccountCreatedEvent,
)
from stripe.events._v2_money_management_financial_account_updated_event import (
    V2MoneyManagementFinancialAccountUpdatedEvent,
)
from stripe.events._v2_money_management_financial_address_activated_event import (
    V2MoneyManagementFinancialAddressActivatedEvent,
)
from stripe.events._v2_money_management_financial_address_failed_event import (
    V2MoneyManagementFinancialAddressFailedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_available_event import (
    V2MoneyManagementInboundTransferAvailableEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
    V2MoneyManagementInboundTransferBankDebitFailedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
    V2MoneyManagementInboundTransferBankDebitProcessingEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
    V2MoneyManagementInboundTransferBankDebitQueuedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
    V2MoneyManagementInboundTransferBankDebitReturnedEvent,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
    V2MoneyManagementInboundTransferBankDebitSucceededEvent,
)
from stripe.events._v2_money_management_outbound_payment_canceled_event import (
    V2MoneyManagementOutboundPaymentCanceledEvent,
)
from stripe.events._v2_money_management_outbound_payment_created_event import (
    V2MoneyManagementOutboundPaymentCreatedEvent,
)
from stripe.events._v2_money_management_outbound_payment_failed_event import (
    V2MoneyManagementOutboundPaymentFailedEvent,
)
from stripe.events._v2_money_management_outbound_payment_posted_event import (
    V2MoneyManagementOutboundPaymentPostedEvent,
)
from stripe.events._v2_money_management_outbound_payment_returned_event import (
    V2MoneyManagementOutboundPaymentReturnedEvent,
)
from stripe.events._v2_money_management_outbound_payment_updated_event import (
    V2MoneyManagementOutboundPaymentUpdatedEvent,
)
from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
    V2MoneyManagementOutboundTransferCanceledEvent,
)
from stripe.events._v2_money_management_outbound_transfer_created_event import (
    V2MoneyManagementOutboundTransferCreatedEvent,
)
from stripe.events._v2_money_management_outbound_transfer_failed_event import (
    V2MoneyManagementOutboundTransferFailedEvent,
)
from stripe.events._v2_money_management_outbound_transfer_posted_event import (
    V2MoneyManagementOutboundTransferPostedEvent,
)
from stripe.events._v2_money_management_outbound_transfer_returned_event import (
    V2MoneyManagementOutboundTransferReturnedEvent,
)
from stripe.events._v2_money_management_outbound_transfer_updated_event import (
    V2MoneyManagementOutboundTransferUpdatedEvent,
)
from stripe.events._v2_money_management_payout_method_updated_event import (
    V2MoneyManagementPayoutMethodUpdatedEvent,
)
from stripe.events._v2_money_management_received_credit_available_event import (
    V2MoneyManagementReceivedCreditAvailableEvent,
)
from stripe.events._v2_money_management_received_credit_failed_event import (
    V2MoneyManagementReceivedCreditFailedEvent,
)
from stripe.events._v2_money_management_received_credit_returned_event import (
    V2MoneyManagementReceivedCreditReturnedEvent,
)
from stripe.events._v2_money_management_received_credit_succeeded_event import (
    V2MoneyManagementReceivedCreditSucceededEvent,
)
from stripe.events._v2_money_management_received_debit_canceled_event import (
    V2MoneyManagementReceivedDebitCanceledEvent,
)
from stripe.events._v2_money_management_received_debit_failed_event import (
    V2MoneyManagementReceivedDebitFailedEvent,
)
from stripe.events._v2_money_management_received_debit_pending_event import (
    V2MoneyManagementReceivedDebitPendingEvent,
)
from stripe.events._v2_money_management_received_debit_succeeded_event import (
    V2MoneyManagementReceivedDebitSucceededEvent,
)
from stripe.events._v2_money_management_received_debit_updated_event import (
    V2MoneyManagementReceivedDebitUpdatedEvent,
)
from stripe.events._v2_money_management_transaction_created_event import (
    V2MoneyManagementTransactionCreatedEvent,
)
from stripe.events._v2_money_management_transaction_updated_event import (
    V2MoneyManagementTransactionUpdatedEvent,
)
from stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event import (
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
)
from stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event import (
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
)
from stripe.events._v2_payments_off_session_payment_canceled_event import (
    V2PaymentsOffSessionPaymentCanceledEvent,
)
from stripe.events._v2_payments_off_session_payment_created_event import (
    V2PaymentsOffSessionPaymentCreatedEvent,
)
from stripe.events._v2_payments_off_session_payment_failed_event import (
    V2PaymentsOffSessionPaymentFailedEvent,
)
from stripe.events._v2_payments_off_session_payment_succeeded_event import (
    V2PaymentsOffSessionPaymentSucceededEvent,
)
from stripe.events._v2_reporting_report_run_created_event import (
    V2ReportingReportRunCreatedEvent,
)
from stripe.events._v2_reporting_report_run_failed_event import (
    V2ReportingReportRunFailedEvent,
)
from stripe.events._v2_reporting_report_run_succeeded_event import (
    V2ReportingReportRunSucceededEvent,
)
from stripe.events._v2_reporting_report_run_updated_event import (
    V2ReportingReportRunUpdatedEvent,
)


THIN_EVENT_CLASSES = {
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V2BillingCadenceBilledEvent.LOOKUP_TYPE: V2BillingCadenceBilledEvent,
    V2BillingCadenceCanceledEvent.LOOKUP_TYPE: V2BillingCadenceCanceledEvent,
    V2BillingCadenceCreatedEvent.LOOKUP_TYPE: V2BillingCadenceCreatedEvent,
    V2BillingCadenceErroredEvent.LOOKUP_TYPE: V2BillingCadenceErroredEvent,
    V2BillingLicensedItemCreatedEvent.LOOKUP_TYPE: V2BillingLicensedItemCreatedEvent,
    V2BillingLicensedItemUpdatedEvent.LOOKUP_TYPE: V2BillingLicensedItemUpdatedEvent,
    V2BillingLicenseFeeCreatedEvent.LOOKUP_TYPE: V2BillingLicenseFeeCreatedEvent,
    V2BillingLicenseFeeUpdatedEvent.LOOKUP_TYPE: V2BillingLicenseFeeUpdatedEvent,
    V2BillingLicenseFeeVersionCreatedEvent.LOOKUP_TYPE: V2BillingLicenseFeeVersionCreatedEvent,
    V2BillingMeteredItemCreatedEvent.LOOKUP_TYPE: V2BillingMeteredItemCreatedEvent,
    V2BillingMeteredItemUpdatedEvent.LOOKUP_TYPE: V2BillingMeteredItemUpdatedEvent,
    V2BillingPricingPlanComponentCreatedEvent.LOOKUP_TYPE: V2BillingPricingPlanComponentCreatedEvent,
    V2BillingPricingPlanComponentUpdatedEvent.LOOKUP_TYPE: V2BillingPricingPlanComponentUpdatedEvent,
    V2BillingPricingPlanCreatedEvent.LOOKUP_TYPE: V2BillingPricingPlanCreatedEvent,
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent,
    V2BillingPricingPlanSubscriptionCollectionCurrentEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionCurrentEvent,
    V2BillingPricingPlanSubscriptionCollectionPastDueEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionPastDueEvent,
    V2BillingPricingPlanSubscriptionCollectionPausedEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionPausedEvent,
    V2BillingPricingPlanSubscriptionCollectionUnpaidEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionUnpaidEvent,
    V2BillingPricingPlanSubscriptionServicingActivatedEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingActivatedEvent,
    V2BillingPricingPlanSubscriptionServicingCanceledEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingCanceledEvent,
    V2BillingPricingPlanSubscriptionServicingPausedEvent.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingPausedEvent,
    V2BillingPricingPlanUpdatedEvent.LOOKUP_TYPE: V2BillingPricingPlanUpdatedEvent,
    V2BillingPricingPlanVersionCreatedEvent.LOOKUP_TYPE: V2BillingPricingPlanVersionCreatedEvent,
    V2BillingRateCardCreatedEvent.LOOKUP_TYPE: V2BillingRateCardCreatedEvent,
    V2BillingRateCardRateCreatedEvent.LOOKUP_TYPE: V2BillingRateCardRateCreatedEvent,
    V2BillingRateCardSubscriptionActivatedEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionActivatedEvent,
    V2BillingRateCardSubscriptionCanceledEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCanceledEvent,
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent,
    V2BillingRateCardSubscriptionCollectionCurrentEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionCurrentEvent,
    V2BillingRateCardSubscriptionCollectionPastDueEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionPastDueEvent,
    V2BillingRateCardSubscriptionCollectionPausedEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionPausedEvent,
    V2BillingRateCardSubscriptionCollectionUnpaidEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionUnpaidEvent,
    V2BillingRateCardSubscriptionServicingActivatedEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingActivatedEvent,
    V2BillingRateCardSubscriptionServicingCanceledEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingCanceledEvent,
    V2BillingRateCardSubscriptionServicingPausedEvent.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingPausedEvent,
    V2BillingRateCardUpdatedEvent.LOOKUP_TYPE: V2BillingRateCardUpdatedEvent,
    V2BillingRateCardVersionCreatedEvent.LOOKUP_TYPE: V2BillingRateCardVersionCreatedEvent,
    V2CoreAccountClosedEvent.LOOKUP_TYPE: V2CoreAccountClosedEvent,
    V2CoreAccountCreatedEvent.LOOKUP_TYPE: V2CoreAccountCreatedEvent,
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationCustomerUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCustomerUpdatedEvent,
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationMerchantUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationMerchantUpdatedEvent,
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationRecipientUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationRecipientUpdatedEvent,
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationStorerUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationStorerUpdatedEvent,
    V2CoreAccountIncludingDefaultsUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingDefaultsUpdatedEvent,
    V2CoreAccountIncludingIdentityUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingIdentityUpdatedEvent,
    V2CoreAccountIncludingRequirementsUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingRequirementsUpdatedEvent,
    V2CoreAccountLinkReturnedEvent.LOOKUP_TYPE: V2CoreAccountLinkReturnedEvent,
    V2CoreAccountPersonCreatedEvent.LOOKUP_TYPE: V2CoreAccountPersonCreatedEvent,
    V2CoreAccountPersonDeletedEvent.LOOKUP_TYPE: V2CoreAccountPersonDeletedEvent,
    V2CoreAccountPersonUpdatedEvent.LOOKUP_TYPE: V2CoreAccountPersonUpdatedEvent,
    V2CoreAccountUpdatedEvent.LOOKUP_TYPE: V2CoreAccountUpdatedEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
    V2CoreHealthApiErrorFiringEvent.LOOKUP_TYPE: V2CoreHealthApiErrorFiringEvent,
    V2CoreHealthApiErrorResolvedEvent.LOOKUP_TYPE: V2CoreHealthApiErrorResolvedEvent,
    V2CoreHealthApiLatencyFiringEvent.LOOKUP_TYPE: V2CoreHealthApiLatencyFiringEvent,
    V2CoreHealthApiLatencyResolvedEvent.LOOKUP_TYPE: V2CoreHealthApiLatencyResolvedEvent,
    V2CoreHealthAuthorizationRateDropFiringEvent.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropFiringEvent,
    V2CoreHealthAuthorizationRateDropResolvedEvent.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropResolvedEvent,
    V2CoreHealthEventGenerationFailureResolvedEvent.LOOKUP_TYPE: V2CoreHealthEventGenerationFailureResolvedEvent,
    V2CoreHealthFraudRateIncreasedEvent.LOOKUP_TYPE: V2CoreHealthFraudRateIncreasedEvent,
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent,
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent,
    V2CoreHealthPaymentMethodErrorFiringEvent.LOOKUP_TYPE: V2CoreHealthPaymentMethodErrorFiringEvent,
    V2CoreHealthPaymentMethodErrorResolvedEvent.LOOKUP_TYPE: V2CoreHealthPaymentMethodErrorResolvedEvent,
    V2CoreHealthTrafficVolumeDropFiringEvent.LOOKUP_TYPE: V2CoreHealthTrafficVolumeDropFiringEvent,
    V2CoreHealthTrafficVolumeDropResolvedEvent.LOOKUP_TYPE: V2CoreHealthTrafficVolumeDropResolvedEvent,
    V2CoreHealthWebhookLatencyFiringEvent.LOOKUP_TYPE: V2CoreHealthWebhookLatencyFiringEvent,
    V2CoreHealthWebhookLatencyResolvedEvent.LOOKUP_TYPE: V2CoreHealthWebhookLatencyResolvedEvent,
    V2MoneyManagementAdjustmentCreatedEvent.LOOKUP_TYPE: V2MoneyManagementAdjustmentCreatedEvent,
    V2MoneyManagementFinancialAccountCreatedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAccountCreatedEvent,
    V2MoneyManagementFinancialAccountUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAccountUpdatedEvent,
    V2MoneyManagementFinancialAddressActivatedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAddressActivatedEvent,
    V2MoneyManagementFinancialAddressFailedEvent.LOOKUP_TYPE: V2MoneyManagementFinancialAddressFailedEvent,
    V2MoneyManagementInboundTransferAvailableEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferAvailableEvent,
    V2MoneyManagementInboundTransferBankDebitFailedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitFailedEvent,
    V2MoneyManagementInboundTransferBankDebitProcessingEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitProcessingEvent,
    V2MoneyManagementInboundTransferBankDebitQueuedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitQueuedEvent,
    V2MoneyManagementInboundTransferBankDebitReturnedEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitReturnedEvent,
    V2MoneyManagementInboundTransferBankDebitSucceededEvent.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitSucceededEvent,
    V2MoneyManagementOutboundPaymentCanceledEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentCanceledEvent,
    V2MoneyManagementOutboundPaymentCreatedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentCreatedEvent,
    V2MoneyManagementOutboundPaymentFailedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentFailedEvent,
    V2MoneyManagementOutboundPaymentPostedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentPostedEvent,
    V2MoneyManagementOutboundPaymentReturnedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentReturnedEvent,
    V2MoneyManagementOutboundPaymentUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentUpdatedEvent,
    V2MoneyManagementOutboundTransferCanceledEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferCanceledEvent,
    V2MoneyManagementOutboundTransferCreatedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferCreatedEvent,
    V2MoneyManagementOutboundTransferFailedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferFailedEvent,
    V2MoneyManagementOutboundTransferPostedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferPostedEvent,
    V2MoneyManagementOutboundTransferReturnedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferReturnedEvent,
    V2MoneyManagementOutboundTransferUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementOutboundTransferUpdatedEvent,
    V2MoneyManagementPayoutMethodUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementPayoutMethodUpdatedEvent,
    V2MoneyManagementReceivedCreditAvailableEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditAvailableEvent,
    V2MoneyManagementReceivedCreditFailedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditFailedEvent,
    V2MoneyManagementReceivedCreditReturnedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditReturnedEvent,
    V2MoneyManagementReceivedCreditSucceededEvent.LOOKUP_TYPE: V2MoneyManagementReceivedCreditSucceededEvent,
    V2MoneyManagementReceivedDebitCanceledEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitCanceledEvent,
    V2MoneyManagementReceivedDebitFailedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitFailedEvent,
    V2MoneyManagementReceivedDebitPendingEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitPendingEvent,
    V2MoneyManagementReceivedDebitSucceededEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitSucceededEvent,
    V2MoneyManagementReceivedDebitUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementReceivedDebitUpdatedEvent,
    V2MoneyManagementTransactionCreatedEvent.LOOKUP_TYPE: V2MoneyManagementTransactionCreatedEvent,
    V2MoneyManagementTransactionUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementTransactionUpdatedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
    V2PaymentsOffSessionPaymentCanceledEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCanceledEvent,
    V2PaymentsOffSessionPaymentCreatedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCreatedEvent,
    V2PaymentsOffSessionPaymentFailedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentFailedEvent,
    V2PaymentsOffSessionPaymentSucceededEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentSucceededEvent,
    V2ReportingReportRunCreatedEvent.LOOKUP_TYPE: V2ReportingReportRunCreatedEvent,
    V2ReportingReportRunFailedEvent.LOOKUP_TYPE: V2ReportingReportRunFailedEvent,
    V2ReportingReportRunSucceededEvent.LOOKUP_TYPE: V2ReportingReportRunSucceededEvent,
    V2ReportingReportRunUpdatedEvent.LOOKUP_TYPE: V2ReportingReportRunUpdatedEvent,
}
