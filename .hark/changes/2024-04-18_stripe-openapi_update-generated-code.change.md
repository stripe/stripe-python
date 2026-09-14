---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1302
is_stripe_api_change: true
released_in_version: 9.4.0b1
---

* Add support for `balances` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `payouts_list` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `capital_overview` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `tax_registrations` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `tax_settings` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `external_account_collection` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
* Add support for `allow_redisplay` on parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.Customer.ListPaymentMethodsParams`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`
* Add support for `subscription_trial_from_plan` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
* Add support for `swish` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for `payment_method_data` on parameter class `stripe.checkout.Session.CreateParams`
* Add support for `saved_payment_method_options` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
* Add support for `mobilepay` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
* Remove support for `config` on parameter class `stripe.forwarding.Request.CreateParams` and resource `stripe.forwarding.Request`
* Change type of fields `stripe.AccountSession.Components.PaymentDetails.Features` and `stripe.AccountSession.Components.Payments.Features` from `Optional[bool]` to `bool` of `destination_on_behalf_of_charge_management`
* Change type of field `stripe.billing.MeterEvent.CreateParams` from `int` to `NotRequired[int]` of `timestamp`
* Add support for `mobilepay` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
* Add support for `other` on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`
