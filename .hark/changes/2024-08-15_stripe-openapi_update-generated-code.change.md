---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1373
is_stripe_api_change: true
released_in_version: 10.8.0
---

* Add support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`
* Add support for `wallet` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.CardPresent`
* Add support for `mandate_options` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsBacsDebit`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsBacsDebit`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsBacsDebit` and resource class `stripe.PaymentIntent.PaymentMethodOptions.BacsDebit`
* Add support for `bacs_debit` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
* Add support for `chips` on resource classes `stripe.treasury.OutboundPayment.TrackingDetails.UsDomesticWire` and `stripe.treasury.OutboundTransfer.TrackingDetails.UsDomesticWire` and parameter classes `stripe.treasury.OutboundPayment.UpdateParamsTrackingDetailsUsDomesticWire` and `stripe.treasury.OutboundTransfer.UpdateParamsTrackingDetailsUsDomesticWire`
* Change type of `imad` on  `stripe.treasury.OutboundPayment.TrackingDetails.UsDomesticWire` and `stripe.treasury.OutboundTransfer.TrackingDetails.UsDomesticWire` from `str` to `Optional[str]`
