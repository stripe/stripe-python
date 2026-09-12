---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1555
is_stripe_api_change: true
released_in_version: 13.1.0b1
---

* Add support for new resources `billing.analytics.MeterUsageRow` and `billing.analytics.MeterUsage`
* Remove support for resources `billing.MeterUsageRow` and `billing.MeterUsage`
* Add support for `retrieve` method on resource `billing.analytics.MeterUsage`
* Remove support for `retrieve` method on resource `billing.MeterUsage`
* Add support for `report_payment_attempt_informational` method on resource `PaymentRecord`
* Add support for `minimum_balance_by_currency` on `BalanceSettings.ModifyParamsPaymentPayout` and `BalanceSettings.Payment.Payout`
* Remove support for values `saturday` and `sunday` from enums `BalanceSettings.ModifyParamsPaymentPayoutSchedule.weekly_payout_days` and `BalanceSettings.Payment.Payout.Schedule.weekly_payout_days`
* Change type of `BalanceSettings.ModifyParamsPaymentSettlementTiming.delay_days_override` from `longInteger` to `emptyable(longInteger)`
* Change `BalanceSettings.ModifyParams.payments` to be optional
* Add support for `delay_days_override` on `BalanceSettings.Payment.SettlementTiming`
* Add support for `automatic_tax` and `invoice_creation` on `checkout.Session.ModifyParams`
* Add support for `unit_label` on `checkout.Session.ModifyParamsLineItemPriceDatumProductDatum`
* Add support for `invoice_settings` on `checkout.Session.ModifyParamsSubscriptionDatum`
* Change `Checkout.Session.CollectedInformation.business_name` to be required
* Add support for `intended_submission_method` on `Dispute.ModifyParams` and `Dispute`
* Change type of `Dispute.SmartDispute.recommended_evidence` from `string` to `array(string)`
* Add support for `pix` on `Invoice.CreateParamsPaymentSettingPaymentMethodOption`, `Invoice.ModifyParamsPaymentSettingPaymentMethodOption`, `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.CreateParamsPaymentSettingPaymentMethodOption`, `Subscription.ModifyParamsPaymentSettingPaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
* Add support for new value `pix` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.ModifyParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.ModifyParamsPaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
* Add support for `billing_schedules` on `Invoice.CreatePreviewParamsSubscriptionDetail`, `Subscription.CreateParams`, `Subscription.ModifyParams`, and `Subscription`
* Add support for `paypay` on `PaymentAttemptRecord.PaymentMethodDetail` and `PaymentRecord.PaymentMethodDetail`
* Add support for `wallet` on `PaymentAttemptRecord.PaymentMethodDetail.Card` and `PaymentRecord.PaymentMethodDetail.Card`
* Change type of `PaymentAttemptRecord.ProcessorDetail.Custom.payment_reference` and `PaymentRecord.ProcessorDetail.Custom.payment_reference` from `string` to `nullable(string)`
* Add support for `flexible` on `QuotePreviewSubscriptionSchedule.BillingMode`
* Add support for `billed_until` on `SubscriptionItem`
* Add support for error codes `financial_connections_account_pending_account_numbers` and `financial_connections_account_unavailable_account_numbers` on `QuotePreviewInvoice.LastFinalizationError`
