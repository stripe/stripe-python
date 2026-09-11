---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1443
is_stripe_api_change: true
released_in_version: 11.6.0
---

* Add support for `pay_by_bank_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
* Add support for `directorship_declaration` on resource class `stripe.Account.Company` and parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
* Add support for `ownership_exemption_reason` on resource class `stripe.Account.Company` and parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
* Add support for `proof_of_ultimate_beneficial_ownership` on parameter class `stripe.Account.CreateParamsDocuments`
* Add support for `financial_account` on resource classes `stripe.AccountSession.Components` and `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `issuing_card` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* Add support for `advice_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
* Add support for `country` on resource classes `stripe.Charge.PaymentMethodDetails.Paypal`, `stripe.ConfirmationToken.PaymentMethodPreview.Paypal`, and `stripe.PaymentMethod.Paypal`
* Add support for `pay_by_bank` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
* Add support for `phone_number_collection` on parameter class `stripe.PaymentLink.ModifyParams`
* Add support for `discounts` on resource `stripe.checkout.Session`
* Add support for `jpy` on parameter classes `stripe.terminal.Configuration.CreateParamsTipping` and `stripe.terminal.Configuration.ModifyParamsTipping` and resource class `stripe.terminal.Configuration.Tipping`
* Add support for `nickname` on parameter classes `stripe.treasury.FinancialAccount.CreateParams` and `stripe.treasury.FinancialAccount.ModifyParams` and resource `stripe.treasury.FinancialAccount`
* Add support for `forwarding_settings` on parameter class `stripe.treasury.FinancialAccount.ModifyParams`
* Add support for `_cls_close` on resource `stripe.treasury.FinancialAccount`
* Add support for `close` on resource `stripe.treasury.FinancialAccount`
* Add support for `is_default` on resource `stripe.treasury.FinancialAccount`
* Add support for `destination_payment_method_data` on parameter class `stripe.treasury.OutboundTransfer.CreateParams`
* Add support for `outbound_transfer` on resource class `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails`
* Add support for `SD` on enums `stripe.checkout.Session.ShippingAddressCollection.allowed_countries`, `stripe.checkout.Session.CreateParamsShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.ShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.CreateParamsShippingAddressCollection.allowed_countries`, and `stripe.PaymentLink.ModifyParamsShippingAddressCollection.allowed_countries`
* Add support for `pay_by_bank` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
* Add support for `financial_account` on enum `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails.type`
* Add support for `outbound_transfer` on enums `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails.type` and `stripe.treasury.ReceivedCredit.ListParamsLinkedFlows.source_flow_type`
* Add support for `2025-01-27.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
* Change type of `pretax_credit_amounts` on  `stripe.CreditNote` and `stripe.CreditNoteLineItem` from `Optional[List[PretaxCreditAmount]]` to `List[PretaxCreditAmount]`
