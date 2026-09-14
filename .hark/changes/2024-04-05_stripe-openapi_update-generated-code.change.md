---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1293
is_stripe_api_change: true
released_in_version: 8.11.0b1
---

* Add support for `risk_controls` on parameter class `stripe.Account.CreateParams` and resource `stripe.Account`
* Add support for `promotion_code` on parameter classes `stripe.Invoice.AddLinesParamsLineDiscount`, `stripe.Invoice.CreateParamsDiscount`, `stripe.Invoice.ModifyParamsDiscount`, `stripe.Invoice.UpdateLinesParamsLineDiscount`, `stripe.InvoiceItem.CreateParamsDiscount`, `stripe.InvoiceItem.ModifyParamsDiscount`, `stripe.InvoiceLineItem.ModifyParamsDiscount`, `stripe.Quote.CreateParamsDiscount`, `stripe.Quote.CreateParamsLineActionAddDiscount`, `stripe.Quote.CreateParamsLineItemDiscount`, `stripe.Quote.CreateParamsPhaseLineItemDiscount`, `stripe.Quote.ModifyParamsDiscount`, `stripe.Quote.ModifyParamsLineActionAddDiscount`, `stripe.Quote.ModifyParamsLineItemDiscount`, and `stripe.Quote.ModifyParamsPhaseLineItemDiscount`
* Add support for `zip` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for `offline` on resource class `stripe.SetupAttempt.PaymentMethodDetails.CardPresent`
* Add support for `card_present` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
* Add support for `modify` on resource `stripe.entitlements.Feature`
* Add support for `email` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
* Add support for `phone` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
* Add support for `verification_flow` on resources `stripe.identity.VerificationReport` and `stripe.identity.VerificationSession` and parameter class `stripe.identity.VerificationSession.CreateParams`
* Add support for `provided_details` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ModifyParams` and resource `stripe.identity.VerificationSession`
* Add support for `allowed_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
* Add support for `blocked_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
* Change type of field `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSwish` from `Literal['']|str` to `str` of `reference`
* Add support for `verification_flow` on enums `stripe.identity.VerificationReport.type` and `stripe.identity.VerificationSession.type`
* Add support for `email_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `email_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `phone_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `phone_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `mobile_phone_reader` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
* Change type of field `stripe.identity.VerificationSession.CreateParams` from `Literal['document', 'id_number']` to `NotRequired[Literal['document', 'id_number']]` of `type`
* Change type of fields `stripe.Invoice`, `stripe.InvoiceLineItem`, `stripe.QuotePreviewInvoice`, `stripe.Subscription`, and `stripe.SubscriptionItem` from `Optional[List[ExpandableField[Discount]]]` to `List[ExpandableField[Discount]]` of `discounts`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `data`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `image_url_png`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `image_url_svg`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str` of `hosted_instructions_url`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str` of `mobile_auth_url`
* Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[QrCode]` to `QrCode` of `qr_code`
* Change type of fields `stripe.QuoteLine.Action.AddItem`, `stripe.QuoteLine.Action.SetItem`, `stripe.QuotePreviewSubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.QuotePreviewSubscriptionSchedule.Phase.Item`, `stripe.QuotePreviewSubscriptionSchedule.Phase`, `stripe.SubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.SubscriptionSchedule.Phase.Item`, and `stripe.SubscriptionSchedule.Phase` from `Optional[List[Discount]]` to `List[Discount]` of `discounts`
