---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1718
is_stripe_api_change: true
released_in_version: 14.2.0a3
---

* Add support for `risk_details` on `DelegatedCheckout.RequestedSession`
* Remove support for `description`, `images`, and `name` on `DelegatedCheckout.RequestedSession.LineItemDetail`
* Add support for `name` on `ProductCatalog.TrialOffer` and `product_catalog.TrialOfferCreateParams`
* Add support for `login_failed` and `registration_failed` on `Radar.AccountEvaluation.Event` and `radar.AccountEvaluationModifyParams`
* Change type of `radar.AccountEvaluationModifyParams.type` from `literal('registration_succeeded')` to `enum('login_failed'|'login_succeeded'|'registration_failed'|'registration_succeeded')`
