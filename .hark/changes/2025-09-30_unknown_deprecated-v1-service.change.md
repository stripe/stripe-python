---
title: Deprecated the V1 service accessors living directly under StripeClient(e.g. customers, products) as they were copied under the new V1 service in our [last release](https://github.com/stripe/stripe-python/releases/tag/v12.5.0). Service accessors living directly under StripeClient(e.g. customers, products) will be removed from StripeClient in a future release. E.g.
is_breaking: true
released_in_version: 13.0.0
---

```diff
client = StripeClient("sk_test...")

# Accessing V1 Stripe services on a StripeClient should be through the V1 namespace
- client.customers.list()
+ client.v1.customers.list()
```
Refer to the [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for help upgrading.
