---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1192
is_stripe_api_change: true
released_in_version: 7.14.0b1
---

* Add support for new value `nn` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bank`
* Add support for new value `NNBANL2G` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bic`
* Change `Invoice.AutomaticTax.liability`, `Invoice.issuer`, and `Subscription.AutomaticTax.liability` to be required
