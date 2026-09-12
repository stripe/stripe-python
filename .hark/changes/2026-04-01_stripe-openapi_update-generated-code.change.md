---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1778
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.1.0a2
---

* Add support for new resources `shared_payment.IssuedToken` and `v2.data.reporting.QueryRun`
* Add support for `create` and `retrieve` methods on resource `v2.data.reporting.QueryRun`
* Add support for `pause` and `resume` methods on resource `v2.payments.OffSessionPayment`
* Add support for `tenant_keys`, `tenant_operator`, and `tenant_values` on `billing.BillingMeterListMeterEventSummaryParams`
* Add support for `money_services` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
* Add support for `payment_method_options` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
* ⚠️ Remove support for `payment_method_data` on `delegated_checkout.RequestedSessionConfirmParams`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
* Add support for `card_brands` and `payment_method_types` on `DelegatedCheckout.RequestedSession.SellerDetail`
* ⚠️ Change type of `DelegatedCheckout.RequestedSession.shared_payment_issued_token` from `string` to `expandable($SharedPayment.IssuedToken)`
* Add support for `check_scan` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`
* ⚠️ Add support for new value `check_scan` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for `processor_details` on `PaymentAttemptRecordReportFailedParams`, `PaymentAttemptRecordReportGuaranteedParams`, `PaymentRecordReportPaymentAttemptFailedParams`, `PaymentRecordReportPaymentAttemptGuaranteedParams`, `PaymentRecordReportPaymentAttemptParamsFailed`, `PaymentRecordReportPaymentAttemptParamsGuaranteed`, `PaymentRecordReportPaymentParamsFailed`, and `PaymentRecordReportPaymentParamsGuaranteed`
* Add support for `payment_details` on `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCard`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCard`, `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCard`
* ⚠️ Remove support for `bill_from` on `QuotePreviewSubscriptionSchedule.BillingSchedule`, `Subscription.BillingSchedule`, and `SubscriptionSchedule.BillingSchedule`
* Add support for `agent_details`, `payment_method_details`, and `risk_details` on `SharedPayment.GrantedToken`
* Add support for `paper_checks` on `V2.Account.Configuration.RecipientDatum.Feature`, `V2.Core.Account.Configuration.Recipient.Capability`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment`, `v2.AccountCreateParamsConfigurationRecipientDatumFeature`, `v2.AccountModifyParamsConfigurationRecipientDatumFeature`, `v2.core.AccountCreateParamsConfigurationRecipientCapability`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPayment`, `v2.core.AccountModifyParamsConfigurationRecipientCapability`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPayment`
* ⚠️ Add support for new value `paper_checks` on enum `V2.Account.Configuration.SupportableFeature.recipient_data`
* ⚠️ Add support for new value `paper_checks` on enum `V2.Account.Requirement.Impact.required_for_features`
* ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.konbini`, `V2.Billing.CollectionSetting.PaymentMethodOption.konbini`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.konbini`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.konbini`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.konbini` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSetting.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.sepa_debit`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.sepa_debit`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.sepa_debit` from `map(string: dynamic)` to `an object`
* Add support for `id` on `V2.Billing.CadenceSpendModifier.MaxBillingPeriodSpend.Amount.CustomPricingUnit`, `V2.Billing.IntentAction.Apply.SpendModifierRule.MaxBillingPeriodSpend.Amount.CustomPricingUnit`, and `v2.billing.IntentCreateParamsActionApplySpendModifierRuleMaxBillingPeriodSpendAmountCustomPricingUnit`
* ⚠️ Add support for new values `outbound_payments.paper_checks` and `paper_checks` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* ⚠️ Add support for new values `bm_crn`, `bo_tin`, `bt_tpn`, `co_nit`, `ec_ruc`, `eg_tin`, `gh_tin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_crn`, `ke_pin`, `ky_crn`, `lk_tin`, `mo_tin`, `mv_tin`, `ng_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `sl_tin`, `sv_nit`, `uy_ruc`, `vg_cn`, and `za_tin` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
* ⚠️ Add support for new values `bm_pp`, `bo_ci`, `bt_cid`, `eg_tin`, `gh_pin`, `gy_tin`, `hn_rtn`, `jm_trn`, `jo_pin`, `ky_pp`, `lk_nic`, `mo_bir`, `mt_nic`, `mv_tin`, `pa_ruc`, `ph_tin`, `py_ruc`, `si_pin`, `sv_nit`, and `vg_pp` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, `v2.core.AccountPersonModifyParamsIdNumber.type`, `v2.core.AccountPersonTokenCreateParamsIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityIndividualIdNumber.type`
* ⚠️ Change type of `V2.Core.Event.Reason.Request.Client.stripe_action` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_processing` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_queued` from `map(string: dynamic)` to `an object`
* ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_succeeded` from `map(string: dynamic)` to `an object`
* ⚠️ Add support for new values `paper_check_attachment_too_large`, `paper_check_expired`, and `paper_check_undeliverable` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* ⚠️ Remove support for `town` on `V2.MoneyManagement.OutboundPayment.TrackingDetail.PaperCheck.MailingAddress`
* Change `V2.MoneyManagement.OutboundPayment.DeliveryOption.PaperCheck.memo` to be required
* ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
* Add support for `application_fee_amount_requested` on `V2.Payments.OffSessionPayment`
* ⚠️ Remove support for `compartment_id` on `V2.Payments.OffSessionPayment`
* ⚠️ Add support for new value `exceeded_retry_window` on enum `V2.Payments.OffSessionPayment.failure_reason`
* Add support for `retry_until` on `V2.Payments.OffSessionPayment.RetryDetail`
* ⚠️ Add support for new value `paused` on enum `V2.Payments.OffSessionPayment.status`
* ⚠️ Change `V2.Reporting.ReportRun.Result.file` to be optional
* Add support for `application_fee_amount` on `v2.payments.OffSessionPaymentCaptureParams` and `v2.payments.OffSessionPaymentCreateParams`
* ⚠️ Add support for new value `paper_checks` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
* ⚠️ Add support for new value `outbound_payments.paper_checks` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for `alert_id` on `EventsV2CoreHealthApiErrorResolvedEvent`, `EventsV2CoreHealthApiLatencyResolvedEvent`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent`, `EventsV2CoreHealthPaymentMethodErrorResolvedEvent`, `EventsV2CoreHealthSepaDebitDelayedFiringEvent`, `EventsV2CoreHealthSepaDebitDelayedResolvedEvent`, `EventsV2CoreHealthTrafficVolumeDropResolvedEvent`, and `EventsV2CoreHealthWebhookLatencyResolvedEvent`
* Add support for `api_key` on `EventsV2IamApiKeyCreatedEvent`, `EventsV2IamApiKeyDefaultSecretRevealedEvent`, `EventsV2IamApiKeyExpiredEvent`, `EventsV2IamApiKeyPermissionsUpdatedEvent`, `EventsV2IamApiKeyRotatedEvent`, and `EventsV2IamApiKeyUpdatedEvent`
* Add support for `stripe_access_grant` on `EventsV2IamStripeAccessGrantApprovedEvent`, `EventsV2IamStripeAccessGrantCanceledEvent`, `EventsV2IamStripeAccessGrantDeniedEvent`, `EventsV2IamStripeAccessGrantRemovedEvent`, `EventsV2IamStripeAccessGrantRequestedEvent`, and `EventsV2IamStripeAccessGrantUpdatedEvent`
* Add support for event notifications `V2DataReportingQueryRunCreatedEvent`, `V2DataReportingQueryRunFailedEvent`, `V2DataReportingQueryRunSucceededEvent`, and `V2DataReportingQueryRunUpdatedEvent` with related object `v2.data.reporting.QueryRun`
* Add support for event notifications `V2PaymentsOffSessionPaymentPausedEvent` and `V2PaymentsOffSessionPaymentResumedEvent` with related object `v2.payments.OffSessionPayment`
