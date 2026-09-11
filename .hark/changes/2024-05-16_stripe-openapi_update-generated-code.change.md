---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1328
is_stripe_api_change: true
released_in_version: 9.7.0
---

* Add support for `fee_source` on resource `stripe.ApplicationFee`
* Add support for `net_available` on resource class `stripe.Balance.InstantAvailable`
* Add support for `preferred_locales` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, and `stripe.PaymentMethod.CardPresent`
* Add support for `klarna` on resource class `stripe.Dispute.PaymentMethodDetails`
* Add support for `routing` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent` and resource class `stripe.PaymentIntent.PaymentMethodOptions.CardPresent`
* Add support for `application_fee` on resource `stripe.Payout`
* Add support for `archived` on parameter class `stripe.entitlements.Feature.ListParams`
* Add support for `lookup_key` on parameter class `stripe.entitlements.Feature.ListParams`
* Add support for `no_valid_authorization` on parameter classes `stripe.issuing.Dispute.CreateParamsEvidence` and `stripe.issuing.Dispute.ModifyParamsEvidence` and resource class `stripe.issuing.Dispute.Evidence`
* Add support for `loss_reason` on resource `stripe.issuing.Dispute`
* Add support for `stripe_s700` on parameter classes `stripe.terminal.Configuration.CreateParams` and `stripe.terminal.Configuration.ModifyParams` and resource `stripe.terminal.Configuration`
* Add support for `klarna` on enum `stripe.Dispute.PaymentMethodDetails.type`
* Add support for `no_valid_authorization` on enums `stripe.issuing.Dispute.Evidence.reason`, `stripe.issuing.Dispute.CreateParamsEvidence.reason`, and `stripe.issuing.Dispute.ModifyParamsEvidence.reason`
* Change type of `countries` on  `stripe.financial_connections.Session.CreateParamsFilters` from `List[str]` to `NotRequired[List[str]]`
