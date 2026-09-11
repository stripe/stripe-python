---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1685
is_stripe_api_change: true
released_in_version: 14.1.0a3
---

* Add support for new resource `product_catalog.TrialOffer`
* Add support for `create` method on resource `product_catalog.TrialOffer`
* Remove support for `amount_subtotal_after_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
* Remove support for `amount_total`, `unit_amount_after_discount`, and `unit_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail`
* Add support for `amount_cart_discount` and `amount_items_discount` on `DelegatedCheckout.RequestedSession.TotalDetail`
* Remove support for `amount_discount` on `DelegatedCheckout.RequestedSession.TotalDetail`
* Add support for `payments_orchestration` on `PaymentIntentCreateParams` and `PaymentIntent`
