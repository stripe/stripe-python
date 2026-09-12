---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1377
is_stripe_api_change: true
released_in_version: 10.9.0b2
---

* Add support for `mb_way_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
* Add support for `mb_way` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
* Remove support for `phases` on parameter classes `stripe.Quote.CreateParams` and `stripe.Quote.ModifyParams`
* Remove support for `from_schedule` on parameter class `stripe.Quote.CreateParamsSubscriptionData`
* Add support for `mb_way` on enums `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
* Add support for `hr_oib` on enums `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Remove support for `accepted` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
* Remove support for `partner_rejected` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
* Remove support for `submitted` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
