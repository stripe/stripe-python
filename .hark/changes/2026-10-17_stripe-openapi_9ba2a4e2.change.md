---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1945
semver_level: major
is_stripe_api_change: true
---

* Add support for new resource `risk.Form`
* Add support for `modify` and `retrieve` methods on resource `risk.Form`
* Add support for `business_profile_management` on `AccountSession.Component`
* Change type of `AccountSession.Component.terminal_hardware_orders` from `nullable(ConnectEmbeddedBaseConfig)` to `ConnectEmbeddedBaseConfig`
* Change type of `AccountSession.Component.terminal_hardware_shop` from `nullable(ConnectEmbeddedBaseConfig)` to `ConnectEmbeddedBaseConfig`
* Change `AccountSession.Component.terminal_hardware_orders` to be required
* Change `AccountSession.Component.terminal_hardware_shop` to be required
* Add support for new value `mandiri` on enums `Charge.PaymentMethodDetail.IdBankTransfer.bank`, `ConfirmationToken.PaymentMethodPreview.IdBankTransfer.bank`, `PaymentAttemptRecord.PaymentMethodDetail.IdBankTransfer.bank`, `PaymentMethod.IdBankTransfer.bank`, `PaymentRecord.PaymentMethodDetail.IdBankTransfer.bank`, and `SetupAttempt.PaymentMethodDetail.IdBankTransfer.bank`
* Add support for `marketing_attributions` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for new values `au_acn`, `au_wpn`, `cz_dic`, `fr_siren`, `fr_siret`, `fr_spi`, `is_kt`, `md_cf`, `mu_vat`, `mz_nuit`, `nz_bn`, `pt_nif`, `sm_coe`, `tt_bir`, and `tt_vat` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, and `Tax.Transaction.CustomerDetail.TaxId.type`
* Add support for `mandate_options` on `Checkout.Session.PaymentMethodOption.Card`
* ⚠️ Change type of `Dispute.Evidence.appeal` from `DisputeAppeal` to `nullable(DisputeAppeal)`
* Change `Dispute.EvidenceDetail.submission_method` to be required
* ⚠️ Remove support for value `email` from enums `identity.VerificationReportListParams.type`, `identity.VerificationSessionCreateParams.type`, and `identity.VerificationSessionModifyParams.type`
* ⚠️ Remove support for `details` on `Identity.VerificationReport.Email`
* ⚠️ Remove support for value `email` from enums `Identity.VerificationReport.type` and `Identity.VerificationSession.type`
* ⚠️ Remove support for `healthcare` on `issuing.AuthorizationCaptureParamsPurchaseDetail`, `issuing.TransactionCreateForceCaptureParamsPurchaseDetail`, and `issuing.TransactionCreateUnlinkedRefundParamsPurchaseDetail`
* Add support for `account_tax_ids`, `custom_fields`, `description`, and `footer` on `PaymentLink.SubscriptionDatum.InvoiceSetting`
* Change type of `Radar.PaymentEvaluation.Signal.early_fraud_warning` from `nullable(Payment Evaluation Signal)` to `Payment Evaluation Signal`
* ⚠️ Change `Radar.PaymentEvaluation.Signal.early_fraud_warning` to be optional
* Add support for `bw`, `ci`, `gh`, and `mu` on `Tax.Registration.CountryOption`
* Add support for new value `account_takeover` on enum `V2.Core.AccountEvaluation.evaluations_triggered`
* Add support for `czk`, `nok`, `pln`, and `sek` on `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapabilityBusinessStorageInbound`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapabilityBusinessStorageOutbound`, `v2.core.AccountModifyParamsConfigurationMoneyManagerCapabilityBusinessStorageInbound`, and `v2.core.AccountModifyParamsConfigurationMoneyManagerCapabilityBusinessStorageOutbound`
* Add support for `account_takeover_confirmation`, `account_takeover_report`, `credential_change`, `mfa_addition`, and `mfa_removal` on `V2.Signals.AccountActivity`, `v2.signals.AccountActivityCreateParams`, and `v2.signals.AccountEvaluationCreateParamsAccountActivityDetailData`
* Add support for new values `account_takeover_confirmation`, `account_takeover_mitigation`, `account_takeover_report`, `credential_change`, `mfa_addition`, and `mfa_removal` on enums `V2.Signals.AccountActivity.type`, `v2.signals.AccountActivityCreateParams.type`, and `v2.signals.AccountEvaluationCreateParamsAccountActivityDetailData.type`
* Add support for `account_takeover` on `V2.Signals.AccountEvaluation.EvaluatedSignal` and `V2.Signals.AccountSignal`
* Add support for new value `account_takeover` on enum `V2.Signals.AccountEvaluation.pending_signals`
* Add support for new value `account_takeover` on enums `V2.Signals.AccountEvaluation.requested_signals` and `v2.signals.AccountEvaluationCreateParams.requested_signals`
* Add support for `customer_risk` on `V2.Signals.AccountSignal`
* Add support for new values `account_takeover` and `customer_risk` on enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
* Add support for new value `account_takeover` on enum `v2.core.AccountEvaluationCreateParams.signals`
* Add support for new values `business_storage.inbound.czk`, `business_storage.inbound.nok`, `business_storage.inbound.pln`, `business_storage.inbound.sek`, `business_storage.outbound.czk`, `business_storage.outbound.nok`, `business_storage.outbound.pln`, and `business_storage.outbound.sek` on enum `EventsV2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for event notification `V2SignalsAccountSignalCustomerRiskReadyEvent` with related object `v2.signals.AccountSignal`
