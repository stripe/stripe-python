---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1489
is_stripe_api_change: true
released_in_version: 12.1.0b2
---

### Breaking changes
* Change type of `V2MoneyManagementReceivedDebit.status_transitions` from `an object` to `nullable(an object)`
* Remove support for values `bank_accounts.local_uk`, `bank_accounts.wire_uk`, `cards_uk`, and `crypto_wallets_v2` from enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`

### Additions
* Add support for new resources `Privacy.RedactionJobRootObjects`, `Privacy.RedactionJobValidationError`, and `Privacy.RedactionJob`
* Add support for `cancel`, `create`, `list`, `modify`, `retrieve`, `run`, and `validate` methods on resource `RedactionJob`
* Add support for `list` and `retrieve` methods on resource `RedactionJobValidationError`
* Add support for `minority_owned_business_designation` on `Account.BusinessProfile`, `Account.CreateParamsBusinessProfile`, and `Account.UpdateParamsBusinessProfile`
* Add support for new value `verification_legal_entity_structure_mismatch` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `AccountCapability.FutureRequirement.Error.code`, `AccountCapability.Requirement.Error.code`, `AccountPerson.FutureRequirement.Error.code`, `AccountPerson.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, and `BankAccount.Requirement.Error.code`
* Add support for `export_tax_transactions` and `payment_disputes` on `AccountSession.CreateParamsComponent`
* Add support for new value `tax_id_prohibited` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `QuotePreviewInvoice.LastFinalizationError.code`, `SetupAttempt.SetupError.code`, `SetupIntent.LastSetupError.code`, and `StripeError.code`
* Add support for new value `fixed_term_loan` on enum `CapitalFinancingOffer.type`
* Add support for `wallet_options` on `CheckoutSession` and `checkout.Session.CreateParams`
* Add support for new values `privacy.redaction_job.canceled`, `privacy.redaction_job.created`, `privacy.redaction_job.ready`, `privacy.redaction_job.succeeded`, and `privacy.redaction_job.validation_error` on enum `Event.type`
* Add support for `klarna` on `PaymentMethodDomain`
* Change type of `TaxCalculationLineItem.reference` from `nullable(string)` to `string`
* Add support for `in` on `TaxRegistration.CountryOption` and `tax.Registration.CreateParamsCountryOption`
* Add support for new values `privacy.redaction_job.canceled`, `privacy.redaction_job.created`, `privacy.redaction_job.ready`, `privacy.redaction_job.succeeded`, and `privacy.redaction_job.validation_error` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.UpdateParams.enabled_events`
