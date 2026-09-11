---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1317
is_stripe_api_change: true
released_in_version: 9.5.0
---

* Add support for `paypal` on resource class `stripe.Dispute.PaymentMethodDetails`
* Add support for `payment_method_types` on parameter class `stripe.PaymentIntent.ConfirmParams`
* Add support for `ship_from_details` on parameter class `stripe.tax.Calculation.CreateParams` and resources `stripe.tax.Calculation` and `stripe.tax.Transaction`
* Add support for `bh`, `eg`, `ge`, `ke`, `kz`, `ng`, `om` on resource class `stripe.tax.Registration.CountryOptions` and parameter class `stripe.tax.Registration.CreateParamsCountryOptions`
* Add support for `paypal` on enum `stripe.Dispute.PaymentMethodDetails.type`
* Add support for `shipping_address_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
* Change type of `metadata` on  `stripe.entitlements.Feature.ModifyParams` from `Dict[str, str]` to `Literal['']|Dict[str, str]`
