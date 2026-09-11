---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1284
is_stripe_api_change: true
released_in_version: 8.10.0
---

* Add support for `subscription_item` on resource `stripe.Discount`
* Add support for `promotion_code` on parameter classes `stripe.Invoice.CreateParamsDiscount`, `stripe.Invoice.ModifyParamsDiscount`, `stripe.InvoiceItem.CreateParamsDiscount`, `stripe.InvoiceItem.ModifyParamsDiscount`, `stripe.InvoiceLineItem.ModifyParamsDiscount`, `stripe.Quote.CreateParamsDiscount`, and `stripe.Quote.ModifyParamsDiscount`
* Add support for `discounts` on parameter classes `stripe.Invoice.UpcomingLinesParamsSubscriptionItem`, `stripe.Invoice.UpcomingParamsSubscriptionItem`, `stripe.Quote.CreateParamsLineItem`, `stripe.Quote.ModifyParamsLineItem`, `stripe.Subscription.CreateParams`, `stripe.Subscription.CreateParamsAddInvoiceItem`, `stripe.Subscription.CreateParamsItem`, `stripe.Subscription.ModifyParams`, `stripe.Subscription.ModifyParamsAddInvoiceItem`, `stripe.Subscription.ModifyParamsItem`, `stripe.SubscriptionItem.CreateParams`, `stripe.SubscriptionItem.ModifyParams`, `stripe.SubscriptionSchedule.CreateParamsPhase`, `stripe.SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem`, `stripe.SubscriptionSchedule.CreateParamsPhaseItem`, `stripe.SubscriptionSchedule.ModifyParamsPhase`, `stripe.SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem`, and `stripe.SubscriptionSchedule.ModifyParamsPhaseItem`, resources `stripe.Subscription` and `stripe.SubscriptionItem`, and resource classes `stripe.SubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.SubscriptionSchedule.Phase.Item`, and `stripe.SubscriptionSchedule.Phase`
* Add support for `zip` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
* Add support for `offline` on resource class `stripe.SetupAttempt.PaymentMethodDetails.CardPresent`
* Add support for `card_present` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
* Add support for `email` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
* Add support for `phone` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
* Add support for `verification_flow` on resources `stripe.identity.VerificationReport` and `stripe.identity.VerificationSession` and parameter class `stripe.identity.VerificationSession.CreateParams`
* Add support for `provided_details` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ModifyParams` and resource `stripe.identity.VerificationSession`
* Add support for `allowed_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
* Add support for `blocked_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
* Change type of `reference` on  `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSwish` from `Literal['']|str` to `str`
* Add support for `verification_flow` on enums `stripe.identity.VerificationReport.type` and `stripe.identity.VerificationSession.type`
* Add support for `email_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `email_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `phone_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `phone_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
* Add support for `mobile_phone_reader` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
* Change type of `type` on  `stripe.identity.VerificationSession.CreateParams` from `Literal['document', 'id_number']` to `NotRequired[Literal['document', 'id_number']]`
* Change type of `discounts` on  `stripe.Invoice` and `stripe.InvoiceLineItem` from `Optional[List[ExpandableField[Discount]]]` to `List[ExpandableField[Discount]]`
* Change type of `data` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
* Change type of `image_url_png` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
* Change type of `image_url_svg` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
* Change type of `hosted_instructions_url` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str`
* Change type of `mobile_auth_url` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str`
* Change type of `qr_code` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[QrCode]` to `QrCode`
