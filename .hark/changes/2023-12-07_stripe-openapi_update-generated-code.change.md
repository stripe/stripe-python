---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1155
is_stripe_api_change: true
released_in_version: 7.8.0
---

* Add support for `payment_details`, `payments`, and `payouts` on `AccountSession.components` and `CreateParams.components`
* Add support for `features` on `AccountSession.components.account_onboarding` and `CreateParams.components.account_onboarding`
* Add support for new values `customer_tax_location_invalid` and `financial_connections_no_successful_transaction_refresh` on enums `Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and `StripeError.code`
* Add support for new values `payment_network_reserve_hold` and `payment_network_reserve_release` on enum `BalanceTransaction.type`
* Change `Climate.Product.metric_tons_available` to be required
* Remove support for value `various` from enum `Climate.Supplier.removal_pathway`
* Remove support for values `challenge_only` and `challenge` from enum `PaymentIntent.payment_method_options.card.request_three_d_secure`
* Add support for `inactive_message` and `restrictions` on `CreateParams`, `ModifyParams`, and `PaymentLink`
* Add support for `transfer_group` on `PaymentLink.payment_intent_data`, `CreateParams.payment_intent_data`, and `ModifyParams.payment_intent_data`
* Add support for `trial_settings` on `PaymentLink.subscription_data`, `CreateParams.subscription_data`, and `ModifyParams.subscription_data`
