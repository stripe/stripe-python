---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1938
semver_level: major
is_stripe_api_change: true
---

* Add support for new resources `PaymentPlan`, `v2.data.QueryRun`, `v2.data.ReportRun`, `v2.data.Report`, and `v2.data.Schema`
* Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentPlan`
* Add support for `list` and `retrieve` methods on resources `v2.data.Report` and `v2.data.Schema`
* Add support for `create` and `retrieve` methods on resources `v2.data.QueryRun` and `v2.data.ReportRun`
* ⚠️ Remove support for `acknowledge_confirmation_of_payee` and `initiate_confirmation_of_payee` methods on resource `v2.core.vault.GbBankAccount`
* Add support for new value `issuing.application_rejected_because_prohibited_business` on enum `AccountNotice.reason`
* Add support for `settlement_currencies` on `BalanceSettings.Payment` and `BalanceSettingsModifyParamsPayment`
* Add support for `default_settlement_currency` on `BalanceSettings.Payment`
* Add support for `wero` on `Charge.PaymentMethodDetail`, `ConfirmationToken.PaymentMethodPreview`, `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.PaymentMethodOption`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodOption`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodOption`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodOption`, `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, `PaymentMethodCreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
* Add support for new value `mandiri` on enums `Charge.PaymentMethodDetail.IdBankTransfer.bank`, `ConfirmationToken.PaymentMethodPreview.IdBankTransfer.bank`, `ConfirmationTokenCreateParamsPaymentMethodDatumIdBankTransfer.bank`, `PaymentAttemptRecord.PaymentMethodDetail.IdBankTransfer.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumIdBankTransfer.bank`, `PaymentIntentCreateParamsPaymentMethodDatumIdBankTransfer.bank`, `PaymentIntentModifyParamsPaymentMethodDatumIdBankTransfer.bank`, `PaymentMethod.IdBankTransfer.bank`, `PaymentMethodCreateParamsIdBankTransfer.bank`, `PaymentRecord.PaymentMethodDetail.IdBankTransfer.bank`, `SetupAttempt.PaymentMethodDetail.IdBankTransfer.bank`, `SetupIntentConfirmParamsPaymentMethodDatumIdBankTransfer.bank`, `SetupIntentCreateParamsPaymentMethodDatumIdBankTransfer.bank`, and `SetupIntentModifyParamsPaymentMethodDatumIdBankTransfer.bank`
* Add support for new values `au_acn`, `au_wpn`, `bw_vat`, `ci_vat`, `cz_dic`, `fr_siren`, `fr_siret`, `fr_spi`, `gh_tin`, `is_kt`, `md_cf`, `mu_vat`, `mz_nuit`, `nz_bn`, `pt_nif`, `sm_coe`, `tt_bir`, and `tt_vat` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Order.TaxDetail.TaxId.type`, and `QuotePreviewInvoice.CustomerTaxId.type`
* Add support for new value `wero` on enums `ConfirmationTokenCreateParamsPaymentMethodDatum.type`, `PaymentIntentConfirmParamsPaymentMethodDatum.type`, `PaymentIntentCreateParamsPaymentMethodDatum.type`, `PaymentIntentModifyParamsPaymentMethodDatum.type`, `SetupIntentConfirmParamsPaymentMethodDatum.type`, `SetupIntentCreateParamsPaymentMethodDatum.type`, and `SetupIntentModifyParamsPaymentMethodDatum.type`
* Add support for `external_token` on `ConfirmationTokenCreateParamsPaymentMethodDatumUsBankAccount`, `PaymentIntentConfirmParamsPaymentMethodDatumUsBankAccount`, `PaymentIntentCreateParamsPaymentMethodDatumUsBankAccount`, `PaymentIntentModifyParamsPaymentMethodDatumUsBankAccount`, `PaymentMethodCreateParamsUsBankAccount`, `SetupIntentConfirmParamsPaymentMethodDatumUsBankAccount`, `SetupIntentCreateParamsPaymentMethodDatumUsBankAccount`, `SetupIntentModifyParamsPaymentMethodDatumUsBankAccount`, and `treasury.OutboundPaymentCreateParamsDestinationPaymentMethodDatumUsBankAccount`
* Add support for new value `wero` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Add support for new value `wero` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* ⚠️ Change type of `Dispute.Evidence.appeal` from `DisputeAppeal` to `nullable(DisputeAppeal)`
* Change `Dispute.EvidenceDetail.submission_method` to be required
* Change `Dispute.intended_submission_method` to be required
* Add support for `payment_plan` on `Invoice`
* Add support for new values `au_acn`, `au_wpn`, `bw_vat`, `ci_vat`, `cz_dic`, `fr_siren`, `fr_siret`, `fr_spi`, `gh_tin`, `is_kt`, `md_cf`, `mu_vat`, `mz_nuit`, `nz_bn`, `pt_nif`, `sm_coe`, `tt_bir`, and `tt_vat` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
* Add support for new value `wero` on enums `PaymentIntent.excluded_payment_method_types`, `PaymentIntentConfirmParams.excluded_payment_method_types`, `PaymentIntentCreateParams.excluded_payment_method_types`, `PaymentIntentModifyParams.excluded_payment_method_types`, `SetupIntent.excluded_payment_method_types`, `SetupIntentCreateParams.excluded_payment_method_types`, and `SetupIntentModifyParams.excluded_payment_method_types`
* Add support for new value `sequra` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Change `QuotePreviewSubscriptionSchedule.pause_schedules` to be required
* ⚠️ Remove support for `default_outbound_destination` on `V2.Core.Account.Configuration.Recipient` and `v2.core.AccountModifyParamsConfigurationRecipient`
* Add support for `crypto_wallets` on `V2.Core.Account.Configuration.Recipient.Capability`, `v2.core.AccountCreateParamsConfigurationRecipientCapability`, and `v2.core.AccountModifyParamsConfigurationRecipientCapability`
* Add support for `ach`, `fedwire`, `fps`, `rtp`, `sepa`, and `swift` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* ⚠️ Remove support for `wire` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* ⚠️ Add support for new value `physical` on enum `V2.Core.Account.Identity.BusinessDetail.AdditionalAddress.purpose`
* Add support for `proof_of_business_presence` on `V2.Core.Account.Identity.BusinessDetail.Document`, `v2.core.AccountCreateParamsIdentityBusinessDetailDocument`, `v2.core.AccountModifyParamsIdentityBusinessDetailDocument`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailDocument`
* Add support for `partial_output_file` on `V2.Core.BatchJob.StatusDetail.BatchFailed`
* Add support for `fingerprint` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod.BankAccount`
* ⚠️ Remove support for values `futsu` and `toza` from enums `V2.Core.Vault.GbBankAccount.bank_account_type` and `v2.core.vault.GbBankAccountCreateParams.bank_account_type`
* Add support for `fedwire_fingerprint` on `V2.Core.Vault.UsBankAccount`
* ⚠️ Remove support for values `balance_exchange` and `inbound_payment` from enum `V2.MoneyManagement.Adjustment.AdjustedFlow.type`
* Add support for `address` on `V2.MoneyManagement.FinancialAddress.BankAccount.Aba`
* ⚠️ Remove support for `account_holder_address` on `V2.MoneyManagement.FinancialAddress.BankAccount.Aba`
* ⚠️ Remove support for `last4` on `V2.MoneyManagement.FinancialAddress.BankAccount.Aba`, `V2.MoneyManagement.FinancialAddress.BankAccount.Iban`, and `V2.MoneyManagement.FinancialAddress.BankAccount.SortCode`
* ⚠️ Remove support for `country` on `V2.MoneyManagement.FinancialAddress.BankAccount.Iban`
* Change `V2.MoneyManagement.FinancialAddress.BankAccount.Aba.account_number` and `V2.MoneyManagement.FinancialAddress.BankAccount.SortCode.account_number` to be required
* Change `V2.MoneyManagement.FinancialAddress.BankAccount.Iban.iban` to be required
* Change `V2.MoneyManagement.FinancialAddress.settlement_currency` to be required
* Add support for `tax_amount` on `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee`
* ⚠️ Remove support for values `becs`, `eft`, `npp`, and `sepa_instant` from enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.NetworkFeeDetail.network`
* Add support for new value `next_day_payout_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
* Add support for `payout_method_options` on `V2.MoneyManagement.OutboundPayment.To`, `V2.MoneyManagement.OutboundPaymentQuote.To`, `V2.MoneyManagement.OutboundTransfer.To`, `v2.money_management.OutboundPaymentCreateParamsTo`, `v2.money_management.OutboundPaymentQuoteCreateParamsTo`, and `v2.money_management.OutboundTransferCreateParamsTo`
* Add support for `payout_intent` and `tracking_details` on `V2.MoneyManagement.OutboundPayment`
* Add support for `recipient_verification` on `V2.MoneyManagement.OutboundPayment` and `v2.money_management.OutboundPaymentCreateParams`
* ⚠️ Change `V2.MoneyManagement.OutboundPayment.To.payout_method` and `V2.MoneyManagement.OutboundSetupIntent.payout_method` to be optional
* Add support for `crypto_wallet` on `V2.MoneyManagement.PayoutMethod` and `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum`
* Add support for `network` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Remove support for `gb_bank_account`, `sepa_bank_account`, and `us_bank_account` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Remove support for `network` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Aba`, `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Iban`, and `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.SortCode`
* Add support for `fee_batch` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* ⚠️ Remove support for `fee_transaction` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* ⚠️ Add support for new value `fee_batch` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* ⚠️ Remove support for value `fee_transaction` from enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for `metadata` and `regulatory_receipt` on `V2.MoneyManagement.Transaction`
* Add support for `contact_email` on `V2.Signals.AccountActivity.AccountDetail.Datum`, `V2.Signals.AccountEvaluation.AccountDetail.Datum`, `v2.signals.AccountActivityCreateParamsAccountDetailData`, and `v2.signals.AccountEvaluationCreateParamsAccountDetailData`
* Add support for new values `fedwire` and `sepa` on enum `v2.money_management.FinancialAddressCreditSimulationCreditParams.network`
* Add support for `statement_descriptor` on `v2.money_management.OutboundPaymentCreateParams` and `v2.money_management.OutboundTransferCreateParams`
* ⚠️ Remove support for `created_gt`, `created_gte`, `created_lt`, and `created_lte` on `v2.money_management.OutboundPaymentListParams`
* ⚠️ Change type of `v2.money_management.OutboundPaymentListParams.created` from `DateTime` to `an object`
* ⚠️ Remove support for `settlement_currency` on `v2.money_management.FinancialAddressCreateParams`
* Add support for new value `eur` on enum `v2.money_management.FinancialAddressCreateParamsBankAccount.currency`
* ⚠️ Remove support for `deposit_insurance_eligibility` on `v2.money_management.FinancialAccountCreateParamsStorage`
* ⚠️ Change type of `v2.core.vault.UsBankAccountListParams.verification_status` from `string` to `enum('awaiting_verification'|'unverified'|'verification_failed'|'verified')`
* Add support for new value `physical` on enums `v2.core.AccountCreateParamsIdentityBusinessDetailAdditionalAddress.purpose`, `v2.core.AccountModifyParamsIdentityBusinessDetailAdditionalAddress.purpose`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailAdditionalAddress.purpose`
* Add support for snapshot events `payment_plan.created`, `payment_plan.installment_due`, `payment_plan.installment_paid`, `payment_plan.installment_will_be_due`, and `payment_plan.updated` with resource `PaymentPlan`
* Add support for event notifications `V2DataQueryRunCreatedEvent`, `V2DataQueryRunFailedEvent`, `V2DataQueryRunSucceededEvent`, and `V2DataQueryRunUpdatedEvent` with related object `v2.data.QueryRun`
* Add support for event notifications `V2DataReportRunCreatedEvent`, `V2DataReportRunFailedEvent`, `V2DataReportRunSucceededEvent`, and `V2DataReportRunUpdatedEvent` with related object `v2.data.ReportRun`
* Add support for error codes `smart_disputes_not_available`, `subscription_update_trial_after_billing_cycle_anchor`, `three_d_secure_authentication_not_supported`, and `three_d_secure_authentication_upstream_error` on `QuotePreviewInvoice.LastFinalizationError`
* ⚠️ Remove support for error code `blocked_payout_method_card` on `BlockedByStripeError`
* Add support for error code `us_bank_account_microdeposits_requires_routing_number` on `CannotProceedError`
* Add support for error codes `gb_bank_account_cannot_be_unarchived` and `us_bank_account_cannot_be_unarchived` on `ControlledByAlternateResourceError`
* ⚠️ Remove support for error code `outbound_flow_from_closed_financial_account_unsupported` on `FeatureNotEnabledError`
* ⚠️ Remove support for error code `invalid_payout_method_card` on `InvalidPayoutMethodError`
* Add support for error code `payout_intent_not_cancelable` on `NotCancelableError`
* ⚠️ Remove support for error code `archived_payout_method_card` on `QuotaExceededError`
