---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1859
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.5.0a2
---

* Add support for new resource `billing.FeedbackOptions`
* Add support for `sequra_payments` on `Account.Capability`
* Add support for `feedback_options` on `BillingPortal.Configuration.Feature.SubscriptionCancel.CancellationReason`
* Add support for `sequra` on `Charge.PaymentMethodDetail`, `Checkout.Session.PaymentMethodOption`, `ConfirmationToken.PaymentMethodPreview`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, and `PaymentRecord.PaymentMethodDetail`
* Add support for `retrieval_reference_number` on `Charge.PaymentMethodDetail.CardPresent`, `ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, `PaymentAttemptRecord.PaymentMethodDetail.CardPresent`, `PaymentMethod.Card.GeneratedFrom.PaymentMethodDetail.CardPresent`, and `PaymentRecord.PaymentMethodDetail.CardPresent`
* Add support for `pricing_group` on `Charge.PaymentMethodDetail.Link`
* Add support for `tax_rates` on `Checkout.Session.ShippingOption`, `checkout.SessionCreateParamsShippingOption`, and `checkout.SessionModifyParamsShippingOption`
* ⚠️ Add support for new value `daikin` on enums `Checkout.Session.AutomaticSurcharge.provider` and `PaymentLink.AutomaticSurcharge.provider`
* Add support for `funding_types_blocked` on `Checkout.Session.PaymentMethodOption.Card.Restriction`
* Add support for new value `sequra` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for new value `sequra` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for new value `sequra` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `healthcare` on `issuing.AuthorizationCaptureParamsPurchaseDetail`, `issuing.AuthorizationCreateParams`, `issuing.TransactionCreateForceCaptureParamsPurchaseDetail`, and `issuing.TransactionCreateUnlinkedRefundParamsPurchaseDetail`
* Change type of `Issuing.Authorization.Healthcare.verification_status` from `nullable(enum('iias_merchant_exempt'|'iias_merchant_not_certified'|'iias_verified'|'not_verified'))` to `enum('iias_merchant_exempt'|'iias_merchant_not_certified'|'iias_verified'|'not_verified')`
* Add support for `is_anomalous` on `PaymentAttemptRecordReportGuaranteedParams`
* Add support for new value `sequra` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for `aade_data` on `PaymentIntent.PaymentMethodOption.CardPresent`
* Change `Radar.PaymentEvaluation.PaymentDetail.PaymentMethodDetail.Card.first6` to be required
* Change `Radar.PaymentEvaluation.PaymentDetail.PaymentMethodDetail.Card.last4` to be required
* Add support for `feedback_option` on `Subscription.CancellationDetail`
* Add support for `application` on `V2.Payments.OffSessionPayment`
* Add support for `status` on `v2.money_management.FinancialAccountStatementListParams`
* Change `v2.billing.ContractCreateParams.pricing_lines` to be optional
