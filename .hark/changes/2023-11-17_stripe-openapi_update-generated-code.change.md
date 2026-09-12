---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1128
is_stripe_api_change: true
released_in_version: 7.6.0b1
---

* Add support for `issuing_card` and `issuing_cards_list` on `AccountSession.CreateParamsComponents`
* Add support for `event_details` and `subscription` on `payment_details` types
* Add support for `affiliate` and `delivery` on `payment_details.flight`, `payment_details.lodging`, and `payment_details.car_rental` types
* Add support for `drivers` on `payment_details.car_rental` types
* Add support for `passengers` on `payment_details.flight` and `payment_details.lodging` types
* Add support for `created` on `CustomerSession`
