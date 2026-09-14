---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1127
is_stripe_api_change: true
released_in_version: 7.5.0
---

* Add support for `bacs_debit_payments` on `Account.CreateParamsSettings`
* Add support for `service_user_number` on `Account.Settings.BacsDebitPayments`
* Add support for `capture_before` on `Charge.PaymentMethodDetails.Card.capture_before`
* Add support for `Paypal` on `Checkout.Session.PaymentMethodOptions`
* Add support for `tax_amounts` on `CreditNote.CreateParamsLine`, `CreditNote.PreviewParamsLine`, and `CreditNote.PreviewLinesParamsLine`
* Add support for `network_data` on `Issuing.Transaction`
* Add support for `status` on `Checkout.Session.ListParams`
