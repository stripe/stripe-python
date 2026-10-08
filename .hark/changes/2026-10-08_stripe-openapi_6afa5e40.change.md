---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1937
semver_level: major
is_stripe_api_change: true
---

* Add support for new resources `radar.Rule`, `v2.money_management.FundingSession`, and `v2.money_management.InboundTransferMandate`
* Add support for `cancel`, `create`, `list`, and `retrieve` methods on resource `v2.money_management.InboundTransferMandate`
* Add support for `create` method on resource `v2.money_management.FundingSession`
* Add support for `excluded_payout_destinations` on `AccountModifyParamsSettingCapital`
* Add support for `wero_payments` on `Account.Capability`
* ⚠️ Change type of `Charge.Outcome.rule` from `RadarRule` to `$Radar.Rule`
* Add support for new value `ousd` on enums `Charge.PaymentMethodDetail.Crypto.token_currency`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.token_currency`, and `PaymentRecord.PaymentMethodDetail.Crypto.token_currency`
* Add support for `location` and `reader` on `Charge.PaymentMethodDetail.Swish`, `PaymentAttemptRecord.PaymentMethodDetail.Swish`, and `PaymentRecord.PaymentMethodDetail.Swish`
* Add support for `payment_settings` on `Checkout.Session` and `checkout.SessionCreateParams`
* Add support for `on_behalf_of` on `Checkout.Session`
* Add support for new values `fednow` and `rtp` on enum `CustomerCashBalanceTransaction.Funded.BankTransfer.UsBankTransfer.network`
* Add support for `flexible_credential` on `Issuing.Authorization`
* Add support for `fuels` on `Issuing.Transaction.PurchaseDetail`
* Add support for `us_bank_account` on `PaymentAttemptRecordReportFailedParamsPaymentMethodDetail`, `PaymentRecordReportPaymentAttemptFailedParamsPaymentMethodDetail`, `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetail`, `PaymentRecordReportPaymentParamsPaymentMethodDetail`, `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail`, and `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail`
* Change type of `PaymentAttemptRecordReportFailedParamsPaymentMethodDetail.type` and `PaymentRecordReportPaymentAttemptFailedParamsPaymentMethodDetail.type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for `fleet` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
* Add support for `subscription_reference` on `PaymentIntent.PaymentMethodOption.Paypay`, `PaymentIntentConfirmParamsPaymentMethodOptionPaypay`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay`
* Add support for new value `us_bank_account` on enums `PaymentRecordReportPaymentAttemptParamsPaymentMethodDetail.type` and `PaymentRecordReportPaymentParamsPaymentMethodDetail.type`
* Add support for `enablement_details` on `QuotePreviewSubscriptionSchedule.DefaultSetting.AutomaticTax`, `QuotePreviewSubscriptionSchedule.Phase.AutomaticTax`, `Subscription.AutomaticTax`, `SubscriptionSchedule.DefaultSetting.AutomaticTax`, and `SubscriptionSchedule.Phase.AutomaticTax`
* Change type of `radar.PaymentEvaluationCreateParamsPaymentDetailMoneyMovementDetail.money_movement_type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for `rules` on `Radar.PaymentEvaluation`
* ⚠️ Change type of `Radar.PaymentEvaluation.PaymentDetail.MoneyMovementDetail.money_movement_type` from `literal('card')` to `enum('card'|'us_bank_account')`
* Add support for new values `request_three_d_secure` and `reroute` on enum `Radar.PaymentEvaluation.recommended_action`
* Add support for `bank_initiated_return` on `Radar.PaymentEvaluation.Signal`
* Add support for new value `hour` on enums `SharedPayment.GrantedToken.UsageLimit.Recurring.interval`, `SharedPayment.IssuedToken.UsageLimit.Recurring.interval`, `shared_payment.GrantedTokenCreateParamsUsageLimitRecurring.interval`, and `shared_payment.IssuedTokenCreateParamsUsageLimitRecurring.interval`
* Add support for new values `digital_excise_tax` and `utility_users_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
* Add support for `utility_users_tax` on `Tax.Registration.CountryOption.Me`
* Add support for `enable_customer_cancellation` on `terminal.ReaderActivateGiftCardParams`, `terminal.ReaderCashoutGiftCardParams`, `terminal.ReaderCheckGiftCardBalanceParams`, and `terminal.ReaderReloadGiftCardParams`
* Add support for `vipps_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `business_custodial_storage` on `V2.Core.Account.Configuration.MoneyManager.Capability`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapability`, and `v2.core.AccountModifyParamsConfigurationMoneyManagerCapability`
* Add support for `offramp` and `onramp` on `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundPayment`, `V2.Core.Account.Configuration.MoneyManager.Capability.OutboundTransfer`, `V2.Core.Account.Configuration.MoneyManager.Capability.ReceivedCredit`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapabilityOutboundPayment`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapabilityOutboundTransfer`, `v2.core.AccountCreateParamsConfigurationMoneyManagerCapabilityReceivedCredit`, `v2.core.AccountModifyParamsConfigurationMoneyManagerCapabilityOutboundPayment`, `v2.core.AccountModifyParamsConfigurationMoneyManagerCapabilityOutboundTransfer`, and `v2.core.AccountModifyParamsConfigurationMoneyManagerCapabilityReceivedCredit`
* Add support for `pix` on `V2.Core.Account.Configuration.Recipient.Capability`, `V2.MoneyManagement.PayoutMethod`, `v2.core.AccountCreateParamsConfigurationRecipientCapability`, `v2.core.AccountModifyParamsConfigurationRecipientCapability`, and `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum`
* ⚠️ Add support for new value `pix` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for new values `pix` and `vipps_payments` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `account` on `V2.MoneyManagement.FinancialAddress`, `v2.money_management.FinancialAddressCreateParams`, and `v2.money_management.FinancialAddressListParams`
* Add support for new values `bre_b`, `nip`, and `pix` on enum `V2.MoneyManagement.FinancialAddress.BankAccount.type`
* Add support for `supported_network_details` on `V2.MoneyManagement.FinancialAddress.CryptoWallet`
* Add support for new value `bitcoin` on enums `V2.MoneyManagement.FinancialAddress.CryptoWallet.network`, `V2.MoneyManagement.ReceivedCredit.CryptoWalletTransfer.CryptoWallet.network`, and `v2.money_management.FinancialAddressCreateParamsCryptoWallet.network`
* Add support for `network_details` on `V2.MoneyManagement.InboundTransfer` and `v2.money_management.InboundTransferCreateParams`
* Add support for `bacs_debit` on `V2.MoneyManagement.InboundTransfer.From.PaymentMethod`
* Add support for new value `pix` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatum.type`
* Add support for `bic` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.Aba` and `V2.MoneyManagement.ReceivedCredit.BankTransfer.OriginatingBankAccount.SortCode`
* Add support for `originating_crypto_wallet`, `token_currency`, and `transaction_hash` on `V2.MoneyManagement.ReceivedCredit.CryptoWalletTransfer`
* Add support for `invoices` on `V2.Tax.IntegrationConfiguration` and `v2.tax.IntegrationConfigurationModifyParams`
* ⚠️ Remove support for `account` on `v2.risk.InquiryListParams`
* Add support for new values `brl`, `cop`, and `ngn` on enum `v2.money_management.FinancialAddressCreateParamsBankAccount.currency`
* Add support for `customer` and `subscription` on `EventsV1InvoiceUpcomingEvent`
* Add support for new value `vipps_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
* Add support for new values `business_custodial_storage.inbound.ousd`, `business_custodial_storage.inbound.usdc`, `business_custodial_storage.outbound.ousd`, `business_custodial_storage.outbound.usdc`, `outbound_payments.offramp.bank_accounts.brl`, `outbound_payments.offramp.bank_accounts.cop`, `outbound_payments.offramp.bank_accounts.eur`, `outbound_payments.offramp.bank_accounts.gbp`, `outbound_payments.offramp.bank_accounts.mxn`, `outbound_payments.offramp.bank_accounts.usd`, `outbound_payments.onramp.crypto_wallets.brl`, `outbound_payments.onramp.crypto_wallets.cop`, `outbound_payments.onramp.crypto_wallets.eur`, `outbound_payments.onramp.crypto_wallets.gbp`, `outbound_payments.onramp.crypto_wallets.mxn`, `outbound_payments.onramp.crypto_wallets.usd`, `outbound_transfers.offramp.bank_accounts.brl`, `outbound_transfers.offramp.bank_accounts.cop`, `outbound_transfers.offramp.bank_accounts.eur`, `outbound_transfers.offramp.bank_accounts.gbp`, `outbound_transfers.offramp.bank_accounts.mxn`, `outbound_transfers.offramp.bank_accounts.usd`, `outbound_transfers.onramp.crypto_wallets.brl`, `outbound_transfers.onramp.crypto_wallets.cop`, `outbound_transfers.onramp.crypto_wallets.eur`, `outbound_transfers.onramp.crypto_wallets.gbp`, `outbound_transfers.onramp.crypto_wallets.mxn`, `outbound_transfers.onramp.crypto_wallets.usd`, `received_credits.offramp.bank_accounts.brl`, `received_credits.offramp.bank_accounts.cop`, `received_credits.offramp.bank_accounts.eur`, `received_credits.offramp.bank_accounts.gbp`, `received_credits.offramp.bank_accounts.mxn`, `received_credits.offramp.bank_accounts.usd`, `received_credits.onramp.crypto_wallets.brl`, `received_credits.onramp.crypto_wallets.cop`, `received_credits.onramp.crypto_wallets.eur`, `received_credits.onramp.crypto_wallets.gbp`, `received_credits.onramp.crypto_wallets.mxn`, and `received_credits.onramp.crypto_wallets.usd` on enum `EventsV2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent.updated_capability`
* Add support for new value `pix` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
* Add support for event notifications `V2MoneyManagementInboundTransferMandateActivatedEvent`, `V2MoneyManagementInboundTransferMandateCreatedEvent`, `V2MoneyManagementInboundTransferMandateExpiredEvent`, `V2MoneyManagementInboundTransferMandateRefusedEvent`, and `V2MoneyManagementInboundTransferMandateRevokedEvent` with related object `v2.money_management.InboundTransferMandate`
* Add support for error code `service_unavailable` on `ServiceUnavailableError`
