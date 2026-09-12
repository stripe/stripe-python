---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1356
is_stripe_api_change: true
released_in_version: 10.4.0b1
---

* Change type of `payment_element` on  `stripe.CustomerSession.Components` from `Optional[PaymentElement]` to `PaymentElement`
* Add support for `not_qualified` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
* Remove support for `billing_policy_remote_function_response_invalid` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
* Remove support for `billing_policy_remote_function_timeout` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
* Remove support for `billing_policy_remote_function_unexpected_status_code` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
* Remove support for `billing_policy_remote_function_unreachable` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
* Remove support for `payment_intent_fx_quote_invalid` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
