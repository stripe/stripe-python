---
title: Add decimal_string coercion for v1 and v2 API fields
pr_url: https://github.com/stripe/stripe-python/pull/1769
is_breaking: true
released_in_version: 15.0.0
---

- All `decimal_string` fields changed type from `str` to `decimal.Decimal` in both request params and response objects. Code that reads or writes these fields as `str` will need to use `Decimal` instead. Affected fields across v1 and v2 APIs:
  - **checkout.Session**: `fx_rate`
  - **climate.Order**: `metric_tons`; **climate.Product**: `metric_tons_available`
  - **CreditNoteLineItem**: `unit_amount_decimal`
  - **InvoiceItem**: `quantity_decimal`, `unit_amount_decimal`
  - **InvoiceLineItem**: `quantity_decimal`, `unit_amount_decimal`
  - **issuing.Authorization** / **issuing.Transaction** (and TestHelpers): `quantity_decimal`, `unit_cost_decimal`, `gross_amount_decimal`, `local_amount_decimal`, `national_amount_decimal`
  - **Plan**: `amount_decimal`, `flat_amount_decimal`, `unit_amount_decimal`
  - **Price**: `unit_amount_decimal`, `flat_amount_decimal` (including `currency_options` and `tiers`)
  - **v2.core.Account** / **v2.core.AccountPerson**: `percent_ownership`
  - Request params on **Invoice**, **Product**, **Quote**, **Subscription**, **SubscriptionItem**, **SubscriptionSchedule**, **PaymentLink**: `unit_amount_decimal`, `flat_amount_decimal`, `quantity_decimal` (where applicable)
