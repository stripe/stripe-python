---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1318
is_stripe_api_change: true
released_in_version: 9.6.0b1
---

* Add support for `rechnung_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
* Add support for `rechnung` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
* Add support for `multibanco` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
* Add support for `multibanco` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
* Add support for `rechnung` on enums `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
* Change type of `transactions` on  `stripe.gift_cards.Card` from `ListObject[Transaction]` to `Optional[ListObject[Transaction]]`
