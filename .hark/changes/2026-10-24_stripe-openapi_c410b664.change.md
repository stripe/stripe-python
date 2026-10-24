---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1952
semver_level: major
is_stripe_api_change: true
---

* Add support for `billing_group` on `Billing.Alert.SpendThreshold.Filter`, `Billing.AlertNotification`, `Billing.AlertTriggered.GroupBy`, `billing.AlertCreateParamsSpendThresholdFilter`, and `billing.BillingAlertListAlertNotificationParams`
* Add support for new values `get_fund` and `nhil` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
* Add support for `physical_address` on `Account.Company`
* Add support for `toss_pay` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for `mandate` on `Charge.PaymentMethodDetail.Paypay`, `PaymentAttemptRecord.PaymentMethodDetail.Paypay`, and `PaymentRecord.PaymentMethodDetail.Paypay`
* Add support for `automatic_pass_through_fee` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for new value `stripe_balance` on enum `checkout.SessionCreateParams.allowed_payment_method_types`
* Add support for new value `stripe_balance` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `paypay` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Change `checkout.SessionCreateParamsMarketingAttribution.ad_conversion` to be optional
* Add support for new values `bw_vat`, `ci_vat`, and `gh_tin` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, and `Tax.Transaction.CustomerDetail.TaxId.type`
* Add support for `adjustable_quantity` on `Checkout.Session.Item.Subscription.Item`
* ⚠️ Change `Checkout.Session.MarketingAttribution.ad_conversion` to be optional
* Add support for new value `toss_pay` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for new value `toss_pay` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for `marketing_attributions` on `CustomerCreateParams` and `Customer`
* Add support for new value `toss_pay` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `delivered_at` and `shipped_at` on `Issuing.Card.Shipping`
* Add support for new value `toss_pay` on enums `PaymentIntent.allowed_payment_method_types`, `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, `PaymentIntentModifyParams.allowed_payment_method_types`, `SetupIntent.allowed_payment_method_types`, `SetupIntentConfirmParams.allowed_payment_method_types`, `SetupIntentCreateParams.allowed_payment_method_types`, and `SetupIntentModifyParams.allowed_payment_method_types`
* Add support for new value `toss_pay` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for `merchant_of_record` on `PaymentIntent.PaymentDetail.MoneyService.AccountFunding`, `PaymentIntentConfirmParamsPaymentDetailMoneyServiceAccountFunding`, `PaymentIntentCreateParamsPaymentDetailMoneyServiceAccountFunding`, and `PaymentIntentModifyParamsPaymentDetailMoneyServiceAccountFunding`
* Add support for `payment_method_data` and `payment_method_options` on `RefundCreateParams`
* Add support for `debit_behavior` on `Subscription.PaymentSetting.PaymentMethodOption.SepaDebit`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionSepaDebit`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionSepaDebit`
* Add support for `triggering_signal` on `V2.Signals.AccountActivity` and `v2.signals.AccountActivityCreateParams`
* Add support for `mfa_challenges` on `V2.Signals.AccountActivity.LoginDecision` and `v2.signals.AccountActivityCreateParamsLoginDecision`
