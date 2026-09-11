---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1584
is_stripe_api_change: true
released_in_version: 13.1.0b1
---

* Add support for new resources `v2.billing.BillSettingVersion`, `v2.billing.BillSetting`, `v2.billing.Cadence`, `v2.billing.CollectionSettingVersion`, `v2.billing.CollectionSetting`, and `v2.billing.Profile`
* Add support for `create`, `list`, `modify`, and `retrieve` methods on resources `v2.billing.BillSetting`, `v2.billing.CollectionSetting`, and `v2.billing.Profile`
* Add support for `list` and `retrieve` methods on resources `v2.billing.BillSettingVersion` and `v2.billing.CollectionSettingVersion`
* Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.Cadence`
* Add support for new value `crypto_wallet` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `profile` on `V2.Core.Account.Default`, `v2.core.Account.CreateParamsDefault`, and `v2.core.Account.ModifyParamsDefault`
* Add support for `i_p` on `V2.Core.Account.Identity.Attestation.DirectorshipDeclaration`, `V2.Core.Account.Identity.Attestation.OwnershipDeclaration`, `V2.Core.Account.Identity.Attestation.TermsOfService.Account`, `V2.Core.Account.Identity.Attestation.TermsOfService.Storer`, `V2.Core.Account.Identity.Individual.AdditionalTermsOfService.Account`, `V2.Core.Person.AdditionalTermsOfService.Account`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Person.CreateParamsAdditionalTermsOfServiceAccount`, and `v2.core.Person.ModifyParamsAdditionalTermsOfServiceAccount`
* Remove support for `ip` on `V2.Core.Account.Identity.Attestation.DirectorshipDeclaration`, `V2.Core.Account.Identity.Attestation.OwnershipDeclaration`, `V2.Core.Account.Identity.Attestation.TermsOfService.Account`, `V2.Core.Account.Identity.Attestation.TermsOfService.Storer`, `V2.Core.Account.Identity.Individual.AdditionalTermsOfService.Account`, `V2.Core.Person.AdditionalTermsOfService.Account`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Person.CreateParamsAdditionalTermsOfServiceAccount`, and `v2.core.Person.ModifyParamsAdditionalTermsOfServiceAccount`
* Remove support for `doing_business_as`, `product_description`, and `url` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.Account.CreateParamsIdentityBusinessDetail`, and `v2.core.Account.ModifyParamsIdentityBusinessDetail`
* Add support for `settlement_currency` on `V2.MoneyManagement.FinancialAddress`
* Add support for `sepa_bank_account` on `V2.MoneyManagement.FinancialAddress.Credential` and `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* Add support for new value `sepa_bank_account` on enum `V2.MoneyManagement.FinancialAddress.Credential.type`
* Add support for `amount_details` and `payments_orchestration` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPayment.CreateParams`
* Add support for new value `authorization_expired` on enum `V2.Payments.OffSessionPayment.failure_reason`
* Add support for `retry_policy` on `V2.Payments.OffSessionPayment.RetryDetail` and `v2.payments.OffSessionPayment.CreateParamsRetryDetail`
* Add support for new values `heuristic` and `scheduled` on enums `V2.Payments.OffSessionPayment.RetryDetail.retry_strategy` and `v2.payments.OffSessionPayment.CreateParamsRetryDetail.retry_strategy`
* Change type of `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_duration` from `literal('five_minutes')` to `enum('five_minutes'|'none')`
* Change type of `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_expires_at` from `DateTime` to `nullable(DateTime)`
* Add support for new value `none` on enum `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_status`
* Add support for new value `crypto_wallet` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntent.CreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntent.ModifyParamsPayoutMethodDatum.type`
* Add support for `origin_type` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* Remove support for `payment_method_type` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
* Add support for `mandate_data` and `payment_method_options` on `v2.payments.OffSessionPayment.CreateParams`
* Add support for `type` on `v2.money_management.FinancialAddress.CreateParams`
* Remove support for `currency` on `v2.money_management.FinancialAddress.CreateParams`
* Add support for new values `financial_addressses.crypto_wallets`, `holds_currencies.usdc`, `outbound_payments.crypto_wallets`, and `outbound_transfers.crypto_wallets` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for thin event `V2BillingBillSettingUpdatedEvent` with related object `v2.billing.BillSetting`
* Add support for error type `RateLimitError`
* Add support for error code `invalid_payout_method_crypto_wallet` on `InvalidPayoutMethodError`
