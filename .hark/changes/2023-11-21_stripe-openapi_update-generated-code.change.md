---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1138
is_stripe_api_change: true
released_in_version: 7.6.0
---

* Add support for `electronic_commerce_indicator` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure` and `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`
* Add support for `exemption_indicator` on resource class `Charge.PaymentMethodDetails.Card.ThreeDSecure`
* Add support for `transaction_id` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure`, `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`, `issuing.Authorization.NetworkData`, and `issuing.Transaction.NetworkData`
* Add support for `offline` on resource class `Charge.PaymentMethodDetails.CardPresent`
* Add support for `transferred_to_balance` on resource `CustomerCashBalanceTransaction`
* Add support for `three_d_secure` on parameter classes `PaymentIntent.ConfirmParamsPaymentMethodOptionsCard`, `PaymentIntent.CreateParamsPaymentMethodOptionsCard`, `PaymentIntent.ModifyParamsPaymentMethodOptionsCard`, `SetupIntent.ConfirmParamsPaymentMethodOptionsCard`, `SetupIntent.CreateParamsPaymentMethodOptionsCard`, and `SetupIntent.ModifyParamsPaymentMethodOptionsCard`
* Add support for `system_trace_audit_number` on resource class `issuing.Authorization.NetworkData`
* Add support for `network_risk_score` on resource classes `issuing.Authorization.PendingRequest` and `issuing.Authorization.RequestHistory`
* Add support for `requested_at` on resource class `issuing.Authorization.RequestHistory`
* Add support for `authorization_code` on resource class `issuing.Transaction.NetworkData`
