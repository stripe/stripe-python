---
title: Pull in V2 FinancialAccount changes for June release
pr_url: https://github.com/stripe/stripe-python/pull/1536
is_stripe_api_change: true
released_in_version: 12.4.0b2
---

* Add support for `close` and `create` methods on resource `v2.money_management.FinancialAccount`
* Add support for new value `storer` on enums `V2.Core.Account.applied_configurations` and `v2.core.Account.CloseParams.applied_configurations`
* Add support for `storer` on `V2.Core.Account.Configuration`, `v2.core.Account.CreateParamsConfiguration`, and `v2.core.Account.ModifyParamsConfiguration`
* Add support for new values `financial_addresses.bank_accounts`, `holds_currencies.gbp`, `inbound_transfers.financial_accounts`, `outbound_payments.bank_accounts`, `outbound_payments.cards`, `outbound_payments.financial_accounts`, `outbound_transfers.bank_accounts`, and `outbound_transfers.financial_accounts` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new value `storer` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
* Add support for `status_details` on `V2.MoneyManagement.FinancialAccount`
* Add support for `status` on `v2.money_management.FinancialAccount.ListParams`
* Add support for new value `configuration.storer` on enums `v2.core.Account.CreateParams.include`, `v2.core.Account.ModifyParams.include`, and `v2.core.Account.RetrieveParams.include`
* Add support for thin events `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
* Add support for error types `AlreadyExistsError` and `NonZeroBalanceError`
