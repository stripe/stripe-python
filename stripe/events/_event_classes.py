# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
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
    from stripe.events._v1_balance_settings_updated_event import (
        V1BalanceSettingsUpdatedEventNotification,
    )
    from stripe.events._v1_billing_alert_triggered_event import (
        V1BillingAlertTriggeredEventNotification,
    )
    from stripe.events._v1_billing_credit_balance_transaction_created_event import (
        V1BillingCreditBalanceTransactionCreatedEventNotification,
    )
    from stripe.events._v1_billing_credit_grant_created_event import (
        V1BillingCreditGrantCreatedEventNotification,
    )
    from stripe.events._v1_billing_credit_grant_updated_event import (
        V1BillingCreditGrantUpdatedEventNotification,
    )
    from stripe.events._v1_billing_meter_created_event import (
        V1BillingMeterCreatedEventNotification,
    )
    from stripe.events._v1_billing_meter_deactivated_event import (
        V1BillingMeterDeactivatedEventNotification,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v1_billing_meter_reactivated_event import (
        V1BillingMeterReactivatedEventNotification,
    )
    from stripe.events._v1_billing_meter_updated_event import (
        V1BillingMeterUpdatedEventNotification,
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
    from stripe.events._v1_customer_discount_created_event import (
        V1CustomerDiscountCreatedEventNotification,
    )
    from stripe.events._v1_customer_discount_deleted_event import (
        V1CustomerDiscountDeletedEventNotification,
    )
    from stripe.events._v1_customer_discount_updated_event import (
        V1CustomerDiscountUpdatedEventNotification,
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
    from stripe.events._v1_financial_connections_account_account_numbers_updated_event import (
        V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification,
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
    from stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event import (
        V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification,
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
    from stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event import (
        V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event import (
        V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification,
    )
    from stripe.events._v1_financial_connections_account_upcoming_deactivation_event import (
        V1FinancialConnectionsAccountUpcomingDeactivationEventNotification,
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
    from stripe.events._v1_invoice_payment_attempt_required_event import (
        V1InvoicePaymentAttemptRequiredEventNotification,
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


_V2_EVENT_CLASS_LOOKUP = {
    "v1.account.application.authorized": (
        "stripe.events._v1_account_application_authorized_event",
        "V1AccountApplicationAuthorizedEvent",
    ),
    "v1.account.application.deauthorized": (
        "stripe.events._v1_account_application_deauthorized_event",
        "V1AccountApplicationDeauthorizedEvent",
    ),
    "v1.account.external_account.created": (
        "stripe.events._v1_account_external_account_created_event",
        "V1AccountExternalAccountCreatedEvent",
    ),
    "v1.account.external_account.deleted": (
        "stripe.events._v1_account_external_account_deleted_event",
        "V1AccountExternalAccountDeletedEvent",
    ),
    "v1.account.external_account.updated": (
        "stripe.events._v1_account_external_account_updated_event",
        "V1AccountExternalAccountUpdatedEvent",
    ),
    "v1.account.updated": (
        "stripe.events._v1_account_updated_event",
        "V1AccountUpdatedEvent",
    ),
    "v1.application_fee.created": (
        "stripe.events._v1_application_fee_created_event",
        "V1ApplicationFeeCreatedEvent",
    ),
    "v1.application_fee.refunded": (
        "stripe.events._v1_application_fee_refunded_event",
        "V1ApplicationFeeRefundedEvent",
    ),
    "v1.application_fee.refund.updated": (
        "stripe.events._v1_application_fee_refund_updated_event",
        "V1ApplicationFeeRefundUpdatedEvent",
    ),
    "v1.balance.available": (
        "stripe.events._v1_balance_available_event",
        "V1BalanceAvailableEvent",
    ),
    "v1.balance_settings.updated": (
        "stripe.events._v1_balance_settings_updated_event",
        "V1BalanceSettingsUpdatedEvent",
    ),
    "v1.billing.alert.triggered": (
        "stripe.events._v1_billing_alert_triggered_event",
        "V1BillingAlertTriggeredEvent",
    ),
    "v1.billing.credit_balance_transaction.created": (
        "stripe.events._v1_billing_credit_balance_transaction_created_event",
        "V1BillingCreditBalanceTransactionCreatedEvent",
    ),
    "v1.billing.credit_grant.created": (
        "stripe.events._v1_billing_credit_grant_created_event",
        "V1BillingCreditGrantCreatedEvent",
    ),
    "v1.billing.credit_grant.updated": (
        "stripe.events._v1_billing_credit_grant_updated_event",
        "V1BillingCreditGrantUpdatedEvent",
    ),
    "v1.billing.meter.created": (
        "stripe.events._v1_billing_meter_created_event",
        "V1BillingMeterCreatedEvent",
    ),
    "v1.billing.meter.deactivated": (
        "stripe.events._v1_billing_meter_deactivated_event",
        "V1BillingMeterDeactivatedEvent",
    ),
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEvent",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEvent",
    ),
    "v1.billing.meter.reactivated": (
        "stripe.events._v1_billing_meter_reactivated_event",
        "V1BillingMeterReactivatedEvent",
    ),
    "v1.billing.meter.updated": (
        "stripe.events._v1_billing_meter_updated_event",
        "V1BillingMeterUpdatedEvent",
    ),
    "v1.billing_portal.configuration.created": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        "V1BillingPortalConfigurationCreatedEvent",
    ),
    "v1.billing_portal.configuration.updated": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        "V1BillingPortalConfigurationUpdatedEvent",
    ),
    "v1.billing_portal.session.created": (
        "stripe.events._v1_billing_portal_session_created_event",
        "V1BillingPortalSessionCreatedEvent",
    ),
    "v1.capability.updated": (
        "stripe.events._v1_capability_updated_event",
        "V1CapabilityUpdatedEvent",
    ),
    "v1.cash_balance.funds_available": (
        "stripe.events._v1_cash_balance_funds_available_event",
        "V1CashBalanceFundsAvailableEvent",
    ),
    "v1.charge.captured": (
        "stripe.events._v1_charge_captured_event",
        "V1ChargeCapturedEvent",
    ),
    "v1.charge.dispute.closed": (
        "stripe.events._v1_charge_dispute_closed_event",
        "V1ChargeDisputeClosedEvent",
    ),
    "v1.charge.dispute.created": (
        "stripe.events._v1_charge_dispute_created_event",
        "V1ChargeDisputeCreatedEvent",
    ),
    "v1.charge.dispute.funds_reinstated": (
        "stripe.events._v1_charge_dispute_funds_reinstated_event",
        "V1ChargeDisputeFundsReinstatedEvent",
    ),
    "v1.charge.dispute.funds_withdrawn": (
        "stripe.events._v1_charge_dispute_funds_withdrawn_event",
        "V1ChargeDisputeFundsWithdrawnEvent",
    ),
    "v1.charge.dispute.updated": (
        "stripe.events._v1_charge_dispute_updated_event",
        "V1ChargeDisputeUpdatedEvent",
    ),
    "v1.charge.expired": (
        "stripe.events._v1_charge_expired_event",
        "V1ChargeExpiredEvent",
    ),
    "v1.charge.failed": (
        "stripe.events._v1_charge_failed_event",
        "V1ChargeFailedEvent",
    ),
    "v1.charge.pending": (
        "stripe.events._v1_charge_pending_event",
        "V1ChargePendingEvent",
    ),
    "v1.charge.refunded": (
        "stripe.events._v1_charge_refunded_event",
        "V1ChargeRefundedEvent",
    ),
    "v1.charge.refund.updated": (
        "stripe.events._v1_charge_refund_updated_event",
        "V1ChargeRefundUpdatedEvent",
    ),
    "v1.charge.succeeded": (
        "stripe.events._v1_charge_succeeded_event",
        "V1ChargeSucceededEvent",
    ),
    "v1.charge.updated": (
        "stripe.events._v1_charge_updated_event",
        "V1ChargeUpdatedEvent",
    ),
    "v1.checkout.session.async_payment_failed": (
        "stripe.events._v1_checkout_session_async_payment_failed_event",
        "V1CheckoutSessionAsyncPaymentFailedEvent",
    ),
    "v1.checkout.session.async_payment_succeeded": (
        "stripe.events._v1_checkout_session_async_payment_succeeded_event",
        "V1CheckoutSessionAsyncPaymentSucceededEvent",
    ),
    "v1.checkout.session.completed": (
        "stripe.events._v1_checkout_session_completed_event",
        "V1CheckoutSessionCompletedEvent",
    ),
    "v1.checkout.session.expired": (
        "stripe.events._v1_checkout_session_expired_event",
        "V1CheckoutSessionExpiredEvent",
    ),
    "v1.climate.order.canceled": (
        "stripe.events._v1_climate_order_canceled_event",
        "V1ClimateOrderCanceledEvent",
    ),
    "v1.climate.order.created": (
        "stripe.events._v1_climate_order_created_event",
        "V1ClimateOrderCreatedEvent",
    ),
    "v1.climate.order.delayed": (
        "stripe.events._v1_climate_order_delayed_event",
        "V1ClimateOrderDelayedEvent",
    ),
    "v1.climate.order.delivered": (
        "stripe.events._v1_climate_order_delivered_event",
        "V1ClimateOrderDeliveredEvent",
    ),
    "v1.climate.order.product_substituted": (
        "stripe.events._v1_climate_order_product_substituted_event",
        "V1ClimateOrderProductSubstitutedEvent",
    ),
    "v1.climate.product.created": (
        "stripe.events._v1_climate_product_created_event",
        "V1ClimateProductCreatedEvent",
    ),
    "v1.climate.product.pricing_updated": (
        "stripe.events._v1_climate_product_pricing_updated_event",
        "V1ClimateProductPricingUpdatedEvent",
    ),
    "v1.coupon.created": (
        "stripe.events._v1_coupon_created_event",
        "V1CouponCreatedEvent",
    ),
    "v1.coupon.deleted": (
        "stripe.events._v1_coupon_deleted_event",
        "V1CouponDeletedEvent",
    ),
    "v1.coupon.updated": (
        "stripe.events._v1_coupon_updated_event",
        "V1CouponUpdatedEvent",
    ),
    "v1.credit_note.created": (
        "stripe.events._v1_credit_note_created_event",
        "V1CreditNoteCreatedEvent",
    ),
    "v1.credit_note.updated": (
        "stripe.events._v1_credit_note_updated_event",
        "V1CreditNoteUpdatedEvent",
    ),
    "v1.credit_note.voided": (
        "stripe.events._v1_credit_note_voided_event",
        "V1CreditNoteVoidedEvent",
    ),
    "v1.customer_cash_balance_transaction.created": (
        "stripe.events._v1_customer_cash_balance_transaction_created_event",
        "V1CustomerCashBalanceTransactionCreatedEvent",
    ),
    "v1.customer.created": (
        "stripe.events._v1_customer_created_event",
        "V1CustomerCreatedEvent",
    ),
    "v1.customer.deleted": (
        "stripe.events._v1_customer_deleted_event",
        "V1CustomerDeletedEvent",
    ),
    "v1.customer.discount.created": (
        "stripe.events._v1_customer_discount_created_event",
        "V1CustomerDiscountCreatedEvent",
    ),
    "v1.customer.discount.deleted": (
        "stripe.events._v1_customer_discount_deleted_event",
        "V1CustomerDiscountDeletedEvent",
    ),
    "v1.customer.discount.updated": (
        "stripe.events._v1_customer_discount_updated_event",
        "V1CustomerDiscountUpdatedEvent",
    ),
    "v1.customer.subscription.created": (
        "stripe.events._v1_customer_subscription_created_event",
        "V1CustomerSubscriptionCreatedEvent",
    ),
    "v1.customer.subscription.deleted": (
        "stripe.events._v1_customer_subscription_deleted_event",
        "V1CustomerSubscriptionDeletedEvent",
    ),
    "v1.customer.subscription.paused": (
        "stripe.events._v1_customer_subscription_paused_event",
        "V1CustomerSubscriptionPausedEvent",
    ),
    "v1.customer.subscription.pending_update_applied": (
        "stripe.events._v1_customer_subscription_pending_update_applied_event",
        "V1CustomerSubscriptionPendingUpdateAppliedEvent",
    ),
    "v1.customer.subscription.pending_update_expired": (
        "stripe.events._v1_customer_subscription_pending_update_expired_event",
        "V1CustomerSubscriptionPendingUpdateExpiredEvent",
    ),
    "v1.customer.subscription.resumed": (
        "stripe.events._v1_customer_subscription_resumed_event",
        "V1CustomerSubscriptionResumedEvent",
    ),
    "v1.customer.subscription.trial_will_end": (
        "stripe.events._v1_customer_subscription_trial_will_end_event",
        "V1CustomerSubscriptionTrialWillEndEvent",
    ),
    "v1.customer.subscription.updated": (
        "stripe.events._v1_customer_subscription_updated_event",
        "V1CustomerSubscriptionUpdatedEvent",
    ),
    "v1.customer.tax_id.created": (
        "stripe.events._v1_customer_tax_id_created_event",
        "V1CustomerTaxIdCreatedEvent",
    ),
    "v1.customer.tax_id.deleted": (
        "stripe.events._v1_customer_tax_id_deleted_event",
        "V1CustomerTaxIdDeletedEvent",
    ),
    "v1.customer.tax_id.updated": (
        "stripe.events._v1_customer_tax_id_updated_event",
        "V1CustomerTaxIdUpdatedEvent",
    ),
    "v1.customer.updated": (
        "stripe.events._v1_customer_updated_event",
        "V1CustomerUpdatedEvent",
    ),
    "v1.entitlements.active_entitlement_summary.updated": (
        "stripe.events._v1_entitlements_active_entitlement_summary_updated_event",
        "V1EntitlementsActiveEntitlementSummaryUpdatedEvent",
    ),
    "v1.file.created": (
        "stripe.events._v1_file_created_event",
        "V1FileCreatedEvent",
    ),
    "v1.financial_connections.account.account_numbers_updated": (
        "stripe.events._v1_financial_connections_account_account_numbers_updated_event",
        "V1FinancialConnectionsAccountAccountNumbersUpdatedEvent",
    ),
    "v1.financial_connections.account.created": (
        "stripe.events._v1_financial_connections_account_created_event",
        "V1FinancialConnectionsAccountCreatedEvent",
    ),
    "v1.financial_connections.account.deactivated": (
        "stripe.events._v1_financial_connections_account_deactivated_event",
        "V1FinancialConnectionsAccountDeactivatedEvent",
    ),
    "v1.financial_connections.account.disconnected": (
        "stripe.events._v1_financial_connections_account_disconnected_event",
        "V1FinancialConnectionsAccountDisconnectedEvent",
    ),
    "v1.financial_connections.account.expected_deactivation_date_updated": (
        "stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event",
        "V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent",
    ),
    "v1.financial_connections.account.reactivated": (
        "stripe.events._v1_financial_connections_account_reactivated_event",
        "V1FinancialConnectionsAccountReactivatedEvent",
    ),
    "v1.financial_connections.account.refreshed_balance": (
        "stripe.events._v1_financial_connections_account_refreshed_balance_event",
        "V1FinancialConnectionsAccountRefreshedBalanceEvent",
    ),
    "v1.financial_connections.account.refreshed_ownership": (
        "stripe.events._v1_financial_connections_account_refreshed_ownership_event",
        "V1FinancialConnectionsAccountRefreshedOwnershipEvent",
    ),
    "v1.financial_connections.account.refreshed_transactions": (
        "stripe.events._v1_financial_connections_account_refreshed_transactions_event",
        "V1FinancialConnectionsAccountRefreshedTransactionsEvent",
    ),
    "v1.financial_connections.account.supported_payment_method_types_updated": (
        "stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event",
        "V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent",
    ),
    "v1.financial_connections.account.upcoming_account_number_expiry": (
        "stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event",
        "V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent",
    ),
    "v1.financial_connections.account.upcoming_deactivation": (
        "stripe.events._v1_financial_connections_account_upcoming_deactivation_event",
        "V1FinancialConnectionsAccountUpcomingDeactivationEvent",
    ),
    "v1.identity.verification_session.canceled": (
        "stripe.events._v1_identity_verification_session_canceled_event",
        "V1IdentityVerificationSessionCanceledEvent",
    ),
    "v1.identity.verification_session.created": (
        "stripe.events._v1_identity_verification_session_created_event",
        "V1IdentityVerificationSessionCreatedEvent",
    ),
    "v1.identity.verification_session.processing": (
        "stripe.events._v1_identity_verification_session_processing_event",
        "V1IdentityVerificationSessionProcessingEvent",
    ),
    "v1.identity.verification_session.redacted": (
        "stripe.events._v1_identity_verification_session_redacted_event",
        "V1IdentityVerificationSessionRedactedEvent",
    ),
    "v1.identity.verification_session.requires_input": (
        "stripe.events._v1_identity_verification_session_requires_input_event",
        "V1IdentityVerificationSessionRequiresInputEvent",
    ),
    "v1.identity.verification_session.verified": (
        "stripe.events._v1_identity_verification_session_verified_event",
        "V1IdentityVerificationSessionVerifiedEvent",
    ),
    "v1.invoice.created": (
        "stripe.events._v1_invoice_created_event",
        "V1InvoiceCreatedEvent",
    ),
    "v1.invoice.deleted": (
        "stripe.events._v1_invoice_deleted_event",
        "V1InvoiceDeletedEvent",
    ),
    "v1.invoice.finalization_failed": (
        "stripe.events._v1_invoice_finalization_failed_event",
        "V1InvoiceFinalizationFailedEvent",
    ),
    "v1.invoice.finalized": (
        "stripe.events._v1_invoice_finalized_event",
        "V1InvoiceFinalizedEvent",
    ),
    "v1.invoiceitem.created": (
        "stripe.events._v1_invoiceitem_created_event",
        "V1InvoiceitemCreatedEvent",
    ),
    "v1.invoiceitem.deleted": (
        "stripe.events._v1_invoiceitem_deleted_event",
        "V1InvoiceitemDeletedEvent",
    ),
    "v1.invoice.marked_uncollectible": (
        "stripe.events._v1_invoice_marked_uncollectible_event",
        "V1InvoiceMarkedUncollectibleEvent",
    ),
    "v1.invoice.overdue": (
        "stripe.events._v1_invoice_overdue_event",
        "V1InvoiceOverdueEvent",
    ),
    "v1.invoice.overpaid": (
        "stripe.events._v1_invoice_overpaid_event",
        "V1InvoiceOverpaidEvent",
    ),
    "v1.invoice.paid": (
        "stripe.events._v1_invoice_paid_event",
        "V1InvoicePaidEvent",
    ),
    "v1.invoice.payment_action_required": (
        "stripe.events._v1_invoice_payment_action_required_event",
        "V1InvoicePaymentActionRequiredEvent",
    ),
    "v1.invoice.payment_attempt_required": (
        "stripe.events._v1_invoice_payment_attempt_required_event",
        "V1InvoicePaymentAttemptRequiredEvent",
    ),
    "v1.invoice.payment_failed": (
        "stripe.events._v1_invoice_payment_failed_event",
        "V1InvoicePaymentFailedEvent",
    ),
    "v1.invoice_payment.paid": (
        "stripe.events._v1_invoice_payment_paid_event",
        "V1InvoicePaymentPaidEvent",
    ),
    "v1.invoice.payment_succeeded": (
        "stripe.events._v1_invoice_payment_succeeded_event",
        "V1InvoicePaymentSucceededEvent",
    ),
    "v1.invoice.sent": (
        "stripe.events._v1_invoice_sent_event",
        "V1InvoiceSentEvent",
    ),
    "v1.invoice.upcoming": (
        "stripe.events._v1_invoice_upcoming_event",
        "V1InvoiceUpcomingEvent",
    ),
    "v1.invoice.updated": (
        "stripe.events._v1_invoice_updated_event",
        "V1InvoiceUpdatedEvent",
    ),
    "v1.invoice.voided": (
        "stripe.events._v1_invoice_voided_event",
        "V1InvoiceVoidedEvent",
    ),
    "v1.invoice.will_be_due": (
        "stripe.events._v1_invoice_will_be_due_event",
        "V1InvoiceWillBeDueEvent",
    ),
    "v1.issuing_authorization.created": (
        "stripe.events._v1_issuing_authorization_created_event",
        "V1IssuingAuthorizationCreatedEvent",
    ),
    "v1.issuing_authorization.request": (
        "stripe.events._v1_issuing_authorization_request_event",
        "V1IssuingAuthorizationRequestEvent",
    ),
    "v1.issuing_authorization.updated": (
        "stripe.events._v1_issuing_authorization_updated_event",
        "V1IssuingAuthorizationUpdatedEvent",
    ),
    "v1.issuing_card.created": (
        "stripe.events._v1_issuing_card_created_event",
        "V1IssuingCardCreatedEvent",
    ),
    "v1.issuing_cardholder.created": (
        "stripe.events._v1_issuing_cardholder_created_event",
        "V1IssuingCardholderCreatedEvent",
    ),
    "v1.issuing_cardholder.updated": (
        "stripe.events._v1_issuing_cardholder_updated_event",
        "V1IssuingCardholderUpdatedEvent",
    ),
    "v1.issuing_card.updated": (
        "stripe.events._v1_issuing_card_updated_event",
        "V1IssuingCardUpdatedEvent",
    ),
    "v1.issuing_dispute.closed": (
        "stripe.events._v1_issuing_dispute_closed_event",
        "V1IssuingDisputeClosedEvent",
    ),
    "v1.issuing_dispute.created": (
        "stripe.events._v1_issuing_dispute_created_event",
        "V1IssuingDisputeCreatedEvent",
    ),
    "v1.issuing_dispute.funds_reinstated": (
        "stripe.events._v1_issuing_dispute_funds_reinstated_event",
        "V1IssuingDisputeFundsReinstatedEvent",
    ),
    "v1.issuing_dispute.funds_rescinded": (
        "stripe.events._v1_issuing_dispute_funds_rescinded_event",
        "V1IssuingDisputeFundsRescindedEvent",
    ),
    "v1.issuing_dispute.submitted": (
        "stripe.events._v1_issuing_dispute_submitted_event",
        "V1IssuingDisputeSubmittedEvent",
    ),
    "v1.issuing_dispute.updated": (
        "stripe.events._v1_issuing_dispute_updated_event",
        "V1IssuingDisputeUpdatedEvent",
    ),
    "v1.issuing_personalization_design.activated": (
        "stripe.events._v1_issuing_personalization_design_activated_event",
        "V1IssuingPersonalizationDesignActivatedEvent",
    ),
    "v1.issuing_personalization_design.deactivated": (
        "stripe.events._v1_issuing_personalization_design_deactivated_event",
        "V1IssuingPersonalizationDesignDeactivatedEvent",
    ),
    "v1.issuing_personalization_design.rejected": (
        "stripe.events._v1_issuing_personalization_design_rejected_event",
        "V1IssuingPersonalizationDesignRejectedEvent",
    ),
    "v1.issuing_personalization_design.updated": (
        "stripe.events._v1_issuing_personalization_design_updated_event",
        "V1IssuingPersonalizationDesignUpdatedEvent",
    ),
    "v1.issuing_token.created": (
        "stripe.events._v1_issuing_token_created_event",
        "V1IssuingTokenCreatedEvent",
    ),
    "v1.issuing_token.updated": (
        "stripe.events._v1_issuing_token_updated_event",
        "V1IssuingTokenUpdatedEvent",
    ),
    "v1.issuing_transaction.created": (
        "stripe.events._v1_issuing_transaction_created_event",
        "V1IssuingTransactionCreatedEvent",
    ),
    "v1.issuing_transaction.purchase_details_receipt_updated": (
        "stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event",
        "V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent",
    ),
    "v1.issuing_transaction.updated": (
        "stripe.events._v1_issuing_transaction_updated_event",
        "V1IssuingTransactionUpdatedEvent",
    ),
    "v1.mandate.updated": (
        "stripe.events._v1_mandate_updated_event",
        "V1MandateUpdatedEvent",
    ),
    "v1.payment_intent.amount_capturable_updated": (
        "stripe.events._v1_payment_intent_amount_capturable_updated_event",
        "V1PaymentIntentAmountCapturableUpdatedEvent",
    ),
    "v1.payment_intent.canceled": (
        "stripe.events._v1_payment_intent_canceled_event",
        "V1PaymentIntentCanceledEvent",
    ),
    "v1.payment_intent.created": (
        "stripe.events._v1_payment_intent_created_event",
        "V1PaymentIntentCreatedEvent",
    ),
    "v1.payment_intent.partially_funded": (
        "stripe.events._v1_payment_intent_partially_funded_event",
        "V1PaymentIntentPartiallyFundedEvent",
    ),
    "v1.payment_intent.payment_failed": (
        "stripe.events._v1_payment_intent_payment_failed_event",
        "V1PaymentIntentPaymentFailedEvent",
    ),
    "v1.payment_intent.processing": (
        "stripe.events._v1_payment_intent_processing_event",
        "V1PaymentIntentProcessingEvent",
    ),
    "v1.payment_intent.requires_action": (
        "stripe.events._v1_payment_intent_requires_action_event",
        "V1PaymentIntentRequiresActionEvent",
    ),
    "v1.payment_intent.succeeded": (
        "stripe.events._v1_payment_intent_succeeded_event",
        "V1PaymentIntentSucceededEvent",
    ),
    "v1.payment_link.created": (
        "stripe.events._v1_payment_link_created_event",
        "V1PaymentLinkCreatedEvent",
    ),
    "v1.payment_link.updated": (
        "stripe.events._v1_payment_link_updated_event",
        "V1PaymentLinkUpdatedEvent",
    ),
    "v1.payment_method.attached": (
        "stripe.events._v1_payment_method_attached_event",
        "V1PaymentMethodAttachedEvent",
    ),
    "v1.payment_method.automatically_updated": (
        "stripe.events._v1_payment_method_automatically_updated_event",
        "V1PaymentMethodAutomaticallyUpdatedEvent",
    ),
    "v1.payment_method.detached": (
        "stripe.events._v1_payment_method_detached_event",
        "V1PaymentMethodDetachedEvent",
    ),
    "v1.payment_method.updated": (
        "stripe.events._v1_payment_method_updated_event",
        "V1PaymentMethodUpdatedEvent",
    ),
    "v1.payout.canceled": (
        "stripe.events._v1_payout_canceled_event",
        "V1PayoutCanceledEvent",
    ),
    "v1.payout.created": (
        "stripe.events._v1_payout_created_event",
        "V1PayoutCreatedEvent",
    ),
    "v1.payout.failed": (
        "stripe.events._v1_payout_failed_event",
        "V1PayoutFailedEvent",
    ),
    "v1.payout.paid": (
        "stripe.events._v1_payout_paid_event",
        "V1PayoutPaidEvent",
    ),
    "v1.payout.reconciliation_completed": (
        "stripe.events._v1_payout_reconciliation_completed_event",
        "V1PayoutReconciliationCompletedEvent",
    ),
    "v1.payout.updated": (
        "stripe.events._v1_payout_updated_event",
        "V1PayoutUpdatedEvent",
    ),
    "v1.person.created": (
        "stripe.events._v1_person_created_event",
        "V1PersonCreatedEvent",
    ),
    "v1.person.deleted": (
        "stripe.events._v1_person_deleted_event",
        "V1PersonDeletedEvent",
    ),
    "v1.person.updated": (
        "stripe.events._v1_person_updated_event",
        "V1PersonUpdatedEvent",
    ),
    "v1.plan.created": (
        "stripe.events._v1_plan_created_event",
        "V1PlanCreatedEvent",
    ),
    "v1.plan.deleted": (
        "stripe.events._v1_plan_deleted_event",
        "V1PlanDeletedEvent",
    ),
    "v1.plan.updated": (
        "stripe.events._v1_plan_updated_event",
        "V1PlanUpdatedEvent",
    ),
    "v1.price.created": (
        "stripe.events._v1_price_created_event",
        "V1PriceCreatedEvent",
    ),
    "v1.price.deleted": (
        "stripe.events._v1_price_deleted_event",
        "V1PriceDeletedEvent",
    ),
    "v1.price.updated": (
        "stripe.events._v1_price_updated_event",
        "V1PriceUpdatedEvent",
    ),
    "v1.product.created": (
        "stripe.events._v1_product_created_event",
        "V1ProductCreatedEvent",
    ),
    "v1.product.deleted": (
        "stripe.events._v1_product_deleted_event",
        "V1ProductDeletedEvent",
    ),
    "v1.product.updated": (
        "stripe.events._v1_product_updated_event",
        "V1ProductUpdatedEvent",
    ),
    "v1.promotion_code.created": (
        "stripe.events._v1_promotion_code_created_event",
        "V1PromotionCodeCreatedEvent",
    ),
    "v1.promotion_code.updated": (
        "stripe.events._v1_promotion_code_updated_event",
        "V1PromotionCodeUpdatedEvent",
    ),
    "v1.quote.accepted": (
        "stripe.events._v1_quote_accepted_event",
        "V1QuoteAcceptedEvent",
    ),
    "v1.quote.canceled": (
        "stripe.events._v1_quote_canceled_event",
        "V1QuoteCanceledEvent",
    ),
    "v1.quote.created": (
        "stripe.events._v1_quote_created_event",
        "V1QuoteCreatedEvent",
    ),
    "v1.quote.finalized": (
        "stripe.events._v1_quote_finalized_event",
        "V1QuoteFinalizedEvent",
    ),
    "v1.radar.early_fraud_warning.created": (
        "stripe.events._v1_radar_early_fraud_warning_created_event",
        "V1RadarEarlyFraudWarningCreatedEvent",
    ),
    "v1.radar.early_fraud_warning.updated": (
        "stripe.events._v1_radar_early_fraud_warning_updated_event",
        "V1RadarEarlyFraudWarningUpdatedEvent",
    ),
    "v1.refund.created": (
        "stripe.events._v1_refund_created_event",
        "V1RefundCreatedEvent",
    ),
    "v1.refund.failed": (
        "stripe.events._v1_refund_failed_event",
        "V1RefundFailedEvent",
    ),
    "v1.refund.updated": (
        "stripe.events._v1_refund_updated_event",
        "V1RefundUpdatedEvent",
    ),
    "v1.review.closed": (
        "stripe.events._v1_review_closed_event",
        "V1ReviewClosedEvent",
    ),
    "v1.review.opened": (
        "stripe.events._v1_review_opened_event",
        "V1ReviewOpenedEvent",
    ),
    "v1.setup_intent.canceled": (
        "stripe.events._v1_setup_intent_canceled_event",
        "V1SetupIntentCanceledEvent",
    ),
    "v1.setup_intent.created": (
        "stripe.events._v1_setup_intent_created_event",
        "V1SetupIntentCreatedEvent",
    ),
    "v1.setup_intent.requires_action": (
        "stripe.events._v1_setup_intent_requires_action_event",
        "V1SetupIntentRequiresActionEvent",
    ),
    "v1.setup_intent.setup_failed": (
        "stripe.events._v1_setup_intent_setup_failed_event",
        "V1SetupIntentSetupFailedEvent",
    ),
    "v1.setup_intent.succeeded": (
        "stripe.events._v1_setup_intent_succeeded_event",
        "V1SetupIntentSucceededEvent",
    ),
    "v1.sigma.scheduled_query_run.created": (
        "stripe.events._v1_sigma_scheduled_query_run_created_event",
        "V1SigmaScheduledQueryRunCreatedEvent",
    ),
    "v1.source.canceled": (
        "stripe.events._v1_source_canceled_event",
        "V1SourceCanceledEvent",
    ),
    "v1.source.chargeable": (
        "stripe.events._v1_source_chargeable_event",
        "V1SourceChargeableEvent",
    ),
    "v1.source.failed": (
        "stripe.events._v1_source_failed_event",
        "V1SourceFailedEvent",
    ),
    "v1.source.refund_attributes_required": (
        "stripe.events._v1_source_refund_attributes_required_event",
        "V1SourceRefundAttributesRequiredEvent",
    ),
    "v1.subscription_schedule.aborted": (
        "stripe.events._v1_subscription_schedule_aborted_event",
        "V1SubscriptionScheduleAbortedEvent",
    ),
    "v1.subscription_schedule.canceled": (
        "stripe.events._v1_subscription_schedule_canceled_event",
        "V1SubscriptionScheduleCanceledEvent",
    ),
    "v1.subscription_schedule.completed": (
        "stripe.events._v1_subscription_schedule_completed_event",
        "V1SubscriptionScheduleCompletedEvent",
    ),
    "v1.subscription_schedule.created": (
        "stripe.events._v1_subscription_schedule_created_event",
        "V1SubscriptionScheduleCreatedEvent",
    ),
    "v1.subscription_schedule.expiring": (
        "stripe.events._v1_subscription_schedule_expiring_event",
        "V1SubscriptionScheduleExpiringEvent",
    ),
    "v1.subscription_schedule.released": (
        "stripe.events._v1_subscription_schedule_released_event",
        "V1SubscriptionScheduleReleasedEvent",
    ),
    "v1.subscription_schedule.updated": (
        "stripe.events._v1_subscription_schedule_updated_event",
        "V1SubscriptionScheduleUpdatedEvent",
    ),
    "v1.tax_rate.created": (
        "stripe.events._v1_tax_rate_created_event",
        "V1TaxRateCreatedEvent",
    ),
    "v1.tax_rate.updated": (
        "stripe.events._v1_tax_rate_updated_event",
        "V1TaxRateUpdatedEvent",
    ),
    "v1.tax.settings.updated": (
        "stripe.events._v1_tax_settings_updated_event",
        "V1TaxSettingsUpdatedEvent",
    ),
    "v1.terminal.reader.action_failed": (
        "stripe.events._v1_terminal_reader_action_failed_event",
        "V1TerminalReaderActionFailedEvent",
    ),
    "v1.terminal.reader.action_succeeded": (
        "stripe.events._v1_terminal_reader_action_succeeded_event",
        "V1TerminalReaderActionSucceededEvent",
    ),
    "v1.terminal.reader.action_updated": (
        "stripe.events._v1_terminal_reader_action_updated_event",
        "V1TerminalReaderActionUpdatedEvent",
    ),
    "v1.test_helpers.test_clock.advancing": (
        "stripe.events._v1_test_helpers_test_clock_advancing_event",
        "V1TestHelpersTestClockAdvancingEvent",
    ),
    "v1.test_helpers.test_clock.created": (
        "stripe.events._v1_test_helpers_test_clock_created_event",
        "V1TestHelpersTestClockCreatedEvent",
    ),
    "v1.test_helpers.test_clock.deleted": (
        "stripe.events._v1_test_helpers_test_clock_deleted_event",
        "V1TestHelpersTestClockDeletedEvent",
    ),
    "v1.test_helpers.test_clock.internal_failure": (
        "stripe.events._v1_test_helpers_test_clock_internal_failure_event",
        "V1TestHelpersTestClockInternalFailureEvent",
    ),
    "v1.test_helpers.test_clock.ready": (
        "stripe.events._v1_test_helpers_test_clock_ready_event",
        "V1TestHelpersTestClockReadyEvent",
    ),
    "v1.topup.canceled": (
        "stripe.events._v1_topup_canceled_event",
        "V1TopupCanceledEvent",
    ),
    "v1.topup.created": (
        "stripe.events._v1_topup_created_event",
        "V1TopupCreatedEvent",
    ),
    "v1.topup.failed": (
        "stripe.events._v1_topup_failed_event",
        "V1TopupFailedEvent",
    ),
    "v1.topup.reversed": (
        "stripe.events._v1_topup_reversed_event",
        "V1TopupReversedEvent",
    ),
    "v1.topup.succeeded": (
        "stripe.events._v1_topup_succeeded_event",
        "V1TopupSucceededEvent",
    ),
    "v1.transfer.created": (
        "stripe.events._v1_transfer_created_event",
        "V1TransferCreatedEvent",
    ),
    "v1.transfer.reversed": (
        "stripe.events._v1_transfer_reversed_event",
        "V1TransferReversedEvent",
    ),
    "v1.transfer.updated": (
        "stripe.events._v1_transfer_updated_event",
        "V1TransferUpdatedEvent",
    ),
    "v2.commerce.product_catalog.imports.failed": (
        "stripe.events._v2_commerce_product_catalog_imports_failed_event",
        "V2CommerceProductCatalogImportsFailedEvent",
    ),
    "v2.commerce.product_catalog.imports.processing": (
        "stripe.events._v2_commerce_product_catalog_imports_processing_event",
        "V2CommerceProductCatalogImportsProcessingEvent",
    ),
    "v2.commerce.product_catalog.imports.succeeded": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_event",
        "V2CommerceProductCatalogImportsSucceededEvent",
    ),
    "v2.commerce.product_catalog.imports.succeeded_with_errors": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event",
        "V2CommerceProductCatalogImportsSucceededWithErrorsEvent",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEvent",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEvent",
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
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEvent",
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
    "v1.account.application.authorized": (
        "stripe.events._v1_account_application_authorized_event",
        "V1AccountApplicationAuthorizedEventNotification",
    ),
    "v1.account.application.deauthorized": (
        "stripe.events._v1_account_application_deauthorized_event",
        "V1AccountApplicationDeauthorizedEventNotification",
    ),
    "v1.account.external_account.created": (
        "stripe.events._v1_account_external_account_created_event",
        "V1AccountExternalAccountCreatedEventNotification",
    ),
    "v1.account.external_account.deleted": (
        "stripe.events._v1_account_external_account_deleted_event",
        "V1AccountExternalAccountDeletedEventNotification",
    ),
    "v1.account.external_account.updated": (
        "stripe.events._v1_account_external_account_updated_event",
        "V1AccountExternalAccountUpdatedEventNotification",
    ),
    "v1.account.updated": (
        "stripe.events._v1_account_updated_event",
        "V1AccountUpdatedEventNotification",
    ),
    "v1.application_fee.created": (
        "stripe.events._v1_application_fee_created_event",
        "V1ApplicationFeeCreatedEventNotification",
    ),
    "v1.application_fee.refunded": (
        "stripe.events._v1_application_fee_refunded_event",
        "V1ApplicationFeeRefundedEventNotification",
    ),
    "v1.application_fee.refund.updated": (
        "stripe.events._v1_application_fee_refund_updated_event",
        "V1ApplicationFeeRefundUpdatedEventNotification",
    ),
    "v1.balance.available": (
        "stripe.events._v1_balance_available_event",
        "V1BalanceAvailableEventNotification",
    ),
    "v1.balance_settings.updated": (
        "stripe.events._v1_balance_settings_updated_event",
        "V1BalanceSettingsUpdatedEventNotification",
    ),
    "v1.billing.alert.triggered": (
        "stripe.events._v1_billing_alert_triggered_event",
        "V1BillingAlertTriggeredEventNotification",
    ),
    "v1.billing.credit_balance_transaction.created": (
        "stripe.events._v1_billing_credit_balance_transaction_created_event",
        "V1BillingCreditBalanceTransactionCreatedEventNotification",
    ),
    "v1.billing.credit_grant.created": (
        "stripe.events._v1_billing_credit_grant_created_event",
        "V1BillingCreditGrantCreatedEventNotification",
    ),
    "v1.billing.credit_grant.updated": (
        "stripe.events._v1_billing_credit_grant_updated_event",
        "V1BillingCreditGrantUpdatedEventNotification",
    ),
    "v1.billing.meter.created": (
        "stripe.events._v1_billing_meter_created_event",
        "V1BillingMeterCreatedEventNotification",
    ),
    "v1.billing.meter.deactivated": (
        "stripe.events._v1_billing_meter_deactivated_event",
        "V1BillingMeterDeactivatedEventNotification",
    ),
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEventNotification",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEventNotification",
    ),
    "v1.billing.meter.reactivated": (
        "stripe.events._v1_billing_meter_reactivated_event",
        "V1BillingMeterReactivatedEventNotification",
    ),
    "v1.billing.meter.updated": (
        "stripe.events._v1_billing_meter_updated_event",
        "V1BillingMeterUpdatedEventNotification",
    ),
    "v1.billing_portal.configuration.created": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        "V1BillingPortalConfigurationCreatedEventNotification",
    ),
    "v1.billing_portal.configuration.updated": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        "V1BillingPortalConfigurationUpdatedEventNotification",
    ),
    "v1.billing_portal.session.created": (
        "stripe.events._v1_billing_portal_session_created_event",
        "V1BillingPortalSessionCreatedEventNotification",
    ),
    "v1.capability.updated": (
        "stripe.events._v1_capability_updated_event",
        "V1CapabilityUpdatedEventNotification",
    ),
    "v1.cash_balance.funds_available": (
        "stripe.events._v1_cash_balance_funds_available_event",
        "V1CashBalanceFundsAvailableEventNotification",
    ),
    "v1.charge.captured": (
        "stripe.events._v1_charge_captured_event",
        "V1ChargeCapturedEventNotification",
    ),
    "v1.charge.dispute.closed": (
        "stripe.events._v1_charge_dispute_closed_event",
        "V1ChargeDisputeClosedEventNotification",
    ),
    "v1.charge.dispute.created": (
        "stripe.events._v1_charge_dispute_created_event",
        "V1ChargeDisputeCreatedEventNotification",
    ),
    "v1.charge.dispute.funds_reinstated": (
        "stripe.events._v1_charge_dispute_funds_reinstated_event",
        "V1ChargeDisputeFundsReinstatedEventNotification",
    ),
    "v1.charge.dispute.funds_withdrawn": (
        "stripe.events._v1_charge_dispute_funds_withdrawn_event",
        "V1ChargeDisputeFundsWithdrawnEventNotification",
    ),
    "v1.charge.dispute.updated": (
        "stripe.events._v1_charge_dispute_updated_event",
        "V1ChargeDisputeUpdatedEventNotification",
    ),
    "v1.charge.expired": (
        "stripe.events._v1_charge_expired_event",
        "V1ChargeExpiredEventNotification",
    ),
    "v1.charge.failed": (
        "stripe.events._v1_charge_failed_event",
        "V1ChargeFailedEventNotification",
    ),
    "v1.charge.pending": (
        "stripe.events._v1_charge_pending_event",
        "V1ChargePendingEventNotification",
    ),
    "v1.charge.refunded": (
        "stripe.events._v1_charge_refunded_event",
        "V1ChargeRefundedEventNotification",
    ),
    "v1.charge.refund.updated": (
        "stripe.events._v1_charge_refund_updated_event",
        "V1ChargeRefundUpdatedEventNotification",
    ),
    "v1.charge.succeeded": (
        "stripe.events._v1_charge_succeeded_event",
        "V1ChargeSucceededEventNotification",
    ),
    "v1.charge.updated": (
        "stripe.events._v1_charge_updated_event",
        "V1ChargeUpdatedEventNotification",
    ),
    "v1.checkout.session.async_payment_failed": (
        "stripe.events._v1_checkout_session_async_payment_failed_event",
        "V1CheckoutSessionAsyncPaymentFailedEventNotification",
    ),
    "v1.checkout.session.async_payment_succeeded": (
        "stripe.events._v1_checkout_session_async_payment_succeeded_event",
        "V1CheckoutSessionAsyncPaymentSucceededEventNotification",
    ),
    "v1.checkout.session.completed": (
        "stripe.events._v1_checkout_session_completed_event",
        "V1CheckoutSessionCompletedEventNotification",
    ),
    "v1.checkout.session.expired": (
        "stripe.events._v1_checkout_session_expired_event",
        "V1CheckoutSessionExpiredEventNotification",
    ),
    "v1.climate.order.canceled": (
        "stripe.events._v1_climate_order_canceled_event",
        "V1ClimateOrderCanceledEventNotification",
    ),
    "v1.climate.order.created": (
        "stripe.events._v1_climate_order_created_event",
        "V1ClimateOrderCreatedEventNotification",
    ),
    "v1.climate.order.delayed": (
        "stripe.events._v1_climate_order_delayed_event",
        "V1ClimateOrderDelayedEventNotification",
    ),
    "v1.climate.order.delivered": (
        "stripe.events._v1_climate_order_delivered_event",
        "V1ClimateOrderDeliveredEventNotification",
    ),
    "v1.climate.order.product_substituted": (
        "stripe.events._v1_climate_order_product_substituted_event",
        "V1ClimateOrderProductSubstitutedEventNotification",
    ),
    "v1.climate.product.created": (
        "stripe.events._v1_climate_product_created_event",
        "V1ClimateProductCreatedEventNotification",
    ),
    "v1.climate.product.pricing_updated": (
        "stripe.events._v1_climate_product_pricing_updated_event",
        "V1ClimateProductPricingUpdatedEventNotification",
    ),
    "v1.coupon.created": (
        "stripe.events._v1_coupon_created_event",
        "V1CouponCreatedEventNotification",
    ),
    "v1.coupon.deleted": (
        "stripe.events._v1_coupon_deleted_event",
        "V1CouponDeletedEventNotification",
    ),
    "v1.coupon.updated": (
        "stripe.events._v1_coupon_updated_event",
        "V1CouponUpdatedEventNotification",
    ),
    "v1.credit_note.created": (
        "stripe.events._v1_credit_note_created_event",
        "V1CreditNoteCreatedEventNotification",
    ),
    "v1.credit_note.updated": (
        "stripe.events._v1_credit_note_updated_event",
        "V1CreditNoteUpdatedEventNotification",
    ),
    "v1.credit_note.voided": (
        "stripe.events._v1_credit_note_voided_event",
        "V1CreditNoteVoidedEventNotification",
    ),
    "v1.customer_cash_balance_transaction.created": (
        "stripe.events._v1_customer_cash_balance_transaction_created_event",
        "V1CustomerCashBalanceTransactionCreatedEventNotification",
    ),
    "v1.customer.created": (
        "stripe.events._v1_customer_created_event",
        "V1CustomerCreatedEventNotification",
    ),
    "v1.customer.deleted": (
        "stripe.events._v1_customer_deleted_event",
        "V1CustomerDeletedEventNotification",
    ),
    "v1.customer.discount.created": (
        "stripe.events._v1_customer_discount_created_event",
        "V1CustomerDiscountCreatedEventNotification",
    ),
    "v1.customer.discount.deleted": (
        "stripe.events._v1_customer_discount_deleted_event",
        "V1CustomerDiscountDeletedEventNotification",
    ),
    "v1.customer.discount.updated": (
        "stripe.events._v1_customer_discount_updated_event",
        "V1CustomerDiscountUpdatedEventNotification",
    ),
    "v1.customer.subscription.created": (
        "stripe.events._v1_customer_subscription_created_event",
        "V1CustomerSubscriptionCreatedEventNotification",
    ),
    "v1.customer.subscription.deleted": (
        "stripe.events._v1_customer_subscription_deleted_event",
        "V1CustomerSubscriptionDeletedEventNotification",
    ),
    "v1.customer.subscription.paused": (
        "stripe.events._v1_customer_subscription_paused_event",
        "V1CustomerSubscriptionPausedEventNotification",
    ),
    "v1.customer.subscription.pending_update_applied": (
        "stripe.events._v1_customer_subscription_pending_update_applied_event",
        "V1CustomerSubscriptionPendingUpdateAppliedEventNotification",
    ),
    "v1.customer.subscription.pending_update_expired": (
        "stripe.events._v1_customer_subscription_pending_update_expired_event",
        "V1CustomerSubscriptionPendingUpdateExpiredEventNotification",
    ),
    "v1.customer.subscription.resumed": (
        "stripe.events._v1_customer_subscription_resumed_event",
        "V1CustomerSubscriptionResumedEventNotification",
    ),
    "v1.customer.subscription.trial_will_end": (
        "stripe.events._v1_customer_subscription_trial_will_end_event",
        "V1CustomerSubscriptionTrialWillEndEventNotification",
    ),
    "v1.customer.subscription.updated": (
        "stripe.events._v1_customer_subscription_updated_event",
        "V1CustomerSubscriptionUpdatedEventNotification",
    ),
    "v1.customer.tax_id.created": (
        "stripe.events._v1_customer_tax_id_created_event",
        "V1CustomerTaxIdCreatedEventNotification",
    ),
    "v1.customer.tax_id.deleted": (
        "stripe.events._v1_customer_tax_id_deleted_event",
        "V1CustomerTaxIdDeletedEventNotification",
    ),
    "v1.customer.tax_id.updated": (
        "stripe.events._v1_customer_tax_id_updated_event",
        "V1CustomerTaxIdUpdatedEventNotification",
    ),
    "v1.customer.updated": (
        "stripe.events._v1_customer_updated_event",
        "V1CustomerUpdatedEventNotification",
    ),
    "v1.entitlements.active_entitlement_summary.updated": (
        "stripe.events._v1_entitlements_active_entitlement_summary_updated_event",
        "V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification",
    ),
    "v1.file.created": (
        "stripe.events._v1_file_created_event",
        "V1FileCreatedEventNotification",
    ),
    "v1.financial_connections.account.account_numbers_updated": (
        "stripe.events._v1_financial_connections_account_account_numbers_updated_event",
        "V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification",
    ),
    "v1.financial_connections.account.created": (
        "stripe.events._v1_financial_connections_account_created_event",
        "V1FinancialConnectionsAccountCreatedEventNotification",
    ),
    "v1.financial_connections.account.deactivated": (
        "stripe.events._v1_financial_connections_account_deactivated_event",
        "V1FinancialConnectionsAccountDeactivatedEventNotification",
    ),
    "v1.financial_connections.account.disconnected": (
        "stripe.events._v1_financial_connections_account_disconnected_event",
        "V1FinancialConnectionsAccountDisconnectedEventNotification",
    ),
    "v1.financial_connections.account.expected_deactivation_date_updated": (
        "stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event",
        "V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification",
    ),
    "v1.financial_connections.account.reactivated": (
        "stripe.events._v1_financial_connections_account_reactivated_event",
        "V1FinancialConnectionsAccountReactivatedEventNotification",
    ),
    "v1.financial_connections.account.refreshed_balance": (
        "stripe.events._v1_financial_connections_account_refreshed_balance_event",
        "V1FinancialConnectionsAccountRefreshedBalanceEventNotification",
    ),
    "v1.financial_connections.account.refreshed_ownership": (
        "stripe.events._v1_financial_connections_account_refreshed_ownership_event",
        "V1FinancialConnectionsAccountRefreshedOwnershipEventNotification",
    ),
    "v1.financial_connections.account.refreshed_transactions": (
        "stripe.events._v1_financial_connections_account_refreshed_transactions_event",
        "V1FinancialConnectionsAccountRefreshedTransactionsEventNotification",
    ),
    "v1.financial_connections.account.supported_payment_method_types_updated": (
        "stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event",
        "V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification",
    ),
    "v1.financial_connections.account.upcoming_account_number_expiry": (
        "stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event",
        "V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification",
    ),
    "v1.financial_connections.account.upcoming_deactivation": (
        "stripe.events._v1_financial_connections_account_upcoming_deactivation_event",
        "V1FinancialConnectionsAccountUpcomingDeactivationEventNotification",
    ),
    "v1.identity.verification_session.canceled": (
        "stripe.events._v1_identity_verification_session_canceled_event",
        "V1IdentityVerificationSessionCanceledEventNotification",
    ),
    "v1.identity.verification_session.created": (
        "stripe.events._v1_identity_verification_session_created_event",
        "V1IdentityVerificationSessionCreatedEventNotification",
    ),
    "v1.identity.verification_session.processing": (
        "stripe.events._v1_identity_verification_session_processing_event",
        "V1IdentityVerificationSessionProcessingEventNotification",
    ),
    "v1.identity.verification_session.redacted": (
        "stripe.events._v1_identity_verification_session_redacted_event",
        "V1IdentityVerificationSessionRedactedEventNotification",
    ),
    "v1.identity.verification_session.requires_input": (
        "stripe.events._v1_identity_verification_session_requires_input_event",
        "V1IdentityVerificationSessionRequiresInputEventNotification",
    ),
    "v1.identity.verification_session.verified": (
        "stripe.events._v1_identity_verification_session_verified_event",
        "V1IdentityVerificationSessionVerifiedEventNotification",
    ),
    "v1.invoice.created": (
        "stripe.events._v1_invoice_created_event",
        "V1InvoiceCreatedEventNotification",
    ),
    "v1.invoice.deleted": (
        "stripe.events._v1_invoice_deleted_event",
        "V1InvoiceDeletedEventNotification",
    ),
    "v1.invoice.finalization_failed": (
        "stripe.events._v1_invoice_finalization_failed_event",
        "V1InvoiceFinalizationFailedEventNotification",
    ),
    "v1.invoice.finalized": (
        "stripe.events._v1_invoice_finalized_event",
        "V1InvoiceFinalizedEventNotification",
    ),
    "v1.invoiceitem.created": (
        "stripe.events._v1_invoiceitem_created_event",
        "V1InvoiceitemCreatedEventNotification",
    ),
    "v1.invoiceitem.deleted": (
        "stripe.events._v1_invoiceitem_deleted_event",
        "V1InvoiceitemDeletedEventNotification",
    ),
    "v1.invoice.marked_uncollectible": (
        "stripe.events._v1_invoice_marked_uncollectible_event",
        "V1InvoiceMarkedUncollectibleEventNotification",
    ),
    "v1.invoice.overdue": (
        "stripe.events._v1_invoice_overdue_event",
        "V1InvoiceOverdueEventNotification",
    ),
    "v1.invoice.overpaid": (
        "stripe.events._v1_invoice_overpaid_event",
        "V1InvoiceOverpaidEventNotification",
    ),
    "v1.invoice.paid": (
        "stripe.events._v1_invoice_paid_event",
        "V1InvoicePaidEventNotification",
    ),
    "v1.invoice.payment_action_required": (
        "stripe.events._v1_invoice_payment_action_required_event",
        "V1InvoicePaymentActionRequiredEventNotification",
    ),
    "v1.invoice.payment_attempt_required": (
        "stripe.events._v1_invoice_payment_attempt_required_event",
        "V1InvoicePaymentAttemptRequiredEventNotification",
    ),
    "v1.invoice.payment_failed": (
        "stripe.events._v1_invoice_payment_failed_event",
        "V1InvoicePaymentFailedEventNotification",
    ),
    "v1.invoice_payment.paid": (
        "stripe.events._v1_invoice_payment_paid_event",
        "V1InvoicePaymentPaidEventNotification",
    ),
    "v1.invoice.payment_succeeded": (
        "stripe.events._v1_invoice_payment_succeeded_event",
        "V1InvoicePaymentSucceededEventNotification",
    ),
    "v1.invoice.sent": (
        "stripe.events._v1_invoice_sent_event",
        "V1InvoiceSentEventNotification",
    ),
    "v1.invoice.upcoming": (
        "stripe.events._v1_invoice_upcoming_event",
        "V1InvoiceUpcomingEventNotification",
    ),
    "v1.invoice.updated": (
        "stripe.events._v1_invoice_updated_event",
        "V1InvoiceUpdatedEventNotification",
    ),
    "v1.invoice.voided": (
        "stripe.events._v1_invoice_voided_event",
        "V1InvoiceVoidedEventNotification",
    ),
    "v1.invoice.will_be_due": (
        "stripe.events._v1_invoice_will_be_due_event",
        "V1InvoiceWillBeDueEventNotification",
    ),
    "v1.issuing_authorization.created": (
        "stripe.events._v1_issuing_authorization_created_event",
        "V1IssuingAuthorizationCreatedEventNotification",
    ),
    "v1.issuing_authorization.request": (
        "stripe.events._v1_issuing_authorization_request_event",
        "V1IssuingAuthorizationRequestEventNotification",
    ),
    "v1.issuing_authorization.updated": (
        "stripe.events._v1_issuing_authorization_updated_event",
        "V1IssuingAuthorizationUpdatedEventNotification",
    ),
    "v1.issuing_card.created": (
        "stripe.events._v1_issuing_card_created_event",
        "V1IssuingCardCreatedEventNotification",
    ),
    "v1.issuing_cardholder.created": (
        "stripe.events._v1_issuing_cardholder_created_event",
        "V1IssuingCardholderCreatedEventNotification",
    ),
    "v1.issuing_cardholder.updated": (
        "stripe.events._v1_issuing_cardholder_updated_event",
        "V1IssuingCardholderUpdatedEventNotification",
    ),
    "v1.issuing_card.updated": (
        "stripe.events._v1_issuing_card_updated_event",
        "V1IssuingCardUpdatedEventNotification",
    ),
    "v1.issuing_dispute.closed": (
        "stripe.events._v1_issuing_dispute_closed_event",
        "V1IssuingDisputeClosedEventNotification",
    ),
    "v1.issuing_dispute.created": (
        "stripe.events._v1_issuing_dispute_created_event",
        "V1IssuingDisputeCreatedEventNotification",
    ),
    "v1.issuing_dispute.funds_reinstated": (
        "stripe.events._v1_issuing_dispute_funds_reinstated_event",
        "V1IssuingDisputeFundsReinstatedEventNotification",
    ),
    "v1.issuing_dispute.funds_rescinded": (
        "stripe.events._v1_issuing_dispute_funds_rescinded_event",
        "V1IssuingDisputeFundsRescindedEventNotification",
    ),
    "v1.issuing_dispute.submitted": (
        "stripe.events._v1_issuing_dispute_submitted_event",
        "V1IssuingDisputeSubmittedEventNotification",
    ),
    "v1.issuing_dispute.updated": (
        "stripe.events._v1_issuing_dispute_updated_event",
        "V1IssuingDisputeUpdatedEventNotification",
    ),
    "v1.issuing_personalization_design.activated": (
        "stripe.events._v1_issuing_personalization_design_activated_event",
        "V1IssuingPersonalizationDesignActivatedEventNotification",
    ),
    "v1.issuing_personalization_design.deactivated": (
        "stripe.events._v1_issuing_personalization_design_deactivated_event",
        "V1IssuingPersonalizationDesignDeactivatedEventNotification",
    ),
    "v1.issuing_personalization_design.rejected": (
        "stripe.events._v1_issuing_personalization_design_rejected_event",
        "V1IssuingPersonalizationDesignRejectedEventNotification",
    ),
    "v1.issuing_personalization_design.updated": (
        "stripe.events._v1_issuing_personalization_design_updated_event",
        "V1IssuingPersonalizationDesignUpdatedEventNotification",
    ),
    "v1.issuing_token.created": (
        "stripe.events._v1_issuing_token_created_event",
        "V1IssuingTokenCreatedEventNotification",
    ),
    "v1.issuing_token.updated": (
        "stripe.events._v1_issuing_token_updated_event",
        "V1IssuingTokenUpdatedEventNotification",
    ),
    "v1.issuing_transaction.created": (
        "stripe.events._v1_issuing_transaction_created_event",
        "V1IssuingTransactionCreatedEventNotification",
    ),
    "v1.issuing_transaction.purchase_details_receipt_updated": (
        "stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event",
        "V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification",
    ),
    "v1.issuing_transaction.updated": (
        "stripe.events._v1_issuing_transaction_updated_event",
        "V1IssuingTransactionUpdatedEventNotification",
    ),
    "v1.mandate.updated": (
        "stripe.events._v1_mandate_updated_event",
        "V1MandateUpdatedEventNotification",
    ),
    "v1.payment_intent.amount_capturable_updated": (
        "stripe.events._v1_payment_intent_amount_capturable_updated_event",
        "V1PaymentIntentAmountCapturableUpdatedEventNotification",
    ),
    "v1.payment_intent.canceled": (
        "stripe.events._v1_payment_intent_canceled_event",
        "V1PaymentIntentCanceledEventNotification",
    ),
    "v1.payment_intent.created": (
        "stripe.events._v1_payment_intent_created_event",
        "V1PaymentIntentCreatedEventNotification",
    ),
    "v1.payment_intent.partially_funded": (
        "stripe.events._v1_payment_intent_partially_funded_event",
        "V1PaymentIntentPartiallyFundedEventNotification",
    ),
    "v1.payment_intent.payment_failed": (
        "stripe.events._v1_payment_intent_payment_failed_event",
        "V1PaymentIntentPaymentFailedEventNotification",
    ),
    "v1.payment_intent.processing": (
        "stripe.events._v1_payment_intent_processing_event",
        "V1PaymentIntentProcessingEventNotification",
    ),
    "v1.payment_intent.requires_action": (
        "stripe.events._v1_payment_intent_requires_action_event",
        "V1PaymentIntentRequiresActionEventNotification",
    ),
    "v1.payment_intent.succeeded": (
        "stripe.events._v1_payment_intent_succeeded_event",
        "V1PaymentIntentSucceededEventNotification",
    ),
    "v1.payment_link.created": (
        "stripe.events._v1_payment_link_created_event",
        "V1PaymentLinkCreatedEventNotification",
    ),
    "v1.payment_link.updated": (
        "stripe.events._v1_payment_link_updated_event",
        "V1PaymentLinkUpdatedEventNotification",
    ),
    "v1.payment_method.attached": (
        "stripe.events._v1_payment_method_attached_event",
        "V1PaymentMethodAttachedEventNotification",
    ),
    "v1.payment_method.automatically_updated": (
        "stripe.events._v1_payment_method_automatically_updated_event",
        "V1PaymentMethodAutomaticallyUpdatedEventNotification",
    ),
    "v1.payment_method.detached": (
        "stripe.events._v1_payment_method_detached_event",
        "V1PaymentMethodDetachedEventNotification",
    ),
    "v1.payment_method.updated": (
        "stripe.events._v1_payment_method_updated_event",
        "V1PaymentMethodUpdatedEventNotification",
    ),
    "v1.payout.canceled": (
        "stripe.events._v1_payout_canceled_event",
        "V1PayoutCanceledEventNotification",
    ),
    "v1.payout.created": (
        "stripe.events._v1_payout_created_event",
        "V1PayoutCreatedEventNotification",
    ),
    "v1.payout.failed": (
        "stripe.events._v1_payout_failed_event",
        "V1PayoutFailedEventNotification",
    ),
    "v1.payout.paid": (
        "stripe.events._v1_payout_paid_event",
        "V1PayoutPaidEventNotification",
    ),
    "v1.payout.reconciliation_completed": (
        "stripe.events._v1_payout_reconciliation_completed_event",
        "V1PayoutReconciliationCompletedEventNotification",
    ),
    "v1.payout.updated": (
        "stripe.events._v1_payout_updated_event",
        "V1PayoutUpdatedEventNotification",
    ),
    "v1.person.created": (
        "stripe.events._v1_person_created_event",
        "V1PersonCreatedEventNotification",
    ),
    "v1.person.deleted": (
        "stripe.events._v1_person_deleted_event",
        "V1PersonDeletedEventNotification",
    ),
    "v1.person.updated": (
        "stripe.events._v1_person_updated_event",
        "V1PersonUpdatedEventNotification",
    ),
    "v1.plan.created": (
        "stripe.events._v1_plan_created_event",
        "V1PlanCreatedEventNotification",
    ),
    "v1.plan.deleted": (
        "stripe.events._v1_plan_deleted_event",
        "V1PlanDeletedEventNotification",
    ),
    "v1.plan.updated": (
        "stripe.events._v1_plan_updated_event",
        "V1PlanUpdatedEventNotification",
    ),
    "v1.price.created": (
        "stripe.events._v1_price_created_event",
        "V1PriceCreatedEventNotification",
    ),
    "v1.price.deleted": (
        "stripe.events._v1_price_deleted_event",
        "V1PriceDeletedEventNotification",
    ),
    "v1.price.updated": (
        "stripe.events._v1_price_updated_event",
        "V1PriceUpdatedEventNotification",
    ),
    "v1.product.created": (
        "stripe.events._v1_product_created_event",
        "V1ProductCreatedEventNotification",
    ),
    "v1.product.deleted": (
        "stripe.events._v1_product_deleted_event",
        "V1ProductDeletedEventNotification",
    ),
    "v1.product.updated": (
        "stripe.events._v1_product_updated_event",
        "V1ProductUpdatedEventNotification",
    ),
    "v1.promotion_code.created": (
        "stripe.events._v1_promotion_code_created_event",
        "V1PromotionCodeCreatedEventNotification",
    ),
    "v1.promotion_code.updated": (
        "stripe.events._v1_promotion_code_updated_event",
        "V1PromotionCodeUpdatedEventNotification",
    ),
    "v1.quote.accepted": (
        "stripe.events._v1_quote_accepted_event",
        "V1QuoteAcceptedEventNotification",
    ),
    "v1.quote.canceled": (
        "stripe.events._v1_quote_canceled_event",
        "V1QuoteCanceledEventNotification",
    ),
    "v1.quote.created": (
        "stripe.events._v1_quote_created_event",
        "V1QuoteCreatedEventNotification",
    ),
    "v1.quote.finalized": (
        "stripe.events._v1_quote_finalized_event",
        "V1QuoteFinalizedEventNotification",
    ),
    "v1.radar.early_fraud_warning.created": (
        "stripe.events._v1_radar_early_fraud_warning_created_event",
        "V1RadarEarlyFraudWarningCreatedEventNotification",
    ),
    "v1.radar.early_fraud_warning.updated": (
        "stripe.events._v1_radar_early_fraud_warning_updated_event",
        "V1RadarEarlyFraudWarningUpdatedEventNotification",
    ),
    "v1.refund.created": (
        "stripe.events._v1_refund_created_event",
        "V1RefundCreatedEventNotification",
    ),
    "v1.refund.failed": (
        "stripe.events._v1_refund_failed_event",
        "V1RefundFailedEventNotification",
    ),
    "v1.refund.updated": (
        "stripe.events._v1_refund_updated_event",
        "V1RefundUpdatedEventNotification",
    ),
    "v1.review.closed": (
        "stripe.events._v1_review_closed_event",
        "V1ReviewClosedEventNotification",
    ),
    "v1.review.opened": (
        "stripe.events._v1_review_opened_event",
        "V1ReviewOpenedEventNotification",
    ),
    "v1.setup_intent.canceled": (
        "stripe.events._v1_setup_intent_canceled_event",
        "V1SetupIntentCanceledEventNotification",
    ),
    "v1.setup_intent.created": (
        "stripe.events._v1_setup_intent_created_event",
        "V1SetupIntentCreatedEventNotification",
    ),
    "v1.setup_intent.requires_action": (
        "stripe.events._v1_setup_intent_requires_action_event",
        "V1SetupIntentRequiresActionEventNotification",
    ),
    "v1.setup_intent.setup_failed": (
        "stripe.events._v1_setup_intent_setup_failed_event",
        "V1SetupIntentSetupFailedEventNotification",
    ),
    "v1.setup_intent.succeeded": (
        "stripe.events._v1_setup_intent_succeeded_event",
        "V1SetupIntentSucceededEventNotification",
    ),
    "v1.sigma.scheduled_query_run.created": (
        "stripe.events._v1_sigma_scheduled_query_run_created_event",
        "V1SigmaScheduledQueryRunCreatedEventNotification",
    ),
    "v1.source.canceled": (
        "stripe.events._v1_source_canceled_event",
        "V1SourceCanceledEventNotification",
    ),
    "v1.source.chargeable": (
        "stripe.events._v1_source_chargeable_event",
        "V1SourceChargeableEventNotification",
    ),
    "v1.source.failed": (
        "stripe.events._v1_source_failed_event",
        "V1SourceFailedEventNotification",
    ),
    "v1.source.refund_attributes_required": (
        "stripe.events._v1_source_refund_attributes_required_event",
        "V1SourceRefundAttributesRequiredEventNotification",
    ),
    "v1.subscription_schedule.aborted": (
        "stripe.events._v1_subscription_schedule_aborted_event",
        "V1SubscriptionScheduleAbortedEventNotification",
    ),
    "v1.subscription_schedule.canceled": (
        "stripe.events._v1_subscription_schedule_canceled_event",
        "V1SubscriptionScheduleCanceledEventNotification",
    ),
    "v1.subscription_schedule.completed": (
        "stripe.events._v1_subscription_schedule_completed_event",
        "V1SubscriptionScheduleCompletedEventNotification",
    ),
    "v1.subscription_schedule.created": (
        "stripe.events._v1_subscription_schedule_created_event",
        "V1SubscriptionScheduleCreatedEventNotification",
    ),
    "v1.subscription_schedule.expiring": (
        "stripe.events._v1_subscription_schedule_expiring_event",
        "V1SubscriptionScheduleExpiringEventNotification",
    ),
    "v1.subscription_schedule.released": (
        "stripe.events._v1_subscription_schedule_released_event",
        "V1SubscriptionScheduleReleasedEventNotification",
    ),
    "v1.subscription_schedule.updated": (
        "stripe.events._v1_subscription_schedule_updated_event",
        "V1SubscriptionScheduleUpdatedEventNotification",
    ),
    "v1.tax_rate.created": (
        "stripe.events._v1_tax_rate_created_event",
        "V1TaxRateCreatedEventNotification",
    ),
    "v1.tax_rate.updated": (
        "stripe.events._v1_tax_rate_updated_event",
        "V1TaxRateUpdatedEventNotification",
    ),
    "v1.tax.settings.updated": (
        "stripe.events._v1_tax_settings_updated_event",
        "V1TaxSettingsUpdatedEventNotification",
    ),
    "v1.terminal.reader.action_failed": (
        "stripe.events._v1_terminal_reader_action_failed_event",
        "V1TerminalReaderActionFailedEventNotification",
    ),
    "v1.terminal.reader.action_succeeded": (
        "stripe.events._v1_terminal_reader_action_succeeded_event",
        "V1TerminalReaderActionSucceededEventNotification",
    ),
    "v1.terminal.reader.action_updated": (
        "stripe.events._v1_terminal_reader_action_updated_event",
        "V1TerminalReaderActionUpdatedEventNotification",
    ),
    "v1.test_helpers.test_clock.advancing": (
        "stripe.events._v1_test_helpers_test_clock_advancing_event",
        "V1TestHelpersTestClockAdvancingEventNotification",
    ),
    "v1.test_helpers.test_clock.created": (
        "stripe.events._v1_test_helpers_test_clock_created_event",
        "V1TestHelpersTestClockCreatedEventNotification",
    ),
    "v1.test_helpers.test_clock.deleted": (
        "stripe.events._v1_test_helpers_test_clock_deleted_event",
        "V1TestHelpersTestClockDeletedEventNotification",
    ),
    "v1.test_helpers.test_clock.internal_failure": (
        "stripe.events._v1_test_helpers_test_clock_internal_failure_event",
        "V1TestHelpersTestClockInternalFailureEventNotification",
    ),
    "v1.test_helpers.test_clock.ready": (
        "stripe.events._v1_test_helpers_test_clock_ready_event",
        "V1TestHelpersTestClockReadyEventNotification",
    ),
    "v1.topup.canceled": (
        "stripe.events._v1_topup_canceled_event",
        "V1TopupCanceledEventNotification",
    ),
    "v1.topup.created": (
        "stripe.events._v1_topup_created_event",
        "V1TopupCreatedEventNotification",
    ),
    "v1.topup.failed": (
        "stripe.events._v1_topup_failed_event",
        "V1TopupFailedEventNotification",
    ),
    "v1.topup.reversed": (
        "stripe.events._v1_topup_reversed_event",
        "V1TopupReversedEventNotification",
    ),
    "v1.topup.succeeded": (
        "stripe.events._v1_topup_succeeded_event",
        "V1TopupSucceededEventNotification",
    ),
    "v1.transfer.created": (
        "stripe.events._v1_transfer_created_event",
        "V1TransferCreatedEventNotification",
    ),
    "v1.transfer.reversed": (
        "stripe.events._v1_transfer_reversed_event",
        "V1TransferReversedEventNotification",
    ),
    "v1.transfer.updated": (
        "stripe.events._v1_transfer_updated_event",
        "V1TransferUpdatedEventNotification",
    ),
    "v2.commerce.product_catalog.imports.failed": (
        "stripe.events._v2_commerce_product_catalog_imports_failed_event",
        "V2CommerceProductCatalogImportsFailedEventNotification",
    ),
    "v2.commerce.product_catalog.imports.processing": (
        "stripe.events._v2_commerce_product_catalog_imports_processing_event",
        "V2CommerceProductCatalogImportsProcessingEventNotification",
    ),
    "v2.commerce.product_catalog.imports.succeeded": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_event",
        "V2CommerceProductCatalogImportsSucceededEventNotification",
    ),
    "v2.commerce.product_catalog.imports.succeeded_with_errors": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event",
        "V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification",
    ),
    "v2.core.account.closed": (
        "stripe.events._v2_core_account_closed_event",
        "V2CoreAccountClosedEventNotification",
    ),
    "v2.core.account.created": (
        "stripe.events._v2_core_account_created_event",
        "V2CoreAccountCreatedEventNotification",
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
    "v2.core.event_destination.ping": (
        "stripe.events._v2_core_event_destination_ping_event",
        "V2CoreEventDestinationPingEventNotification",
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
    "V1AccountApplicationAuthorizedEventNotification",
    "V1AccountApplicationDeauthorizedEventNotification",
    "V1AccountExternalAccountCreatedEventNotification",
    "V1AccountExternalAccountDeletedEventNotification",
    "V1AccountExternalAccountUpdatedEventNotification",
    "V1AccountUpdatedEventNotification",
    "V1ApplicationFeeCreatedEventNotification",
    "V1ApplicationFeeRefundedEventNotification",
    "V1ApplicationFeeRefundUpdatedEventNotification",
    "V1BalanceAvailableEventNotification",
    "V1BalanceSettingsUpdatedEventNotification",
    "V1BillingAlertTriggeredEventNotification",
    "V1BillingCreditBalanceTransactionCreatedEventNotification",
    "V1BillingCreditGrantCreatedEventNotification",
    "V1BillingCreditGrantUpdatedEventNotification",
    "V1BillingMeterCreatedEventNotification",
    "V1BillingMeterDeactivatedEventNotification",
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V1BillingMeterReactivatedEventNotification",
    "V1BillingMeterUpdatedEventNotification",
    "V1BillingPortalConfigurationCreatedEventNotification",
    "V1BillingPortalConfigurationUpdatedEventNotification",
    "V1BillingPortalSessionCreatedEventNotification",
    "V1CapabilityUpdatedEventNotification",
    "V1CashBalanceFundsAvailableEventNotification",
    "V1ChargeCapturedEventNotification",
    "V1ChargeDisputeClosedEventNotification",
    "V1ChargeDisputeCreatedEventNotification",
    "V1ChargeDisputeFundsReinstatedEventNotification",
    "V1ChargeDisputeFundsWithdrawnEventNotification",
    "V1ChargeDisputeUpdatedEventNotification",
    "V1ChargeExpiredEventNotification",
    "V1ChargeFailedEventNotification",
    "V1ChargePendingEventNotification",
    "V1ChargeRefundedEventNotification",
    "V1ChargeRefundUpdatedEventNotification",
    "V1ChargeSucceededEventNotification",
    "V1ChargeUpdatedEventNotification",
    "V1CheckoutSessionAsyncPaymentFailedEventNotification",
    "V1CheckoutSessionAsyncPaymentSucceededEventNotification",
    "V1CheckoutSessionCompletedEventNotification",
    "V1CheckoutSessionExpiredEventNotification",
    "V1ClimateOrderCanceledEventNotification",
    "V1ClimateOrderCreatedEventNotification",
    "V1ClimateOrderDelayedEventNotification",
    "V1ClimateOrderDeliveredEventNotification",
    "V1ClimateOrderProductSubstitutedEventNotification",
    "V1ClimateProductCreatedEventNotification",
    "V1ClimateProductPricingUpdatedEventNotification",
    "V1CouponCreatedEventNotification",
    "V1CouponDeletedEventNotification",
    "V1CouponUpdatedEventNotification",
    "V1CreditNoteCreatedEventNotification",
    "V1CreditNoteUpdatedEventNotification",
    "V1CreditNoteVoidedEventNotification",
    "V1CustomerCashBalanceTransactionCreatedEventNotification",
    "V1CustomerCreatedEventNotification",
    "V1CustomerDeletedEventNotification",
    "V1CustomerDiscountCreatedEventNotification",
    "V1CustomerDiscountDeletedEventNotification",
    "V1CustomerDiscountUpdatedEventNotification",
    "V1CustomerSubscriptionCreatedEventNotification",
    "V1CustomerSubscriptionDeletedEventNotification",
    "V1CustomerSubscriptionPausedEventNotification",
    "V1CustomerSubscriptionPendingUpdateAppliedEventNotification",
    "V1CustomerSubscriptionPendingUpdateExpiredEventNotification",
    "V1CustomerSubscriptionResumedEventNotification",
    "V1CustomerSubscriptionTrialWillEndEventNotification",
    "V1CustomerSubscriptionUpdatedEventNotification",
    "V1CustomerTaxIdCreatedEventNotification",
    "V1CustomerTaxIdDeletedEventNotification",
    "V1CustomerTaxIdUpdatedEventNotification",
    "V1CustomerUpdatedEventNotification",
    "V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification",
    "V1FileCreatedEventNotification",
    "V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification",
    "V1FinancialConnectionsAccountCreatedEventNotification",
    "V1FinancialConnectionsAccountDeactivatedEventNotification",
    "V1FinancialConnectionsAccountDisconnectedEventNotification",
    "V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification",
    "V1FinancialConnectionsAccountReactivatedEventNotification",
    "V1FinancialConnectionsAccountRefreshedBalanceEventNotification",
    "V1FinancialConnectionsAccountRefreshedOwnershipEventNotification",
    "V1FinancialConnectionsAccountRefreshedTransactionsEventNotification",
    "V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification",
    "V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification",
    "V1FinancialConnectionsAccountUpcomingDeactivationEventNotification",
    "V1IdentityVerificationSessionCanceledEventNotification",
    "V1IdentityVerificationSessionCreatedEventNotification",
    "V1IdentityVerificationSessionProcessingEventNotification",
    "V1IdentityVerificationSessionRedactedEventNotification",
    "V1IdentityVerificationSessionRequiresInputEventNotification",
    "V1IdentityVerificationSessionVerifiedEventNotification",
    "V1InvoiceCreatedEventNotification",
    "V1InvoiceDeletedEventNotification",
    "V1InvoiceFinalizationFailedEventNotification",
    "V1InvoiceFinalizedEventNotification",
    "V1InvoiceitemCreatedEventNotification",
    "V1InvoiceitemDeletedEventNotification",
    "V1InvoiceMarkedUncollectibleEventNotification",
    "V1InvoiceOverdueEventNotification",
    "V1InvoiceOverpaidEventNotification",
    "V1InvoicePaidEventNotification",
    "V1InvoicePaymentActionRequiredEventNotification",
    "V1InvoicePaymentAttemptRequiredEventNotification",
    "V1InvoicePaymentFailedEventNotification",
    "V1InvoicePaymentPaidEventNotification",
    "V1InvoicePaymentSucceededEventNotification",
    "V1InvoiceSentEventNotification",
    "V1InvoiceUpcomingEventNotification",
    "V1InvoiceUpdatedEventNotification",
    "V1InvoiceVoidedEventNotification",
    "V1InvoiceWillBeDueEventNotification",
    "V1IssuingAuthorizationCreatedEventNotification",
    "V1IssuingAuthorizationRequestEventNotification",
    "V1IssuingAuthorizationUpdatedEventNotification",
    "V1IssuingCardCreatedEventNotification",
    "V1IssuingCardholderCreatedEventNotification",
    "V1IssuingCardholderUpdatedEventNotification",
    "V1IssuingCardUpdatedEventNotification",
    "V1IssuingDisputeClosedEventNotification",
    "V1IssuingDisputeCreatedEventNotification",
    "V1IssuingDisputeFundsReinstatedEventNotification",
    "V1IssuingDisputeFundsRescindedEventNotification",
    "V1IssuingDisputeSubmittedEventNotification",
    "V1IssuingDisputeUpdatedEventNotification",
    "V1IssuingPersonalizationDesignActivatedEventNotification",
    "V1IssuingPersonalizationDesignDeactivatedEventNotification",
    "V1IssuingPersonalizationDesignRejectedEventNotification",
    "V1IssuingPersonalizationDesignUpdatedEventNotification",
    "V1IssuingTokenCreatedEventNotification",
    "V1IssuingTokenUpdatedEventNotification",
    "V1IssuingTransactionCreatedEventNotification",
    "V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification",
    "V1IssuingTransactionUpdatedEventNotification",
    "V1MandateUpdatedEventNotification",
    "V1PaymentIntentAmountCapturableUpdatedEventNotification",
    "V1PaymentIntentCanceledEventNotification",
    "V1PaymentIntentCreatedEventNotification",
    "V1PaymentIntentPartiallyFundedEventNotification",
    "V1PaymentIntentPaymentFailedEventNotification",
    "V1PaymentIntentProcessingEventNotification",
    "V1PaymentIntentRequiresActionEventNotification",
    "V1PaymentIntentSucceededEventNotification",
    "V1PaymentLinkCreatedEventNotification",
    "V1PaymentLinkUpdatedEventNotification",
    "V1PaymentMethodAttachedEventNotification",
    "V1PaymentMethodAutomaticallyUpdatedEventNotification",
    "V1PaymentMethodDetachedEventNotification",
    "V1PaymentMethodUpdatedEventNotification",
    "V1PayoutCanceledEventNotification",
    "V1PayoutCreatedEventNotification",
    "V1PayoutFailedEventNotification",
    "V1PayoutPaidEventNotification",
    "V1PayoutReconciliationCompletedEventNotification",
    "V1PayoutUpdatedEventNotification",
    "V1PersonCreatedEventNotification",
    "V1PersonDeletedEventNotification",
    "V1PersonUpdatedEventNotification",
    "V1PlanCreatedEventNotification",
    "V1PlanDeletedEventNotification",
    "V1PlanUpdatedEventNotification",
    "V1PriceCreatedEventNotification",
    "V1PriceDeletedEventNotification",
    "V1PriceUpdatedEventNotification",
    "V1ProductCreatedEventNotification",
    "V1ProductDeletedEventNotification",
    "V1ProductUpdatedEventNotification",
    "V1PromotionCodeCreatedEventNotification",
    "V1PromotionCodeUpdatedEventNotification",
    "V1QuoteAcceptedEventNotification",
    "V1QuoteCanceledEventNotification",
    "V1QuoteCreatedEventNotification",
    "V1QuoteFinalizedEventNotification",
    "V1RadarEarlyFraudWarningCreatedEventNotification",
    "V1RadarEarlyFraudWarningUpdatedEventNotification",
    "V1RefundCreatedEventNotification",
    "V1RefundFailedEventNotification",
    "V1RefundUpdatedEventNotification",
    "V1ReviewClosedEventNotification",
    "V1ReviewOpenedEventNotification",
    "V1SetupIntentCanceledEventNotification",
    "V1SetupIntentCreatedEventNotification",
    "V1SetupIntentRequiresActionEventNotification",
    "V1SetupIntentSetupFailedEventNotification",
    "V1SetupIntentSucceededEventNotification",
    "V1SigmaScheduledQueryRunCreatedEventNotification",
    "V1SourceCanceledEventNotification",
    "V1SourceChargeableEventNotification",
    "V1SourceFailedEventNotification",
    "V1SourceRefundAttributesRequiredEventNotification",
    "V1SubscriptionScheduleAbortedEventNotification",
    "V1SubscriptionScheduleCanceledEventNotification",
    "V1SubscriptionScheduleCompletedEventNotification",
    "V1SubscriptionScheduleCreatedEventNotification",
    "V1SubscriptionScheduleExpiringEventNotification",
    "V1SubscriptionScheduleReleasedEventNotification",
    "V1SubscriptionScheduleUpdatedEventNotification",
    "V1TaxRateCreatedEventNotification",
    "V1TaxRateUpdatedEventNotification",
    "V1TaxSettingsUpdatedEventNotification",
    "V1TerminalReaderActionFailedEventNotification",
    "V1TerminalReaderActionSucceededEventNotification",
    "V1TerminalReaderActionUpdatedEventNotification",
    "V1TestHelpersTestClockAdvancingEventNotification",
    "V1TestHelpersTestClockCreatedEventNotification",
    "V1TestHelpersTestClockDeletedEventNotification",
    "V1TestHelpersTestClockInternalFailureEventNotification",
    "V1TestHelpersTestClockReadyEventNotification",
    "V1TopupCanceledEventNotification",
    "V1TopupCreatedEventNotification",
    "V1TopupFailedEventNotification",
    "V1TopupReversedEventNotification",
    "V1TopupSucceededEventNotification",
    "V1TransferCreatedEventNotification",
    "V1TransferReversedEventNotification",
    "V1TransferUpdatedEventNotification",
    "V2CommerceProductCatalogImportsFailedEventNotification",
    "V2CommerceProductCatalogImportsProcessingEventNotification",
    "V2CommerceProductCatalogImportsSucceededEventNotification",
    "V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification",
    "V2CoreAccountClosedEventNotification",
    "V2CoreAccountCreatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification",
    "V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification",
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification",
    "V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification",
    "V2CoreAccountIncludingIdentityUpdatedEventNotification",
    "V2CoreAccountIncludingRequirementsUpdatedEventNotification",
    "V2CoreAccountLinkReturnedEventNotification",
    "V2CoreAccountPersonCreatedEventNotification",
    "V2CoreAccountPersonDeletedEventNotification",
    "V2CoreAccountPersonUpdatedEventNotification",
    "V2CoreAccountUpdatedEventNotification",
    "V2CoreEventDestinationPingEventNotification",
]
