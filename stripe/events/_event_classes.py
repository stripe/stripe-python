# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v2_billing_cadence_billed_event import (
        V2BillingCadenceBilledEventNotification,
    )
    from stripe.events._v2_billing_cadence_canceled_event import (
        V2BillingCadenceCanceledEventNotification,
    )
    from stripe.events._v2_billing_cadence_created_event import (
        V2BillingCadenceCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_created_event import (
        V2BillingLicensedItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_updated_event import (
        V2BillingLicensedItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_created_event import (
        V2BillingLicenseFeeCreatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_updated_event import (
        V2BillingLicenseFeeUpdatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_version_created_event import (
        V2BillingLicenseFeeVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_created_event import (
        V2BillingMeteredItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_updated_event import (
        V2BillingMeteredItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_created_event import (
        V2BillingPricingPlanComponentCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_updated_event import (
        V2BillingPricingPlanComponentUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_created_event import (
        V2BillingPricingPlanCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event import (
        V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_current_event import (
        V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event import (
        V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event import (
        V2BillingPricingPlanSubscriptionCollectionPausedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event import (
        V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event import (
        V2BillingPricingPlanSubscriptionServicingActivatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event import (
        V2BillingPricingPlanSubscriptionServicingCanceledEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event import (
        V2BillingPricingPlanSubscriptionServicingPausedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_updated_event import (
        V2BillingPricingPlanUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_version_created_event import (
        V2BillingPricingPlanVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_created_event import (
        V2BillingRateCardCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_rate_created_event import (
        V2BillingRateCardRateCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_activated_event import (
        V2BillingRateCardSubscriptionActivatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_canceled_event import (
        V2BillingRateCardSubscriptionCanceledEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event import (
        V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_current_event import (
        V2BillingRateCardSubscriptionCollectionCurrentEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_past_due_event import (
        V2BillingRateCardSubscriptionCollectionPastDueEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_paused_event import (
        V2BillingRateCardSubscriptionCollectionPausedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event import (
        V2BillingRateCardSubscriptionCollectionUnpaidEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_activated_event import (
        V2BillingRateCardSubscriptionServicingActivatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event import (
        V2BillingRateCardSubscriptionServicingCanceledEventNotification,
    )
    from stripe.events._v2_billing_rate_card_subscription_servicing_paused_event import (
        V2BillingRateCardSubscriptionServicingPausedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_updated_event import (
        V2BillingRateCardUpdatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_version_created_event import (
        V2BillingRateCardVersionCreatedEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event import (
        V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_configuration_card_creator_updated_event import (
        V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification,
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
    from stripe.events._v2_core_claimable_sandbox_claimed_event import (
        V2CoreClaimableSandboxClaimedEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_created_event import (
        V2CoreClaimableSandboxCreatedEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_expired_event import (
        V2CoreClaimableSandboxExpiredEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_expiring_event import (
        V2CoreClaimableSandboxExpiringEventNotification,
    )
    from stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event import (
        V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_event_destination_ping_event import (
        V2CoreEventDestinationPingEventNotification,
    )
    from stripe.events._v2_core_health_api_error_firing_event import (
        V2CoreHealthApiErrorFiringEventNotification,
    )
    from stripe.events._v2_core_health_api_error_resolved_event import (
        V2CoreHealthApiErrorResolvedEventNotification,
    )
    from stripe.events._v2_core_health_api_latency_firing_event import (
        V2CoreHealthApiLatencyFiringEventNotification,
    )
    from stripe.events._v2_core_health_api_latency_resolved_event import (
        V2CoreHealthApiLatencyResolvedEventNotification,
    )
    from stripe.events._v2_core_health_authorization_rate_drop_firing_event import (
        V2CoreHealthAuthorizationRateDropFiringEventNotification,
    )
    from stripe.events._v2_core_health_authorization_rate_drop_resolved_event import (
        V2CoreHealthAuthorizationRateDropResolvedEventNotification,
    )
    from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
        V2CoreHealthEventGenerationFailureResolvedEventNotification,
    )
    from stripe.events._v2_core_health_fraud_rate_increased_event import (
        V2CoreHealthFraudRateIncreasedEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event import (
        V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event import (
        V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event import (
        V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification,
    )
    from stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event import (
        V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification,
    )
    from stripe.events._v2_core_health_payment_method_error_firing_event import (
        V2CoreHealthPaymentMethodErrorFiringEventNotification,
    )
    from stripe.events._v2_core_health_payment_method_error_resolved_event import (
        V2CoreHealthPaymentMethodErrorResolvedEventNotification,
    )
    from stripe.events._v2_core_health_sepa_debit_delayed_firing_event import (
        V2CoreHealthSepaDebitDelayedFiringEventNotification,
    )
    from stripe.events._v2_core_health_sepa_debit_delayed_resolved_event import (
        V2CoreHealthSepaDebitDelayedResolvedEventNotification,
    )
    from stripe.events._v2_core_health_traffic_volume_drop_firing_event import (
        V2CoreHealthTrafficVolumeDropFiringEventNotification,
    )
    from stripe.events._v2_core_health_traffic_volume_drop_resolved_event import (
        V2CoreHealthTrafficVolumeDropResolvedEventNotification,
    )
    from stripe.events._v2_core_health_webhook_latency_firing_event import (
        V2CoreHealthWebhookLatencyFiringEventNotification,
    )
    from stripe.events._v2_core_health_webhook_latency_resolved_event import (
        V2CoreHealthWebhookLatencyResolvedEventNotification,
    )
    from stripe.events._v2_iam_api_key_created_event import (
        V2IamApiKeyCreatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_default_secret_revealed_event import (
        V2IamApiKeyDefaultSecretRevealedEventNotification,
    )
    from stripe.events._v2_iam_api_key_expired_event import (
        V2IamApiKeyExpiredEventNotification,
    )
    from stripe.events._v2_iam_api_key_permissions_updated_event import (
        V2IamApiKeyPermissionsUpdatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_rotated_event import (
        V2IamApiKeyRotatedEventNotification,
    )
    from stripe.events._v2_iam_api_key_updated_event import (
        V2IamApiKeyUpdatedEventNotification,
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
    from stripe.events._v2_money_management_recipient_verification_created_event import (
        V2MoneyManagementRecipientVerificationCreatedEventNotification,
    )
    from stripe.events._v2_money_management_recipient_verification_updated_event import (
        V2MoneyManagementRecipientVerificationUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_failed_event import (
        V2PaymentsOffSessionPaymentAttemptFailedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_attempt_started_event import (
        V2PaymentsOffSessionPaymentAttemptStartedEventNotification,
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
    from stripe.events._v2_payments_settlement_allocation_intent_canceled_event import (
        V2PaymentsSettlementAllocationIntentCanceledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_created_event import (
        V2PaymentsSettlementAllocationIntentCreatedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_errored_event import (
        V2PaymentsSettlementAllocationIntentErroredEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event import (
        V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_matched_event import (
        V2PaymentsSettlementAllocationIntentMatchedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_not_found_event import (
        V2PaymentsSettlementAllocationIntentNotFoundEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_settled_event import (
        V2PaymentsSettlementAllocationIntentSettledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event import (
        V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_created_event import (
        V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_split_settled_event import (
        V2PaymentsSettlementAllocationIntentSplitSettledEventNotification,
    )
    from stripe.events._v2_payments_settlement_allocation_intent_submitted_event import (
        V2PaymentsSettlementAllocationIntentSubmittedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_created_event import (
        V2ReportingReportRunCreatedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_failed_event import (
        V2ReportingReportRunFailedEventNotification,
    )
    from stripe.events._v2_reporting_report_run_succeeded_event import (
        V2ReportingReportRunSucceededEventNotification,
    )
    from stripe.events._v2_reporting_report_run_updated_event import (
        V2ReportingReportRunUpdatedEventNotification,
    )


_V2_EVENT_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEvent",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEvent",
    ),
    "v2.billing.cadence.billed": (
        "stripe.events._v2_billing_cadence_billed_event",
        "V2BillingCadenceBilledEvent",
    ),
    "v2.billing.cadence.canceled": (
        "stripe.events._v2_billing_cadence_canceled_event",
        "V2BillingCadenceCanceledEvent",
    ),
    "v2.billing.cadence.created": (
        "stripe.events._v2_billing_cadence_created_event",
        "V2BillingCadenceCreatedEvent",
    ),
    "v2.billing.licensed_item.created": (
        "stripe.events._v2_billing_licensed_item_created_event",
        "V2BillingLicensedItemCreatedEvent",
    ),
    "v2.billing.licensed_item.updated": (
        "stripe.events._v2_billing_licensed_item_updated_event",
        "V2BillingLicensedItemUpdatedEvent",
    ),
    "v2.billing.license_fee.created": (
        "stripe.events._v2_billing_license_fee_created_event",
        "V2BillingLicenseFeeCreatedEvent",
    ),
    "v2.billing.license_fee.updated": (
        "stripe.events._v2_billing_license_fee_updated_event",
        "V2BillingLicenseFeeUpdatedEvent",
    ),
    "v2.billing.license_fee_version.created": (
        "stripe.events._v2_billing_license_fee_version_created_event",
        "V2BillingLicenseFeeVersionCreatedEvent",
    ),
    "v2.billing.metered_item.created": (
        "stripe.events._v2_billing_metered_item_created_event",
        "V2BillingMeteredItemCreatedEvent",
    ),
    "v2.billing.metered_item.updated": (
        "stripe.events._v2_billing_metered_item_updated_event",
        "V2BillingMeteredItemUpdatedEvent",
    ),
    "v2.billing.pricing_plan_component.created": (
        "stripe.events._v2_billing_pricing_plan_component_created_event",
        "V2BillingPricingPlanComponentCreatedEvent",
    ),
    "v2.billing.pricing_plan_component.updated": (
        "stripe.events._v2_billing_pricing_plan_component_updated_event",
        "V2BillingPricingPlanComponentUpdatedEvent",
    ),
    "v2.billing.pricing_plan.created": (
        "stripe.events._v2_billing_pricing_plan_created_event",
        "V2BillingPricingPlanCreatedEvent",
    ),
    "v2.billing.pricing_plan_subscription.collection_awaiting_customer_action": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event",
        "V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent",
    ),
    "v2.billing.pricing_plan_subscription.collection_current": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_current_event",
        "V2BillingPricingPlanSubscriptionCollectionCurrentEvent",
    ),
    "v2.billing.pricing_plan_subscription.collection_past_due": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event",
        "V2BillingPricingPlanSubscriptionCollectionPastDueEvent",
    ),
    "v2.billing.pricing_plan_subscription.collection_paused": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event",
        "V2BillingPricingPlanSubscriptionCollectionPausedEvent",
    ),
    "v2.billing.pricing_plan_subscription.collection_unpaid": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event",
        "V2BillingPricingPlanSubscriptionCollectionUnpaidEvent",
    ),
    "v2.billing.pricing_plan_subscription.servicing_activated": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event",
        "V2BillingPricingPlanSubscriptionServicingActivatedEvent",
    ),
    "v2.billing.pricing_plan_subscription.servicing_canceled": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event",
        "V2BillingPricingPlanSubscriptionServicingCanceledEvent",
    ),
    "v2.billing.pricing_plan_subscription.servicing_paused": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event",
        "V2BillingPricingPlanSubscriptionServicingPausedEvent",
    ),
    "v2.billing.pricing_plan.updated": (
        "stripe.events._v2_billing_pricing_plan_updated_event",
        "V2BillingPricingPlanUpdatedEvent",
    ),
    "v2.billing.pricing_plan_version.created": (
        "stripe.events._v2_billing_pricing_plan_version_created_event",
        "V2BillingPricingPlanVersionCreatedEvent",
    ),
    "v2.billing.rate_card.created": (
        "stripe.events._v2_billing_rate_card_created_event",
        "V2BillingRateCardCreatedEvent",
    ),
    "v2.billing.rate_card_rate.created": (
        "stripe.events._v2_billing_rate_card_rate_created_event",
        "V2BillingRateCardRateCreatedEvent",
    ),
    "v2.billing.rate_card_subscription.activated": (
        "stripe.events._v2_billing_rate_card_subscription_activated_event",
        "V2BillingRateCardSubscriptionActivatedEvent",
    ),
    "v2.billing.rate_card_subscription.canceled": (
        "stripe.events._v2_billing_rate_card_subscription_canceled_event",
        "V2BillingRateCardSubscriptionCanceledEvent",
    ),
    "v2.billing.rate_card_subscription.collection_awaiting_customer_action": (
        "stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event",
        "V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent",
    ),
    "v2.billing.rate_card_subscription.collection_current": (
        "stripe.events._v2_billing_rate_card_subscription_collection_current_event",
        "V2BillingRateCardSubscriptionCollectionCurrentEvent",
    ),
    "v2.billing.rate_card_subscription.collection_past_due": (
        "stripe.events._v2_billing_rate_card_subscription_collection_past_due_event",
        "V2BillingRateCardSubscriptionCollectionPastDueEvent",
    ),
    "v2.billing.rate_card_subscription.collection_paused": (
        "stripe.events._v2_billing_rate_card_subscription_collection_paused_event",
        "V2BillingRateCardSubscriptionCollectionPausedEvent",
    ),
    "v2.billing.rate_card_subscription.collection_unpaid": (
        "stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event",
        "V2BillingRateCardSubscriptionCollectionUnpaidEvent",
    ),
    "v2.billing.rate_card_subscription.servicing_activated": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_activated_event",
        "V2BillingRateCardSubscriptionServicingActivatedEvent",
    ),
    "v2.billing.rate_card_subscription.servicing_canceled": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event",
        "V2BillingRateCardSubscriptionServicingCanceledEvent",
    ),
    "v2.billing.rate_card_subscription.servicing_paused": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_paused_event",
        "V2BillingRateCardSubscriptionServicingPausedEvent",
    ),
    "v2.billing.rate_card.updated": (
        "stripe.events._v2_billing_rate_card_updated_event",
        "V2BillingRateCardUpdatedEvent",
    ),
    "v2.billing.rate_card_version.created": (
        "stripe.events._v2_billing_rate_card_version_created_event",
        "V2BillingRateCardVersionCreatedEvent",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEvent",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEvent",
    ),
    "v2.core.account[configuration.card_creator].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.card_creator].updated": (
        "stripe.events._v2_core_account_including_configuration_card_creator_updated_event",
        "V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent",
    ),
    "v2.core.account[configuration.customer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.customer].updated": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerUpdatedEvent",
    ),
    "v2.core.account[configuration.merchant].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.merchant].updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantUpdatedEvent",
    ),
    "v2.core.account[configuration.recipient].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.recipient].updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientUpdatedEvent",
    ),
    "v2.core.account[configuration.storer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent",
    ),
    "v2.core.account[configuration.storer].updated": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        "V2CoreAccountIncludingConfigurationStorerUpdatedEvent",
    ),
    "v2.core.account[defaults].updated": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        "V2CoreAccountIncludingDefaultsUpdatedEvent",
    ),
    "v2.core.account[future_requirements].updated": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
        "V2CoreAccountIncludingFutureRequirementsUpdatedEvent",
    ),
    "v2.core.account[identity].updated": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        "V2CoreAccountIncludingIdentityUpdatedEvent",
    ),
    "v2.core.account[requirements].updated": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        "V2CoreAccountIncludingRequirementsUpdatedEvent",
    ),
    "v2.core.account_link.returned": (
        "stripe.events._v2_core_account_link_returned_event",
        "V2CoreAccountLinkReturnedEvent",
    ),
    "v2.core.account_person.created": (
        "stripe.events._v2_core_account_person_created_event",
        "V2CoreAccountPersonCreatedEvent",
    ),
    "v2.core.account_person.deleted": (
        "stripe.events._v2_core_account_person_deleted_event",
        "V2CoreAccountPersonDeletedEvent",
    ),
    "v2.core.account_person.updated": (
        "stripe.events._v2_core_account_person_updated_event",
        "V2CoreAccountPersonUpdatedEvent",
    ),
    "v2.core.account.updated": (
        "stripe.events._v2_core_account_updated_event",
        "V2CoreAccountUpdatedEvent",
    ),
    "v2.core.claimable_sandbox.claimed": (
        "stripe.events._v2_core_claimable_sandbox_claimed_event",
        "V2CoreClaimableSandboxClaimedEvent",
    ),
    "v2.core.claimable_sandbox.created": (
        "stripe.events._v2_core_claimable_sandbox_created_event",
        "V2CoreClaimableSandboxCreatedEvent",
    ),
    "v2.core.claimable_sandbox.expired": (
        "stripe.events._v2_core_claimable_sandbox_expired_event",
        "V2CoreClaimableSandboxExpiredEvent",
    ),
    "v2.core.claimable_sandbox.expiring": (
        "stripe.events._v2_core_claimable_sandbox_expiring_event",
        "V2CoreClaimableSandboxExpiringEvent",
    ),
    "v2.core.claimable_sandbox.sandbox_details_owner_account_updated": (
        "stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event",
        "V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEvent",
    ),
    "v2.core.health.api_error.firing": (
        "stripe.events._v2_core_health_api_error_firing_event",
        "V2CoreHealthApiErrorFiringEvent",
    ),
    "v2.core.health.api_error.resolved": (
        "stripe.events._v2_core_health_api_error_resolved_event",
        "V2CoreHealthApiErrorResolvedEvent",
    ),
    "v2.core.health.api_latency.firing": (
        "stripe.events._v2_core_health_api_latency_firing_event",
        "V2CoreHealthApiLatencyFiringEvent",
    ),
    "v2.core.health.api_latency.resolved": (
        "stripe.events._v2_core_health_api_latency_resolved_event",
        "V2CoreHealthApiLatencyResolvedEvent",
    ),
    "v2.core.health.authorization_rate_drop.firing": (
        "stripe.events._v2_core_health_authorization_rate_drop_firing_event",
        "V2CoreHealthAuthorizationRateDropFiringEvent",
    ),
    "v2.core.health.authorization_rate_drop.resolved": (
        "stripe.events._v2_core_health_authorization_rate_drop_resolved_event",
        "V2CoreHealthAuthorizationRateDropResolvedEvent",
    ),
    "v2.core.health.event_generation_failure.resolved": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        "V2CoreHealthEventGenerationFailureResolvedEvent",
    ),
    "v2.core.health.fraud_rate.increased": (
        "stripe.events._v2_core_health_fraud_rate_increased_event",
        "V2CoreHealthFraudRateIncreasedEvent",
    ),
    "v2.core.health.issuing_authorization_request_errors.firing": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event",
        "V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent",
    ),
    "v2.core.health.issuing_authorization_request_errors.resolved": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event",
        "V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent",
    ),
    "v2.core.health.issuing_authorization_request_timeout.firing": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event",
        "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent",
    ),
    "v2.core.health.issuing_authorization_request_timeout.resolved": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event",
        "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent",
    ),
    "v2.core.health.payment_method_error.firing": (
        "stripe.events._v2_core_health_payment_method_error_firing_event",
        "V2CoreHealthPaymentMethodErrorFiringEvent",
    ),
    "v2.core.health.payment_method_error.resolved": (
        "stripe.events._v2_core_health_payment_method_error_resolved_event",
        "V2CoreHealthPaymentMethodErrorResolvedEvent",
    ),
    "v2.core.health.sepa_debit_delayed.firing": (
        "stripe.events._v2_core_health_sepa_debit_delayed_firing_event",
        "V2CoreHealthSepaDebitDelayedFiringEvent",
    ),
    "v2.core.health.sepa_debit_delayed.resolved": (
        "stripe.events._v2_core_health_sepa_debit_delayed_resolved_event",
        "V2CoreHealthSepaDebitDelayedResolvedEvent",
    ),
    "v2.core.health.traffic_volume_drop.firing": (
        "stripe.events._v2_core_health_traffic_volume_drop_firing_event",
        "V2CoreHealthTrafficVolumeDropFiringEvent",
    ),
    "v2.core.health.traffic_volume_drop.resolved": (
        "stripe.events._v2_core_health_traffic_volume_drop_resolved_event",
        "V2CoreHealthTrafficVolumeDropResolvedEvent",
    ),
    "v2.core.health.webhook_latency.firing": (
        "stripe.events._v2_core_health_webhook_latency_firing_event",
        "V2CoreHealthWebhookLatencyFiringEvent",
    ),
    "v2.core.health.webhook_latency.resolved": (
        "stripe.events._v2_core_health_webhook_latency_resolved_event",
        "V2CoreHealthWebhookLatencyResolvedEvent",
    ),
    "v2.iam.api_key.created": (
        "stripe.events._v2_iam_api_key_created_event",
        "V2IamApiKeyCreatedEvent",
    ),
    "v2.iam.api_key.default_secret_revealed": (
        "stripe.events._v2_iam_api_key_default_secret_revealed_event",
        "V2IamApiKeyDefaultSecretRevealedEvent",
    ),
    "v2.iam.api_key.expired": (
        "stripe.events._v2_iam_api_key_expired_event",
        "V2IamApiKeyExpiredEvent",
    ),
    "v2.iam.api_key.permissions_updated": (
        "stripe.events._v2_iam_api_key_permissions_updated_event",
        "V2IamApiKeyPermissionsUpdatedEvent",
    ),
    "v2.iam.api_key.rotated": (
        "stripe.events._v2_iam_api_key_rotated_event",
        "V2IamApiKeyRotatedEvent",
    ),
    "v2.iam.api_key.updated": (
        "stripe.events._v2_iam_api_key_updated_event",
        "V2IamApiKeyUpdatedEvent",
    ),
    "v2.money_management.adjustment.created": (
        "stripe.events._v2_money_management_adjustment_created_event",
        "V2MoneyManagementAdjustmentCreatedEvent",
    ),
    "v2.money_management.financial_account.created": (
        "stripe.events._v2_money_management_financial_account_created_event",
        "V2MoneyManagementFinancialAccountCreatedEvent",
    ),
    "v2.money_management.financial_account.updated": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        "V2MoneyManagementFinancialAccountUpdatedEvent",
    ),
    "v2.money_management.financial_address.activated": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        "V2MoneyManagementFinancialAddressActivatedEvent",
    ),
    "v2.money_management.financial_address.failed": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        "V2MoneyManagementFinancialAddressFailedEvent",
    ),
    "v2.money_management.inbound_transfer.available": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        "V2MoneyManagementInboundTransferAvailableEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_failed": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        "V2MoneyManagementInboundTransferBankDebitFailedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_processing": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        "V2MoneyManagementInboundTransferBankDebitProcessingEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_queued": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        "V2MoneyManagementInboundTransferBankDebitQueuedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_returned": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        "V2MoneyManagementInboundTransferBankDebitReturnedEvent",
    ),
    "v2.money_management.inbound_transfer.bank_debit_succeeded": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        "V2MoneyManagementInboundTransferBankDebitSucceededEvent",
    ),
    "v2.money_management.outbound_payment.canceled": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        "V2MoneyManagementOutboundPaymentCanceledEvent",
    ),
    "v2.money_management.outbound_payment.created": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        "V2MoneyManagementOutboundPaymentCreatedEvent",
    ),
    "v2.money_management.outbound_payment.failed": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        "V2MoneyManagementOutboundPaymentFailedEvent",
    ),
    "v2.money_management.outbound_payment.posted": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        "V2MoneyManagementOutboundPaymentPostedEvent",
    ),
    "v2.money_management.outbound_payment.returned": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        "V2MoneyManagementOutboundPaymentReturnedEvent",
    ),
    "v2.money_management.outbound_payment.updated": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        "V2MoneyManagementOutboundPaymentUpdatedEvent",
    ),
    "v2.money_management.outbound_transfer.canceled": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        "V2MoneyManagementOutboundTransferCanceledEvent",
    ),
    "v2.money_management.outbound_transfer.created": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        "V2MoneyManagementOutboundTransferCreatedEvent",
    ),
    "v2.money_management.outbound_transfer.failed": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        "V2MoneyManagementOutboundTransferFailedEvent",
    ),
    "v2.money_management.outbound_transfer.posted": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        "V2MoneyManagementOutboundTransferPostedEvent",
    ),
    "v2.money_management.outbound_transfer.returned": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        "V2MoneyManagementOutboundTransferReturnedEvent",
    ),
    "v2.money_management.outbound_transfer.updated": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        "V2MoneyManagementOutboundTransferUpdatedEvent",
    ),
    "v2.money_management.payout_method.created": (
        "stripe.events._v2_money_management_payout_method_created_event",
        "V2MoneyManagementPayoutMethodCreatedEvent",
    ),
    "v2.money_management.payout_method.updated": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        "V2MoneyManagementPayoutMethodUpdatedEvent",
    ),
    "v2.money_management.received_credit.available": (
        "stripe.events._v2_money_management_received_credit_available_event",
        "V2MoneyManagementReceivedCreditAvailableEvent",
    ),
    "v2.money_management.received_credit.failed": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        "V2MoneyManagementReceivedCreditFailedEvent",
    ),
    "v2.money_management.received_credit.returned": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        "V2MoneyManagementReceivedCreditReturnedEvent",
    ),
    "v2.money_management.received_credit.succeeded": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        "V2MoneyManagementReceivedCreditSucceededEvent",
    ),
    "v2.money_management.received_debit.canceled": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        "V2MoneyManagementReceivedDebitCanceledEvent",
    ),
    "v2.money_management.received_debit.failed": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        "V2MoneyManagementReceivedDebitFailedEvent",
    ),
    "v2.money_management.received_debit.pending": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        "V2MoneyManagementReceivedDebitPendingEvent",
    ),
    "v2.money_management.received_debit.succeeded": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        "V2MoneyManagementReceivedDebitSucceededEvent",
    ),
    "v2.money_management.received_debit.updated": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        "V2MoneyManagementReceivedDebitUpdatedEvent",
    ),
    "v2.money_management.recipient_verification.created": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        "V2MoneyManagementRecipientVerificationCreatedEvent",
    ),
    "v2.money_management.recipient_verification.updated": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
        "V2MoneyManagementRecipientVerificationUpdatedEvent",
    ),
    "v2.money_management.transaction.created": (
        "stripe.events._v2_money_management_transaction_created_event",
        "V2MoneyManagementTransactionCreatedEvent",
    ),
    "v2.money_management.transaction.updated": (
        "stripe.events._v2_money_management_transaction_updated_event",
        "V2MoneyManagementTransactionUpdatedEvent",
    ),
    "v2.payments.off_session_payment.attempt_failed": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        "V2PaymentsOffSessionPaymentAttemptFailedEvent",
    ),
    "v2.payments.off_session_payment.attempt_started": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        "V2PaymentsOffSessionPaymentAttemptStartedEvent",
    ),
    "v2.payments.off_session_payment.authorization_attempt_failed": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent",
    ),
    "v2.payments.off_session_payment.authorization_attempt_started": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent",
    ),
    "v2.payments.off_session_payment.canceled": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        "V2PaymentsOffSessionPaymentCanceledEvent",
    ),
    "v2.payments.off_session_payment.created": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        "V2PaymentsOffSessionPaymentCreatedEvent",
    ),
    "v2.payments.off_session_payment.failed": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        "V2PaymentsOffSessionPaymentFailedEvent",
    ),
    "v2.payments.off_session_payment.requires_capture": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        "V2PaymentsOffSessionPaymentRequiresCaptureEvent",
    ),
    "v2.payments.off_session_payment.succeeded": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        "V2PaymentsOffSessionPaymentSucceededEvent",
    ),
    "v2.payments.settlement_allocation_intent.canceled": (
        "stripe.events._v2_payments_settlement_allocation_intent_canceled_event",
        "V2PaymentsSettlementAllocationIntentCanceledEvent",
    ),
    "v2.payments.settlement_allocation_intent.created": (
        "stripe.events._v2_payments_settlement_allocation_intent_created_event",
        "V2PaymentsSettlementAllocationIntentCreatedEvent",
    ),
    "v2.payments.settlement_allocation_intent.errored": (
        "stripe.events._v2_payments_settlement_allocation_intent_errored_event",
        "V2PaymentsSettlementAllocationIntentErroredEvent",
    ),
    "v2.payments.settlement_allocation_intent.funds_not_received": (
        "stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event",
        "V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent",
    ),
    "v2.payments.settlement_allocation_intent.matched": (
        "stripe.events._v2_payments_settlement_allocation_intent_matched_event",
        "V2PaymentsSettlementAllocationIntentMatchedEvent",
    ),
    "v2.payments.settlement_allocation_intent.not_found": (
        "stripe.events._v2_payments_settlement_allocation_intent_not_found_event",
        "V2PaymentsSettlementAllocationIntentNotFoundEvent",
    ),
    "v2.payments.settlement_allocation_intent.settled": (
        "stripe.events._v2_payments_settlement_allocation_intent_settled_event",
        "V2PaymentsSettlementAllocationIntentSettledEvent",
    ),
    "v2.payments.settlement_allocation_intent_split.canceled": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event",
        "V2PaymentsSettlementAllocationIntentSplitCanceledEvent",
    ),
    "v2.payments.settlement_allocation_intent_split.created": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_created_event",
        "V2PaymentsSettlementAllocationIntentSplitCreatedEvent",
    ),
    "v2.payments.settlement_allocation_intent_split.settled": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_settled_event",
        "V2PaymentsSettlementAllocationIntentSplitSettledEvent",
    ),
    "v2.payments.settlement_allocation_intent.submitted": (
        "stripe.events._v2_payments_settlement_allocation_intent_submitted_event",
        "V2PaymentsSettlementAllocationIntentSubmittedEvent",
    ),
    "v2.reporting.report_run.created": (
        "stripe.events._v2_reporting_report_run_created_event",
        "V2ReportingReportRunCreatedEvent",
    ),
    "v2.reporting.report_run.failed": (
        "stripe.events._v2_reporting_report_run_failed_event",
        "V2ReportingReportRunFailedEvent",
    ),
    "v2.reporting.report_run.succeeded": (
        "stripe.events._v2_reporting_report_run_succeeded_event",
        "V2ReportingReportRunSucceededEvent",
    ),
    "v2.reporting.report_run.updated": (
        "stripe.events._v2_reporting_report_run_updated_event",
        "V2ReportingReportRunUpdatedEvent",
    ),
}


def get_v2_event_class(type_: str):
    if type_ not in _V2_EVENT_CLASS_LOOKUP:
        return StripeObject

    import_path, class_name = _V2_EVENT_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


_V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEventNotification",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEventNotification",
    ),
    "v2.billing.cadence.billed": (
        "stripe.events._v2_billing_cadence_billed_event",
        "V2BillingCadenceBilledEventNotification",
    ),
    "v2.billing.cadence.canceled": (
        "stripe.events._v2_billing_cadence_canceled_event",
        "V2BillingCadenceCanceledEventNotification",
    ),
    "v2.billing.cadence.created": (
        "stripe.events._v2_billing_cadence_created_event",
        "V2BillingCadenceCreatedEventNotification",
    ),
    "v2.billing.licensed_item.created": (
        "stripe.events._v2_billing_licensed_item_created_event",
        "V2BillingLicensedItemCreatedEventNotification",
    ),
    "v2.billing.licensed_item.updated": (
        "stripe.events._v2_billing_licensed_item_updated_event",
        "V2BillingLicensedItemUpdatedEventNotification",
    ),
    "v2.billing.license_fee.created": (
        "stripe.events._v2_billing_license_fee_created_event",
        "V2BillingLicenseFeeCreatedEventNotification",
    ),
    "v2.billing.license_fee.updated": (
        "stripe.events._v2_billing_license_fee_updated_event",
        "V2BillingLicenseFeeUpdatedEventNotification",
    ),
    "v2.billing.license_fee_version.created": (
        "stripe.events._v2_billing_license_fee_version_created_event",
        "V2BillingLicenseFeeVersionCreatedEventNotification",
    ),
    "v2.billing.metered_item.created": (
        "stripe.events._v2_billing_metered_item_created_event",
        "V2BillingMeteredItemCreatedEventNotification",
    ),
    "v2.billing.metered_item.updated": (
        "stripe.events._v2_billing_metered_item_updated_event",
        "V2BillingMeteredItemUpdatedEventNotification",
    ),
    "v2.billing.pricing_plan_component.created": (
        "stripe.events._v2_billing_pricing_plan_component_created_event",
        "V2BillingPricingPlanComponentCreatedEventNotification",
    ),
    "v2.billing.pricing_plan_component.updated": (
        "stripe.events._v2_billing_pricing_plan_component_updated_event",
        "V2BillingPricingPlanComponentUpdatedEventNotification",
    ),
    "v2.billing.pricing_plan.created": (
        "stripe.events._v2_billing_pricing_plan_created_event",
        "V2BillingPricingPlanCreatedEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.collection_awaiting_customer_action": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event",
        "V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.collection_current": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_current_event",
        "V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.collection_past_due": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event",
        "V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.collection_paused": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event",
        "V2BillingPricingPlanSubscriptionCollectionPausedEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.collection_unpaid": (
        "stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event",
        "V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.servicing_activated": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event",
        "V2BillingPricingPlanSubscriptionServicingActivatedEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.servicing_canceled": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event",
        "V2BillingPricingPlanSubscriptionServicingCanceledEventNotification",
    ),
    "v2.billing.pricing_plan_subscription.servicing_paused": (
        "stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event",
        "V2BillingPricingPlanSubscriptionServicingPausedEventNotification",
    ),
    "v2.billing.pricing_plan.updated": (
        "stripe.events._v2_billing_pricing_plan_updated_event",
        "V2BillingPricingPlanUpdatedEventNotification",
    ),
    "v2.billing.pricing_plan_version.created": (
        "stripe.events._v2_billing_pricing_plan_version_created_event",
        "V2BillingPricingPlanVersionCreatedEventNotification",
    ),
    "v2.billing.rate_card.created": (
        "stripe.events._v2_billing_rate_card_created_event",
        "V2BillingRateCardCreatedEventNotification",
    ),
    "v2.billing.rate_card_rate.created": (
        "stripe.events._v2_billing_rate_card_rate_created_event",
        "V2BillingRateCardRateCreatedEventNotification",
    ),
    "v2.billing.rate_card_subscription.activated": (
        "stripe.events._v2_billing_rate_card_subscription_activated_event",
        "V2BillingRateCardSubscriptionActivatedEventNotification",
    ),
    "v2.billing.rate_card_subscription.canceled": (
        "stripe.events._v2_billing_rate_card_subscription_canceled_event",
        "V2BillingRateCardSubscriptionCanceledEventNotification",
    ),
    "v2.billing.rate_card_subscription.collection_awaiting_customer_action": (
        "stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event",
        "V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification",
    ),
    "v2.billing.rate_card_subscription.collection_current": (
        "stripe.events._v2_billing_rate_card_subscription_collection_current_event",
        "V2BillingRateCardSubscriptionCollectionCurrentEventNotification",
    ),
    "v2.billing.rate_card_subscription.collection_past_due": (
        "stripe.events._v2_billing_rate_card_subscription_collection_past_due_event",
        "V2BillingRateCardSubscriptionCollectionPastDueEventNotification",
    ),
    "v2.billing.rate_card_subscription.collection_paused": (
        "stripe.events._v2_billing_rate_card_subscription_collection_paused_event",
        "V2BillingRateCardSubscriptionCollectionPausedEventNotification",
    ),
    "v2.billing.rate_card_subscription.collection_unpaid": (
        "stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event",
        "V2BillingRateCardSubscriptionCollectionUnpaidEventNotification",
    ),
    "v2.billing.rate_card_subscription.servicing_activated": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_activated_event",
        "V2BillingRateCardSubscriptionServicingActivatedEventNotification",
    ),
    "v2.billing.rate_card_subscription.servicing_canceled": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event",
        "V2BillingRateCardSubscriptionServicingCanceledEventNotification",
    ),
    "v2.billing.rate_card_subscription.servicing_paused": (
        "stripe.events._v2_billing_rate_card_subscription_servicing_paused_event",
        "V2BillingRateCardSubscriptionServicingPausedEventNotification",
    ),
    "v2.billing.rate_card.updated": (
        "stripe.events._v2_billing_rate_card_updated_event",
        "V2BillingRateCardUpdatedEventNotification",
    ),
    "v2.billing.rate_card_version.created": (
        "stripe.events._v2_billing_rate_card_version_created_event",
        "V2BillingRateCardVersionCreatedEventNotification",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEventNotification",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEventNotification",
    ),
    "v2.core.account[configuration.card_creator].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.card_creator].updated": (
        "stripe.events._v2_core_account_including_configuration_card_creator_updated_event",
        "V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification",
    ),
    "v2.core.account[configuration.customer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.customer].updated": (
        "stripe.events._v2_core_account_including_configuration_customer_updated_event",
        "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification",
    ),
    "v2.core.account[configuration.merchant].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.merchant].updated": (
        "stripe.events._v2_core_account_including_configuration_merchant_updated_event",
        "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification",
    ),
    "v2.core.account[configuration.recipient].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.recipient].updated": (
        "stripe.events._v2_core_account_including_configuration_recipient_updated_event",
        "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification",
    ),
    "v2.core.account[configuration.storer].capability_status_updated": (
        "stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event",
        "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification",
    ),
    "v2.core.account[configuration.storer].updated": (
        "stripe.events._v2_core_account_including_configuration_storer_updated_event",
        "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification",
    ),
    "v2.core.account[defaults].updated": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        "V2CoreAccountIncludingDefaultsUpdatedEventNotification",
    ),
    "v2.core.account[future_requirements].updated": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
        "V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification",
    ),
    "v2.core.account[identity].updated": (
        "stripe.events._v2_core_account_including_identity_updated_event",
        "V2CoreAccountIncludingIdentityUpdatedEventNotification",
    ),
    "v2.core.account[requirements].updated": (
        "stripe.events._v2_core_account_including_requirements_updated_event",
        "V2CoreAccountIncludingRequirementsUpdatedEventNotification",
    ),
    "v2.core.account_link.returned": (
        "stripe.events._v2_core_account_link_returned_event",
        "V2CoreAccountLinkReturnedEventNotification",
    ),
    "v2.core.account_person.created": (
        "stripe.events._v2_core_account_person_created_event",
        "V2CoreAccountPersonCreatedEventNotification",
    ),
    "v2.core.account_person.deleted": (
        "stripe.events._v2_core_account_person_deleted_event",
        "V2CoreAccountPersonDeletedEventNotification",
    ),
    "v2.core.account_person.updated": (
        "stripe.events._v2_core_account_person_updated_event",
        "V2CoreAccountPersonUpdatedEventNotification",
    ),
    "v2.core.account.updated": (
        "stripe.events._v2_core_account_updated_event",
        "V2CoreAccountUpdatedEventNotification",
    ),
    "v2.core.claimable_sandbox.claimed": (
        "stripe.events._v2_core_claimable_sandbox_claimed_event",
        "V2CoreClaimableSandboxClaimedEventNotification",
    ),
    "v2.core.claimable_sandbox.created": (
        "stripe.events._v2_core_claimable_sandbox_created_event",
        "V2CoreClaimableSandboxCreatedEventNotification",
    ),
    "v2.core.claimable_sandbox.expired": (
        "stripe.events._v2_core_claimable_sandbox_expired_event",
        "V2CoreClaimableSandboxExpiredEventNotification",
    ),
    "v2.core.claimable_sandbox.expiring": (
        "stripe.events._v2_core_claimable_sandbox_expiring_event",
        "V2CoreClaimableSandboxExpiringEventNotification",
    ),
    "v2.core.claimable_sandbox.sandbox_details_owner_account_updated": (
        "stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event",
        "V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification",
    ),
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEventNotification",
    ),
    "v2.core.health.api_error.firing": (
        "stripe.events._v2_core_health_api_error_firing_event",
        "V2CoreHealthApiErrorFiringEventNotification",
    ),
    "v2.core.health.api_error.resolved": (
        "stripe.events._v2_core_health_api_error_resolved_event",
        "V2CoreHealthApiErrorResolvedEventNotification",
    ),
    "v2.core.health.api_latency.firing": (
        "stripe.events._v2_core_health_api_latency_firing_event",
        "V2CoreHealthApiLatencyFiringEventNotification",
    ),
    "v2.core.health.api_latency.resolved": (
        "stripe.events._v2_core_health_api_latency_resolved_event",
        "V2CoreHealthApiLatencyResolvedEventNotification",
    ),
    "v2.core.health.authorization_rate_drop.firing": (
        "stripe.events._v2_core_health_authorization_rate_drop_firing_event",
        "V2CoreHealthAuthorizationRateDropFiringEventNotification",
    ),
    "v2.core.health.authorization_rate_drop.resolved": (
        "stripe.events._v2_core_health_authorization_rate_drop_resolved_event",
        "V2CoreHealthAuthorizationRateDropResolvedEventNotification",
    ),
    "v2.core.health.event_generation_failure.resolved": (
        "stripe.events._v2_core_health_event_generation_failure_resolved_event",
        "V2CoreHealthEventGenerationFailureResolvedEventNotification",
    ),
    "v2.core.health.fraud_rate.increased": (
        "stripe.events._v2_core_health_fraud_rate_increased_event",
        "V2CoreHealthFraudRateIncreasedEventNotification",
    ),
    "v2.core.health.issuing_authorization_request_errors.firing": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event",
        "V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification",
    ),
    "v2.core.health.issuing_authorization_request_errors.resolved": (
        "stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event",
        "V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification",
    ),
    "v2.core.health.issuing_authorization_request_timeout.firing": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event",
        "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification",
    ),
    "v2.core.health.issuing_authorization_request_timeout.resolved": (
        "stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event",
        "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification",
    ),
    "v2.core.health.payment_method_error.firing": (
        "stripe.events._v2_core_health_payment_method_error_firing_event",
        "V2CoreHealthPaymentMethodErrorFiringEventNotification",
    ),
    "v2.core.health.payment_method_error.resolved": (
        "stripe.events._v2_core_health_payment_method_error_resolved_event",
        "V2CoreHealthPaymentMethodErrorResolvedEventNotification",
    ),
    "v2.core.health.sepa_debit_delayed.firing": (
        "stripe.events._v2_core_health_sepa_debit_delayed_firing_event",
        "V2CoreHealthSepaDebitDelayedFiringEventNotification",
    ),
    "v2.core.health.sepa_debit_delayed.resolved": (
        "stripe.events._v2_core_health_sepa_debit_delayed_resolved_event",
        "V2CoreHealthSepaDebitDelayedResolvedEventNotification",
    ),
    "v2.core.health.traffic_volume_drop.firing": (
        "stripe.events._v2_core_health_traffic_volume_drop_firing_event",
        "V2CoreHealthTrafficVolumeDropFiringEventNotification",
    ),
    "v2.core.health.traffic_volume_drop.resolved": (
        "stripe.events._v2_core_health_traffic_volume_drop_resolved_event",
        "V2CoreHealthTrafficVolumeDropResolvedEventNotification",
    ),
    "v2.core.health.webhook_latency.firing": (
        "stripe.events._v2_core_health_webhook_latency_firing_event",
        "V2CoreHealthWebhookLatencyFiringEventNotification",
    ),
    "v2.core.health.webhook_latency.resolved": (
        "stripe.events._v2_core_health_webhook_latency_resolved_event",
        "V2CoreHealthWebhookLatencyResolvedEventNotification",
    ),
    "v2.iam.api_key.created": (
        "stripe.events._v2_iam_api_key_created_event",
        "V2IamApiKeyCreatedEventNotification",
    ),
    "v2.iam.api_key.default_secret_revealed": (
        "stripe.events._v2_iam_api_key_default_secret_revealed_event",
        "V2IamApiKeyDefaultSecretRevealedEventNotification",
    ),
    "v2.iam.api_key.expired": (
        "stripe.events._v2_iam_api_key_expired_event",
        "V2IamApiKeyExpiredEventNotification",
    ),
    "v2.iam.api_key.permissions_updated": (
        "stripe.events._v2_iam_api_key_permissions_updated_event",
        "V2IamApiKeyPermissionsUpdatedEventNotification",
    ),
    "v2.iam.api_key.rotated": (
        "stripe.events._v2_iam_api_key_rotated_event",
        "V2IamApiKeyRotatedEventNotification",
    ),
    "v2.iam.api_key.updated": (
        "stripe.events._v2_iam_api_key_updated_event",
        "V2IamApiKeyUpdatedEventNotification",
    ),
    "v2.money_management.adjustment.created": (
        "stripe.events._v2_money_management_adjustment_created_event",
        "V2MoneyManagementAdjustmentCreatedEventNotification",
    ),
    "v2.money_management.financial_account.created": (
        "stripe.events._v2_money_management_financial_account_created_event",
        "V2MoneyManagementFinancialAccountCreatedEventNotification",
    ),
    "v2.money_management.financial_account.updated": (
        "stripe.events._v2_money_management_financial_account_updated_event",
        "V2MoneyManagementFinancialAccountUpdatedEventNotification",
    ),
    "v2.money_management.financial_address.activated": (
        "stripe.events._v2_money_management_financial_address_activated_event",
        "V2MoneyManagementFinancialAddressActivatedEventNotification",
    ),
    "v2.money_management.financial_address.failed": (
        "stripe.events._v2_money_management_financial_address_failed_event",
        "V2MoneyManagementFinancialAddressFailedEventNotification",
    ),
    "v2.money_management.inbound_transfer.available": (
        "stripe.events._v2_money_management_inbound_transfer_available_event",
        "V2MoneyManagementInboundTransferAvailableEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_failed": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event",
        "V2MoneyManagementInboundTransferBankDebitFailedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_processing": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event",
        "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_queued": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event",
        "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_returned": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event",
        "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification",
    ),
    "v2.money_management.inbound_transfer.bank_debit_succeeded": (
        "stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event",
        "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification",
    ),
    "v2.money_management.outbound_payment.canceled": (
        "stripe.events._v2_money_management_outbound_payment_canceled_event",
        "V2MoneyManagementOutboundPaymentCanceledEventNotification",
    ),
    "v2.money_management.outbound_payment.created": (
        "stripe.events._v2_money_management_outbound_payment_created_event",
        "V2MoneyManagementOutboundPaymentCreatedEventNotification",
    ),
    "v2.money_management.outbound_payment.failed": (
        "stripe.events._v2_money_management_outbound_payment_failed_event",
        "V2MoneyManagementOutboundPaymentFailedEventNotification",
    ),
    "v2.money_management.outbound_payment.posted": (
        "stripe.events._v2_money_management_outbound_payment_posted_event",
        "V2MoneyManagementOutboundPaymentPostedEventNotification",
    ),
    "v2.money_management.outbound_payment.returned": (
        "stripe.events._v2_money_management_outbound_payment_returned_event",
        "V2MoneyManagementOutboundPaymentReturnedEventNotification",
    ),
    "v2.money_management.outbound_payment.updated": (
        "stripe.events._v2_money_management_outbound_payment_updated_event",
        "V2MoneyManagementOutboundPaymentUpdatedEventNotification",
    ),
    "v2.money_management.outbound_transfer.canceled": (
        "stripe.events._v2_money_management_outbound_transfer_canceled_event",
        "V2MoneyManagementOutboundTransferCanceledEventNotification",
    ),
    "v2.money_management.outbound_transfer.created": (
        "stripe.events._v2_money_management_outbound_transfer_created_event",
        "V2MoneyManagementOutboundTransferCreatedEventNotification",
    ),
    "v2.money_management.outbound_transfer.failed": (
        "stripe.events._v2_money_management_outbound_transfer_failed_event",
        "V2MoneyManagementOutboundTransferFailedEventNotification",
    ),
    "v2.money_management.outbound_transfer.posted": (
        "stripe.events._v2_money_management_outbound_transfer_posted_event",
        "V2MoneyManagementOutboundTransferPostedEventNotification",
    ),
    "v2.money_management.outbound_transfer.returned": (
        "stripe.events._v2_money_management_outbound_transfer_returned_event",
        "V2MoneyManagementOutboundTransferReturnedEventNotification",
    ),
    "v2.money_management.outbound_transfer.updated": (
        "stripe.events._v2_money_management_outbound_transfer_updated_event",
        "V2MoneyManagementOutboundTransferUpdatedEventNotification",
    ),
    "v2.money_management.payout_method.created": (
        "stripe.events._v2_money_management_payout_method_created_event",
        "V2MoneyManagementPayoutMethodCreatedEventNotification",
    ),
    "v2.money_management.payout_method.updated": (
        "stripe.events._v2_money_management_payout_method_updated_event",
        "V2MoneyManagementPayoutMethodUpdatedEventNotification",
    ),
    "v2.money_management.received_credit.available": (
        "stripe.events._v2_money_management_received_credit_available_event",
        "V2MoneyManagementReceivedCreditAvailableEventNotification",
    ),
    "v2.money_management.received_credit.failed": (
        "stripe.events._v2_money_management_received_credit_failed_event",
        "V2MoneyManagementReceivedCreditFailedEventNotification",
    ),
    "v2.money_management.received_credit.returned": (
        "stripe.events._v2_money_management_received_credit_returned_event",
        "V2MoneyManagementReceivedCreditReturnedEventNotification",
    ),
    "v2.money_management.received_credit.succeeded": (
        "stripe.events._v2_money_management_received_credit_succeeded_event",
        "V2MoneyManagementReceivedCreditSucceededEventNotification",
    ),
    "v2.money_management.received_debit.canceled": (
        "stripe.events._v2_money_management_received_debit_canceled_event",
        "V2MoneyManagementReceivedDebitCanceledEventNotification",
    ),
    "v2.money_management.received_debit.failed": (
        "stripe.events._v2_money_management_received_debit_failed_event",
        "V2MoneyManagementReceivedDebitFailedEventNotification",
    ),
    "v2.money_management.received_debit.pending": (
        "stripe.events._v2_money_management_received_debit_pending_event",
        "V2MoneyManagementReceivedDebitPendingEventNotification",
    ),
    "v2.money_management.received_debit.succeeded": (
        "stripe.events._v2_money_management_received_debit_succeeded_event",
        "V2MoneyManagementReceivedDebitSucceededEventNotification",
    ),
    "v2.money_management.received_debit.updated": (
        "stripe.events._v2_money_management_received_debit_updated_event",
        "V2MoneyManagementReceivedDebitUpdatedEventNotification",
    ),
    "v2.money_management.recipient_verification.created": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        "V2MoneyManagementRecipientVerificationCreatedEventNotification",
    ),
    "v2.money_management.recipient_verification.updated": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
        "V2MoneyManagementRecipientVerificationUpdatedEventNotification",
    ),
    "v2.money_management.transaction.created": (
        "stripe.events._v2_money_management_transaction_created_event",
        "V2MoneyManagementTransactionCreatedEventNotification",
    ),
    "v2.money_management.transaction.updated": (
        "stripe.events._v2_money_management_transaction_updated_event",
        "V2MoneyManagementTransactionUpdatedEventNotification",
    ),
    "v2.payments.off_session_payment.attempt_failed": (
        "stripe.events._v2_payments_off_session_payment_attempt_failed_event",
        "V2PaymentsOffSessionPaymentAttemptFailedEventNotification",
    ),
    "v2.payments.off_session_payment.attempt_started": (
        "stripe.events._v2_payments_off_session_payment_attempt_started_event",
        "V2PaymentsOffSessionPaymentAttemptStartedEventNotification",
    ),
    "v2.payments.off_session_payment.authorization_attempt_failed": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event",
        "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification",
    ),
    "v2.payments.off_session_payment.authorization_attempt_started": (
        "stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event",
        "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification",
    ),
    "v2.payments.off_session_payment.canceled": (
        "stripe.events._v2_payments_off_session_payment_canceled_event",
        "V2PaymentsOffSessionPaymentCanceledEventNotification",
    ),
    "v2.payments.off_session_payment.created": (
        "stripe.events._v2_payments_off_session_payment_created_event",
        "V2PaymentsOffSessionPaymentCreatedEventNotification",
    ),
    "v2.payments.off_session_payment.failed": (
        "stripe.events._v2_payments_off_session_payment_failed_event",
        "V2PaymentsOffSessionPaymentFailedEventNotification",
    ),
    "v2.payments.off_session_payment.requires_capture": (
        "stripe.events._v2_payments_off_session_payment_requires_capture_event",
        "V2PaymentsOffSessionPaymentRequiresCaptureEventNotification",
    ),
    "v2.payments.off_session_payment.succeeded": (
        "stripe.events._v2_payments_off_session_payment_succeeded_event",
        "V2PaymentsOffSessionPaymentSucceededEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.canceled": (
        "stripe.events._v2_payments_settlement_allocation_intent_canceled_event",
        "V2PaymentsSettlementAllocationIntentCanceledEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.created": (
        "stripe.events._v2_payments_settlement_allocation_intent_created_event",
        "V2PaymentsSettlementAllocationIntentCreatedEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.errored": (
        "stripe.events._v2_payments_settlement_allocation_intent_errored_event",
        "V2PaymentsSettlementAllocationIntentErroredEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.funds_not_received": (
        "stripe.events._v2_payments_settlement_allocation_intent_funds_not_received_event",
        "V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.matched": (
        "stripe.events._v2_payments_settlement_allocation_intent_matched_event",
        "V2PaymentsSettlementAllocationIntentMatchedEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.not_found": (
        "stripe.events._v2_payments_settlement_allocation_intent_not_found_event",
        "V2PaymentsSettlementAllocationIntentNotFoundEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.settled": (
        "stripe.events._v2_payments_settlement_allocation_intent_settled_event",
        "V2PaymentsSettlementAllocationIntentSettledEventNotification",
    ),
    "v2.payments.settlement_allocation_intent_split.canceled": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_canceled_event",
        "V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification",
    ),
    "v2.payments.settlement_allocation_intent_split.created": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_created_event",
        "V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification",
    ),
    "v2.payments.settlement_allocation_intent_split.settled": (
        "stripe.events._v2_payments_settlement_allocation_intent_split_settled_event",
        "V2PaymentsSettlementAllocationIntentSplitSettledEventNotification",
    ),
    "v2.payments.settlement_allocation_intent.submitted": (
        "stripe.events._v2_payments_settlement_allocation_intent_submitted_event",
        "V2PaymentsSettlementAllocationIntentSubmittedEventNotification",
    ),
    "v2.reporting.report_run.created": (
        "stripe.events._v2_reporting_report_run_created_event",
        "V2ReportingReportRunCreatedEventNotification",
    ),
    "v2.reporting.report_run.failed": (
        "stripe.events._v2_reporting_report_run_failed_event",
        "V2ReportingReportRunFailedEventNotification",
    ),
    "v2.reporting.report_run.succeeded": (
        "stripe.events._v2_reporting_report_run_succeeded_event",
        "V2ReportingReportRunSucceededEventNotification",
    ),
    "v2.reporting.report_run.updated": (
        "stripe.events._v2_reporting_report_run_updated_event",
        "V2ReportingReportRunUpdatedEventNotification",
    ),
}


def get_v2_event_notification_class(type_: str):
    if type_ not in _V2_EVENT_NOTIFICATION_CLASS_LOOKUP:
        return UnknownEventNotification

    import_path, class_name = _V2_EVENT_NOTIFICATION_CLASS_LOOKUP[type_]
    return getattr(
        import_module(import_path),
        class_name,
    )


ALL_EVENT_NOTIFICATIONS = Union[
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V2BillingCadenceBilledEventNotification",
    "V2BillingCadenceCanceledEventNotification",
    "V2BillingCadenceCreatedEventNotification",
    "V2BillingLicensedItemCreatedEventNotification",
    "V2BillingLicensedItemUpdatedEventNotification",
    "V2BillingLicenseFeeCreatedEventNotification",
    "V2BillingLicenseFeeUpdatedEventNotification",
    "V2BillingLicenseFeeVersionCreatedEventNotification",
    "V2BillingMeteredItemCreatedEventNotification",
    "V2BillingMeteredItemUpdatedEventNotification",
    "V2BillingPricingPlanComponentCreatedEventNotification",
    "V2BillingPricingPlanComponentUpdatedEventNotification",
    "V2BillingPricingPlanCreatedEventNotification",
    "V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification",
    "V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification",
    "V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification",
    "V2BillingPricingPlanSubscriptionCollectionPausedEventNotification",
    "V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification",
    "V2BillingPricingPlanSubscriptionServicingActivatedEventNotification",
    "V2BillingPricingPlanSubscriptionServicingCanceledEventNotification",
    "V2BillingPricingPlanSubscriptionServicingPausedEventNotification",
    "V2BillingPricingPlanUpdatedEventNotification",
    "V2BillingPricingPlanVersionCreatedEventNotification",
    "V2BillingRateCardCreatedEventNotification",
    "V2BillingRateCardRateCreatedEventNotification",
    "V2BillingRateCardSubscriptionActivatedEventNotification",
    "V2BillingRateCardSubscriptionCanceledEventNotification",
    "V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification",
    "V2BillingRateCardSubscriptionCollectionCurrentEventNotification",
    "V2BillingRateCardSubscriptionCollectionPastDueEventNotification",
    "V2BillingRateCardSubscriptionCollectionPausedEventNotification",
    "V2BillingRateCardSubscriptionCollectionUnpaidEventNotification",
    "V2BillingRateCardSubscriptionServicingActivatedEventNotification",
    "V2BillingRateCardSubscriptionServicingCanceledEventNotification",
    "V2BillingRateCardSubscriptionServicingPausedEventNotification",
    "V2BillingRateCardUpdatedEventNotification",
    "V2BillingRateCardVersionCreatedEventNotification",
    "V2CoreAccountClosedEventNotification",
    "V2CoreAccountCreatedEventNotification",
    "V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification",
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification",
    "V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification",
    "V2CoreAccountIncludingIdentityUpdatedEventNotification",
    "V2CoreAccountIncludingRequirementsUpdatedEventNotification",
    "V2CoreAccountLinkReturnedEventNotification",
    "V2CoreAccountPersonCreatedEventNotification",
    "V2CoreAccountPersonDeletedEventNotification",
    "V2CoreAccountPersonUpdatedEventNotification",
    "V2CoreAccountUpdatedEventNotification",
    "V2CoreClaimableSandboxClaimedEventNotification",
    "V2CoreClaimableSandboxCreatedEventNotification",
    "V2CoreClaimableSandboxExpiredEventNotification",
    "V2CoreClaimableSandboxExpiringEventNotification",
    "V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification",
    "V2CoreEventDestinationPingEventNotification",
    "V2CoreHealthApiErrorFiringEventNotification",
    "V2CoreHealthApiErrorResolvedEventNotification",
    "V2CoreHealthApiLatencyFiringEventNotification",
    "V2CoreHealthApiLatencyResolvedEventNotification",
    "V2CoreHealthAuthorizationRateDropFiringEventNotification",
    "V2CoreHealthAuthorizationRateDropResolvedEventNotification",
    "V2CoreHealthEventGenerationFailureResolvedEventNotification",
    "V2CoreHealthFraudRateIncreasedEventNotification",
    "V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification",
    "V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification",
    "V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification",
    "V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification",
    "V2CoreHealthPaymentMethodErrorFiringEventNotification",
    "V2CoreHealthPaymentMethodErrorResolvedEventNotification",
    "V2CoreHealthSepaDebitDelayedFiringEventNotification",
    "V2CoreHealthSepaDebitDelayedResolvedEventNotification",
    "V2CoreHealthTrafficVolumeDropFiringEventNotification",
    "V2CoreHealthTrafficVolumeDropResolvedEventNotification",
    "V2CoreHealthWebhookLatencyFiringEventNotification",
    "V2CoreHealthWebhookLatencyResolvedEventNotification",
    "V2IamApiKeyCreatedEventNotification",
    "V2IamApiKeyDefaultSecretRevealedEventNotification",
    "V2IamApiKeyExpiredEventNotification",
    "V2IamApiKeyPermissionsUpdatedEventNotification",
    "V2IamApiKeyRotatedEventNotification",
    "V2IamApiKeyUpdatedEventNotification",
    "V2MoneyManagementAdjustmentCreatedEventNotification",
    "V2MoneyManagementFinancialAccountCreatedEventNotification",
    "V2MoneyManagementFinancialAccountUpdatedEventNotification",
    "V2MoneyManagementFinancialAddressActivatedEventNotification",
    "V2MoneyManagementFinancialAddressFailedEventNotification",
    "V2MoneyManagementInboundTransferAvailableEventNotification",
    "V2MoneyManagementInboundTransferBankDebitFailedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitProcessingEventNotification",
    "V2MoneyManagementInboundTransferBankDebitQueuedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitReturnedEventNotification",
    "V2MoneyManagementInboundTransferBankDebitSucceededEventNotification",
    "V2MoneyManagementOutboundPaymentCanceledEventNotification",
    "V2MoneyManagementOutboundPaymentCreatedEventNotification",
    "V2MoneyManagementOutboundPaymentFailedEventNotification",
    "V2MoneyManagementOutboundPaymentPostedEventNotification",
    "V2MoneyManagementOutboundPaymentReturnedEventNotification",
    "V2MoneyManagementOutboundPaymentUpdatedEventNotification",
    "V2MoneyManagementOutboundTransferCanceledEventNotification",
    "V2MoneyManagementOutboundTransferCreatedEventNotification",
    "V2MoneyManagementOutboundTransferFailedEventNotification",
    "V2MoneyManagementOutboundTransferPostedEventNotification",
    "V2MoneyManagementOutboundTransferReturnedEventNotification",
    "V2MoneyManagementOutboundTransferUpdatedEventNotification",
    "V2MoneyManagementPayoutMethodCreatedEventNotification",
    "V2MoneyManagementPayoutMethodUpdatedEventNotification",
    "V2MoneyManagementReceivedCreditAvailableEventNotification",
    "V2MoneyManagementReceivedCreditFailedEventNotification",
    "V2MoneyManagementReceivedCreditReturnedEventNotification",
    "V2MoneyManagementReceivedCreditSucceededEventNotification",
    "V2MoneyManagementReceivedDebitCanceledEventNotification",
    "V2MoneyManagementReceivedDebitFailedEventNotification",
    "V2MoneyManagementReceivedDebitPendingEventNotification",
    "V2MoneyManagementReceivedDebitSucceededEventNotification",
    "V2MoneyManagementReceivedDebitUpdatedEventNotification",
    "V2MoneyManagementRecipientVerificationCreatedEventNotification",
    "V2MoneyManagementRecipientVerificationUpdatedEventNotification",
    "V2MoneyManagementTransactionCreatedEventNotification",
    "V2MoneyManagementTransactionUpdatedEventNotification",
    "V2PaymentsOffSessionPaymentAttemptFailedEventNotification",
    "V2PaymentsOffSessionPaymentAttemptStartedEventNotification",
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification",
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification",
    "V2PaymentsOffSessionPaymentCanceledEventNotification",
    "V2PaymentsOffSessionPaymentCreatedEventNotification",
    "V2PaymentsOffSessionPaymentFailedEventNotification",
    "V2PaymentsOffSessionPaymentRequiresCaptureEventNotification",
    "V2PaymentsOffSessionPaymentSucceededEventNotification",
    "V2PaymentsSettlementAllocationIntentCanceledEventNotification",
    "V2PaymentsSettlementAllocationIntentCreatedEventNotification",
    "V2PaymentsSettlementAllocationIntentErroredEventNotification",
    "V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification",
    "V2PaymentsSettlementAllocationIntentMatchedEventNotification",
    "V2PaymentsSettlementAllocationIntentNotFoundEventNotification",
    "V2PaymentsSettlementAllocationIntentSettledEventNotification",
    "V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification",
    "V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification",
    "V2PaymentsSettlementAllocationIntentSplitSettledEventNotification",
    "V2PaymentsSettlementAllocationIntentSubmittedEventNotification",
    "V2ReportingReportRunCreatedEventNotification",
    "V2ReportingReportRunFailedEventNotification",
    "V2ReportingReportRunSucceededEventNotification",
    "V2ReportingReportRunUpdatedEventNotification",
]
