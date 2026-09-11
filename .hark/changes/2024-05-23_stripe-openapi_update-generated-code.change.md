---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1331
is_stripe_api_change: true
released_in_version: 9.9.0b1
---

* Change type of `refund` on  `stripe.CreditNote.CreateParamsRefund`, `stripe.CreditNote.PreviewParamsRefund`, and `stripe.CreditNote.PreviewLinesParamsRefund` from `str` to `NotRequired[str]`
* Add support for `terminal_reader_invalid_location_for_payment` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
