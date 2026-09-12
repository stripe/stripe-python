---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/947
is_stripe_api_change: true
released_in_version: 5.3.0
---

* Add support for new resources `Tax.CalculationLineItem`, `Tax.Calculation`, `Tax.TransactionLineItem`, and `Tax.Transaction`
* Add support for `create` and `list_line_items` methods on resource `Calculation`
* Add support for `create_from_calculation`, `create_reversal`, `create`, `list_line_items`, and `retrieve` methods on resource `Transaction`
