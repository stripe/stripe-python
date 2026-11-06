---
title: Omit API keys from pickled StripeObjects
semver_level: major
---
StripeObject pickles no longer preserve API keys. Before making requests through an unpickled object, call `stripe_object.reattach_api_key(api_key)` with a key from secure configuration. This also reattaches API keys to nested objects while preserving their connected accounts and API versions. Until you reattach a key, requests through the object raise `AuthenticationError`, even if you set a global or per-call API key. Calling `reattach_api_key()` more than once, or on an object whose API key wasn't replaced with the serialization placeholder, raises `ValueError`.

See the [v17 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v17.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects)
