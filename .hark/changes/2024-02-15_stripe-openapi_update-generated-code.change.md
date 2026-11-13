---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1230
is_stripe_api_change: true
released_in_version: 8.3.0
---

* Add support for `networks` on `Card`, `PaymentMethod.CreateParamsCard`, `PaymentMethod.ModifyParamsCard`, and `Token.CreateParamsCard`
* Add support for new value `no_voec` on enums `Checkout.Session.CustomerDetails.TaxId.type`, `Invoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetails.TaxId.type`, `Tax.Transaction.CustomerDetails.TaxId.type`, and `TaxId.type`
* Add support for new value `no_voec` on enums `Customer.CreateParams.tax_id_data[].type`, `Invoice.UpcomingLinesParams.customer_details.tax_ids[].type`, `Invoice.UpcomingParams.customer_details.tax_ids[].type`,  and `Tax.Calculation.CreateParams.customer_details.tax_ids[].type`
* Add support for new value `financial_connections.account.refreshed_ownership` on enum `Event.type`
* Add support for `display_brand` on `PaymentMethod.card`
* Add support for new value `financial_connections.account.refreshed_ownership` on enums `WebhookEndpoint.CreateParams.enabled_events[]` and `WebhookEndpoint.UpdateParams.enabled_events[]`
