---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1815
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.3.0a1
---

* Change type of `billing.AlertCreateParamsSpendThreshold.group_by` from `literal('pricing_plan_subscription')` to `enum('billing_cadence'|'pricing_plan_subscription')`
* ⚠️ Change type of `Billing.Alert.SpendThreshold.group_by` from `literal('pricing_plan_subscription')` to `enum('billing_cadence'|'pricing_plan_subscription')`
* Change `DelegatedCheckout.RequestedSession.affiliate_attributions` to be required
* ⚠️ Add support for new value `institution_requirement` on enum `FinancialConnections.Account.StatusDetail.Inactive.cause`
* Add support for `wechat_pay` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
* Add support for `gift_card` on `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodOption`, and `PaymentIntentModifyParamsPaymentMethodOption`
* Add support for `payment_details` on `PaymentIntentCreateParamsPaymentsOrchestration`
* Add support for `enabled` on `PaymentIntent.PaymentDetail.Benefit.FrMealVoucher` and `SetupIntent.SetupDetail.Benefit.FrMealVoucher`
* ⚠️ Remove support for `login_failed`, `registration_failed`, `registration_success`, and `type` on `radar.CustomerEvaluationModifyParams`
* ⚠️ Remove support for `latest_version` on `V2.Billing.LicenseFee`, `V2.Billing.PricingPlan`, and `V2.Billing.RateCard`
* ⚠️ Remove support for `service_interval_count` and `service_interval` on `V2.Billing.LicenseFee` and `V2.Billing.RateCard`
* Add support for `debit_agreement` on `V2.MoneyManagement.ReceivedCredit.StripeBalancePayment`
* Add support for new value `chaps` on enum `v2.FinancialAddressCreditSimulationCreditParams.network`
* Add support for `canonical_path` on `EventsV2CoreHealthTrafficVolumeDropFiringEvent.Impact` and `EventsV2CoreHealthTrafficVolumeDropResolvedEvent.Impact`
* Add support for snapshot event `payment_intent.expired` with resource `PaymentIntent`
* Add support for event notifications `V2CoreHealthElementsErrorFiringEvent`, `V2CoreHealthElementsErrorResolvedEvent`, `V2CoreHealthInvoiceCountDroppedFiringEvent`, and `V2CoreHealthInvoiceCountDroppedResolvedEvent`
