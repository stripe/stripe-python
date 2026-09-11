---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1659
is_stripe_api_change: true
released_in_version: 13.2.0a2
---

* Change `delegated_checkout.RequestedSessionModifyParamsLineItemDetail.quantity` to be required
* Add support for `payment_method_preview` on `DelegatedCheckout.RequestedSession`
* Add support for `order_id` on `DelegatedCheckout.RequestedSession.OrderDetail`
* Add support for `lead` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
* Add support for `global_account_holder` on `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
* Add support for new value `commercial.lead.prepaid_card` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new value `commercial.lead.prepaid_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`
