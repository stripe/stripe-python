---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1269
is_stripe_api_change: true
released_in_version: 8.7.0
---

* Add support for `personalization_design` on parameter classes `CardService.CreateParams`, `CardService.ListParams`, `CardService.UpdateParams`, `stripe.issuing.Card.CreateParams`, `stripe.issuing.Card.ListParams`, and `stripe.issuing.Card.ModifyParams` and resource `stripe.issuing.Card`
* Add support for `sepa_debit` on parameter classes `SubscriptionService.CreateParamsPaymentSettingsPaymentMethodOptions`, `SubscriptionService.UpdateParamsPaymentSettingsPaymentMethodOptions`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptions`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions` and resource class `stripe.Subscription.PaymentSettings.PaymentMethodOptions`
* Add support for resource `stripe.issuing.PersonalizationDesign`
* Add support for resource `stripe.issuing.PhysicalBundle`
* Change type from `float` to `Literal['']|float` of `application_fee_percent` on fields `stripe.Subscription.CreateParams`, `stripe.Subscription.ModifyParams`, `SubscriptionService.UpdateParams`, and `SubscriptionService.CreateParams`
