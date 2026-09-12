---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1833
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.4.0a1
---

* Add support for new resources `v2.billing.ContractPricingLineQuantityChange`, `v2.core.health.AlertHistoryEntry`, `v2.core.health.Alert`, `v2.money_management.FinancialAddressDebitSimulation`, and `v2.money_management.PayoutIntent`
* ⚠️ Remove support for resource `v2.billing.ContractLicensePricingQuantityChange`
* Add support for `report_offer_acceptance` method on resource `issuing.CreditUnderwritingRecord`
* Add support for `provisional_credit` test helper method on resource `issuing.Dispute`
* Add support for `report_early_fraud_warning` method on resource `PaymentAttemptRecord`
* Add support for `search` method on resource `PaymentRecord`
* Add support for `debit` method on resource `v2.money_management.FinancialAddressDebitSimulation`
* Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.money_management.PayoutIntent`
* Add support for `list` and `retrieve` methods on resource `v2.core.health.Alert`
* Add support for `delete` method on resource `v2.billing.Contract`
* ⚠️ Remove support for `performance_location_details` on `Tax.TransactionLineItem`
* Add support for `financial_accounts_transactions`, `financial_accounts`, and `recipients_list` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.GiftCard`, `GiftCardOperation`, `PaymentAttemptRecord.PaymentMethodDetail.GiftCard`, and `PaymentRecord.PaymentMethodDetail.GiftCard`
* Add support for `subscription` on `checkout.SessionCreateParamsItem`
* Add support for `items` on `Checkout.Session`
* Add support for `brand` on `Checkout.Session.CurrentAttempt.PaymentMethodDetail.Card`
* Add support for `network_data` on `issuing.AuthorizationCaptureParams` and `issuing.TransactionCreateForceCaptureParams`
* Add support for `enriched_merchant_data` on `Issuing.Authorization`
* Add support for `available_balance` and `current_balance` on `Issuing.Authorization.BalanceResponse`
* ⚠️ Remove support for `amount` on `Issuing.Authorization.BalanceResponse`
* Add support for `decision_deadline_updated_at` on `Issuing.CreditUnderwritingRecord`
* Add support for `acquirer_reference_number` on `Issuing.Transaction.NetworkDatum`
* Change `PaymentAttemptRecordReportRefundParams.outcome` and `PaymentRecordReportRefundParams.outcome` to be optional
* Add support for `tip` on `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentDecrementAuthorizationParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
* ⚠️ Remove support for values `billing.alert.recovered` and `payment_intent.expired` from enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for `billing_cycle_anchor` on `V2.Billing.Contract` and `v2.billing.ContractCreateParams`
* ⚠️ Remove support for `contract_line_details`, `contract_value_details`, and `license_quantities` on `V2.Billing.Contract`
* Add support for `bill_settings_details` on `V2.Billing.Contract.BillingSetting` and `v2.billing.ContractCreateParamsBillingSetting`
* Add support for `billing_profile_details` and `collection_settings_details` on `V2.Billing.Contract.BillingSetting`
* ⚠️ Remove support for `contract_billing_details` on `V2.Billing.Contract.BillingSetting` and `v2.billing.ContractCreateParamsBillingSetting`
* ⚠️ Change type of `V2.Billing.Contract.one_time_fees` from `array(an object)` to `an object`
* ⚠️ Change type of `V2.Billing.Contract.pricing_lines` from `array(an object)` to `an object`
* ⚠️ Change type of `V2.Billing.Contract.pricing_overrides` from `array(an object)` to `an object`
* ⚠️ Change `V2.Billing.Contract.pricing_lines` to be optional
* ⚠️ Change `V2.Billing.Contract.pricing_overrides` to be optional
* Add support for `mode` on `V2.Commerce.ProductCatalogImport`
* Add support for new value `money_manager` on enums `EventsV2CoreAccountLinkReturnedEvent.configurations`, `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`, `v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding.configurations`, and `v2.core.AccountLinkCreateParamsUseCaseAccountUpdate.configurations`
* ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
* ⚠️ Remove support for value `storer` from enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
* Add support for `money_manager` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `storer` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* Add support for `sunbit_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `ach`, `becs`, `eft`, `fedwire`, `fps`, `npp`, `rtp`, `sepa_credit`, `sepa_instant`, and `swift` on `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* Add support for new values `bank_accounts.ach`, `bank_accounts.becs`, `bank_accounts.eft`, `bank_accounts.fedwire`, `bank_accounts.fps`, `bank_accounts.npp`, `bank_accounts.rtp`, `bank_accounts.sepa_credit`, `bank_accounts.sepa_instant`, `bank_accounts.swift`, `business_storage.inbound.eur`, `business_storage.inbound.gbp`, `business_storage.inbound.usd`, `business_storage.outbound.eur`, `business_storage.outbound.gbp`, `business_storage.outbound.usd`, `consumer_storage.inbound.usd`, `consumer_storage.outbound.usd`, `received_credits.bank_accounts`, and `received_debits.bank_accounts` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new value `money_manager` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.configuration` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
* Add support for `consumer_money_manager` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* Add support for `crypto_money_manager` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `consumer_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `crypto_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `maximum_rps` on `V2.Core.BatchJob` and `v2.core.BatchJobCreateParams`
* Add support for `bic` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* ⚠️ Remove support for `swift_code` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* Add support for `attachment` on `V2.MoneyManagement.OutboundPayment.DeliveryOption.PaperCheck` and `v2.money_management.OutboundPaymentCreateParamsDeliveryOptionPaperCheck`
* Add support for `processing` on `V2.MoneyManagement.OutboundPayment.StatusDetail` and `V2.MoneyManagement.OutboundTransfer.StatusDetail`
* Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* Add support for `payout_method_options` on `V2.MoneyManagement.OutboundPayment.To`, `V2.MoneyManagement.OutboundTransfer.To`, `v2.money_management.OutboundPaymentCreateParamsTo`, and `v2.money_management.OutboundTransferCreateParamsTo`
* Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
* Add support for `account_holder_name` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount`
* Add support for `returned` on `V2.MoneyManagement.ReceivedDebit.StatusDetail`
* Add support for new value `capability_inactive` on enum `V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason`
* Add support for `returned_at` on `V2.MoneyManagement.ReceivedDebit.StatusTransition`
* Add support for `payout_intent` on `v2.money_management.OutboundPaymentCreateParams`
* Add support for `statuses` on `v2.money_management.FinancialAccountListParams`
* ⚠️ Remove support for `status` on `v2.money_management.FinancialAccountListParams`
* Change `v2.core.BatchJobCreateParams.metadata` to be optional
* ⚠️ Add support for new value `configuration.money_manager` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* ⚠️ Remove support for value `configuration.storer` from enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* Add support for `include` on `v2.billing.ContractListParams`
* ⚠️ Remove support for `contract_lines` on `v2.billing.ContractCreateParams`
* ⚠️ Remove support for `license_quantity_actions` on `v2.billing.ContractCreateParams` and `v2.billing.ContractModifyParams`
* ⚠️ Add support for `billing_profile_details` and `collection_settings_details` on `v2.billing.ContractCreateParamsBillingSetting`
* ⚠️ Add support for new value `billing_settings` on enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
* ⚠️ Remove support for values `contract_line_details` and `license_quantities` from enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
* ⚠️ Add support for `amount`, `bill_at`, and `product` on `v2.billing.ContractCreateParamsOneTimeFee`
* Add support for `lookup_key` on `v2.billing.ContractCreateParamsOneTimeFee`
* ⚠️ Remove support for `bill_schedule`, `billable_item_type`, and `product_details` on `v2.billing.ContractCreateParamsOneTimeFee`
* Add support for `pricing_overrides` and `quantity_changes` on `v2.billing.ContractCreateParamsPricingLinePricingPriceDetail` and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetail`
* ⚠️ Remove support for `quantity` on `v2.billing.ContractCreateParamsPricingLinePricingPriceDetail` and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetail`
* ⚠️ Remove support for `overwrite_price` on `v2.billing.ContractCreateParamsPricingOverride`
* Add support for `pricing_line_ids` and `pricing_line_lookup_keys` on `v2.billing.ContractCreateParamsPricingOverrideMultiplierCriterion` and `v2.billing.ContractModifyParamsPricingOverrideActionAddMultiplierCriterion`
* ⚠️ Remove support for `billable_item_ids`, `billable_item_lookup_keys`, `billable_item_types`, `metadata_conditions`, and `rate_card_ids` on `v2.billing.ContractCreateParamsPricingOverrideMultiplierCriterion` and `v2.billing.ContractModifyParamsPricingOverrideActionAddMultiplierCriterion`
* ⚠️ Change type of `v2.billing.ContractCreateParamsPricingOverride.type` and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.type` from `enum('multiplier'|'overwrite_price')` to `literal('multiplier')`
* Change `v2.billing.ContractCreateParams.pricing_overrides` to be optional
* Change `v2.billing.ContractCreateParamsPricingOverrideMultiplier.criteria` to be optional
* Add support for `pricing` on `v2.billing.ContractModifyParamsPricingLineActionUpdate`
* ⚠️ Remove support for `price` on `v2.billing.ContractModifyParamsPricingOverrideActionAddOverwritePrice`
* Add support for `cancel_pricing_lines` and `proration_behavior` on `v2.billing.ContractCancelParams`
* Add support for new value `sunbit_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
* Add support for new values `bank_accounts.ach`, `bank_accounts.becs`, `bank_accounts.eft`, `bank_accounts.fedwire`, `bank_accounts.fps`, `bank_accounts.npp`, `bank_accounts.rtp`, `bank_accounts.sepa_credit`, `bank_accounts.sepa_instant`, and `bank_accounts.swift` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
* Add support for event notifications `V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEvent` with related object `v2.core.Account`
* Add support for event notifications `V2MoneyManagementDebitDisputeFailedEvent`, `V2MoneyManagementDebitDisputeSubmittedEvent`, and `V2MoneyManagementDebitDisputeSucceededEvent` with related object `v2.money_management.DebitDispute`
* Add support for event notification `V2MoneyManagementOutboundPaymentUnderReviewEvent` with related object `v2.money_management.OutboundPayment`
* Add support for event notification `V2MoneyManagementOutboundTransferUnderReviewEvent` with related object `v2.money_management.OutboundTransfer`
* ⚠️ Remove support for event notifications `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
* Add support for error codes `us_bank_account_microdeposits_cannot_be_confirmed` and `us_bank_account_microdeposits_cannot_be_sent` on `ControlledByAlternateResourceError`
* Add support for error code `payout_intent_not_cancelable` on `NotCancelableError`
