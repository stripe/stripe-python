---
title: "Generated changes from [#1749](https://github.com/stripe/stripe-python/pull/1749), [#1771](https://github.com/stripe/stripe-python/pull/1771), [#1773](https://github.com/stripe/stripe-python/pull/1773), [#1775](https://github.com/stripe/stripe-python/pull/1775)"
is_breaking: true
is_stripe_api_change: true
section: ⚠️ Breaking changes  due to changes in the Stripe API
released_in_version: 15.0.0
---

* Add support for `upi_payments` on `Account.Capability`, `AccountCreateParamsCapability`, and `AccountModifyParamsCapability`
* Add support for `upi` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `Mandate.PaymentMethodDetail`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodOption`, `SetupIntentModifyParamsPaymentMethodDatum`, `SetupIntentModifyParamsPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `tempo` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
* Add support for `integration_identifier` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for new value `upi` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, `SetupIntentModifyParams.excluded_payment_method_types`, and `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `crypto` on `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `upi` on enum `checkout.SessionCreateParams.payment_method_types`
* Add support for `pending_invoice_item_interval` on `checkout.SessionCreateParamsSubscriptionDatum`
* Add support for new values `elements`, `embedded_page`, `form`, and `hosted_page` on enums `Checkout.Session.ui_mode` and `checkout.SessionCreateParams.ui_mode`
* Add support for new value `marine_carbon_removal` on enum `Climate.Supplier.removal_pathway`
* Add support for new value `upi` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for new value `upi` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for `metadata` on `CreditNoteCreateParamsLine`, `CreditNoteLineItem`, `CreditNotePreviewLinesParamsLine`, and `CreditNotePreviewParamsLine`
* Add support for new value `upi` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `quantity_decimal` on `InvoiceAddLinesParamsLine`, `InvoiceCreatePreviewParamsInvoiceItem`, `InvoiceItemCreateParams`, `InvoiceItemModifyParams`, `InvoiceItem`, `InvoiceLineItemModifyParams`, `InvoiceLineItem`, and `InvoiceUpdateLinesParamsLine`
* ⚠️ Add support for `level` on `issuing.AuthorizationCreateParamsRiskAssessmentCardTestingRisk` and `issuing.AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk`
* ⚠️ Remove support for `risk_level` on `issuing.AuthorizationCreateParamsRiskAssessmentCardTestingRisk` and `issuing.AuthorizationCreateParamsRiskAssessmentMerchantDisputeRisk`
* Add support for `lifecycle_controls` on `Issuing.Card` and `issuing.CardCreateParams`
* ⚠️ Change type of `Issuing.Token.NetworkDatum.Visa.card_reference_id` from `string` to `nullable(string)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.brand` and `PaymentRecord.PaymentMethodDetail.Card.brand` from `enum` to `nullable(enum)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_month` and `PaymentRecord.PaymentMethodDetail.Card.exp_month` from `longInteger` to `nullable(longInteger)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_year` and `PaymentRecord.PaymentMethodDetail.Card.exp_year` from `longInteger` to `nullable(longInteger)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.funding` and `PaymentRecord.PaymentMethodDetail.Card.funding` from `enum('credit'|'debit'|'prepaid'|'unknown')` to `nullable(enum('credit'|'debit'|'prepaid'|'unknown'))`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.last4` and `PaymentRecord.PaymentMethodDetail.Card.last4` from `string` to `nullable(string)`
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.Card.moto` and `PaymentRecord.PaymentMethodDetail.Card.moto` from `boolean` to `nullable(boolean)`
* Add support for `cryptogram`, `electronic_commerce_indicator`, `exemption_indicator_applied`, and `exemption_indicator` on `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure` and `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure`
* Add support for `upi_handle_redirect_or_display_qr_code` on `PaymentIntent.NextAction` and `SetupIntent.NextAction`
* Add support for new value `upi` on enums `PaymentLink.payment_method_types`, `PaymentLinkCreateParams.payment_method_types`, and `PaymentLinkModifyParams.payment_method_types`
* Add support for `recommended_action` and `signals` on `Radar.PaymentEvaluation`
* ⚠️ Remove support for `insights` on `Radar.PaymentEvaluation`
* Add support for new value `crypto_fingerprint` on enums `Radar.ValueList.item_type` and `radar.ValueListCreateParams.item_type`
* Add support for new value `canceled_by_retention_policy` on enum `Subscription.CancellationDetail.reason`
* Add support for new value `2026-03-25.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* ⚠️ Change type of `V2.Core.EventDestination.events_from` and `v2.core.EventDestinationCreateParams.events_from` from `enum('other_accounts'|'self')` to `string`
* Add support for error code `service_period_coupon_with_metered_tiered_item_unsupported` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
