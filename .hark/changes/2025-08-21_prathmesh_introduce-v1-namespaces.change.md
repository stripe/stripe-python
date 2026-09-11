---
title: Introduce V1 namespaces in StripeClient
pr_link: https://github.com/stripe/stripe-python/pull/1549
released_in_version: 12.5.0
---

- All the top level non-namespaced services under StripeClient services(eg. customers, products) are copied under the new V1 namespace. These top level non-namespaced services will be marked as deprecated in the next major release and will be removed in a future release. Eg.
```diff
client = StripeClient("sk_test...")

# Accessing V1 Stripe services on a StripeClient should be through the V1 namespace
- client.customers.list()
+ client.v1.customers.list()
```
Refer to the [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for help upgrading.
