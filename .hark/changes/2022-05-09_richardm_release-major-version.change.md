---
title: Release of major version v3.0.0. The [migration guide](https://github.com/stripe/stripe-python/wiki/Migration-Guide-for-v3) contains more information.
pr_link: https://github.com/stripe/stripe-python/pull/809
is_breaking: true
released_in_version: 3.0.0
---

(⚠️ = breaking changes):
* ⚠️ Replace the legacy `Order` API with the new `Order` API.
  * New methods: `cancel`, `list_line_items`, `reopen`, and `submit`
  * Removed methods: `pay` and `return_order`
  * Removed resources: `OrderItem` and `OrderReturn`
* ⚠️ Rename `financial_connections.account.refresh` to `financial_connections.refresh_account`
* Add support for `amount_discount`, `amount_tax`, and `product` on `LineItem`
