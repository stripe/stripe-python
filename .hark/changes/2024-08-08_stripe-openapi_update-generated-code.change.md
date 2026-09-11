---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1371
is_stripe_api_change: true
released_in_version: 10.7.0
---

* Add support for `type` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent.Offline`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent.Offline`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent.Offline`, and `stripe.SetupAttempt.PaymentMethodDetails.CardPresent.Offline`
* Add support for `offline` on resource classes `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent` and `stripe.PaymentMethod.CardPresent`
* Add support for `_cls_activate` on resource `stripe.billing.Alert`
* Add support for `_cls_archive` on resource `stripe.billing.Alert`
* Add support for `_cls_deactivate` on resource `stripe.billing.Alert`
* Add support for `activate` on resource `stripe.billing.Alert`
* Add support for `archive` on resource `stripe.billing.Alert`
* Add support for `create` on resource `stripe.billing.Alert`
* Add support for `deactivate` on resource `stripe.billing.Alert`
* Add support for `list` on resource `stripe.billing.Alert`
* Add support for `retrieve` on resources `stripe.billing.Alert` and `stripe.tax.Calculation`
* Add support for `related_customer` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ListParams` and resource `stripe.identity.VerificationSession`
* Add support for `invalid_mandate_reference_prefix_format` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
* Add support for `girocard` on enums `stripe.PaymentIntent.PaymentMethodOptions.Card.network`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.PaymentMethodOptions.Card.network`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.Card.network`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard.network`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard.network`
* Add support for `financial_addresses.aba.forwarding` on enums `stripe.treasury.FinancialAccount.active_features`, `stripe.treasury.FinancialAccount.pending_features`, and `stripe.treasury.FinancialAccount.restricted_features`
* Change type of `count` on  `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan` from `int` to `NotRequired[int]`
* Change type of `interval` on  `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan` from `Literal['month']` to `NotRequired[Literal['month']]`
* Change type of `account` on  `stripe.Person.AdditionalTosAcceptances` from `Account` to `Optional[Account]`
