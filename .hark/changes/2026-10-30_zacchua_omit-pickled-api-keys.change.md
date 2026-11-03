---
title: Omit API keys from pickled StripeObjects
semver_level: major
---
StripeObject pickles no longer preserve API keys. Applications making object-based requests after cache or queue round trips must supply credentials, either through global configuration or per call, e.g. `customer.refresh(api_key=api_key)`. `refresh()`, `refresh_async()`, `save()`, and `auto_paging_iter()` on list and search result objects now accept an `api_key` keyword argument for this. See the [v17 migration guide](https://github.com/stripe/stripe-python/blob/master/.hark/migration-guides/v17.md#api-keys-are-no-longer-preserved-in-pickled-stripeobjects).
