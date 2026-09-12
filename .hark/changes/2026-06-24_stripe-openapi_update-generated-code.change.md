---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1819
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.4.0b1
---

* Add support for `redaction` on `Card`, `Charge`, `Checkout.Session`, `Customer`, `Issuing.Authorization`, `Issuing.Card`, `Issuing.Cardholder`, `Issuing.Dispute`, `Issuing.Transaction`, `PaymentIntent`, `PaymentMethod`, `SetupIntent`, `Source`, and `Token`
* Add support for `disclaimer_variant` on `Capital.FinancingOffer` and `Capital.FinancingSummary.Detail`
* Add support for `active` on `FinancialConnections.Account.StatusDetail` and `FinancialConnections.Authorization.StatusDetail`
* ⚠️ Add support for new value `institution_requirement` on enum `FinancialConnections.Account.StatusDetail.Inactive.cause`
* Change type of `financial_connections.SessionCreateParamsLimit.accounts` from `longInteger` to `emptyable(longInteger)`
* Add support for `pause` on `InvoiceCreatePreviewParamsSubscriptionDetail`
* ⚠️ Add support for new value `satispay` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Add support for `release_details` on `Reserve.Hold`
* Add support for `buyer_id` on `SharedPayment.GrantedToken.PaymentMethodDetail.Bizum` and `SharedPayment.GrantedToken.PaymentMethodDetail.Blik`
* Add support for `fingerprint` on `SharedPayment.GrantedToken.PaymentMethodDetail.Pix`
* ⚠️ Remove support for value `invoice_payment.detached` from enum `WebhookEndpointModifyParams.enabled_events`
* ⚠️ Add support for new value `money_manager` on enums `EventsV2CoreAccountLinkReturnedEvent.configurations`, `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, and `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`
* ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
* ⚠️ Remove support for value `storer` from enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
* Add support for `money_manager` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* ⚠️ Remove support for `storer` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
* ⚠️ Add support for new values `business_storage.inbound.eur`, `business_storage.inbound.gbp`, `business_storage.inbound.usd`, `business_storage.outbound.eur`, `business_storage.outbound.gbp`, `business_storage.outbound.usd`, `received_credits.bank_accounts`, and `received_debits.bank_accounts` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.configuration` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
* ⚠️ Remove support for `maximum_rps` on `V2.Core.BatchJob` and `v2.core.BatchJobCreateParams`
* Add support for `bic` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* ⚠️ Remove support for `swift_code` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* Add support for `processing` on `V2.MoneyManagement.OutboundPayment.StatusDetail` and `V2.MoneyManagement.OutboundTransfer.StatusDetail`
* ⚠️ Add support for new values `fx_rate_drift_exceeded_after_review`, `payout_method_amount_limit_exceeded`, and `review_rejected` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
* ⚠️ Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
* Add support for `account_holder_name` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount`
* ⚠️ Add support for new value `capability_inactive` on enum `V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason`
* Add support for `statuses` on `v2.money_management.FinancialAccountListParams`
* ⚠️ Remove support for `status` on `v2.money_management.FinancialAccountListParams`
* Change `v2.core.BatchJobCreateParams.metadata` to be optional
* Add support for new value `money_manager` on enums `v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding.configurations` and `v2.core.AccountLinkCreateParamsUseCaseAccountUpdate.configurations`
* ⚠️ Add support for new value `configuration.money_manager` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* ⚠️ Remove support for value `configuration.storer` from enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* Add support for event notifications `V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEvent` with related object `v2.core.Account`
* Add support for event notification `V2MoneyManagementOutboundPaymentUnderReviewEvent` with related object `v2.money_management.OutboundPayment`
* Add support for event notification `V2MoneyManagementOutboundTransferUnderReviewEvent` with related object `v2.money_management.OutboundTransfer`
* ⚠️ Remove support for event notifications `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
* Add support for error codes `anomalous_money_movement_request`, `failed_tax_calculation`, `financial_account_balance_does_not_support_currency`, `financial_account_capability_not_enabled`, and `financial_account_capability_restricted` on `QuotePreviewInvoice.LastFinalizationError`
* Add support for error code `default_us_bank_account_cannot_be_archived` on `CannotProceedError`
