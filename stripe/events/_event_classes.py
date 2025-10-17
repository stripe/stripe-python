# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing import Union
from typing_extensions import TYPE_CHECKING
from stripe.v2.core._event import UnknownEventNotification
from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe.events._v1_account_updated_event import (
        V1AccountUpdatedEventNotification,
    )
    from stripe.events._v1_application_fee_created_event import (
        V1ApplicationFeeCreatedEventNotification,
    )
    from stripe.events._v1_application_fee_refunded_event import (
        V1ApplicationFeeRefundedEventNotification,
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
    from stripe.events._v1_capability_updated_event import (
        V1CapabilityUpdatedEventNotification,
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
    from stripe.events._v1_charge_refund_updated_event import (
        V1ChargeRefundUpdatedEventNotification,
    )
    from stripe.events._v1_charge_refunded_event import (
        V1ChargeRefundedEventNotification,
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
    from stripe.events._v1_invoice_payment_paid_event import (
        V1InvoicePaymentPaidEventNotification,
    )
    from stripe.events._v1_invoiceitem_created_event import (
        V1InvoiceitemCreatedEventNotification,
    )
    from stripe.events._v1_invoiceitem_deleted_event import (
        V1InvoiceitemDeletedEventNotification,
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
    from stripe.events._v1_issuing_card_updated_event import (
        V1IssuingCardUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_created_event import (
        V1IssuingCardholderCreatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_updated_event import (
        V1IssuingCardholderUpdatedEventNotification,
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
    from stripe.events._v2_billing_license_fee_created_event import (
        V2BillingLicenseFeeCreatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_updated_event import (
        V2BillingLicenseFeeUpdatedEventNotification,
    )
    from stripe.events._v2_billing_license_fee_version_created_event import (
        V2BillingLicenseFeeVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_created_event import (
        V2BillingLicensedItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_licensed_item_updated_event import (
        V2BillingLicensedItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_created_event import (
        V2BillingMeteredItemCreatedEventNotification,
    )
    from stripe.events._v2_billing_metered_item_updated_event import (
        V2BillingMeteredItemUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_created_event import (
        V2BillingPricingPlanCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_updated_event import (
        V2BillingPricingPlanUpdatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_created_event import (
        V2BillingPricingPlanComponentCreatedEventNotification,
    )
    from stripe.events._v2_billing_pricing_plan_component_updated_event import (
        V2BillingPricingPlanComponentUpdatedEventNotification,
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
    from stripe.events._v2_billing_pricing_plan_version_created_event import (
        V2BillingPricingPlanVersionCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_created_event import (
        V2BillingRateCardCreatedEventNotification,
    )
    from stripe.events._v2_billing_rate_card_updated_event import (
        V2BillingRateCardUpdatedEventNotification,
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
    from stripe.events._v2_billing_rate_card_version_created_event import (
        V2BillingRateCardVersionCreatedEventNotification,
    )
    from stripe.events._v2_core_account_closed_event import (
        V2CoreAccountClosedEventNotification,
    )
    from stripe.events._v2_core_account_created_event import (
        V2CoreAccountCreatedEventNotification,
    )
    from stripe.events._v2_core_account_updated_event import (
        V2CoreAccountUpdatedEventNotification,
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


_V2_EVENT_CLASS_LOOKUP = {
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
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEvent",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEvent",
    ),
    "v1.billing_portal.configuration.created": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        "V1BillingPortalConfigurationCreatedEvent",
    ),
    "v1.billing_portal.configuration.updated": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        "V1BillingPortalConfigurationUpdatedEvent",
    ),
    "v1.capability.updated": (
        "stripe.events._v1_capability_updated_event",
        "V1CapabilityUpdatedEvent",
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
    "v1.customer.created": (
        "stripe.events._v1_customer_created_event",
        "V1CustomerCreatedEvent",
    ),
    "v1.customer.deleted": (
        "stripe.events._v1_customer_deleted_event",
        "V1CustomerDeletedEvent",
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
    "v1.file.created": (
        "stripe.events._v1_file_created_event",
        "V1FileCreatedEvent",
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
    "v1.billing.meter.error_report_triggered": (
        "stripe.events._v1_billing_meter_error_report_triggered_event",
        "V1BillingMeterErrorReportTriggeredEventNotification",
    ),
    "v1.billing.meter.no_meter_found": (
        "stripe.events._v1_billing_meter_no_meter_found_event",
        "V1BillingMeterNoMeterFoundEventNotification",
    ),
    "v1.billing_portal.configuration.created": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        "V1BillingPortalConfigurationCreatedEventNotification",
    ),
    "v1.billing_portal.configuration.updated": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        "V1BillingPortalConfigurationUpdatedEventNotification",
    ),
    "v1.capability.updated": (
        "stripe.events._v1_capability_updated_event",
        "V1CapabilityUpdatedEventNotification",
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
    "v1.customer.created": (
        "stripe.events._v1_customer_created_event",
        "V1CustomerCreatedEventNotification",
    ),
    "v1.customer.deleted": (
        "stripe.events._v1_customer_deleted_event",
        "V1CustomerDeletedEventNotification",
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
    "v1.file.created": (
        "stripe.events._v1_file_created_event",
        "V1FileCreatedEventNotification",
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
    "V1AccountUpdatedEventNotification",
    "V1ApplicationFeeCreatedEventNotification",
    "V1ApplicationFeeRefundedEventNotification",
    "V1BillingMeterErrorReportTriggeredEventNotification",
    "V1BillingMeterNoMeterFoundEventNotification",
    "V1BillingPortalConfigurationCreatedEventNotification",
    "V1BillingPortalConfigurationUpdatedEventNotification",
    "V1CapabilityUpdatedEventNotification",
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
    "V1CustomerCreatedEventNotification",
    "V1CustomerDeletedEventNotification",
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
    "V1FileCreatedEventNotification",
    "V1FinancialConnectionsAccountCreatedEventNotification",
    "V1FinancialConnectionsAccountDeactivatedEventNotification",
    "V1FinancialConnectionsAccountDisconnectedEventNotification",
    "V1FinancialConnectionsAccountReactivatedEventNotification",
    "V1FinancialConnectionsAccountRefreshedBalanceEventNotification",
    "V1FinancialConnectionsAccountRefreshedOwnershipEventNotification",
    "V1FinancialConnectionsAccountRefreshedTransactionsEventNotification",
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
    "V2CoreHealthTrafficVolumeDropFiringEventNotification",
    "V2CoreHealthTrafficVolumeDropResolvedEventNotification",
    "V2CoreHealthWebhookLatencyFiringEventNotification",
    "V2CoreHealthWebhookLatencyResolvedEventNotification",
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
    "V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification",
    "V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification",
    "V2PaymentsOffSessionPaymentCanceledEventNotification",
    "V2PaymentsOffSessionPaymentCreatedEventNotification",
    "V2PaymentsOffSessionPaymentFailedEventNotification",
    "V2PaymentsOffSessionPaymentRequiresCaptureEventNotification",
    "V2PaymentsOffSessionPaymentSucceededEventNotification",
]
