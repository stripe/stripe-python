---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1624
is_stripe_api_change: true
released_in_version: 13.2.0b1
---

* Add support for `modify` method on resource `v2.money_management.FinancialAccount`
* Add support for `confirm_microdeposits`, `list`, and `send_microdeposits` methods on resource `v2.core.vault.UsBankAccount`
* Add support for `list` method on resource `v2.core.vault.GbBankAccount`
* Add support for new value `verification_data_not_found` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
* Add support for `payment_portal_url` on `Charge.PaymentMethodDetail.Rechnung`, `PaymentAttemptRecord.PaymentMethodDetail.Rechnung`, and `PaymentRecord.PaymentMethodDetail.Rechnung`
* Add support for `tax_id_element` on `CustomerSession.Component` and `CustomerSessionCreateParamsComponent`
* Add support for `starting_after` on `PaymentAttemptRecordListParams`
* Add support for new value `solana` on enums `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network` and `PaymentRecord.PaymentMethodDetail.Crypto.network`
* Add support for `reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionKlarna`
* Change `PaymentIntent.PaymentDetail.customer_reference` to be required
* Change `PaymentIntent.PaymentDetail.order_reference` to be required
* Add support for `subscription_reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`
* Add support for `closed` on `V2.Core.Account` and `v2.core.AccountListParams`
* Add support for new value `payment_method` on enums `V2.Core.Account.Configuration.Customer.AutomaticIndirectTax.location_source`, `v2.core.AccountCreateParamsConfigurationCustomerAutomaticIndirectTax.location_source`, and `v2.core.AccountModifyParamsConfigurationCustomerAutomaticIndirectTax.location_source`
* Add support for `usd` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
* Add support for new values `application_custom` and `application_express` on enums `V2.Core.Account.Default.Responsibility.fees_collector`, `v2.core.AccountCreateParamsDefaultResponsibility.fees_collector`, and `v2.core.AccountModifyParamsDefaultResponsibility.fees_collector`
* Add support for `representative_declaration` on `V2.Core.Account.Identity.Attestation`, `v2.core.AccountCreateParamsIdentityAttestation`, and `v2.core.AccountModifyParamsIdentityAttestation`
* Add support for new value `holds_currencies.usd` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `verification` on `V2.Core.Vault.UsBankAccount`
* Add support for `v1_id` on `EventsV2MoneyManagementTransactionCreatedEvent`
* Remove support for thin event `V2BillingBillSettingUpdatedEvent` with related object `v2.billing.BillSetting`
* Add support for error code `payment_intent_rate_limit_exceeded` on `QuotePreviewInvoice.LastFinalizationError`
* Add support for error codes `blocked_payout_method_crypto_wallet` and `unsupported_payout_method_crypto_wallet` on `BlockedByStripeError`
* Add support for error code `outbound_flow_from_closed_financial_account_unsupported` on `FeatureNotEnabledError`
* Add support for error code `limit_payout_method_crypto_wallet` on `QuotaExceededError`
