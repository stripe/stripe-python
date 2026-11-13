---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1336
is_stripe_api_change: true
released_in_version: 9.9.0
---

* Add support for `generated_from` on resource classes `stripe.ConfirmationToken.PaymentMethodPreview.Card` and `stripe.PaymentMethod.Card`
* Add support for `default_value` on parameter classes `stripe.checkout.Session.CreateParamsCustomFieldDropdown`, `stripe.checkout.Session.CreateParamsCustomFieldNumeric`, and `stripe.checkout.Session.CreateParamsCustomFieldText` and resource classes `stripe.checkout.Session.CustomField.Dropdown`, `stripe.checkout.Session.CustomField.Numeric`, and `stripe.checkout.Session.CustomField.Text`
* Add support for `verification_requires_additional_proof_of_registration` on enums `stripe.Account.FutureRequirements.Error.code`, `stripe.Account.Requirements.Error.code`, `stripe.BankAccount.FutureRequirements.Error.code`, `stripe.BankAccount.Requirements.Error.code`, `stripe.Capability.FutureRequirements.Error.code`, `stripe.Capability.Requirements.Error.code`, `stripe.Person.FutureRequirements.Error.code`, and `stripe.Person.Requirements.Error.code`
* Add support for `issuing_personalization_design.activated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_personalization_design.deactivated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_personalization_design.rejected` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `issuing_personalization_design.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
* Add support for `en-RO` on enums `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna.preferred_locale`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsKlarna.preferred_locale`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna.preferred_locale`
* Add support for `ro-RO` on enums `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna.preferred_locale`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsKlarna.preferred_locale`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna.preferred_locale`
* Change type of `features` on  `stripe.issuing.PhysicalBundle` from `Optional[Features]` to `Features`
