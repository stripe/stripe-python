---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1802
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.2.0a3
---

* Add support for `debit_card` on `V2.Core.Account.Configuration.CardCreator.Capability.Consumer.Lead`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Consumer.Lead`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityConsumerLead`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorConsumerLead`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityConsumerLead`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorConsumerLead`
* ⚠️ Add support for new value `consumer.lead.debit_card` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* ⚠️ Add support for new value `consumer.lead.debit_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`
