---
title: Support for APIs in the new API version 2024-09-30.acacia
pr_url: https://github.com/stripe/stripe-python/pull/1404
is_stripe_api_change: true
released_in_version: 11.0.0
---

This release changes the pinned API version to `2024-09-30.acacia`. Please read the [API Changelog](https://docs.stripe.com/changelog/acacia#2024-09-30.acacia) and carefully review the API changes before upgrading.

### ⚠️ Breaking changes due to changes in the API


* Rename for `usage_threshold_config` to `usage_threshold` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`
* Remove support for `filter` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`. Use the filters on the `usage_threshold` instead
* * Remove support for `customer_consent_collected` on parameter class `stripe.terminal.Reader.ProcessSetupIntentParams`

### ⚠️ Other Breaking changes in the SDK
* Adjusted default values for HTTP requests. You can use the old defaults by setting them explicitly. New values are:
  - max retries: `0` -> `2`
  - max timeout (seconds): `2` -> `5`

### Additions

* Add support for `custom_unit_amount` on parameter class `stripe.Product.CreateParamsDefaultPriceData`
* Add support for `usage_threshold` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`
* Add support for `allow_redisplay` on parameter classes `stripe.terminal.Reader.ProcessPaymentIntentParamsProcessConfig` and `stripe.terminal.Reader.ProcessSetupIntentParams`
* Add support for `international_transaction` on enum `stripe.treasury.ReceivedCredit.failure_code`
* Add support for `2024-09-30.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
* Add support for new Usage Billing APIs `stripe.v2.billing.MeterEvent`, `stripe.v2.billing.MeterEventAdjustments`, `stripe.v2.billing.MeterEventSession`, `stripe.v2.billing.MeterEventStream` and the new Events API `stripe.v2.core.Events` under the [v2 namespace ](https://docs.corp.stripe.com/api-v2-overview)
* Add method [rawRequest()](https://github.com/stripe/stripe-python/tree/master?tab=readme-ov-file#custom-requests) on the `StripeClient` class that takes a HTTP method type, url and relevant parameters to make requests to the Stripe API that are not yet supported in the SDK.
* Add method `parse_thin_event()` on the `StripeClient` class to parse [thin events](https://docs.corp.stripe.com/event-destinations#events-overview)

### Other changes
* Change type of `default_allowed_updates` on  `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` from `Union[Literal[''], List[Literal['price', 'promotion_code', 'quantity']]]` to `NotRequired[Literal['']|List[Literal['price', 'promotion_code', 'quantity']]]`
* Change type of `products` on  `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` from `Union[Literal[''], List[Configuration.CreateParamsFeaturesSubscriptionUpdateProduct]]` to `NotRequired[Literal['']|List[Configuration.CreateParamsFeaturesSubscriptionUpdateProduct]]`
