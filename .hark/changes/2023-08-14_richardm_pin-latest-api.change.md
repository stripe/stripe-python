---
title: Pin to the latest API version
pr_url: https://github.com/stripe/stripe-python/pull/987
is_breaking: true
released_in_version: 6.0.0
---

In this release, Stripe API Version `2023-08-16` (the latest at time of release) will be sent by default on all requests.
The previous default was to use your [Stripe account's default API version](https://stripe.com/docs/development/dashboard/request-logs#view-your-default-api-version).

To successfully upgrade to stripe-python v6, you must either

1. **(Recommended) Upgrade your integration to be compatible with API Version `2023-08-16`.**

   Please read the API Changelog carefully for each API Version from `2023-08-16` back to your [Stripe account's default API version](https://stripe.com/docs/development/dashboard/request-logs#view-your-default-api-version). Determine if you are using any of the APIs that have changed in a breaking way, and adjust your integration accordingly. Carefully test your changes with Stripe [Test Mode](https://stripe.com/docs/keys#test-live-modes) before deploying them to production.

   You can read the [v6 migration guide](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v6) for more detailed instructions.

2. **(Alternative option) Specify a version other than `2023-08-16` when initializing `stripe-python`.**

   If you were previously initializing stripe-python without an explicit API Version, you can postpone modifying your integration by specifying a version equal to your [Stripe account's default API version](https://stripe.com/docs/development/dashboard/request-logs#view-your-default-api-version). For example:

   ```diff
     import stripe
     stripe.api_key = "sk_test_..."
   + stripe.api_version = '2020-08-27'
   ```

   If you were already initializing stripe-python with an explicit API Version, upgrading to v6 will not affect your integration.

   Read the [v6 migration guide](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v6) for more details.

Going forward, each major release of this library will be *pinned* by default to the latest Stripe API Version at the time of release.

That is, instead of upgrading stripe-python and separately upgrading your Stripe API Version through the Stripe Dashboard, whenever you upgrade major versions of stripe-python, you should also upgrade your integration to be compatible with the latest Stripe API version.
