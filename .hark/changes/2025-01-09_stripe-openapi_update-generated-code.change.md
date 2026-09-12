---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1433
is_stripe_api_change: true
released_in_version: 11.5.0b1
---

* Add support for `directorship_declaration` on resource class `stripe.Account.Company`
* Add support for `ownership_exemption_reason` on resource class `stripe.Account.Company` and parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
* Add support for `brand_product` on resource `stripe.Card` and resource classes `stripe.Source.Card`, `stripe.Source.CardPresent`, and `stripe.Source.ThreeDSecure`
* Add support for `advice_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
* Add support for `country` on resource classes `stripe.Charge.PaymentMethodDetails.Paypal`, `stripe.ConfirmationToken.PaymentMethodPreview.Paypal`, and `stripe.PaymentMethod.Paypal`
* Add support for `phone_number_collection` on parameter class `stripe.PaymentLink.ModifyParams`
* Add support for `nickname` on parameter classes `stripe.treasury.FinancialAccount.CreateParams` and `stripe.treasury.FinancialAccount.ModifyParams` and resource `stripe.treasury.FinancialAccount`
* Add support for `forwarding_settings` on parameter class `stripe.treasury.FinancialAccount.ModifyParams`
* Add support for `_cls_close` on resource `stripe.treasury.FinancialAccount`
* Add support for `close` on resource `stripe.treasury.FinancialAccount`
* Add support for `is_default` on resource `stripe.treasury.FinancialAccount`
* Add support for `destination_payment_method_data` on parameter class `stripe.treasury.OutboundTransfer.CreateParams`
* Add support for `financial_account` on resource class `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails`
* Add support for `outbound_transfer` on resource class `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails`
* Remove support for `always_invoice` on enums `stripe.billing_portal.Configuration.Features.SubscriptionCancel.proration_behavior`, `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionCancel.proration_behavior`, and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionCancel.proration_behavior`
* Add support for `al_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
* Add support for `financial_account` on enum `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails.type`
* Add support for `outbound_transfer` on enums `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails.type` and `stripe.treasury.ReceivedCredit.ListParamsLinkedFlows.source_flow_type`
* Change type of `pretax_credit_amounts` on  `stripe.CreditNote` and `stripe.CreditNoteLineItem` from `Optional[List[PretaxCreditAmount]]` to `List[PretaxCreditAmount]`
