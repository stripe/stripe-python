---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1650
is_stripe_api_change: true
released_in_version: 13.1.0
---

* Add support for new resources `PaymentAttemptRecord`, `PaymentIntentAmountDetailsLineItem`, and `PaymentRecord`
* Add support for `list` and `retrieve` methods on resource `PaymentAttemptRecord`
* Add support for `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_payment_attempt`, `report_payment`, `report_refund`, and `retrieve` methods on resource `PaymentRecord`
* Add support for `list` method on resource `PaymentIntentAmountDetailsLineItem`
* Add support for `representative_declaration` on `Account.Company`, `AccountCreateParamsCompany`, `AccountModifyParamsCompany`, and `TokenCreateParamsAccountCompany`
* Change `billing.CreditGrantCreateParams.category` to be optional
* Add support for `payment_method_configuration` on `billing_portal.ConfigurationCreateParamsFeaturePaymentMethodUpdate` and `billing_portal.ConfigurationModifyParamsFeaturePaymentMethodUpdate`
* Add support for new value `solana` on enum `Charge.PaymentMethodDetail.Crypto.network`
* Add support for new value `mb_way` on enum `checkout.SessionCreateParams.excluded_payment_method_types`
* Add support for `twint` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `mb_way` on enum `checkout.SessionCreateParams.payment_method_types`
* Add support for new value `custom` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for `payment_record_refund` and `type` on `CreditNote.Refund`, `CreditNoteCreateParamsRefund`, `CreditNotePreviewLinesParamsRefund`, and `CreditNotePreviewParamsRefund`
* Add support for `customer_sheet` and `mobile_payment_element` on `CustomerSession.Component` and `CustomerSessionCreateParamsComponent`
* Add support for new value `custom` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `provider` on `Customer.Tax`
* Add support for new values `balance_settings.updated` and `invoice.payment_attempt_required` on enum `Event.type`
* Add support for new value `platform_terms_of_service` on enums `File.purpose` and `FileListParams.purpose`
* Add support for new value `platform_terms_of_service` on enum `FileCreateParams.purpose`
* Add support for `payment_record` on `InvoiceAttachPaymentParams`, `InvoicePayment.Payment`, and `InvoicePaymentListParamsPayment`
* Change type of `InvoicePaymentListParamsPayment.type` from `literal('payment_intent')` to `enum('payment_intent'|'payment_record')`
* Add support for new value `custom` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for `amount_details` on `PaymentIntentCaptureParams`, `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentIncrementAuthorizationParams`, and `PaymentIntentModifyParams`
* Add support for `payment_details` on `PaymentIntentCaptureParams`, `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentIncrementAuthorizationParams`, `PaymentIntentModifyParams`, and `PaymentIntent`
* Add support for `discount_amount`, `line_items`, `shipping`, and `tax` on `PaymentIntent.AmountDetail`
* Add support for `name_collection` on `PaymentLinkCreateParams`, `PaymentLinkModifyParams`, and `PaymentLink`
* Add support for new value `mb_way` on enums `PaymentLink.payment_method_types`, `PaymentLinkCreateParams.payment_method_types`, and `PaymentLinkModifyParams.payment_method_types`
* Add support for `crypto` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, and `Refund.DestinationDetail`
* Add support for `mb_way` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, and `PaymentMethodConfiguration`
* Add support for `custom` on `PaymentMethodCreateParams` and `PaymentMethod`
* Add support for `excluded_payment_method_types` on `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
* Change `SetupIntent.flow_directions` to be optional
* Add support for `tw` on `Tax.Registration.CountryOption` and `tax.RegistrationCreateParamsCountryOption`
* Add support for `gip` on `Terminal.Configuration.Tipping`, `terminal.ConfigurationCreateParamsTipping`, and `terminal.ConfigurationModifyParamsTipping`
* Add support for `last_seen_at` on `Terminal.Reader`
* Add support for new values `balance_settings.updated` and `invoice.payment_attempt_required` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for new value `2025-10-29.clover` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `gt`, `gte`, `lt`, `lte`, and `types` on `v2.core.EventListParams`
* Change `v2.core.EventListParams.object_id` to be optional
* Add support for snapshot event `balance_settings.updated` with resource `BalanceSettings`
* Add support for snapshot event `invoice.payment_attempt_required` with resource `Invoice`
* Add support for error code `payment_intent_rate_limit_exceeded` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
