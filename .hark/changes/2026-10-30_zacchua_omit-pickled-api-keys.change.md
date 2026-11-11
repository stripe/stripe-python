---
title: Omit API keys from pickled StripeObjects
semver_level: major
---
StripeObject pickles no longer preserve API keys. Before making requests through an unpickled object, call `reattach_api_key(api_key)`. This also reattaches API keys to nested objects.

See the [v17 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v17.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects) for details.
