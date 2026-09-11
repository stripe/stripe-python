---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1629
is_stripe_api_change: true
released_in_version: 13.1.0a2
---

* Add support for new resource `PaymentMethodBalance`
* Add support for `check_balance` method on resource `PaymentMethod`
* Add support for `benefits` on `Card`, `Charge.PaymentMethodDetail.Card`, `ConfirmationToken.PaymentMethodPreview.Card`, and `PaymentMethod.Card`
* Add support for `benefit` on `PaymentIntent.PaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
* Add support for `setup_details` on `SetupIntentConfirmParams`, `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
* Add support for new value `card_creator` on enums `V2.Core.Account.applied_configurations` and `v2.core.AccountCloseParams.applied_configurations`
* Add support for `card_creator` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`
* Add support for new values `commercial.celtic.charge_card`, `commercial.celtic.spend_card`, `commercial.cross_river_bank.charge_card`, `commercial.cross_river_bank.spend_card`, `commercial.stripe.charge_card`, and `commercial.stripe.prepaid_card` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new value `card_creator` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
* Add support for new value `configuration.card_creator` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* Add support for thin events `V2CoreAccountIncludingConfigurationCardCreatorCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationCardCreatorUpdatedEvent` with related object `v2.core.Account`
* Remove support for thin events `V1CustomerDiscountCreatedEvent`, `V1CustomerDiscountDeletedEvent`, and `V1CustomerDiscountUpdatedEvent` with related object `Discount`
