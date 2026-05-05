# -*- coding: utf-8 -*-
# File copied from our code generator; changes here will be overwritten.
from dataclasses import dataclass
from typing_extensions import TYPE_CHECKING

from typing import TypeVar, Callable, List

# Import at runtime for isinstance check and type annotations
from stripe.v2.core._event import EventNotification, UnknownEventNotification

if TYPE_CHECKING:
    from stripe._stripe_client import StripeClient

    # event-notification-types: The beginning of the section generated from our OpenAPI spec
    from stripe.events._v1_account_application_authorized_event import (
        V1AccountApplicationAuthorizedEventNotification,
    )
    from stripe.events._v1_account_application_deauthorized_event import (
        V1AccountApplicationDeauthorizedEventNotification,
    )
    from stripe.events._v1_account_external_account_created_event import (
        V1AccountExternalAccountCreatedEventNotification,
    )
    from stripe.events._v1_account_external_account_deleted_event import (
        V1AccountExternalAccountDeletedEventNotification,
    )
    from stripe.events._v1_account_external_account_updated_event import (
        V1AccountExternalAccountUpdatedEventNotification,
    )
    from stripe.events._v1_account_signals_including_delinquency_created_event import (
        V1AccountSignalsIncludingDelinquencyCreatedEventNotification,
    )
    from stripe.events._v1_account_updated_event import (
        V1AccountUpdatedEventNotification,
    )
    from stripe.events._v1_application_fee_created_event import (
        V1ApplicationFeeCreatedEventNotification,
    )
    from stripe.events._v1_application_fee_refunded_event import (
        V1ApplicationFeeRefundedEventNotification,
    )
    from stripe.events._v1_application_fee_refund_updated_event import (
        V1ApplicationFeeRefundUpdatedEventNotification,
    )
    from stripe.events._v1_balance_available_event import (
        V1BalanceAvailableEventNotification,
    )
    from stripe.events._v1_billing_alert_triggered_event import (
        V1BillingAlertTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v1_billing_portal_configuration_created_event import (
        V1BillingPortalConfigurationCreatedEventNotification,
    )
    from stripe.events._v1_billing_portal_configuration_updated_event import (
        V1BillingPortalConfigurationUpdatedEventNotification,
    )
    from stripe.events._v1_billing_portal_session_created_event import (
        V1BillingPortalSessionCreatedEventNotification,
    )
    from stripe.events._v1_capability_updated_event import (
        V1CapabilityUpdatedEventNotification,
    )
    from stripe.events._v1_cash_balance_funds_available_event import (
        V1CashBalanceFundsAvailableEventNotification,
    )
    from stripe.events._v1_charge_captured_event import (
        V1ChargeCapturedEventNotification,
    )
    from stripe.events._v1_charge_dispute_closed_event import (
        V1ChargeDisputeClosedEventNotification,
    )
    from stripe.events._v1_charge_dispute_created_event import (
        V1ChargeDisputeCreatedEventNotification,
    )
    from stripe.events._v1_charge_dispute_funds_reinstated_event import (
        V1ChargeDisputeFundsReinstatedEventNotification,
    )
    from stripe.events._v1_charge_dispute_funds_withdrawn_event import (
        V1ChargeDisputeFundsWithdrawnEventNotification,
    )
    from stripe.events._v1_charge_dispute_updated_event import (
        V1ChargeDisputeUpdatedEventNotification,
    )
    from stripe.events._v1_charge_expired_event import (
        V1ChargeExpiredEventNotification,
    )
    from stripe.events._v1_charge_failed_event import (
        V1ChargeFailedEventNotification,
    )
    from stripe.events._v1_charge_pending_event import (
        V1ChargePendingEventNotification,
    )
    from stripe.events._v1_charge_refunded_event import (
        V1ChargeRefundedEventNotification,
    )
    from stripe.events._v1_charge_refund_updated_event import (
        V1ChargeRefundUpdatedEventNotification,
    )
    from stripe.events._v1_charge_succeeded_event import (
        V1ChargeSucceededEventNotification,
    )
    from stripe.events._v1_charge_updated_event import (
        V1ChargeUpdatedEventNotification,
    )
    from stripe.events._v1_checkout_session_async_payment_failed_event import (
        V1CheckoutSessionAsyncPaymentFailedEventNotification,
    )
    from stripe.events._v1_checkout_session_async_payment_succeeded_event import (
        V1CheckoutSessionAsyncPaymentSucceededEventNotification,
    )
    from stripe.events._v1_checkout_session_completed_event import (
        V1CheckoutSessionCompletedEventNotification,
    )
    from stripe.events._v1_checkout_session_expired_event import (
        V1CheckoutSessionExpiredEventNotification,
    )
    from stripe.events._v1_climate_order_canceled_event import (
        V1ClimateOrderCanceledEventNotification,
    )
    from stripe.events._v1_climate_order_created_event import (
        V1ClimateOrderCreatedEventNotification,
    )
    from stripe.events._v1_climate_order_delayed_event import (
        V1ClimateOrderDelayedEventNotification,
    )
    from stripe.events._v1_climate_order_delivered_event import (
        V1ClimateOrderDeliveredEventNotification,
    )
    from stripe.events._v1_climate_order_product_substituted_event import (
        V1ClimateOrderProductSubstitutedEventNotification,
    )
    from stripe.events._v1_climate_product_created_event import (
        V1ClimateProductCreatedEventNotification,
    )
    from stripe.events._v1_climate_product_pricing_updated_event import (
        V1ClimateProductPricingUpdatedEventNotification,
    )
    from stripe.events._v1_coupon_created_event import (
        V1CouponCreatedEventNotification,
    )
    from stripe.events._v1_coupon_deleted_event import (
        V1CouponDeletedEventNotification,
    )
    from stripe.events._v1_coupon_updated_event import (
        V1CouponUpdatedEventNotification,
    )
    from stripe.events._v1_credit_note_created_event import (
        V1CreditNoteCreatedEventNotification,
    )
    from stripe.events._v1_credit_note_updated_event import (
        V1CreditNoteUpdatedEventNotification,
    )
    from stripe.events._v1_credit_note_voided_event import (
        V1CreditNoteVoidedEventNotification,
    )
    from stripe.events._v1_customer_cash_balance_transaction_created_event import (
        V1CustomerCashBalanceTransactionCreatedEventNotification,
    )
    from stripe.events._v1_customer_created_event import (
        V1CustomerCreatedEventNotification,
    )
    from stripe.events._v1_customer_deleted_event import (
        V1CustomerDeletedEventNotification,
    )
    from stripe.events._v1_customer_subscription_created_event import (
        V1CustomerSubscriptionCreatedEventNotification,
    )
    from stripe.events._v1_customer_subscription_deleted_event import (
        V1CustomerSubscriptionDeletedEventNotification,
    )
    from stripe.events._v1_customer_subscription_paused_event import (
        V1CustomerSubscriptionPausedEventNotification,
    )
    from stripe.events._v1_customer_subscription_pending_update_applied_event import (
        V1CustomerSubscriptionPendingUpdateAppliedEventNotification,
    )
    from stripe.events._v1_customer_subscription_pending_update_expired_event import (
        V1CustomerSubscriptionPendingUpdateExpiredEventNotification,
    )
    from stripe.events._v1_customer_subscription_resumed_event import (
        V1CustomerSubscriptionResumedEventNotification,
    )
    from stripe.events._v1_customer_subscription_trial_will_end_event import (
        V1CustomerSubscriptionTrialWillEndEventNotification,
    )
    from stripe.events._v1_customer_subscription_updated_event import (
        V1CustomerSubscriptionUpdatedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_created_event import (
        V1CustomerTaxIdCreatedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_deleted_event import (
        V1CustomerTaxIdDeletedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_updated_event import (
        V1CustomerTaxIdUpdatedEventNotification,
    )
    from stripe.events._v1_customer_updated_event import (
        V1CustomerUpdatedEventNotification,
    )
    from stripe.events._v1_entitlements_active_entitlement_summary_updated_event import (
        V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification,
    )
    from stripe.events._v1_file_created_event import (
        V1FileCreatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_created_event import (
        V1FinancialConnectionsAccountCreatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_deactivated_event import (
        V1FinancialConnectionsAccountDeactivatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_disconnected_event import (
        V1FinancialConnectionsAccountDisconnectedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_reactivated_event import (
        V1FinancialConnectionsAccountReactivatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_balance_event import (
        V1FinancialConnectionsAccountRefreshedBalanceEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_ownership_event import (
        V1FinancialConnectionsAccountRefreshedOwnershipEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_transactions_event import (
        V1FinancialConnectionsAccountRefreshedTransactionsEventNotification,
    )
    from stripe.events._v1_identity_verification_session_canceled_event import (
        V1IdentityVerificationSessionCanceledEventNotification,
    )
    from stripe.events._v1_identity_verification_session_created_event import (
        V1IdentityVerificationSessionCreatedEventNotification,
    )
    from stripe.events._v1_identity_verification_session_processing_event import (
        V1IdentityVerificationSessionProcessingEventNotification,
    )
    from stripe.events._v1_identity_verification_session_redacted_event import (
        V1IdentityVerificationSessionRedactedEventNotification,
    )
    from stripe.events._v1_identity_verification_session_requires_input_event import (
        V1IdentityVerificationSessionRequiresInputEventNotification,
    )
    from stripe.events._v1_identity_verification_session_verified_event import (
        V1IdentityVerificationSessionVerifiedEventNotification,
    )
    from stripe.events._v1_invoice_created_event import (
        V1InvoiceCreatedEventNotification,
    )
    from stripe.events._v1_invoice_deleted_event import (
        V1InvoiceDeletedEventNotification,
    )
    from stripe.events._v1_invoice_finalization_failed_event import (
        V1InvoiceFinalizationFailedEventNotification,
    )
    from stripe.events._v1_invoice_finalized_event import (
        V1InvoiceFinalizedEventNotification,
    )
    from stripe.events._v1_invoiceitem_created_event import (
        V1InvoiceitemCreatedEventNotification,
    )
    from stripe.events._v1_invoiceitem_deleted_event import (
        V1InvoiceitemDeletedEventNotification,
    )
    from stripe.events._v1_invoice_marked_uncollectible_event import (
        V1InvoiceMarkedUncollectibleEventNotification,
    )
    from stripe.events._v1_invoice_overdue_event import (
        V1InvoiceOverdueEventNotification,
    )
    from stripe.events._v1_invoice_overpaid_event import (
        V1InvoiceOverpaidEventNotification,
    )
    from stripe.events._v1_invoice_paid_event import (
        V1InvoicePaidEventNotification,
    )
    from stripe.events._v1_invoice_payment_action_required_event import (
        V1InvoicePaymentActionRequiredEventNotification,
    )
    from stripe.events._v1_invoice_payment_failed_event import (
        V1InvoicePaymentFailedEventNotification,
    )
    from stripe.events._v1_invoice_payment_paid_event import (
        V1InvoicePaymentPaidEventNotification,
    )
    from stripe.events._v1_invoice_payment_succeeded_event import (
        V1InvoicePaymentSucceededEventNotification,
    )
    from stripe.events._v1_invoice_sent_event import (
        V1InvoiceSentEventNotification,
    )
    from stripe.events._v1_invoice_upcoming_event import (
        V1InvoiceUpcomingEventNotification,
    )
    from stripe.events._v1_invoice_updated_event import (
        V1InvoiceUpdatedEventNotification,
    )
    from stripe.events._v1_invoice_voided_event import (
        V1InvoiceVoidedEventNotification,
    )
    from stripe.events._v1_invoice_will_be_due_event import (
        V1InvoiceWillBeDueEventNotification,
    )
    from stripe.events._v1_issuing_authorization_created_event import (
        V1IssuingAuthorizationCreatedEventNotification,
    )
    from stripe.events._v1_issuing_authorization_request_event import (
        V1IssuingAuthorizationRequestEventNotification,
    )
    from stripe.events._v1_issuing_authorization_updated_event import (
        V1IssuingAuthorizationUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_card_created_event import (
        V1IssuingCardCreatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_created_event import (
        V1IssuingCardholderCreatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_updated_event import (
        V1IssuingCardholderUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_card_updated_event import (
        V1IssuingCardUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_closed_event import (
        V1IssuingDisputeClosedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_created_event import (
        V1IssuingDisputeCreatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_funds_reinstated_event import (
        V1IssuingDisputeFundsReinstatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_funds_rescinded_event import (
        V1IssuingDisputeFundsRescindedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_submitted_event import (
        V1IssuingDisputeSubmittedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_updated_event import (
        V1IssuingDisputeUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_activated_event import (
        V1IssuingPersonalizationDesignActivatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_deactivated_event import (
        V1IssuingPersonalizationDesignDeactivatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_rejected_event import (
        V1IssuingPersonalizationDesignRejectedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_updated_event import (
        V1IssuingPersonalizationDesignUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_token_created_event import (
        V1IssuingTokenCreatedEventNotification,
    )
    from stripe.events._v1_issuing_token_updated_event import (
        V1IssuingTokenUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_created_event import (
        V1IssuingTransactionCreatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event import (
        V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_updated_event import (
        V1IssuingTransactionUpdatedEventNotification,
    )
    from stripe.events._v1_mandate_updated_event import (
        V1MandateUpdatedEventNotification,
    )
    from stripe.events._v1_payment_intent_amount_capturable_updated_event import (
        V1PaymentIntentAmountCapturableUpdatedEventNotification,
    )
    from stripe.events._v1_payment_intent_canceled_event import (
        V1PaymentIntentCanceledEventNotification,
    )
    from stripe.events._v1_payment_intent_created_event import (
        V1PaymentIntentCreatedEventNotification,
    )
    from stripe.events._v1_payment_intent_partially_funded_event import (
        V1PaymentIntentPartiallyFundedEventNotification,
    )
    from stripe.events._v1_payment_intent_payment_failed_event import (
        V1PaymentIntentPaymentFailedEventNotification,
    )
    from stripe.events._v1_payment_intent_processing_event import (
        V1PaymentIntentProcessingEventNotification,
    )
    from stripe.events._v1_payment_intent_requires_action_event import (
        V1PaymentIntentRequiresActionEventNotification,
    )
    from stripe.events._v1_payment_intent_succeeded_event import (
        V1PaymentIntentSucceededEventNotification,
    )
    from stripe.events._v1_payment_link_created_event import (
        V1PaymentLinkCreatedEventNotification,
    )
    from stripe.events._v1_payment_link_updated_event import (
        V1PaymentLinkUpdatedEventNotification,
    )
    from stripe.events._v1_payment_method_attached_event import (
        V1PaymentMethodAttachedEventNotification,
    )
    from stripe.events._v1_payment_method_automatically_updated_event import (
        V1PaymentMethodAutomaticallyUpdatedEventNotification,
    )
    from stripe.events._v1_payment_method_detached_event import (
        V1PaymentMethodDetachedEventNotification,
    )
    from stripe.events._v1_payment_method_updated_event import (
        V1PaymentMethodUpdatedEventNotification,
    )
    from stripe.events._v1_payout_canceled_event import (
        V1PayoutCanceledEventNotification,
    )
    from stripe.events._v1_payout_created_event import (
        V1PayoutCreatedEventNotification,
    )
    from stripe.events._v1_payout_failed_event import (
        V1PayoutFailedEventNotification,
    )
    from stripe.events._v1_payout_paid_event import (
        V1PayoutPaidEventNotification,
    )
    from stripe.events._v1_payout_reconciliation_completed_event import (
        V1PayoutReconciliationCompletedEventNotification,
    )
    from stripe.events._v1_payout_updated_event import (
        V1PayoutUpdatedEventNotification,
    )
    from stripe.events._v1_person_created_event import (
        V1PersonCreatedEventNotification,
    )
    from stripe.events._v1_person_deleted_event import (
        V1PersonDeletedEventNotification,
    )
    from stripe.events._v1_person_updated_event import (
        V1PersonUpdatedEventNotification,
    )
    from stripe.events._v1_plan_created_event import (
        V1PlanCreatedEventNotification,
    )
    from stripe.events._v1_plan_deleted_event import (
        V1PlanDeletedEventNotification,
    )
    from stripe.events._v1_plan_updated_event import (
        V1PlanUpdatedEventNotification,
    )
    from stripe.events._v1_price_created_event import (
        V1PriceCreatedEventNotification,
    )
    from stripe.events._v1_price_deleted_event import (
        V1PriceDeletedEventNotification,
    )
    from stripe.events._v1_price_updated_event import (
        V1PriceUpdatedEventNotification,
    )
    from stripe.events._v1_product_created_event import (
        V1ProductCreatedEventNotification,
    )
    from stripe.events._v1_product_deleted_event import (
        V1ProductDeletedEventNotification,
    )
    from stripe.events._v1_product_updated_event import (
        V1ProductUpdatedEventNotification,
    )
    from stripe.events._v1_promotion_code_created_event import (
        V1PromotionCodeCreatedEventNotification,
    )
    from stripe.events._v1_promotion_code_updated_event import (
        V1PromotionCodeUpdatedEventNotification,
    )
    from stripe.events._v1_quote_accepted_event import (
        V1QuoteAcceptedEventNotification,
    )
    from stripe.events._v1_quote_canceled_event import (
        V1QuoteCanceledEventNotification,
    )
    from stripe.events._v1_quote_created_event import (
        V1QuoteCreatedEventNotification,
    )
    from stripe.events._v1_quote_finalized_event import (
        V1QuoteFinalizedEventNotification,
    )
    from stripe.events._v1_radar_early_fraud_warning_created_event import (
        V1RadarEarlyFraudWarningCreatedEventNotification,
    )
    from stripe.events._v1_radar_early_fraud_warning_updated_event import (
        V1RadarEarlyFraudWarningUpdatedEventNotification,
    )
    from stripe.events._v1_refund_created_event import (
        V1RefundCreatedEventNotification,
    )
    from stripe.events._v1_refund_failed_event import (
        V1RefundFailedEventNotification,
    )
    from stripe.events._v1_refund_updated_event import (
        V1RefundUpdatedEventNotification,
    )
    from stripe.events._v1_review_closed_event import (
        V1ReviewClosedEventNotification,
    )
    from stripe.events._v1_review_opened_event import (
        V1ReviewOpenedEventNotification,
    )
    from stripe.events._v1_setup_intent_canceled_event import (
        V1SetupIntentCanceledEventNotification,
    )
    from stripe.events._v1_setup_intent_created_event import (
        V1SetupIntentCreatedEventNotification,
    )
    from stripe.events._v1_setup_intent_requires_action_event import (
        V1SetupIntentRequiresActionEventNotification,
    )
    from stripe.events._v1_setup_intent_setup_failed_event import (
        V1SetupIntentSetupFailedEventNotification,
    )
    from stripe.events._v1_setup_intent_succeeded_event import (
        V1SetupIntentSucceededEventNotification,
    )
    from stripe.events._v1_sigma_scheduled_query_run_created_event import (
        V1SigmaScheduledQueryRunCreatedEventNotification,
    )
    from stripe.events._v1_source_canceled_event import (
        V1SourceCanceledEventNotification,
    )
    from stripe.events._v1_source_chargeable_event import (
        V1SourceChargeableEventNotification,
    )
    from stripe.events._v1_source_failed_event import (
        V1SourceFailedEventNotification,
    )
    from stripe.events._v1_source_refund_attributes_required_event import (
        V1SourceRefundAttributesRequiredEventNotification,
    )
    from stripe.events._v1_subscription_schedule_aborted_event import (
        V1SubscriptionScheduleAbortedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_canceled_event import (
        V1SubscriptionScheduleCanceledEventNotification,
    )
    from stripe.events._v1_subscription_schedule_completed_event import (
        V1SubscriptionScheduleCompletedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_created_event import (
        V1SubscriptionScheduleCreatedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_expiring_event import (
        V1SubscriptionScheduleExpiringEventNotification,
    )
    from stripe.events._v1_subscription_schedule_released_event import (
        V1SubscriptionScheduleReleasedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_updated_event import (
        V1SubscriptionScheduleUpdatedEventNotification,
    )
    from stripe.events._v1_tax_rate_created_event import (
        V1TaxRateCreatedEventNotification,
    )
    from stripe.events._v1_tax_rate_updated_event import (
        V1TaxRateUpdatedEventNotification,
    )
    from stripe.events._v1_tax_settings_updated_event import (
        V1TaxSettingsUpdatedEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_failed_event import (
        V1TerminalReaderActionFailedEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_succeeded_event import (
        V1TerminalReaderActionSucceededEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_updated_event import (
        V1TerminalReaderActionUpdatedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_advancing_event import (
        V1TestHelpersTestClockAdvancingEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_created_event import (
        V1TestHelpersTestClockCreatedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_deleted_event import (
        V1TestHelpersTestClockDeletedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_internal_failure_event import (
        V1TestHelpersTestClockInternalFailureEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_ready_event import (
        V1TestHelpersTestClockReadyEventNotification,
    )
    from stripe.events._v1_topup_canceled_event import (
        V1TopupCanceledEventNotification,
    )
    from stripe.events._v1_topup_created_event import (
        V1TopupCreatedEventNotification,
    )
    from stripe.events._v1_topup_failed_event import (
        V1TopupFailedEventNotification,
    )
    from stripe.events._v1_topup_reversed_event import (
        V1TopupReversedEventNotification,
    )
    from stripe.events._v1_topup_succeeded_event import (
        V1TopupSucceededEventNotification,
    )
    from stripe.events._v1_transfer_created_event import (
        V1TransferCreatedEventNotification,
    )
    from stripe.events._v1_transfer_reversed_event import (
        V1TransferReversedEventNotification,
    )
    from stripe.events._v1_transfer_updated_event import (
        V1TransferUpdatedEventNotification,
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
    from stripe.events._v2_billing_rate_card_custom_pricing_unit_overage_rate_created_event import (
        V2BillingRateCardCustomPricingUnitOverageRateCreatedEventNotification,
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
    from stripe.events._v2_core_account_signals_fraudulent_website_ready_event import (
        V2CoreAccountSignalsFraudulentWebsiteReadyEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEventNotification,
    )
    from stripe.events._v2_core_approval_request_approved_event import (
        V2CoreApprovalRequestApprovedEventNotification,
    )
    from stripe.events._v2_core_approval_request_canceled_event import (
        V2CoreApprovalRequestCanceledEventNotification,
    )
    from stripe.events._v2_core_approval_request_created_event import (
        V2CoreApprovalRequestCreatedEventNotification,
    )
    from stripe.events._v2_core_approval_request_expired_event import (
        V2CoreApprovalRequestExpiredEventNotification,
    )
    from stripe.events._v2_core_approval_request_failed_event import (
        V2CoreApprovalRequestFailedEventNotification,
    )
    from stripe.events._v2_core_approval_request_rejected_event import (
        V2CoreApprovalRequestRejectedEventNotification,
    )
    from stripe.events._v2_core_approval_request_succeeded_event import (
        V2CoreApprovalRequestSucceededEventNotification,
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
    from stripe.events._v2_core_claimable_sandbox_updated_event import (
        V2CoreClaimableSandboxUpdatedEventNotification,
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
    from stripe.events._v2_core_health_meter_event_summaries_delayed_firing_event import (
        V2CoreHealthMeterEventSummariesDelayedFiringEventNotification,
    )
    from stripe.events._v2_core_health_meter_event_summaries_delayed_resolved_event import (
        V2CoreHealthMeterEventSummariesDelayedResolvedEventNotification,
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
    from stripe.events._v2_extend_extension_run_failed_event import (
        V2ExtendExtensionRunFailedEventNotification,
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
    from stripe.events._v2_iam_stripe_access_grant_approved_event import (
        V2IamStripeAccessGrantApprovedEventNotification,
    )
    from stripe.events._v2_iam_stripe_access_grant_canceled_event import (
        V2IamStripeAccessGrantCanceledEventNotification,
    )
    from stripe.events._v2_iam_stripe_access_grant_denied_event import (
        V2IamStripeAccessGrantDeniedEventNotification,
    )
    from stripe.events._v2_iam_stripe_access_grant_removed_event import (
        V2IamStripeAccessGrantRemovedEventNotification,
    )
    from stripe.events._v2_iam_stripe_access_grant_requested_event import (
        V2IamStripeAccessGrantRequestedEventNotification,
    )
    from stripe.events._v2_iam_stripe_access_grant_updated_event import (
        V2IamStripeAccessGrantUpdatedEventNotification,
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
    from stripe.events._v2_payments_off_session_payment_paused_event import (
        V2PaymentsOffSessionPaymentPausedEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_requires_capture_event import (
        V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    )
    from stripe.events._v2_payments_off_session_payment_resumed_event import (
        V2PaymentsOffSessionPaymentResumedEventNotification,
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
    from stripe.events._v2_signals_account_signal_fraudulent_merchant_ready_event import (
        V2SignalsAccountSignalFraudulentMerchantReadyEventNotification,
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
    def on_v1_account_application_authorized(
        self,
        func: "Callable[[V1AccountApplicationAuthorizedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountApplicationAuthorizedEvent` (`v1.account.application.authorized`) event notification.
        """
        self._register(
            "v1.account.application.authorized",
            func,
        )
        return func

    def on_v1_account_application_deauthorized(
        self,
        func: "Callable[[V1AccountApplicationDeauthorizedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountApplicationDeauthorizedEvent` (`v1.account.application.deauthorized`) event notification.
        """
        self._register(
            "v1.account.application.deauthorized",
            func,
        )
        return func

    def on_v1_account_external_account_created(
        self,
        func: "Callable[[V1AccountExternalAccountCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountExternalAccountCreatedEvent` (`v1.account.external_account.created`) event notification.
        """
        self._register(
            "v1.account.external_account.created",
            func,
        )
        return func

    def on_v1_account_external_account_deleted(
        self,
        func: "Callable[[V1AccountExternalAccountDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountExternalAccountDeletedEvent` (`v1.account.external_account.deleted`) event notification.
        """
        self._register(
            "v1.account.external_account.deleted",
            func,
        )
        return func

    def on_v1_account_external_account_updated(
        self,
        func: "Callable[[V1AccountExternalAccountUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountExternalAccountUpdatedEvent` (`v1.account.external_account.updated`) event notification.
        """
        self._register(
            "v1.account.external_account.updated",
            func,
        )
        return func

    def on_v1_account_signals_including_delinquency_created(
        self,
        func: "Callable[[V1AccountSignalsIncludingDelinquencyCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountSignalsIncludingDelinquencyCreatedEvent` (`v1.account_signals[delinquency].created`) event notification.
        """
        self._register(
            "v1.account_signals[delinquency].created",
            func,
        )
        return func

    def on_v1_account_updated(
        self,
        func: "Callable[[V1AccountUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1AccountUpdatedEvent` (`v1.account.updated`) event notification.
        """
        self._register(
            "v1.account.updated",
            func,
        )
        return func

    def on_v1_application_fee_created(
        self,
        func: "Callable[[V1ApplicationFeeCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ApplicationFeeCreatedEvent` (`v1.application_fee.created`) event notification.
        """
        self._register(
            "v1.application_fee.created",
            func,
        )
        return func

    def on_v1_application_fee_refunded(
        self,
        func: "Callable[[V1ApplicationFeeRefundedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ApplicationFeeRefundedEvent` (`v1.application_fee.refunded`) event notification.
        """
        self._register(
            "v1.application_fee.refunded",
            func,
        )
        return func

    def on_v1_application_fee_refund_updated(
        self,
        func: "Callable[[V1ApplicationFeeRefundUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ApplicationFeeRefundUpdatedEvent` (`v1.application_fee.refund.updated`) event notification.
        """
        self._register(
            "v1.application_fee.refund.updated",
            func,
        )
        return func

    def on_v1_balance_available(
        self,
        func: "Callable[[V1BalanceAvailableEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1BalanceAvailableEvent` (`v1.balance.available`) event notification.
        """
        self._register(
            "v1.balance.available",
            func,
        )
        return func

    def on_v1_billing_alert_triggered(
        self,
        func: "Callable[[V1BillingAlertTriggeredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1BillingAlertTriggeredEvent` (`v1.billing.alert.triggered`) event notification.
        """
        self._register(
            "v1.billing.alert.triggered",
            func,
        )
        return func

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

    def on_v1_billing_portal_configuration_created(
        self,
        func: "Callable[[V1BillingPortalConfigurationCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1BillingPortalConfigurationCreatedEvent` (`v1.billing_portal.configuration.created`) event notification.
        """
        self._register(
            "v1.billing_portal.configuration.created",
            func,
        )
        return func

    def on_v1_billing_portal_configuration_updated(
        self,
        func: "Callable[[V1BillingPortalConfigurationUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1BillingPortalConfigurationUpdatedEvent` (`v1.billing_portal.configuration.updated`) event notification.
        """
        self._register(
            "v1.billing_portal.configuration.updated",
            func,
        )
        return func

    def on_v1_billing_portal_session_created(
        self,
        func: "Callable[[V1BillingPortalSessionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1BillingPortalSessionCreatedEvent` (`v1.billing_portal.session.created`) event notification.
        """
        self._register(
            "v1.billing_portal.session.created",
            func,
        )
        return func

    def on_v1_capability_updated(
        self,
        func: "Callable[[V1CapabilityUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CapabilityUpdatedEvent` (`v1.capability.updated`) event notification.
        """
        self._register(
            "v1.capability.updated",
            func,
        )
        return func

    def on_v1_cash_balance_funds_available(
        self,
        func: "Callable[[V1CashBalanceFundsAvailableEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CashBalanceFundsAvailableEvent` (`v1.cash_balance.funds_available`) event notification.
        """
        self._register(
            "v1.cash_balance.funds_available",
            func,
        )
        return func

    def on_v1_charge_captured(
        self,
        func: "Callable[[V1ChargeCapturedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeCapturedEvent` (`v1.charge.captured`) event notification.
        """
        self._register(
            "v1.charge.captured",
            func,
        )
        return func

    def on_v1_charge_dispute_closed(
        self,
        func: "Callable[[V1ChargeDisputeClosedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeDisputeClosedEvent` (`v1.charge.dispute.closed`) event notification.
        """
        self._register(
            "v1.charge.dispute.closed",
            func,
        )
        return func

    def on_v1_charge_dispute_created(
        self,
        func: "Callable[[V1ChargeDisputeCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeDisputeCreatedEvent` (`v1.charge.dispute.created`) event notification.
        """
        self._register(
            "v1.charge.dispute.created",
            func,
        )
        return func

    def on_v1_charge_dispute_funds_reinstated(
        self,
        func: "Callable[[V1ChargeDisputeFundsReinstatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeDisputeFundsReinstatedEvent` (`v1.charge.dispute.funds_reinstated`) event notification.
        """
        self._register(
            "v1.charge.dispute.funds_reinstated",
            func,
        )
        return func

    def on_v1_charge_dispute_funds_withdrawn(
        self,
        func: "Callable[[V1ChargeDisputeFundsWithdrawnEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeDisputeFundsWithdrawnEvent` (`v1.charge.dispute.funds_withdrawn`) event notification.
        """
        self._register(
            "v1.charge.dispute.funds_withdrawn",
            func,
        )
        return func

    def on_v1_charge_dispute_updated(
        self,
        func: "Callable[[V1ChargeDisputeUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeDisputeUpdatedEvent` (`v1.charge.dispute.updated`) event notification.
        """
        self._register(
            "v1.charge.dispute.updated",
            func,
        )
        return func

    def on_v1_charge_expired(
        self,
        func: "Callable[[V1ChargeExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeExpiredEvent` (`v1.charge.expired`) event notification.
        """
        self._register(
            "v1.charge.expired",
            func,
        )
        return func

    def on_v1_charge_failed(
        self,
        func: "Callable[[V1ChargeFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeFailedEvent` (`v1.charge.failed`) event notification.
        """
        self._register(
            "v1.charge.failed",
            func,
        )
        return func

    def on_v1_charge_pending(
        self,
        func: "Callable[[V1ChargePendingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargePendingEvent` (`v1.charge.pending`) event notification.
        """
        self._register(
            "v1.charge.pending",
            func,
        )
        return func

    def on_v1_charge_refunded(
        self,
        func: "Callable[[V1ChargeRefundedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeRefundedEvent` (`v1.charge.refunded`) event notification.
        """
        self._register(
            "v1.charge.refunded",
            func,
        )
        return func

    def on_v1_charge_refund_updated(
        self,
        func: "Callable[[V1ChargeRefundUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeRefundUpdatedEvent` (`v1.charge.refund.updated`) event notification.
        """
        self._register(
            "v1.charge.refund.updated",
            func,
        )
        return func

    def on_v1_charge_succeeded(
        self,
        func: "Callable[[V1ChargeSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeSucceededEvent` (`v1.charge.succeeded`) event notification.
        """
        self._register(
            "v1.charge.succeeded",
            func,
        )
        return func

    def on_v1_charge_updated(
        self,
        func: "Callable[[V1ChargeUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ChargeUpdatedEvent` (`v1.charge.updated`) event notification.
        """
        self._register(
            "v1.charge.updated",
            func,
        )
        return func

    def on_v1_checkout_session_async_payment_failed(
        self,
        func: "Callable[[V1CheckoutSessionAsyncPaymentFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CheckoutSessionAsyncPaymentFailedEvent` (`v1.checkout.session.async_payment_failed`) event notification.
        """
        self._register(
            "v1.checkout.session.async_payment_failed",
            func,
        )
        return func

    def on_v1_checkout_session_async_payment_succeeded(
        self,
        func: "Callable[[V1CheckoutSessionAsyncPaymentSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CheckoutSessionAsyncPaymentSucceededEvent` (`v1.checkout.session.async_payment_succeeded`) event notification.
        """
        self._register(
            "v1.checkout.session.async_payment_succeeded",
            func,
        )
        return func

    def on_v1_checkout_session_completed(
        self,
        func: "Callable[[V1CheckoutSessionCompletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CheckoutSessionCompletedEvent` (`v1.checkout.session.completed`) event notification.
        """
        self._register(
            "v1.checkout.session.completed",
            func,
        )
        return func

    def on_v1_checkout_session_expired(
        self,
        func: "Callable[[V1CheckoutSessionExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CheckoutSessionExpiredEvent` (`v1.checkout.session.expired`) event notification.
        """
        self._register(
            "v1.checkout.session.expired",
            func,
        )
        return func

    def on_v1_climate_order_canceled(
        self,
        func: "Callable[[V1ClimateOrderCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateOrderCanceledEvent` (`v1.climate.order.canceled`) event notification.
        """
        self._register(
            "v1.climate.order.canceled",
            func,
        )
        return func

    def on_v1_climate_order_created(
        self,
        func: "Callable[[V1ClimateOrderCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateOrderCreatedEvent` (`v1.climate.order.created`) event notification.
        """
        self._register(
            "v1.climate.order.created",
            func,
        )
        return func

    def on_v1_climate_order_delayed(
        self,
        func: "Callable[[V1ClimateOrderDelayedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateOrderDelayedEvent` (`v1.climate.order.delayed`) event notification.
        """
        self._register(
            "v1.climate.order.delayed",
            func,
        )
        return func

    def on_v1_climate_order_delivered(
        self,
        func: "Callable[[V1ClimateOrderDeliveredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateOrderDeliveredEvent` (`v1.climate.order.delivered`) event notification.
        """
        self._register(
            "v1.climate.order.delivered",
            func,
        )
        return func

    def on_v1_climate_order_product_substituted(
        self,
        func: "Callable[[V1ClimateOrderProductSubstitutedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateOrderProductSubstitutedEvent` (`v1.climate.order.product_substituted`) event notification.
        """
        self._register(
            "v1.climate.order.product_substituted",
            func,
        )
        return func

    def on_v1_climate_product_created(
        self,
        func: "Callable[[V1ClimateProductCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateProductCreatedEvent` (`v1.climate.product.created`) event notification.
        """
        self._register(
            "v1.climate.product.created",
            func,
        )
        return func

    def on_v1_climate_product_pricing_updated(
        self,
        func: "Callable[[V1ClimateProductPricingUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ClimateProductPricingUpdatedEvent` (`v1.climate.product.pricing_updated`) event notification.
        """
        self._register(
            "v1.climate.product.pricing_updated",
            func,
        )
        return func

    def on_v1_coupon_created(
        self,
        func: "Callable[[V1CouponCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CouponCreatedEvent` (`v1.coupon.created`) event notification.
        """
        self._register(
            "v1.coupon.created",
            func,
        )
        return func

    def on_v1_coupon_deleted(
        self,
        func: "Callable[[V1CouponDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CouponDeletedEvent` (`v1.coupon.deleted`) event notification.
        """
        self._register(
            "v1.coupon.deleted",
            func,
        )
        return func

    def on_v1_coupon_updated(
        self,
        func: "Callable[[V1CouponUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CouponUpdatedEvent` (`v1.coupon.updated`) event notification.
        """
        self._register(
            "v1.coupon.updated",
            func,
        )
        return func

    def on_v1_credit_note_created(
        self,
        func: "Callable[[V1CreditNoteCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CreditNoteCreatedEvent` (`v1.credit_note.created`) event notification.
        """
        self._register(
            "v1.credit_note.created",
            func,
        )
        return func

    def on_v1_credit_note_updated(
        self,
        func: "Callable[[V1CreditNoteUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CreditNoteUpdatedEvent` (`v1.credit_note.updated`) event notification.
        """
        self._register(
            "v1.credit_note.updated",
            func,
        )
        return func

    def on_v1_credit_note_voided(
        self,
        func: "Callable[[V1CreditNoteVoidedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CreditNoteVoidedEvent` (`v1.credit_note.voided`) event notification.
        """
        self._register(
            "v1.credit_note.voided",
            func,
        )
        return func

    def on_v1_customer_cash_balance_transaction_created(
        self,
        func: "Callable[[V1CustomerCashBalanceTransactionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerCashBalanceTransactionCreatedEvent` (`v1.customer_cash_balance_transaction.created`) event notification.
        """
        self._register(
            "v1.customer_cash_balance_transaction.created",
            func,
        )
        return func

    def on_v1_customer_created(
        self,
        func: "Callable[[V1CustomerCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerCreatedEvent` (`v1.customer.created`) event notification.
        """
        self._register(
            "v1.customer.created",
            func,
        )
        return func

    def on_v1_customer_deleted(
        self,
        func: "Callable[[V1CustomerDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerDeletedEvent` (`v1.customer.deleted`) event notification.
        """
        self._register(
            "v1.customer.deleted",
            func,
        )
        return func

    def on_v1_customer_subscription_created(
        self,
        func: "Callable[[V1CustomerSubscriptionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionCreatedEvent` (`v1.customer.subscription.created`) event notification.
        """
        self._register(
            "v1.customer.subscription.created",
            func,
        )
        return func

    def on_v1_customer_subscription_deleted(
        self,
        func: "Callable[[V1CustomerSubscriptionDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionDeletedEvent` (`v1.customer.subscription.deleted`) event notification.
        """
        self._register(
            "v1.customer.subscription.deleted",
            func,
        )
        return func

    def on_v1_customer_subscription_paused(
        self,
        func: "Callable[[V1CustomerSubscriptionPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionPausedEvent` (`v1.customer.subscription.paused`) event notification.
        """
        self._register(
            "v1.customer.subscription.paused",
            func,
        )
        return func

    def on_v1_customer_subscription_pending_update_applied(
        self,
        func: "Callable[[V1CustomerSubscriptionPendingUpdateAppliedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionPendingUpdateAppliedEvent` (`v1.customer.subscription.pending_update_applied`) event notification.
        """
        self._register(
            "v1.customer.subscription.pending_update_applied",
            func,
        )
        return func

    def on_v1_customer_subscription_pending_update_expired(
        self,
        func: "Callable[[V1CustomerSubscriptionPendingUpdateExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionPendingUpdateExpiredEvent` (`v1.customer.subscription.pending_update_expired`) event notification.
        """
        self._register(
            "v1.customer.subscription.pending_update_expired",
            func,
        )
        return func

    def on_v1_customer_subscription_resumed(
        self,
        func: "Callable[[V1CustomerSubscriptionResumedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionResumedEvent` (`v1.customer.subscription.resumed`) event notification.
        """
        self._register(
            "v1.customer.subscription.resumed",
            func,
        )
        return func

    def on_v1_customer_subscription_trial_will_end(
        self,
        func: "Callable[[V1CustomerSubscriptionTrialWillEndEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionTrialWillEndEvent` (`v1.customer.subscription.trial_will_end`) event notification.
        """
        self._register(
            "v1.customer.subscription.trial_will_end",
            func,
        )
        return func

    def on_v1_customer_subscription_updated(
        self,
        func: "Callable[[V1CustomerSubscriptionUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerSubscriptionUpdatedEvent` (`v1.customer.subscription.updated`) event notification.
        """
        self._register(
            "v1.customer.subscription.updated",
            func,
        )
        return func

    def on_v1_customer_tax_id_created(
        self,
        func: "Callable[[V1CustomerTaxIdCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerTaxIdCreatedEvent` (`v1.customer.tax_id.created`) event notification.
        """
        self._register(
            "v1.customer.tax_id.created",
            func,
        )
        return func

    def on_v1_customer_tax_id_deleted(
        self,
        func: "Callable[[V1CustomerTaxIdDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerTaxIdDeletedEvent` (`v1.customer.tax_id.deleted`) event notification.
        """
        self._register(
            "v1.customer.tax_id.deleted",
            func,
        )
        return func

    def on_v1_customer_tax_id_updated(
        self,
        func: "Callable[[V1CustomerTaxIdUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerTaxIdUpdatedEvent` (`v1.customer.tax_id.updated`) event notification.
        """
        self._register(
            "v1.customer.tax_id.updated",
            func,
        )
        return func

    def on_v1_customer_updated(
        self,
        func: "Callable[[V1CustomerUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1CustomerUpdatedEvent` (`v1.customer.updated`) event notification.
        """
        self._register(
            "v1.customer.updated",
            func,
        )
        return func

    def on_v1_entitlements_active_entitlement_summary_updated(
        self,
        func: "Callable[[V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1EntitlementsActiveEntitlementSummaryUpdatedEvent` (`v1.entitlements.active_entitlement_summary.updated`) event notification.
        """
        self._register(
            "v1.entitlements.active_entitlement_summary.updated",
            func,
        )
        return func

    def on_v1_file_created(
        self,
        func: "Callable[[V1FileCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FileCreatedEvent` (`v1.file.created`) event notification.
        """
        self._register(
            "v1.file.created",
            func,
        )
        return func

    def on_v1_financial_connections_account_created(
        self,
        func: "Callable[[V1FinancialConnectionsAccountCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountCreatedEvent` (`v1.financial_connections.account.created`) event notification.
        """
        self._register(
            "v1.financial_connections.account.created",
            func,
        )
        return func

    def on_v1_financial_connections_account_deactivated(
        self,
        func: "Callable[[V1FinancialConnectionsAccountDeactivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountDeactivatedEvent` (`v1.financial_connections.account.deactivated`) event notification.
        """
        self._register(
            "v1.financial_connections.account.deactivated",
            func,
        )
        return func

    def on_v1_financial_connections_account_disconnected(
        self,
        func: "Callable[[V1FinancialConnectionsAccountDisconnectedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountDisconnectedEvent` (`v1.financial_connections.account.disconnected`) event notification.
        """
        self._register(
            "v1.financial_connections.account.disconnected",
            func,
        )
        return func

    def on_v1_financial_connections_account_reactivated(
        self,
        func: "Callable[[V1FinancialConnectionsAccountReactivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountReactivatedEvent` (`v1.financial_connections.account.reactivated`) event notification.
        """
        self._register(
            "v1.financial_connections.account.reactivated",
            func,
        )
        return func

    def on_v1_financial_connections_account_refreshed_balance(
        self,
        func: "Callable[[V1FinancialConnectionsAccountRefreshedBalanceEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountRefreshedBalanceEvent` (`v1.financial_connections.account.refreshed_balance`) event notification.
        """
        self._register(
            "v1.financial_connections.account.refreshed_balance",
            func,
        )
        return func

    def on_v1_financial_connections_account_refreshed_ownership(
        self,
        func: "Callable[[V1FinancialConnectionsAccountRefreshedOwnershipEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountRefreshedOwnershipEvent` (`v1.financial_connections.account.refreshed_ownership`) event notification.
        """
        self._register(
            "v1.financial_connections.account.refreshed_ownership",
            func,
        )
        return func

    def on_v1_financial_connections_account_refreshed_transactions(
        self,
        func: "Callable[[V1FinancialConnectionsAccountRefreshedTransactionsEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1FinancialConnectionsAccountRefreshedTransactionsEvent` (`v1.financial_connections.account.refreshed_transactions`) event notification.
        """
        self._register(
            "v1.financial_connections.account.refreshed_transactions",
            func,
        )
        return func

    def on_v1_identity_verification_session_canceled(
        self,
        func: "Callable[[V1IdentityVerificationSessionCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionCanceledEvent` (`v1.identity.verification_session.canceled`) event notification.
        """
        self._register(
            "v1.identity.verification_session.canceled",
            func,
        )
        return func

    def on_v1_identity_verification_session_created(
        self,
        func: "Callable[[V1IdentityVerificationSessionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionCreatedEvent` (`v1.identity.verification_session.created`) event notification.
        """
        self._register(
            "v1.identity.verification_session.created",
            func,
        )
        return func

    def on_v1_identity_verification_session_processing(
        self,
        func: "Callable[[V1IdentityVerificationSessionProcessingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionProcessingEvent` (`v1.identity.verification_session.processing`) event notification.
        """
        self._register(
            "v1.identity.verification_session.processing",
            func,
        )
        return func

    def on_v1_identity_verification_session_redacted(
        self,
        func: "Callable[[V1IdentityVerificationSessionRedactedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionRedactedEvent` (`v1.identity.verification_session.redacted`) event notification.
        """
        self._register(
            "v1.identity.verification_session.redacted",
            func,
        )
        return func

    def on_v1_identity_verification_session_requires_input(
        self,
        func: "Callable[[V1IdentityVerificationSessionRequiresInputEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionRequiresInputEvent` (`v1.identity.verification_session.requires_input`) event notification.
        """
        self._register(
            "v1.identity.verification_session.requires_input",
            func,
        )
        return func

    def on_v1_identity_verification_session_verified(
        self,
        func: "Callable[[V1IdentityVerificationSessionVerifiedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IdentityVerificationSessionVerifiedEvent` (`v1.identity.verification_session.verified`) event notification.
        """
        self._register(
            "v1.identity.verification_session.verified",
            func,
        )
        return func

    def on_v1_invoice_created(
        self,
        func: "Callable[[V1InvoiceCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceCreatedEvent` (`v1.invoice.created`) event notification.
        """
        self._register(
            "v1.invoice.created",
            func,
        )
        return func

    def on_v1_invoice_deleted(
        self,
        func: "Callable[[V1InvoiceDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceDeletedEvent` (`v1.invoice.deleted`) event notification.
        """
        self._register(
            "v1.invoice.deleted",
            func,
        )
        return func

    def on_v1_invoice_finalization_failed(
        self,
        func: "Callable[[V1InvoiceFinalizationFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceFinalizationFailedEvent` (`v1.invoice.finalization_failed`) event notification.
        """
        self._register(
            "v1.invoice.finalization_failed",
            func,
        )
        return func

    def on_v1_invoice_finalized(
        self,
        func: "Callable[[V1InvoiceFinalizedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceFinalizedEvent` (`v1.invoice.finalized`) event notification.
        """
        self._register(
            "v1.invoice.finalized",
            func,
        )
        return func

    def on_v1_invoiceitem_created(
        self,
        func: "Callable[[V1InvoiceitemCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceitemCreatedEvent` (`v1.invoiceitem.created`) event notification.
        """
        self._register(
            "v1.invoiceitem.created",
            func,
        )
        return func

    def on_v1_invoiceitem_deleted(
        self,
        func: "Callable[[V1InvoiceitemDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceitemDeletedEvent` (`v1.invoiceitem.deleted`) event notification.
        """
        self._register(
            "v1.invoiceitem.deleted",
            func,
        )
        return func

    def on_v1_invoice_marked_uncollectible(
        self,
        func: "Callable[[V1InvoiceMarkedUncollectibleEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceMarkedUncollectibleEvent` (`v1.invoice.marked_uncollectible`) event notification.
        """
        self._register(
            "v1.invoice.marked_uncollectible",
            func,
        )
        return func

    def on_v1_invoice_overdue(
        self,
        func: "Callable[[V1InvoiceOverdueEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceOverdueEvent` (`v1.invoice.overdue`) event notification.
        """
        self._register(
            "v1.invoice.overdue",
            func,
        )
        return func

    def on_v1_invoice_overpaid(
        self,
        func: "Callable[[V1InvoiceOverpaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceOverpaidEvent` (`v1.invoice.overpaid`) event notification.
        """
        self._register(
            "v1.invoice.overpaid",
            func,
        )
        return func

    def on_v1_invoice_paid(
        self,
        func: "Callable[[V1InvoicePaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoicePaidEvent` (`v1.invoice.paid`) event notification.
        """
        self._register(
            "v1.invoice.paid",
            func,
        )
        return func

    def on_v1_invoice_payment_action_required(
        self,
        func: "Callable[[V1InvoicePaymentActionRequiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoicePaymentActionRequiredEvent` (`v1.invoice.payment_action_required`) event notification.
        """
        self._register(
            "v1.invoice.payment_action_required",
            func,
        )
        return func

    def on_v1_invoice_payment_failed(
        self,
        func: "Callable[[V1InvoicePaymentFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoicePaymentFailedEvent` (`v1.invoice.payment_failed`) event notification.
        """
        self._register(
            "v1.invoice.payment_failed",
            func,
        )
        return func

    def on_v1_invoice_payment_paid(
        self,
        func: "Callable[[V1InvoicePaymentPaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoicePaymentPaidEvent` (`v1.invoice_payment.paid`) event notification.
        """
        self._register(
            "v1.invoice_payment.paid",
            func,
        )
        return func

    def on_v1_invoice_payment_succeeded(
        self,
        func: "Callable[[V1InvoicePaymentSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoicePaymentSucceededEvent` (`v1.invoice.payment_succeeded`) event notification.
        """
        self._register(
            "v1.invoice.payment_succeeded",
            func,
        )
        return func

    def on_v1_invoice_sent(
        self,
        func: "Callable[[V1InvoiceSentEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceSentEvent` (`v1.invoice.sent`) event notification.
        """
        self._register(
            "v1.invoice.sent",
            func,
        )
        return func

    def on_v1_invoice_upcoming(
        self,
        func: "Callable[[V1InvoiceUpcomingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceUpcomingEvent` (`v1.invoice.upcoming`) event notification.
        """
        self._register(
            "v1.invoice.upcoming",
            func,
        )
        return func

    def on_v1_invoice_updated(
        self,
        func: "Callable[[V1InvoiceUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceUpdatedEvent` (`v1.invoice.updated`) event notification.
        """
        self._register(
            "v1.invoice.updated",
            func,
        )
        return func

    def on_v1_invoice_voided(
        self,
        func: "Callable[[V1InvoiceVoidedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceVoidedEvent` (`v1.invoice.voided`) event notification.
        """
        self._register(
            "v1.invoice.voided",
            func,
        )
        return func

    def on_v1_invoice_will_be_due(
        self,
        func: "Callable[[V1InvoiceWillBeDueEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1InvoiceWillBeDueEvent` (`v1.invoice.will_be_due`) event notification.
        """
        self._register(
            "v1.invoice.will_be_due",
            func,
        )
        return func

    def on_v1_issuing_authorization_created(
        self,
        func: "Callable[[V1IssuingAuthorizationCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingAuthorizationCreatedEvent` (`v1.issuing_authorization.created`) event notification.
        """
        self._register(
            "v1.issuing_authorization.created",
            func,
        )
        return func

    def on_v1_issuing_authorization_request(
        self,
        func: "Callable[[V1IssuingAuthorizationRequestEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingAuthorizationRequestEvent` (`v1.issuing_authorization.request`) event notification.
        """
        self._register(
            "v1.issuing_authorization.request",
            func,
        )
        return func

    def on_v1_issuing_authorization_updated(
        self,
        func: "Callable[[V1IssuingAuthorizationUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingAuthorizationUpdatedEvent` (`v1.issuing_authorization.updated`) event notification.
        """
        self._register(
            "v1.issuing_authorization.updated",
            func,
        )
        return func

    def on_v1_issuing_card_created(
        self,
        func: "Callable[[V1IssuingCardCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingCardCreatedEvent` (`v1.issuing_card.created`) event notification.
        """
        self._register(
            "v1.issuing_card.created",
            func,
        )
        return func

    def on_v1_issuing_cardholder_created(
        self,
        func: "Callable[[V1IssuingCardholderCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingCardholderCreatedEvent` (`v1.issuing_cardholder.created`) event notification.
        """
        self._register(
            "v1.issuing_cardholder.created",
            func,
        )
        return func

    def on_v1_issuing_cardholder_updated(
        self,
        func: "Callable[[V1IssuingCardholderUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingCardholderUpdatedEvent` (`v1.issuing_cardholder.updated`) event notification.
        """
        self._register(
            "v1.issuing_cardholder.updated",
            func,
        )
        return func

    def on_v1_issuing_card_updated(
        self,
        func: "Callable[[V1IssuingCardUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingCardUpdatedEvent` (`v1.issuing_card.updated`) event notification.
        """
        self._register(
            "v1.issuing_card.updated",
            func,
        )
        return func

    def on_v1_issuing_dispute_closed(
        self,
        func: "Callable[[V1IssuingDisputeClosedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeClosedEvent` (`v1.issuing_dispute.closed`) event notification.
        """
        self._register(
            "v1.issuing_dispute.closed",
            func,
        )
        return func

    def on_v1_issuing_dispute_created(
        self,
        func: "Callable[[V1IssuingDisputeCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeCreatedEvent` (`v1.issuing_dispute.created`) event notification.
        """
        self._register(
            "v1.issuing_dispute.created",
            func,
        )
        return func

    def on_v1_issuing_dispute_funds_reinstated(
        self,
        func: "Callable[[V1IssuingDisputeFundsReinstatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeFundsReinstatedEvent` (`v1.issuing_dispute.funds_reinstated`) event notification.
        """
        self._register(
            "v1.issuing_dispute.funds_reinstated",
            func,
        )
        return func

    def on_v1_issuing_dispute_funds_rescinded(
        self,
        func: "Callable[[V1IssuingDisputeFundsRescindedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeFundsRescindedEvent` (`v1.issuing_dispute.funds_rescinded`) event notification.
        """
        self._register(
            "v1.issuing_dispute.funds_rescinded",
            func,
        )
        return func

    def on_v1_issuing_dispute_submitted(
        self,
        func: "Callable[[V1IssuingDisputeSubmittedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeSubmittedEvent` (`v1.issuing_dispute.submitted`) event notification.
        """
        self._register(
            "v1.issuing_dispute.submitted",
            func,
        )
        return func

    def on_v1_issuing_dispute_updated(
        self,
        func: "Callable[[V1IssuingDisputeUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingDisputeUpdatedEvent` (`v1.issuing_dispute.updated`) event notification.
        """
        self._register(
            "v1.issuing_dispute.updated",
            func,
        )
        return func

    def on_v1_issuing_personalization_design_activated(
        self,
        func: "Callable[[V1IssuingPersonalizationDesignActivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingPersonalizationDesignActivatedEvent` (`v1.issuing_personalization_design.activated`) event notification.
        """
        self._register(
            "v1.issuing_personalization_design.activated",
            func,
        )
        return func

    def on_v1_issuing_personalization_design_deactivated(
        self,
        func: "Callable[[V1IssuingPersonalizationDesignDeactivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingPersonalizationDesignDeactivatedEvent` (`v1.issuing_personalization_design.deactivated`) event notification.
        """
        self._register(
            "v1.issuing_personalization_design.deactivated",
            func,
        )
        return func

    def on_v1_issuing_personalization_design_rejected(
        self,
        func: "Callable[[V1IssuingPersonalizationDesignRejectedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingPersonalizationDesignRejectedEvent` (`v1.issuing_personalization_design.rejected`) event notification.
        """
        self._register(
            "v1.issuing_personalization_design.rejected",
            func,
        )
        return func

    def on_v1_issuing_personalization_design_updated(
        self,
        func: "Callable[[V1IssuingPersonalizationDesignUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingPersonalizationDesignUpdatedEvent` (`v1.issuing_personalization_design.updated`) event notification.
        """
        self._register(
            "v1.issuing_personalization_design.updated",
            func,
        )
        return func

    def on_v1_issuing_token_created(
        self,
        func: "Callable[[V1IssuingTokenCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingTokenCreatedEvent` (`v1.issuing_token.created`) event notification.
        """
        self._register(
            "v1.issuing_token.created",
            func,
        )
        return func

    def on_v1_issuing_token_updated(
        self,
        func: "Callable[[V1IssuingTokenUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingTokenUpdatedEvent` (`v1.issuing_token.updated`) event notification.
        """
        self._register(
            "v1.issuing_token.updated",
            func,
        )
        return func

    def on_v1_issuing_transaction_created(
        self,
        func: "Callable[[V1IssuingTransactionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingTransactionCreatedEvent` (`v1.issuing_transaction.created`) event notification.
        """
        self._register(
            "v1.issuing_transaction.created",
            func,
        )
        return func

    def on_v1_issuing_transaction_purchase_details_receipt_updated(
        self,
        func: "Callable[[V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent` (`v1.issuing_transaction.purchase_details_receipt_updated`) event notification.
        """
        self._register(
            "v1.issuing_transaction.purchase_details_receipt_updated",
            func,
        )
        return func

    def on_v1_issuing_transaction_updated(
        self,
        func: "Callable[[V1IssuingTransactionUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1IssuingTransactionUpdatedEvent` (`v1.issuing_transaction.updated`) event notification.
        """
        self._register(
            "v1.issuing_transaction.updated",
            func,
        )
        return func

    def on_v1_mandate_updated(
        self,
        func: "Callable[[V1MandateUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1MandateUpdatedEvent` (`v1.mandate.updated`) event notification.
        """
        self._register(
            "v1.mandate.updated",
            func,
        )
        return func

    def on_v1_payment_intent_amount_capturable_updated(
        self,
        func: "Callable[[V1PaymentIntentAmountCapturableUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentAmountCapturableUpdatedEvent` (`v1.payment_intent.amount_capturable_updated`) event notification.
        """
        self._register(
            "v1.payment_intent.amount_capturable_updated",
            func,
        )
        return func

    def on_v1_payment_intent_canceled(
        self,
        func: "Callable[[V1PaymentIntentCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentCanceledEvent` (`v1.payment_intent.canceled`) event notification.
        """
        self._register(
            "v1.payment_intent.canceled",
            func,
        )
        return func

    def on_v1_payment_intent_created(
        self,
        func: "Callable[[V1PaymentIntentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentCreatedEvent` (`v1.payment_intent.created`) event notification.
        """
        self._register(
            "v1.payment_intent.created",
            func,
        )
        return func

    def on_v1_payment_intent_partially_funded(
        self,
        func: "Callable[[V1PaymentIntentPartiallyFundedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentPartiallyFundedEvent` (`v1.payment_intent.partially_funded`) event notification.
        """
        self._register(
            "v1.payment_intent.partially_funded",
            func,
        )
        return func

    def on_v1_payment_intent_payment_failed(
        self,
        func: "Callable[[V1PaymentIntentPaymentFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentPaymentFailedEvent` (`v1.payment_intent.payment_failed`) event notification.
        """
        self._register(
            "v1.payment_intent.payment_failed",
            func,
        )
        return func

    def on_v1_payment_intent_processing(
        self,
        func: "Callable[[V1PaymentIntentProcessingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentProcessingEvent` (`v1.payment_intent.processing`) event notification.
        """
        self._register(
            "v1.payment_intent.processing",
            func,
        )
        return func

    def on_v1_payment_intent_requires_action(
        self,
        func: "Callable[[V1PaymentIntentRequiresActionEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentRequiresActionEvent` (`v1.payment_intent.requires_action`) event notification.
        """
        self._register(
            "v1.payment_intent.requires_action",
            func,
        )
        return func

    def on_v1_payment_intent_succeeded(
        self,
        func: "Callable[[V1PaymentIntentSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentIntentSucceededEvent` (`v1.payment_intent.succeeded`) event notification.
        """
        self._register(
            "v1.payment_intent.succeeded",
            func,
        )
        return func

    def on_v1_payment_link_created(
        self,
        func: "Callable[[V1PaymentLinkCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentLinkCreatedEvent` (`v1.payment_link.created`) event notification.
        """
        self._register(
            "v1.payment_link.created",
            func,
        )
        return func

    def on_v1_payment_link_updated(
        self,
        func: "Callable[[V1PaymentLinkUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentLinkUpdatedEvent` (`v1.payment_link.updated`) event notification.
        """
        self._register(
            "v1.payment_link.updated",
            func,
        )
        return func

    def on_v1_payment_method_attached(
        self,
        func: "Callable[[V1PaymentMethodAttachedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentMethodAttachedEvent` (`v1.payment_method.attached`) event notification.
        """
        self._register(
            "v1.payment_method.attached",
            func,
        )
        return func

    def on_v1_payment_method_automatically_updated(
        self,
        func: "Callable[[V1PaymentMethodAutomaticallyUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentMethodAutomaticallyUpdatedEvent` (`v1.payment_method.automatically_updated`) event notification.
        """
        self._register(
            "v1.payment_method.automatically_updated",
            func,
        )
        return func

    def on_v1_payment_method_detached(
        self,
        func: "Callable[[V1PaymentMethodDetachedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentMethodDetachedEvent` (`v1.payment_method.detached`) event notification.
        """
        self._register(
            "v1.payment_method.detached",
            func,
        )
        return func

    def on_v1_payment_method_updated(
        self,
        func: "Callable[[V1PaymentMethodUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PaymentMethodUpdatedEvent` (`v1.payment_method.updated`) event notification.
        """
        self._register(
            "v1.payment_method.updated",
            func,
        )
        return func

    def on_v1_payout_canceled(
        self,
        func: "Callable[[V1PayoutCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutCanceledEvent` (`v1.payout.canceled`) event notification.
        """
        self._register(
            "v1.payout.canceled",
            func,
        )
        return func

    def on_v1_payout_created(
        self,
        func: "Callable[[V1PayoutCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutCreatedEvent` (`v1.payout.created`) event notification.
        """
        self._register(
            "v1.payout.created",
            func,
        )
        return func

    def on_v1_payout_failed(
        self,
        func: "Callable[[V1PayoutFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutFailedEvent` (`v1.payout.failed`) event notification.
        """
        self._register(
            "v1.payout.failed",
            func,
        )
        return func

    def on_v1_payout_paid(
        self,
        func: "Callable[[V1PayoutPaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutPaidEvent` (`v1.payout.paid`) event notification.
        """
        self._register(
            "v1.payout.paid",
            func,
        )
        return func

    def on_v1_payout_reconciliation_completed(
        self,
        func: "Callable[[V1PayoutReconciliationCompletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutReconciliationCompletedEvent` (`v1.payout.reconciliation_completed`) event notification.
        """
        self._register(
            "v1.payout.reconciliation_completed",
            func,
        )
        return func

    def on_v1_payout_updated(
        self,
        func: "Callable[[V1PayoutUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PayoutUpdatedEvent` (`v1.payout.updated`) event notification.
        """
        self._register(
            "v1.payout.updated",
            func,
        )
        return func

    def on_v1_person_created(
        self,
        func: "Callable[[V1PersonCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PersonCreatedEvent` (`v1.person.created`) event notification.
        """
        self._register(
            "v1.person.created",
            func,
        )
        return func

    def on_v1_person_deleted(
        self,
        func: "Callable[[V1PersonDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PersonDeletedEvent` (`v1.person.deleted`) event notification.
        """
        self._register(
            "v1.person.deleted",
            func,
        )
        return func

    def on_v1_person_updated(
        self,
        func: "Callable[[V1PersonUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PersonUpdatedEvent` (`v1.person.updated`) event notification.
        """
        self._register(
            "v1.person.updated",
            func,
        )
        return func

    def on_v1_plan_created(
        self,
        func: "Callable[[V1PlanCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PlanCreatedEvent` (`v1.plan.created`) event notification.
        """
        self._register(
            "v1.plan.created",
            func,
        )
        return func

    def on_v1_plan_deleted(
        self,
        func: "Callable[[V1PlanDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PlanDeletedEvent` (`v1.plan.deleted`) event notification.
        """
        self._register(
            "v1.plan.deleted",
            func,
        )
        return func

    def on_v1_plan_updated(
        self,
        func: "Callable[[V1PlanUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PlanUpdatedEvent` (`v1.plan.updated`) event notification.
        """
        self._register(
            "v1.plan.updated",
            func,
        )
        return func

    def on_v1_price_created(
        self,
        func: "Callable[[V1PriceCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PriceCreatedEvent` (`v1.price.created`) event notification.
        """
        self._register(
            "v1.price.created",
            func,
        )
        return func

    def on_v1_price_deleted(
        self,
        func: "Callable[[V1PriceDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PriceDeletedEvent` (`v1.price.deleted`) event notification.
        """
        self._register(
            "v1.price.deleted",
            func,
        )
        return func

    def on_v1_price_updated(
        self,
        func: "Callable[[V1PriceUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PriceUpdatedEvent` (`v1.price.updated`) event notification.
        """
        self._register(
            "v1.price.updated",
            func,
        )
        return func

    def on_v1_product_created(
        self,
        func: "Callable[[V1ProductCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ProductCreatedEvent` (`v1.product.created`) event notification.
        """
        self._register(
            "v1.product.created",
            func,
        )
        return func

    def on_v1_product_deleted(
        self,
        func: "Callable[[V1ProductDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ProductDeletedEvent` (`v1.product.deleted`) event notification.
        """
        self._register(
            "v1.product.deleted",
            func,
        )
        return func

    def on_v1_product_updated(
        self,
        func: "Callable[[V1ProductUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ProductUpdatedEvent` (`v1.product.updated`) event notification.
        """
        self._register(
            "v1.product.updated",
            func,
        )
        return func

    def on_v1_promotion_code_created(
        self,
        func: "Callable[[V1PromotionCodeCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PromotionCodeCreatedEvent` (`v1.promotion_code.created`) event notification.
        """
        self._register(
            "v1.promotion_code.created",
            func,
        )
        return func

    def on_v1_promotion_code_updated(
        self,
        func: "Callable[[V1PromotionCodeUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1PromotionCodeUpdatedEvent` (`v1.promotion_code.updated`) event notification.
        """
        self._register(
            "v1.promotion_code.updated",
            func,
        )
        return func

    def on_v1_quote_accepted(
        self,
        func: "Callable[[V1QuoteAcceptedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1QuoteAcceptedEvent` (`v1.quote.accepted`) event notification.
        """
        self._register(
            "v1.quote.accepted",
            func,
        )
        return func

    def on_v1_quote_canceled(
        self,
        func: "Callable[[V1QuoteCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1QuoteCanceledEvent` (`v1.quote.canceled`) event notification.
        """
        self._register(
            "v1.quote.canceled",
            func,
        )
        return func

    def on_v1_quote_created(
        self,
        func: "Callable[[V1QuoteCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1QuoteCreatedEvent` (`v1.quote.created`) event notification.
        """
        self._register(
            "v1.quote.created",
            func,
        )
        return func

    def on_v1_quote_finalized(
        self,
        func: "Callable[[V1QuoteFinalizedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1QuoteFinalizedEvent` (`v1.quote.finalized`) event notification.
        """
        self._register(
            "v1.quote.finalized",
            func,
        )
        return func

    def on_v1_radar_early_fraud_warning_created(
        self,
        func: "Callable[[V1RadarEarlyFraudWarningCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1RadarEarlyFraudWarningCreatedEvent` (`v1.radar.early_fraud_warning.created`) event notification.
        """
        self._register(
            "v1.radar.early_fraud_warning.created",
            func,
        )
        return func

    def on_v1_radar_early_fraud_warning_updated(
        self,
        func: "Callable[[V1RadarEarlyFraudWarningUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1RadarEarlyFraudWarningUpdatedEvent` (`v1.radar.early_fraud_warning.updated`) event notification.
        """
        self._register(
            "v1.radar.early_fraud_warning.updated",
            func,
        )
        return func

    def on_v1_refund_created(
        self,
        func: "Callable[[V1RefundCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1RefundCreatedEvent` (`v1.refund.created`) event notification.
        """
        self._register(
            "v1.refund.created",
            func,
        )
        return func

    def on_v1_refund_failed(
        self,
        func: "Callable[[V1RefundFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1RefundFailedEvent` (`v1.refund.failed`) event notification.
        """
        self._register(
            "v1.refund.failed",
            func,
        )
        return func

    def on_v1_refund_updated(
        self,
        func: "Callable[[V1RefundUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1RefundUpdatedEvent` (`v1.refund.updated`) event notification.
        """
        self._register(
            "v1.refund.updated",
            func,
        )
        return func

    def on_v1_review_closed(
        self,
        func: "Callable[[V1ReviewClosedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ReviewClosedEvent` (`v1.review.closed`) event notification.
        """
        self._register(
            "v1.review.closed",
            func,
        )
        return func

    def on_v1_review_opened(
        self,
        func: "Callable[[V1ReviewOpenedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1ReviewOpenedEvent` (`v1.review.opened`) event notification.
        """
        self._register(
            "v1.review.opened",
            func,
        )
        return func

    def on_v1_setup_intent_canceled(
        self,
        func: "Callable[[V1SetupIntentCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SetupIntentCanceledEvent` (`v1.setup_intent.canceled`) event notification.
        """
        self._register(
            "v1.setup_intent.canceled",
            func,
        )
        return func

    def on_v1_setup_intent_created(
        self,
        func: "Callable[[V1SetupIntentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SetupIntentCreatedEvent` (`v1.setup_intent.created`) event notification.
        """
        self._register(
            "v1.setup_intent.created",
            func,
        )
        return func

    def on_v1_setup_intent_requires_action(
        self,
        func: "Callable[[V1SetupIntentRequiresActionEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SetupIntentRequiresActionEvent` (`v1.setup_intent.requires_action`) event notification.
        """
        self._register(
            "v1.setup_intent.requires_action",
            func,
        )
        return func

    def on_v1_setup_intent_setup_failed(
        self,
        func: "Callable[[V1SetupIntentSetupFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SetupIntentSetupFailedEvent` (`v1.setup_intent.setup_failed`) event notification.
        """
        self._register(
            "v1.setup_intent.setup_failed",
            func,
        )
        return func

    def on_v1_setup_intent_succeeded(
        self,
        func: "Callable[[V1SetupIntentSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SetupIntentSucceededEvent` (`v1.setup_intent.succeeded`) event notification.
        """
        self._register(
            "v1.setup_intent.succeeded",
            func,
        )
        return func

    def on_v1_sigma_scheduled_query_run_created(
        self,
        func: "Callable[[V1SigmaScheduledQueryRunCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SigmaScheduledQueryRunCreatedEvent` (`v1.sigma.scheduled_query_run.created`) event notification.
        """
        self._register(
            "v1.sigma.scheduled_query_run.created",
            func,
        )
        return func

    def on_v1_source_canceled(
        self,
        func: "Callable[[V1SourceCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SourceCanceledEvent` (`v1.source.canceled`) event notification.
        """
        self._register(
            "v1.source.canceled",
            func,
        )
        return func

    def on_v1_source_chargeable(
        self,
        func: "Callable[[V1SourceChargeableEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SourceChargeableEvent` (`v1.source.chargeable`) event notification.
        """
        self._register(
            "v1.source.chargeable",
            func,
        )
        return func

    def on_v1_source_failed(
        self,
        func: "Callable[[V1SourceFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SourceFailedEvent` (`v1.source.failed`) event notification.
        """
        self._register(
            "v1.source.failed",
            func,
        )
        return func

    def on_v1_source_refund_attributes_required(
        self,
        func: "Callable[[V1SourceRefundAttributesRequiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SourceRefundAttributesRequiredEvent` (`v1.source.refund_attributes_required`) event notification.
        """
        self._register(
            "v1.source.refund_attributes_required",
            func,
        )
        return func

    def on_v1_subscription_schedule_aborted(
        self,
        func: "Callable[[V1SubscriptionScheduleAbortedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleAbortedEvent` (`v1.subscription_schedule.aborted`) event notification.
        """
        self._register(
            "v1.subscription_schedule.aborted",
            func,
        )
        return func

    def on_v1_subscription_schedule_canceled(
        self,
        func: "Callable[[V1SubscriptionScheduleCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleCanceledEvent` (`v1.subscription_schedule.canceled`) event notification.
        """
        self._register(
            "v1.subscription_schedule.canceled",
            func,
        )
        return func

    def on_v1_subscription_schedule_completed(
        self,
        func: "Callable[[V1SubscriptionScheduleCompletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleCompletedEvent` (`v1.subscription_schedule.completed`) event notification.
        """
        self._register(
            "v1.subscription_schedule.completed",
            func,
        )
        return func

    def on_v1_subscription_schedule_created(
        self,
        func: "Callable[[V1SubscriptionScheduleCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleCreatedEvent` (`v1.subscription_schedule.created`) event notification.
        """
        self._register(
            "v1.subscription_schedule.created",
            func,
        )
        return func

    def on_v1_subscription_schedule_expiring(
        self,
        func: "Callable[[V1SubscriptionScheduleExpiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleExpiringEvent` (`v1.subscription_schedule.expiring`) event notification.
        """
        self._register(
            "v1.subscription_schedule.expiring",
            func,
        )
        return func

    def on_v1_subscription_schedule_released(
        self,
        func: "Callable[[V1SubscriptionScheduleReleasedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleReleasedEvent` (`v1.subscription_schedule.released`) event notification.
        """
        self._register(
            "v1.subscription_schedule.released",
            func,
        )
        return func

    def on_v1_subscription_schedule_updated(
        self,
        func: "Callable[[V1SubscriptionScheduleUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1SubscriptionScheduleUpdatedEvent` (`v1.subscription_schedule.updated`) event notification.
        """
        self._register(
            "v1.subscription_schedule.updated",
            func,
        )
        return func

    def on_v1_tax_rate_created(
        self,
        func: "Callable[[V1TaxRateCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TaxRateCreatedEvent` (`v1.tax_rate.created`) event notification.
        """
        self._register(
            "v1.tax_rate.created",
            func,
        )
        return func

    def on_v1_tax_rate_updated(
        self,
        func: "Callable[[V1TaxRateUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TaxRateUpdatedEvent` (`v1.tax_rate.updated`) event notification.
        """
        self._register(
            "v1.tax_rate.updated",
            func,
        )
        return func

    def on_v1_tax_settings_updated(
        self,
        func: "Callable[[V1TaxSettingsUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TaxSettingsUpdatedEvent` (`v1.tax.settings.updated`) event notification.
        """
        self._register(
            "v1.tax.settings.updated",
            func,
        )
        return func

    def on_v1_terminal_reader_action_failed(
        self,
        func: "Callable[[V1TerminalReaderActionFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TerminalReaderActionFailedEvent` (`v1.terminal.reader.action_failed`) event notification.
        """
        self._register(
            "v1.terminal.reader.action_failed",
            func,
        )
        return func

    def on_v1_terminal_reader_action_succeeded(
        self,
        func: "Callable[[V1TerminalReaderActionSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TerminalReaderActionSucceededEvent` (`v1.terminal.reader.action_succeeded`) event notification.
        """
        self._register(
            "v1.terminal.reader.action_succeeded",
            func,
        )
        return func

    def on_v1_terminal_reader_action_updated(
        self,
        func: "Callable[[V1TerminalReaderActionUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TerminalReaderActionUpdatedEvent` (`v1.terminal.reader.action_updated`) event notification.
        """
        self._register(
            "v1.terminal.reader.action_updated",
            func,
        )
        return func

    def on_v1_test_helpers_test_clock_advancing(
        self,
        func: "Callable[[V1TestHelpersTestClockAdvancingEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TestHelpersTestClockAdvancingEvent` (`v1.test_helpers.test_clock.advancing`) event notification.
        """
        self._register(
            "v1.test_helpers.test_clock.advancing",
            func,
        )
        return func

    def on_v1_test_helpers_test_clock_created(
        self,
        func: "Callable[[V1TestHelpersTestClockCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TestHelpersTestClockCreatedEvent` (`v1.test_helpers.test_clock.created`) event notification.
        """
        self._register(
            "v1.test_helpers.test_clock.created",
            func,
        )
        return func

    def on_v1_test_helpers_test_clock_deleted(
        self,
        func: "Callable[[V1TestHelpersTestClockDeletedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TestHelpersTestClockDeletedEvent` (`v1.test_helpers.test_clock.deleted`) event notification.
        """
        self._register(
            "v1.test_helpers.test_clock.deleted",
            func,
        )
        return func

    def on_v1_test_helpers_test_clock_internal_failure(
        self,
        func: "Callable[[V1TestHelpersTestClockInternalFailureEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TestHelpersTestClockInternalFailureEvent` (`v1.test_helpers.test_clock.internal_failure`) event notification.
        """
        self._register(
            "v1.test_helpers.test_clock.internal_failure",
            func,
        )
        return func

    def on_v1_test_helpers_test_clock_ready(
        self,
        func: "Callable[[V1TestHelpersTestClockReadyEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TestHelpersTestClockReadyEvent` (`v1.test_helpers.test_clock.ready`) event notification.
        """
        self._register(
            "v1.test_helpers.test_clock.ready",
            func,
        )
        return func

    def on_v1_topup_canceled(
        self,
        func: "Callable[[V1TopupCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TopupCanceledEvent` (`v1.topup.canceled`) event notification.
        """
        self._register(
            "v1.topup.canceled",
            func,
        )
        return func

    def on_v1_topup_created(
        self,
        func: "Callable[[V1TopupCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TopupCreatedEvent` (`v1.topup.created`) event notification.
        """
        self._register(
            "v1.topup.created",
            func,
        )
        return func

    def on_v1_topup_failed(
        self,
        func: "Callable[[V1TopupFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TopupFailedEvent` (`v1.topup.failed`) event notification.
        """
        self._register(
            "v1.topup.failed",
            func,
        )
        return func

    def on_v1_topup_reversed(
        self,
        func: "Callable[[V1TopupReversedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TopupReversedEvent` (`v1.topup.reversed`) event notification.
        """
        self._register(
            "v1.topup.reversed",
            func,
        )
        return func

    def on_v1_topup_succeeded(
        self,
        func: "Callable[[V1TopupSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TopupSucceededEvent` (`v1.topup.succeeded`) event notification.
        """
        self._register(
            "v1.topup.succeeded",
            func,
        )
        return func

    def on_v1_transfer_created(
        self,
        func: "Callable[[V1TransferCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TransferCreatedEvent` (`v1.transfer.created`) event notification.
        """
        self._register(
            "v1.transfer.created",
            func,
        )
        return func

    def on_v1_transfer_reversed(
        self,
        func: "Callable[[V1TransferReversedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TransferReversedEvent` (`v1.transfer.reversed`) event notification.
        """
        self._register(
            "v1.transfer.reversed",
            func,
        )
        return func

    def on_v1_transfer_updated(
        self,
        func: "Callable[[V1TransferUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V1TransferUpdatedEvent` (`v1.transfer.updated`) event notification.
        """
        self._register(
            "v1.transfer.updated",
            func,
        )
        return func

    def on_v2_billing_cadence_billed(
        self,
        func: "Callable[[V2BillingCadenceBilledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingCadenceBilledEvent` (`v2.billing.cadence.billed`) event notification.
        """
        self._register(
            "v2.billing.cadence.billed",
            func,
        )
        return func

    def on_v2_billing_cadence_canceled(
        self,
        func: "Callable[[V2BillingCadenceCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingCadenceCanceledEvent` (`v2.billing.cadence.canceled`) event notification.
        """
        self._register(
            "v2.billing.cadence.canceled",
            func,
        )
        return func

    def on_v2_billing_cadence_created(
        self,
        func: "Callable[[V2BillingCadenceCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingCadenceCreatedEvent` (`v2.billing.cadence.created`) event notification.
        """
        self._register(
            "v2.billing.cadence.created",
            func,
        )
        return func

    def on_v2_billing_licensed_item_created(
        self,
        func: "Callable[[V2BillingLicensedItemCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingLicensedItemCreatedEvent` (`v2.billing.licensed_item.created`) event notification.
        """
        self._register(
            "v2.billing.licensed_item.created",
            func,
        )
        return func

    def on_v2_billing_licensed_item_updated(
        self,
        func: "Callable[[V2BillingLicensedItemUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingLicensedItemUpdatedEvent` (`v2.billing.licensed_item.updated`) event notification.
        """
        self._register(
            "v2.billing.licensed_item.updated",
            func,
        )
        return func

    def on_v2_billing_license_fee_created(
        self,
        func: "Callable[[V2BillingLicenseFeeCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingLicenseFeeCreatedEvent` (`v2.billing.license_fee.created`) event notification.
        """
        self._register(
            "v2.billing.license_fee.created",
            func,
        )
        return func

    def on_v2_billing_license_fee_updated(
        self,
        func: "Callable[[V2BillingLicenseFeeUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingLicenseFeeUpdatedEvent` (`v2.billing.license_fee.updated`) event notification.
        """
        self._register(
            "v2.billing.license_fee.updated",
            func,
        )
        return func

    def on_v2_billing_license_fee_version_created(
        self,
        func: "Callable[[V2BillingLicenseFeeVersionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingLicenseFeeVersionCreatedEvent` (`v2.billing.license_fee_version.created`) event notification.
        """
        self._register(
            "v2.billing.license_fee_version.created",
            func,
        )
        return func

    def on_v2_billing_metered_item_created(
        self,
        func: "Callable[[V2BillingMeteredItemCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingMeteredItemCreatedEvent` (`v2.billing.metered_item.created`) event notification.
        """
        self._register(
            "v2.billing.metered_item.created",
            func,
        )
        return func

    def on_v2_billing_metered_item_updated(
        self,
        func: "Callable[[V2BillingMeteredItemUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingMeteredItemUpdatedEvent` (`v2.billing.metered_item.updated`) event notification.
        """
        self._register(
            "v2.billing.metered_item.updated",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_component_created(
        self,
        func: "Callable[[V2BillingPricingPlanComponentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanComponentCreatedEvent` (`v2.billing.pricing_plan_component.created`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_component.created",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_component_updated(
        self,
        func: "Callable[[V2BillingPricingPlanComponentUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanComponentUpdatedEvent` (`v2.billing.pricing_plan_component.updated`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_component.updated",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_created(
        self,
        func: "Callable[[V2BillingPricingPlanCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanCreatedEvent` (`v2.billing.pricing_plan.created`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan.created",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_collection_awaiting_customer_action(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent` (`v2.billing.pricing_plan_subscription.collection_awaiting_customer_action`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.collection_awaiting_customer_action",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_collection_current(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionCollectionCurrentEvent` (`v2.billing.pricing_plan_subscription.collection_current`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.collection_current",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_collection_past_due(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionCollectionPastDueEvent` (`v2.billing.pricing_plan_subscription.collection_past_due`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.collection_past_due",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_collection_paused(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionCollectionPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionCollectionPausedEvent` (`v2.billing.pricing_plan_subscription.collection_paused`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.collection_paused",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_collection_unpaid(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionCollectionUnpaidEvent` (`v2.billing.pricing_plan_subscription.collection_unpaid`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.collection_unpaid",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_servicing_activated(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionServicingActivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionServicingActivatedEvent` (`v2.billing.pricing_plan_subscription.servicing_activated`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.servicing_activated",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_servicing_canceled(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionServicingCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionServicingCanceledEvent` (`v2.billing.pricing_plan_subscription.servicing_canceled`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.servicing_canceled",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_subscription_servicing_paused(
        self,
        func: "Callable[[V2BillingPricingPlanSubscriptionServicingPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanSubscriptionServicingPausedEvent` (`v2.billing.pricing_plan_subscription.servicing_paused`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_subscription.servicing_paused",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_updated(
        self,
        func: "Callable[[V2BillingPricingPlanUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanUpdatedEvent` (`v2.billing.pricing_plan.updated`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan.updated",
            func,
        )
        return func

    def on_v2_billing_pricing_plan_version_created(
        self,
        func: "Callable[[V2BillingPricingPlanVersionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingPricingPlanVersionCreatedEvent` (`v2.billing.pricing_plan_version.created`) event notification.
        """
        self._register(
            "v2.billing.pricing_plan_version.created",
            func,
        )
        return func

    def on_v2_billing_rate_card_created(
        self,
        func: "Callable[[V2BillingRateCardCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardCreatedEvent` (`v2.billing.rate_card.created`) event notification.
        """
        self._register(
            "v2.billing.rate_card.created",
            func,
        )
        return func

    def on_v2_billing_rate_card_custom_pricing_unit_overage_rate_created(
        self,
        func: "Callable[[V2BillingRateCardCustomPricingUnitOverageRateCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardCustomPricingUnitOverageRateCreatedEvent` (`v2.billing.rate_card_custom_pricing_unit_overage_rate.created`) event notification.
        """
        self._register(
            "v2.billing.rate_card_custom_pricing_unit_overage_rate.created",
            func,
        )
        return func

    def on_v2_billing_rate_card_rate_created(
        self,
        func: "Callable[[V2BillingRateCardRateCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardRateCreatedEvent` (`v2.billing.rate_card_rate.created`) event notification.
        """
        self._register(
            "v2.billing.rate_card_rate.created",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_activated(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionActivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionActivatedEvent` (`v2.billing.rate_card_subscription.activated`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.activated",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_canceled(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCanceledEvent` (`v2.billing.rate_card_subscription.canceled`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.canceled",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_collection_awaiting_customer_action(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent` (`v2.billing.rate_card_subscription.collection_awaiting_customer_action`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.collection_awaiting_customer_action",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_collection_current(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCollectionCurrentEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCollectionCurrentEvent` (`v2.billing.rate_card_subscription.collection_current`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.collection_current",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_collection_past_due(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCollectionPastDueEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCollectionPastDueEvent` (`v2.billing.rate_card_subscription.collection_past_due`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.collection_past_due",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_collection_paused(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCollectionPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCollectionPausedEvent` (`v2.billing.rate_card_subscription.collection_paused`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.collection_paused",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_collection_unpaid(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionCollectionUnpaidEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionCollectionUnpaidEvent` (`v2.billing.rate_card_subscription.collection_unpaid`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.collection_unpaid",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_servicing_activated(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionServicingActivatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionServicingActivatedEvent` (`v2.billing.rate_card_subscription.servicing_activated`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.servicing_activated",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_servicing_canceled(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionServicingCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionServicingCanceledEvent` (`v2.billing.rate_card_subscription.servicing_canceled`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.servicing_canceled",
            func,
        )
        return func

    def on_v2_billing_rate_card_subscription_servicing_paused(
        self,
        func: "Callable[[V2BillingRateCardSubscriptionServicingPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardSubscriptionServicingPausedEvent` (`v2.billing.rate_card_subscription.servicing_paused`) event notification.
        """
        self._register(
            "v2.billing.rate_card_subscription.servicing_paused",
            func,
        )
        return func

    def on_v2_billing_rate_card_updated(
        self,
        func: "Callable[[V2BillingRateCardUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardUpdatedEvent` (`v2.billing.rate_card.updated`) event notification.
        """
        self._register(
            "v2.billing.rate_card.updated",
            func,
        )
        return func

    def on_v2_billing_rate_card_version_created(
        self,
        func: "Callable[[V2BillingRateCardVersionCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2BillingRateCardVersionCreatedEvent` (`v2.billing.rate_card_version.created`) event notification.
        """
        self._register(
            "v2.billing.rate_card_version.created",
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

    def on_v2_core_account_including_configuration_card_creator_capability_status_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent` (`v2.core.account[configuration.card_creator].capability_status_updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.card_creator].capability_status_updated",
            func,
        )
        return func

    def on_v2_core_account_including_configuration_card_creator_updated(
        self,
        func: "Callable[[V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent` (`v2.core.account[configuration.card_creator].updated`) event notification.
        """
        self._register(
            "v2.core.account[configuration.card_creator].updated",
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

    def on_v2_core_account_signals_fraudulent_website_ready(
        self,
        func: "Callable[[V2CoreAccountSignalsFraudulentWebsiteReadyEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreAccountSignalsFraudulentWebsiteReadyEvent` (`v2.core.account_signals.fraudulent_website_ready`) event notification.
        """
        self._register(
            "v2.core.account_signals.fraudulent_website_ready",
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

    def on_v2_core_approval_request_approved(
        self,
        func: "Callable[[V2CoreApprovalRequestApprovedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestApprovedEvent` (`v2.core.approval_request.approved`) event notification.
        """
        self._register(
            "v2.core.approval_request.approved",
            func,
        )
        return func

    def on_v2_core_approval_request_canceled(
        self,
        func: "Callable[[V2CoreApprovalRequestCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestCanceledEvent` (`v2.core.approval_request.canceled`) event notification.
        """
        self._register(
            "v2.core.approval_request.canceled",
            func,
        )
        return func

    def on_v2_core_approval_request_created(
        self,
        func: "Callable[[V2CoreApprovalRequestCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestCreatedEvent` (`v2.core.approval_request.created`) event notification.
        """
        self._register(
            "v2.core.approval_request.created",
            func,
        )
        return func

    def on_v2_core_approval_request_expired(
        self,
        func: "Callable[[V2CoreApprovalRequestExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestExpiredEvent` (`v2.core.approval_request.expired`) event notification.
        """
        self._register(
            "v2.core.approval_request.expired",
            func,
        )
        return func

    def on_v2_core_approval_request_failed(
        self,
        func: "Callable[[V2CoreApprovalRequestFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestFailedEvent` (`v2.core.approval_request.failed`) event notification.
        """
        self._register(
            "v2.core.approval_request.failed",
            func,
        )
        return func

    def on_v2_core_approval_request_rejected(
        self,
        func: "Callable[[V2CoreApprovalRequestRejectedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestRejectedEvent` (`v2.core.approval_request.rejected`) event notification.
        """
        self._register(
            "v2.core.approval_request.rejected",
            func,
        )
        return func

    def on_v2_core_approval_request_succeeded(
        self,
        func: "Callable[[V2CoreApprovalRequestSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreApprovalRequestSucceededEvent` (`v2.core.approval_request.succeeded`) event notification.
        """
        self._register(
            "v2.core.approval_request.succeeded",
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

    def on_v2_core_claimable_sandbox_claimed(
        self,
        func: "Callable[[V2CoreClaimableSandboxClaimedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreClaimableSandboxClaimedEvent` (`v2.core.claimable_sandbox.claimed`) event notification.
        """
        self._register(
            "v2.core.claimable_sandbox.claimed",
            func,
        )
        return func

    def on_v2_core_claimable_sandbox_created(
        self,
        func: "Callable[[V2CoreClaimableSandboxCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreClaimableSandboxCreatedEvent` (`v2.core.claimable_sandbox.created`) event notification.
        """
        self._register(
            "v2.core.claimable_sandbox.created",
            func,
        )
        return func

    def on_v2_core_claimable_sandbox_expired(
        self,
        func: "Callable[[V2CoreClaimableSandboxExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreClaimableSandboxExpiredEvent` (`v2.core.claimable_sandbox.expired`) event notification.
        """
        self._register(
            "v2.core.claimable_sandbox.expired",
            func,
        )
        return func

    def on_v2_core_claimable_sandbox_expiring(
        self,
        func: "Callable[[V2CoreClaimableSandboxExpiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreClaimableSandboxExpiringEvent` (`v2.core.claimable_sandbox.expiring`) event notification.
        """
        self._register(
            "v2.core.claimable_sandbox.expiring",
            func,
        )
        return func

    def on_v2_core_claimable_sandbox_updated(
        self,
        func: "Callable[[V2CoreClaimableSandboxUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreClaimableSandboxUpdatedEvent` (`v2.core.claimable_sandbox.updated`) event notification.
        """
        self._register(
            "v2.core.claimable_sandbox.updated",
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

    def on_v2_core_health_api_error_firing(
        self,
        func: "Callable[[V2CoreHealthApiErrorFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthApiErrorFiringEvent` (`v2.core.health.api_error.firing`) event notification.
        """
        self._register(
            "v2.core.health.api_error.firing",
            func,
        )
        return func

    def on_v2_core_health_api_error_resolved(
        self,
        func: "Callable[[V2CoreHealthApiErrorResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthApiErrorResolvedEvent` (`v2.core.health.api_error.resolved`) event notification.
        """
        self._register(
            "v2.core.health.api_error.resolved",
            func,
        )
        return func

    def on_v2_core_health_api_latency_firing(
        self,
        func: "Callable[[V2CoreHealthApiLatencyFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthApiLatencyFiringEvent` (`v2.core.health.api_latency.firing`) event notification.
        """
        self._register(
            "v2.core.health.api_latency.firing",
            func,
        )
        return func

    def on_v2_core_health_api_latency_resolved(
        self,
        func: "Callable[[V2CoreHealthApiLatencyResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthApiLatencyResolvedEvent` (`v2.core.health.api_latency.resolved`) event notification.
        """
        self._register(
            "v2.core.health.api_latency.resolved",
            func,
        )
        return func

    def on_v2_core_health_authorization_rate_drop_firing(
        self,
        func: "Callable[[V2CoreHealthAuthorizationRateDropFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthAuthorizationRateDropFiringEvent` (`v2.core.health.authorization_rate_drop.firing`) event notification.
        """
        self._register(
            "v2.core.health.authorization_rate_drop.firing",
            func,
        )
        return func

    def on_v2_core_health_authorization_rate_drop_resolved(
        self,
        func: "Callable[[V2CoreHealthAuthorizationRateDropResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthAuthorizationRateDropResolvedEvent` (`v2.core.health.authorization_rate_drop.resolved`) event notification.
        """
        self._register(
            "v2.core.health.authorization_rate_drop.resolved",
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

    def on_v2_core_health_fraud_rate_increased(
        self,
        func: "Callable[[V2CoreHealthFraudRateIncreasedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthFraudRateIncreasedEvent` (`v2.core.health.fraud_rate.increased`) event notification.
        """
        self._register(
            "v2.core.health.fraud_rate.increased",
            func,
        )
        return func

    def on_v2_core_health_issuing_authorization_request_errors_firing(
        self,
        func: "Callable[[V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent` (`v2.core.health.issuing_authorization_request_errors.firing`) event notification.
        """
        self._register(
            "v2.core.health.issuing_authorization_request_errors.firing",
            func,
        )
        return func

    def on_v2_core_health_issuing_authorization_request_errors_resolved(
        self,
        func: "Callable[[V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent` (`v2.core.health.issuing_authorization_request_errors.resolved`) event notification.
        """
        self._register(
            "v2.core.health.issuing_authorization_request_errors.resolved",
            func,
        )
        return func

    def on_v2_core_health_issuing_authorization_request_timeout_firing(
        self,
        func: "Callable[[V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent` (`v2.core.health.issuing_authorization_request_timeout.firing`) event notification.
        """
        self._register(
            "v2.core.health.issuing_authorization_request_timeout.firing",
            func,
        )
        return func

    def on_v2_core_health_issuing_authorization_request_timeout_resolved(
        self,
        func: "Callable[[V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent` (`v2.core.health.issuing_authorization_request_timeout.resolved`) event notification.
        """
        self._register(
            "v2.core.health.issuing_authorization_request_timeout.resolved",
            func,
        )
        return func

    def on_v2_core_health_meter_event_summaries_delayed_firing(
        self,
        func: "Callable[[V2CoreHealthMeterEventSummariesDelayedFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthMeterEventSummariesDelayedFiringEvent` (`v2.core.health.meter_event_summaries_delayed.firing`) event notification.
        """
        self._register(
            "v2.core.health.meter_event_summaries_delayed.firing",
            func,
        )
        return func

    def on_v2_core_health_meter_event_summaries_delayed_resolved(
        self,
        func: "Callable[[V2CoreHealthMeterEventSummariesDelayedResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthMeterEventSummariesDelayedResolvedEvent` (`v2.core.health.meter_event_summaries_delayed.resolved`) event notification.
        """
        self._register(
            "v2.core.health.meter_event_summaries_delayed.resolved",
            func,
        )
        return func

    def on_v2_core_health_payment_method_error_firing(
        self,
        func: "Callable[[V2CoreHealthPaymentMethodErrorFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthPaymentMethodErrorFiringEvent` (`v2.core.health.payment_method_error.firing`) event notification.
        """
        self._register(
            "v2.core.health.payment_method_error.firing",
            func,
        )
        return func

    def on_v2_core_health_payment_method_error_resolved(
        self,
        func: "Callable[[V2CoreHealthPaymentMethodErrorResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthPaymentMethodErrorResolvedEvent` (`v2.core.health.payment_method_error.resolved`) event notification.
        """
        self._register(
            "v2.core.health.payment_method_error.resolved",
            func,
        )
        return func

    def on_v2_core_health_sepa_debit_delayed_firing(
        self,
        func: "Callable[[V2CoreHealthSepaDebitDelayedFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthSepaDebitDelayedFiringEvent` (`v2.core.health.sepa_debit_delayed.firing`) event notification.
        """
        self._register(
            "v2.core.health.sepa_debit_delayed.firing",
            func,
        )
        return func

    def on_v2_core_health_sepa_debit_delayed_resolved(
        self,
        func: "Callable[[V2CoreHealthSepaDebitDelayedResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthSepaDebitDelayedResolvedEvent` (`v2.core.health.sepa_debit_delayed.resolved`) event notification.
        """
        self._register(
            "v2.core.health.sepa_debit_delayed.resolved",
            func,
        )
        return func

    def on_v2_core_health_traffic_volume_drop_firing(
        self,
        func: "Callable[[V2CoreHealthTrafficVolumeDropFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthTrafficVolumeDropFiringEvent` (`v2.core.health.traffic_volume_drop.firing`) event notification.
        """
        self._register(
            "v2.core.health.traffic_volume_drop.firing",
            func,
        )
        return func

    def on_v2_core_health_traffic_volume_drop_resolved(
        self,
        func: "Callable[[V2CoreHealthTrafficVolumeDropResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthTrafficVolumeDropResolvedEvent` (`v2.core.health.traffic_volume_drop.resolved`) event notification.
        """
        self._register(
            "v2.core.health.traffic_volume_drop.resolved",
            func,
        )
        return func

    def on_v2_core_health_webhook_latency_firing(
        self,
        func: "Callable[[V2CoreHealthWebhookLatencyFiringEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthWebhookLatencyFiringEvent` (`v2.core.health.webhook_latency.firing`) event notification.
        """
        self._register(
            "v2.core.health.webhook_latency.firing",
            func,
        )
        return func

    def on_v2_core_health_webhook_latency_resolved(
        self,
        func: "Callable[[V2CoreHealthWebhookLatencyResolvedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2CoreHealthWebhookLatencyResolvedEvent` (`v2.core.health.webhook_latency.resolved`) event notification.
        """
        self._register(
            "v2.core.health.webhook_latency.resolved",
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

    def on_v2_extend_extension_run_failed(
        self,
        func: "Callable[[V2ExtendExtensionRunFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ExtendExtensionRunFailedEvent` (`v2.extend.extension_run.failed`) event notification.
        """
        self._register(
            "v2.extend.extension_run.failed",
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

    def on_v2_iam_api_key_created(
        self,
        func: "Callable[[V2IamApiKeyCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyCreatedEvent` (`v2.iam.api_key.created`) event notification.
        """
        self._register(
            "v2.iam.api_key.created",
            func,
        )
        return func

    def on_v2_iam_api_key_default_secret_revealed(
        self,
        func: "Callable[[V2IamApiKeyDefaultSecretRevealedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyDefaultSecretRevealedEvent` (`v2.iam.api_key.default_secret_revealed`) event notification.
        """
        self._register(
            "v2.iam.api_key.default_secret_revealed",
            func,
        )
        return func

    def on_v2_iam_api_key_expired(
        self,
        func: "Callable[[V2IamApiKeyExpiredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyExpiredEvent` (`v2.iam.api_key.expired`) event notification.
        """
        self._register(
            "v2.iam.api_key.expired",
            func,
        )
        return func

    def on_v2_iam_api_key_permissions_updated(
        self,
        func: "Callable[[V2IamApiKeyPermissionsUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyPermissionsUpdatedEvent` (`v2.iam.api_key.permissions_updated`) event notification.
        """
        self._register(
            "v2.iam.api_key.permissions_updated",
            func,
        )
        return func

    def on_v2_iam_api_key_rotated(
        self,
        func: "Callable[[V2IamApiKeyRotatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyRotatedEvent` (`v2.iam.api_key.rotated`) event notification.
        """
        self._register(
            "v2.iam.api_key.rotated",
            func,
        )
        return func

    def on_v2_iam_api_key_updated(
        self,
        func: "Callable[[V2IamApiKeyUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamApiKeyUpdatedEvent` (`v2.iam.api_key.updated`) event notification.
        """
        self._register(
            "v2.iam.api_key.updated",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_approved(
        self,
        func: "Callable[[V2IamStripeAccessGrantApprovedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantApprovedEvent` (`v2.iam.stripe_access_grant.approved`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.approved",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_canceled(
        self,
        func: "Callable[[V2IamStripeAccessGrantCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantCanceledEvent` (`v2.iam.stripe_access_grant.canceled`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.canceled",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_denied(
        self,
        func: "Callable[[V2IamStripeAccessGrantDeniedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantDeniedEvent` (`v2.iam.stripe_access_grant.denied`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.denied",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_removed(
        self,
        func: "Callable[[V2IamStripeAccessGrantRemovedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantRemovedEvent` (`v2.iam.stripe_access_grant.removed`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.removed",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_requested(
        self,
        func: "Callable[[V2IamStripeAccessGrantRequestedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantRequestedEvent` (`v2.iam.stripe_access_grant.requested`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.requested",
            func,
        )
        return func

    def on_v2_iam_stripe_access_grant_updated(
        self,
        func: "Callable[[V2IamStripeAccessGrantUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2IamStripeAccessGrantUpdatedEvent` (`v2.iam.stripe_access_grant.updated`) event notification.
        """
        self._register(
            "v2.iam.stripe_access_grant.updated",
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

    def on_v2_money_management_recipient_verification_created(
        self,
        func: "Callable[[V2MoneyManagementRecipientVerificationCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementRecipientVerificationCreatedEvent` (`v2.money_management.recipient_verification.created`) event notification.
        """
        self._register(
            "v2.money_management.recipient_verification.created",
            func,
        )
        return func

    def on_v2_money_management_recipient_verification_updated(
        self,
        func: "Callable[[V2MoneyManagementRecipientVerificationUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2MoneyManagementRecipientVerificationUpdatedEvent` (`v2.money_management.recipient_verification.updated`) event notification.
        """
        self._register(
            "v2.money_management.recipient_verification.updated",
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

    def on_v2_payments_off_session_payment_attempt_failed(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAttemptFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentAttemptFailedEvent` (`v2.payments.off_session_payment.attempt_failed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.attempt_failed",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_attempt_started(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAttemptStartedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentAttemptStartedEvent` (`v2.payments.off_session_payment.attempt_started`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.attempt_started",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_authorization_attempt_failed(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent` (`v2.payments.off_session_payment.authorization_attempt_failed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.authorization_attempt_failed",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_authorization_attempt_started(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent` (`v2.payments.off_session_payment.authorization_attempt_started`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.authorization_attempt_started",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_canceled(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentCanceledEvent` (`v2.payments.off_session_payment.canceled`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.canceled",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_created(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentCreatedEvent` (`v2.payments.off_session_payment.created`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.created",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_failed(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentFailedEvent` (`v2.payments.off_session_payment.failed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.failed",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_paused(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentPausedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentPausedEvent` (`v2.payments.off_session_payment.paused`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.paused",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_requires_capture(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentRequiresCaptureEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentRequiresCaptureEvent` (`v2.payments.off_session_payment.requires_capture`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.requires_capture",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_resumed(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentResumedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentResumedEvent` (`v2.payments.off_session_payment.resumed`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.resumed",
            func,
        )
        return func

    def on_v2_payments_off_session_payment_succeeded(
        self,
        func: "Callable[[V2PaymentsOffSessionPaymentSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsOffSessionPaymentSucceededEvent` (`v2.payments.off_session_payment.succeeded`) event notification.
        """
        self._register(
            "v2.payments.off_session_payment.succeeded",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_canceled(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentCanceledEvent` (`v2.payments.settlement_allocation_intent.canceled`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.canceled",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_created(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentCreatedEvent` (`v2.payments.settlement_allocation_intent.created`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.created",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_errored(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentErroredEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentErroredEvent` (`v2.payments.settlement_allocation_intent.errored`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.errored",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_funds_not_received(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentFundsNotReceivedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent` (`v2.payments.settlement_allocation_intent.funds_not_received`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.funds_not_received",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_matched(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentMatchedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentMatchedEvent` (`v2.payments.settlement_allocation_intent.matched`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.matched",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_not_found(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentNotFoundEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentNotFoundEvent` (`v2.payments.settlement_allocation_intent.not_found`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.not_found",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_settled(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentSettledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentSettledEvent` (`v2.payments.settlement_allocation_intent.settled`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.settled",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_split_canceled(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentSplitCanceledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentSplitCanceledEvent` (`v2.payments.settlement_allocation_intent_split.canceled`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent_split.canceled",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_split_created(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentSplitCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentSplitCreatedEvent` (`v2.payments.settlement_allocation_intent_split.created`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent_split.created",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_split_settled(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentSplitSettledEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentSplitSettledEvent` (`v2.payments.settlement_allocation_intent_split.settled`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent_split.settled",
            func,
        )
        return func

    def on_v2_payments_settlement_allocation_intent_submitted(
        self,
        func: "Callable[[V2PaymentsSettlementAllocationIntentSubmittedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2PaymentsSettlementAllocationIntentSubmittedEvent` (`v2.payments.settlement_allocation_intent.submitted`) event notification.
        """
        self._register(
            "v2.payments.settlement_allocation_intent.submitted",
            func,
        )
        return func

    def on_v2_reporting_report_run_created(
        self,
        func: "Callable[[V2ReportingReportRunCreatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ReportingReportRunCreatedEvent` (`v2.reporting.report_run.created`) event notification.
        """
        self._register(
            "v2.reporting.report_run.created",
            func,
        )
        return func

    def on_v2_reporting_report_run_failed(
        self,
        func: "Callable[[V2ReportingReportRunFailedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ReportingReportRunFailedEvent` (`v2.reporting.report_run.failed`) event notification.
        """
        self._register(
            "v2.reporting.report_run.failed",
            func,
        )
        return func

    def on_v2_reporting_report_run_succeeded(
        self,
        func: "Callable[[V2ReportingReportRunSucceededEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ReportingReportRunSucceededEvent` (`v2.reporting.report_run.succeeded`) event notification.
        """
        self._register(
            "v2.reporting.report_run.succeeded",
            func,
        )
        return func

    def on_v2_reporting_report_run_updated(
        self,
        func: "Callable[[V2ReportingReportRunUpdatedEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2ReportingReportRunUpdatedEvent` (`v2.reporting.report_run.updated`) event notification.
        """
        self._register(
            "v2.reporting.report_run.updated",
            func,
        )
        return func

    def on_v2_signals_account_signal_fraudulent_merchant_ready(
        self,
        func: "Callable[[V2SignalsAccountSignalFraudulentMerchantReadyEventNotification, StripeClient], None]",
    ):
        """
        Registers a callback for the `V2SignalsAccountSignalFraudulentMerchantReadyEvent` (`v2.signals.account_signal.fraudulent_merchant_ready`) event notification.
        """
        self._register(
            "v2.signals.account_signal.fraudulent_merchant_ready",
            func,
        )
        return func

    # event-notification-registration-methods: The end of the section generated from our OpenAPI spec
