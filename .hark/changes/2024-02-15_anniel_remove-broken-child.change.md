---
title: Remove broken child methods
pr_url: https://github.com/stripe/stripe-python/pull/1237
released_in_version: 8.3.0
---

* Bugfix: remove support for `CreditNoteLineItem.list`, `CustomerCashBalanceTransaction.list`, and `CustomerCashBalanceTransaction.retrieve`. These methods were included in the library unintentionally and never functioned.
