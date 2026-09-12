---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1750
is_breaking: true
is_stripe_api_change: true
released_in_version: 14.5.0a3
---

* Add support for new resource `radar.IssuingAuthorizationEvaluation`
* Add support for `create` method on resource `radar.IssuingAuthorizationEvaluation`
* Add support for new value `fee_credits` on enum `BalanceTransaction.balance_type`
* ⚠️ Rename `affiliate_attributions` to `affiliate_attribution` on `delegated_checkout.RequestedSessionConfirmParams` and `delegated_checkout.RequestedSessionCreateParams`
* Add support for `amount_to_counter` on `Dispute`
* Add support for `frozen_fields` on `InvoiceItem`
* Add support for new value `next_billing_period_start` on enums `V2.Billing.IntentAction.Apply.EffectiveAt.type` and `v2.billing.IntentCreateParamsActionApplyEffectiveAt.type`
* Add support for `consumer` on `V2.Core.Account.Configuration.CardCreator.Capability`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapability`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreator`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapability`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreator`
* Add support for `fifth_third` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercial`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercial`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercial`
* Add support for `prepaid_card` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank`, `V2.Core.Account.Identity.Attestation.TermsOfService.CardCreator.Commercial.CrossRiverBank`, `v2.core.AccountCreateParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBank`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfServiceCardCreatorCommercialCrossRiverBank`, `v2.core.AccountModifyParamsConfigurationCardCreatorCapabilityCommercialCrossRiverBank`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfServiceCardCreatorCommercialCrossRiverBank`
* Add support for new values `commercial.cross_river_bank.prepaid_card`, `commercial.fifth_third.charge_card`, `consumer.celtic.revolving_credit_card`, `consumer.cross_river_bank.prepaid_card`, and `consumer.lead.prepaid_card` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `payment_method_data` on `v2.payments.OffSessionPaymentCreateParams`
* Change `v2.payments.OffSessionPaymentCreateParams.payment_method` to be optional
* Add support for new values `commercial.cross_river_bank.prepaid_card`, `commercial.fifth_third.charge_card`, `consumer.celtic.revolving_credit_card`, `consumer.cross_river_bank.prepaid_card`, and `consumer.lead.prepaid_card` on enum `EventsV2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent.updated_capability`
