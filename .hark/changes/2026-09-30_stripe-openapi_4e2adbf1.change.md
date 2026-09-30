---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1892
semver_level: major
is_stripe_api_change: true
---

* Add support for new resources `radar.BillingEvaluation`, `v2.money_management.FinancialAddressCreditSimulation`, and `v2.money_management.FinancialAddressGeneratedMicrodeposits`
* ⚠️ Remove support for resources `v2.FinancialAddressCreditSimulation` and `v2.FinancialAddressGeneratedMicrodeposits`
* Add support for `create` method on resource `radar.BillingEvaluation`
* Add support for `list` method on resource `reserve.Plan`
* Add support for `credit` method on resource `v2.money_management.FinancialAddressCreditSimulation`
* Add support for `generate_microdeposits` method on resource `v2.money_management.FinancialAddressGeneratedMicrodeposits`
* ⚠️ Remove support for `credit` method on resource `v2.FinancialAddressCreditSimulation`
* ⚠️ Remove support for `generate_microdeposits` method on resource `v2.FinancialAddressGeneratedMicrodeposits`
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
* Add support for new values `final_payment_failure` and `first_payment_failure` on enum `Subscription.StatusDetail.Paused.Subscription.type`
* Change `Subscription.TrialSetting.EndBehavior.billing_cycle_anchor` to be required
* Add support for new value `igic` on enums `Tax.Registration.CountryOption.E.type` and `tax.RegistrationCreateParamsCountryOptionE.type`
* Change `TaxCode.requirements` to be required
* ⚠️ Remove support for `configurations` on `V2.Core.AccountLink.UseCase.AccountOnboarding`, `V2.Core.AccountLink.UseCase.AccountUpdate`, `v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding`, and `v2.core.AccountLinkCreateParamsUseCaseAccountUpdate`
* ⚠️ Add support for new value `rejected` on enums `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Aud.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Cad.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Eur.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Gbp.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Usd.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Aud.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Cad.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Eur.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Gbp.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Usd.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.InboundTransfer.BankAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.BankAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.Card.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.FinancialAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundTransfer.BankAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundTransfer.FinancialAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.ReceivedCredit.BankAccount.status`, `V2.Core.Account.Configuration.MoneyManager.Capability.ReceivedDebit.BankAccount.status`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Local.status`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Wire.status`, and `V2.Core.Account.Configuration.Recipient.Capability.Card.status`
* ⚠️ Add support for new values `rejected_fraud`, `rejected_incomplete_verification`, `rejected_listed`, `rejected_other`, `rejected_platform_fraud`, `rejected_platform_other`, `rejected_platform_terms_of_service`, and `rejected_terms_of_service` on enums `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Aud.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Cad.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Eur.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Gbp.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Inbound.Usd.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Aud.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Cad.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Eur.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Gbp.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.BusinessStorage.Outbound.Usd.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.InboundTransfer.BankAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.BankAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.Card.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment.FinancialAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundTransfer.BankAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundTransfer.FinancialAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.ReceivedCredit.BankAccount.StatusDetail.code`, `V2.Core.Account.Configuration.MoneyManager.Capability.ReceivedDebit.BankAccount.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Local.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Wire.StatusDetail.code`, and `V2.Core.Account.Configuration.Recipient.Capability.Card.StatusDetail.code`
* Add support for `related_object` and `request` on `V2.Iam.ActivityLog`
* ⚠️ Add support for new value `stripe_action` on enum `V2.Iam.ActivityLog.Actor.type`
* Add support for `account_security`, `authentication`, `scim`, `sso`, and `user_profile` on `V2.Iam.ActivityLog.Detail`
* Add support for new values `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, and `user_profile` on enum `V2.Iam.ActivityLog.Detail.type`
* Add support for new values `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, and `user_two_step_authentication_reset_requested` on enum `V2.Iam.ActivityLog.type`
* Add support for `deposit_insurance_eligibility` on `V2.MoneyManagement.FinancialAccount.Storage` and `v2.money_management.FinancialAccountCreateParamsStorage`
* Add support for `bank_account` on `V2.MoneyManagement.FinancialAddress` and `v2.money_management.FinancialAddressCreateParams`
* Add support for `type` on `V2.MoneyManagement.FinancialAddress`
* ⚠️ Remove support for `credentials` and `currency` on `V2.MoneyManagement.FinancialAddress`
* ⚠️ Remove support for `level` on `V2.MoneyManagement.InboundTransfer.TransferHistory`
* Add support for `network_fee_details` on `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee`
* Add support for new value `network_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
* Add support for `archived` on `V2.MoneyManagement.PayoutMethod`
* ⚠️ Remove support for `archived` on `V2.MoneyManagement.PayoutMethod.BankAccount` and `V2.MoneyManagement.PayoutMethod.Card`
* ⚠️ Add support for new value `ineligible` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.payments`
* ⚠️ Add support for new value `ineligible` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.transfers`
* Add support for `amount_received` on `V2.MoneyManagement.ReceivedCredit`
* Add support for `originating_bank_account` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* ⚠️ Remove support for `origin_type` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* Add support for `identity` on `V2.Signals.AccountActivity.AccountDetail.Datum`, `V2.Signals.AccountEvaluation.AccountDetail.Datum`, `v2.signals.AccountActivityCreateParamsAccountDetailData`, and `v2.signals.AccountEvaluationCreateParamsAccountDetailData`
* Add support for `fraudulent_website` on `V2.Signals.AccountEvaluation.EvaluatedSignal` and `V2.Signals.AccountSignal`
* Add support for new value `fraudulent_website` on enum `V2.Signals.AccountEvaluation.pending_signals`
* Add support for new value `fraudulent_website` on enums `V2.Signals.AccountEvaluation.requested_signals` and `v2.signals.AccountEvaluationCreateParams.requested_signals`
* Add support for `fraudulent_merchant` on `V2.Signals.AccountSignal`
* Add support for new values `fraudulent_merchant` and `fraudulent_website` on enums `V2.Signals.AccountSignal.type` and `v2.signals.AccountSignalListParams.type`
* ⚠️ Remove support for `created_gt`, `created_gte`, `created_lt`, and `created_lte` on `v2.money_management.AdjustmentListParams`, `v2.money_management.InboundTransferListParams`, `v2.money_management.ReceivedCreditListParams`, `v2.money_management.TransactionEntryListParams`, and `v2.money_management.TransactionListParams`
* ⚠️ Change type of `v2.money_management.AdjustmentListParams.created`, `v2.money_management.InboundTransferListParams.created`, `v2.money_management.ReceivedCreditListParams.created`, `v2.money_management.TransactionEntryListParams.created`, and `v2.money_management.TransactionListParams.created` from `DateTime` to `an object`
* Add support for new value `ineligible` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.payments`
* Add support for new value `ineligible` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.transfers`
* ⚠️ Remove support for `include` on `v2.money_management.FinancialAddressListParams` and `v2.money_management.FinancialAddressRetrieveParams`
* Add support for `settlement_currency` on `v2.money_management.FinancialAddressCreateParams`
* ⚠️ Add support for new value `bank_account` on enum `v2.money_management.FinancialAddressCreateParams.type`
* ⚠️ Remove support for values `gb_bank_account` and `us_bank_account` from enum `v2.money_management.FinancialAddressCreateParams.type`
* Add support for `include` on `v2.money_management.FinancialAccountListParams` and `v2.money_management.FinancialAccountRetrieveParams`
* Add support for new values `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, and `user_profile` on enum `v2.iam.ActivityLogListParams.action_groups`
* Add support for new values `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, and `user_two_step_authentication_reset_requested` on enum `v2.iam.ActivityLogListParams.actions`
* Add support for `treasury_transaction` on `EventsV2MoneyManagementTransactionUpdatedEvent`
* Add support for event notifications `V2SignalsAccountSignalFraudulentMerchantReadyEvent` and `V2SignalsAccountSignalFraudulentWebsiteReadyEvent` with related object `v2.signals.AccountSignal`
* Add support for error types `InvalidVaultedCredentialError`, `VerificationAttemptFailedError`, `VerificationExpiredError`, and `VerificationNotInitiatedError`
* ⚠️ Remove support for error type `ControlledByDashboardError`
* Add support for error codes `dispute_evidence_page_limit_exceeded`, `financial_connections_consent_locale_invalid`, `financial_connections_consent_locale_unsupported`, and `payment_evaluation_on_api_version_not_supported` on `QuotePreviewInvoice.LastFinalizationError`
* Add support for error codes `blocked_gb_bank_account`, `unsupported_gb_bank`, and `unsupported_us_bank` on `BlockedByStripeError`
* ⚠️ Remove support for error codes `blocked_payout_method_bank_account`, `blocked_payout_method_crypto_wallet`, `unsupported_payout_method_bank_account`, and `unsupported_payout_method_crypto_wallet` on `BlockedByStripeError`
* Add support for error codes `default_gb_bank_account_cannot_be_archived`, `gb_bank_account_incompatible_currency`, `gb_bank_account_unsupported_currency`, `incompatible_payout_method_currency`, `unsupported_payout_method_currency`, `us_bank_account_incompatible_currency`, and `us_bank_account_unsupported_currency` on `CannotProceedError`
* Add support for error codes `gb_bank_account_cannot_be_archived` and `us_bank_account_cannot_be_archived` on `ControlledByAlternateResourceError`
* ⚠️ Remove support for error codes `invalid_payout_method_bank_account` and `invalid_payout_method_crypto_wallet` on `InvalidPayoutMethodError`
* Add support for error code `limit_gb_bank_account` on `QuotaExceededError`
* ⚠️ Remove support for error codes `limit_payout_method_bank_account`, `limit_payout_method_card`, and `limit_payout_method_crypto_wallet` on `QuotaExceededError`
