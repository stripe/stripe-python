# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from stripe.events._v1_account_updated_event import (
    V1AccountUpdatedEvent,
    V1AccountUpdatedEventNotification,
)
from stripe.events._v1_application_fee_created_event import (
    V1ApplicationFeeCreatedEvent,
    V1ApplicationFeeCreatedEventNotification,
)
from stripe.events._v1_application_fee_refunded_event import (
    V1ApplicationFeeRefundedEvent,
    V1ApplicationFeeRefundedEventNotification,
)
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterErrorReportTriggeredEventNotification,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
    V1BillingMeterNoMeterFoundEventNotification,
)
from stripe.events._v1_billing_portal_configuration_created_event import (
    V1BillingPortalConfigurationCreatedEvent,
    V1BillingPortalConfigurationCreatedEventNotification,
)
from stripe.events._v1_billing_portal_configuration_updated_event import (
    V1BillingPortalConfigurationUpdatedEvent,
    V1BillingPortalConfigurationUpdatedEventNotification,
)
from stripe.events._v1_capability_updated_event import (
    V1CapabilityUpdatedEvent,
    V1CapabilityUpdatedEventNotification,
)
from stripe.events._v1_charge_captured_event import (
    V1ChargeCapturedEvent,
    V1ChargeCapturedEventNotification,
)
from stripe.events._v1_charge_dispute_closed_event import (
    V1ChargeDisputeClosedEvent,
    V1ChargeDisputeClosedEventNotification,
)
from stripe.events._v1_charge_dispute_created_event import (
    V1ChargeDisputeCreatedEvent,
    V1ChargeDisputeCreatedEventNotification,
)
from stripe.events._v1_charge_dispute_funds_reinstated_event import (
    V1ChargeDisputeFundsReinstatedEvent,
    V1ChargeDisputeFundsReinstatedEventNotification,
)
from stripe.events._v1_charge_dispute_funds_withdrawn_event import (
    V1ChargeDisputeFundsWithdrawnEvent,
    V1ChargeDisputeFundsWithdrawnEventNotification,
)
from stripe.events._v1_charge_dispute_updated_event import (
    V1ChargeDisputeUpdatedEvent,
    V1ChargeDisputeUpdatedEventNotification,
)
from stripe.events._v1_charge_expired_event import (
    V1ChargeExpiredEvent,
    V1ChargeExpiredEventNotification,
)
from stripe.events._v1_charge_failed_event import (
    V1ChargeFailedEvent,
    V1ChargeFailedEventNotification,
)
from stripe.events._v1_charge_pending_event import (
    V1ChargePendingEvent,
    V1ChargePendingEventNotification,
)
from stripe.events._v1_charge_refund_updated_event import (
    V1ChargeRefundUpdatedEvent,
    V1ChargeRefundUpdatedEventNotification,
)
from stripe.events._v1_charge_refunded_event import (
    V1ChargeRefundedEvent,
    V1ChargeRefundedEventNotification,
)
from stripe.events._v1_charge_succeeded_event import (
    V1ChargeSucceededEvent,
    V1ChargeSucceededEventNotification,
)
from stripe.events._v1_charge_updated_event import (
    V1ChargeUpdatedEvent,
    V1ChargeUpdatedEventNotification,
)
from stripe.events._v1_checkout_session_async_payment_failed_event import (
    V1CheckoutSessionAsyncPaymentFailedEvent,
    V1CheckoutSessionAsyncPaymentFailedEventNotification,
)
from stripe.events._v1_checkout_session_async_payment_succeeded_event import (
    V1CheckoutSessionAsyncPaymentSucceededEvent,
    V1CheckoutSessionAsyncPaymentSucceededEventNotification,
)
from stripe.events._v1_checkout_session_completed_event import (
    V1CheckoutSessionCompletedEvent,
    V1CheckoutSessionCompletedEventNotification,
)
from stripe.events._v1_checkout_session_expired_event import (
    V1CheckoutSessionExpiredEvent,
    V1CheckoutSessionExpiredEventNotification,
)
from stripe.events._v1_climate_order_canceled_event import (
    V1ClimateOrderCanceledEvent,
    V1ClimateOrderCanceledEventNotification,
)
from stripe.events._v1_climate_order_created_event import (
    V1ClimateOrderCreatedEvent,
    V1ClimateOrderCreatedEventNotification,
)
from stripe.events._v1_climate_order_delayed_event import (
    V1ClimateOrderDelayedEvent,
    V1ClimateOrderDelayedEventNotification,
)
from stripe.events._v1_climate_order_delivered_event import (
    V1ClimateOrderDeliveredEvent,
    V1ClimateOrderDeliveredEventNotification,
)
from stripe.events._v1_climate_order_product_substituted_event import (
    V1ClimateOrderProductSubstitutedEvent,
    V1ClimateOrderProductSubstitutedEventNotification,
)
from stripe.events._v1_climate_product_created_event import (
    V1ClimateProductCreatedEvent,
    V1ClimateProductCreatedEventNotification,
)
from stripe.events._v1_climate_product_pricing_updated_event import (
    V1ClimateProductPricingUpdatedEvent,
    V1ClimateProductPricingUpdatedEventNotification,
)
from stripe.events._v1_coupon_created_event import (
    V1CouponCreatedEvent,
    V1CouponCreatedEventNotification,
)
from stripe.events._v1_coupon_deleted_event import (
    V1CouponDeletedEvent,
    V1CouponDeletedEventNotification,
)
from stripe.events._v1_coupon_updated_event import (
    V1CouponUpdatedEvent,
    V1CouponUpdatedEventNotification,
)
from stripe.events._v1_credit_note_created_event import (
    V1CreditNoteCreatedEvent,
    V1CreditNoteCreatedEventNotification,
)
from stripe.events._v1_credit_note_updated_event import (
    V1CreditNoteUpdatedEvent,
    V1CreditNoteUpdatedEventNotification,
)
from stripe.events._v1_credit_note_voided_event import (
    V1CreditNoteVoidedEvent,
    V1CreditNoteVoidedEventNotification,
)
from stripe.events._v1_customer_created_event import (
    V1CustomerCreatedEvent,
    V1CustomerCreatedEventNotification,
)
from stripe.events._v1_customer_deleted_event import (
    V1CustomerDeletedEvent,
    V1CustomerDeletedEventNotification,
)
from stripe.events._v1_customer_subscription_created_event import (
    V1CustomerSubscriptionCreatedEvent,
    V1CustomerSubscriptionCreatedEventNotification,
)
from stripe.events._v1_customer_subscription_deleted_event import (
    V1CustomerSubscriptionDeletedEvent,
    V1CustomerSubscriptionDeletedEventNotification,
)
from stripe.events._v1_customer_subscription_paused_event import (
    V1CustomerSubscriptionPausedEvent,
    V1CustomerSubscriptionPausedEventNotification,
)
from stripe.events._v1_customer_subscription_pending_update_applied_event import (
    V1CustomerSubscriptionPendingUpdateAppliedEvent,
    V1CustomerSubscriptionPendingUpdateAppliedEventNotification,
)
from stripe.events._v1_customer_subscription_pending_update_expired_event import (
    V1CustomerSubscriptionPendingUpdateExpiredEvent,
    V1CustomerSubscriptionPendingUpdateExpiredEventNotification,
)
from stripe.events._v1_customer_subscription_resumed_event import (
    V1CustomerSubscriptionResumedEvent,
    V1CustomerSubscriptionResumedEventNotification,
)
from stripe.events._v1_customer_subscription_trial_will_end_event import (
    V1CustomerSubscriptionTrialWillEndEvent,
    V1CustomerSubscriptionTrialWillEndEventNotification,
)
from stripe.events._v1_customer_subscription_updated_event import (
    V1CustomerSubscriptionUpdatedEvent,
    V1CustomerSubscriptionUpdatedEventNotification,
)
from stripe.events._v1_customer_tax_id_created_event import (
    V1CustomerTaxIdCreatedEvent,
    V1CustomerTaxIdCreatedEventNotification,
)
from stripe.events._v1_customer_tax_id_deleted_event import (
    V1CustomerTaxIdDeletedEvent,
    V1CustomerTaxIdDeletedEventNotification,
)
from stripe.events._v1_customer_tax_id_updated_event import (
    V1CustomerTaxIdUpdatedEvent,
    V1CustomerTaxIdUpdatedEventNotification,
)
from stripe.events._v1_customer_updated_event import (
    V1CustomerUpdatedEvent,
    V1CustomerUpdatedEventNotification,
)
from stripe.events._v1_file_created_event import (
    V1FileCreatedEvent,
    V1FileCreatedEventNotification,
)
from stripe.events._v1_financial_connections_account_created_event import (
    V1FinancialConnectionsAccountCreatedEvent,
    V1FinancialConnectionsAccountCreatedEventNotification,
)
from stripe.events._v1_financial_connections_account_deactivated_event import (
    V1FinancialConnectionsAccountDeactivatedEvent,
    V1FinancialConnectionsAccountDeactivatedEventNotification,
)
from stripe.events._v1_financial_connections_account_disconnected_event import (
    V1FinancialConnectionsAccountDisconnectedEvent,
    V1FinancialConnectionsAccountDisconnectedEventNotification,
)
from stripe.events._v1_financial_connections_account_reactivated_event import (
    V1FinancialConnectionsAccountReactivatedEvent,
    V1FinancialConnectionsAccountReactivatedEventNotification,
)
from stripe.events._v1_financial_connections_account_refreshed_balance_event import (
    V1FinancialConnectionsAccountRefreshedBalanceEvent,
    V1FinancialConnectionsAccountRefreshedBalanceEventNotification,
)
from stripe.events._v1_financial_connections_account_refreshed_ownership_event import (
    V1FinancialConnectionsAccountRefreshedOwnershipEvent,
    V1FinancialConnectionsAccountRefreshedOwnershipEventNotification,
)
from stripe.events._v1_financial_connections_account_refreshed_transactions_event import (
    V1FinancialConnectionsAccountRefreshedTransactionsEvent,
    V1FinancialConnectionsAccountRefreshedTransactionsEventNotification,
)
from stripe.events._v1_identity_verification_session_canceled_event import (
    V1IdentityVerificationSessionCanceledEvent,
    V1IdentityVerificationSessionCanceledEventNotification,
)
from stripe.events._v1_identity_verification_session_created_event import (
    V1IdentityVerificationSessionCreatedEvent,
    V1IdentityVerificationSessionCreatedEventNotification,
)
from stripe.events._v1_identity_verification_session_processing_event import (
    V1IdentityVerificationSessionProcessingEvent,
    V1IdentityVerificationSessionProcessingEventNotification,
)
from stripe.events._v1_identity_verification_session_redacted_event import (
    V1IdentityVerificationSessionRedactedEvent,
    V1IdentityVerificationSessionRedactedEventNotification,
)
from stripe.events._v1_identity_verification_session_requires_input_event import (
    V1IdentityVerificationSessionRequiresInputEvent,
    V1IdentityVerificationSessionRequiresInputEventNotification,
)
from stripe.events._v1_identity_verification_session_verified_event import (
    V1IdentityVerificationSessionVerifiedEvent,
    V1IdentityVerificationSessionVerifiedEventNotification,
)
from stripe.events._v1_invoice_created_event import (
    V1InvoiceCreatedEvent,
    V1InvoiceCreatedEventNotification,
)
from stripe.events._v1_invoice_deleted_event import (
    V1InvoiceDeletedEvent,
    V1InvoiceDeletedEventNotification,
)
from stripe.events._v1_invoice_finalization_failed_event import (
    V1InvoiceFinalizationFailedEvent,
    V1InvoiceFinalizationFailedEventNotification,
)
from stripe.events._v1_invoice_finalized_event import (
    V1InvoiceFinalizedEvent,
    V1InvoiceFinalizedEventNotification,
)
from stripe.events._v1_invoice_marked_uncollectible_event import (
    V1InvoiceMarkedUncollectibleEvent,
    V1InvoiceMarkedUncollectibleEventNotification,
)
from stripe.events._v1_invoice_overdue_event import (
    V1InvoiceOverdueEvent,
    V1InvoiceOverdueEventNotification,
)
from stripe.events._v1_invoice_overpaid_event import (
    V1InvoiceOverpaidEvent,
    V1InvoiceOverpaidEventNotification,
)
from stripe.events._v1_invoice_paid_event import (
    V1InvoicePaidEvent,
    V1InvoicePaidEventNotification,
)
from stripe.events._v1_invoice_payment_action_required_event import (
    V1InvoicePaymentActionRequiredEvent,
    V1InvoicePaymentActionRequiredEventNotification,
)
from stripe.events._v1_invoice_payment_failed_event import (
    V1InvoicePaymentFailedEvent,
    V1InvoicePaymentFailedEventNotification,
)
from stripe.events._v1_invoice_payment_succeeded_event import (
    V1InvoicePaymentSucceededEvent,
    V1InvoicePaymentSucceededEventNotification,
)
from stripe.events._v1_invoice_sent_event import (
    V1InvoiceSentEvent,
    V1InvoiceSentEventNotification,
)
from stripe.events._v1_invoice_upcoming_event import (
    V1InvoiceUpcomingEvent,
    V1InvoiceUpcomingEventNotification,
)
from stripe.events._v1_invoice_updated_event import (
    V1InvoiceUpdatedEvent,
    V1InvoiceUpdatedEventNotification,
)
from stripe.events._v1_invoice_voided_event import (
    V1InvoiceVoidedEvent,
    V1InvoiceVoidedEventNotification,
)
from stripe.events._v1_invoice_will_be_due_event import (
    V1InvoiceWillBeDueEvent,
    V1InvoiceWillBeDueEventNotification,
)
from stripe.events._v1_invoice_payment_paid_event import (
    V1InvoicePaymentPaidEvent,
    V1InvoicePaymentPaidEventNotification,
)
from stripe.events._v1_invoiceitem_created_event import (
    V1InvoiceitemCreatedEvent,
    V1InvoiceitemCreatedEventNotification,
)
from stripe.events._v1_invoiceitem_deleted_event import (
    V1InvoiceitemDeletedEvent,
    V1InvoiceitemDeletedEventNotification,
)
from stripe.events._v1_issuing_authorization_created_event import (
    V1IssuingAuthorizationCreatedEvent,
    V1IssuingAuthorizationCreatedEventNotification,
)
from stripe.events._v1_issuing_authorization_request_event import (
    V1IssuingAuthorizationRequestEvent,
    V1IssuingAuthorizationRequestEventNotification,
)
from stripe.events._v1_issuing_authorization_updated_event import (
    V1IssuingAuthorizationUpdatedEvent,
    V1IssuingAuthorizationUpdatedEventNotification,
)
from stripe.events._v1_issuing_card_created_event import (
    V1IssuingCardCreatedEvent,
    V1IssuingCardCreatedEventNotification,
)
from stripe.events._v1_issuing_card_updated_event import (
    V1IssuingCardUpdatedEvent,
    V1IssuingCardUpdatedEventNotification,
)
from stripe.events._v1_issuing_cardholder_created_event import (
    V1IssuingCardholderCreatedEvent,
    V1IssuingCardholderCreatedEventNotification,
)
from stripe.events._v1_issuing_cardholder_updated_event import (
    V1IssuingCardholderUpdatedEvent,
    V1IssuingCardholderUpdatedEventNotification,
)
from stripe.events._v1_issuing_dispute_closed_event import (
    V1IssuingDisputeClosedEvent,
    V1IssuingDisputeClosedEventNotification,
)
from stripe.events._v1_issuing_dispute_created_event import (
    V1IssuingDisputeCreatedEvent,
    V1IssuingDisputeCreatedEventNotification,
)
from stripe.events._v1_issuing_dispute_funds_reinstated_event import (
    V1IssuingDisputeFundsReinstatedEvent,
    V1IssuingDisputeFundsReinstatedEventNotification,
)
from stripe.events._v1_issuing_dispute_funds_rescinded_event import (
    V1IssuingDisputeFundsRescindedEvent,
    V1IssuingDisputeFundsRescindedEventNotification,
)
from stripe.events._v1_issuing_dispute_submitted_event import (
    V1IssuingDisputeSubmittedEvent,
    V1IssuingDisputeSubmittedEventNotification,
)
from stripe.events._v1_issuing_dispute_updated_event import (
    V1IssuingDisputeUpdatedEvent,
    V1IssuingDisputeUpdatedEventNotification,
)
from stripe.events._v1_issuing_personalization_design_activated_event import (
    V1IssuingPersonalizationDesignActivatedEvent,
    V1IssuingPersonalizationDesignActivatedEventNotification,
)
from stripe.events._v1_issuing_personalization_design_deactivated_event import (
    V1IssuingPersonalizationDesignDeactivatedEvent,
    V1IssuingPersonalizationDesignDeactivatedEventNotification,
)
from stripe.events._v1_issuing_personalization_design_rejected_event import (
    V1IssuingPersonalizationDesignRejectedEvent,
    V1IssuingPersonalizationDesignRejectedEventNotification,
)
from stripe.events._v1_issuing_personalization_design_updated_event import (
    V1IssuingPersonalizationDesignUpdatedEvent,
    V1IssuingPersonalizationDesignUpdatedEventNotification,
)
from stripe.events._v1_issuing_token_created_event import (
    V1IssuingTokenCreatedEvent,
    V1IssuingTokenCreatedEventNotification,
)
from stripe.events._v1_issuing_token_updated_event import (
    V1IssuingTokenUpdatedEvent,
    V1IssuingTokenUpdatedEventNotification,
)
from stripe.events._v1_issuing_transaction_created_event import (
    V1IssuingTransactionCreatedEvent,
    V1IssuingTransactionCreatedEventNotification,
)
from stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event import (
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent,
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification,
)
from stripe.events._v1_issuing_transaction_updated_event import (
    V1IssuingTransactionUpdatedEvent,
    V1IssuingTransactionUpdatedEventNotification,
)
from stripe.events._v1_mandate_updated_event import (
    V1MandateUpdatedEvent,
    V1MandateUpdatedEventNotification,
)
from stripe.events._v1_payment_intent_amount_capturable_updated_event import (
    V1PaymentIntentAmountCapturableUpdatedEvent,
    V1PaymentIntentAmountCapturableUpdatedEventNotification,
)
from stripe.events._v1_payment_intent_canceled_event import (
    V1PaymentIntentCanceledEvent,
    V1PaymentIntentCanceledEventNotification,
)
from stripe.events._v1_payment_intent_created_event import (
    V1PaymentIntentCreatedEvent,
    V1PaymentIntentCreatedEventNotification,
)
from stripe.events._v1_payment_intent_partially_funded_event import (
    V1PaymentIntentPartiallyFundedEvent,
    V1PaymentIntentPartiallyFundedEventNotification,
)
from stripe.events._v1_payment_intent_payment_failed_event import (
    V1PaymentIntentPaymentFailedEvent,
    V1PaymentIntentPaymentFailedEventNotification,
)
from stripe.events._v1_payment_intent_processing_event import (
    V1PaymentIntentProcessingEvent,
    V1PaymentIntentProcessingEventNotification,
)
from stripe.events._v1_payment_intent_requires_action_event import (
    V1PaymentIntentRequiresActionEvent,
    V1PaymentIntentRequiresActionEventNotification,
)
from stripe.events._v1_payment_intent_succeeded_event import (
    V1PaymentIntentSucceededEvent,
    V1PaymentIntentSucceededEventNotification,
)
from stripe.events._v1_payment_link_created_event import (
    V1PaymentLinkCreatedEvent,
    V1PaymentLinkCreatedEventNotification,
)
from stripe.events._v1_payment_link_updated_event import (
    V1PaymentLinkUpdatedEvent,
    V1PaymentLinkUpdatedEventNotification,
)
from stripe.events._v1_payment_method_attached_event import (
    V1PaymentMethodAttachedEvent,
    V1PaymentMethodAttachedEventNotification,
)
from stripe.events._v1_payment_method_automatically_updated_event import (
    V1PaymentMethodAutomaticallyUpdatedEvent,
    V1PaymentMethodAutomaticallyUpdatedEventNotification,
)
from stripe.events._v1_payment_method_detached_event import (
    V1PaymentMethodDetachedEvent,
    V1PaymentMethodDetachedEventNotification,
)
from stripe.events._v1_payment_method_updated_event import (
    V1PaymentMethodUpdatedEvent,
    V1PaymentMethodUpdatedEventNotification,
)
from stripe.events._v1_payout_canceled_event import (
    V1PayoutCanceledEvent,
    V1PayoutCanceledEventNotification,
)
from stripe.events._v1_payout_created_event import (
    V1PayoutCreatedEvent,
    V1PayoutCreatedEventNotification,
)
from stripe.events._v1_payout_failed_event import (
    V1PayoutFailedEvent,
    V1PayoutFailedEventNotification,
)
from stripe.events._v1_payout_paid_event import (
    V1PayoutPaidEvent,
    V1PayoutPaidEventNotification,
)
from stripe.events._v1_payout_reconciliation_completed_event import (
    V1PayoutReconciliationCompletedEvent,
    V1PayoutReconciliationCompletedEventNotification,
)
from stripe.events._v1_payout_updated_event import (
    V1PayoutUpdatedEvent,
    V1PayoutUpdatedEventNotification,
)
from stripe.events._v1_person_created_event import (
    V1PersonCreatedEvent,
    V1PersonCreatedEventNotification,
)
from stripe.events._v1_person_deleted_event import (
    V1PersonDeletedEvent,
    V1PersonDeletedEventNotification,
)
from stripe.events._v1_person_updated_event import (
    V1PersonUpdatedEvent,
    V1PersonUpdatedEventNotification,
)
from stripe.events._v1_plan_created_event import (
    V1PlanCreatedEvent,
    V1PlanCreatedEventNotification,
)
from stripe.events._v1_plan_deleted_event import (
    V1PlanDeletedEvent,
    V1PlanDeletedEventNotification,
)
from stripe.events._v1_plan_updated_event import (
    V1PlanUpdatedEvent,
    V1PlanUpdatedEventNotification,
)
from stripe.events._v1_price_created_event import (
    V1PriceCreatedEvent,
    V1PriceCreatedEventNotification,
)
from stripe.events._v1_price_deleted_event import (
    V1PriceDeletedEvent,
    V1PriceDeletedEventNotification,
)
from stripe.events._v1_price_updated_event import (
    V1PriceUpdatedEvent,
    V1PriceUpdatedEventNotification,
)
from stripe.events._v1_product_created_event import (
    V1ProductCreatedEvent,
    V1ProductCreatedEventNotification,
)
from stripe.events._v1_product_deleted_event import (
    V1ProductDeletedEvent,
    V1ProductDeletedEventNotification,
)
from stripe.events._v1_product_updated_event import (
    V1ProductUpdatedEvent,
    V1ProductUpdatedEventNotification,
)
from stripe.events._v1_promotion_code_created_event import (
    V1PromotionCodeCreatedEvent,
    V1PromotionCodeCreatedEventNotification,
)
from stripe.events._v1_promotion_code_updated_event import (
    V1PromotionCodeUpdatedEvent,
    V1PromotionCodeUpdatedEventNotification,
)
from stripe.events._v1_quote_accepted_event import (
    V1QuoteAcceptedEvent,
    V1QuoteAcceptedEventNotification,
)
from stripe.events._v1_quote_canceled_event import (
    V1QuoteCanceledEvent,
    V1QuoteCanceledEventNotification,
)
from stripe.events._v1_quote_created_event import (
    V1QuoteCreatedEvent,
    V1QuoteCreatedEventNotification,
)
from stripe.events._v1_quote_finalized_event import (
    V1QuoteFinalizedEvent,
    V1QuoteFinalizedEventNotification,
)
from stripe.events._v1_radar_early_fraud_warning_created_event import (
    V1RadarEarlyFraudWarningCreatedEvent,
    V1RadarEarlyFraudWarningCreatedEventNotification,
)
from stripe.events._v1_radar_early_fraud_warning_updated_event import (
    V1RadarEarlyFraudWarningUpdatedEvent,
    V1RadarEarlyFraudWarningUpdatedEventNotification,
)
from stripe.events._v1_refund_created_event import (
    V1RefundCreatedEvent,
    V1RefundCreatedEventNotification,
)
from stripe.events._v1_refund_failed_event import (
    V1RefundFailedEvent,
    V1RefundFailedEventNotification,
)
from stripe.events._v1_refund_updated_event import (
    V1RefundUpdatedEvent,
    V1RefundUpdatedEventNotification,
)
from stripe.events._v1_review_closed_event import (
    V1ReviewClosedEvent,
    V1ReviewClosedEventNotification,
)
from stripe.events._v1_review_opened_event import (
    V1ReviewOpenedEvent,
    V1ReviewOpenedEventNotification,
)
from stripe.events._v1_setup_intent_canceled_event import (
    V1SetupIntentCanceledEvent,
    V1SetupIntentCanceledEventNotification,
)
from stripe.events._v1_setup_intent_created_event import (
    V1SetupIntentCreatedEvent,
    V1SetupIntentCreatedEventNotification,
)
from stripe.events._v1_setup_intent_requires_action_event import (
    V1SetupIntentRequiresActionEvent,
    V1SetupIntentRequiresActionEventNotification,
)
from stripe.events._v1_setup_intent_setup_failed_event import (
    V1SetupIntentSetupFailedEvent,
    V1SetupIntentSetupFailedEventNotification,
)
from stripe.events._v1_setup_intent_succeeded_event import (
    V1SetupIntentSucceededEvent,
    V1SetupIntentSucceededEventNotification,
)
from stripe.events._v1_sigma_scheduled_query_run_created_event import (
    V1SigmaScheduledQueryRunCreatedEvent,
    V1SigmaScheduledQueryRunCreatedEventNotification,
)
from stripe.events._v1_source_canceled_event import (
    V1SourceCanceledEvent,
    V1SourceCanceledEventNotification,
)
from stripe.events._v1_source_chargeable_event import (
    V1SourceChargeableEvent,
    V1SourceChargeableEventNotification,
)
from stripe.events._v1_source_failed_event import (
    V1SourceFailedEvent,
    V1SourceFailedEventNotification,
)
from stripe.events._v1_source_refund_attributes_required_event import (
    V1SourceRefundAttributesRequiredEvent,
    V1SourceRefundAttributesRequiredEventNotification,
)
from stripe.events._v1_subscription_schedule_aborted_event import (
    V1SubscriptionScheduleAbortedEvent,
    V1SubscriptionScheduleAbortedEventNotification,
)
from stripe.events._v1_subscription_schedule_canceled_event import (
    V1SubscriptionScheduleCanceledEvent,
    V1SubscriptionScheduleCanceledEventNotification,
)
from stripe.events._v1_subscription_schedule_completed_event import (
    V1SubscriptionScheduleCompletedEvent,
    V1SubscriptionScheduleCompletedEventNotification,
)
from stripe.events._v1_subscription_schedule_created_event import (
    V1SubscriptionScheduleCreatedEvent,
    V1SubscriptionScheduleCreatedEventNotification,
)
from stripe.events._v1_subscription_schedule_expiring_event import (
    V1SubscriptionScheduleExpiringEvent,
    V1SubscriptionScheduleExpiringEventNotification,
)
from stripe.events._v1_subscription_schedule_released_event import (
    V1SubscriptionScheduleReleasedEvent,
    V1SubscriptionScheduleReleasedEventNotification,
)
from stripe.events._v1_subscription_schedule_updated_event import (
    V1SubscriptionScheduleUpdatedEvent,
    V1SubscriptionScheduleUpdatedEventNotification,
)
from stripe.events._v1_tax_rate_created_event import (
    V1TaxRateCreatedEvent,
    V1TaxRateCreatedEventNotification,
)
from stripe.events._v1_tax_rate_updated_event import (
    V1TaxRateUpdatedEvent,
    V1TaxRateUpdatedEventNotification,
)
from stripe.events._v1_terminal_reader_action_failed_event import (
    V1TerminalReaderActionFailedEvent,
    V1TerminalReaderActionFailedEventNotification,
)
from stripe.events._v1_terminal_reader_action_succeeded_event import (
    V1TerminalReaderActionSucceededEvent,
    V1TerminalReaderActionSucceededEventNotification,
)
from stripe.events._v1_terminal_reader_action_updated_event import (
    V1TerminalReaderActionUpdatedEvent,
    V1TerminalReaderActionUpdatedEventNotification,
)
from stripe.events._v1_test_helpers_test_clock_advancing_event import (
    V1TestHelpersTestClockAdvancingEvent,
    V1TestHelpersTestClockAdvancingEventNotification,
)
from stripe.events._v1_test_helpers_test_clock_created_event import (
    V1TestHelpersTestClockCreatedEvent,
    V1TestHelpersTestClockCreatedEventNotification,
)
from stripe.events._v1_test_helpers_test_clock_deleted_event import (
    V1TestHelpersTestClockDeletedEvent,
    V1TestHelpersTestClockDeletedEventNotification,
)
from stripe.events._v1_test_helpers_test_clock_internal_failure_event import (
    V1TestHelpersTestClockInternalFailureEvent,
    V1TestHelpersTestClockInternalFailureEventNotification,
)
from stripe.events._v1_test_helpers_test_clock_ready_event import (
    V1TestHelpersTestClockReadyEvent,
    V1TestHelpersTestClockReadyEventNotification,
)
from stripe.events._v1_topup_canceled_event import (
    V1TopupCanceledEvent,
    V1TopupCanceledEventNotification,
)
from stripe.events._v1_topup_created_event import (
    V1TopupCreatedEvent,
    V1TopupCreatedEventNotification,
)
from stripe.events._v1_topup_failed_event import (
    V1TopupFailedEvent,
    V1TopupFailedEventNotification,
)
from stripe.events._v1_topup_reversed_event import (
    V1TopupReversedEvent,
    V1TopupReversedEventNotification,
)
from stripe.events._v1_topup_succeeded_event import (
    V1TopupSucceededEvent,
    V1TopupSucceededEventNotification,
)
from stripe.events._v1_transfer_created_event import (
    V1TransferCreatedEvent,
    V1TransferCreatedEventNotification,
)
from stripe.events._v1_transfer_reversed_event import (
    V1TransferReversedEvent,
    V1TransferReversedEventNotification,
)
from stripe.events._v1_transfer_updated_event import (
    V1TransferUpdatedEvent,
    V1TransferUpdatedEventNotification,
)
from stripe.events._v2_billing_cadence_billed_event import (
    V2BillingCadenceBilledEvent,
    V2BillingCadenceBilledEventNotification,
)
from stripe.events._v2_billing_cadence_canceled_event import (
    V2BillingCadenceCanceledEvent,
    V2BillingCadenceCanceledEventNotification,
)
from stripe.events._v2_billing_cadence_created_event import (
    V2BillingCadenceCreatedEvent,
    V2BillingCadenceCreatedEventNotification,
)
from stripe.events._v2_billing_license_fee_created_event import (
    V2BillingLicenseFeeCreatedEvent,
    V2BillingLicenseFeeCreatedEventNotification,
)
from stripe.events._v2_billing_license_fee_updated_event import (
    V2BillingLicenseFeeUpdatedEvent,
    V2BillingLicenseFeeUpdatedEventNotification,
)
from stripe.events._v2_billing_license_fee_version_created_event import (
    V2BillingLicenseFeeVersionCreatedEvent,
    V2BillingLicenseFeeVersionCreatedEventNotification,
)
from stripe.events._v2_billing_licensed_item_created_event import (
    V2BillingLicensedItemCreatedEvent,
    V2BillingLicensedItemCreatedEventNotification,
)
from stripe.events._v2_billing_licensed_item_updated_event import (
    V2BillingLicensedItemUpdatedEvent,
    V2BillingLicensedItemUpdatedEventNotification,
)
from stripe.events._v2_billing_metered_item_created_event import (
    V2BillingMeteredItemCreatedEvent,
    V2BillingMeteredItemCreatedEventNotification,
)
from stripe.events._v2_billing_metered_item_updated_event import (
    V2BillingMeteredItemUpdatedEvent,
    V2BillingMeteredItemUpdatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_created_event import (
    V2BillingPricingPlanCreatedEvent,
    V2BillingPricingPlanCreatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_updated_event import (
    V2BillingPricingPlanUpdatedEvent,
    V2BillingPricingPlanUpdatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_component_created_event import (
    V2BillingPricingPlanComponentCreatedEvent,
    V2BillingPricingPlanComponentCreatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_component_updated_event import (
    V2BillingPricingPlanComponentUpdatedEvent,
    V2BillingPricingPlanComponentUpdatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_awaiting_customer_action_event import (
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEvent,
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_current_event import (
    V2BillingPricingPlanSubscriptionCollectionCurrentEvent,
    V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_past_due_event import (
    V2BillingPricingPlanSubscriptionCollectionPastDueEvent,
    V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_paused_event import (
    V2BillingPricingPlanSubscriptionCollectionPausedEvent,
    V2BillingPricingPlanSubscriptionCollectionPausedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_collection_unpaid_event import (
    V2BillingPricingPlanSubscriptionCollectionUnpaidEvent,
    V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_activated_event import (
    V2BillingPricingPlanSubscriptionServicingActivatedEvent,
    V2BillingPricingPlanSubscriptionServicingActivatedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_canceled_event import (
    V2BillingPricingPlanSubscriptionServicingCanceledEvent,
    V2BillingPricingPlanSubscriptionServicingCanceledEventNotification,
)
from stripe.events._v2_billing_pricing_plan_subscription_servicing_paused_event import (
    V2BillingPricingPlanSubscriptionServicingPausedEvent,
    V2BillingPricingPlanSubscriptionServicingPausedEventNotification,
)
from stripe.events._v2_billing_pricing_plan_version_created_event import (
    V2BillingPricingPlanVersionCreatedEvent,
    V2BillingPricingPlanVersionCreatedEventNotification,
)
from stripe.events._v2_billing_rate_card_created_event import (
    V2BillingRateCardCreatedEvent,
    V2BillingRateCardCreatedEventNotification,
)
from stripe.events._v2_billing_rate_card_updated_event import (
    V2BillingRateCardUpdatedEvent,
    V2BillingRateCardUpdatedEventNotification,
)
from stripe.events._v2_billing_rate_card_rate_created_event import (
    V2BillingRateCardRateCreatedEvent,
    V2BillingRateCardRateCreatedEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_activated_event import (
    V2BillingRateCardSubscriptionActivatedEvent,
    V2BillingRateCardSubscriptionActivatedEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_canceled_event import (
    V2BillingRateCardSubscriptionCanceledEvent,
    V2BillingRateCardSubscriptionCanceledEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_collection_awaiting_customer_action_event import (
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEvent,
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_collection_current_event import (
    V2BillingRateCardSubscriptionCollectionCurrentEvent,
    V2BillingRateCardSubscriptionCollectionCurrentEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_collection_past_due_event import (
    V2BillingRateCardSubscriptionCollectionPastDueEvent,
    V2BillingRateCardSubscriptionCollectionPastDueEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_collection_paused_event import (
    V2BillingRateCardSubscriptionCollectionPausedEvent,
    V2BillingRateCardSubscriptionCollectionPausedEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_collection_unpaid_event import (
    V2BillingRateCardSubscriptionCollectionUnpaidEvent,
    V2BillingRateCardSubscriptionCollectionUnpaidEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_activated_event import (
    V2BillingRateCardSubscriptionServicingActivatedEvent,
    V2BillingRateCardSubscriptionServicingActivatedEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_canceled_event import (
    V2BillingRateCardSubscriptionServicingCanceledEvent,
    V2BillingRateCardSubscriptionServicingCanceledEventNotification,
)
from stripe.events._v2_billing_rate_card_subscription_servicing_paused_event import (
    V2BillingRateCardSubscriptionServicingPausedEvent,
    V2BillingRateCardSubscriptionServicingPausedEventNotification,
)
from stripe.events._v2_billing_rate_card_version_created_event import (
    V2BillingRateCardVersionCreatedEvent,
    V2BillingRateCardVersionCreatedEventNotification,
)
from stripe.events._v2_core_account_closed_event import (
    V2CoreAccountClosedEvent,
    V2CoreAccountClosedEventNotification,
)
from stripe.events._v2_core_account_created_event import (
    V2CoreAccountCreatedEvent,
    V2CoreAccountCreatedEventNotification,
)
from stripe.events._v2_core_account_updated_event import (
    V2CoreAccountUpdatedEvent,
    V2CoreAccountUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_card_creator_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_card_creator_updated_event import (
    V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent,
    V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_customer_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_customer_updated_event import (
    V2CoreAccountIncludingConfigurationCustomerUpdatedEvent,
    V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_merchant_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_merchant_updated_event import (
    V2CoreAccountIncludingConfigurationMerchantUpdatedEvent,
    V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_recipient_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_recipient_updated_event import (
    V2CoreAccountIncludingConfigurationRecipientUpdatedEvent,
    V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_storer_capability_status_updated_event import (
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_configuration_storer_updated_event import (
    V2CoreAccountIncludingConfigurationStorerUpdatedEvent,
    V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_defaults_updated_event import (
    V2CoreAccountIncludingDefaultsUpdatedEvent,
    V2CoreAccountIncludingDefaultsUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_identity_updated_event import (
    V2CoreAccountIncludingIdentityUpdatedEvent,
    V2CoreAccountIncludingIdentityUpdatedEventNotification,
)
from stripe.events._v2_core_account_including_requirements_updated_event import (
    V2CoreAccountIncludingRequirementsUpdatedEvent,
    V2CoreAccountIncludingRequirementsUpdatedEventNotification,
)
from stripe.events._v2_core_account_link_returned_event import (
    V2CoreAccountLinkReturnedEvent,
    V2CoreAccountLinkReturnedEventNotification,
)
from stripe.events._v2_core_account_person_created_event import (
    V2CoreAccountPersonCreatedEvent,
    V2CoreAccountPersonCreatedEventNotification,
)
from stripe.events._v2_core_account_person_deleted_event import (
    V2CoreAccountPersonDeletedEvent,
    V2CoreAccountPersonDeletedEventNotification,
)
from stripe.events._v2_core_account_person_updated_event import (
    V2CoreAccountPersonUpdatedEvent,
    V2CoreAccountPersonUpdatedEventNotification,
)
from stripe.events._v2_core_claimable_sandbox_claimed_event import (
    V2CoreClaimableSandboxClaimedEvent,
    V2CoreClaimableSandboxClaimedEventNotification,
)
from stripe.events._v2_core_claimable_sandbox_created_event import (
    V2CoreClaimableSandboxCreatedEvent,
    V2CoreClaimableSandboxCreatedEventNotification,
)
from stripe.events._v2_core_claimable_sandbox_expired_event import (
    V2CoreClaimableSandboxExpiredEvent,
    V2CoreClaimableSandboxExpiredEventNotification,
)
from stripe.events._v2_core_claimable_sandbox_expiring_event import (
    V2CoreClaimableSandboxExpiringEvent,
    V2CoreClaimableSandboxExpiringEventNotification,
)
from stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event import (
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent,
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification,
)
from stripe.events._v2_core_event_destination_ping_event import (
    V2CoreEventDestinationPingEvent,
    V2CoreEventDestinationPingEventNotification,
)
from stripe.events._v2_core_health_api_error_firing_event import (
    V2CoreHealthApiErrorFiringEvent,
    V2CoreHealthApiErrorFiringEventNotification,
)
from stripe.events._v2_core_health_api_error_resolved_event import (
    V2CoreHealthApiErrorResolvedEvent,
    V2CoreHealthApiErrorResolvedEventNotification,
)
from stripe.events._v2_core_health_api_latency_firing_event import (
    V2CoreHealthApiLatencyFiringEvent,
    V2CoreHealthApiLatencyFiringEventNotification,
)
from stripe.events._v2_core_health_api_latency_resolved_event import (
    V2CoreHealthApiLatencyResolvedEvent,
    V2CoreHealthApiLatencyResolvedEventNotification,
)
from stripe.events._v2_core_health_authorization_rate_drop_firing_event import (
    V2CoreHealthAuthorizationRateDropFiringEvent,
    V2CoreHealthAuthorizationRateDropFiringEventNotification,
)
from stripe.events._v2_core_health_authorization_rate_drop_resolved_event import (
    V2CoreHealthAuthorizationRateDropResolvedEvent,
    V2CoreHealthAuthorizationRateDropResolvedEventNotification,
)
from stripe.events._v2_core_health_event_generation_failure_resolved_event import (
    V2CoreHealthEventGenerationFailureResolvedEvent,
    V2CoreHealthEventGenerationFailureResolvedEventNotification,
)
from stripe.events._v2_core_health_fraud_rate_increased_event import (
    V2CoreHealthFraudRateIncreasedEvent,
    V2CoreHealthFraudRateIncreasedEventNotification,
)
from stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event import (
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent,
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification,
)
from stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event import (
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent,
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification,
)
from stripe.events._v2_core_health_issuing_authorization_request_timeout_firing_event import (
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent,
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification,
)
from stripe.events._v2_core_health_issuing_authorization_request_timeout_resolved_event import (
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent,
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification,
)
from stripe.events._v2_core_health_payment_method_error_firing_event import (
    V2CoreHealthPaymentMethodErrorFiringEvent,
    V2CoreHealthPaymentMethodErrorFiringEventNotification,
)
from stripe.events._v2_core_health_payment_method_error_resolved_event import (
    V2CoreHealthPaymentMethodErrorResolvedEvent,
    V2CoreHealthPaymentMethodErrorResolvedEventNotification,
)
from stripe.events._v2_core_health_traffic_volume_drop_firing_event import (
    V2CoreHealthTrafficVolumeDropFiringEvent,
    V2CoreHealthTrafficVolumeDropFiringEventNotification,
)
from stripe.events._v2_core_health_traffic_volume_drop_resolved_event import (
    V2CoreHealthTrafficVolumeDropResolvedEvent,
    V2CoreHealthTrafficVolumeDropResolvedEventNotification,
)
from stripe.events._v2_core_health_webhook_latency_firing_event import (
    V2CoreHealthWebhookLatencyFiringEvent,
    V2CoreHealthWebhookLatencyFiringEventNotification,
)
from stripe.events._v2_core_health_webhook_latency_resolved_event import (
    V2CoreHealthWebhookLatencyResolvedEvent,
    V2CoreHealthWebhookLatencyResolvedEventNotification,
)
from stripe.events._v2_money_management_adjustment_created_event import (
    V2MoneyManagementAdjustmentCreatedEvent,
    V2MoneyManagementAdjustmentCreatedEventNotification,
)
from stripe.events._v2_money_management_financial_account_created_event import (
    V2MoneyManagementFinancialAccountCreatedEvent,
    V2MoneyManagementFinancialAccountCreatedEventNotification,
)
from stripe.events._v2_money_management_financial_account_updated_event import (
    V2MoneyManagementFinancialAccountUpdatedEvent,
    V2MoneyManagementFinancialAccountUpdatedEventNotification,
)
from stripe.events._v2_money_management_financial_address_activated_event import (
    V2MoneyManagementFinancialAddressActivatedEvent,
    V2MoneyManagementFinancialAddressActivatedEventNotification,
)
from stripe.events._v2_money_management_financial_address_failed_event import (
    V2MoneyManagementFinancialAddressFailedEvent,
    V2MoneyManagementFinancialAddressFailedEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_available_event import (
    V2MoneyManagementInboundTransferAvailableEvent,
    V2MoneyManagementInboundTransferAvailableEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_failed_event import (
    V2MoneyManagementInboundTransferBankDebitFailedEvent,
    V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_processing_event import (
    V2MoneyManagementInboundTransferBankDebitProcessingEvent,
    V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_queued_event import (
    V2MoneyManagementInboundTransferBankDebitQueuedEvent,
    V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_returned_event import (
    V2MoneyManagementInboundTransferBankDebitReturnedEvent,
    V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
)
from stripe.events._v2_money_management_inbound_transfer_bank_debit_succeeded_event import (
    V2MoneyManagementInboundTransferBankDebitSucceededEvent,
    V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_canceled_event import (
    V2MoneyManagementOutboundPaymentCanceledEvent,
    V2MoneyManagementOutboundPaymentCanceledEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_created_event import (
    V2MoneyManagementOutboundPaymentCreatedEvent,
    V2MoneyManagementOutboundPaymentCreatedEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_failed_event import (
    V2MoneyManagementOutboundPaymentFailedEvent,
    V2MoneyManagementOutboundPaymentFailedEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_posted_event import (
    V2MoneyManagementOutboundPaymentPostedEvent,
    V2MoneyManagementOutboundPaymentPostedEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_returned_event import (
    V2MoneyManagementOutboundPaymentReturnedEvent,
    V2MoneyManagementOutboundPaymentReturnedEventNotification,
)
from stripe.events._v2_money_management_outbound_payment_updated_event import (
    V2MoneyManagementOutboundPaymentUpdatedEvent,
    V2MoneyManagementOutboundPaymentUpdatedEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_canceled_event import (
    V2MoneyManagementOutboundTransferCanceledEvent,
    V2MoneyManagementOutboundTransferCanceledEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_created_event import (
    V2MoneyManagementOutboundTransferCreatedEvent,
    V2MoneyManagementOutboundTransferCreatedEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_failed_event import (
    V2MoneyManagementOutboundTransferFailedEvent,
    V2MoneyManagementOutboundTransferFailedEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_posted_event import (
    V2MoneyManagementOutboundTransferPostedEvent,
    V2MoneyManagementOutboundTransferPostedEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_returned_event import (
    V2MoneyManagementOutboundTransferReturnedEvent,
    V2MoneyManagementOutboundTransferReturnedEventNotification,
)
from stripe.events._v2_money_management_outbound_transfer_updated_event import (
    V2MoneyManagementOutboundTransferUpdatedEvent,
    V2MoneyManagementOutboundTransferUpdatedEventNotification,
)
from stripe.events._v2_money_management_payout_method_updated_event import (
    V2MoneyManagementPayoutMethodUpdatedEvent,
    V2MoneyManagementPayoutMethodUpdatedEventNotification,
)
from stripe.events._v2_money_management_received_credit_available_event import (
    V2MoneyManagementReceivedCreditAvailableEvent,
    V2MoneyManagementReceivedCreditAvailableEventNotification,
)
from stripe.events._v2_money_management_received_credit_failed_event import (
    V2MoneyManagementReceivedCreditFailedEvent,
    V2MoneyManagementReceivedCreditFailedEventNotification,
)
from stripe.events._v2_money_management_received_credit_returned_event import (
    V2MoneyManagementReceivedCreditReturnedEvent,
    V2MoneyManagementReceivedCreditReturnedEventNotification,
)
from stripe.events._v2_money_management_received_credit_succeeded_event import (
    V2MoneyManagementReceivedCreditSucceededEvent,
    V2MoneyManagementReceivedCreditSucceededEventNotification,
)
from stripe.events._v2_money_management_received_debit_canceled_event import (
    V2MoneyManagementReceivedDebitCanceledEvent,
    V2MoneyManagementReceivedDebitCanceledEventNotification,
)
from stripe.events._v2_money_management_received_debit_failed_event import (
    V2MoneyManagementReceivedDebitFailedEvent,
    V2MoneyManagementReceivedDebitFailedEventNotification,
)
from stripe.events._v2_money_management_received_debit_pending_event import (
    V2MoneyManagementReceivedDebitPendingEvent,
    V2MoneyManagementReceivedDebitPendingEventNotification,
)
from stripe.events._v2_money_management_received_debit_succeeded_event import (
    V2MoneyManagementReceivedDebitSucceededEvent,
    V2MoneyManagementReceivedDebitSucceededEventNotification,
)
from stripe.events._v2_money_management_received_debit_updated_event import (
    V2MoneyManagementReceivedDebitUpdatedEvent,
    V2MoneyManagementReceivedDebitUpdatedEventNotification,
)
from stripe.events._v2_money_management_recipient_verification_created_event import (
    V2MoneyManagementRecipientVerificationCreatedEvent,
    V2MoneyManagementRecipientVerificationCreatedEventNotification,
)
from stripe.events._v2_money_management_recipient_verification_updated_event import (
    V2MoneyManagementRecipientVerificationUpdatedEvent,
    V2MoneyManagementRecipientVerificationUpdatedEventNotification,
)
from stripe.events._v2_money_management_transaction_created_event import (
    V2MoneyManagementTransactionCreatedEvent,
    V2MoneyManagementTransactionCreatedEventNotification,
)
from stripe.events._v2_money_management_transaction_updated_event import (
    V2MoneyManagementTransactionUpdatedEvent,
    V2MoneyManagementTransactionUpdatedEventNotification,
)
from stripe.events._v2_payments_off_session_payment_authorization_attempt_failed_event import (
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
)
from stripe.events._v2_payments_off_session_payment_authorization_attempt_started_event import (
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
)
from stripe.events._v2_payments_off_session_payment_canceled_event import (
    V2PaymentsOffSessionPaymentCanceledEvent,
    V2PaymentsOffSessionPaymentCanceledEventNotification,
)
from stripe.events._v2_payments_off_session_payment_created_event import (
    V2PaymentsOffSessionPaymentCreatedEvent,
    V2PaymentsOffSessionPaymentCreatedEventNotification,
)
from stripe.events._v2_payments_off_session_payment_failed_event import (
    V2PaymentsOffSessionPaymentFailedEvent,
    V2PaymentsOffSessionPaymentFailedEventNotification,
)
from stripe.events._v2_payments_off_session_payment_requires_capture_event import (
    V2PaymentsOffSessionPaymentRequiresCaptureEvent,
    V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
)
from stripe.events._v2_payments_off_session_payment_succeeded_event import (
    V2PaymentsOffSessionPaymentSucceededEvent,
    V2PaymentsOffSessionPaymentSucceededEventNotification,
)


V2_EVENT_CLASS_LOOKUP = {
    V1AccountUpdatedEvent.LOOKUP_TYPE: V1AccountUpdatedEvent,
    V1ApplicationFeeCreatedEvent.LOOKUP_TYPE: V1ApplicationFeeCreatedEvent,
    V1ApplicationFeeRefundedEvent.LOOKUP_TYPE: V1ApplicationFeeRefundedEvent,
    V1BillingMeterErrorReportTriggeredEvent.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEvent,
    V1BillingMeterNoMeterFoundEvent.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEvent,
    V1BillingPortalConfigurationCreatedEvent.LOOKUP_TYPE: V1BillingPortalConfigurationCreatedEvent,
    V1BillingPortalConfigurationUpdatedEvent.LOOKUP_TYPE: V1BillingPortalConfigurationUpdatedEvent,
    V1CapabilityUpdatedEvent.LOOKUP_TYPE: V1CapabilityUpdatedEvent,
    V1ChargeCapturedEvent.LOOKUP_TYPE: V1ChargeCapturedEvent,
    V1ChargeDisputeClosedEvent.LOOKUP_TYPE: V1ChargeDisputeClosedEvent,
    V1ChargeDisputeCreatedEvent.LOOKUP_TYPE: V1ChargeDisputeCreatedEvent,
    V1ChargeDisputeFundsReinstatedEvent.LOOKUP_TYPE: V1ChargeDisputeFundsReinstatedEvent,
    V1ChargeDisputeFundsWithdrawnEvent.LOOKUP_TYPE: V1ChargeDisputeFundsWithdrawnEvent,
    V1ChargeDisputeUpdatedEvent.LOOKUP_TYPE: V1ChargeDisputeUpdatedEvent,
    V1ChargeExpiredEvent.LOOKUP_TYPE: V1ChargeExpiredEvent,
    V1ChargeFailedEvent.LOOKUP_TYPE: V1ChargeFailedEvent,
    V1ChargePendingEvent.LOOKUP_TYPE: V1ChargePendingEvent,
    V1ChargeRefundedEvent.LOOKUP_TYPE: V1ChargeRefundedEvent,
    V1ChargeRefundUpdatedEvent.LOOKUP_TYPE: V1ChargeRefundUpdatedEvent,
    V1ChargeSucceededEvent.LOOKUP_TYPE: V1ChargeSucceededEvent,
    V1ChargeUpdatedEvent.LOOKUP_TYPE: V1ChargeUpdatedEvent,
    V1CheckoutSessionAsyncPaymentFailedEvent.LOOKUP_TYPE: V1CheckoutSessionAsyncPaymentFailedEvent,
    V1CheckoutSessionAsyncPaymentSucceededEvent.LOOKUP_TYPE: V1CheckoutSessionAsyncPaymentSucceededEvent,
    V1CheckoutSessionCompletedEvent.LOOKUP_TYPE: V1CheckoutSessionCompletedEvent,
    V1CheckoutSessionExpiredEvent.LOOKUP_TYPE: V1CheckoutSessionExpiredEvent,
    V1ClimateOrderCanceledEvent.LOOKUP_TYPE: V1ClimateOrderCanceledEvent,
    V1ClimateOrderCreatedEvent.LOOKUP_TYPE: V1ClimateOrderCreatedEvent,
    V1ClimateOrderDelayedEvent.LOOKUP_TYPE: V1ClimateOrderDelayedEvent,
    V1ClimateOrderDeliveredEvent.LOOKUP_TYPE: V1ClimateOrderDeliveredEvent,
    V1ClimateOrderProductSubstitutedEvent.LOOKUP_TYPE: V1ClimateOrderProductSubstitutedEvent,
    V1ClimateProductCreatedEvent.LOOKUP_TYPE: V1ClimateProductCreatedEvent,
    V1ClimateProductPricingUpdatedEvent.LOOKUP_TYPE: V1ClimateProductPricingUpdatedEvent,
    V1CouponCreatedEvent.LOOKUP_TYPE: V1CouponCreatedEvent,
    V1CouponDeletedEvent.LOOKUP_TYPE: V1CouponDeletedEvent,
    V1CouponUpdatedEvent.LOOKUP_TYPE: V1CouponUpdatedEvent,
    V1CreditNoteCreatedEvent.LOOKUP_TYPE: V1CreditNoteCreatedEvent,
    V1CreditNoteUpdatedEvent.LOOKUP_TYPE: V1CreditNoteUpdatedEvent,
    V1CreditNoteVoidedEvent.LOOKUP_TYPE: V1CreditNoteVoidedEvent,
    V1CustomerCreatedEvent.LOOKUP_TYPE: V1CustomerCreatedEvent,
    V1CustomerDeletedEvent.LOOKUP_TYPE: V1CustomerDeletedEvent,
    V1CustomerSubscriptionCreatedEvent.LOOKUP_TYPE: V1CustomerSubscriptionCreatedEvent,
    V1CustomerSubscriptionDeletedEvent.LOOKUP_TYPE: V1CustomerSubscriptionDeletedEvent,
    V1CustomerSubscriptionPausedEvent.LOOKUP_TYPE: V1CustomerSubscriptionPausedEvent,
    V1CustomerSubscriptionPendingUpdateAppliedEvent.LOOKUP_TYPE: V1CustomerSubscriptionPendingUpdateAppliedEvent,
    V1CustomerSubscriptionPendingUpdateExpiredEvent.LOOKUP_TYPE: V1CustomerSubscriptionPendingUpdateExpiredEvent,
    V1CustomerSubscriptionResumedEvent.LOOKUP_TYPE: V1CustomerSubscriptionResumedEvent,
    V1CustomerSubscriptionTrialWillEndEvent.LOOKUP_TYPE: V1CustomerSubscriptionTrialWillEndEvent,
    V1CustomerSubscriptionUpdatedEvent.LOOKUP_TYPE: V1CustomerSubscriptionUpdatedEvent,
    V1CustomerTaxIdCreatedEvent.LOOKUP_TYPE: V1CustomerTaxIdCreatedEvent,
    V1CustomerTaxIdDeletedEvent.LOOKUP_TYPE: V1CustomerTaxIdDeletedEvent,
    V1CustomerTaxIdUpdatedEvent.LOOKUP_TYPE: V1CustomerTaxIdUpdatedEvent,
    V1CustomerUpdatedEvent.LOOKUP_TYPE: V1CustomerUpdatedEvent,
    V1FileCreatedEvent.LOOKUP_TYPE: V1FileCreatedEvent,
    V1FinancialConnectionsAccountCreatedEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountCreatedEvent,
    V1FinancialConnectionsAccountDeactivatedEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountDeactivatedEvent,
    V1FinancialConnectionsAccountDisconnectedEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountDisconnectedEvent,
    V1FinancialConnectionsAccountReactivatedEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountReactivatedEvent,
    V1FinancialConnectionsAccountRefreshedBalanceEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedBalanceEvent,
    V1FinancialConnectionsAccountRefreshedOwnershipEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedOwnershipEvent,
    V1FinancialConnectionsAccountRefreshedTransactionsEvent.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedTransactionsEvent,
    V1IdentityVerificationSessionCanceledEvent.LOOKUP_TYPE: V1IdentityVerificationSessionCanceledEvent,
    V1IdentityVerificationSessionCreatedEvent.LOOKUP_TYPE: V1IdentityVerificationSessionCreatedEvent,
    V1IdentityVerificationSessionProcessingEvent.LOOKUP_TYPE: V1IdentityVerificationSessionProcessingEvent,
    V1IdentityVerificationSessionRedactedEvent.LOOKUP_TYPE: V1IdentityVerificationSessionRedactedEvent,
    V1IdentityVerificationSessionRequiresInputEvent.LOOKUP_TYPE: V1IdentityVerificationSessionRequiresInputEvent,
    V1IdentityVerificationSessionVerifiedEvent.LOOKUP_TYPE: V1IdentityVerificationSessionVerifiedEvent,
    V1InvoiceCreatedEvent.LOOKUP_TYPE: V1InvoiceCreatedEvent,
    V1InvoiceDeletedEvent.LOOKUP_TYPE: V1InvoiceDeletedEvent,
    V1InvoiceFinalizationFailedEvent.LOOKUP_TYPE: V1InvoiceFinalizationFailedEvent,
    V1InvoiceFinalizedEvent.LOOKUP_TYPE: V1InvoiceFinalizedEvent,
    V1InvoiceitemCreatedEvent.LOOKUP_TYPE: V1InvoiceitemCreatedEvent,
    V1InvoiceitemDeletedEvent.LOOKUP_TYPE: V1InvoiceitemDeletedEvent,
    V1InvoiceMarkedUncollectibleEvent.LOOKUP_TYPE: V1InvoiceMarkedUncollectibleEvent,
    V1InvoiceOverdueEvent.LOOKUP_TYPE: V1InvoiceOverdueEvent,
    V1InvoiceOverpaidEvent.LOOKUP_TYPE: V1InvoiceOverpaidEvent,
    V1InvoicePaidEvent.LOOKUP_TYPE: V1InvoicePaidEvent,
    V1InvoicePaymentActionRequiredEvent.LOOKUP_TYPE: V1InvoicePaymentActionRequiredEvent,
    V1InvoicePaymentFailedEvent.LOOKUP_TYPE: V1InvoicePaymentFailedEvent,
    V1InvoicePaymentPaidEvent.LOOKUP_TYPE: V1InvoicePaymentPaidEvent,
    V1InvoicePaymentSucceededEvent.LOOKUP_TYPE: V1InvoicePaymentSucceededEvent,
    V1InvoiceSentEvent.LOOKUP_TYPE: V1InvoiceSentEvent,
    V1InvoiceUpcomingEvent.LOOKUP_TYPE: V1InvoiceUpcomingEvent,
    V1InvoiceUpdatedEvent.LOOKUP_TYPE: V1InvoiceUpdatedEvent,
    V1InvoiceVoidedEvent.LOOKUP_TYPE: V1InvoiceVoidedEvent,
    V1InvoiceWillBeDueEvent.LOOKUP_TYPE: V1InvoiceWillBeDueEvent,
    V1IssuingAuthorizationCreatedEvent.LOOKUP_TYPE: V1IssuingAuthorizationCreatedEvent,
    V1IssuingAuthorizationRequestEvent.LOOKUP_TYPE: V1IssuingAuthorizationRequestEvent,
    V1IssuingAuthorizationUpdatedEvent.LOOKUP_TYPE: V1IssuingAuthorizationUpdatedEvent,
    V1IssuingCardCreatedEvent.LOOKUP_TYPE: V1IssuingCardCreatedEvent,
    V1IssuingCardholderCreatedEvent.LOOKUP_TYPE: V1IssuingCardholderCreatedEvent,
    V1IssuingCardholderUpdatedEvent.LOOKUP_TYPE: V1IssuingCardholderUpdatedEvent,
    V1IssuingCardUpdatedEvent.LOOKUP_TYPE: V1IssuingCardUpdatedEvent,
    V1IssuingDisputeClosedEvent.LOOKUP_TYPE: V1IssuingDisputeClosedEvent,
    V1IssuingDisputeCreatedEvent.LOOKUP_TYPE: V1IssuingDisputeCreatedEvent,
    V1IssuingDisputeFundsReinstatedEvent.LOOKUP_TYPE: V1IssuingDisputeFundsReinstatedEvent,
    V1IssuingDisputeFundsRescindedEvent.LOOKUP_TYPE: V1IssuingDisputeFundsRescindedEvent,
    V1IssuingDisputeSubmittedEvent.LOOKUP_TYPE: V1IssuingDisputeSubmittedEvent,
    V1IssuingDisputeUpdatedEvent.LOOKUP_TYPE: V1IssuingDisputeUpdatedEvent,
    V1IssuingPersonalizationDesignActivatedEvent.LOOKUP_TYPE: V1IssuingPersonalizationDesignActivatedEvent,
    V1IssuingPersonalizationDesignDeactivatedEvent.LOOKUP_TYPE: V1IssuingPersonalizationDesignDeactivatedEvent,
    V1IssuingPersonalizationDesignRejectedEvent.LOOKUP_TYPE: V1IssuingPersonalizationDesignRejectedEvent,
    V1IssuingPersonalizationDesignUpdatedEvent.LOOKUP_TYPE: V1IssuingPersonalizationDesignUpdatedEvent,
    V1IssuingTokenCreatedEvent.LOOKUP_TYPE: V1IssuingTokenCreatedEvent,
    V1IssuingTokenUpdatedEvent.LOOKUP_TYPE: V1IssuingTokenUpdatedEvent,
    V1IssuingTransactionCreatedEvent.LOOKUP_TYPE: V1IssuingTransactionCreatedEvent,
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent.LOOKUP_TYPE: V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent,
    V1IssuingTransactionUpdatedEvent.LOOKUP_TYPE: V1IssuingTransactionUpdatedEvent,
    V1MandateUpdatedEvent.LOOKUP_TYPE: V1MandateUpdatedEvent,
    V1PaymentIntentAmountCapturableUpdatedEvent.LOOKUP_TYPE: V1PaymentIntentAmountCapturableUpdatedEvent,
    V1PaymentIntentCanceledEvent.LOOKUP_TYPE: V1PaymentIntentCanceledEvent,
    V1PaymentIntentCreatedEvent.LOOKUP_TYPE: V1PaymentIntentCreatedEvent,
    V1PaymentIntentPartiallyFundedEvent.LOOKUP_TYPE: V1PaymentIntentPartiallyFundedEvent,
    V1PaymentIntentPaymentFailedEvent.LOOKUP_TYPE: V1PaymentIntentPaymentFailedEvent,
    V1PaymentIntentProcessingEvent.LOOKUP_TYPE: V1PaymentIntentProcessingEvent,
    V1PaymentIntentRequiresActionEvent.LOOKUP_TYPE: V1PaymentIntentRequiresActionEvent,
    V1PaymentIntentSucceededEvent.LOOKUP_TYPE: V1PaymentIntentSucceededEvent,
    V1PaymentLinkCreatedEvent.LOOKUP_TYPE: V1PaymentLinkCreatedEvent,
    V1PaymentLinkUpdatedEvent.LOOKUP_TYPE: V1PaymentLinkUpdatedEvent,
    V1PaymentMethodAttachedEvent.LOOKUP_TYPE: V1PaymentMethodAttachedEvent,
    V1PaymentMethodAutomaticallyUpdatedEvent.LOOKUP_TYPE: V1PaymentMethodAutomaticallyUpdatedEvent,
    V1PaymentMethodDetachedEvent.LOOKUP_TYPE: V1PaymentMethodDetachedEvent,
    V1PaymentMethodUpdatedEvent.LOOKUP_TYPE: V1PaymentMethodUpdatedEvent,
    V1PayoutCanceledEvent.LOOKUP_TYPE: V1PayoutCanceledEvent,
    V1PayoutCreatedEvent.LOOKUP_TYPE: V1PayoutCreatedEvent,
    V1PayoutFailedEvent.LOOKUP_TYPE: V1PayoutFailedEvent,
    V1PayoutPaidEvent.LOOKUP_TYPE: V1PayoutPaidEvent,
    V1PayoutReconciliationCompletedEvent.LOOKUP_TYPE: V1PayoutReconciliationCompletedEvent,
    V1PayoutUpdatedEvent.LOOKUP_TYPE: V1PayoutUpdatedEvent,
    V1PersonCreatedEvent.LOOKUP_TYPE: V1PersonCreatedEvent,
    V1PersonDeletedEvent.LOOKUP_TYPE: V1PersonDeletedEvent,
    V1PersonUpdatedEvent.LOOKUP_TYPE: V1PersonUpdatedEvent,
    V1PlanCreatedEvent.LOOKUP_TYPE: V1PlanCreatedEvent,
    V1PlanDeletedEvent.LOOKUP_TYPE: V1PlanDeletedEvent,
    V1PlanUpdatedEvent.LOOKUP_TYPE: V1PlanUpdatedEvent,
    V1PriceCreatedEvent.LOOKUP_TYPE: V1PriceCreatedEvent,
    V1PriceDeletedEvent.LOOKUP_TYPE: V1PriceDeletedEvent,
    V1PriceUpdatedEvent.LOOKUP_TYPE: V1PriceUpdatedEvent,
    V1ProductCreatedEvent.LOOKUP_TYPE: V1ProductCreatedEvent,
    V1ProductDeletedEvent.LOOKUP_TYPE: V1ProductDeletedEvent,
    V1ProductUpdatedEvent.LOOKUP_TYPE: V1ProductUpdatedEvent,
    V1PromotionCodeCreatedEvent.LOOKUP_TYPE: V1PromotionCodeCreatedEvent,
    V1PromotionCodeUpdatedEvent.LOOKUP_TYPE: V1PromotionCodeUpdatedEvent,
    V1QuoteAcceptedEvent.LOOKUP_TYPE: V1QuoteAcceptedEvent,
    V1QuoteCanceledEvent.LOOKUP_TYPE: V1QuoteCanceledEvent,
    V1QuoteCreatedEvent.LOOKUP_TYPE: V1QuoteCreatedEvent,
    V1QuoteFinalizedEvent.LOOKUP_TYPE: V1QuoteFinalizedEvent,
    V1RadarEarlyFraudWarningCreatedEvent.LOOKUP_TYPE: V1RadarEarlyFraudWarningCreatedEvent,
    V1RadarEarlyFraudWarningUpdatedEvent.LOOKUP_TYPE: V1RadarEarlyFraudWarningUpdatedEvent,
    V1RefundCreatedEvent.LOOKUP_TYPE: V1RefundCreatedEvent,
    V1RefundFailedEvent.LOOKUP_TYPE: V1RefundFailedEvent,
    V1RefundUpdatedEvent.LOOKUP_TYPE: V1RefundUpdatedEvent,
    V1ReviewClosedEvent.LOOKUP_TYPE: V1ReviewClosedEvent,
    V1ReviewOpenedEvent.LOOKUP_TYPE: V1ReviewOpenedEvent,
    V1SetupIntentCanceledEvent.LOOKUP_TYPE: V1SetupIntentCanceledEvent,
    V1SetupIntentCreatedEvent.LOOKUP_TYPE: V1SetupIntentCreatedEvent,
    V1SetupIntentRequiresActionEvent.LOOKUP_TYPE: V1SetupIntentRequiresActionEvent,
    V1SetupIntentSetupFailedEvent.LOOKUP_TYPE: V1SetupIntentSetupFailedEvent,
    V1SetupIntentSucceededEvent.LOOKUP_TYPE: V1SetupIntentSucceededEvent,
    V1SigmaScheduledQueryRunCreatedEvent.LOOKUP_TYPE: V1SigmaScheduledQueryRunCreatedEvent,
    V1SourceCanceledEvent.LOOKUP_TYPE: V1SourceCanceledEvent,
    V1SourceChargeableEvent.LOOKUP_TYPE: V1SourceChargeableEvent,
    V1SourceFailedEvent.LOOKUP_TYPE: V1SourceFailedEvent,
    V1SourceRefundAttributesRequiredEvent.LOOKUP_TYPE: V1SourceRefundAttributesRequiredEvent,
    V1SubscriptionScheduleAbortedEvent.LOOKUP_TYPE: V1SubscriptionScheduleAbortedEvent,
    V1SubscriptionScheduleCanceledEvent.LOOKUP_TYPE: V1SubscriptionScheduleCanceledEvent,
    V1SubscriptionScheduleCompletedEvent.LOOKUP_TYPE: V1SubscriptionScheduleCompletedEvent,
    V1SubscriptionScheduleCreatedEvent.LOOKUP_TYPE: V1SubscriptionScheduleCreatedEvent,
    V1SubscriptionScheduleExpiringEvent.LOOKUP_TYPE: V1SubscriptionScheduleExpiringEvent,
    V1SubscriptionScheduleReleasedEvent.LOOKUP_TYPE: V1SubscriptionScheduleReleasedEvent,
    V1SubscriptionScheduleUpdatedEvent.LOOKUP_TYPE: V1SubscriptionScheduleUpdatedEvent,
    V1TaxRateCreatedEvent.LOOKUP_TYPE: V1TaxRateCreatedEvent,
    V1TaxRateUpdatedEvent.LOOKUP_TYPE: V1TaxRateUpdatedEvent,
    V1TerminalReaderActionFailedEvent.LOOKUP_TYPE: V1TerminalReaderActionFailedEvent,
    V1TerminalReaderActionSucceededEvent.LOOKUP_TYPE: V1TerminalReaderActionSucceededEvent,
    V1TerminalReaderActionUpdatedEvent.LOOKUP_TYPE: V1TerminalReaderActionUpdatedEvent,
    V1TestHelpersTestClockAdvancingEvent.LOOKUP_TYPE: V1TestHelpersTestClockAdvancingEvent,
    V1TestHelpersTestClockCreatedEvent.LOOKUP_TYPE: V1TestHelpersTestClockCreatedEvent,
    V1TestHelpersTestClockDeletedEvent.LOOKUP_TYPE: V1TestHelpersTestClockDeletedEvent,
    V1TestHelpersTestClockInternalFailureEvent.LOOKUP_TYPE: V1TestHelpersTestClockInternalFailureEvent,
    V1TestHelpersTestClockReadyEvent.LOOKUP_TYPE: V1TestHelpersTestClockReadyEvent,
    V1TopupCanceledEvent.LOOKUP_TYPE: V1TopupCanceledEvent,
    V1TopupCreatedEvent.LOOKUP_TYPE: V1TopupCreatedEvent,
    V1TopupFailedEvent.LOOKUP_TYPE: V1TopupFailedEvent,
    V1TopupReversedEvent.LOOKUP_TYPE: V1TopupReversedEvent,
    V1TopupSucceededEvent.LOOKUP_TYPE: V1TopupSucceededEvent,
    V1TransferCreatedEvent.LOOKUP_TYPE: V1TransferCreatedEvent,
    V1TransferReversedEvent.LOOKUP_TYPE: V1TransferReversedEvent,
    V1TransferUpdatedEvent.LOOKUP_TYPE: V1TransferUpdatedEvent,
    V2BillingCadenceBilledEvent.LOOKUP_TYPE: V2BillingCadenceBilledEvent,
    V2BillingCadenceCanceledEvent.LOOKUP_TYPE: V2BillingCadenceCanceledEvent,
    V2BillingCadenceCreatedEvent.LOOKUP_TYPE: V2BillingCadenceCreatedEvent,
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
    V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent,
    V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent,
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
    V2CoreClaimableSandboxClaimedEvent.LOOKUP_TYPE: V2CoreClaimableSandboxClaimedEvent,
    V2CoreClaimableSandboxCreatedEvent.LOOKUP_TYPE: V2CoreClaimableSandboxCreatedEvent,
    V2CoreClaimableSandboxExpiredEvent.LOOKUP_TYPE: V2CoreClaimableSandboxExpiredEvent,
    V2CoreClaimableSandboxExpiringEvent.LOOKUP_TYPE: V2CoreClaimableSandboxExpiringEvent,
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent.LOOKUP_TYPE: V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent,
    V2CoreEventDestinationPingEvent.LOOKUP_TYPE: V2CoreEventDestinationPingEvent,
    V2CoreHealthApiErrorFiringEvent.LOOKUP_TYPE: V2CoreHealthApiErrorFiringEvent,
    V2CoreHealthApiErrorResolvedEvent.LOOKUP_TYPE: V2CoreHealthApiErrorResolvedEvent,
    V2CoreHealthApiLatencyFiringEvent.LOOKUP_TYPE: V2CoreHealthApiLatencyFiringEvent,
    V2CoreHealthApiLatencyResolvedEvent.LOOKUP_TYPE: V2CoreHealthApiLatencyResolvedEvent,
    V2CoreHealthAuthorizationRateDropFiringEvent.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropFiringEvent,
    V2CoreHealthAuthorizationRateDropResolvedEvent.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropResolvedEvent,
    V2CoreHealthEventGenerationFailureResolvedEvent.LOOKUP_TYPE: V2CoreHealthEventGenerationFailureResolvedEvent,
    V2CoreHealthFraudRateIncreasedEvent.LOOKUP_TYPE: V2CoreHealthFraudRateIncreasedEvent,
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent,
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent,
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
    V2MoneyManagementRecipientVerificationCreatedEvent.LOOKUP_TYPE: V2MoneyManagementRecipientVerificationCreatedEvent,
    V2MoneyManagementRecipientVerificationUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementRecipientVerificationUpdatedEvent,
    V2MoneyManagementTransactionCreatedEvent.LOOKUP_TYPE: V2MoneyManagementTransactionCreatedEvent,
    V2MoneyManagementTransactionUpdatedEvent.LOOKUP_TYPE: V2MoneyManagementTransactionUpdatedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent,
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent,
    V2PaymentsOffSessionPaymentCanceledEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCanceledEvent,
    V2PaymentsOffSessionPaymentCreatedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCreatedEvent,
    V2PaymentsOffSessionPaymentFailedEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentFailedEvent,
    V2PaymentsOffSessionPaymentRequiresCaptureEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentRequiresCaptureEvent,
    V2PaymentsOffSessionPaymentSucceededEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentSucceededEvent,
}

V2_EVENT_NOTIFICATION_CLASS_LOOKUP = {
    V1AccountUpdatedEventNotification.LOOKUP_TYPE: V1AccountUpdatedEventNotification,
    V1ApplicationFeeCreatedEventNotification.LOOKUP_TYPE: V1ApplicationFeeCreatedEventNotification,
    V1ApplicationFeeRefundedEventNotification.LOOKUP_TYPE: V1ApplicationFeeRefundedEventNotification,
    V1BillingMeterErrorReportTriggeredEventNotification.LOOKUP_TYPE: V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterNoMeterFoundEventNotification.LOOKUP_TYPE: V1BillingMeterNoMeterFoundEventNotification,
    V1BillingPortalConfigurationCreatedEventNotification.LOOKUP_TYPE: V1BillingPortalConfigurationCreatedEventNotification,
    V1BillingPortalConfigurationUpdatedEventNotification.LOOKUP_TYPE: V1BillingPortalConfigurationUpdatedEventNotification,
    V1CapabilityUpdatedEventNotification.LOOKUP_TYPE: V1CapabilityUpdatedEventNotification,
    V1ChargeCapturedEventNotification.LOOKUP_TYPE: V1ChargeCapturedEventNotification,
    V1ChargeDisputeClosedEventNotification.LOOKUP_TYPE: V1ChargeDisputeClosedEventNotification,
    V1ChargeDisputeCreatedEventNotification.LOOKUP_TYPE: V1ChargeDisputeCreatedEventNotification,
    V1ChargeDisputeFundsReinstatedEventNotification.LOOKUP_TYPE: V1ChargeDisputeFundsReinstatedEventNotification,
    V1ChargeDisputeFundsWithdrawnEventNotification.LOOKUP_TYPE: V1ChargeDisputeFundsWithdrawnEventNotification,
    V1ChargeDisputeUpdatedEventNotification.LOOKUP_TYPE: V1ChargeDisputeUpdatedEventNotification,
    V1ChargeExpiredEventNotification.LOOKUP_TYPE: V1ChargeExpiredEventNotification,
    V1ChargeFailedEventNotification.LOOKUP_TYPE: V1ChargeFailedEventNotification,
    V1ChargePendingEventNotification.LOOKUP_TYPE: V1ChargePendingEventNotification,
    V1ChargeRefundedEventNotification.LOOKUP_TYPE: V1ChargeRefundedEventNotification,
    V1ChargeRefundUpdatedEventNotification.LOOKUP_TYPE: V1ChargeRefundUpdatedEventNotification,
    V1ChargeSucceededEventNotification.LOOKUP_TYPE: V1ChargeSucceededEventNotification,
    V1ChargeUpdatedEventNotification.LOOKUP_TYPE: V1ChargeUpdatedEventNotification,
    V1CheckoutSessionAsyncPaymentFailedEventNotification.LOOKUP_TYPE: V1CheckoutSessionAsyncPaymentFailedEventNotification,
    V1CheckoutSessionAsyncPaymentSucceededEventNotification.LOOKUP_TYPE: V1CheckoutSessionAsyncPaymentSucceededEventNotification,
    V1CheckoutSessionCompletedEventNotification.LOOKUP_TYPE: V1CheckoutSessionCompletedEventNotification,
    V1CheckoutSessionExpiredEventNotification.LOOKUP_TYPE: V1CheckoutSessionExpiredEventNotification,
    V1ClimateOrderCanceledEventNotification.LOOKUP_TYPE: V1ClimateOrderCanceledEventNotification,
    V1ClimateOrderCreatedEventNotification.LOOKUP_TYPE: V1ClimateOrderCreatedEventNotification,
    V1ClimateOrderDelayedEventNotification.LOOKUP_TYPE: V1ClimateOrderDelayedEventNotification,
    V1ClimateOrderDeliveredEventNotification.LOOKUP_TYPE: V1ClimateOrderDeliveredEventNotification,
    V1ClimateOrderProductSubstitutedEventNotification.LOOKUP_TYPE: V1ClimateOrderProductSubstitutedEventNotification,
    V1ClimateProductCreatedEventNotification.LOOKUP_TYPE: V1ClimateProductCreatedEventNotification,
    V1ClimateProductPricingUpdatedEventNotification.LOOKUP_TYPE: V1ClimateProductPricingUpdatedEventNotification,
    V1CouponCreatedEventNotification.LOOKUP_TYPE: V1CouponCreatedEventNotification,
    V1CouponDeletedEventNotification.LOOKUP_TYPE: V1CouponDeletedEventNotification,
    V1CouponUpdatedEventNotification.LOOKUP_TYPE: V1CouponUpdatedEventNotification,
    V1CreditNoteCreatedEventNotification.LOOKUP_TYPE: V1CreditNoteCreatedEventNotification,
    V1CreditNoteUpdatedEventNotification.LOOKUP_TYPE: V1CreditNoteUpdatedEventNotification,
    V1CreditNoteVoidedEventNotification.LOOKUP_TYPE: V1CreditNoteVoidedEventNotification,
    V1CustomerCreatedEventNotification.LOOKUP_TYPE: V1CustomerCreatedEventNotification,
    V1CustomerDeletedEventNotification.LOOKUP_TYPE: V1CustomerDeletedEventNotification,
    V1CustomerSubscriptionCreatedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionCreatedEventNotification,
    V1CustomerSubscriptionDeletedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionDeletedEventNotification,
    V1CustomerSubscriptionPausedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionPausedEventNotification,
    V1CustomerSubscriptionPendingUpdateAppliedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionPendingUpdateAppliedEventNotification,
    V1CustomerSubscriptionPendingUpdateExpiredEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionPendingUpdateExpiredEventNotification,
    V1CustomerSubscriptionResumedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionResumedEventNotification,
    V1CustomerSubscriptionTrialWillEndEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionTrialWillEndEventNotification,
    V1CustomerSubscriptionUpdatedEventNotification.LOOKUP_TYPE: V1CustomerSubscriptionUpdatedEventNotification,
    V1CustomerTaxIdCreatedEventNotification.LOOKUP_TYPE: V1CustomerTaxIdCreatedEventNotification,
    V1CustomerTaxIdDeletedEventNotification.LOOKUP_TYPE: V1CustomerTaxIdDeletedEventNotification,
    V1CustomerTaxIdUpdatedEventNotification.LOOKUP_TYPE: V1CustomerTaxIdUpdatedEventNotification,
    V1CustomerUpdatedEventNotification.LOOKUP_TYPE: V1CustomerUpdatedEventNotification,
    V1FileCreatedEventNotification.LOOKUP_TYPE: V1FileCreatedEventNotification,
    V1FinancialConnectionsAccountCreatedEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountCreatedEventNotification,
    V1FinancialConnectionsAccountDeactivatedEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountDeactivatedEventNotification,
    V1FinancialConnectionsAccountDisconnectedEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountDisconnectedEventNotification,
    V1FinancialConnectionsAccountReactivatedEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountReactivatedEventNotification,
    V1FinancialConnectionsAccountRefreshedBalanceEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedBalanceEventNotification,
    V1FinancialConnectionsAccountRefreshedOwnershipEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedOwnershipEventNotification,
    V1FinancialConnectionsAccountRefreshedTransactionsEventNotification.LOOKUP_TYPE: V1FinancialConnectionsAccountRefreshedTransactionsEventNotification,
    V1IdentityVerificationSessionCanceledEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionCanceledEventNotification,
    V1IdentityVerificationSessionCreatedEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionCreatedEventNotification,
    V1IdentityVerificationSessionProcessingEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionProcessingEventNotification,
    V1IdentityVerificationSessionRedactedEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionRedactedEventNotification,
    V1IdentityVerificationSessionRequiresInputEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionRequiresInputEventNotification,
    V1IdentityVerificationSessionVerifiedEventNotification.LOOKUP_TYPE: V1IdentityVerificationSessionVerifiedEventNotification,
    V1InvoiceCreatedEventNotification.LOOKUP_TYPE: V1InvoiceCreatedEventNotification,
    V1InvoiceDeletedEventNotification.LOOKUP_TYPE: V1InvoiceDeletedEventNotification,
    V1InvoiceFinalizationFailedEventNotification.LOOKUP_TYPE: V1InvoiceFinalizationFailedEventNotification,
    V1InvoiceFinalizedEventNotification.LOOKUP_TYPE: V1InvoiceFinalizedEventNotification,
    V1InvoiceitemCreatedEventNotification.LOOKUP_TYPE: V1InvoiceitemCreatedEventNotification,
    V1InvoiceitemDeletedEventNotification.LOOKUP_TYPE: V1InvoiceitemDeletedEventNotification,
    V1InvoiceMarkedUncollectibleEventNotification.LOOKUP_TYPE: V1InvoiceMarkedUncollectibleEventNotification,
    V1InvoiceOverdueEventNotification.LOOKUP_TYPE: V1InvoiceOverdueEventNotification,
    V1InvoiceOverpaidEventNotification.LOOKUP_TYPE: V1InvoiceOverpaidEventNotification,
    V1InvoicePaidEventNotification.LOOKUP_TYPE: V1InvoicePaidEventNotification,
    V1InvoicePaymentActionRequiredEventNotification.LOOKUP_TYPE: V1InvoicePaymentActionRequiredEventNotification,
    V1InvoicePaymentFailedEventNotification.LOOKUP_TYPE: V1InvoicePaymentFailedEventNotification,
    V1InvoicePaymentPaidEventNotification.LOOKUP_TYPE: V1InvoicePaymentPaidEventNotification,
    V1InvoicePaymentSucceededEventNotification.LOOKUP_TYPE: V1InvoicePaymentSucceededEventNotification,
    V1InvoiceSentEventNotification.LOOKUP_TYPE: V1InvoiceSentEventNotification,
    V1InvoiceUpcomingEventNotification.LOOKUP_TYPE: V1InvoiceUpcomingEventNotification,
    V1InvoiceUpdatedEventNotification.LOOKUP_TYPE: V1InvoiceUpdatedEventNotification,
    V1InvoiceVoidedEventNotification.LOOKUP_TYPE: V1InvoiceVoidedEventNotification,
    V1InvoiceWillBeDueEventNotification.LOOKUP_TYPE: V1InvoiceWillBeDueEventNotification,
    V1IssuingAuthorizationCreatedEventNotification.LOOKUP_TYPE: V1IssuingAuthorizationCreatedEventNotification,
    V1IssuingAuthorizationRequestEventNotification.LOOKUP_TYPE: V1IssuingAuthorizationRequestEventNotification,
    V1IssuingAuthorizationUpdatedEventNotification.LOOKUP_TYPE: V1IssuingAuthorizationUpdatedEventNotification,
    V1IssuingCardCreatedEventNotification.LOOKUP_TYPE: V1IssuingCardCreatedEventNotification,
    V1IssuingCardholderCreatedEventNotification.LOOKUP_TYPE: V1IssuingCardholderCreatedEventNotification,
    V1IssuingCardholderUpdatedEventNotification.LOOKUP_TYPE: V1IssuingCardholderUpdatedEventNotification,
    V1IssuingCardUpdatedEventNotification.LOOKUP_TYPE: V1IssuingCardUpdatedEventNotification,
    V1IssuingDisputeClosedEventNotification.LOOKUP_TYPE: V1IssuingDisputeClosedEventNotification,
    V1IssuingDisputeCreatedEventNotification.LOOKUP_TYPE: V1IssuingDisputeCreatedEventNotification,
    V1IssuingDisputeFundsReinstatedEventNotification.LOOKUP_TYPE: V1IssuingDisputeFundsReinstatedEventNotification,
    V1IssuingDisputeFundsRescindedEventNotification.LOOKUP_TYPE: V1IssuingDisputeFundsRescindedEventNotification,
    V1IssuingDisputeSubmittedEventNotification.LOOKUP_TYPE: V1IssuingDisputeSubmittedEventNotification,
    V1IssuingDisputeUpdatedEventNotification.LOOKUP_TYPE: V1IssuingDisputeUpdatedEventNotification,
    V1IssuingPersonalizationDesignActivatedEventNotification.LOOKUP_TYPE: V1IssuingPersonalizationDesignActivatedEventNotification,
    V1IssuingPersonalizationDesignDeactivatedEventNotification.LOOKUP_TYPE: V1IssuingPersonalizationDesignDeactivatedEventNotification,
    V1IssuingPersonalizationDesignRejectedEventNotification.LOOKUP_TYPE: V1IssuingPersonalizationDesignRejectedEventNotification,
    V1IssuingPersonalizationDesignUpdatedEventNotification.LOOKUP_TYPE: V1IssuingPersonalizationDesignUpdatedEventNotification,
    V1IssuingTokenCreatedEventNotification.LOOKUP_TYPE: V1IssuingTokenCreatedEventNotification,
    V1IssuingTokenUpdatedEventNotification.LOOKUP_TYPE: V1IssuingTokenUpdatedEventNotification,
    V1IssuingTransactionCreatedEventNotification.LOOKUP_TYPE: V1IssuingTransactionCreatedEventNotification,
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification.LOOKUP_TYPE: V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification,
    V1IssuingTransactionUpdatedEventNotification.LOOKUP_TYPE: V1IssuingTransactionUpdatedEventNotification,
    V1MandateUpdatedEventNotification.LOOKUP_TYPE: V1MandateUpdatedEventNotification,
    V1PaymentIntentAmountCapturableUpdatedEventNotification.LOOKUP_TYPE: V1PaymentIntentAmountCapturableUpdatedEventNotification,
    V1PaymentIntentCanceledEventNotification.LOOKUP_TYPE: V1PaymentIntentCanceledEventNotification,
    V1PaymentIntentCreatedEventNotification.LOOKUP_TYPE: V1PaymentIntentCreatedEventNotification,
    V1PaymentIntentPartiallyFundedEventNotification.LOOKUP_TYPE: V1PaymentIntentPartiallyFundedEventNotification,
    V1PaymentIntentPaymentFailedEventNotification.LOOKUP_TYPE: V1PaymentIntentPaymentFailedEventNotification,
    V1PaymentIntentProcessingEventNotification.LOOKUP_TYPE: V1PaymentIntentProcessingEventNotification,
    V1PaymentIntentRequiresActionEventNotification.LOOKUP_TYPE: V1PaymentIntentRequiresActionEventNotification,
    V1PaymentIntentSucceededEventNotification.LOOKUP_TYPE: V1PaymentIntentSucceededEventNotification,
    V1PaymentLinkCreatedEventNotification.LOOKUP_TYPE: V1PaymentLinkCreatedEventNotification,
    V1PaymentLinkUpdatedEventNotification.LOOKUP_TYPE: V1PaymentLinkUpdatedEventNotification,
    V1PaymentMethodAttachedEventNotification.LOOKUP_TYPE: V1PaymentMethodAttachedEventNotification,
    V1PaymentMethodAutomaticallyUpdatedEventNotification.LOOKUP_TYPE: V1PaymentMethodAutomaticallyUpdatedEventNotification,
    V1PaymentMethodDetachedEventNotification.LOOKUP_TYPE: V1PaymentMethodDetachedEventNotification,
    V1PaymentMethodUpdatedEventNotification.LOOKUP_TYPE: V1PaymentMethodUpdatedEventNotification,
    V1PayoutCanceledEventNotification.LOOKUP_TYPE: V1PayoutCanceledEventNotification,
    V1PayoutCreatedEventNotification.LOOKUP_TYPE: V1PayoutCreatedEventNotification,
    V1PayoutFailedEventNotification.LOOKUP_TYPE: V1PayoutFailedEventNotification,
    V1PayoutPaidEventNotification.LOOKUP_TYPE: V1PayoutPaidEventNotification,
    V1PayoutReconciliationCompletedEventNotification.LOOKUP_TYPE: V1PayoutReconciliationCompletedEventNotification,
    V1PayoutUpdatedEventNotification.LOOKUP_TYPE: V1PayoutUpdatedEventNotification,
    V1PersonCreatedEventNotification.LOOKUP_TYPE: V1PersonCreatedEventNotification,
    V1PersonDeletedEventNotification.LOOKUP_TYPE: V1PersonDeletedEventNotification,
    V1PersonUpdatedEventNotification.LOOKUP_TYPE: V1PersonUpdatedEventNotification,
    V1PlanCreatedEventNotification.LOOKUP_TYPE: V1PlanCreatedEventNotification,
    V1PlanDeletedEventNotification.LOOKUP_TYPE: V1PlanDeletedEventNotification,
    V1PlanUpdatedEventNotification.LOOKUP_TYPE: V1PlanUpdatedEventNotification,
    V1PriceCreatedEventNotification.LOOKUP_TYPE: V1PriceCreatedEventNotification,
    V1PriceDeletedEventNotification.LOOKUP_TYPE: V1PriceDeletedEventNotification,
    V1PriceUpdatedEventNotification.LOOKUP_TYPE: V1PriceUpdatedEventNotification,
    V1ProductCreatedEventNotification.LOOKUP_TYPE: V1ProductCreatedEventNotification,
    V1ProductDeletedEventNotification.LOOKUP_TYPE: V1ProductDeletedEventNotification,
    V1ProductUpdatedEventNotification.LOOKUP_TYPE: V1ProductUpdatedEventNotification,
    V1PromotionCodeCreatedEventNotification.LOOKUP_TYPE: V1PromotionCodeCreatedEventNotification,
    V1PromotionCodeUpdatedEventNotification.LOOKUP_TYPE: V1PromotionCodeUpdatedEventNotification,
    V1QuoteAcceptedEventNotification.LOOKUP_TYPE: V1QuoteAcceptedEventNotification,
    V1QuoteCanceledEventNotification.LOOKUP_TYPE: V1QuoteCanceledEventNotification,
    V1QuoteCreatedEventNotification.LOOKUP_TYPE: V1QuoteCreatedEventNotification,
    V1QuoteFinalizedEventNotification.LOOKUP_TYPE: V1QuoteFinalizedEventNotification,
    V1RadarEarlyFraudWarningCreatedEventNotification.LOOKUP_TYPE: V1RadarEarlyFraudWarningCreatedEventNotification,
    V1RadarEarlyFraudWarningUpdatedEventNotification.LOOKUP_TYPE: V1RadarEarlyFraudWarningUpdatedEventNotification,
    V1RefundCreatedEventNotification.LOOKUP_TYPE: V1RefundCreatedEventNotification,
    V1RefundFailedEventNotification.LOOKUP_TYPE: V1RefundFailedEventNotification,
    V1RefundUpdatedEventNotification.LOOKUP_TYPE: V1RefundUpdatedEventNotification,
    V1ReviewClosedEventNotification.LOOKUP_TYPE: V1ReviewClosedEventNotification,
    V1ReviewOpenedEventNotification.LOOKUP_TYPE: V1ReviewOpenedEventNotification,
    V1SetupIntentCanceledEventNotification.LOOKUP_TYPE: V1SetupIntentCanceledEventNotification,
    V1SetupIntentCreatedEventNotification.LOOKUP_TYPE: V1SetupIntentCreatedEventNotification,
    V1SetupIntentRequiresActionEventNotification.LOOKUP_TYPE: V1SetupIntentRequiresActionEventNotification,
    V1SetupIntentSetupFailedEventNotification.LOOKUP_TYPE: V1SetupIntentSetupFailedEventNotification,
    V1SetupIntentSucceededEventNotification.LOOKUP_TYPE: V1SetupIntentSucceededEventNotification,
    V1SigmaScheduledQueryRunCreatedEventNotification.LOOKUP_TYPE: V1SigmaScheduledQueryRunCreatedEventNotification,
    V1SourceCanceledEventNotification.LOOKUP_TYPE: V1SourceCanceledEventNotification,
    V1SourceChargeableEventNotification.LOOKUP_TYPE: V1SourceChargeableEventNotification,
    V1SourceFailedEventNotification.LOOKUP_TYPE: V1SourceFailedEventNotification,
    V1SourceRefundAttributesRequiredEventNotification.LOOKUP_TYPE: V1SourceRefundAttributesRequiredEventNotification,
    V1SubscriptionScheduleAbortedEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleAbortedEventNotification,
    V1SubscriptionScheduleCanceledEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleCanceledEventNotification,
    V1SubscriptionScheduleCompletedEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleCompletedEventNotification,
    V1SubscriptionScheduleCreatedEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleCreatedEventNotification,
    V1SubscriptionScheduleExpiringEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleExpiringEventNotification,
    V1SubscriptionScheduleReleasedEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleReleasedEventNotification,
    V1SubscriptionScheduleUpdatedEventNotification.LOOKUP_TYPE: V1SubscriptionScheduleUpdatedEventNotification,
    V1TaxRateCreatedEventNotification.LOOKUP_TYPE: V1TaxRateCreatedEventNotification,
    V1TaxRateUpdatedEventNotification.LOOKUP_TYPE: V1TaxRateUpdatedEventNotification,
    V1TerminalReaderActionFailedEventNotification.LOOKUP_TYPE: V1TerminalReaderActionFailedEventNotification,
    V1TerminalReaderActionSucceededEventNotification.LOOKUP_TYPE: V1TerminalReaderActionSucceededEventNotification,
    V1TerminalReaderActionUpdatedEventNotification.LOOKUP_TYPE: V1TerminalReaderActionUpdatedEventNotification,
    V1TestHelpersTestClockAdvancingEventNotification.LOOKUP_TYPE: V1TestHelpersTestClockAdvancingEventNotification,
    V1TestHelpersTestClockCreatedEventNotification.LOOKUP_TYPE: V1TestHelpersTestClockCreatedEventNotification,
    V1TestHelpersTestClockDeletedEventNotification.LOOKUP_TYPE: V1TestHelpersTestClockDeletedEventNotification,
    V1TestHelpersTestClockInternalFailureEventNotification.LOOKUP_TYPE: V1TestHelpersTestClockInternalFailureEventNotification,
    V1TestHelpersTestClockReadyEventNotification.LOOKUP_TYPE: V1TestHelpersTestClockReadyEventNotification,
    V1TopupCanceledEventNotification.LOOKUP_TYPE: V1TopupCanceledEventNotification,
    V1TopupCreatedEventNotification.LOOKUP_TYPE: V1TopupCreatedEventNotification,
    V1TopupFailedEventNotification.LOOKUP_TYPE: V1TopupFailedEventNotification,
    V1TopupReversedEventNotification.LOOKUP_TYPE: V1TopupReversedEventNotification,
    V1TopupSucceededEventNotification.LOOKUP_TYPE: V1TopupSucceededEventNotification,
    V1TransferCreatedEventNotification.LOOKUP_TYPE: V1TransferCreatedEventNotification,
    V1TransferReversedEventNotification.LOOKUP_TYPE: V1TransferReversedEventNotification,
    V1TransferUpdatedEventNotification.LOOKUP_TYPE: V1TransferUpdatedEventNotification,
    V2BillingCadenceBilledEventNotification.LOOKUP_TYPE: V2BillingCadenceBilledEventNotification,
    V2BillingCadenceCanceledEventNotification.LOOKUP_TYPE: V2BillingCadenceCanceledEventNotification,
    V2BillingCadenceCreatedEventNotification.LOOKUP_TYPE: V2BillingCadenceCreatedEventNotification,
    V2BillingLicensedItemCreatedEventNotification.LOOKUP_TYPE: V2BillingLicensedItemCreatedEventNotification,
    V2BillingLicensedItemUpdatedEventNotification.LOOKUP_TYPE: V2BillingLicensedItemUpdatedEventNotification,
    V2BillingLicenseFeeCreatedEventNotification.LOOKUP_TYPE: V2BillingLicenseFeeCreatedEventNotification,
    V2BillingLicenseFeeUpdatedEventNotification.LOOKUP_TYPE: V2BillingLicenseFeeUpdatedEventNotification,
    V2BillingLicenseFeeVersionCreatedEventNotification.LOOKUP_TYPE: V2BillingLicenseFeeVersionCreatedEventNotification,
    V2BillingMeteredItemCreatedEventNotification.LOOKUP_TYPE: V2BillingMeteredItemCreatedEventNotification,
    V2BillingMeteredItemUpdatedEventNotification.LOOKUP_TYPE: V2BillingMeteredItemUpdatedEventNotification,
    V2BillingPricingPlanComponentCreatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanComponentCreatedEventNotification,
    V2BillingPricingPlanComponentUpdatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanComponentUpdatedEventNotification,
    V2BillingPricingPlanCreatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanCreatedEventNotification,
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification,
    V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification,
    V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification,
    V2BillingPricingPlanSubscriptionCollectionPausedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionPausedEventNotification,
    V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification,
    V2BillingPricingPlanSubscriptionServicingActivatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingActivatedEventNotification,
    V2BillingPricingPlanSubscriptionServicingCanceledEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingCanceledEventNotification,
    V2BillingPricingPlanSubscriptionServicingPausedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanSubscriptionServicingPausedEventNotification,
    V2BillingPricingPlanUpdatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanUpdatedEventNotification,
    V2BillingPricingPlanVersionCreatedEventNotification.LOOKUP_TYPE: V2BillingPricingPlanVersionCreatedEventNotification,
    V2BillingRateCardCreatedEventNotification.LOOKUP_TYPE: V2BillingRateCardCreatedEventNotification,
    V2BillingRateCardRateCreatedEventNotification.LOOKUP_TYPE: V2BillingRateCardRateCreatedEventNotification,
    V2BillingRateCardSubscriptionActivatedEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionActivatedEventNotification,
    V2BillingRateCardSubscriptionCanceledEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCanceledEventNotification,
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification,
    V2BillingRateCardSubscriptionCollectionCurrentEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionCurrentEventNotification,
    V2BillingRateCardSubscriptionCollectionPastDueEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionPastDueEventNotification,
    V2BillingRateCardSubscriptionCollectionPausedEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionPausedEventNotification,
    V2BillingRateCardSubscriptionCollectionUnpaidEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionCollectionUnpaidEventNotification,
    V2BillingRateCardSubscriptionServicingActivatedEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingActivatedEventNotification,
    V2BillingRateCardSubscriptionServicingCanceledEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingCanceledEventNotification,
    V2BillingRateCardSubscriptionServicingPausedEventNotification.LOOKUP_TYPE: V2BillingRateCardSubscriptionServicingPausedEventNotification,
    V2BillingRateCardUpdatedEventNotification.LOOKUP_TYPE: V2BillingRateCardUpdatedEventNotification,
    V2BillingRateCardVersionCreatedEventNotification.LOOKUP_TYPE: V2BillingRateCardVersionCreatedEventNotification,
    V2CoreAccountClosedEventNotification.LOOKUP_TYPE: V2CoreAccountClosedEventNotification,
    V2CoreAccountCreatedEventNotification.LOOKUP_TYPE: V2CoreAccountCreatedEventNotification,
    V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    V2CoreAccountIncludingDefaultsUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    V2CoreAccountIncludingIdentityUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingIdentityUpdatedEventNotification,
    V2CoreAccountIncludingRequirementsUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    V2CoreAccountLinkReturnedEventNotification.LOOKUP_TYPE: V2CoreAccountLinkReturnedEventNotification,
    V2CoreAccountPersonCreatedEventNotification.LOOKUP_TYPE: V2CoreAccountPersonCreatedEventNotification,
    V2CoreAccountPersonDeletedEventNotification.LOOKUP_TYPE: V2CoreAccountPersonDeletedEventNotification,
    V2CoreAccountPersonUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountPersonUpdatedEventNotification,
    V2CoreAccountUpdatedEventNotification.LOOKUP_TYPE: V2CoreAccountUpdatedEventNotification,
    V2CoreClaimableSandboxClaimedEventNotification.LOOKUP_TYPE: V2CoreClaimableSandboxClaimedEventNotification,
    V2CoreClaimableSandboxCreatedEventNotification.LOOKUP_TYPE: V2CoreClaimableSandboxCreatedEventNotification,
    V2CoreClaimableSandboxExpiredEventNotification.LOOKUP_TYPE: V2CoreClaimableSandboxExpiredEventNotification,
    V2CoreClaimableSandboxExpiringEventNotification.LOOKUP_TYPE: V2CoreClaimableSandboxExpiringEventNotification,
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification.LOOKUP_TYPE: V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification,
    V2CoreEventDestinationPingEventNotification.LOOKUP_TYPE: V2CoreEventDestinationPingEventNotification,
    V2CoreHealthApiErrorFiringEventNotification.LOOKUP_TYPE: V2CoreHealthApiErrorFiringEventNotification,
    V2CoreHealthApiErrorResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthApiErrorResolvedEventNotification,
    V2CoreHealthApiLatencyFiringEventNotification.LOOKUP_TYPE: V2CoreHealthApiLatencyFiringEventNotification,
    V2CoreHealthApiLatencyResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthApiLatencyResolvedEventNotification,
    V2CoreHealthAuthorizationRateDropFiringEventNotification.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropFiringEventNotification,
    V2CoreHealthAuthorizationRateDropResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthAuthorizationRateDropResolvedEventNotification,
    V2CoreHealthEventGenerationFailureResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthEventGenerationFailureResolvedEventNotification,
    V2CoreHealthFraudRateIncreasedEventNotification.LOOKUP_TYPE: V2CoreHealthFraudRateIncreasedEventNotification,
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification,
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification,
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification,
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification,
    V2CoreHealthPaymentMethodErrorFiringEventNotification.LOOKUP_TYPE: V2CoreHealthPaymentMethodErrorFiringEventNotification,
    V2CoreHealthPaymentMethodErrorResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthPaymentMethodErrorResolvedEventNotification,
    V2CoreHealthTrafficVolumeDropFiringEventNotification.LOOKUP_TYPE: V2CoreHealthTrafficVolumeDropFiringEventNotification,
    V2CoreHealthTrafficVolumeDropResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthTrafficVolumeDropResolvedEventNotification,
    V2CoreHealthWebhookLatencyFiringEventNotification.LOOKUP_TYPE: V2CoreHealthWebhookLatencyFiringEventNotification,
    V2CoreHealthWebhookLatencyResolvedEventNotification.LOOKUP_TYPE: V2CoreHealthWebhookLatencyResolvedEventNotification,
    V2MoneyManagementAdjustmentCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementAdjustmentCreatedEventNotification,
    V2MoneyManagementFinancialAccountCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementFinancialAccountCreatedEventNotification,
    V2MoneyManagementFinancialAccountUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementFinancialAccountUpdatedEventNotification,
    V2MoneyManagementFinancialAddressActivatedEventNotification.LOOKUP_TYPE: V2MoneyManagementFinancialAddressActivatedEventNotification,
    V2MoneyManagementFinancialAddressFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementFinancialAddressFailedEventNotification,
    V2MoneyManagementInboundTransferAvailableEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferAvailableEventNotification,
    V2MoneyManagementInboundTransferBankDebitFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    V2MoneyManagementInboundTransferBankDebitProcessingEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    V2MoneyManagementInboundTransferBankDebitQueuedEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    V2MoneyManagementInboundTransferBankDebitReturnedEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    V2MoneyManagementInboundTransferBankDebitSucceededEventNotification.LOOKUP_TYPE: V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    V2MoneyManagementOutboundPaymentCanceledEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentCanceledEventNotification,
    V2MoneyManagementOutboundPaymentCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentCreatedEventNotification,
    V2MoneyManagementOutboundPaymentFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentFailedEventNotification,
    V2MoneyManagementOutboundPaymentPostedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentPostedEventNotification,
    V2MoneyManagementOutboundPaymentReturnedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentReturnedEventNotification,
    V2MoneyManagementOutboundPaymentUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    V2MoneyManagementOutboundTransferCanceledEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferCanceledEventNotification,
    V2MoneyManagementOutboundTransferCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferCreatedEventNotification,
    V2MoneyManagementOutboundTransferFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferFailedEventNotification,
    V2MoneyManagementOutboundTransferPostedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferPostedEventNotification,
    V2MoneyManagementOutboundTransferReturnedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferReturnedEventNotification,
    V2MoneyManagementOutboundTransferUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementOutboundTransferUpdatedEventNotification,
    V2MoneyManagementPayoutMethodUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementPayoutMethodUpdatedEventNotification,
    V2MoneyManagementReceivedCreditAvailableEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedCreditAvailableEventNotification,
    V2MoneyManagementReceivedCreditFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedCreditFailedEventNotification,
    V2MoneyManagementReceivedCreditReturnedEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedCreditReturnedEventNotification,
    V2MoneyManagementReceivedCreditSucceededEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedCreditSucceededEventNotification,
    V2MoneyManagementReceivedDebitCanceledEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedDebitCanceledEventNotification,
    V2MoneyManagementReceivedDebitFailedEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedDebitFailedEventNotification,
    V2MoneyManagementReceivedDebitPendingEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedDebitPendingEventNotification,
    V2MoneyManagementReceivedDebitSucceededEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedDebitSucceededEventNotification,
    V2MoneyManagementReceivedDebitUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementReceivedDebitUpdatedEventNotification,
    V2MoneyManagementRecipientVerificationCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementRecipientVerificationCreatedEventNotification,
    V2MoneyManagementRecipientVerificationUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementRecipientVerificationUpdatedEventNotification,
    V2MoneyManagementTransactionCreatedEventNotification.LOOKUP_TYPE: V2MoneyManagementTransactionCreatedEventNotification,
    V2MoneyManagementTransactionUpdatedEventNotification.LOOKUP_TYPE: V2MoneyManagementTransactionUpdatedEventNotification,
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
    V2PaymentsOffSessionPaymentCanceledEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCanceledEventNotification,
    V2PaymentsOffSessionPaymentCreatedEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentCreatedEventNotification,
    V2PaymentsOffSessionPaymentFailedEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentFailedEventNotification,
    V2PaymentsOffSessionPaymentRequiresCaptureEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    V2PaymentsOffSessionPaymentSucceededEventNotification.LOOKUP_TYPE: V2PaymentsOffSessionPaymentSucceededEventNotification,
}

ALL_EVENT_NOTIFICATIONS = Union[
    V1AccountUpdatedEventNotification,
    V1ApplicationFeeCreatedEventNotification,
    V1ApplicationFeeRefundedEventNotification,
    V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterNoMeterFoundEventNotification,
    V1BillingPortalConfigurationCreatedEventNotification,
    V1BillingPortalConfigurationUpdatedEventNotification,
    V1CapabilityUpdatedEventNotification,
    V1ChargeCapturedEventNotification,
    V1ChargeDisputeClosedEventNotification,
    V1ChargeDisputeCreatedEventNotification,
    V1ChargeDisputeFundsReinstatedEventNotification,
    V1ChargeDisputeFundsWithdrawnEventNotification,
    V1ChargeDisputeUpdatedEventNotification,
    V1ChargeExpiredEventNotification,
    V1ChargeFailedEventNotification,
    V1ChargePendingEventNotification,
    V1ChargeRefundedEventNotification,
    V1ChargeRefundUpdatedEventNotification,
    V1ChargeSucceededEventNotification,
    V1ChargeUpdatedEventNotification,
    V1CheckoutSessionAsyncPaymentFailedEventNotification,
    V1CheckoutSessionAsyncPaymentSucceededEventNotification,
    V1CheckoutSessionCompletedEventNotification,
    V1CheckoutSessionExpiredEventNotification,
    V1ClimateOrderCanceledEventNotification,
    V1ClimateOrderCreatedEventNotification,
    V1ClimateOrderDelayedEventNotification,
    V1ClimateOrderDeliveredEventNotification,
    V1ClimateOrderProductSubstitutedEventNotification,
    V1ClimateProductCreatedEventNotification,
    V1ClimateProductPricingUpdatedEventNotification,
    V1CouponCreatedEventNotification,
    V1CouponDeletedEventNotification,
    V1CouponUpdatedEventNotification,
    V1CreditNoteCreatedEventNotification,
    V1CreditNoteUpdatedEventNotification,
    V1CreditNoteVoidedEventNotification,
    V1CustomerCreatedEventNotification,
    V1CustomerDeletedEventNotification,
    V1CustomerSubscriptionCreatedEventNotification,
    V1CustomerSubscriptionDeletedEventNotification,
    V1CustomerSubscriptionPausedEventNotification,
    V1CustomerSubscriptionPendingUpdateAppliedEventNotification,
    V1CustomerSubscriptionPendingUpdateExpiredEventNotification,
    V1CustomerSubscriptionResumedEventNotification,
    V1CustomerSubscriptionTrialWillEndEventNotification,
    V1CustomerSubscriptionUpdatedEventNotification,
    V1CustomerTaxIdCreatedEventNotification,
    V1CustomerTaxIdDeletedEventNotification,
    V1CustomerTaxIdUpdatedEventNotification,
    V1CustomerUpdatedEventNotification,
    V1FileCreatedEventNotification,
    V1FinancialConnectionsAccountCreatedEventNotification,
    V1FinancialConnectionsAccountDeactivatedEventNotification,
    V1FinancialConnectionsAccountDisconnectedEventNotification,
    V1FinancialConnectionsAccountReactivatedEventNotification,
    V1FinancialConnectionsAccountRefreshedBalanceEventNotification,
    V1FinancialConnectionsAccountRefreshedOwnershipEventNotification,
    V1FinancialConnectionsAccountRefreshedTransactionsEventNotification,
    V1IdentityVerificationSessionCanceledEventNotification,
    V1IdentityVerificationSessionCreatedEventNotification,
    V1IdentityVerificationSessionProcessingEventNotification,
    V1IdentityVerificationSessionRedactedEventNotification,
    V1IdentityVerificationSessionRequiresInputEventNotification,
    V1IdentityVerificationSessionVerifiedEventNotification,
    V1InvoiceCreatedEventNotification,
    V1InvoiceDeletedEventNotification,
    V1InvoiceFinalizationFailedEventNotification,
    V1InvoiceFinalizedEventNotification,
    V1InvoiceitemCreatedEventNotification,
    V1InvoiceitemDeletedEventNotification,
    V1InvoiceMarkedUncollectibleEventNotification,
    V1InvoiceOverdueEventNotification,
    V1InvoiceOverpaidEventNotification,
    V1InvoicePaidEventNotification,
    V1InvoicePaymentActionRequiredEventNotification,
    V1InvoicePaymentFailedEventNotification,
    V1InvoicePaymentPaidEventNotification,
    V1InvoicePaymentSucceededEventNotification,
    V1InvoiceSentEventNotification,
    V1InvoiceUpcomingEventNotification,
    V1InvoiceUpdatedEventNotification,
    V1InvoiceVoidedEventNotification,
    V1InvoiceWillBeDueEventNotification,
    V1IssuingAuthorizationCreatedEventNotification,
    V1IssuingAuthorizationRequestEventNotification,
    V1IssuingAuthorizationUpdatedEventNotification,
    V1IssuingCardCreatedEventNotification,
    V1IssuingCardholderCreatedEventNotification,
    V1IssuingCardholderUpdatedEventNotification,
    V1IssuingCardUpdatedEventNotification,
    V1IssuingDisputeClosedEventNotification,
    V1IssuingDisputeCreatedEventNotification,
    V1IssuingDisputeFundsReinstatedEventNotification,
    V1IssuingDisputeFundsRescindedEventNotification,
    V1IssuingDisputeSubmittedEventNotification,
    V1IssuingDisputeUpdatedEventNotification,
    V1IssuingPersonalizationDesignActivatedEventNotification,
    V1IssuingPersonalizationDesignDeactivatedEventNotification,
    V1IssuingPersonalizationDesignRejectedEventNotification,
    V1IssuingPersonalizationDesignUpdatedEventNotification,
    V1IssuingTokenCreatedEventNotification,
    V1IssuingTokenUpdatedEventNotification,
    V1IssuingTransactionCreatedEventNotification,
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification,
    V1IssuingTransactionUpdatedEventNotification,
    V1MandateUpdatedEventNotification,
    V1PaymentIntentAmountCapturableUpdatedEventNotification,
    V1PaymentIntentCanceledEventNotification,
    V1PaymentIntentCreatedEventNotification,
    V1PaymentIntentPartiallyFundedEventNotification,
    V1PaymentIntentPaymentFailedEventNotification,
    V1PaymentIntentProcessingEventNotification,
    V1PaymentIntentRequiresActionEventNotification,
    V1PaymentIntentSucceededEventNotification,
    V1PaymentLinkCreatedEventNotification,
    V1PaymentLinkUpdatedEventNotification,
    V1PaymentMethodAttachedEventNotification,
    V1PaymentMethodAutomaticallyUpdatedEventNotification,
    V1PaymentMethodDetachedEventNotification,
    V1PaymentMethodUpdatedEventNotification,
    V1PayoutCanceledEventNotification,
    V1PayoutCreatedEventNotification,
    V1PayoutFailedEventNotification,
    V1PayoutPaidEventNotification,
    V1PayoutReconciliationCompletedEventNotification,
    V1PayoutUpdatedEventNotification,
    V1PersonCreatedEventNotification,
    V1PersonDeletedEventNotification,
    V1PersonUpdatedEventNotification,
    V1PlanCreatedEventNotification,
    V1PlanDeletedEventNotification,
    V1PlanUpdatedEventNotification,
    V1PriceCreatedEventNotification,
    V1PriceDeletedEventNotification,
    V1PriceUpdatedEventNotification,
    V1ProductCreatedEventNotification,
    V1ProductDeletedEventNotification,
    V1ProductUpdatedEventNotification,
    V1PromotionCodeCreatedEventNotification,
    V1PromotionCodeUpdatedEventNotification,
    V1QuoteAcceptedEventNotification,
    V1QuoteCanceledEventNotification,
    V1QuoteCreatedEventNotification,
    V1QuoteFinalizedEventNotification,
    V1RadarEarlyFraudWarningCreatedEventNotification,
    V1RadarEarlyFraudWarningUpdatedEventNotification,
    V1RefundCreatedEventNotification,
    V1RefundFailedEventNotification,
    V1RefundUpdatedEventNotification,
    V1ReviewClosedEventNotification,
    V1ReviewOpenedEventNotification,
    V1SetupIntentCanceledEventNotification,
    V1SetupIntentCreatedEventNotification,
    V1SetupIntentRequiresActionEventNotification,
    V1SetupIntentSetupFailedEventNotification,
    V1SetupIntentSucceededEventNotification,
    V1SigmaScheduledQueryRunCreatedEventNotification,
    V1SourceCanceledEventNotification,
    V1SourceChargeableEventNotification,
    V1SourceFailedEventNotification,
    V1SourceRefundAttributesRequiredEventNotification,
    V1SubscriptionScheduleAbortedEventNotification,
    V1SubscriptionScheduleCanceledEventNotification,
    V1SubscriptionScheduleCompletedEventNotification,
    V1SubscriptionScheduleCreatedEventNotification,
    V1SubscriptionScheduleExpiringEventNotification,
    V1SubscriptionScheduleReleasedEventNotification,
    V1SubscriptionScheduleUpdatedEventNotification,
    V1TaxRateCreatedEventNotification,
    V1TaxRateUpdatedEventNotification,
    V1TerminalReaderActionFailedEventNotification,
    V1TerminalReaderActionSucceededEventNotification,
    V1TerminalReaderActionUpdatedEventNotification,
    V1TestHelpersTestClockAdvancingEventNotification,
    V1TestHelpersTestClockCreatedEventNotification,
    V1TestHelpersTestClockDeletedEventNotification,
    V1TestHelpersTestClockInternalFailureEventNotification,
    V1TestHelpersTestClockReadyEventNotification,
    V1TopupCanceledEventNotification,
    V1TopupCreatedEventNotification,
    V1TopupFailedEventNotification,
    V1TopupReversedEventNotification,
    V1TopupSucceededEventNotification,
    V1TransferCreatedEventNotification,
    V1TransferReversedEventNotification,
    V1TransferUpdatedEventNotification,
    V2BillingCadenceBilledEventNotification,
    V2BillingCadenceCanceledEventNotification,
    V2BillingCadenceCreatedEventNotification,
    V2BillingLicensedItemCreatedEventNotification,
    V2BillingLicensedItemUpdatedEventNotification,
    V2BillingLicenseFeeCreatedEventNotification,
    V2BillingLicenseFeeUpdatedEventNotification,
    V2BillingLicenseFeeVersionCreatedEventNotification,
    V2BillingMeteredItemCreatedEventNotification,
    V2BillingMeteredItemUpdatedEventNotification,
    V2BillingPricingPlanComponentCreatedEventNotification,
    V2BillingPricingPlanComponentUpdatedEventNotification,
    V2BillingPricingPlanCreatedEventNotification,
    V2BillingPricingPlanSubscriptionCollectionAwaitingCustomerActionEventNotification,
    V2BillingPricingPlanSubscriptionCollectionCurrentEventNotification,
    V2BillingPricingPlanSubscriptionCollectionPastDueEventNotification,
    V2BillingPricingPlanSubscriptionCollectionPausedEventNotification,
    V2BillingPricingPlanSubscriptionCollectionUnpaidEventNotification,
    V2BillingPricingPlanSubscriptionServicingActivatedEventNotification,
    V2BillingPricingPlanSubscriptionServicingCanceledEventNotification,
    V2BillingPricingPlanSubscriptionServicingPausedEventNotification,
    V2BillingPricingPlanUpdatedEventNotification,
    V2BillingPricingPlanVersionCreatedEventNotification,
    V2BillingRateCardCreatedEventNotification,
    V2BillingRateCardRateCreatedEventNotification,
    V2BillingRateCardSubscriptionActivatedEventNotification,
    V2BillingRateCardSubscriptionCanceledEventNotification,
    V2BillingRateCardSubscriptionCollectionAwaitingCustomerActionEventNotification,
    V2BillingRateCardSubscriptionCollectionCurrentEventNotification,
    V2BillingRateCardSubscriptionCollectionPastDueEventNotification,
    V2BillingRateCardSubscriptionCollectionPausedEventNotification,
    V2BillingRateCardSubscriptionCollectionUnpaidEventNotification,
    V2BillingRateCardSubscriptionServicingActivatedEventNotification,
    V2BillingRateCardSubscriptionServicingCanceledEventNotification,
    V2BillingRateCardSubscriptionServicingPausedEventNotification,
    V2BillingRateCardUpdatedEventNotification,
    V2BillingRateCardVersionCreatedEventNotification,
    V2CoreAccountClosedEventNotification,
    V2CoreAccountCreatedEventNotification,
    V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCardCreatorUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationCustomerUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationMerchantUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationRecipientUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEventNotification,
    V2CoreAccountIncludingConfigurationStorerUpdatedEventNotification,
    V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    V2CoreAccountIncludingIdentityUpdatedEventNotification,
    V2CoreAccountIncludingRequirementsUpdatedEventNotification,
    V2CoreAccountLinkReturnedEventNotification,
    V2CoreAccountPersonCreatedEventNotification,
    V2CoreAccountPersonDeletedEventNotification,
    V2CoreAccountPersonUpdatedEventNotification,
    V2CoreAccountUpdatedEventNotification,
    V2CoreClaimableSandboxClaimedEventNotification,
    V2CoreClaimableSandboxCreatedEventNotification,
    V2CoreClaimableSandboxExpiredEventNotification,
    V2CoreClaimableSandboxExpiringEventNotification,
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEventNotification,
    V2CoreEventDestinationPingEventNotification,
    V2CoreHealthApiErrorFiringEventNotification,
    V2CoreHealthApiErrorResolvedEventNotification,
    V2CoreHealthApiLatencyFiringEventNotification,
    V2CoreHealthApiLatencyResolvedEventNotification,
    V2CoreHealthAuthorizationRateDropFiringEventNotification,
    V2CoreHealthAuthorizationRateDropResolvedEventNotification,
    V2CoreHealthEventGenerationFailureResolvedEventNotification,
    V2CoreHealthFraudRateIncreasedEventNotification,
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEventNotification,
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEventNotification,
    V2CoreHealthIssuingAuthorizationRequestTimeoutFiringEventNotification,
    V2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEventNotification,
    V2CoreHealthPaymentMethodErrorFiringEventNotification,
    V2CoreHealthPaymentMethodErrorResolvedEventNotification,
    V2CoreHealthTrafficVolumeDropFiringEventNotification,
    V2CoreHealthTrafficVolumeDropResolvedEventNotification,
    V2CoreHealthWebhookLatencyFiringEventNotification,
    V2CoreHealthWebhookLatencyResolvedEventNotification,
    V2MoneyManagementAdjustmentCreatedEventNotification,
    V2MoneyManagementFinancialAccountCreatedEventNotification,
    V2MoneyManagementFinancialAccountUpdatedEventNotification,
    V2MoneyManagementFinancialAddressActivatedEventNotification,
    V2MoneyManagementFinancialAddressFailedEventNotification,
    V2MoneyManagementInboundTransferAvailableEventNotification,
    V2MoneyManagementInboundTransferBankDebitFailedEventNotification,
    V2MoneyManagementInboundTransferBankDebitProcessingEventNotification,
    V2MoneyManagementInboundTransferBankDebitQueuedEventNotification,
    V2MoneyManagementInboundTransferBankDebitReturnedEventNotification,
    V2MoneyManagementInboundTransferBankDebitSucceededEventNotification,
    V2MoneyManagementOutboundPaymentCanceledEventNotification,
    V2MoneyManagementOutboundPaymentCreatedEventNotification,
    V2MoneyManagementOutboundPaymentFailedEventNotification,
    V2MoneyManagementOutboundPaymentPostedEventNotification,
    V2MoneyManagementOutboundPaymentReturnedEventNotification,
    V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    V2MoneyManagementOutboundTransferCanceledEventNotification,
    V2MoneyManagementOutboundTransferCreatedEventNotification,
    V2MoneyManagementOutboundTransferFailedEventNotification,
    V2MoneyManagementOutboundTransferPostedEventNotification,
    V2MoneyManagementOutboundTransferReturnedEventNotification,
    V2MoneyManagementOutboundTransferUpdatedEventNotification,
    V2MoneyManagementPayoutMethodUpdatedEventNotification,
    V2MoneyManagementReceivedCreditAvailableEventNotification,
    V2MoneyManagementReceivedCreditFailedEventNotification,
    V2MoneyManagementReceivedCreditReturnedEventNotification,
    V2MoneyManagementReceivedCreditSucceededEventNotification,
    V2MoneyManagementReceivedDebitCanceledEventNotification,
    V2MoneyManagementReceivedDebitFailedEventNotification,
    V2MoneyManagementReceivedDebitPendingEventNotification,
    V2MoneyManagementReceivedDebitSucceededEventNotification,
    V2MoneyManagementReceivedDebitUpdatedEventNotification,
    V2MoneyManagementRecipientVerificationCreatedEventNotification,
    V2MoneyManagementRecipientVerificationUpdatedEventNotification,
    V2MoneyManagementTransactionCreatedEventNotification,
    V2MoneyManagementTransactionUpdatedEventNotification,
    V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEventNotification,
    V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEventNotification,
    V2PaymentsOffSessionPaymentCanceledEventNotification,
    V2PaymentsOffSessionPaymentCreatedEventNotification,
    V2PaymentsOffSessionPaymentFailedEventNotification,
    V2PaymentsOffSessionPaymentRequiresCaptureEventNotification,
    V2PaymentsOffSessionPaymentSucceededEventNotification,
]
