---
title: Omit API keys from pickled StripeObjects
semver_level: major
---
StripeObject pickles no longer preserve API keys. Applications making object-based requests after cache or queue round trips must configure credentials. The new `set_api_key(api_key)` method sets the root and nested StripeObjects API keys in place without changing global configuration. This is a breaking authentication change. See the [v17 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v17.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects).
