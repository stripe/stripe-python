---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1449
is_stripe_api_change: true
released_in_version: 11.6.0b1
---

* Add support for `rejected_reason` on resource class `stripe.Account.RiskControls`
* Add support for `product_tax_code_selector` on parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `brand_product` on resource classes `stripe.Charge.PaymentMethodDetails.AmazonPay.Funding.Card` and `stripe.Charge.PaymentMethodDetails.RevolutPay.Funding.Card`
* Add support for `prices` on parameter classes `stripe.billing.CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope` and `stripe.billing.CreditGrant.CreateParamsApplicabilityConfigScope` and resource class `stripe.billing.CreditGrant.ApplicabilityConfig.Scope`
* Add support for `restrictions` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
* Change type of `political_exposure` on  `stripe.Account.CreatePersonParams`, `stripe.Account.ModifyPersonParams`, and `stripe.Token.CreateParamsPerson` from `str` to `Literal['existing', 'none']`
* Change type of `price_type` on  `stripe.billing.CreditGrant.ApplicabilityConfig.Scope` from `Literal['metered']` to `Optional[Literal['metered']]`
