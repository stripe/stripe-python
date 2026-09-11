---
title: Port **async support** from beta to the stable channel. To use it, add an `_async` suffix to any request-making method.
pr_link: https://github.com/stripe/stripe-python/pull/1288
released_in_version: 8.10.0
---

```diff
- cus = stripe.Customer.create(...)
+ cus = await stripe.Customer.create_async(...)
```

See the [README](./README.md#async) for detailed usage instructions. Support is provided out of the box for async requests via the HTTPX (used by default) and aiohttp libraries. For other libraries, you can also provide your own `stripe.HTTPClient` implementation. Please do not hesitate to [open a Github issue](https://github.com/stripe/stripe-python/issues/new/choose) if you have any feedback on this feature.
