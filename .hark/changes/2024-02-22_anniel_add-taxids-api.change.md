---
title: Add TaxIds API
pr_url: https://github.com/stripe/stripe-python/pull/1244
released_in_version: 8.4.0
---

* Add support for `create`, `retrieve`, `delete`, and `list` methods on resource `TaxId`
* The `instance_url` function on resource `TaxId` now returns the top-level `/v1/tax_ids/{id}` path instead of the `/v1/customers/{customer}/tax_ids/{id}` path.
