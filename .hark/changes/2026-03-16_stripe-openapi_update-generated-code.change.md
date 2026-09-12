---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1755
is_breaking: true
is_stripe_api_change: true
released_in_version: 14.5.0a4
---

* Add support for new resources `orchestration.PaymentAttempt` and `radar.CustomerEvaluation`
* Add support for `retrieve` method on resource `orchestration.PaymentAttempt`
* Add support for `create` and `modify` methods on resource `radar.CustomerEvaluation`
* Add support for `approve` method on resource `checkout.Session`
* Add support for `report_authenticated`, `report_canceled`, `report_failed`, `report_guaranteed`, `report_informational`, and `report_refund` methods on resource `PaymentAttemptRecord`
* Add support for `create_us_paper_check_on_application` on `AccountSessionCreateParamsComponentCheckScanningFeature`
* ⚠️ Change `AccountSignals.delinquency` to be optional
* Add support for `approval_method` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for `current_attempt` on `Checkout.Session`
* Add support for `selected_fulfillment_option_overrides` on `delegated_checkout.RequestedSessionModifyParamsFulfillmentDetail`
* Add support for `pricing_plan_subscription_details` on `InvoiceItem.Parent` and `InvoiceLineItem.Parent`
* ⚠️ Remove support for `license_fee_subscription_details` on `InvoiceItem.Parent` and `InvoiceLineItem.Parent`
* ⚠️ Remove support for `pricing_plan_subscription` and `pricing_plan_version` on `InvoiceItem.Parent.RateCardSubscriptionDetail` and `InvoiceLineItem.Parent.RateCardSubscriptionDetail`
* Add support for new value `pricing_plan_subscription_details` on enum `InvoiceItem.Parent.type`
* ⚠️ Remove support for value `license_fee_subscription_details` from enum `InvoiceItem.Parent.type`
* Add support for new value `discounts` on enum `InvoiceItem.frozen_fields`
* Add support for new value `pricing_plan_subscription_details` on enum `InvoiceLineItem.Parent.type`
* ⚠️ Remove support for value `license_fee_subscription_details` from enum `InvoiceLineItem.Parent.type`
* Add support for `token_details` on `Issuing.Authorization`
* Add support for `failure_code` on `PaymentRecordReportPaymentAttemptFailedParams`, `PaymentRecordReportPaymentAttemptParamsFailed`, and `PaymentRecordReportPaymentParamsFailed`
* Change `PaymentRecordReportPaymentAttemptCanceledParams.canceled_at` to be optional
* Change `PaymentRecordReportPaymentAttemptFailedParams.failed_at` to be optional
* Change `PaymentRecordReportPaymentAttemptGuaranteedParams.guaranteed_at` to be optional
* Change `PaymentRecordReportRefundParams.refunded` to be optional
* ⚠️ Remove support for value `now` from enums `QuoteCreateParamsSubscriptionDataOverrideBillingScheduleBillFrom.type`, `QuoteCreateParamsSubscriptionDatumBillingScheduleBillFrom.type`, `QuoteModifyParamsSubscriptionDataOverrideBillingScheduleBillFrom.type`, and `QuoteModifyParamsSubscriptionDatumBillingScheduleBillFrom.type`
* ⚠️ Change `radar.IssuingAuthorizationEvaluationCreateParamsCardDetail.bin_country` to be required
* Add support for `recurring_interval` on `shared_payment.GrantedTokenCreateParamsUsageLimit`
* Change `shared_payment.GrantedTokenCreateParamsUsageLimit.expires_at` to be optional
* Add support for `home_rule_tax` on `Tax.Registration.CountryOption.Me` and `tax.RegistrationCreateParamsCountryOptionMe`
* Add support for new value `home_rule_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
