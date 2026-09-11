---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1225
is_stripe_api_change: true
released_in_version: 8.2.0
---

* Add support for `invoices` on `Account.Settings`
* Add support for new value `velobank` on various enums `PaymentMethodDetails.P24.bank`
* Add support for `setup_future_usage` on `PaymentMethodOptions.Blik`
* Add support for `require_cvc_recollection` on `PaymentMethodOptions.Card`
* Add support for `account_tax_ids` on various `InvoiceSettings` request parameters
