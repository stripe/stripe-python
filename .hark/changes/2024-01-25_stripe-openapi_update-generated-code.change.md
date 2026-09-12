---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1199
is_stripe_api_change: true
released_in_version: 7.14.0
---

* Add support for `annual_revenue` and `estimated_worker_count` on `Account.business_profile`, `Account.CreateParams.business_profile`, and `Account.UpdateParams.business_profile`
* Add support for new value `registered_charity` on enums `Account.CreateParams.company.structure`, `Account.UpdateParams.company.structure`, and `Token.CreateParams.account.company.structure`
* Add support for `collection_options` on `AccountLink.CreateParams`
* Add support for `liability` on `Checkout.Session.automatic_tax`, `PaymentLink.automatic_tax`, `PaymentLink.CreateParams.automatic_tax`, `PaymentLink.UpdateParams.automatic_tax`, `Quote.automatic_tax`, `Quote.CreateParams.automatic_tax`, `Quote.UpdateParams.automatic_tax`, `SubscriptionSchedule.default_settings.automatic_tax`, `SubscriptionSchedule.phases[].automatic_tax`, `SubscriptionSchedule.CreateParams.default_settings.automatic_tax`, `SubscriptionSchedule.CreateParams.phases[].automatic_tax`, `SubscriptionSchedule.UpdateParams.default_settings.automatic_tax`, `SubscriptionSchedule.UpdateParams.phases[].automatic_tax`, and `checkout.Session.CreateParams.automatic_tax`
* Add support for `issuer` on `Checkout.Session.invoice_creation.invoice_data`, `PaymentLink.invoice_creation.invoice_data`, `PaymentLink.CreateParams.invoice_creation.invoice_data`, `PaymentLink.UpdateParams.invoice_creation.invoice_data`, `Quote.invoice_settings`, `Quote.CreateParams.invoice_settings`, `Quote.UpdateParams.invoice_settings`, `SubscriptionSchedule.default_settings.invoice_settings`, `SubscriptionSchedule.phases[].invoice_settings`, `SubscriptionSchedule.CreateParams.default_settings.invoice_settings`, `SubscriptionSchedule.CreateParams.phases[].invoice_settings`, `SubscriptionSchedule.UpdateParams.default_settings.invoice_settings`, `SubscriptionSchedule.UpdateParams.phases[].invoice_settings`, and `checkout.Session.CreateParams.invoice_creation.invoice_data`
* Add support for `invoice_settings` on `PaymentLink.subscription_data`, `PaymentLink.CreateParams.subscription_data`, `PaymentLink.UpdateParams.subscription_data`, and `checkout.Session.CreateParams.subscription_data`
* Add support for new value `challenge` on enums `Invoice.CreateParams.payment_settings.payment_method_options.card.request_three_d_secure`, `Invoice.UpdateParams.payment_settings.payment_method_options.card.request_three_d_secure`, `Subscription.CreateParams.payment_settings.payment_method_options.card.request_three_d_secure`, and `Subscription.UpdateParams.payment_settings.payment_method_options.card.request_three_d_secure`
* Add support for `promotion_code` on `Invoice.UpcomingLinesParams.discounts[]`, `Invoice.UpcomingLinesParams.invoice_items[].discounts[]`, `Invoice.UpcomingParams.discounts[]`, and `Invoice.UpcomingParams.invoice_items[].discounts[]`
* Add support for `account_type` on `PaymentMethod.UpdateParams.us_bank_account`
