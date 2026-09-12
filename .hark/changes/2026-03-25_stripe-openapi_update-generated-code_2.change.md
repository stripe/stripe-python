---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1763
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.1.0a1
---

* Add support for new resource `v2.core.AccountEvaluation`
* ⚠️ Remove support for resources `v2.billing.LicenseFeeSubscription` and `v2.billing.PricingPlanSubscriptionComponents`
* Add support for `create` method on resource `v2.core.AccountEvaluation`
* ⚠️ Remove support for `retrieve` method on resources `v2.billing.LicenseFeeSubscription` and `v2.billing.PricingPlanSubscriptionComponents`
* Add support for `modify_rates` method on resource `v2.billing.RateCard`
* Add support for `remove_discounts` method on resource `v2.billing.PricingPlanSubscription`
* ⚠️ Add support for new value `eg_bank_account` on enum `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type`
* Add support for `invoice_resources` on `V2.Billing.Intent`
* Add support for `amount_due` and `customer_balance_applied` on `V2.Billing.Intent.AmountDetail`
* Add support for `expires_at` on `V2.Billing.Intent.StatusTransition`
* Add support for `discount` on `V2.Billing.IntentAction.Apply` and `v2.billing.IntentCreateParamsActionApply`
* Add support for `timestamp` on `V2.Billing.IntentAction.Apply.EffectiveAt` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt`
* ⚠️ Add support for new values `current_billing_period_start` and `timestamp` on enums `V2.Billing.IntentAction.Apply.EffectiveAt.type` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt.type`
* ⚠️ Add support for new value `discount` on enums `V2.Billing.IntentAction.Apply.type` and `v2.billing.IntentCreateParamsActionApply.type`
* ⚠️ Change type of `V2.Billing.IntentAction.Deactivate.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `V2.Billing.IntentAction.Modify.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `V2.Billing.IntentAction.Subscribe.PricingPlanSubscriptionDetail.Override.PartialPeriodBehavior.type`, `v2.billing.IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type`, `v2.billing.IntentCreateParamsActionModifyPricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type`, and `v2.billing.IntentCreateParamsActionSubscribePricingPlanSubscriptionDetailOverridePartialPeriodBehavior.type` from `literal('license_fee')` to `enum('license_fee'|'recurring_credit_grant')`
* Add support for `service_cycle` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
* ⚠️ Remove support for `latest_version` on `V2.Billing.LicenseFee`, `V2.Billing.PricingPlan`, and `V2.Billing.RateCard`
* ⚠️ Remove support for `service_interval_count` and `service_interval` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
* ⚠️ Change type of `V2.Billing.LicenseFee.TransformQuantity.divide_by`, `V2.Billing.LicenseFeeVersion.TransformQuantity.divide_by`, `V2.Billing.RateCardRate.TransformQuantity.divide_by`, `v2.billing.LicenseFeeCreateParamsTransformQuantity.divide_by`, `v2.billing.LicenseFeeModifyParamsTransformQuantity.divide_by`, and `v2.billing.RateCardRateCreateParamsTransformQuantity.divide_by` from `longInteger` to `int64_string`
* Add support for `discount_details` and `pricing_plan_component_details` on `V2.Billing.PricingPlanSubscription`
* ⚠️ Add support for new value `crypto_wallets` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* ⚠️ Remove support for value `crypto` from enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `balance_by_funds_type` on `V2.MoneyManagement.FinancialAccount.Payment`
* ⚠️ Add support for new value `next_day_payout_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
* Add support for `treasury_transaction_entry` on `V2.MoneyManagement.TransactionEntry`
* Add support for `treasury_credit_reversal`, `treasury_debit_reversal`, `treasury_inbound_transfer`, `treasury_issuing_authorization`, `treasury_outbound_payment`, `treasury_outbound_transfer`, `treasury_received_credit`, and `treasury_received_debit` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* ⚠️ Add support for new values `treasury_credit_reversal`, `treasury_debit_reversal`, `treasury_inbound_transfer`, `treasury_issuing_authorization`, `treasury_other`, `treasury_outbound_payment`, `treasury_outbound_transfer`, `treasury_received_credit`, and `treasury_received_debit` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for `treasury_transaction` on `V2.MoneyManagement.Transaction`
* ⚠️ Add support for new value `no_valid_payment_method` on enum `V2.Payments.OffSessionPayment.failure_reason`
* Add support for `metadata` on `V2.Payments.SettlementAllocationIntentSplit`
* ⚠️ Change type of `V2.Reporting.ReportRun.Result.File.size` from `longInteger` to `int64_string`
* Add support for `statement_descriptor` on `v2.money_management.OutboundPaymentCreateParams` and `v2.money_management.OutboundTransferCreateParams`
* Add support for `include` on `v2.billing.IntentCreateParams`, `v2.billing.IntentReserveParams`, `v2.billing.PricingPlanSubscriptionListParams`, `v2.billing.PricingPlanSubscriptionRetrieveParams`, `v2.money_management.FinancialAccountListParams`, and `v2.money_management.FinancialAccountRetrieveParams`
* Add support for event notifications `V1AccountSignalsIncludingDelinquencyCreatedEvent`, `V2CoreAccountSignalsFraudulentWebsiteReadyEvent`, and `V2SignalsAccountSignalFraudulentMerchantReadyEvent`
