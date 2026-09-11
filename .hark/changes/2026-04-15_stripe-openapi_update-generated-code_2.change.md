---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1791
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.1.0a4
---

* Add support for new resources `v2.core.WorkflowRun` and `v2.core.Workflow`
* Add support for `report_authorized` method on resource `PaymentAttemptRecord`
* Add support for `list` and `retrieve` methods on resource `v2.core.WorkflowRun`
* Add support for `invoke`, `list`, and `retrieve` methods on resource `v2.core.Workflow`
* Add support for `next_action` and `status` on `SharedPayment.IssuedToken`
* ⚠️ Remove support for `network_id` on `SharedPayment.IssuedToken.SellerDetail`
* Add support for `bills` on `AccountSession.Component`
* Add support for `settlement_currencies` on `BalanceSettings.Payment` and `BalanceSettingsModifyParamsPayment`
* Add support for `default_settlement_currency` on `BalanceSettings.Payment`
* Add support for `account_funding` on `Charge.PaymentMethodDetail.Card`
* Add support for `automatic_surcharge` on `Checkout.Session`, `PaymentLinkCreateParams`, `PaymentLink`, and `checkout.SessionCreateParams`
* Add support for `bizum` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for `surcharge_cost` on `Checkout.Session`
* Add support for `amount_surcharge` on `Checkout.Session.TotalDetail`
* Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for new value `email` on enums `identity.VerificationReportListParams.type`, `identity.VerificationSessionCreateParams.type`, and `identity.VerificationSessionModifyParams.type`
* Add support for `details` on `Identity.VerificationReport.Email`
* ⚠️ Add support for new value `email` on enums `Identity.VerificationReport.type` and `Identity.VerificationSession.type`
* Add support for `confirm` on `identity.VerificationSessionCreateParams` and `identity.VerificationSessionModifyParams`
* Add support for `subscription` on `InvoiceItem.Parent.ScheduleDetail`
* ⚠️ Remove support for `shared_payment_granted_token` on `PaymentIntentConfirmParams` and `PaymentIntentCreateParams`
* Add support for `money_services` on `PaymentIntent.PaymentDetail`
* ⚠️ Remove support for `external_reference` on `Plan`
* Change `SharedPayment.GrantedToken.PaymentMethodDetail.billing_details` to be required
