---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1161
is_stripe_api_change: true
released_in_version: 7.9.0
---

* Add support for `payment_method_reuse_agreement` on resource classes `PaymentLink.ConsentCollection` and `checkout.Session.ConsentCollection` and parameter classes `PaymentLink.CreateParamsConsentCollection` and `checkout.Session.CreateParamsConsentCollection`
* Add support for `after_submit` on parameter classes `PaymentLink.CreateParamsCustomText`, `PaymentLink.ModifyParamsCustomText`, and `checkout.Session.CreateParamsCustomText` and resource classes `PaymentLink.CustomText` and `checkout.Session.CustomText`
* Add support for `created` on parameter class `radar.EarlyFraudWarning.ListParams`
