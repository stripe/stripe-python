---
title: Fixed InvoiceLineItem method definition
pr_url: https://github.com/stripe/stripe-python/pull/1604
is_breaking: true
released_in_version: 13.0.0
---

* ⚠️ `InvoiceLineItem.modify` and `InvoiceLineItem.modify_async` now require `invoice` and `line_item_id` as method parameters.
  * Removed `InvoiceLineItem.ModifyParam` class. Use a `typing.dict` to type hint instead.
