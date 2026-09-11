---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1760
is_stripe_api_change: true
released_in_version: 14.5.0a4
---

* Add support for `simulate_crypto_deposit` test helper method on resource `PaymentIntent`
* Add support for `deposit_options` and `mode` on `PaymentIntent.PaymentMethodOption.Crypto`, `PaymentIntentConfirmParamsPaymentMethodOptionCrypto`, `PaymentIntentCreateParamsPaymentMethodOptionCrypto`, and `PaymentIntentModifyParamsPaymentMethodOptionCrypto`
* Add support for `crypto_display_details` on `PaymentIntent.NextAction`
