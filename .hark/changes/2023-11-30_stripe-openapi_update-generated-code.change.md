---
title: Update generated code
pr_link: https://github.com/stripe/stripe-python/pull/1147
is_stripe_api_change: true
released_in_version: 7.7.0
---

* Add support for new resources `Climate.Order`, `Climate.Product`, and `Climate.Supplier`
* Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `Order`
* Add support for `list` and `retrieve` methods on resources `Product` and `Supplier`
* Add support for new value `financial_connections_account_inactive` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `SetupAttempt.SetupError.code`, and `SetupIntent.LastSetupError.code`
* Add support for new values `climate_order_purchase` and `climate_order_refund` on enum `BalanceTransaction.type`
* Add support for `created` on `Checkout.Session.ListParams`
* Add support for `validate_location` on `Customer.CreateParamsTax` and `Customer.ModifyParamsTax`
* Add support for new values `climate.order.canceled`, `climate.order.created`, `climate.order.delayed`, `climate.order.delivered`, `climate.order.product_substituted`, `climate.product.created`, and `climate.product.pricing_updated` on enum `Event.type`
* Add support for new value `challenge` on enums `PaymentIntent. PaymentMethodOptions.Card.request_three_d_secure` and `SetupIntent. PaymentMethodOptions.Card.request_three_d_secure`
* Add support for new values `climate_order_purchase` and `climate_order_refund` on enum `Reporting.ReportRun. CreateParamsParameters.reporting_category`
* Add support for new values `climate.order.canceled`, `climate.order.created`, `climate.order.delayed`, `climate.order.delivered`, `climate.order.product_substituted`, `climate.product.created`, and `climate.product.pricing_updated` on enums `WebhookEndpoint.CreateParams.enabled_events[]` and `WebhookEndpoint.ModifyParams.enabled_events[]`
