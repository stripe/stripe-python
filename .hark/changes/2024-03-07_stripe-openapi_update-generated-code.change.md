---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1267
is_stripe_api_change: true
released_in_version: 8.6.0
---

* Add support for `documents` on `AccountSession.Components`
* Add support for `request_three_d_secure` on `Checkout.Session.PaymentMethodOptionsCard` and `Checkout.Session.CreateParams.PaymentMethodOptionsCard`
* Add support for `created` on `CreditNote.ListParams`
* Add support for `sepa_debit` on `Invoice.PaymentSettings.PaymentMethodOptions`, `InvoiceCreateParams.PaymentSettings.PaymentMethodOptions`, and `InvoiceUpdateParams.PaymentSettings.PaymentMethodOptions`
