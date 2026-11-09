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
    from stripe.events._v1_account_application_authorized_event import (
        V1AccountApplicationAuthorizedEvent as V1AccountApplicationAuthorizedEvent,
        V1AccountApplicationAuthorizedEventNotification as V1AccountApplicationAuthorizedEventNotification,
    )
    from stripe.events._v1_account_application_deauthorized_event import (
        V1AccountApplicationDeauthorizedEvent as V1AccountApplicationDeauthorizedEvent,
        V1AccountApplicationDeauthorizedEventNotification as V1AccountApplicationDeauthorizedEventNotification,
    )
    from stripe.events._v1_account_external_account_created_event import (
        V1AccountExternalAccountCreatedEvent as V1AccountExternalAccountCreatedEvent,
        V1AccountExternalAccountCreatedEventNotification as V1AccountExternalAccountCreatedEventNotification,
    )
    from stripe.events._v1_account_external_account_deleted_event import (
        V1AccountExternalAccountDeletedEvent as V1AccountExternalAccountDeletedEvent,
        V1AccountExternalAccountDeletedEventNotification as V1AccountExternalAccountDeletedEventNotification,
    )
    from stripe.events._v1_account_external_account_updated_event import (
        V1AccountExternalAccountUpdatedEvent as V1AccountExternalAccountUpdatedEvent,
        V1AccountExternalAccountUpdatedEventNotification as V1AccountExternalAccountUpdatedEventNotification,
    )
    from stripe.events._v1_account_updated_event import (
        V1AccountUpdatedEvent as V1AccountUpdatedEvent,
        V1AccountUpdatedEventNotification as V1AccountUpdatedEventNotification,
    )
    from stripe.events._v1_application_fee_created_event import (
        V1ApplicationFeeCreatedEvent as V1ApplicationFeeCreatedEvent,
        V1ApplicationFeeCreatedEventNotification as V1ApplicationFeeCreatedEventNotification,
    )
    from stripe.events._v1_application_fee_refund_updated_event import (
        V1ApplicationFeeRefundUpdatedEvent as V1ApplicationFeeRefundUpdatedEvent,
        V1ApplicationFeeRefundUpdatedEventNotification as V1ApplicationFeeRefundUpdatedEventNotification,
    )
    from stripe.events._v1_application_fee_refunded_event import (
        V1ApplicationFeeRefundedEvent as V1ApplicationFeeRefundedEvent,
        V1ApplicationFeeRefundedEventNotification as V1ApplicationFeeRefundedEventNotification,
    )
    from stripe.events._v1_balance_available_event import (
        V1BalanceAvailableEvent as V1BalanceAvailableEvent,
        V1BalanceAvailableEventNotification as V1BalanceAvailableEventNotification,
    )
    from stripe.events._v1_balance_settings_updated_event import (
        V1BalanceSettingsUpdatedEvent as V1BalanceSettingsUpdatedEvent,
        V1BalanceSettingsUpdatedEventNotification as V1BalanceSettingsUpdatedEventNotification,
    )
    from stripe.events._v1_billing_alert_triggered_event import (
        V1BillingAlertTriggeredEvent as V1BillingAlertTriggeredEvent,
        V1BillingAlertTriggeredEventNotification as V1BillingAlertTriggeredEventNotification,
    )
    from stripe.events._v1_billing_credit_balance_transaction_created_event import (
        V1BillingCreditBalanceTransactionCreatedEvent as V1BillingCreditBalanceTransactionCreatedEvent,
        V1BillingCreditBalanceTransactionCreatedEventNotification as V1BillingCreditBalanceTransactionCreatedEventNotification,
    )
    from stripe.events._v1_billing_credit_grant_created_event import (
        V1BillingCreditGrantCreatedEvent as V1BillingCreditGrantCreatedEvent,
        V1BillingCreditGrantCreatedEventNotification as V1BillingCreditGrantCreatedEventNotification,
    )
    from stripe.events._v1_billing_credit_grant_updated_event import (
        V1BillingCreditGrantUpdatedEvent as V1BillingCreditGrantUpdatedEvent,
        V1BillingCreditGrantUpdatedEventNotification as V1BillingCreditGrantUpdatedEventNotification,
    )
    from stripe.events._v1_billing_meter_created_event import (
        V1BillingMeterCreatedEvent as V1BillingMeterCreatedEvent,
        V1BillingMeterCreatedEventNotification as V1BillingMeterCreatedEventNotification,
    )
    from stripe.events._v1_billing_meter_deactivated_event import (
        V1BillingMeterDeactivatedEvent as V1BillingMeterDeactivatedEvent,
        V1BillingMeterDeactivatedEventNotification as V1BillingMeterDeactivatedEventNotification,
    )
    from stripe.events._v1_billing_meter_error_report_triggered_event import (
        V1BillingMeterErrorReportTriggeredEvent as V1BillingMeterErrorReportTriggeredEvent,
        V1BillingMeterErrorReportTriggeredEventNotification as V1BillingMeterErrorReportTriggeredEventNotification,
    )
    from stripe.events._v1_billing_meter_no_meter_found_event import (
        V1BillingMeterNoMeterFoundEvent as V1BillingMeterNoMeterFoundEvent,
        V1BillingMeterNoMeterFoundEventNotification as V1BillingMeterNoMeterFoundEventNotification,
    )
    from stripe.events._v1_billing_meter_reactivated_event import (
        V1BillingMeterReactivatedEvent as V1BillingMeterReactivatedEvent,
        V1BillingMeterReactivatedEventNotification as V1BillingMeterReactivatedEventNotification,
    )
    from stripe.events._v1_billing_meter_updated_event import (
        V1BillingMeterUpdatedEvent as V1BillingMeterUpdatedEvent,
        V1BillingMeterUpdatedEventNotification as V1BillingMeterUpdatedEventNotification,
    )
    from stripe.events._v1_billing_portal_configuration_created_event import (
        V1BillingPortalConfigurationCreatedEvent as V1BillingPortalConfigurationCreatedEvent,
        V1BillingPortalConfigurationCreatedEventNotification as V1BillingPortalConfigurationCreatedEventNotification,
    )
    from stripe.events._v1_billing_portal_configuration_updated_event import (
        V1BillingPortalConfigurationUpdatedEvent as V1BillingPortalConfigurationUpdatedEvent,
        V1BillingPortalConfigurationUpdatedEventNotification as V1BillingPortalConfigurationUpdatedEventNotification,
    )
    from stripe.events._v1_billing_portal_session_created_event import (
        V1BillingPortalSessionCreatedEvent as V1BillingPortalSessionCreatedEvent,
        V1BillingPortalSessionCreatedEventNotification as V1BillingPortalSessionCreatedEventNotification,
    )
    from stripe.events._v1_capability_updated_event import (
        V1CapabilityUpdatedEvent as V1CapabilityUpdatedEvent,
        V1CapabilityUpdatedEventNotification as V1CapabilityUpdatedEventNotification,
    )
    from stripe.events._v1_cash_balance_funds_available_event import (
        V1CashBalanceFundsAvailableEvent as V1CashBalanceFundsAvailableEvent,
        V1CashBalanceFundsAvailableEventNotification as V1CashBalanceFundsAvailableEventNotification,
    )
    from stripe.events._v1_charge_captured_event import (
        V1ChargeCapturedEvent as V1ChargeCapturedEvent,
        V1ChargeCapturedEventNotification as V1ChargeCapturedEventNotification,
    )
    from stripe.events._v1_charge_dispute_closed_event import (
        V1ChargeDisputeClosedEvent as V1ChargeDisputeClosedEvent,
        V1ChargeDisputeClosedEventNotification as V1ChargeDisputeClosedEventNotification,
    )
    from stripe.events._v1_charge_dispute_created_event import (
        V1ChargeDisputeCreatedEvent as V1ChargeDisputeCreatedEvent,
        V1ChargeDisputeCreatedEventNotification as V1ChargeDisputeCreatedEventNotification,
    )
    from stripe.events._v1_charge_dispute_funds_reinstated_event import (
        V1ChargeDisputeFundsReinstatedEvent as V1ChargeDisputeFundsReinstatedEvent,
        V1ChargeDisputeFundsReinstatedEventNotification as V1ChargeDisputeFundsReinstatedEventNotification,
    )
    from stripe.events._v1_charge_dispute_funds_withdrawn_event import (
        V1ChargeDisputeFundsWithdrawnEvent as V1ChargeDisputeFundsWithdrawnEvent,
        V1ChargeDisputeFundsWithdrawnEventNotification as V1ChargeDisputeFundsWithdrawnEventNotification,
    )
    from stripe.events._v1_charge_dispute_updated_event import (
        V1ChargeDisputeUpdatedEvent as V1ChargeDisputeUpdatedEvent,
        V1ChargeDisputeUpdatedEventNotification as V1ChargeDisputeUpdatedEventNotification,
    )
    from stripe.events._v1_charge_expired_event import (
        V1ChargeExpiredEvent as V1ChargeExpiredEvent,
        V1ChargeExpiredEventNotification as V1ChargeExpiredEventNotification,
    )
    from stripe.events._v1_charge_failed_event import (
        V1ChargeFailedEvent as V1ChargeFailedEvent,
        V1ChargeFailedEventNotification as V1ChargeFailedEventNotification,
    )
    from stripe.events._v1_charge_pending_event import (
        V1ChargePendingEvent as V1ChargePendingEvent,
        V1ChargePendingEventNotification as V1ChargePendingEventNotification,
    )
    from stripe.events._v1_charge_refund_updated_event import (
        V1ChargeRefundUpdatedEvent as V1ChargeRefundUpdatedEvent,
        V1ChargeRefundUpdatedEventNotification as V1ChargeRefundUpdatedEventNotification,
    )
    from stripe.events._v1_charge_refunded_event import (
        V1ChargeRefundedEvent as V1ChargeRefundedEvent,
        V1ChargeRefundedEventNotification as V1ChargeRefundedEventNotification,
    )
    from stripe.events._v1_charge_succeeded_event import (
        V1ChargeSucceededEvent as V1ChargeSucceededEvent,
        V1ChargeSucceededEventNotification as V1ChargeSucceededEventNotification,
    )
    from stripe.events._v1_charge_updated_event import (
        V1ChargeUpdatedEvent as V1ChargeUpdatedEvent,
        V1ChargeUpdatedEventNotification as V1ChargeUpdatedEventNotification,
    )
    from stripe.events._v1_checkout_session_async_payment_failed_event import (
        V1CheckoutSessionAsyncPaymentFailedEvent as V1CheckoutSessionAsyncPaymentFailedEvent,
        V1CheckoutSessionAsyncPaymentFailedEventNotification as V1CheckoutSessionAsyncPaymentFailedEventNotification,
    )
    from stripe.events._v1_checkout_session_async_payment_succeeded_event import (
        V1CheckoutSessionAsyncPaymentSucceededEvent as V1CheckoutSessionAsyncPaymentSucceededEvent,
        V1CheckoutSessionAsyncPaymentSucceededEventNotification as V1CheckoutSessionAsyncPaymentSucceededEventNotification,
    )
    from stripe.events._v1_checkout_session_completed_event import (
        V1CheckoutSessionCompletedEvent as V1CheckoutSessionCompletedEvent,
        V1CheckoutSessionCompletedEventNotification as V1CheckoutSessionCompletedEventNotification,
    )
    from stripe.events._v1_checkout_session_expired_event import (
        V1CheckoutSessionExpiredEvent as V1CheckoutSessionExpiredEvent,
        V1CheckoutSessionExpiredEventNotification as V1CheckoutSessionExpiredEventNotification,
    )
    from stripe.events._v1_climate_order_canceled_event import (
        V1ClimateOrderCanceledEvent as V1ClimateOrderCanceledEvent,
        V1ClimateOrderCanceledEventNotification as V1ClimateOrderCanceledEventNotification,
    )
    from stripe.events._v1_climate_order_created_event import (
        V1ClimateOrderCreatedEvent as V1ClimateOrderCreatedEvent,
        V1ClimateOrderCreatedEventNotification as V1ClimateOrderCreatedEventNotification,
    )
    from stripe.events._v1_climate_order_delayed_event import (
        V1ClimateOrderDelayedEvent as V1ClimateOrderDelayedEvent,
        V1ClimateOrderDelayedEventNotification as V1ClimateOrderDelayedEventNotification,
    )
    from stripe.events._v1_climate_order_delivered_event import (
        V1ClimateOrderDeliveredEvent as V1ClimateOrderDeliveredEvent,
        V1ClimateOrderDeliveredEventNotification as V1ClimateOrderDeliveredEventNotification,
    )
    from stripe.events._v1_climate_order_product_substituted_event import (
        V1ClimateOrderProductSubstitutedEvent as V1ClimateOrderProductSubstitutedEvent,
        V1ClimateOrderProductSubstitutedEventNotification as V1ClimateOrderProductSubstitutedEventNotification,
    )
    from stripe.events._v1_climate_product_created_event import (
        V1ClimateProductCreatedEvent as V1ClimateProductCreatedEvent,
        V1ClimateProductCreatedEventNotification as V1ClimateProductCreatedEventNotification,
    )
    from stripe.events._v1_climate_product_pricing_updated_event import (
        V1ClimateProductPricingUpdatedEvent as V1ClimateProductPricingUpdatedEvent,
        V1ClimateProductPricingUpdatedEventNotification as V1ClimateProductPricingUpdatedEventNotification,
    )
    from stripe.events._v1_coupon_created_event import (
        V1CouponCreatedEvent as V1CouponCreatedEvent,
        V1CouponCreatedEventNotification as V1CouponCreatedEventNotification,
    )
    from stripe.events._v1_coupon_deleted_event import (
        V1CouponDeletedEvent as V1CouponDeletedEvent,
        V1CouponDeletedEventNotification as V1CouponDeletedEventNotification,
    )
    from stripe.events._v1_coupon_updated_event import (
        V1CouponUpdatedEvent as V1CouponUpdatedEvent,
        V1CouponUpdatedEventNotification as V1CouponUpdatedEventNotification,
    )
    from stripe.events._v1_credit_note_created_event import (
        V1CreditNoteCreatedEvent as V1CreditNoteCreatedEvent,
        V1CreditNoteCreatedEventNotification as V1CreditNoteCreatedEventNotification,
    )
    from stripe.events._v1_credit_note_updated_event import (
        V1CreditNoteUpdatedEvent as V1CreditNoteUpdatedEvent,
        V1CreditNoteUpdatedEventNotification as V1CreditNoteUpdatedEventNotification,
    )
    from stripe.events._v1_credit_note_voided_event import (
        V1CreditNoteVoidedEvent as V1CreditNoteVoidedEvent,
        V1CreditNoteVoidedEventNotification as V1CreditNoteVoidedEventNotification,
    )
    from stripe.events._v1_customer_cash_balance_transaction_created_event import (
        V1CustomerCashBalanceTransactionCreatedEvent as V1CustomerCashBalanceTransactionCreatedEvent,
        V1CustomerCashBalanceTransactionCreatedEventNotification as V1CustomerCashBalanceTransactionCreatedEventNotification,
    )
    from stripe.events._v1_customer_created_event import (
        V1CustomerCreatedEvent as V1CustomerCreatedEvent,
        V1CustomerCreatedEventNotification as V1CustomerCreatedEventNotification,
    )
    from stripe.events._v1_customer_deleted_event import (
        V1CustomerDeletedEvent as V1CustomerDeletedEvent,
        V1CustomerDeletedEventNotification as V1CustomerDeletedEventNotification,
    )
    from stripe.events._v1_customer_discount_created_event import (
        V1CustomerDiscountCreatedEvent as V1CustomerDiscountCreatedEvent,
        V1CustomerDiscountCreatedEventNotification as V1CustomerDiscountCreatedEventNotification,
    )
    from stripe.events._v1_customer_discount_deleted_event import (
        V1CustomerDiscountDeletedEvent as V1CustomerDiscountDeletedEvent,
        V1CustomerDiscountDeletedEventNotification as V1CustomerDiscountDeletedEventNotification,
    )
    from stripe.events._v1_customer_discount_source_changed_event import (
        V1CustomerDiscountSourceChangedEvent as V1CustomerDiscountSourceChangedEvent,
        V1CustomerDiscountSourceChangedEventNotification as V1CustomerDiscountSourceChangedEventNotification,
    )
    from stripe.events._v1_customer_discount_updated_event import (
        V1CustomerDiscountUpdatedEvent as V1CustomerDiscountUpdatedEvent,
        V1CustomerDiscountUpdatedEventNotification as V1CustomerDiscountUpdatedEventNotification,
    )
    from stripe.events._v1_customer_subscription_active_event import (
        V1CustomerSubscriptionActiveEvent as V1CustomerSubscriptionActiveEvent,
        V1CustomerSubscriptionActiveEventNotification as V1CustomerSubscriptionActiveEventNotification,
    )
    from stripe.events._v1_customer_subscription_cancel_at_changed_event import (
        V1CustomerSubscriptionCancelAtChangedEvent as V1CustomerSubscriptionCancelAtChangedEvent,
        V1CustomerSubscriptionCancelAtChangedEventNotification as V1CustomerSubscriptionCancelAtChangedEventNotification,
    )
    from stripe.events._v1_customer_subscription_created_event import (
        V1CustomerSubscriptionCreatedEvent as V1CustomerSubscriptionCreatedEvent,
        V1CustomerSubscriptionCreatedEventNotification as V1CustomerSubscriptionCreatedEventNotification,
    )
    from stripe.events._v1_customer_subscription_default_payment_method_changed_event import (
        V1CustomerSubscriptionDefaultPaymentMethodChangedEvent as V1CustomerSubscriptionDefaultPaymentMethodChangedEvent,
        V1CustomerSubscriptionDefaultPaymentMethodChangedEventNotification as V1CustomerSubscriptionDefaultPaymentMethodChangedEventNotification,
    )
    from stripe.events._v1_customer_subscription_deleted_event import (
        V1CustomerSubscriptionDeletedEvent as V1CustomerSubscriptionDeletedEvent,
        V1CustomerSubscriptionDeletedEventNotification as V1CustomerSubscriptionDeletedEventNotification,
    )
    from stripe.events._v1_customer_subscription_incomplete_event import (
        V1CustomerSubscriptionIncompleteEvent as V1CustomerSubscriptionIncompleteEvent,
        V1CustomerSubscriptionIncompleteEventNotification as V1CustomerSubscriptionIncompleteEventNotification,
    )
    from stripe.events._v1_customer_subscription_incomplete_expired_event import (
        V1CustomerSubscriptionIncompleteExpiredEvent as V1CustomerSubscriptionIncompleteExpiredEvent,
        V1CustomerSubscriptionIncompleteExpiredEventNotification as V1CustomerSubscriptionIncompleteExpiredEventNotification,
    )
    from stripe.events._v1_customer_subscription_item_added_event import (
        V1CustomerSubscriptionItemAddedEvent as V1CustomerSubscriptionItemAddedEvent,
        V1CustomerSubscriptionItemAddedEventNotification as V1CustomerSubscriptionItemAddedEventNotification,
    )
    from stripe.events._v1_customer_subscription_item_price_changed_event import (
        V1CustomerSubscriptionItemPriceChangedEvent as V1CustomerSubscriptionItemPriceChangedEvent,
        V1CustomerSubscriptionItemPriceChangedEventNotification as V1CustomerSubscriptionItemPriceChangedEventNotification,
    )
    from stripe.events._v1_customer_subscription_item_quantity_changed_event import (
        V1CustomerSubscriptionItemQuantityChangedEvent as V1CustomerSubscriptionItemQuantityChangedEvent,
        V1CustomerSubscriptionItemQuantityChangedEventNotification as V1CustomerSubscriptionItemQuantityChangedEventNotification,
    )
    from stripe.events._v1_customer_subscription_item_removed_event import (
        V1CustomerSubscriptionItemRemovedEvent as V1CustomerSubscriptionItemRemovedEvent,
        V1CustomerSubscriptionItemRemovedEventNotification as V1CustomerSubscriptionItemRemovedEventNotification,
    )
    from stripe.events._v1_customer_subscription_item_tax_rates_changed_event import (
        V1CustomerSubscriptionItemTaxRatesChangedEvent as V1CustomerSubscriptionItemTaxRatesChangedEvent,
        V1CustomerSubscriptionItemTaxRatesChangedEventNotification as V1CustomerSubscriptionItemTaxRatesChangedEventNotification,
    )
    from stripe.events._v1_customer_subscription_past_due_event import (
        V1CustomerSubscriptionPastDueEvent as V1CustomerSubscriptionPastDueEvent,
        V1CustomerSubscriptionPastDueEventNotification as V1CustomerSubscriptionPastDueEventNotification,
    )
    from stripe.events._v1_customer_subscription_paused_event import (
        V1CustomerSubscriptionPausedEvent as V1CustomerSubscriptionPausedEvent,
        V1CustomerSubscriptionPausedEventNotification as V1CustomerSubscriptionPausedEventNotification,
    )
    from stripe.events._v1_customer_subscription_pending_update_applied_event import (
        V1CustomerSubscriptionPendingUpdateAppliedEvent as V1CustomerSubscriptionPendingUpdateAppliedEvent,
        V1CustomerSubscriptionPendingUpdateAppliedEventNotification as V1CustomerSubscriptionPendingUpdateAppliedEventNotification,
    )
    from stripe.events._v1_customer_subscription_pending_update_expired_event import (
        V1CustomerSubscriptionPendingUpdateExpiredEvent as V1CustomerSubscriptionPendingUpdateExpiredEvent,
        V1CustomerSubscriptionPendingUpdateExpiredEventNotification as V1CustomerSubscriptionPendingUpdateExpiredEventNotification,
    )
    from stripe.events._v1_customer_subscription_resumed_event import (
        V1CustomerSubscriptionResumedEvent as V1CustomerSubscriptionResumedEvent,
        V1CustomerSubscriptionResumedEventNotification as V1CustomerSubscriptionResumedEventNotification,
    )
    from stripe.events._v1_customer_subscription_trial_will_end_event import (
        V1CustomerSubscriptionTrialWillEndEvent as V1CustomerSubscriptionTrialWillEndEvent,
        V1CustomerSubscriptionTrialWillEndEventNotification as V1CustomerSubscriptionTrialWillEndEventNotification,
    )
    from stripe.events._v1_customer_subscription_trialing_event import (
        V1CustomerSubscriptionTrialingEvent as V1CustomerSubscriptionTrialingEvent,
        V1CustomerSubscriptionTrialingEventNotification as V1CustomerSubscriptionTrialingEventNotification,
    )
    from stripe.events._v1_customer_subscription_unpaid_event import (
        V1CustomerSubscriptionUnpaidEvent as V1CustomerSubscriptionUnpaidEvent,
        V1CustomerSubscriptionUnpaidEventNotification as V1CustomerSubscriptionUnpaidEventNotification,
    )
    from stripe.events._v1_customer_subscription_updated_event import (
        V1CustomerSubscriptionUpdatedEvent as V1CustomerSubscriptionUpdatedEvent,
        V1CustomerSubscriptionUpdatedEventNotification as V1CustomerSubscriptionUpdatedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_created_event import (
        V1CustomerTaxIdCreatedEvent as V1CustomerTaxIdCreatedEvent,
        V1CustomerTaxIdCreatedEventNotification as V1CustomerTaxIdCreatedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_deleted_event import (
        V1CustomerTaxIdDeletedEvent as V1CustomerTaxIdDeletedEvent,
        V1CustomerTaxIdDeletedEventNotification as V1CustomerTaxIdDeletedEventNotification,
    )
    from stripe.events._v1_customer_tax_id_updated_event import (
        V1CustomerTaxIdUpdatedEvent as V1CustomerTaxIdUpdatedEvent,
        V1CustomerTaxIdUpdatedEventNotification as V1CustomerTaxIdUpdatedEventNotification,
    )
    from stripe.events._v1_customer_updated_event import (
        V1CustomerUpdatedEvent as V1CustomerUpdatedEvent,
        V1CustomerUpdatedEventNotification as V1CustomerUpdatedEventNotification,
    )
    from stripe.events._v1_entitlements_active_entitlement_summary_entitlement_added_event import (
        V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent as V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent,
        V1EntitlementsActiveEntitlementSummaryEntitlementAddedEventNotification as V1EntitlementsActiveEntitlementSummaryEntitlementAddedEventNotification,
    )
    from stripe.events._v1_entitlements_active_entitlement_summary_entitlement_removed_event import (
        V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent as V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent,
        V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEventNotification as V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEventNotification,
    )
    from stripe.events._v1_entitlements_active_entitlement_summary_updated_event import (
        V1EntitlementsActiveEntitlementSummaryUpdatedEvent as V1EntitlementsActiveEntitlementSummaryUpdatedEvent,
        V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification as V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification,
    )
    from stripe.events._v1_file_created_event import (
        V1FileCreatedEvent as V1FileCreatedEvent,
        V1FileCreatedEventNotification as V1FileCreatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_account_numbers_updated_event import (
        V1FinancialConnectionsAccountAccountNumbersUpdatedEvent as V1FinancialConnectionsAccountAccountNumbersUpdatedEvent,
        V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification as V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_balance_refresh_failed_event import (
        V1FinancialConnectionsAccountBalanceRefreshFailedEvent as V1FinancialConnectionsAccountBalanceRefreshFailedEvent,
        V1FinancialConnectionsAccountBalanceRefreshFailedEventNotification as V1FinancialConnectionsAccountBalanceRefreshFailedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_balance_refresh_succeeded_event import (
        V1FinancialConnectionsAccountBalanceRefreshSucceededEvent as V1FinancialConnectionsAccountBalanceRefreshSucceededEvent,
        V1FinancialConnectionsAccountBalanceRefreshSucceededEventNotification as V1FinancialConnectionsAccountBalanceRefreshSucceededEventNotification,
    )
    from stripe.events._v1_financial_connections_account_created_event import (
        V1FinancialConnectionsAccountCreatedEvent as V1FinancialConnectionsAccountCreatedEvent,
        V1FinancialConnectionsAccountCreatedEventNotification as V1FinancialConnectionsAccountCreatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_deactivated_event import (
        V1FinancialConnectionsAccountDeactivatedEvent as V1FinancialConnectionsAccountDeactivatedEvent,
        V1FinancialConnectionsAccountDeactivatedEventNotification as V1FinancialConnectionsAccountDeactivatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_disconnected_event import (
        V1FinancialConnectionsAccountDisconnectedEvent as V1FinancialConnectionsAccountDisconnectedEvent,
        V1FinancialConnectionsAccountDisconnectedEventNotification as V1FinancialConnectionsAccountDisconnectedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event import (
        V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent as V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent,
        V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification as V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_inferred_balances_refresh_failed_event import (
        V1FinancialConnectionsAccountInferredBalancesRefreshFailedEvent as V1FinancialConnectionsAccountInferredBalancesRefreshFailedEvent,
        V1FinancialConnectionsAccountInferredBalancesRefreshFailedEventNotification as V1FinancialConnectionsAccountInferredBalancesRefreshFailedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_inferred_balances_refresh_succeeded_event import (
        V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEvent as V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEvent,
        V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEventNotification as V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEventNotification,
    )
    from stripe.events._v1_financial_connections_account_ownership_refresh_failed_event import (
        V1FinancialConnectionsAccountOwnershipRefreshFailedEvent as V1FinancialConnectionsAccountOwnershipRefreshFailedEvent,
        V1FinancialConnectionsAccountOwnershipRefreshFailedEventNotification as V1FinancialConnectionsAccountOwnershipRefreshFailedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_ownership_refresh_succeeded_event import (
        V1FinancialConnectionsAccountOwnershipRefreshSucceededEvent as V1FinancialConnectionsAccountOwnershipRefreshSucceededEvent,
        V1FinancialConnectionsAccountOwnershipRefreshSucceededEventNotification as V1FinancialConnectionsAccountOwnershipRefreshSucceededEventNotification,
    )
    from stripe.events._v1_financial_connections_account_reactivated_event import (
        V1FinancialConnectionsAccountReactivatedEvent as V1FinancialConnectionsAccountReactivatedEvent,
        V1FinancialConnectionsAccountReactivatedEventNotification as V1FinancialConnectionsAccountReactivatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_balance_event import (
        V1FinancialConnectionsAccountRefreshedBalanceEvent as V1FinancialConnectionsAccountRefreshedBalanceEvent,
        V1FinancialConnectionsAccountRefreshedBalanceEventNotification as V1FinancialConnectionsAccountRefreshedBalanceEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_ownership_event import (
        V1FinancialConnectionsAccountRefreshedOwnershipEvent as V1FinancialConnectionsAccountRefreshedOwnershipEvent,
        V1FinancialConnectionsAccountRefreshedOwnershipEventNotification as V1FinancialConnectionsAccountRefreshedOwnershipEventNotification,
    )
    from stripe.events._v1_financial_connections_account_refreshed_transactions_event import (
        V1FinancialConnectionsAccountRefreshedTransactionsEvent as V1FinancialConnectionsAccountRefreshedTransactionsEvent,
        V1FinancialConnectionsAccountRefreshedTransactionsEventNotification as V1FinancialConnectionsAccountRefreshedTransactionsEventNotification,
    )
    from stripe.events._v1_financial_connections_account_risk_intelligence_refresh_failed_event import (
        V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEvent as V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEvent,
        V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEventNotification as V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_risk_intelligence_refresh_succeeded_event import (
        V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEvent as V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEvent,
        V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEventNotification as V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEventNotification,
    )
    from stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event import (
        V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent as V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent,
        V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification as V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_transactions_refresh_failed_event import (
        V1FinancialConnectionsAccountTransactionsRefreshFailedEvent as V1FinancialConnectionsAccountTransactionsRefreshFailedEvent,
        V1FinancialConnectionsAccountTransactionsRefreshFailedEventNotification as V1FinancialConnectionsAccountTransactionsRefreshFailedEventNotification,
    )
    from stripe.events._v1_financial_connections_account_transactions_refresh_succeeded_event import (
        V1FinancialConnectionsAccountTransactionsRefreshSucceededEvent as V1FinancialConnectionsAccountTransactionsRefreshSucceededEvent,
        V1FinancialConnectionsAccountTransactionsRefreshSucceededEventNotification as V1FinancialConnectionsAccountTransactionsRefreshSucceededEventNotification,
    )
    from stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event import (
        V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent as V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent,
        V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification as V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification,
    )
    from stripe.events._v1_financial_connections_account_upcoming_deactivation_event import (
        V1FinancialConnectionsAccountUpcomingDeactivationEvent as V1FinancialConnectionsAccountUpcomingDeactivationEvent,
        V1FinancialConnectionsAccountUpcomingDeactivationEventNotification as V1FinancialConnectionsAccountUpcomingDeactivationEventNotification,
    )
    from stripe.events._v1_identity_verification_session_canceled_event import (
        V1IdentityVerificationSessionCanceledEvent as V1IdentityVerificationSessionCanceledEvent,
        V1IdentityVerificationSessionCanceledEventNotification as V1IdentityVerificationSessionCanceledEventNotification,
    )
    from stripe.events._v1_identity_verification_session_created_event import (
        V1IdentityVerificationSessionCreatedEvent as V1IdentityVerificationSessionCreatedEvent,
        V1IdentityVerificationSessionCreatedEventNotification as V1IdentityVerificationSessionCreatedEventNotification,
    )
    from stripe.events._v1_identity_verification_session_processing_event import (
        V1IdentityVerificationSessionProcessingEvent as V1IdentityVerificationSessionProcessingEvent,
        V1IdentityVerificationSessionProcessingEventNotification as V1IdentityVerificationSessionProcessingEventNotification,
    )
    from stripe.events._v1_identity_verification_session_redacted_event import (
        V1IdentityVerificationSessionRedactedEvent as V1IdentityVerificationSessionRedactedEvent,
        V1IdentityVerificationSessionRedactedEventNotification as V1IdentityVerificationSessionRedactedEventNotification,
    )
    from stripe.events._v1_identity_verification_session_requires_input_event import (
        V1IdentityVerificationSessionRequiresInputEvent as V1IdentityVerificationSessionRequiresInputEvent,
        V1IdentityVerificationSessionRequiresInputEventNotification as V1IdentityVerificationSessionRequiresInputEventNotification,
    )
    from stripe.events._v1_identity_verification_session_verified_event import (
        V1IdentityVerificationSessionVerifiedEvent as V1IdentityVerificationSessionVerifiedEvent,
        V1IdentityVerificationSessionVerifiedEventNotification as V1IdentityVerificationSessionVerifiedEventNotification,
    )
    from stripe.events._v1_invoice_created_event import (
        V1InvoiceCreatedEvent as V1InvoiceCreatedEvent,
        V1InvoiceCreatedEventNotification as V1InvoiceCreatedEventNotification,
    )
    from stripe.events._v1_invoice_deleted_event import (
        V1InvoiceDeletedEvent as V1InvoiceDeletedEvent,
        V1InvoiceDeletedEventNotification as V1InvoiceDeletedEventNotification,
    )
    from stripe.events._v1_invoice_discount_added_event import (
        V1InvoiceDiscountAddedEvent as V1InvoiceDiscountAddedEvent,
        V1InvoiceDiscountAddedEventNotification as V1InvoiceDiscountAddedEventNotification,
    )
    from stripe.events._v1_invoice_discount_removed_event import (
        V1InvoiceDiscountRemovedEvent as V1InvoiceDiscountRemovedEvent,
        V1InvoiceDiscountRemovedEventNotification as V1InvoiceDiscountRemovedEventNotification,
    )
    from stripe.events._v1_invoice_finalization_failed_event import (
        V1InvoiceFinalizationFailedEvent as V1InvoiceFinalizationFailedEvent,
        V1InvoiceFinalizationFailedEventNotification as V1InvoiceFinalizationFailedEventNotification,
    )
    from stripe.events._v1_invoice_finalized_event import (
        V1InvoiceFinalizedEvent as V1InvoiceFinalizedEvent,
        V1InvoiceFinalizedEventNotification as V1InvoiceFinalizedEventNotification,
    )
    from stripe.events._v1_invoice_line_item_added_event import (
        V1InvoiceLineItemAddedEvent as V1InvoiceLineItemAddedEvent,
        V1InvoiceLineItemAddedEventNotification as V1InvoiceLineItemAddedEventNotification,
    )
    from stripe.events._v1_invoice_line_item_pricing_changed_event import (
        V1InvoiceLineItemPricingChangedEvent as V1InvoiceLineItemPricingChangedEvent,
        V1InvoiceLineItemPricingChangedEventNotification as V1InvoiceLineItemPricingChangedEventNotification,
    )
    from stripe.events._v1_invoice_line_item_quantity_changed_event import (
        V1InvoiceLineItemQuantityChangedEvent as V1InvoiceLineItemQuantityChangedEvent,
        V1InvoiceLineItemQuantityChangedEventNotification as V1InvoiceLineItemQuantityChangedEventNotification,
    )
    from stripe.events._v1_invoice_line_item_removed_event import (
        V1InvoiceLineItemRemovedEvent as V1InvoiceLineItemRemovedEvent,
        V1InvoiceLineItemRemovedEventNotification as V1InvoiceLineItemRemovedEventNotification,
    )
    from stripe.events._v1_invoice_marked_uncollectible_event import (
        V1InvoiceMarkedUncollectibleEvent as V1InvoiceMarkedUncollectibleEvent,
        V1InvoiceMarkedUncollectibleEventNotification as V1InvoiceMarkedUncollectibleEventNotification,
    )
    from stripe.events._v1_invoice_overdue_event import (
        V1InvoiceOverdueEvent as V1InvoiceOverdueEvent,
        V1InvoiceOverdueEventNotification as V1InvoiceOverdueEventNotification,
    )
    from stripe.events._v1_invoice_overpaid_event import (
        V1InvoiceOverpaidEvent as V1InvoiceOverpaidEvent,
        V1InvoiceOverpaidEventNotification as V1InvoiceOverpaidEventNotification,
    )
    from stripe.events._v1_invoice_paid_event import (
        V1InvoicePaidEvent as V1InvoicePaidEvent,
        V1InvoicePaidEventNotification as V1InvoicePaidEventNotification,
    )
    from stripe.events._v1_invoice_payment_action_required_event import (
        V1InvoicePaymentActionRequiredEvent as V1InvoicePaymentActionRequiredEvent,
        V1InvoicePaymentActionRequiredEventNotification as V1InvoicePaymentActionRequiredEventNotification,
    )
    from stripe.events._v1_invoice_payment_attempt_required_event import (
        V1InvoicePaymentAttemptRequiredEvent as V1InvoicePaymentAttemptRequiredEvent,
        V1InvoicePaymentAttemptRequiredEventNotification as V1InvoicePaymentAttemptRequiredEventNotification,
    )
    from stripe.events._v1_invoice_payment_canceled_event import (
        V1InvoicePaymentCanceledEvent as V1InvoicePaymentCanceledEvent,
        V1InvoicePaymentCanceledEventNotification as V1InvoicePaymentCanceledEventNotification,
    )
    from stripe.events._v1_invoice_payment_failed_event import (
        V1InvoicePaymentFailedEvent as V1InvoicePaymentFailedEvent,
        V1InvoicePaymentFailedEventNotification as V1InvoicePaymentFailedEventNotification,
    )
    from stripe.events._v1_invoice_payment_open_event import (
        V1InvoicePaymentOpenEvent as V1InvoicePaymentOpenEvent,
        V1InvoicePaymentOpenEventNotification as V1InvoicePaymentOpenEventNotification,
    )
    from stripe.events._v1_invoice_payment_paid_event import (
        V1InvoicePaymentPaidEvent as V1InvoicePaymentPaidEvent,
        V1InvoicePaymentPaidEventNotification as V1InvoicePaymentPaidEventNotification,
    )
    from stripe.events._v1_invoice_payment_succeeded_event import (
        V1InvoicePaymentSucceededEvent as V1InvoicePaymentSucceededEvent,
        V1InvoicePaymentSucceededEventNotification as V1InvoicePaymentSucceededEventNotification,
    )
    from stripe.events._v1_invoice_sent_event import (
        V1InvoiceSentEvent as V1InvoiceSentEvent,
        V1InvoiceSentEventNotification as V1InvoiceSentEventNotification,
    )
    from stripe.events._v1_invoice_upcoming_event import (
        V1InvoiceUpcomingEvent as V1InvoiceUpcomingEvent,
        V1InvoiceUpcomingEventNotification as V1InvoiceUpcomingEventNotification,
    )
    from stripe.events._v1_invoice_updated_event import (
        V1InvoiceUpdatedEvent as V1InvoiceUpdatedEvent,
        V1InvoiceUpdatedEventNotification as V1InvoiceUpdatedEventNotification,
    )
    from stripe.events._v1_invoice_voided_event import (
        V1InvoiceVoidedEvent as V1InvoiceVoidedEvent,
        V1InvoiceVoidedEventNotification as V1InvoiceVoidedEventNotification,
    )
    from stripe.events._v1_invoice_will_be_due_event import (
        V1InvoiceWillBeDueEvent as V1InvoiceWillBeDueEvent,
        V1InvoiceWillBeDueEventNotification as V1InvoiceWillBeDueEventNotification,
    )
    from stripe.events._v1_invoiceitem_amount_changed_event import (
        V1InvoiceitemAmountChangedEvent as V1InvoiceitemAmountChangedEvent,
        V1InvoiceitemAmountChangedEventNotification as V1InvoiceitemAmountChangedEventNotification,
    )
    from stripe.events._v1_invoiceitem_created_event import (
        V1InvoiceitemCreatedEvent as V1InvoiceitemCreatedEvent,
        V1InvoiceitemCreatedEventNotification as V1InvoiceitemCreatedEventNotification,
    )
    from stripe.events._v1_invoiceitem_deleted_event import (
        V1InvoiceitemDeletedEvent as V1InvoiceitemDeletedEvent,
        V1InvoiceitemDeletedEventNotification as V1InvoiceitemDeletedEventNotification,
    )
    from stripe.events._v1_invoiceitem_discount_added_event import (
        V1InvoiceitemDiscountAddedEvent as V1InvoiceitemDiscountAddedEvent,
        V1InvoiceitemDiscountAddedEventNotification as V1InvoiceitemDiscountAddedEventNotification,
    )
    from stripe.events._v1_invoiceitem_discount_removed_event import (
        V1InvoiceitemDiscountRemovedEvent as V1InvoiceitemDiscountRemovedEvent,
        V1InvoiceitemDiscountRemovedEventNotification as V1InvoiceitemDiscountRemovedEventNotification,
    )
    from stripe.events._v1_issuing_authorization_created_event import (
        V1IssuingAuthorizationCreatedEvent as V1IssuingAuthorizationCreatedEvent,
        V1IssuingAuthorizationCreatedEventNotification as V1IssuingAuthorizationCreatedEventNotification,
    )
    from stripe.events._v1_issuing_authorization_request_event import (
        V1IssuingAuthorizationRequestEvent as V1IssuingAuthorizationRequestEvent,
        V1IssuingAuthorizationRequestEventNotification as V1IssuingAuthorizationRequestEventNotification,
    )
    from stripe.events._v1_issuing_authorization_updated_event import (
        V1IssuingAuthorizationUpdatedEvent as V1IssuingAuthorizationUpdatedEvent,
        V1IssuingAuthorizationUpdatedEventNotification as V1IssuingAuthorizationUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_card_created_event import (
        V1IssuingCardCreatedEvent as V1IssuingCardCreatedEvent,
        V1IssuingCardCreatedEventNotification as V1IssuingCardCreatedEventNotification,
    )
    from stripe.events._v1_issuing_card_updated_event import (
        V1IssuingCardUpdatedEvent as V1IssuingCardUpdatedEvent,
        V1IssuingCardUpdatedEventNotification as V1IssuingCardUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_created_event import (
        V1IssuingCardholderCreatedEvent as V1IssuingCardholderCreatedEvent,
        V1IssuingCardholderCreatedEventNotification as V1IssuingCardholderCreatedEventNotification,
    )
    from stripe.events._v1_issuing_cardholder_updated_event import (
        V1IssuingCardholderUpdatedEvent as V1IssuingCardholderUpdatedEvent,
        V1IssuingCardholderUpdatedEventNotification as V1IssuingCardholderUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_closed_event import (
        V1IssuingDisputeClosedEvent as V1IssuingDisputeClosedEvent,
        V1IssuingDisputeClosedEventNotification as V1IssuingDisputeClosedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_created_event import (
        V1IssuingDisputeCreatedEvent as V1IssuingDisputeCreatedEvent,
        V1IssuingDisputeCreatedEventNotification as V1IssuingDisputeCreatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_funds_reinstated_event import (
        V1IssuingDisputeFundsReinstatedEvent as V1IssuingDisputeFundsReinstatedEvent,
        V1IssuingDisputeFundsReinstatedEventNotification as V1IssuingDisputeFundsReinstatedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_funds_rescinded_event import (
        V1IssuingDisputeFundsRescindedEvent as V1IssuingDisputeFundsRescindedEvent,
        V1IssuingDisputeFundsRescindedEventNotification as V1IssuingDisputeFundsRescindedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_submitted_event import (
        V1IssuingDisputeSubmittedEvent as V1IssuingDisputeSubmittedEvent,
        V1IssuingDisputeSubmittedEventNotification as V1IssuingDisputeSubmittedEventNotification,
    )
    from stripe.events._v1_issuing_dispute_updated_event import (
        V1IssuingDisputeUpdatedEvent as V1IssuingDisputeUpdatedEvent,
        V1IssuingDisputeUpdatedEventNotification as V1IssuingDisputeUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_activated_event import (
        V1IssuingPersonalizationDesignActivatedEvent as V1IssuingPersonalizationDesignActivatedEvent,
        V1IssuingPersonalizationDesignActivatedEventNotification as V1IssuingPersonalizationDesignActivatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_deactivated_event import (
        V1IssuingPersonalizationDesignDeactivatedEvent as V1IssuingPersonalizationDesignDeactivatedEvent,
        V1IssuingPersonalizationDesignDeactivatedEventNotification as V1IssuingPersonalizationDesignDeactivatedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_rejected_event import (
        V1IssuingPersonalizationDesignRejectedEvent as V1IssuingPersonalizationDesignRejectedEvent,
        V1IssuingPersonalizationDesignRejectedEventNotification as V1IssuingPersonalizationDesignRejectedEventNotification,
    )
    from stripe.events._v1_issuing_personalization_design_updated_event import (
        V1IssuingPersonalizationDesignUpdatedEvent as V1IssuingPersonalizationDesignUpdatedEvent,
        V1IssuingPersonalizationDesignUpdatedEventNotification as V1IssuingPersonalizationDesignUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_token_created_event import (
        V1IssuingTokenCreatedEvent as V1IssuingTokenCreatedEvent,
        V1IssuingTokenCreatedEventNotification as V1IssuingTokenCreatedEventNotification,
    )
    from stripe.events._v1_issuing_token_updated_event import (
        V1IssuingTokenUpdatedEvent as V1IssuingTokenUpdatedEvent,
        V1IssuingTokenUpdatedEventNotification as V1IssuingTokenUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_created_event import (
        V1IssuingTransactionCreatedEvent as V1IssuingTransactionCreatedEvent,
        V1IssuingTransactionCreatedEventNotification as V1IssuingTransactionCreatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event import (
        V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent as V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent,
        V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification as V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification,
    )
    from stripe.events._v1_issuing_transaction_updated_event import (
        V1IssuingTransactionUpdatedEvent as V1IssuingTransactionUpdatedEvent,
        V1IssuingTransactionUpdatedEventNotification as V1IssuingTransactionUpdatedEventNotification,
    )
    from stripe.events._v1_mandate_updated_event import (
        V1MandateUpdatedEvent as V1MandateUpdatedEvent,
        V1MandateUpdatedEventNotification as V1MandateUpdatedEventNotification,
    )
    from stripe.events._v1_payment_intent_amount_capturable_updated_event import (
        V1PaymentIntentAmountCapturableUpdatedEvent as V1PaymentIntentAmountCapturableUpdatedEvent,
        V1PaymentIntentAmountCapturableUpdatedEventNotification as V1PaymentIntentAmountCapturableUpdatedEventNotification,
    )
    from stripe.events._v1_payment_intent_canceled_event import (
        V1PaymentIntentCanceledEvent as V1PaymentIntentCanceledEvent,
        V1PaymentIntentCanceledEventNotification as V1PaymentIntentCanceledEventNotification,
    )
    from stripe.events._v1_payment_intent_created_event import (
        V1PaymentIntentCreatedEvent as V1PaymentIntentCreatedEvent,
        V1PaymentIntentCreatedEventNotification as V1PaymentIntentCreatedEventNotification,
    )
    from stripe.events._v1_payment_intent_partially_funded_event import (
        V1PaymentIntentPartiallyFundedEvent as V1PaymentIntentPartiallyFundedEvent,
        V1PaymentIntentPartiallyFundedEventNotification as V1PaymentIntentPartiallyFundedEventNotification,
    )
    from stripe.events._v1_payment_intent_payment_failed_event import (
        V1PaymentIntentPaymentFailedEvent as V1PaymentIntentPaymentFailedEvent,
        V1PaymentIntentPaymentFailedEventNotification as V1PaymentIntentPaymentFailedEventNotification,
    )
    from stripe.events._v1_payment_intent_processing_event import (
        V1PaymentIntentProcessingEvent as V1PaymentIntentProcessingEvent,
        V1PaymentIntentProcessingEventNotification as V1PaymentIntentProcessingEventNotification,
    )
    from stripe.events._v1_payment_intent_requires_action_event import (
        V1PaymentIntentRequiresActionEvent as V1PaymentIntentRequiresActionEvent,
        V1PaymentIntentRequiresActionEventNotification as V1PaymentIntentRequiresActionEventNotification,
    )
    from stripe.events._v1_payment_intent_succeeded_event import (
        V1PaymentIntentSucceededEvent as V1PaymentIntentSucceededEvent,
        V1PaymentIntentSucceededEventNotification as V1PaymentIntentSucceededEventNotification,
    )
    from stripe.events._v1_payment_link_created_event import (
        V1PaymentLinkCreatedEvent as V1PaymentLinkCreatedEvent,
        V1PaymentLinkCreatedEventNotification as V1PaymentLinkCreatedEventNotification,
    )
    from stripe.events._v1_payment_link_updated_event import (
        V1PaymentLinkUpdatedEvent as V1PaymentLinkUpdatedEvent,
        V1PaymentLinkUpdatedEventNotification as V1PaymentLinkUpdatedEventNotification,
    )
    from stripe.events._v1_payment_method_attached_event import (
        V1PaymentMethodAttachedEvent as V1PaymentMethodAttachedEvent,
        V1PaymentMethodAttachedEventNotification as V1PaymentMethodAttachedEventNotification,
    )
    from stripe.events._v1_payment_method_automatically_updated_event import (
        V1PaymentMethodAutomaticallyUpdatedEvent as V1PaymentMethodAutomaticallyUpdatedEvent,
        V1PaymentMethodAutomaticallyUpdatedEventNotification as V1PaymentMethodAutomaticallyUpdatedEventNotification,
    )
    from stripe.events._v1_payment_method_detached_event import (
        V1PaymentMethodDetachedEvent as V1PaymentMethodDetachedEvent,
        V1PaymentMethodDetachedEventNotification as V1PaymentMethodDetachedEventNotification,
    )
    from stripe.events._v1_payment_method_updated_event import (
        V1PaymentMethodUpdatedEvent as V1PaymentMethodUpdatedEvent,
        V1PaymentMethodUpdatedEventNotification as V1PaymentMethodUpdatedEventNotification,
    )
    from stripe.events._v1_payout_canceled_event import (
        V1PayoutCanceledEvent as V1PayoutCanceledEvent,
        V1PayoutCanceledEventNotification as V1PayoutCanceledEventNotification,
    )
    from stripe.events._v1_payout_created_event import (
        V1PayoutCreatedEvent as V1PayoutCreatedEvent,
        V1PayoutCreatedEventNotification as V1PayoutCreatedEventNotification,
    )
    from stripe.events._v1_payout_failed_event import (
        V1PayoutFailedEvent as V1PayoutFailedEvent,
        V1PayoutFailedEventNotification as V1PayoutFailedEventNotification,
    )
    from stripe.events._v1_payout_paid_event import (
        V1PayoutPaidEvent as V1PayoutPaidEvent,
        V1PayoutPaidEventNotification as V1PayoutPaidEventNotification,
    )
    from stripe.events._v1_payout_reconciliation_completed_event import (
        V1PayoutReconciliationCompletedEvent as V1PayoutReconciliationCompletedEvent,
        V1PayoutReconciliationCompletedEventNotification as V1PayoutReconciliationCompletedEventNotification,
    )
    from stripe.events._v1_payout_updated_event import (
        V1PayoutUpdatedEvent as V1PayoutUpdatedEvent,
        V1PayoutUpdatedEventNotification as V1PayoutUpdatedEventNotification,
    )
    from stripe.events._v1_person_created_event import (
        V1PersonCreatedEvent as V1PersonCreatedEvent,
        V1PersonCreatedEventNotification as V1PersonCreatedEventNotification,
    )
    from stripe.events._v1_person_deleted_event import (
        V1PersonDeletedEvent as V1PersonDeletedEvent,
        V1PersonDeletedEventNotification as V1PersonDeletedEventNotification,
    )
    from stripe.events._v1_person_updated_event import (
        V1PersonUpdatedEvent as V1PersonUpdatedEvent,
        V1PersonUpdatedEventNotification as V1PersonUpdatedEventNotification,
    )
    from stripe.events._v1_plan_created_event import (
        V1PlanCreatedEvent as V1PlanCreatedEvent,
        V1PlanCreatedEventNotification as V1PlanCreatedEventNotification,
    )
    from stripe.events._v1_plan_deleted_event import (
        V1PlanDeletedEvent as V1PlanDeletedEvent,
        V1PlanDeletedEventNotification as V1PlanDeletedEventNotification,
    )
    from stripe.events._v1_plan_updated_event import (
        V1PlanUpdatedEvent as V1PlanUpdatedEvent,
        V1PlanUpdatedEventNotification as V1PlanUpdatedEventNotification,
    )
    from stripe.events._v1_price_activated_event import (
        V1PriceActivatedEvent as V1PriceActivatedEvent,
        V1PriceActivatedEventNotification as V1PriceActivatedEventNotification,
    )
    from stripe.events._v1_price_created_event import (
        V1PriceCreatedEvent as V1PriceCreatedEvent,
        V1PriceCreatedEventNotification as V1PriceCreatedEventNotification,
    )
    from stripe.events._v1_price_deactivated_event import (
        V1PriceDeactivatedEvent as V1PriceDeactivatedEvent,
        V1PriceDeactivatedEventNotification as V1PriceDeactivatedEventNotification,
    )
    from stripe.events._v1_price_deleted_event import (
        V1PriceDeletedEvent as V1PriceDeletedEvent,
        V1PriceDeletedEventNotification as V1PriceDeletedEventNotification,
    )
    from stripe.events._v1_price_lookup_key_changed_event import (
        V1PriceLookupKeyChangedEvent as V1PriceLookupKeyChangedEvent,
        V1PriceLookupKeyChangedEventNotification as V1PriceLookupKeyChangedEventNotification,
    )
    from stripe.events._v1_price_tax_behavior_changed_event import (
        V1PriceTaxBehaviorChangedEvent as V1PriceTaxBehaviorChangedEvent,
        V1PriceTaxBehaviorChangedEventNotification as V1PriceTaxBehaviorChangedEventNotification,
    )
    from stripe.events._v1_price_updated_event import (
        V1PriceUpdatedEvent as V1PriceUpdatedEvent,
        V1PriceUpdatedEventNotification as V1PriceUpdatedEventNotification,
    )
    from stripe.events._v1_product_activated_event import (
        V1ProductActivatedEvent as V1ProductActivatedEvent,
        V1ProductActivatedEventNotification as V1ProductActivatedEventNotification,
    )
    from stripe.events._v1_product_created_event import (
        V1ProductCreatedEvent as V1ProductCreatedEvent,
        V1ProductCreatedEventNotification as V1ProductCreatedEventNotification,
    )
    from stripe.events._v1_product_deactivated_event import (
        V1ProductDeactivatedEvent as V1ProductDeactivatedEvent,
        V1ProductDeactivatedEventNotification as V1ProductDeactivatedEventNotification,
    )
    from stripe.events._v1_product_default_price_changed_event import (
        V1ProductDefaultPriceChangedEvent as V1ProductDefaultPriceChangedEvent,
        V1ProductDefaultPriceChangedEventNotification as V1ProductDefaultPriceChangedEventNotification,
    )
    from stripe.events._v1_product_deleted_event import (
        V1ProductDeletedEvent as V1ProductDeletedEvent,
        V1ProductDeletedEventNotification as V1ProductDeletedEventNotification,
    )
    from stripe.events._v1_product_tax_code_changed_event import (
        V1ProductTaxCodeChangedEvent as V1ProductTaxCodeChangedEvent,
        V1ProductTaxCodeChangedEventNotification as V1ProductTaxCodeChangedEventNotification,
    )
    from stripe.events._v1_product_updated_event import (
        V1ProductUpdatedEvent as V1ProductUpdatedEvent,
        V1ProductUpdatedEventNotification as V1ProductUpdatedEventNotification,
    )
    from stripe.events._v1_promotion_code_created_event import (
        V1PromotionCodeCreatedEvent as V1PromotionCodeCreatedEvent,
        V1PromotionCodeCreatedEventNotification as V1PromotionCodeCreatedEventNotification,
    )
    from stripe.events._v1_promotion_code_fully_redeemed_event import (
        V1PromotionCodeFullyRedeemedEvent as V1PromotionCodeFullyRedeemedEvent,
        V1PromotionCodeFullyRedeemedEventNotification as V1PromotionCodeFullyRedeemedEventNotification,
    )
    from stripe.events._v1_promotion_code_updated_event import (
        V1PromotionCodeUpdatedEvent as V1PromotionCodeUpdatedEvent,
        V1PromotionCodeUpdatedEventNotification as V1PromotionCodeUpdatedEventNotification,
    )
    from stripe.events._v1_quote_accepted_event import (
        V1QuoteAcceptedEvent as V1QuoteAcceptedEvent,
        V1QuoteAcceptedEventNotification as V1QuoteAcceptedEventNotification,
    )
    from stripe.events._v1_quote_canceled_event import (
        V1QuoteCanceledEvent as V1QuoteCanceledEvent,
        V1QuoteCanceledEventNotification as V1QuoteCanceledEventNotification,
    )
    from stripe.events._v1_quote_created_event import (
        V1QuoteCreatedEvent as V1QuoteCreatedEvent,
        V1QuoteCreatedEventNotification as V1QuoteCreatedEventNotification,
    )
    from stripe.events._v1_quote_finalized_event import (
        V1QuoteFinalizedEvent as V1QuoteFinalizedEvent,
        V1QuoteFinalizedEventNotification as V1QuoteFinalizedEventNotification,
    )
    from stripe.events._v1_radar_early_fraud_warning_created_event import (
        V1RadarEarlyFraudWarningCreatedEvent as V1RadarEarlyFraudWarningCreatedEvent,
        V1RadarEarlyFraudWarningCreatedEventNotification as V1RadarEarlyFraudWarningCreatedEventNotification,
    )
    from stripe.events._v1_radar_early_fraud_warning_updated_event import (
        V1RadarEarlyFraudWarningUpdatedEvent as V1RadarEarlyFraudWarningUpdatedEvent,
        V1RadarEarlyFraudWarningUpdatedEventNotification as V1RadarEarlyFraudWarningUpdatedEventNotification,
    )
    from stripe.events._v1_refund_created_event import (
        V1RefundCreatedEvent as V1RefundCreatedEvent,
        V1RefundCreatedEventNotification as V1RefundCreatedEventNotification,
    )
    from stripe.events._v1_refund_failed_event import (
        V1RefundFailedEvent as V1RefundFailedEvent,
        V1RefundFailedEventNotification as V1RefundFailedEventNotification,
    )
    from stripe.events._v1_refund_updated_event import (
        V1RefundUpdatedEvent as V1RefundUpdatedEvent,
        V1RefundUpdatedEventNotification as V1RefundUpdatedEventNotification,
    )
    from stripe.events._v1_review_closed_event import (
        V1ReviewClosedEvent as V1ReviewClosedEvent,
        V1ReviewClosedEventNotification as V1ReviewClosedEventNotification,
    )
    from stripe.events._v1_review_opened_event import (
        V1ReviewOpenedEvent as V1ReviewOpenedEvent,
        V1ReviewOpenedEventNotification as V1ReviewOpenedEventNotification,
    )
    from stripe.events._v1_setup_intent_canceled_event import (
        V1SetupIntentCanceledEvent as V1SetupIntentCanceledEvent,
        V1SetupIntentCanceledEventNotification as V1SetupIntentCanceledEventNotification,
    )
    from stripe.events._v1_setup_intent_created_event import (
        V1SetupIntentCreatedEvent as V1SetupIntentCreatedEvent,
        V1SetupIntentCreatedEventNotification as V1SetupIntentCreatedEventNotification,
    )
    from stripe.events._v1_setup_intent_requires_action_event import (
        V1SetupIntentRequiresActionEvent as V1SetupIntentRequiresActionEvent,
        V1SetupIntentRequiresActionEventNotification as V1SetupIntentRequiresActionEventNotification,
    )
    from stripe.events._v1_setup_intent_setup_failed_event import (
        V1SetupIntentSetupFailedEvent as V1SetupIntentSetupFailedEvent,
        V1SetupIntentSetupFailedEventNotification as V1SetupIntentSetupFailedEventNotification,
    )
    from stripe.events._v1_setup_intent_succeeded_event import (
        V1SetupIntentSucceededEvent as V1SetupIntentSucceededEvent,
        V1SetupIntentSucceededEventNotification as V1SetupIntentSucceededEventNotification,
    )
    from stripe.events._v1_sigma_scheduled_query_run_created_event import (
        V1SigmaScheduledQueryRunCreatedEvent as V1SigmaScheduledQueryRunCreatedEvent,
        V1SigmaScheduledQueryRunCreatedEventNotification as V1SigmaScheduledQueryRunCreatedEventNotification,
    )
    from stripe.events._v1_source_canceled_event import (
        V1SourceCanceledEvent as V1SourceCanceledEvent,
        V1SourceCanceledEventNotification as V1SourceCanceledEventNotification,
    )
    from stripe.events._v1_source_chargeable_event import (
        V1SourceChargeableEvent as V1SourceChargeableEvent,
        V1SourceChargeableEventNotification as V1SourceChargeableEventNotification,
    )
    from stripe.events._v1_source_failed_event import (
        V1SourceFailedEvent as V1SourceFailedEvent,
        V1SourceFailedEventNotification as V1SourceFailedEventNotification,
    )
    from stripe.events._v1_source_refund_attributes_required_event import (
        V1SourceRefundAttributesRequiredEvent as V1SourceRefundAttributesRequiredEvent,
        V1SourceRefundAttributesRequiredEventNotification as V1SourceRefundAttributesRequiredEventNotification,
    )
    from stripe.events._v1_subscription_schedule_aborted_event import (
        V1SubscriptionScheduleAbortedEvent as V1SubscriptionScheduleAbortedEvent,
        V1SubscriptionScheduleAbortedEventNotification as V1SubscriptionScheduleAbortedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_canceled_event import (
        V1SubscriptionScheduleCanceledEvent as V1SubscriptionScheduleCanceledEvent,
        V1SubscriptionScheduleCanceledEventNotification as V1SubscriptionScheduleCanceledEventNotification,
    )
    from stripe.events._v1_subscription_schedule_completed_event import (
        V1SubscriptionScheduleCompletedEvent as V1SubscriptionScheduleCompletedEvent,
        V1SubscriptionScheduleCompletedEventNotification as V1SubscriptionScheduleCompletedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_created_event import (
        V1SubscriptionScheduleCreatedEvent as V1SubscriptionScheduleCreatedEvent,
        V1SubscriptionScheduleCreatedEventNotification as V1SubscriptionScheduleCreatedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_expiring_event import (
        V1SubscriptionScheduleExpiringEvent as V1SubscriptionScheduleExpiringEvent,
        V1SubscriptionScheduleExpiringEventNotification as V1SubscriptionScheduleExpiringEventNotification,
    )
    from stripe.events._v1_subscription_schedule_phase_added_event import (
        V1SubscriptionSchedulePhaseAddedEvent as V1SubscriptionSchedulePhaseAddedEvent,
        V1SubscriptionSchedulePhaseAddedEventNotification as V1SubscriptionSchedulePhaseAddedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_phase_default_tax_rates_changed_event import (
        V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEvent as V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEvent,
        V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEventNotification as V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_phase_end_date_changed_event import (
        V1SubscriptionSchedulePhaseEndDateChangedEvent as V1SubscriptionSchedulePhaseEndDateChangedEvent,
        V1SubscriptionSchedulePhaseEndDateChangedEventNotification as V1SubscriptionSchedulePhaseEndDateChangedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_phase_removed_event import (
        V1SubscriptionSchedulePhaseRemovedEvent as V1SubscriptionSchedulePhaseRemovedEvent,
        V1SubscriptionSchedulePhaseRemovedEventNotification as V1SubscriptionSchedulePhaseRemovedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_phase_trial_end_changed_event import (
        V1SubscriptionSchedulePhaseTrialEndChangedEvent as V1SubscriptionSchedulePhaseTrialEndChangedEvent,
        V1SubscriptionSchedulePhaseTrialEndChangedEventNotification as V1SubscriptionSchedulePhaseTrialEndChangedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_released_event import (
        V1SubscriptionScheduleReleasedEvent as V1SubscriptionScheduleReleasedEvent,
        V1SubscriptionScheduleReleasedEventNotification as V1SubscriptionScheduleReleasedEventNotification,
    )
    from stripe.events._v1_subscription_schedule_updated_event import (
        V1SubscriptionScheduleUpdatedEvent as V1SubscriptionScheduleUpdatedEvent,
        V1SubscriptionScheduleUpdatedEventNotification as V1SubscriptionScheduleUpdatedEventNotification,
    )
    from stripe.events._v1_tax_rate_created_event import (
        V1TaxRateCreatedEvent as V1TaxRateCreatedEvent,
        V1TaxRateCreatedEventNotification as V1TaxRateCreatedEventNotification,
    )
    from stripe.events._v1_tax_rate_updated_event import (
        V1TaxRateUpdatedEvent as V1TaxRateUpdatedEvent,
        V1TaxRateUpdatedEventNotification as V1TaxRateUpdatedEventNotification,
    )
    from stripe.events._v1_tax_settings_updated_event import (
        V1TaxSettingsUpdatedEvent as V1TaxSettingsUpdatedEvent,
        V1TaxSettingsUpdatedEventNotification as V1TaxSettingsUpdatedEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_failed_event import (
        V1TerminalReaderActionFailedEvent as V1TerminalReaderActionFailedEvent,
        V1TerminalReaderActionFailedEventNotification as V1TerminalReaderActionFailedEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_succeeded_event import (
        V1TerminalReaderActionSucceededEvent as V1TerminalReaderActionSucceededEvent,
        V1TerminalReaderActionSucceededEventNotification as V1TerminalReaderActionSucceededEventNotification,
    )
    from stripe.events._v1_terminal_reader_action_updated_event import (
        V1TerminalReaderActionUpdatedEvent as V1TerminalReaderActionUpdatedEvent,
        V1TerminalReaderActionUpdatedEventNotification as V1TerminalReaderActionUpdatedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_advancing_event import (
        V1TestHelpersTestClockAdvancingEvent as V1TestHelpersTestClockAdvancingEvent,
        V1TestHelpersTestClockAdvancingEventNotification as V1TestHelpersTestClockAdvancingEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_created_event import (
        V1TestHelpersTestClockCreatedEvent as V1TestHelpersTestClockCreatedEvent,
        V1TestHelpersTestClockCreatedEventNotification as V1TestHelpersTestClockCreatedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_deleted_event import (
        V1TestHelpersTestClockDeletedEvent as V1TestHelpersTestClockDeletedEvent,
        V1TestHelpersTestClockDeletedEventNotification as V1TestHelpersTestClockDeletedEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_internal_failure_event import (
        V1TestHelpersTestClockInternalFailureEvent as V1TestHelpersTestClockInternalFailureEvent,
        V1TestHelpersTestClockInternalFailureEventNotification as V1TestHelpersTestClockInternalFailureEventNotification,
    )
    from stripe.events._v1_test_helpers_test_clock_ready_event import (
        V1TestHelpersTestClockReadyEvent as V1TestHelpersTestClockReadyEvent,
        V1TestHelpersTestClockReadyEventNotification as V1TestHelpersTestClockReadyEventNotification,
    )
    from stripe.events._v1_topup_canceled_event import (
        V1TopupCanceledEvent as V1TopupCanceledEvent,
        V1TopupCanceledEventNotification as V1TopupCanceledEventNotification,
    )
    from stripe.events._v1_topup_created_event import (
        V1TopupCreatedEvent as V1TopupCreatedEvent,
        V1TopupCreatedEventNotification as V1TopupCreatedEventNotification,
    )
    from stripe.events._v1_topup_failed_event import (
        V1TopupFailedEvent as V1TopupFailedEvent,
        V1TopupFailedEventNotification as V1TopupFailedEventNotification,
    )
    from stripe.events._v1_topup_reversed_event import (
        V1TopupReversedEvent as V1TopupReversedEvent,
        V1TopupReversedEventNotification as V1TopupReversedEventNotification,
    )
    from stripe.events._v1_topup_succeeded_event import (
        V1TopupSucceededEvent as V1TopupSucceededEvent,
        V1TopupSucceededEventNotification as V1TopupSucceededEventNotification,
    )
    from stripe.events._v1_transfer_created_event import (
        V1TransferCreatedEvent as V1TransferCreatedEvent,
        V1TransferCreatedEventNotification as V1TransferCreatedEventNotification,
    )
    from stripe.events._v1_transfer_reversed_event import (
        V1TransferReversedEvent as V1TransferReversedEvent,
        V1TransferReversedEventNotification as V1TransferReversedEventNotification,
    )
    from stripe.events._v1_transfer_updated_event import (
        V1TransferUpdatedEvent as V1TransferUpdatedEvent,
        V1TransferUpdatedEventNotification as V1TransferUpdatedEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_failed_event import (
        V2CommerceProductCatalogImportsFailedEvent as V2CommerceProductCatalogImportsFailedEvent,
        V2CommerceProductCatalogImportsFailedEventNotification as V2CommerceProductCatalogImportsFailedEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_processing_event import (
        V2CommerceProductCatalogImportsProcessingEvent as V2CommerceProductCatalogImportsProcessingEvent,
        V2CommerceProductCatalogImportsProcessingEventNotification as V2CommerceProductCatalogImportsProcessingEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_succeeded_event import (
        V2CommerceProductCatalogImportsSucceededEvent as V2CommerceProductCatalogImportsSucceededEvent,
        V2CommerceProductCatalogImportsSucceededEventNotification as V2CommerceProductCatalogImportsSucceededEventNotification,
    )
    from stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event import (
        V2CommerceProductCatalogImportsSucceededWithErrorsEvent as V2CommerceProductCatalogImportsSucceededWithErrorsEvent,
        V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification as V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification,
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
    from stripe.events._v2_core_account_including_defaults_updated_event import (
        V2CoreAccountIncludingDefaultsUpdatedEvent as V2CoreAccountIncludingDefaultsUpdatedEvent,
        V2CoreAccountIncludingDefaultsUpdatedEventNotification as V2CoreAccountIncludingDefaultsUpdatedEventNotification,
    )
    from stripe.events._v2_core_account_including_future_requirements_updated_event import (
        V2CoreAccountIncludingFutureRequirementsUpdatedEvent as V2CoreAccountIncludingFutureRequirementsUpdatedEvent,
        V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification as V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification,
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
    from stripe.events._v2_money_management_outbound_payment_under_review_event import (
        V2MoneyManagementOutboundPaymentUnderReviewEvent as V2MoneyManagementOutboundPaymentUnderReviewEvent,
        V2MoneyManagementOutboundPaymentUnderReviewEventNotification as V2MoneyManagementOutboundPaymentUnderReviewEventNotification,
    )
    from stripe.events._v2_money_management_outbound_payment_updated_event import (
        V2MoneyManagementOutboundPaymentUpdatedEvent as V2MoneyManagementOutboundPaymentUpdatedEvent,
        V2MoneyManagementOutboundPaymentUpdatedEventNotification as V2MoneyManagementOutboundPaymentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_canceled_event import (
        V2MoneyManagementPayoutIntentCanceledEvent as V2MoneyManagementPayoutIntentCanceledEvent,
        V2MoneyManagementPayoutIntentCanceledEventNotification as V2MoneyManagementPayoutIntentCanceledEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_created_event import (
        V2MoneyManagementPayoutIntentCreatedEvent as V2MoneyManagementPayoutIntentCreatedEvent,
        V2MoneyManagementPayoutIntentCreatedEventNotification as V2MoneyManagementPayoutIntentCreatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_pending_event import (
        V2MoneyManagementPayoutIntentPendingEvent as V2MoneyManagementPayoutIntentPendingEvent,
        V2MoneyManagementPayoutIntentPendingEventNotification as V2MoneyManagementPayoutIntentPendingEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_posted_event import (
        V2MoneyManagementPayoutIntentPostedEvent as V2MoneyManagementPayoutIntentPostedEvent,
        V2MoneyManagementPayoutIntentPostedEventNotification as V2MoneyManagementPayoutIntentPostedEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_processing_event import (
        V2MoneyManagementPayoutIntentProcessingEvent as V2MoneyManagementPayoutIntentProcessingEvent,
        V2MoneyManagementPayoutIntentProcessingEventNotification as V2MoneyManagementPayoutIntentProcessingEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_requires_action_event import (
        V2MoneyManagementPayoutIntentRequiresActionEvent as V2MoneyManagementPayoutIntentRequiresActionEvent,
        V2MoneyManagementPayoutIntentRequiresActionEventNotification as V2MoneyManagementPayoutIntentRequiresActionEventNotification,
    )
    from stripe.events._v2_money_management_payout_intent_updated_event import (
        V2MoneyManagementPayoutIntentUpdatedEvent as V2MoneyManagementPayoutIntentUpdatedEvent,
        V2MoneyManagementPayoutIntentUpdatedEventNotification as V2MoneyManagementPayoutIntentUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_payout_method_created_event import (
        V2MoneyManagementPayoutMethodCreatedEvent as V2MoneyManagementPayoutMethodCreatedEvent,
        V2MoneyManagementPayoutMethodCreatedEventNotification as V2MoneyManagementPayoutMethodCreatedEventNotification,
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
    from stripe.events._v2_money_management_recipient_verification_created_event import (
        V2MoneyManagementRecipientVerificationCreatedEvent as V2MoneyManagementRecipientVerificationCreatedEvent,
        V2MoneyManagementRecipientVerificationCreatedEventNotification as V2MoneyManagementRecipientVerificationCreatedEventNotification,
    )
    from stripe.events._v2_money_management_recipient_verification_updated_event import (
        V2MoneyManagementRecipientVerificationUpdatedEvent as V2MoneyManagementRecipientVerificationUpdatedEvent,
        V2MoneyManagementRecipientVerificationUpdatedEventNotification as V2MoneyManagementRecipientVerificationUpdatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_created_event import (
        V2MoneyManagementTransactionCreatedEvent as V2MoneyManagementTransactionCreatedEvent,
        V2MoneyManagementTransactionCreatedEventNotification as V2MoneyManagementTransactionCreatedEventNotification,
    )
    from stripe.events._v2_money_management_transaction_updated_event import (
        V2MoneyManagementTransactionUpdatedEvent as V2MoneyManagementTransactionUpdatedEvent,
        V2MoneyManagementTransactionUpdatedEventNotification as V2MoneyManagementTransactionUpdatedEventNotification,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "ALL_EVENT_NOTIFICATIONS": ("stripe.events._event_classes", False),
    "V1AccountApplicationAuthorizedEvent": (
        "stripe.events._v1_account_application_authorized_event",
        False,
    ),
    "V1AccountApplicationAuthorizedEventNotification": (
        "stripe.events._v1_account_application_authorized_event",
        False,
    ),
    "V1AccountApplicationDeauthorizedEvent": (
        "stripe.events._v1_account_application_deauthorized_event",
        False,
    ),
    "V1AccountApplicationDeauthorizedEventNotification": (
        "stripe.events._v1_account_application_deauthorized_event",
        False,
    ),
    "V1AccountExternalAccountCreatedEvent": (
        "stripe.events._v1_account_external_account_created_event",
        False,
    ),
    "V1AccountExternalAccountCreatedEventNotification": (
        "stripe.events._v1_account_external_account_created_event",
        False,
    ),
    "V1AccountExternalAccountDeletedEvent": (
        "stripe.events._v1_account_external_account_deleted_event",
        False,
    ),
    "V1AccountExternalAccountDeletedEventNotification": (
        "stripe.events._v1_account_external_account_deleted_event",
        False,
    ),
    "V1AccountExternalAccountUpdatedEvent": (
        "stripe.events._v1_account_external_account_updated_event",
        False,
    ),
    "V1AccountExternalAccountUpdatedEventNotification": (
        "stripe.events._v1_account_external_account_updated_event",
        False,
    ),
    "V1AccountUpdatedEvent": (
        "stripe.events._v1_account_updated_event",
        False,
    ),
    "V1AccountUpdatedEventNotification": (
        "stripe.events._v1_account_updated_event",
        False,
    ),
    "V1ApplicationFeeCreatedEvent": (
        "stripe.events._v1_application_fee_created_event",
        False,
    ),
    "V1ApplicationFeeCreatedEventNotification": (
        "stripe.events._v1_application_fee_created_event",
        False,
    ),
    "V1ApplicationFeeRefundUpdatedEvent": (
        "stripe.events._v1_application_fee_refund_updated_event",
        False,
    ),
    "V1ApplicationFeeRefundUpdatedEventNotification": (
        "stripe.events._v1_application_fee_refund_updated_event",
        False,
    ),
    "V1ApplicationFeeRefundedEvent": (
        "stripe.events._v1_application_fee_refunded_event",
        False,
    ),
    "V1ApplicationFeeRefundedEventNotification": (
        "stripe.events._v1_application_fee_refunded_event",
        False,
    ),
    "V1BalanceAvailableEvent": (
        "stripe.events._v1_balance_available_event",
        False,
    ),
    "V1BalanceAvailableEventNotification": (
        "stripe.events._v1_balance_available_event",
        False,
    ),
    "V1BalanceSettingsUpdatedEvent": (
        "stripe.events._v1_balance_settings_updated_event",
        False,
    ),
    "V1BalanceSettingsUpdatedEventNotification": (
        "stripe.events._v1_balance_settings_updated_event",
        False,
    ),
    "V1BillingAlertTriggeredEvent": (
        "stripe.events._v1_billing_alert_triggered_event",
        False,
    ),
    "V1BillingAlertTriggeredEventNotification": (
        "stripe.events._v1_billing_alert_triggered_event",
        False,
    ),
    "V1BillingCreditBalanceTransactionCreatedEvent": (
        "stripe.events._v1_billing_credit_balance_transaction_created_event",
        False,
    ),
    "V1BillingCreditBalanceTransactionCreatedEventNotification": (
        "stripe.events._v1_billing_credit_balance_transaction_created_event",
        False,
    ),
    "V1BillingCreditGrantCreatedEvent": (
        "stripe.events._v1_billing_credit_grant_created_event",
        False,
    ),
    "V1BillingCreditGrantCreatedEventNotification": (
        "stripe.events._v1_billing_credit_grant_created_event",
        False,
    ),
    "V1BillingCreditGrantUpdatedEvent": (
        "stripe.events._v1_billing_credit_grant_updated_event",
        False,
    ),
    "V1BillingCreditGrantUpdatedEventNotification": (
        "stripe.events._v1_billing_credit_grant_updated_event",
        False,
    ),
    "V1BillingMeterCreatedEvent": (
        "stripe.events._v1_billing_meter_created_event",
        False,
    ),
    "V1BillingMeterCreatedEventNotification": (
        "stripe.events._v1_billing_meter_created_event",
        False,
    ),
    "V1BillingMeterDeactivatedEvent": (
        "stripe.events._v1_billing_meter_deactivated_event",
        False,
    ),
    "V1BillingMeterDeactivatedEventNotification": (
        "stripe.events._v1_billing_meter_deactivated_event",
        False,
    ),
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
    "V1BillingMeterReactivatedEvent": (
        "stripe.events._v1_billing_meter_reactivated_event",
        False,
    ),
    "V1BillingMeterReactivatedEventNotification": (
        "stripe.events._v1_billing_meter_reactivated_event",
        False,
    ),
    "V1BillingMeterUpdatedEvent": (
        "stripe.events._v1_billing_meter_updated_event",
        False,
    ),
    "V1BillingMeterUpdatedEventNotification": (
        "stripe.events._v1_billing_meter_updated_event",
        False,
    ),
    "V1BillingPortalConfigurationCreatedEvent": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        False,
    ),
    "V1BillingPortalConfigurationCreatedEventNotification": (
        "stripe.events._v1_billing_portal_configuration_created_event",
        False,
    ),
    "V1BillingPortalConfigurationUpdatedEvent": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        False,
    ),
    "V1BillingPortalConfigurationUpdatedEventNotification": (
        "stripe.events._v1_billing_portal_configuration_updated_event",
        False,
    ),
    "V1BillingPortalSessionCreatedEvent": (
        "stripe.events._v1_billing_portal_session_created_event",
        False,
    ),
    "V1BillingPortalSessionCreatedEventNotification": (
        "stripe.events._v1_billing_portal_session_created_event",
        False,
    ),
    "V1CapabilityUpdatedEvent": (
        "stripe.events._v1_capability_updated_event",
        False,
    ),
    "V1CapabilityUpdatedEventNotification": (
        "stripe.events._v1_capability_updated_event",
        False,
    ),
    "V1CashBalanceFundsAvailableEvent": (
        "stripe.events._v1_cash_balance_funds_available_event",
        False,
    ),
    "V1CashBalanceFundsAvailableEventNotification": (
        "stripe.events._v1_cash_balance_funds_available_event",
        False,
    ),
    "V1ChargeCapturedEvent": (
        "stripe.events._v1_charge_captured_event",
        False,
    ),
    "V1ChargeCapturedEventNotification": (
        "stripe.events._v1_charge_captured_event",
        False,
    ),
    "V1ChargeDisputeClosedEvent": (
        "stripe.events._v1_charge_dispute_closed_event",
        False,
    ),
    "V1ChargeDisputeClosedEventNotification": (
        "stripe.events._v1_charge_dispute_closed_event",
        False,
    ),
    "V1ChargeDisputeCreatedEvent": (
        "stripe.events._v1_charge_dispute_created_event",
        False,
    ),
    "V1ChargeDisputeCreatedEventNotification": (
        "stripe.events._v1_charge_dispute_created_event",
        False,
    ),
    "V1ChargeDisputeFundsReinstatedEvent": (
        "stripe.events._v1_charge_dispute_funds_reinstated_event",
        False,
    ),
    "V1ChargeDisputeFundsReinstatedEventNotification": (
        "stripe.events._v1_charge_dispute_funds_reinstated_event",
        False,
    ),
    "V1ChargeDisputeFundsWithdrawnEvent": (
        "stripe.events._v1_charge_dispute_funds_withdrawn_event",
        False,
    ),
    "V1ChargeDisputeFundsWithdrawnEventNotification": (
        "stripe.events._v1_charge_dispute_funds_withdrawn_event",
        False,
    ),
    "V1ChargeDisputeUpdatedEvent": (
        "stripe.events._v1_charge_dispute_updated_event",
        False,
    ),
    "V1ChargeDisputeUpdatedEventNotification": (
        "stripe.events._v1_charge_dispute_updated_event",
        False,
    ),
    "V1ChargeExpiredEvent": ("stripe.events._v1_charge_expired_event", False),
    "V1ChargeExpiredEventNotification": (
        "stripe.events._v1_charge_expired_event",
        False,
    ),
    "V1ChargeFailedEvent": ("stripe.events._v1_charge_failed_event", False),
    "V1ChargeFailedEventNotification": (
        "stripe.events._v1_charge_failed_event",
        False,
    ),
    "V1ChargePendingEvent": ("stripe.events._v1_charge_pending_event", False),
    "V1ChargePendingEventNotification": (
        "stripe.events._v1_charge_pending_event",
        False,
    ),
    "V1ChargeRefundUpdatedEvent": (
        "stripe.events._v1_charge_refund_updated_event",
        False,
    ),
    "V1ChargeRefundUpdatedEventNotification": (
        "stripe.events._v1_charge_refund_updated_event",
        False,
    ),
    "V1ChargeRefundedEvent": (
        "stripe.events._v1_charge_refunded_event",
        False,
    ),
    "V1ChargeRefundedEventNotification": (
        "stripe.events._v1_charge_refunded_event",
        False,
    ),
    "V1ChargeSucceededEvent": (
        "stripe.events._v1_charge_succeeded_event",
        False,
    ),
    "V1ChargeSucceededEventNotification": (
        "stripe.events._v1_charge_succeeded_event",
        False,
    ),
    "V1ChargeUpdatedEvent": ("stripe.events._v1_charge_updated_event", False),
    "V1ChargeUpdatedEventNotification": (
        "stripe.events._v1_charge_updated_event",
        False,
    ),
    "V1CheckoutSessionAsyncPaymentFailedEvent": (
        "stripe.events._v1_checkout_session_async_payment_failed_event",
        False,
    ),
    "V1CheckoutSessionAsyncPaymentFailedEventNotification": (
        "stripe.events._v1_checkout_session_async_payment_failed_event",
        False,
    ),
    "V1CheckoutSessionAsyncPaymentSucceededEvent": (
        "stripe.events._v1_checkout_session_async_payment_succeeded_event",
        False,
    ),
    "V1CheckoutSessionAsyncPaymentSucceededEventNotification": (
        "stripe.events._v1_checkout_session_async_payment_succeeded_event",
        False,
    ),
    "V1CheckoutSessionCompletedEvent": (
        "stripe.events._v1_checkout_session_completed_event",
        False,
    ),
    "V1CheckoutSessionCompletedEventNotification": (
        "stripe.events._v1_checkout_session_completed_event",
        False,
    ),
    "V1CheckoutSessionExpiredEvent": (
        "stripe.events._v1_checkout_session_expired_event",
        False,
    ),
    "V1CheckoutSessionExpiredEventNotification": (
        "stripe.events._v1_checkout_session_expired_event",
        False,
    ),
    "V1ClimateOrderCanceledEvent": (
        "stripe.events._v1_climate_order_canceled_event",
        False,
    ),
    "V1ClimateOrderCanceledEventNotification": (
        "stripe.events._v1_climate_order_canceled_event",
        False,
    ),
    "V1ClimateOrderCreatedEvent": (
        "stripe.events._v1_climate_order_created_event",
        False,
    ),
    "V1ClimateOrderCreatedEventNotification": (
        "stripe.events._v1_climate_order_created_event",
        False,
    ),
    "V1ClimateOrderDelayedEvent": (
        "stripe.events._v1_climate_order_delayed_event",
        False,
    ),
    "V1ClimateOrderDelayedEventNotification": (
        "stripe.events._v1_climate_order_delayed_event",
        False,
    ),
    "V1ClimateOrderDeliveredEvent": (
        "stripe.events._v1_climate_order_delivered_event",
        False,
    ),
    "V1ClimateOrderDeliveredEventNotification": (
        "stripe.events._v1_climate_order_delivered_event",
        False,
    ),
    "V1ClimateOrderProductSubstitutedEvent": (
        "stripe.events._v1_climate_order_product_substituted_event",
        False,
    ),
    "V1ClimateOrderProductSubstitutedEventNotification": (
        "stripe.events._v1_climate_order_product_substituted_event",
        False,
    ),
    "V1ClimateProductCreatedEvent": (
        "stripe.events._v1_climate_product_created_event",
        False,
    ),
    "V1ClimateProductCreatedEventNotification": (
        "stripe.events._v1_climate_product_created_event",
        False,
    ),
    "V1ClimateProductPricingUpdatedEvent": (
        "stripe.events._v1_climate_product_pricing_updated_event",
        False,
    ),
    "V1ClimateProductPricingUpdatedEventNotification": (
        "stripe.events._v1_climate_product_pricing_updated_event",
        False,
    ),
    "V1CouponCreatedEvent": ("stripe.events._v1_coupon_created_event", False),
    "V1CouponCreatedEventNotification": (
        "stripe.events._v1_coupon_created_event",
        False,
    ),
    "V1CouponDeletedEvent": ("stripe.events._v1_coupon_deleted_event", False),
    "V1CouponDeletedEventNotification": (
        "stripe.events._v1_coupon_deleted_event",
        False,
    ),
    "V1CouponUpdatedEvent": ("stripe.events._v1_coupon_updated_event", False),
    "V1CouponUpdatedEventNotification": (
        "stripe.events._v1_coupon_updated_event",
        False,
    ),
    "V1CreditNoteCreatedEvent": (
        "stripe.events._v1_credit_note_created_event",
        False,
    ),
    "V1CreditNoteCreatedEventNotification": (
        "stripe.events._v1_credit_note_created_event",
        False,
    ),
    "V1CreditNoteUpdatedEvent": (
        "stripe.events._v1_credit_note_updated_event",
        False,
    ),
    "V1CreditNoteUpdatedEventNotification": (
        "stripe.events._v1_credit_note_updated_event",
        False,
    ),
    "V1CreditNoteVoidedEvent": (
        "stripe.events._v1_credit_note_voided_event",
        False,
    ),
    "V1CreditNoteVoidedEventNotification": (
        "stripe.events._v1_credit_note_voided_event",
        False,
    ),
    "V1CustomerCashBalanceTransactionCreatedEvent": (
        "stripe.events._v1_customer_cash_balance_transaction_created_event",
        False,
    ),
    "V1CustomerCashBalanceTransactionCreatedEventNotification": (
        "stripe.events._v1_customer_cash_balance_transaction_created_event",
        False,
    ),
    "V1CustomerCreatedEvent": (
        "stripe.events._v1_customer_created_event",
        False,
    ),
    "V1CustomerCreatedEventNotification": (
        "stripe.events._v1_customer_created_event",
        False,
    ),
    "V1CustomerDeletedEvent": (
        "stripe.events._v1_customer_deleted_event",
        False,
    ),
    "V1CustomerDeletedEventNotification": (
        "stripe.events._v1_customer_deleted_event",
        False,
    ),
    "V1CustomerDiscountCreatedEvent": (
        "stripe.events._v1_customer_discount_created_event",
        False,
    ),
    "V1CustomerDiscountCreatedEventNotification": (
        "stripe.events._v1_customer_discount_created_event",
        False,
    ),
    "V1CustomerDiscountDeletedEvent": (
        "stripe.events._v1_customer_discount_deleted_event",
        False,
    ),
    "V1CustomerDiscountDeletedEventNotification": (
        "stripe.events._v1_customer_discount_deleted_event",
        False,
    ),
    "V1CustomerDiscountSourceChangedEvent": (
        "stripe.events._v1_customer_discount_source_changed_event",
        False,
    ),
    "V1CustomerDiscountSourceChangedEventNotification": (
        "stripe.events._v1_customer_discount_source_changed_event",
        False,
    ),
    "V1CustomerDiscountUpdatedEvent": (
        "stripe.events._v1_customer_discount_updated_event",
        False,
    ),
    "V1CustomerDiscountUpdatedEventNotification": (
        "stripe.events._v1_customer_discount_updated_event",
        False,
    ),
    "V1CustomerSubscriptionActiveEvent": (
        "stripe.events._v1_customer_subscription_active_event",
        False,
    ),
    "V1CustomerSubscriptionActiveEventNotification": (
        "stripe.events._v1_customer_subscription_active_event",
        False,
    ),
    "V1CustomerSubscriptionCancelAtChangedEvent": (
        "stripe.events._v1_customer_subscription_cancel_at_changed_event",
        False,
    ),
    "V1CustomerSubscriptionCancelAtChangedEventNotification": (
        "stripe.events._v1_customer_subscription_cancel_at_changed_event",
        False,
    ),
    "V1CustomerSubscriptionCreatedEvent": (
        "stripe.events._v1_customer_subscription_created_event",
        False,
    ),
    "V1CustomerSubscriptionCreatedEventNotification": (
        "stripe.events._v1_customer_subscription_created_event",
        False,
    ),
    "V1CustomerSubscriptionDefaultPaymentMethodChangedEvent": (
        "stripe.events._v1_customer_subscription_default_payment_method_changed_event",
        False,
    ),
    "V1CustomerSubscriptionDefaultPaymentMethodChangedEventNotification": (
        "stripe.events._v1_customer_subscription_default_payment_method_changed_event",
        False,
    ),
    "V1CustomerSubscriptionDeletedEvent": (
        "stripe.events._v1_customer_subscription_deleted_event",
        False,
    ),
    "V1CustomerSubscriptionDeletedEventNotification": (
        "stripe.events._v1_customer_subscription_deleted_event",
        False,
    ),
    "V1CustomerSubscriptionIncompleteEvent": (
        "stripe.events._v1_customer_subscription_incomplete_event",
        False,
    ),
    "V1CustomerSubscriptionIncompleteEventNotification": (
        "stripe.events._v1_customer_subscription_incomplete_event",
        False,
    ),
    "V1CustomerSubscriptionIncompleteExpiredEvent": (
        "stripe.events._v1_customer_subscription_incomplete_expired_event",
        False,
    ),
    "V1CustomerSubscriptionIncompleteExpiredEventNotification": (
        "stripe.events._v1_customer_subscription_incomplete_expired_event",
        False,
    ),
    "V1CustomerSubscriptionItemAddedEvent": (
        "stripe.events._v1_customer_subscription_item_added_event",
        False,
    ),
    "V1CustomerSubscriptionItemAddedEventNotification": (
        "stripe.events._v1_customer_subscription_item_added_event",
        False,
    ),
    "V1CustomerSubscriptionItemPriceChangedEvent": (
        "stripe.events._v1_customer_subscription_item_price_changed_event",
        False,
    ),
    "V1CustomerSubscriptionItemPriceChangedEventNotification": (
        "stripe.events._v1_customer_subscription_item_price_changed_event",
        False,
    ),
    "V1CustomerSubscriptionItemQuantityChangedEvent": (
        "stripe.events._v1_customer_subscription_item_quantity_changed_event",
        False,
    ),
    "V1CustomerSubscriptionItemQuantityChangedEventNotification": (
        "stripe.events._v1_customer_subscription_item_quantity_changed_event",
        False,
    ),
    "V1CustomerSubscriptionItemRemovedEvent": (
        "stripe.events._v1_customer_subscription_item_removed_event",
        False,
    ),
    "V1CustomerSubscriptionItemRemovedEventNotification": (
        "stripe.events._v1_customer_subscription_item_removed_event",
        False,
    ),
    "V1CustomerSubscriptionItemTaxRatesChangedEvent": (
        "stripe.events._v1_customer_subscription_item_tax_rates_changed_event",
        False,
    ),
    "V1CustomerSubscriptionItemTaxRatesChangedEventNotification": (
        "stripe.events._v1_customer_subscription_item_tax_rates_changed_event",
        False,
    ),
    "V1CustomerSubscriptionPastDueEvent": (
        "stripe.events._v1_customer_subscription_past_due_event",
        False,
    ),
    "V1CustomerSubscriptionPastDueEventNotification": (
        "stripe.events._v1_customer_subscription_past_due_event",
        False,
    ),
    "V1CustomerSubscriptionPausedEvent": (
        "stripe.events._v1_customer_subscription_paused_event",
        False,
    ),
    "V1CustomerSubscriptionPausedEventNotification": (
        "stripe.events._v1_customer_subscription_paused_event",
        False,
    ),
    "V1CustomerSubscriptionPendingUpdateAppliedEvent": (
        "stripe.events._v1_customer_subscription_pending_update_applied_event",
        False,
    ),
    "V1CustomerSubscriptionPendingUpdateAppliedEventNotification": (
        "stripe.events._v1_customer_subscription_pending_update_applied_event",
        False,
    ),
    "V1CustomerSubscriptionPendingUpdateExpiredEvent": (
        "stripe.events._v1_customer_subscription_pending_update_expired_event",
        False,
    ),
    "V1CustomerSubscriptionPendingUpdateExpiredEventNotification": (
        "stripe.events._v1_customer_subscription_pending_update_expired_event",
        False,
    ),
    "V1CustomerSubscriptionResumedEvent": (
        "stripe.events._v1_customer_subscription_resumed_event",
        False,
    ),
    "V1CustomerSubscriptionResumedEventNotification": (
        "stripe.events._v1_customer_subscription_resumed_event",
        False,
    ),
    "V1CustomerSubscriptionTrialWillEndEvent": (
        "stripe.events._v1_customer_subscription_trial_will_end_event",
        False,
    ),
    "V1CustomerSubscriptionTrialWillEndEventNotification": (
        "stripe.events._v1_customer_subscription_trial_will_end_event",
        False,
    ),
    "V1CustomerSubscriptionTrialingEvent": (
        "stripe.events._v1_customer_subscription_trialing_event",
        False,
    ),
    "V1CustomerSubscriptionTrialingEventNotification": (
        "stripe.events._v1_customer_subscription_trialing_event",
        False,
    ),
    "V1CustomerSubscriptionUnpaidEvent": (
        "stripe.events._v1_customer_subscription_unpaid_event",
        False,
    ),
    "V1CustomerSubscriptionUnpaidEventNotification": (
        "stripe.events._v1_customer_subscription_unpaid_event",
        False,
    ),
    "V1CustomerSubscriptionUpdatedEvent": (
        "stripe.events._v1_customer_subscription_updated_event",
        False,
    ),
    "V1CustomerSubscriptionUpdatedEventNotification": (
        "stripe.events._v1_customer_subscription_updated_event",
        False,
    ),
    "V1CustomerTaxIdCreatedEvent": (
        "stripe.events._v1_customer_tax_id_created_event",
        False,
    ),
    "V1CustomerTaxIdCreatedEventNotification": (
        "stripe.events._v1_customer_tax_id_created_event",
        False,
    ),
    "V1CustomerTaxIdDeletedEvent": (
        "stripe.events._v1_customer_tax_id_deleted_event",
        False,
    ),
    "V1CustomerTaxIdDeletedEventNotification": (
        "stripe.events._v1_customer_tax_id_deleted_event",
        False,
    ),
    "V1CustomerTaxIdUpdatedEvent": (
        "stripe.events._v1_customer_tax_id_updated_event",
        False,
    ),
    "V1CustomerTaxIdUpdatedEventNotification": (
        "stripe.events._v1_customer_tax_id_updated_event",
        False,
    ),
    "V1CustomerUpdatedEvent": (
        "stripe.events._v1_customer_updated_event",
        False,
    ),
    "V1CustomerUpdatedEventNotification": (
        "stripe.events._v1_customer_updated_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEvent": (
        "stripe.events._v1_entitlements_active_entitlement_summary_entitlement_added_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryEntitlementAddedEventNotification": (
        "stripe.events._v1_entitlements_active_entitlement_summary_entitlement_added_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEvent": (
        "stripe.events._v1_entitlements_active_entitlement_summary_entitlement_removed_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryEntitlementRemovedEventNotification": (
        "stripe.events._v1_entitlements_active_entitlement_summary_entitlement_removed_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryUpdatedEvent": (
        "stripe.events._v1_entitlements_active_entitlement_summary_updated_event",
        False,
    ),
    "V1EntitlementsActiveEntitlementSummaryUpdatedEventNotification": (
        "stripe.events._v1_entitlements_active_entitlement_summary_updated_event",
        False,
    ),
    "V1FileCreatedEvent": ("stripe.events._v1_file_created_event", False),
    "V1FileCreatedEventNotification": (
        "stripe.events._v1_file_created_event",
        False,
    ),
    "V1FinancialConnectionsAccountAccountNumbersUpdatedEvent": (
        "stripe.events._v1_financial_connections_account_account_numbers_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountAccountNumbersUpdatedEventNotification": (
        "stripe.events._v1_financial_connections_account_account_numbers_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountBalanceRefreshFailedEvent": (
        "stripe.events._v1_financial_connections_account_balance_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountBalanceRefreshFailedEventNotification": (
        "stripe.events._v1_financial_connections_account_balance_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountBalanceRefreshSucceededEvent": (
        "stripe.events._v1_financial_connections_account_balance_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountBalanceRefreshSucceededEventNotification": (
        "stripe.events._v1_financial_connections_account_balance_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountCreatedEvent": (
        "stripe.events._v1_financial_connections_account_created_event",
        False,
    ),
    "V1FinancialConnectionsAccountCreatedEventNotification": (
        "stripe.events._v1_financial_connections_account_created_event",
        False,
    ),
    "V1FinancialConnectionsAccountDeactivatedEvent": (
        "stripe.events._v1_financial_connections_account_deactivated_event",
        False,
    ),
    "V1FinancialConnectionsAccountDeactivatedEventNotification": (
        "stripe.events._v1_financial_connections_account_deactivated_event",
        False,
    ),
    "V1FinancialConnectionsAccountDisconnectedEvent": (
        "stripe.events._v1_financial_connections_account_disconnected_event",
        False,
    ),
    "V1FinancialConnectionsAccountDisconnectedEventNotification": (
        "stripe.events._v1_financial_connections_account_disconnected_event",
        False,
    ),
    "V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEvent": (
        "stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountExpectedDeactivationDateUpdatedEventNotification": (
        "stripe.events._v1_financial_connections_account_expected_deactivation_date_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountInferredBalancesRefreshFailedEvent": (
        "stripe.events._v1_financial_connections_account_inferred_balances_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountInferredBalancesRefreshFailedEventNotification": (
        "stripe.events._v1_financial_connections_account_inferred_balances_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEvent": (
        "stripe.events._v1_financial_connections_account_inferred_balances_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountInferredBalancesRefreshSucceededEventNotification": (
        "stripe.events._v1_financial_connections_account_inferred_balances_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountOwnershipRefreshFailedEvent": (
        "stripe.events._v1_financial_connections_account_ownership_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountOwnershipRefreshFailedEventNotification": (
        "stripe.events._v1_financial_connections_account_ownership_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountOwnershipRefreshSucceededEvent": (
        "stripe.events._v1_financial_connections_account_ownership_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountOwnershipRefreshSucceededEventNotification": (
        "stripe.events._v1_financial_connections_account_ownership_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountReactivatedEvent": (
        "stripe.events._v1_financial_connections_account_reactivated_event",
        False,
    ),
    "V1FinancialConnectionsAccountReactivatedEventNotification": (
        "stripe.events._v1_financial_connections_account_reactivated_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedBalanceEvent": (
        "stripe.events._v1_financial_connections_account_refreshed_balance_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedBalanceEventNotification": (
        "stripe.events._v1_financial_connections_account_refreshed_balance_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedOwnershipEvent": (
        "stripe.events._v1_financial_connections_account_refreshed_ownership_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedOwnershipEventNotification": (
        "stripe.events._v1_financial_connections_account_refreshed_ownership_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedTransactionsEvent": (
        "stripe.events._v1_financial_connections_account_refreshed_transactions_event",
        False,
    ),
    "V1FinancialConnectionsAccountRefreshedTransactionsEventNotification": (
        "stripe.events._v1_financial_connections_account_refreshed_transactions_event",
        False,
    ),
    "V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEvent": (
        "stripe.events._v1_financial_connections_account_risk_intelligence_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountRiskIntelligenceRefreshFailedEventNotification": (
        "stripe.events._v1_financial_connections_account_risk_intelligence_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEvent": (
        "stripe.events._v1_financial_connections_account_risk_intelligence_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountRiskIntelligenceRefreshSucceededEventNotification": (
        "stripe.events._v1_financial_connections_account_risk_intelligence_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEvent": (
        "stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountSupportedPaymentMethodTypesUpdatedEventNotification": (
        "stripe.events._v1_financial_connections_account_supported_payment_method_types_updated_event",
        False,
    ),
    "V1FinancialConnectionsAccountTransactionsRefreshFailedEvent": (
        "stripe.events._v1_financial_connections_account_transactions_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountTransactionsRefreshFailedEventNotification": (
        "stripe.events._v1_financial_connections_account_transactions_refresh_failed_event",
        False,
    ),
    "V1FinancialConnectionsAccountTransactionsRefreshSucceededEvent": (
        "stripe.events._v1_financial_connections_account_transactions_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountTransactionsRefreshSucceededEventNotification": (
        "stripe.events._v1_financial_connections_account_transactions_refresh_succeeded_event",
        False,
    ),
    "V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEvent": (
        "stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event",
        False,
    ),
    "V1FinancialConnectionsAccountUpcomingAccountNumberExpiryEventNotification": (
        "stripe.events._v1_financial_connections_account_upcoming_account_number_expiry_event",
        False,
    ),
    "V1FinancialConnectionsAccountUpcomingDeactivationEvent": (
        "stripe.events._v1_financial_connections_account_upcoming_deactivation_event",
        False,
    ),
    "V1FinancialConnectionsAccountUpcomingDeactivationEventNotification": (
        "stripe.events._v1_financial_connections_account_upcoming_deactivation_event",
        False,
    ),
    "V1IdentityVerificationSessionCanceledEvent": (
        "stripe.events._v1_identity_verification_session_canceled_event",
        False,
    ),
    "V1IdentityVerificationSessionCanceledEventNotification": (
        "stripe.events._v1_identity_verification_session_canceled_event",
        False,
    ),
    "V1IdentityVerificationSessionCreatedEvent": (
        "stripe.events._v1_identity_verification_session_created_event",
        False,
    ),
    "V1IdentityVerificationSessionCreatedEventNotification": (
        "stripe.events._v1_identity_verification_session_created_event",
        False,
    ),
    "V1IdentityVerificationSessionProcessingEvent": (
        "stripe.events._v1_identity_verification_session_processing_event",
        False,
    ),
    "V1IdentityVerificationSessionProcessingEventNotification": (
        "stripe.events._v1_identity_verification_session_processing_event",
        False,
    ),
    "V1IdentityVerificationSessionRedactedEvent": (
        "stripe.events._v1_identity_verification_session_redacted_event",
        False,
    ),
    "V1IdentityVerificationSessionRedactedEventNotification": (
        "stripe.events._v1_identity_verification_session_redacted_event",
        False,
    ),
    "V1IdentityVerificationSessionRequiresInputEvent": (
        "stripe.events._v1_identity_verification_session_requires_input_event",
        False,
    ),
    "V1IdentityVerificationSessionRequiresInputEventNotification": (
        "stripe.events._v1_identity_verification_session_requires_input_event",
        False,
    ),
    "V1IdentityVerificationSessionVerifiedEvent": (
        "stripe.events._v1_identity_verification_session_verified_event",
        False,
    ),
    "V1IdentityVerificationSessionVerifiedEventNotification": (
        "stripe.events._v1_identity_verification_session_verified_event",
        False,
    ),
    "V1InvoiceCreatedEvent": (
        "stripe.events._v1_invoice_created_event",
        False,
    ),
    "V1InvoiceCreatedEventNotification": (
        "stripe.events._v1_invoice_created_event",
        False,
    ),
    "V1InvoiceDeletedEvent": (
        "stripe.events._v1_invoice_deleted_event",
        False,
    ),
    "V1InvoiceDeletedEventNotification": (
        "stripe.events._v1_invoice_deleted_event",
        False,
    ),
    "V1InvoiceDiscountAddedEvent": (
        "stripe.events._v1_invoice_discount_added_event",
        False,
    ),
    "V1InvoiceDiscountAddedEventNotification": (
        "stripe.events._v1_invoice_discount_added_event",
        False,
    ),
    "V1InvoiceDiscountRemovedEvent": (
        "stripe.events._v1_invoice_discount_removed_event",
        False,
    ),
    "V1InvoiceDiscountRemovedEventNotification": (
        "stripe.events._v1_invoice_discount_removed_event",
        False,
    ),
    "V1InvoiceFinalizationFailedEvent": (
        "stripe.events._v1_invoice_finalization_failed_event",
        False,
    ),
    "V1InvoiceFinalizationFailedEventNotification": (
        "stripe.events._v1_invoice_finalization_failed_event",
        False,
    ),
    "V1InvoiceFinalizedEvent": (
        "stripe.events._v1_invoice_finalized_event",
        False,
    ),
    "V1InvoiceFinalizedEventNotification": (
        "stripe.events._v1_invoice_finalized_event",
        False,
    ),
    "V1InvoiceLineItemAddedEvent": (
        "stripe.events._v1_invoice_line_item_added_event",
        False,
    ),
    "V1InvoiceLineItemAddedEventNotification": (
        "stripe.events._v1_invoice_line_item_added_event",
        False,
    ),
    "V1InvoiceLineItemPricingChangedEvent": (
        "stripe.events._v1_invoice_line_item_pricing_changed_event",
        False,
    ),
    "V1InvoiceLineItemPricingChangedEventNotification": (
        "stripe.events._v1_invoice_line_item_pricing_changed_event",
        False,
    ),
    "V1InvoiceLineItemQuantityChangedEvent": (
        "stripe.events._v1_invoice_line_item_quantity_changed_event",
        False,
    ),
    "V1InvoiceLineItemQuantityChangedEventNotification": (
        "stripe.events._v1_invoice_line_item_quantity_changed_event",
        False,
    ),
    "V1InvoiceLineItemRemovedEvent": (
        "stripe.events._v1_invoice_line_item_removed_event",
        False,
    ),
    "V1InvoiceLineItemRemovedEventNotification": (
        "stripe.events._v1_invoice_line_item_removed_event",
        False,
    ),
    "V1InvoiceMarkedUncollectibleEvent": (
        "stripe.events._v1_invoice_marked_uncollectible_event",
        False,
    ),
    "V1InvoiceMarkedUncollectibleEventNotification": (
        "stripe.events._v1_invoice_marked_uncollectible_event",
        False,
    ),
    "V1InvoiceOverdueEvent": (
        "stripe.events._v1_invoice_overdue_event",
        False,
    ),
    "V1InvoiceOverdueEventNotification": (
        "stripe.events._v1_invoice_overdue_event",
        False,
    ),
    "V1InvoiceOverpaidEvent": (
        "stripe.events._v1_invoice_overpaid_event",
        False,
    ),
    "V1InvoiceOverpaidEventNotification": (
        "stripe.events._v1_invoice_overpaid_event",
        False,
    ),
    "V1InvoicePaidEvent": ("stripe.events._v1_invoice_paid_event", False),
    "V1InvoicePaidEventNotification": (
        "stripe.events._v1_invoice_paid_event",
        False,
    ),
    "V1InvoicePaymentActionRequiredEvent": (
        "stripe.events._v1_invoice_payment_action_required_event",
        False,
    ),
    "V1InvoicePaymentActionRequiredEventNotification": (
        "stripe.events._v1_invoice_payment_action_required_event",
        False,
    ),
    "V1InvoicePaymentAttemptRequiredEvent": (
        "stripe.events._v1_invoice_payment_attempt_required_event",
        False,
    ),
    "V1InvoicePaymentAttemptRequiredEventNotification": (
        "stripe.events._v1_invoice_payment_attempt_required_event",
        False,
    ),
    "V1InvoicePaymentCanceledEvent": (
        "stripe.events._v1_invoice_payment_canceled_event",
        False,
    ),
    "V1InvoicePaymentCanceledEventNotification": (
        "stripe.events._v1_invoice_payment_canceled_event",
        False,
    ),
    "V1InvoicePaymentFailedEvent": (
        "stripe.events._v1_invoice_payment_failed_event",
        False,
    ),
    "V1InvoicePaymentFailedEventNotification": (
        "stripe.events._v1_invoice_payment_failed_event",
        False,
    ),
    "V1InvoicePaymentOpenEvent": (
        "stripe.events._v1_invoice_payment_open_event",
        False,
    ),
    "V1InvoicePaymentOpenEventNotification": (
        "stripe.events._v1_invoice_payment_open_event",
        False,
    ),
    "V1InvoicePaymentPaidEvent": (
        "stripe.events._v1_invoice_payment_paid_event",
        False,
    ),
    "V1InvoicePaymentPaidEventNotification": (
        "stripe.events._v1_invoice_payment_paid_event",
        False,
    ),
    "V1InvoicePaymentSucceededEvent": (
        "stripe.events._v1_invoice_payment_succeeded_event",
        False,
    ),
    "V1InvoicePaymentSucceededEventNotification": (
        "stripe.events._v1_invoice_payment_succeeded_event",
        False,
    ),
    "V1InvoiceSentEvent": ("stripe.events._v1_invoice_sent_event", False),
    "V1InvoiceSentEventNotification": (
        "stripe.events._v1_invoice_sent_event",
        False,
    ),
    "V1InvoiceUpcomingEvent": (
        "stripe.events._v1_invoice_upcoming_event",
        False,
    ),
    "V1InvoiceUpcomingEventNotification": (
        "stripe.events._v1_invoice_upcoming_event",
        False,
    ),
    "V1InvoiceUpdatedEvent": (
        "stripe.events._v1_invoice_updated_event",
        False,
    ),
    "V1InvoiceUpdatedEventNotification": (
        "stripe.events._v1_invoice_updated_event",
        False,
    ),
    "V1InvoiceVoidedEvent": ("stripe.events._v1_invoice_voided_event", False),
    "V1InvoiceVoidedEventNotification": (
        "stripe.events._v1_invoice_voided_event",
        False,
    ),
    "V1InvoiceWillBeDueEvent": (
        "stripe.events._v1_invoice_will_be_due_event",
        False,
    ),
    "V1InvoiceWillBeDueEventNotification": (
        "stripe.events._v1_invoice_will_be_due_event",
        False,
    ),
    "V1InvoiceitemAmountChangedEvent": (
        "stripe.events._v1_invoiceitem_amount_changed_event",
        False,
    ),
    "V1InvoiceitemAmountChangedEventNotification": (
        "stripe.events._v1_invoiceitem_amount_changed_event",
        False,
    ),
    "V1InvoiceitemCreatedEvent": (
        "stripe.events._v1_invoiceitem_created_event",
        False,
    ),
    "V1InvoiceitemCreatedEventNotification": (
        "stripe.events._v1_invoiceitem_created_event",
        False,
    ),
    "V1InvoiceitemDeletedEvent": (
        "stripe.events._v1_invoiceitem_deleted_event",
        False,
    ),
    "V1InvoiceitemDeletedEventNotification": (
        "stripe.events._v1_invoiceitem_deleted_event",
        False,
    ),
    "V1InvoiceitemDiscountAddedEvent": (
        "stripe.events._v1_invoiceitem_discount_added_event",
        False,
    ),
    "V1InvoiceitemDiscountAddedEventNotification": (
        "stripe.events._v1_invoiceitem_discount_added_event",
        False,
    ),
    "V1InvoiceitemDiscountRemovedEvent": (
        "stripe.events._v1_invoiceitem_discount_removed_event",
        False,
    ),
    "V1InvoiceitemDiscountRemovedEventNotification": (
        "stripe.events._v1_invoiceitem_discount_removed_event",
        False,
    ),
    "V1IssuingAuthorizationCreatedEvent": (
        "stripe.events._v1_issuing_authorization_created_event",
        False,
    ),
    "V1IssuingAuthorizationCreatedEventNotification": (
        "stripe.events._v1_issuing_authorization_created_event",
        False,
    ),
    "V1IssuingAuthorizationRequestEvent": (
        "stripe.events._v1_issuing_authorization_request_event",
        False,
    ),
    "V1IssuingAuthorizationRequestEventNotification": (
        "stripe.events._v1_issuing_authorization_request_event",
        False,
    ),
    "V1IssuingAuthorizationUpdatedEvent": (
        "stripe.events._v1_issuing_authorization_updated_event",
        False,
    ),
    "V1IssuingAuthorizationUpdatedEventNotification": (
        "stripe.events._v1_issuing_authorization_updated_event",
        False,
    ),
    "V1IssuingCardCreatedEvent": (
        "stripe.events._v1_issuing_card_created_event",
        False,
    ),
    "V1IssuingCardCreatedEventNotification": (
        "stripe.events._v1_issuing_card_created_event",
        False,
    ),
    "V1IssuingCardUpdatedEvent": (
        "stripe.events._v1_issuing_card_updated_event",
        False,
    ),
    "V1IssuingCardUpdatedEventNotification": (
        "stripe.events._v1_issuing_card_updated_event",
        False,
    ),
    "V1IssuingCardholderCreatedEvent": (
        "stripe.events._v1_issuing_cardholder_created_event",
        False,
    ),
    "V1IssuingCardholderCreatedEventNotification": (
        "stripe.events._v1_issuing_cardholder_created_event",
        False,
    ),
    "V1IssuingCardholderUpdatedEvent": (
        "stripe.events._v1_issuing_cardholder_updated_event",
        False,
    ),
    "V1IssuingCardholderUpdatedEventNotification": (
        "stripe.events._v1_issuing_cardholder_updated_event",
        False,
    ),
    "V1IssuingDisputeClosedEvent": (
        "stripe.events._v1_issuing_dispute_closed_event",
        False,
    ),
    "V1IssuingDisputeClosedEventNotification": (
        "stripe.events._v1_issuing_dispute_closed_event",
        False,
    ),
    "V1IssuingDisputeCreatedEvent": (
        "stripe.events._v1_issuing_dispute_created_event",
        False,
    ),
    "V1IssuingDisputeCreatedEventNotification": (
        "stripe.events._v1_issuing_dispute_created_event",
        False,
    ),
    "V1IssuingDisputeFundsReinstatedEvent": (
        "stripe.events._v1_issuing_dispute_funds_reinstated_event",
        False,
    ),
    "V1IssuingDisputeFundsReinstatedEventNotification": (
        "stripe.events._v1_issuing_dispute_funds_reinstated_event",
        False,
    ),
    "V1IssuingDisputeFundsRescindedEvent": (
        "stripe.events._v1_issuing_dispute_funds_rescinded_event",
        False,
    ),
    "V1IssuingDisputeFundsRescindedEventNotification": (
        "stripe.events._v1_issuing_dispute_funds_rescinded_event",
        False,
    ),
    "V1IssuingDisputeSubmittedEvent": (
        "stripe.events._v1_issuing_dispute_submitted_event",
        False,
    ),
    "V1IssuingDisputeSubmittedEventNotification": (
        "stripe.events._v1_issuing_dispute_submitted_event",
        False,
    ),
    "V1IssuingDisputeUpdatedEvent": (
        "stripe.events._v1_issuing_dispute_updated_event",
        False,
    ),
    "V1IssuingDisputeUpdatedEventNotification": (
        "stripe.events._v1_issuing_dispute_updated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignActivatedEvent": (
        "stripe.events._v1_issuing_personalization_design_activated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignActivatedEventNotification": (
        "stripe.events._v1_issuing_personalization_design_activated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignDeactivatedEvent": (
        "stripe.events._v1_issuing_personalization_design_deactivated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignDeactivatedEventNotification": (
        "stripe.events._v1_issuing_personalization_design_deactivated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignRejectedEvent": (
        "stripe.events._v1_issuing_personalization_design_rejected_event",
        False,
    ),
    "V1IssuingPersonalizationDesignRejectedEventNotification": (
        "stripe.events._v1_issuing_personalization_design_rejected_event",
        False,
    ),
    "V1IssuingPersonalizationDesignUpdatedEvent": (
        "stripe.events._v1_issuing_personalization_design_updated_event",
        False,
    ),
    "V1IssuingPersonalizationDesignUpdatedEventNotification": (
        "stripe.events._v1_issuing_personalization_design_updated_event",
        False,
    ),
    "V1IssuingTokenCreatedEvent": (
        "stripe.events._v1_issuing_token_created_event",
        False,
    ),
    "V1IssuingTokenCreatedEventNotification": (
        "stripe.events._v1_issuing_token_created_event",
        False,
    ),
    "V1IssuingTokenUpdatedEvent": (
        "stripe.events._v1_issuing_token_updated_event",
        False,
    ),
    "V1IssuingTokenUpdatedEventNotification": (
        "stripe.events._v1_issuing_token_updated_event",
        False,
    ),
    "V1IssuingTransactionCreatedEvent": (
        "stripe.events._v1_issuing_transaction_created_event",
        False,
    ),
    "V1IssuingTransactionCreatedEventNotification": (
        "stripe.events._v1_issuing_transaction_created_event",
        False,
    ),
    "V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent": (
        "stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event",
        False,
    ),
    "V1IssuingTransactionPurchaseDetailsReceiptUpdatedEventNotification": (
        "stripe.events._v1_issuing_transaction_purchase_details_receipt_updated_event",
        False,
    ),
    "V1IssuingTransactionUpdatedEvent": (
        "stripe.events._v1_issuing_transaction_updated_event",
        False,
    ),
    "V1IssuingTransactionUpdatedEventNotification": (
        "stripe.events._v1_issuing_transaction_updated_event",
        False,
    ),
    "V1MandateUpdatedEvent": (
        "stripe.events._v1_mandate_updated_event",
        False,
    ),
    "V1MandateUpdatedEventNotification": (
        "stripe.events._v1_mandate_updated_event",
        False,
    ),
    "V1PaymentIntentAmountCapturableUpdatedEvent": (
        "stripe.events._v1_payment_intent_amount_capturable_updated_event",
        False,
    ),
    "V1PaymentIntentAmountCapturableUpdatedEventNotification": (
        "stripe.events._v1_payment_intent_amount_capturable_updated_event",
        False,
    ),
    "V1PaymentIntentCanceledEvent": (
        "stripe.events._v1_payment_intent_canceled_event",
        False,
    ),
    "V1PaymentIntentCanceledEventNotification": (
        "stripe.events._v1_payment_intent_canceled_event",
        False,
    ),
    "V1PaymentIntentCreatedEvent": (
        "stripe.events._v1_payment_intent_created_event",
        False,
    ),
    "V1PaymentIntentCreatedEventNotification": (
        "stripe.events._v1_payment_intent_created_event",
        False,
    ),
    "V1PaymentIntentPartiallyFundedEvent": (
        "stripe.events._v1_payment_intent_partially_funded_event",
        False,
    ),
    "V1PaymentIntentPartiallyFundedEventNotification": (
        "stripe.events._v1_payment_intent_partially_funded_event",
        False,
    ),
    "V1PaymentIntentPaymentFailedEvent": (
        "stripe.events._v1_payment_intent_payment_failed_event",
        False,
    ),
    "V1PaymentIntentPaymentFailedEventNotification": (
        "stripe.events._v1_payment_intent_payment_failed_event",
        False,
    ),
    "V1PaymentIntentProcessingEvent": (
        "stripe.events._v1_payment_intent_processing_event",
        False,
    ),
    "V1PaymentIntentProcessingEventNotification": (
        "stripe.events._v1_payment_intent_processing_event",
        False,
    ),
    "V1PaymentIntentRequiresActionEvent": (
        "stripe.events._v1_payment_intent_requires_action_event",
        False,
    ),
    "V1PaymentIntentRequiresActionEventNotification": (
        "stripe.events._v1_payment_intent_requires_action_event",
        False,
    ),
    "V1PaymentIntentSucceededEvent": (
        "stripe.events._v1_payment_intent_succeeded_event",
        False,
    ),
    "V1PaymentIntentSucceededEventNotification": (
        "stripe.events._v1_payment_intent_succeeded_event",
        False,
    ),
    "V1PaymentLinkCreatedEvent": (
        "stripe.events._v1_payment_link_created_event",
        False,
    ),
    "V1PaymentLinkCreatedEventNotification": (
        "stripe.events._v1_payment_link_created_event",
        False,
    ),
    "V1PaymentLinkUpdatedEvent": (
        "stripe.events._v1_payment_link_updated_event",
        False,
    ),
    "V1PaymentLinkUpdatedEventNotification": (
        "stripe.events._v1_payment_link_updated_event",
        False,
    ),
    "V1PaymentMethodAttachedEvent": (
        "stripe.events._v1_payment_method_attached_event",
        False,
    ),
    "V1PaymentMethodAttachedEventNotification": (
        "stripe.events._v1_payment_method_attached_event",
        False,
    ),
    "V1PaymentMethodAutomaticallyUpdatedEvent": (
        "stripe.events._v1_payment_method_automatically_updated_event",
        False,
    ),
    "V1PaymentMethodAutomaticallyUpdatedEventNotification": (
        "stripe.events._v1_payment_method_automatically_updated_event",
        False,
    ),
    "V1PaymentMethodDetachedEvent": (
        "stripe.events._v1_payment_method_detached_event",
        False,
    ),
    "V1PaymentMethodDetachedEventNotification": (
        "stripe.events._v1_payment_method_detached_event",
        False,
    ),
    "V1PaymentMethodUpdatedEvent": (
        "stripe.events._v1_payment_method_updated_event",
        False,
    ),
    "V1PaymentMethodUpdatedEventNotification": (
        "stripe.events._v1_payment_method_updated_event",
        False,
    ),
    "V1PayoutCanceledEvent": (
        "stripe.events._v1_payout_canceled_event",
        False,
    ),
    "V1PayoutCanceledEventNotification": (
        "stripe.events._v1_payout_canceled_event",
        False,
    ),
    "V1PayoutCreatedEvent": ("stripe.events._v1_payout_created_event", False),
    "V1PayoutCreatedEventNotification": (
        "stripe.events._v1_payout_created_event",
        False,
    ),
    "V1PayoutFailedEvent": ("stripe.events._v1_payout_failed_event", False),
    "V1PayoutFailedEventNotification": (
        "stripe.events._v1_payout_failed_event",
        False,
    ),
    "V1PayoutPaidEvent": ("stripe.events._v1_payout_paid_event", False),
    "V1PayoutPaidEventNotification": (
        "stripe.events._v1_payout_paid_event",
        False,
    ),
    "V1PayoutReconciliationCompletedEvent": (
        "stripe.events._v1_payout_reconciliation_completed_event",
        False,
    ),
    "V1PayoutReconciliationCompletedEventNotification": (
        "stripe.events._v1_payout_reconciliation_completed_event",
        False,
    ),
    "V1PayoutUpdatedEvent": ("stripe.events._v1_payout_updated_event", False),
    "V1PayoutUpdatedEventNotification": (
        "stripe.events._v1_payout_updated_event",
        False,
    ),
    "V1PersonCreatedEvent": ("stripe.events._v1_person_created_event", False),
    "V1PersonCreatedEventNotification": (
        "stripe.events._v1_person_created_event",
        False,
    ),
    "V1PersonDeletedEvent": ("stripe.events._v1_person_deleted_event", False),
    "V1PersonDeletedEventNotification": (
        "stripe.events._v1_person_deleted_event",
        False,
    ),
    "V1PersonUpdatedEvent": ("stripe.events._v1_person_updated_event", False),
    "V1PersonUpdatedEventNotification": (
        "stripe.events._v1_person_updated_event",
        False,
    ),
    "V1PlanCreatedEvent": ("stripe.events._v1_plan_created_event", False),
    "V1PlanCreatedEventNotification": (
        "stripe.events._v1_plan_created_event",
        False,
    ),
    "V1PlanDeletedEvent": ("stripe.events._v1_plan_deleted_event", False),
    "V1PlanDeletedEventNotification": (
        "stripe.events._v1_plan_deleted_event",
        False,
    ),
    "V1PlanUpdatedEvent": ("stripe.events._v1_plan_updated_event", False),
    "V1PlanUpdatedEventNotification": (
        "stripe.events._v1_plan_updated_event",
        False,
    ),
    "V1PriceActivatedEvent": (
        "stripe.events._v1_price_activated_event",
        False,
    ),
    "V1PriceActivatedEventNotification": (
        "stripe.events._v1_price_activated_event",
        False,
    ),
    "V1PriceCreatedEvent": ("stripe.events._v1_price_created_event", False),
    "V1PriceCreatedEventNotification": (
        "stripe.events._v1_price_created_event",
        False,
    ),
    "V1PriceDeactivatedEvent": (
        "stripe.events._v1_price_deactivated_event",
        False,
    ),
    "V1PriceDeactivatedEventNotification": (
        "stripe.events._v1_price_deactivated_event",
        False,
    ),
    "V1PriceDeletedEvent": ("stripe.events._v1_price_deleted_event", False),
    "V1PriceDeletedEventNotification": (
        "stripe.events._v1_price_deleted_event",
        False,
    ),
    "V1PriceLookupKeyChangedEvent": (
        "stripe.events._v1_price_lookup_key_changed_event",
        False,
    ),
    "V1PriceLookupKeyChangedEventNotification": (
        "stripe.events._v1_price_lookup_key_changed_event",
        False,
    ),
    "V1PriceTaxBehaviorChangedEvent": (
        "stripe.events._v1_price_tax_behavior_changed_event",
        False,
    ),
    "V1PriceTaxBehaviorChangedEventNotification": (
        "stripe.events._v1_price_tax_behavior_changed_event",
        False,
    ),
    "V1PriceUpdatedEvent": ("stripe.events._v1_price_updated_event", False),
    "V1PriceUpdatedEventNotification": (
        "stripe.events._v1_price_updated_event",
        False,
    ),
    "V1ProductActivatedEvent": (
        "stripe.events._v1_product_activated_event",
        False,
    ),
    "V1ProductActivatedEventNotification": (
        "stripe.events._v1_product_activated_event",
        False,
    ),
    "V1ProductCreatedEvent": (
        "stripe.events._v1_product_created_event",
        False,
    ),
    "V1ProductCreatedEventNotification": (
        "stripe.events._v1_product_created_event",
        False,
    ),
    "V1ProductDeactivatedEvent": (
        "stripe.events._v1_product_deactivated_event",
        False,
    ),
    "V1ProductDeactivatedEventNotification": (
        "stripe.events._v1_product_deactivated_event",
        False,
    ),
    "V1ProductDefaultPriceChangedEvent": (
        "stripe.events._v1_product_default_price_changed_event",
        False,
    ),
    "V1ProductDefaultPriceChangedEventNotification": (
        "stripe.events._v1_product_default_price_changed_event",
        False,
    ),
    "V1ProductDeletedEvent": (
        "stripe.events._v1_product_deleted_event",
        False,
    ),
    "V1ProductDeletedEventNotification": (
        "stripe.events._v1_product_deleted_event",
        False,
    ),
    "V1ProductTaxCodeChangedEvent": (
        "stripe.events._v1_product_tax_code_changed_event",
        False,
    ),
    "V1ProductTaxCodeChangedEventNotification": (
        "stripe.events._v1_product_tax_code_changed_event",
        False,
    ),
    "V1ProductUpdatedEvent": (
        "stripe.events._v1_product_updated_event",
        False,
    ),
    "V1ProductUpdatedEventNotification": (
        "stripe.events._v1_product_updated_event",
        False,
    ),
    "V1PromotionCodeCreatedEvent": (
        "stripe.events._v1_promotion_code_created_event",
        False,
    ),
    "V1PromotionCodeCreatedEventNotification": (
        "stripe.events._v1_promotion_code_created_event",
        False,
    ),
    "V1PromotionCodeFullyRedeemedEvent": (
        "stripe.events._v1_promotion_code_fully_redeemed_event",
        False,
    ),
    "V1PromotionCodeFullyRedeemedEventNotification": (
        "stripe.events._v1_promotion_code_fully_redeemed_event",
        False,
    ),
    "V1PromotionCodeUpdatedEvent": (
        "stripe.events._v1_promotion_code_updated_event",
        False,
    ),
    "V1PromotionCodeUpdatedEventNotification": (
        "stripe.events._v1_promotion_code_updated_event",
        False,
    ),
    "V1QuoteAcceptedEvent": ("stripe.events._v1_quote_accepted_event", False),
    "V1QuoteAcceptedEventNotification": (
        "stripe.events._v1_quote_accepted_event",
        False,
    ),
    "V1QuoteCanceledEvent": ("stripe.events._v1_quote_canceled_event", False),
    "V1QuoteCanceledEventNotification": (
        "stripe.events._v1_quote_canceled_event",
        False,
    ),
    "V1QuoteCreatedEvent": ("stripe.events._v1_quote_created_event", False),
    "V1QuoteCreatedEventNotification": (
        "stripe.events._v1_quote_created_event",
        False,
    ),
    "V1QuoteFinalizedEvent": (
        "stripe.events._v1_quote_finalized_event",
        False,
    ),
    "V1QuoteFinalizedEventNotification": (
        "stripe.events._v1_quote_finalized_event",
        False,
    ),
    "V1RadarEarlyFraudWarningCreatedEvent": (
        "stripe.events._v1_radar_early_fraud_warning_created_event",
        False,
    ),
    "V1RadarEarlyFraudWarningCreatedEventNotification": (
        "stripe.events._v1_radar_early_fraud_warning_created_event",
        False,
    ),
    "V1RadarEarlyFraudWarningUpdatedEvent": (
        "stripe.events._v1_radar_early_fraud_warning_updated_event",
        False,
    ),
    "V1RadarEarlyFraudWarningUpdatedEventNotification": (
        "stripe.events._v1_radar_early_fraud_warning_updated_event",
        False,
    ),
    "V1RefundCreatedEvent": ("stripe.events._v1_refund_created_event", False),
    "V1RefundCreatedEventNotification": (
        "stripe.events._v1_refund_created_event",
        False,
    ),
    "V1RefundFailedEvent": ("stripe.events._v1_refund_failed_event", False),
    "V1RefundFailedEventNotification": (
        "stripe.events._v1_refund_failed_event",
        False,
    ),
    "V1RefundUpdatedEvent": ("stripe.events._v1_refund_updated_event", False),
    "V1RefundUpdatedEventNotification": (
        "stripe.events._v1_refund_updated_event",
        False,
    ),
    "V1ReviewClosedEvent": ("stripe.events._v1_review_closed_event", False),
    "V1ReviewClosedEventNotification": (
        "stripe.events._v1_review_closed_event",
        False,
    ),
    "V1ReviewOpenedEvent": ("stripe.events._v1_review_opened_event", False),
    "V1ReviewOpenedEventNotification": (
        "stripe.events._v1_review_opened_event",
        False,
    ),
    "V1SetupIntentCanceledEvent": (
        "stripe.events._v1_setup_intent_canceled_event",
        False,
    ),
    "V1SetupIntentCanceledEventNotification": (
        "stripe.events._v1_setup_intent_canceled_event",
        False,
    ),
    "V1SetupIntentCreatedEvent": (
        "stripe.events._v1_setup_intent_created_event",
        False,
    ),
    "V1SetupIntentCreatedEventNotification": (
        "stripe.events._v1_setup_intent_created_event",
        False,
    ),
    "V1SetupIntentRequiresActionEvent": (
        "stripe.events._v1_setup_intent_requires_action_event",
        False,
    ),
    "V1SetupIntentRequiresActionEventNotification": (
        "stripe.events._v1_setup_intent_requires_action_event",
        False,
    ),
    "V1SetupIntentSetupFailedEvent": (
        "stripe.events._v1_setup_intent_setup_failed_event",
        False,
    ),
    "V1SetupIntentSetupFailedEventNotification": (
        "stripe.events._v1_setup_intent_setup_failed_event",
        False,
    ),
    "V1SetupIntentSucceededEvent": (
        "stripe.events._v1_setup_intent_succeeded_event",
        False,
    ),
    "V1SetupIntentSucceededEventNotification": (
        "stripe.events._v1_setup_intent_succeeded_event",
        False,
    ),
    "V1SigmaScheduledQueryRunCreatedEvent": (
        "stripe.events._v1_sigma_scheduled_query_run_created_event",
        False,
    ),
    "V1SigmaScheduledQueryRunCreatedEventNotification": (
        "stripe.events._v1_sigma_scheduled_query_run_created_event",
        False,
    ),
    "V1SourceCanceledEvent": (
        "stripe.events._v1_source_canceled_event",
        False,
    ),
    "V1SourceCanceledEventNotification": (
        "stripe.events._v1_source_canceled_event",
        False,
    ),
    "V1SourceChargeableEvent": (
        "stripe.events._v1_source_chargeable_event",
        False,
    ),
    "V1SourceChargeableEventNotification": (
        "stripe.events._v1_source_chargeable_event",
        False,
    ),
    "V1SourceFailedEvent": ("stripe.events._v1_source_failed_event", False),
    "V1SourceFailedEventNotification": (
        "stripe.events._v1_source_failed_event",
        False,
    ),
    "V1SourceRefundAttributesRequiredEvent": (
        "stripe.events._v1_source_refund_attributes_required_event",
        False,
    ),
    "V1SourceRefundAttributesRequiredEventNotification": (
        "stripe.events._v1_source_refund_attributes_required_event",
        False,
    ),
    "V1SubscriptionScheduleAbortedEvent": (
        "stripe.events._v1_subscription_schedule_aborted_event",
        False,
    ),
    "V1SubscriptionScheduleAbortedEventNotification": (
        "stripe.events._v1_subscription_schedule_aborted_event",
        False,
    ),
    "V1SubscriptionScheduleCanceledEvent": (
        "stripe.events._v1_subscription_schedule_canceled_event",
        False,
    ),
    "V1SubscriptionScheduleCanceledEventNotification": (
        "stripe.events._v1_subscription_schedule_canceled_event",
        False,
    ),
    "V1SubscriptionScheduleCompletedEvent": (
        "stripe.events._v1_subscription_schedule_completed_event",
        False,
    ),
    "V1SubscriptionScheduleCompletedEventNotification": (
        "stripe.events._v1_subscription_schedule_completed_event",
        False,
    ),
    "V1SubscriptionScheduleCreatedEvent": (
        "stripe.events._v1_subscription_schedule_created_event",
        False,
    ),
    "V1SubscriptionScheduleCreatedEventNotification": (
        "stripe.events._v1_subscription_schedule_created_event",
        False,
    ),
    "V1SubscriptionScheduleExpiringEvent": (
        "stripe.events._v1_subscription_schedule_expiring_event",
        False,
    ),
    "V1SubscriptionScheduleExpiringEventNotification": (
        "stripe.events._v1_subscription_schedule_expiring_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseAddedEvent": (
        "stripe.events._v1_subscription_schedule_phase_added_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseAddedEventNotification": (
        "stripe.events._v1_subscription_schedule_phase_added_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEvent": (
        "stripe.events._v1_subscription_schedule_phase_default_tax_rates_changed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseDefaultTaxRatesChangedEventNotification": (
        "stripe.events._v1_subscription_schedule_phase_default_tax_rates_changed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseEndDateChangedEvent": (
        "stripe.events._v1_subscription_schedule_phase_end_date_changed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseEndDateChangedEventNotification": (
        "stripe.events._v1_subscription_schedule_phase_end_date_changed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseRemovedEvent": (
        "stripe.events._v1_subscription_schedule_phase_removed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseRemovedEventNotification": (
        "stripe.events._v1_subscription_schedule_phase_removed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseTrialEndChangedEvent": (
        "stripe.events._v1_subscription_schedule_phase_trial_end_changed_event",
        False,
    ),
    "V1SubscriptionSchedulePhaseTrialEndChangedEventNotification": (
        "stripe.events._v1_subscription_schedule_phase_trial_end_changed_event",
        False,
    ),
    "V1SubscriptionScheduleReleasedEvent": (
        "stripe.events._v1_subscription_schedule_released_event",
        False,
    ),
    "V1SubscriptionScheduleReleasedEventNotification": (
        "stripe.events._v1_subscription_schedule_released_event",
        False,
    ),
    "V1SubscriptionScheduleUpdatedEvent": (
        "stripe.events._v1_subscription_schedule_updated_event",
        False,
    ),
    "V1SubscriptionScheduleUpdatedEventNotification": (
        "stripe.events._v1_subscription_schedule_updated_event",
        False,
    ),
    "V1TaxRateCreatedEvent": (
        "stripe.events._v1_tax_rate_created_event",
        False,
    ),
    "V1TaxRateCreatedEventNotification": (
        "stripe.events._v1_tax_rate_created_event",
        False,
    ),
    "V1TaxRateUpdatedEvent": (
        "stripe.events._v1_tax_rate_updated_event",
        False,
    ),
    "V1TaxRateUpdatedEventNotification": (
        "stripe.events._v1_tax_rate_updated_event",
        False,
    ),
    "V1TaxSettingsUpdatedEvent": (
        "stripe.events._v1_tax_settings_updated_event",
        False,
    ),
    "V1TaxSettingsUpdatedEventNotification": (
        "stripe.events._v1_tax_settings_updated_event",
        False,
    ),
    "V1TerminalReaderActionFailedEvent": (
        "stripe.events._v1_terminal_reader_action_failed_event",
        False,
    ),
    "V1TerminalReaderActionFailedEventNotification": (
        "stripe.events._v1_terminal_reader_action_failed_event",
        False,
    ),
    "V1TerminalReaderActionSucceededEvent": (
        "stripe.events._v1_terminal_reader_action_succeeded_event",
        False,
    ),
    "V1TerminalReaderActionSucceededEventNotification": (
        "stripe.events._v1_terminal_reader_action_succeeded_event",
        False,
    ),
    "V1TerminalReaderActionUpdatedEvent": (
        "stripe.events._v1_terminal_reader_action_updated_event",
        False,
    ),
    "V1TerminalReaderActionUpdatedEventNotification": (
        "stripe.events._v1_terminal_reader_action_updated_event",
        False,
    ),
    "V1TestHelpersTestClockAdvancingEvent": (
        "stripe.events._v1_test_helpers_test_clock_advancing_event",
        False,
    ),
    "V1TestHelpersTestClockAdvancingEventNotification": (
        "stripe.events._v1_test_helpers_test_clock_advancing_event",
        False,
    ),
    "V1TestHelpersTestClockCreatedEvent": (
        "stripe.events._v1_test_helpers_test_clock_created_event",
        False,
    ),
    "V1TestHelpersTestClockCreatedEventNotification": (
        "stripe.events._v1_test_helpers_test_clock_created_event",
        False,
    ),
    "V1TestHelpersTestClockDeletedEvent": (
        "stripe.events._v1_test_helpers_test_clock_deleted_event",
        False,
    ),
    "V1TestHelpersTestClockDeletedEventNotification": (
        "stripe.events._v1_test_helpers_test_clock_deleted_event",
        False,
    ),
    "V1TestHelpersTestClockInternalFailureEvent": (
        "stripe.events._v1_test_helpers_test_clock_internal_failure_event",
        False,
    ),
    "V1TestHelpersTestClockInternalFailureEventNotification": (
        "stripe.events._v1_test_helpers_test_clock_internal_failure_event",
        False,
    ),
    "V1TestHelpersTestClockReadyEvent": (
        "stripe.events._v1_test_helpers_test_clock_ready_event",
        False,
    ),
    "V1TestHelpersTestClockReadyEventNotification": (
        "stripe.events._v1_test_helpers_test_clock_ready_event",
        False,
    ),
    "V1TopupCanceledEvent": ("stripe.events._v1_topup_canceled_event", False),
    "V1TopupCanceledEventNotification": (
        "stripe.events._v1_topup_canceled_event",
        False,
    ),
    "V1TopupCreatedEvent": ("stripe.events._v1_topup_created_event", False),
    "V1TopupCreatedEventNotification": (
        "stripe.events._v1_topup_created_event",
        False,
    ),
    "V1TopupFailedEvent": ("stripe.events._v1_topup_failed_event", False),
    "V1TopupFailedEventNotification": (
        "stripe.events._v1_topup_failed_event",
        False,
    ),
    "V1TopupReversedEvent": ("stripe.events._v1_topup_reversed_event", False),
    "V1TopupReversedEventNotification": (
        "stripe.events._v1_topup_reversed_event",
        False,
    ),
    "V1TopupSucceededEvent": (
        "stripe.events._v1_topup_succeeded_event",
        False,
    ),
    "V1TopupSucceededEventNotification": (
        "stripe.events._v1_topup_succeeded_event",
        False,
    ),
    "V1TransferCreatedEvent": (
        "stripe.events._v1_transfer_created_event",
        False,
    ),
    "V1TransferCreatedEventNotification": (
        "stripe.events._v1_transfer_created_event",
        False,
    ),
    "V1TransferReversedEvent": (
        "stripe.events._v1_transfer_reversed_event",
        False,
    ),
    "V1TransferReversedEventNotification": (
        "stripe.events._v1_transfer_reversed_event",
        False,
    ),
    "V1TransferUpdatedEvent": (
        "stripe.events._v1_transfer_updated_event",
        False,
    ),
    "V1TransferUpdatedEventNotification": (
        "stripe.events._v1_transfer_updated_event",
        False,
    ),
    "V2CommerceProductCatalogImportsFailedEvent": (
        "stripe.events._v2_commerce_product_catalog_imports_failed_event",
        False,
    ),
    "V2CommerceProductCatalogImportsFailedEventNotification": (
        "stripe.events._v2_commerce_product_catalog_imports_failed_event",
        False,
    ),
    "V2CommerceProductCatalogImportsProcessingEvent": (
        "stripe.events._v2_commerce_product_catalog_imports_processing_event",
        False,
    ),
    "V2CommerceProductCatalogImportsProcessingEventNotification": (
        "stripe.events._v2_commerce_product_catalog_imports_processing_event",
        False,
    ),
    "V2CommerceProductCatalogImportsSucceededEvent": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_event",
        False,
    ),
    "V2CommerceProductCatalogImportsSucceededEventNotification": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_event",
        False,
    ),
    "V2CommerceProductCatalogImportsSucceededWithErrorsEvent": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event",
        False,
    ),
    "V2CommerceProductCatalogImportsSucceededWithErrorsEventNotification": (
        "stripe.events._v2_commerce_product_catalog_imports_succeeded_with_errors_event",
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
    "V2CoreAccountIncludingDefaultsUpdatedEvent": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingDefaultsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_defaults_updated_event",
        False,
    ),
    "V2CoreAccountIncludingFutureRequirementsUpdatedEvent": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
        False,
    ),
    "V2CoreAccountIncludingFutureRequirementsUpdatedEventNotification": (
        "stripe.events._v2_core_account_including_future_requirements_updated_event",
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
    "V2MoneyManagementOutboundPaymentUnderReviewEvent": (
        "stripe.events._v2_money_management_outbound_payment_under_review_event",
        False,
    ),
    "V2MoneyManagementOutboundPaymentUnderReviewEventNotification": (
        "stripe.events._v2_money_management_outbound_payment_under_review_event",
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
    "V2MoneyManagementPayoutIntentCanceledEvent": (
        "stripe.events._v2_money_management_payout_intent_canceled_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentCanceledEventNotification": (
        "stripe.events._v2_money_management_payout_intent_canceled_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentCreatedEvent": (
        "stripe.events._v2_money_management_payout_intent_created_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentCreatedEventNotification": (
        "stripe.events._v2_money_management_payout_intent_created_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentPendingEvent": (
        "stripe.events._v2_money_management_payout_intent_pending_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentPendingEventNotification": (
        "stripe.events._v2_money_management_payout_intent_pending_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentPostedEvent": (
        "stripe.events._v2_money_management_payout_intent_posted_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentPostedEventNotification": (
        "stripe.events._v2_money_management_payout_intent_posted_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentProcessingEvent": (
        "stripe.events._v2_money_management_payout_intent_processing_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentProcessingEventNotification": (
        "stripe.events._v2_money_management_payout_intent_processing_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentRequiresActionEvent": (
        "stripe.events._v2_money_management_payout_intent_requires_action_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentRequiresActionEventNotification": (
        "stripe.events._v2_money_management_payout_intent_requires_action_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentUpdatedEvent": (
        "stripe.events._v2_money_management_payout_intent_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutIntentUpdatedEventNotification": (
        "stripe.events._v2_money_management_payout_intent_updated_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodCreatedEvent": (
        "stripe.events._v2_money_management_payout_method_created_event",
        False,
    ),
    "V2MoneyManagementPayoutMethodCreatedEventNotification": (
        "stripe.events._v2_money_management_payout_method_created_event",
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
    "V2MoneyManagementRecipientVerificationCreatedEvent": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationCreatedEventNotification": (
        "stripe.events._v2_money_management_recipient_verification_created_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationUpdatedEvent": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
        False,
    ),
    "V2MoneyManagementRecipientVerificationUpdatedEventNotification": (
        "stripe.events._v2_money_management_recipient_verification_updated_event",
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
