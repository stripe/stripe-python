# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.events._v1_account_updated_event import V1AccountUpdatedEvent
from stripe.events._v1_application_fee_created_event import (
    V1ApplicationFeeCreatedEvent,
)
from stripe.events._v1_application_fee_refunded_event import (
    V1ApplicationFeeRefundedEvent,
)
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_billing_meter_no_meter_found_event import (
    V1BillingMeterNoMeterFoundEvent,
)
from stripe.events._v1_billing_portal_configuration_created_event import (
    V1BillingPortalConfigurationCreatedEvent,
)
from stripe.events._v1_billing_portal_configuration_updated_event import (
    V1BillingPortalConfigurationUpdatedEvent,
)
from stripe.events._v1_capability_updated_event import V1CapabilityUpdatedEvent
from stripe.events._v1_charge_captured_event import V1ChargeCapturedEvent
from stripe.events._v1_charge_dispute_closed_event import (
    V1ChargeDisputeClosedEvent,
)
from stripe.events._v1_charge_dispute_created_event import (
    V1ChargeDisputeCreatedEvent,
)
from stripe.events._v1_charge_dispute_funds_reinstated_event import (
    V1ChargeDisputeFundsReinstatedEvent,
)
from stripe.events._v1_charge_dispute_funds_withdrawn_event import (
    V1ChargeDisputeFundsWithdrawnEvent,
)
from stripe.events._v1_charge_dispute_updated_event import (
    V1ChargeDisputeUpdatedEvent,
)
from stripe.events._v1_charge_expired_event import V1ChargeExpiredEvent
from stripe.events._v1_charge_failed_event import V1ChargeFailedEvent
from stripe.events._v1_charge_pending_event import V1ChargePendingEvent
from stripe.events._v1_charge_refund_updated_event import (
    V1ChargeRefundUpdatedEvent,
)
from stripe.events._v1_charge_refunded_event import V1ChargeRefundedEvent
from stripe.events._v1_charge_succeeded_event import V1ChargeSucceededEvent
from stripe.events._v1_charge_updated_event import V1ChargeUpdatedEvent
from stripe.events._v1_checkout_session_async_payment_failed_event import (
    V1CheckoutSessionAsyncPaymentFailedEvent,
)
from stripe.events._v1_checkout_session_async_payment_succeeded_event import (
    V1CheckoutSessionAsyncPaymentSucceededEvent,
)
from stripe.events._v1_checkout_session_completed_event import (
    V1CheckoutSessionCompletedEvent,
)
from stripe.events._v1_checkout_session_expired_event import (
    V1CheckoutSessionExpiredEvent,
)
from stripe.events._v1_climate_order_canceled_event import (
    V1ClimateOrderCanceledEvent,
)
from stripe.events._v1_climate_order_created_event import (
    V1ClimateOrderCreatedEvent,
)
from stripe.events._v1_climate_order_delayed_event import (
    V1ClimateOrderDelayedEvent,
)
from stripe.events._v1_climate_order_delivered_event import (
    V1ClimateOrderDeliveredEvent,
)
from stripe.events._v1_climate_order_product_substituted_event import (
    V1ClimateOrderProductSubstitutedEvent,
)
from stripe.events._v1_climate_product_created_event import (
    V1ClimateProductCreatedEvent,
)
from stripe.events._v1_climate_product_pricing_updated_event import (
    V1ClimateProductPricingUpdatedEvent,
)
from stripe.events._v1_coupon_created_event import V1CouponCreatedEvent
from stripe.events._v1_coupon_deleted_event import V1CouponDeletedEvent
from stripe.events._v1_coupon_updated_event import V1CouponUpdatedEvent
from stripe.events._v1_credit_note_created_event import (
    V1CreditNoteCreatedEvent,
)
from stripe.events._v1_credit_note_updated_event import (
    V1CreditNoteUpdatedEvent,
)
from stripe.events._v1_credit_note_voided_event import V1CreditNoteVoidedEvent
from stripe.events._v1_customer_created_event import V1CustomerCreatedEvent
from stripe.events._v1_customer_deleted_event import V1CustomerDeletedEvent
from stripe.events._v1_customer_discount_created_event import (
    V1CustomerDiscountCreatedEvent,
)
from stripe.events._v1_customer_discount_deleted_event import (
    V1CustomerDiscountDeletedEvent,
)
from stripe.events._v1_customer_discount_updated_event import (
    V1CustomerDiscountUpdatedEvent,
)
from stripe.events._v1_customer_subscription_created_event import (
    V1CustomerSubscriptionCreatedEvent,
)
from stripe.events._v1_customer_subscription_deleted_event import (
    V1CustomerSubscriptionDeletedEvent,
)
from stripe.events._v1_customer_subscription_paused_event import (
    V1CustomerSubscriptionPausedEvent,
)
from stripe.events._v1_customer_subscription_pending_update_applied_event import (
    V1CustomerSubscriptionPendingUpdateAppliedEvent,
)
from stripe.events._v1_customer_subscription_pending_update_expired_event import (
    V1CustomerSubscriptionPendingUpdateExpiredEvent,
)
from stripe.events._v1_customer_subscription_resumed_event import (
    V1CustomerSubscriptionResumedEvent,
)
from stripe.events._v1_customer_subscription_trial_will_end_event import (
    V1CustomerSubscriptionTrialWillEndEvent,
)
from stripe.events._v1_customer_subscription_updated_event import (
    V1CustomerSubscriptionUpdatedEvent,
)
from stripe.events._v1_customer_tax_id_created_event import (
    V1CustomerTaxIdCreatedEvent,
)
from stripe.events._v1_customer_tax_id_deleted_event import (
    V1CustomerTaxIdDeletedEvent,
)
from stripe.events._v1_customer_tax_id_updated_event import (
    V1CustomerTaxIdUpdatedEvent,
)
from stripe.events._v1_customer_updated_event import V1CustomerUpdatedEvent
from stripe.events._v1_file_created_event import V1FileCreatedEvent
from stripe.events._v1_financial_connections_account_created_event import (
    V1FinancialConnectionsAccountCreatedEvent,
)
from stripe.events._v1_financial_connections_account_deactivated_event import (
    V1FinancialConnectionsAccountDeactivatedEvent,
)
from stripe.events._v1_financial_connections_account_disconnected_event import (
    V1FinancialConnectionsAccountDisconnectedEvent,
)
from stripe.events._v1_financial_connections_account_reactivated_event import (
    V1FinancialConnectionsAccountReactivatedEvent,
)
from stripe.events._v1_financial_connections_account_refreshed_balance_event import (
    V1FinancialConnectionsAccountRefreshedBalanceEvent,
)
from stripe.events._v1_financial_connections_account_refreshed_ownership_event import (
    V1FinancialConnectionsAccountRefreshedOwnershipEvent,
)
from stripe.events._v1_financial_connections_account_refreshed_transactions_event import (
    V1FinancialConnectionsAccountRefreshedTransactionsEvent,
)
from stripe.events._v1_identity_verification_session_canceled_event import (
    V1IdentityVerificationSessionCanceledEvent,
)
from stripe.events._v1_identity_verification_session_created_event import (
    V1IdentityVerificationSessionCreatedEvent,
)
from stripe.events._v1_identity_verification_session_processing_event import (
    V1IdentityVerificationSessionProcessingEvent,
)
from stripe.events._v1_identity_verification_session_redacted_event import (
    V1IdentityVerificationSessionRedactedEvent,
)
from stripe.events._v1_identity_verification_session_requires_input_event import (
    V1IdentityVerificationSessionRequiresInputEvent,
)
from stripe.events._v1_identity_verification_session_verified_event import (
    V1IdentityVerificationSessionVerifiedEvent,
)
from stripe.events._v1_invoice_created_event import V1InvoiceCreatedEvent
from stripe.events._v1_invoice_deleted_event import V1InvoiceDeletedEvent
from stripe.events._v1_invoice_finalization_failed_event import (
    V1InvoiceFinalizationFailedEvent,
)
from stripe.events._v1_invoice_finalized_event import V1InvoiceFinalizedEvent
from stripe.events._v1_invoice_marked_uncollectible_event import (
    V1InvoiceMarkedUncollectibleEvent,
)
from stripe.events._v1_invoice_overdue_event import V1InvoiceOverdueEvent
from stripe.events._v1_invoice_overpaid_event import V1InvoiceOverpaidEvent
from stripe.events._v1_invoice_paid_event import V1InvoicePaidEvent
from stripe.events._v1_invoice_payment_action_required_event import (
    V1InvoicePaymentActionRequiredEvent,
)
from stripe.events._v1_invoice_payment_failed_event import (
    V1InvoicePaymentFailedEvent,
)
from stripe.events._v1_invoice_payment_succeeded_event import (
    V1InvoicePaymentSucceededEvent,
)
from stripe.events._v1_invoice_sent_event import V1InvoiceSentEvent
from stripe.events._v1_invoice_upcoming_event import V1InvoiceUpcomingEvent
from stripe.events._v1_invoice_updated_event import V1InvoiceUpdatedEvent
from stripe.events._v1_invoice_voided_event import V1InvoiceVoidedEvent
from stripe.events._v1_invoice_will_be_due_event import V1InvoiceWillBeDueEvent
from stripe.events._v1_invoice_payment_paid_event import (
    V1InvoicePaymentPaidEvent,
)
from stripe.events._v1_invoiceitem_created_event import (
    V1InvoiceitemCreatedEvent,
)
from stripe.events._v1_invoiceitem_deleted_event import (
    V1InvoiceitemDeletedEvent,
)
from stripe.events._v1_issuing_authorization_created_event import (
    V1IssuingAuthorizationCreatedEvent,
)
from stripe.events._v1_issuing_authorization_request_event import (
    V1IssuingAuthorizationRequestEvent,
)
from stripe.events._v1_issuing_authorization_updated_event import (
    V1IssuingAuthorizationUpdatedEvent,
)
from stripe.events._v1_issuing_card_created_event import (
    V1IssuingCardCreatedEvent,
)
from stripe.events._v1_issuing_card_updated_event import (
    V1IssuingCardUpdatedEvent,
)
from stripe.events._v1_issuing_cardholder_created_event import (
    V1IssuingCardholderCreatedEvent,
)
from stripe.events._v1_issuing_cardholder_updated_event import (
    V1IssuingCardholderUpdatedEvent,
)
from stripe.events._v1_issuing_dispute_closed_event import (
    V1IssuingDisputeClosedEvent,
)
from stripe.events._v1_issuing_dispute_created_event import (
    V1IssuingDisputeCreatedEvent,
)
from stripe.events._v1_issuing_dispute_funds_reinstated_event import (
    V1IssuingDisputeFundsReinstatedEvent,
)
from stripe.events._v1_issuing_dispute_funds_rescinded_event import (
    V1IssuingDisputeFundsRescindedEvent,
)
from stripe.events._v1_issuing_dispute_submitted_event import (
    V1IssuingDisputeSubmittedEvent,
)
from stripe.events._v1_issuing_dispute_updated_event import (
    V1IssuingDisputeUpdatedEvent,
)
from stripe.events._v1_issuing_personalization_design_activated_event import (
    V1IssuingPersonalizationDesignActivatedEvent,
)
from stripe.events._v1_issuing_personalization_design_deactivated_event import (
    V1IssuingPersonalizationDesignDeactivatedEvent,
)
from stripe.events._v1_issuing_personalization_design_rejected_event import (
    V1IssuingPersonalizationDesignRejectedEvent,
)
from stripe.events._v1_issuing_personalization_design_updated_event import (
    V1IssuingPersonalizationDesignUpdatedEvent,
)
from stripe.events._v1_issuing_token_created_event import (
    V1IssuingTokenCreatedEvent,
)
from stripe.events._v1_issuing_token_updated_event import (
    V1IssuingTokenUpdatedEvent,
)
from stripe.events._v1_issuing_transaction_created_event import (
    V1IssuingTransactionCreatedEvent,
)
from stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event import (
    V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent,
)
from stripe.events._v1_issuing_transaction_updated_event import (
    V1IssuingTransactionUpdatedEvent,
)
from stripe.events._v1_mandate_updated_event import V1MandateUpdatedEvent
from stripe.events._v1_payment_intent_amount_capturable_updated_event import (
    V1PaymentIntentAmountCapturableUpdatedEvent,
)
from stripe.events._v1_payment_intent_canceled_event import (
    V1PaymentIntentCanceledEvent,
)
from stripe.events._v1_payment_intent_created_event import (
    V1PaymentIntentCreatedEvent,
)
from stripe.events._v1_payment_intent_partially_funded_event import (
    V1PaymentIntentPartiallyFundedEvent,
)
from stripe.events._v1_payment_intent_payment_failed_event import (
    V1PaymentIntentPaymentFailedEvent,
)
from stripe.events._v1_payment_intent_processing_event import (
    V1PaymentIntentProcessingEvent,
)
from stripe.events._v1_payment_intent_requires_action_event import (
    V1PaymentIntentRequiresActionEvent,
)
from stripe.events._v1_payment_intent_succeeded_event import (
    V1PaymentIntentSucceededEvent,
)
from stripe.events._v1_payment_link_created_event import (
    V1PaymentLinkCreatedEvent,
)
from stripe.events._v1_payment_link_updated_event import (
    V1PaymentLinkUpdatedEvent,
)
from stripe.events._v1_payment_method_attached_event import (
    V1PaymentMethodAttachedEvent,
)
from stripe.events._v1_payment_method_automatically_updated_event import (
    V1PaymentMethodAutomaticallyUpdatedEvent,
)
from stripe.events._v1_payment_method_detached_event import (
    V1PaymentMethodDetachedEvent,
)
from stripe.events._v1_payment_method_updated_event import (
    V1PaymentMethodUpdatedEvent,
)
from stripe.events._v1_payout_canceled_event import V1PayoutCanceledEvent
from stripe.events._v1_payout_created_event import V1PayoutCreatedEvent
from stripe.events._v1_payout_failed_event import V1PayoutFailedEvent
from stripe.events._v1_payout_paid_event import V1PayoutPaidEvent
from stripe.events._v1_payout_reconciliation_completed_event import (
    V1PayoutReconciliationCompletedEvent,
)
from stripe.events._v1_payout_updated_event import V1PayoutUpdatedEvent
from stripe.events._v1_person_created_event import V1PersonCreatedEvent
from stripe.events._v1_person_deleted_event import V1PersonDeletedEvent
from stripe.events._v1_person_updated_event import V1PersonUpdatedEvent
from stripe.events._v1_plan_created_event import V1PlanCreatedEvent
from stripe.events._v1_plan_deleted_event import V1PlanDeletedEvent
from stripe.events._v1_plan_updated_event import V1PlanUpdatedEvent
from stripe.events._v1_price_created_event import V1PriceCreatedEvent
from stripe.events._v1_price_deleted_event import V1PriceDeletedEvent
from stripe.events._v1_price_updated_event import V1PriceUpdatedEvent
from stripe.events._v1_product_created_event import V1ProductCreatedEvent
from stripe.events._v1_product_deleted_event import V1ProductDeletedEvent
from stripe.events._v1_product_updated_event import V1ProductUpdatedEvent
from stripe.events._v1_promotion_code_created_event import (
    V1PromotionCodeCreatedEvent,
)
from stripe.events._v1_promotion_code_updated_event import (
    V1PromotionCodeUpdatedEvent,
)
from stripe.events._v1_quote_accepted_event import V1QuoteAcceptedEvent
from stripe.events._v1_quote_canceled_event import V1QuoteCanceledEvent
from stripe.events._v1_quote_created_event import V1QuoteCreatedEvent
from stripe.events._v1_quote_finalized_event import V1QuoteFinalizedEvent
from stripe.events._v1_radar_early_fraud_warning_created_event import (
    V1RadarEarlyFraudWarningCreatedEvent,
)
from stripe.events._v1_radar_early_fraud_warning_updated_event import (
    V1RadarEarlyFraudWarningUpdatedEvent,
)
from stripe.events._v1_refund_created_event import V1RefundCreatedEvent
from stripe.events._v1_refund_failed_event import V1RefundFailedEvent
from stripe.events._v1_refund_updated_event import V1RefundUpdatedEvent
from stripe.events._v1_review_closed_event import V1ReviewClosedEvent
from stripe.events._v1_review_opened_event import V1ReviewOpenedEvent
from stripe.events._v1_setup_intent_canceled_event import (
    V1SetupIntentCanceledEvent,
)
from stripe.events._v1_setup_intent_created_event import (
    V1SetupIntentCreatedEvent,
)
from stripe.events._v1_setup_intent_requires_action_event import (
    V1SetupIntentRequiresActionEvent,
)
from stripe.events._v1_setup_intent_setup_failed_event import (
    V1SetupIntentSetupFailedEvent,
)
from stripe.events._v1_setup_intent_succeeded_event import (
    V1SetupIntentSucceededEvent,
)
from stripe.events._v1_sigma_scheduled_query_run_created_event import (
    V1SigmaScheduledQueryRunCreatedEvent,
)
from stripe.events._v1_source_canceled_event import V1SourceCanceledEvent
from stripe.events._v1_source_chargeable_event import V1SourceChargeableEvent
from stripe.events._v1_source_failed_event import V1SourceFailedEvent
from stripe.events._v1_source_refund_attributes_required_event import (
    V1SourceRefundAttributesRequiredEvent,
)
from stripe.events._v1_subscription_schedule_aborted_event import (
    V1SubscriptionScheduleAbortedEvent,
)
from stripe.events._v1_subscription_schedule_canceled_event import (
    V1SubscriptionScheduleCanceledEvent,
)
from stripe.events._v1_subscription_schedule_completed_event import (
    V1SubscriptionScheduleCompletedEvent,
)
from stripe.events._v1_subscription_schedule_created_event import (
    V1SubscriptionScheduleCreatedEvent,
)
from stripe.events._v1_subscription_schedule_expiring_event import (
    V1SubscriptionScheduleExpiringEvent,
)
from stripe.events._v1_subscription_schedule_released_event import (
    V1SubscriptionScheduleReleasedEvent,
)
from stripe.events._v1_subscription_schedule_updated_event import (
    V1SubscriptionScheduleUpdatedEvent,
)
from stripe.events._v1_tax_rate_created_event import V1TaxRateCreatedEvent
from stripe.events._v1_tax_rate_updated_event import V1TaxRateUpdatedEvent
from stripe.events._v1_terminal_reader_action_failed_event import (
    V1TerminalReaderActionFailedEvent,
)
from stripe.events._v1_terminal_reader_action_succeeded_event import (
    V1TerminalReaderActionSucceededEvent,
)
from stripe.events._v1_terminal_reader_action_updated_event import (
    V1TerminalReaderActionUpdatedEvent,
)
from stripe.events._v1_test_helpers_test_clock_advancing_event import (
    V1TestHelpersTestClockAdvancingEvent,
)
from stripe.events._v1_test_helpers_test_clock_created_event import (
    V1TestHelpersTestClockCreatedEvent,
)
from stripe.events._v1_test_helpers_test_clock_deleted_event import (
    V1TestHelpersTestClockDeletedEvent,
)
from stripe.events._v1_test_helpers_test_clock_internal_failure_event import (
    V1TestHelpersTestClockInternalFailureEvent,
)
from stripe.events._v1_test_helpers_test_clock_ready_event import (
    V1TestHelpersTestClockReadyEvent,
)
from stripe.events._v1_topup_canceled_event import V1TopupCanceledEvent
from stripe.events._v1_topup_created_event import V1TopupCreatedEvent
from stripe.events._v1_topup_failed_event import V1TopupFailedEvent
from stripe.events._v1_topup_reversed_event import V1TopupReversedEvent
from stripe.events._v1_topup_succeeded_event import V1TopupSucceededEvent
from stripe.events._v1_transfer_created_event import V1TransferCreatedEvent
from stripe.events._v1_transfer_reversed_event import V1TransferReversedEvent
from stripe.events._v1_transfer_updated_event import V1TransferUpdatedEvent
from stripe.events._v2_billing_bill_setting_updated_event import (
    V2BillingBillSettingUpdatedEvent,
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
from stripe.events._v2_core_claimable_sandbox_claimed_event import (
    V2CoreClaimableSandboxClaimedEvent,
)
from stripe.events._v2_core_claimable_sandbox_created_event import (
    V2CoreClaimableSandboxCreatedEvent,
)
from stripe.events._v2_core_claimable_sandbox_expired_event import (
    V2CoreClaimableSandboxExpiredEvent,
)
from stripe.events._v2_core_claimable_sandbox_expiring_event import (
    V2CoreClaimableSandboxExpiringEvent,
)
from stripe.events._v2_core_claimable_sandbox_sandbox_details_owner_account_updated_event import (
    V2CoreClaimableSandboxSandboxDetailsOwnerAccountUpdatedEvent,
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
from stripe.events._v2_core_health_issuing_authorization_request_errors_firing_event import (
    V2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent,
)
from stripe.events._v2_core_health_issuing_authorization_request_errors_resolved_event import (
    V2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent,
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
from stripe.events._v2_money_management_recipient_verification_created_event import (
    V2MoneyManagementRecipientVerificationCreatedEvent,
)
from stripe.events._v2_money_management_recipient_verification_updated_event import (
    V2MoneyManagementRecipientVerificationUpdatedEvent,
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


THIN_EVENT_CLASSES = {
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
    V1CustomerDiscountCreatedEvent.LOOKUP_TYPE: V1CustomerDiscountCreatedEvent,
    V1CustomerDiscountDeletedEvent.LOOKUP_TYPE: V1CustomerDiscountDeletedEvent,
    V1CustomerDiscountUpdatedEvent.LOOKUP_TYPE: V1CustomerDiscountUpdatedEvent,
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
    V2BillingBillSettingUpdatedEvent.LOOKUP_TYPE: V2BillingBillSettingUpdatedEvent,
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
    V2PaymentsOffSessionPaymentSucceededEvent.LOOKUP_TYPE: V2PaymentsOffSessionPaymentSucceededEvent,
}
