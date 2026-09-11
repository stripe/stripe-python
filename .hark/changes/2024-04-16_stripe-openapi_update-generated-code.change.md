---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1301
is_stripe_api_change: true
released_in_version: 9.2.0
---

* Add support for `balances` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `payouts_list` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `capture_method` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsRevolutPay`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsRevolutPay`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsRevolutPay` and resource class `stripe.PaymentIntent.PaymentMethodOptions.RevolutPay`
* Add support for `swish` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for resource `stripe.entitlements.ActiveEntitlementSummary`
* Remove support for `config` on parameter class `stripe.forwarding.Request.CreateParams` and resource `stripe.forwarding.Request`. This field is no longer used by the Forwarding Request API.
* Change type of `destination_on_behalf_of_charge_management` on  `stripe.AccountSession.Components.PaymentDetails.Features` and `stripe.AccountSession.Components.Payments.Features` from `Optional[bool]` to `bool`
* Change type of `timestamp` on  `stripe.billing.MeterEvent.CreateParams` from `int` to `NotRequired[int]`
* Add support for `entitlements.active_entitlement_summary.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
