---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1892
semver_level: major
is_stripe_api_change: true
---

* Add support for new resource `radar.BillingEvaluation`
* Add support for `create` method on resource `radar.BillingEvaluation`
* Add support for `list` method on resource `reserve.Plan`
* Change `Tax.CalculationLineItem.performance_location` and `TaxCode.Requirement.performance_location` to be required
* Change `Account.BusinessProfile.specified_commercial_transactions_act_url` to be required
* Add support for `after_expiration` on `BillingPortal.Session` and `billing_portal.SessionCreateParams`
* Add support for new value `fundbox_ca_financing` on enums `Capital.FinancingOffer.disclaimer_variant` and `Capital.FinancingSummary.Detail.disclaimer_variant`
* Add support for `setup_credential_usage` on `Charge.PaymentMethodDetail.Card`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCard`, `SetupIntent.PaymentMethodOption.Card`, `SetupIntentConfirmParamsPaymentMethodOptionCard`, `SetupIntentCreateParamsPaymentMethodOptionCard`, and `SetupIntentModifyParamsPaymentMethodOptionCard`
* Add support for `stored_credential_usage` on `Charge.PaymentMethodDetail.Card`, `PaymentAttemptRecord.PaymentMethodDetail.Card`, `PaymentIntent.PaymentMethodOption.Card`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCard`, and `PaymentRecord.PaymentMethodDetail.Card`
* Add support for `expires_at` on `Subscription.PaymentSetting.PaymentMethodOption.Blik.MandateOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionBlikMandateOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionBlikMandateOption`, and `checkout.SessionCreateParamsPaymentMethodOptionBlikMandateOption`
* ⚠️ Remove support for `expires_after` on `Subscription.PaymentSetting.PaymentMethodOption.Blik.MandateOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionBlikMandateOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionBlikMandateOption`, and `checkout.SessionCreateParamsPaymentMethodOptionBlikMandateOption`
* ⚠️ Remove support for value `on_session` from enum `checkout.SessionCreateParamsPaymentMethodOptionBlik.setup_future_usage`
* Add support for `payment_intent_data` on `checkout.SessionModifyParams`
* Add support for `appeal` on `Dispute.Evidence` and `DisputeModifyParamsEvidence`
* Add support for `livemode` on `FxQuote`
* ⚠️ Remove support for `capture_method` on `PaymentIntentConfirmParamsPaymentMethodOptionPaypay`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay`
* Add support for `active` on `ProductCatalog.TrialOffer`, `product_catalog.TrialOfferCreateParams`, and `product_catalog.TrialOfferListParams`
* Add support for `nickname` on `ProductCatalog.TrialOffer` and `product_catalog.TrialOfferCreateParams`
* ⚠️ Remove support for `name` on `ProductCatalog.TrialOffer` and `product_catalog.TrialOfferCreateParams`
* ⚠️ Change `ProductCatalog.TrialOffer.EndBehavior.transition` to be optional
* Change `Product.tax_details` to be required
* Add support for `status_details` on `QuotePreviewInvoice`
* Add support for `company_details` and `reference` on `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Billie`
* Add support for `pause_schedules` on `QuotePreviewSubscriptionSchedule`
* Add support for `destination` on `Reserve.Hold`, `Reserve.Plan`, and `Reserve.Release`
* Add support for `manual_release` on `Reserve.Plan`
* ⚠️ Add support for new value `other` on enum `Reserve.Plan.status`
* ⚠️ Add support for new values `manual_release` and `other` on enum `Reserve.Plan.type`
* ⚠️ Add support for new value `hold_expired` on enum `Reserve.Release.reason`
* ⚠️ Remove support for value `bulk_hold_expiry` from enum `Reserve.Release.reason`
* Change `SubscriptionItem.current_trial` to be required
* Change `Subscription.TrialSetting.EndBehavior.billing_cycle_anchor` to be required
* Add support for new value `igic` on enums `Tax.Registration.CountryOption.E.type` and `tax.RegistrationCreateParamsCountryOptionE.type`
* Change `TaxCode.requirements` to be required
* Add support for error codes `dispute_evidence_page_limit_exceeded`, `financial_connections_consent_locale_invalid`, `financial_connections_consent_locale_unsupported`, and `payment_evaluation_on_api_version_not_supported` on `QuotePreviewInvoice.LastFinalizationError`
