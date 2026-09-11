---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1649
is_stripe_api_change: true
released_in_version: 13.1.0a4
---

* Add support for new resource `v2.billing.PricingPlanSubscriptionComponents`
* Add support for `retrieve` method on resource `v2.billing.PricingPlanSubscriptionComponents`
* Add support for `dimension_payload_keys` on `Billing.Meter` and `billing.MeterCreateParams`
* Add support for `dimension_filters` and `dimension_group_by_keys` on `billing.BillingMeterListMeterEventSummaryParams`
* Add support for `dimensions` on `Billing.MeterEventSummary`
* Add support for `fulfillment_details` and `payment_method_data` on `delegated_checkout.RequestedSessionCreateParams` and `delegated_checkout.RequestedSessionModifyParams`
* Add support for `line_item_details`, `metadata`, `payment_method`, and `shared_metadata` on `DelegatedCheckout.RequestedSession`, `delegated_checkout.RequestedSessionCreateParams`, and `delegated_checkout.RequestedSessionModifyParams`
* Add support for `currency`, `customer`, and `risk_details` on `delegated_checkout.RequestedSessionCreateParams`
* Add support for `seller_details` and `setup_future_usage` on `DelegatedCheckout.RequestedSession` and `delegated_checkout.RequestedSessionCreateParams`
* Add support for `amount_subtotal`, `amount_total`, `created_at`, `expires_at`, `order_details`, `shared_payment_issued_token`, `status`, `total_details`, and `updated_at` on `DelegatedCheckout.RequestedSession`
* Add support for `address`, `email`, `fulfillment_options`, `name`, `phone`, and `selected_fulfillment_option` on `DelegatedCheckout.RequestedSession.FulfillmentDetail`
* Add support for new values `billie`, `crypto`, `kr_card`, `kriya`, `mb_way`, `mondu`, `ng_bank_transfer`, `ng_bank`, `ng_card`, `ng_market`, `ng_ussd`, `ng_wallet`, `payco`, `paypay`, `rechnung`, `samsung_pay`, `satispay`, `scalapay`, `sequra`, `sunbit`, `us_bank_account`, and `vipps` on enums `EventsV2CoreHealthAuthorizationRateDropFiringEvent.Impact.payment_method_type`, `EventsV2CoreHealthAuthorizationRateDropResolvedEvent.Impact.payment_method_type`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact.payment_method_type`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact.payment_method_type`
