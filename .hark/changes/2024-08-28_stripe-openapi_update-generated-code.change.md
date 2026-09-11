---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1380
is_stripe_api_change: true
released_in_version: 10.11.0b1
---

* Add support for `email` on resource class `stripe.checkout.Session.CollectedInformation`
* Add support for `phone` on resource class `stripe.checkout.Session.CollectedInformation`
* Add support for `regulatory_reporting_file` on parameter classes `stripe.issuing.CreditUnderwritingRecord.CorrectParams`, `stripe.issuing.CreditUnderwritingRecord.CreateFromProactiveReviewParams`, and `stripe.issuing.CreditUnderwritingRecord.ReportDecisionParams` and resource `stripe.issuing.CreditUnderwritingRecord`
* Add support for resource `stripe.terminal.ReaderCollectedData`
* Remove support for `rechnung` on parameter class `stripe.PaymentMethod.ModifyParams`
* Add support for `mb_way` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
* Add support for `terminal_reader_collected_data_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
