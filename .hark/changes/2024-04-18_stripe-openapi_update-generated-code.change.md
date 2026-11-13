---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1305
is_stripe_api_change: true
released_in_version: 9.3.0
---

* Add support for `allow_redisplay` on parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.Customer.ListPaymentMethodsParams`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`
* Add support for `schedule_details` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
* Add support for `subscription_details` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
* Add support for `create_preview` on resource `stripe.Invoice`
* Add support for `payment_method_data` on parameter class `stripe.checkout.Session.CreateParams`
* Add support for `saved_payment_method_options` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
* Add support for `mobilepay` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
* Add support for `mobilepay` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
* Add support for `other` on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`
