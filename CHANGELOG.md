# Changelog

## 8.4.0b1 - 2024-02-16
* [#1235](https://github.com/stripe/stripe-python/pull/1235) Update generated code for beta
  * Add support for `payto` and `twint` payment methods throughout the API
  * Add support for `decrement_authorization` method on resource `PaymentIntent`
* [#1236](https://github.com/stripe/stripe-python/pull/1236) Beta: StripeStreamResponseAsync.read helper
* [#1233](https://github.com/stripe/stripe-python/pull/1233) Beta: async streaming

## 8.3.0 - 2024-02-15
* [#1230](https://github.com/stripe/stripe-python/pull/1230) Update generated code
  * Add support for `networks` on `Card`, `PaymentMethod.CreateParamsCard`, `PaymentMethod.ModifyParamsCard`, and `Token.CreateParamsCard`
  * Add support for new value `no_voec` on enums `Checkout.Session.CustomerDetails.TaxId.type`, `Invoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetails.TaxId.type`, `Tax.Transaction.CustomerDetails.TaxId.type`, and `TaxId.type`
  * Add support for new value `no_voec` on enums `Customer.CreateParams.tax_id_data[].type`, `Invoice.UpcomingLinesParams.customer_details.tax_ids[].type`, `Invoice.UpcomingParams.customer_details.tax_ids[].type`,  and `Tax.Calculation.CreateParams.customer_details.tax_ids[].type`
  * Add support for new value `financial_connections.account.refreshed_ownership` on enum `Event.type`
  * Add support for `display_brand` on `PaymentMethod.card`
  * Add support for new value `financial_connections.account.refreshed_ownership` on enums `WebhookEndpoint.CreateParams.enabled_events[]` and `WebhookEndpoint.UpdateParams.enabled_events[]`
* [#1237](https://github.com/stripe/stripe-python/pull/1237) Remove broken child methods
  * Bugfix: remove support for `CreditNoteLineItem.list`, `CustomerCashBalanceTransaction.list`, and `CustomerCashBalanceTransaction.retrieve`. These methods were included in the library unintentionally and never functioned.
* [#1232](https://github.com/stripe/stripe-python/pull/1232) Improve types in _http_client.py

## 8.3.0b1 - 2024-02-08
* [#1226](https://github.com/stripe/stripe-python/pull/1226) Update generated code for beta
  * Add support for `payment_method_options` on `ConfirmationToken`
* [#1228](https://github.com/stripe/stripe-python/pull/1228) Beta: add `_async` methods for StripeClient

## 8.2.0 - 2024-02-08
* [#1225](https://github.com/stripe/stripe-python/pull/1225) Update generated code
  * Add support for `invoices` on `Account.Settings`
  * Add support for new value `velobank` on various enums `PaymentMethodDetails.P24.bank`
  * Add support for `setup_future_usage` on `PaymentMethodOptions.Blik`
  * Add support for `require_cvc_recollection` on `PaymentMethodOptions.Card`
  * Add support for `account_tax_ids` on various `InvoiceSettings` request parameters
* [#1223](https://github.com/stripe/stripe-python/pull/1223) Move StripeClient usage collection onto StripeService
* [#1220](https://github.com/stripe/stripe-python/pull/1220) Measure StripeClient usage

## 8.2.0b1 - 2024-02-05
* [#1218](https://github.com/stripe/stripe-python/pull/1218) Update generated code for beta
  * Add support for new resources `Entitlements.Event` and `Entitlements.Feature`
  * Add support for `create` method on resource `Event`
  * Add support for `create` and `list` methods on resource `Feature`
* [#1171](https://github.com/stripe/stripe-python/pull/1171) Beta: codegenned async methods on resources
* [#1219](https://github.com/stripe/stripe-python/pull/1219) Beta: more async infrastructure
* [#1210](https://github.com/stripe/stripe-python/pull/1210) Beta: better support for trio in HTTPClientAsync
    * Fixes support for `trio` on HttpClientAsync.
* [#1209](https://github.com/stripe/stripe-python/pull/1209) Beta: Fix HTTPXClient retries

## 8.1.0 - 2024-02-01
* [#1213](https://github.com/stripe/stripe-python/pull/1213) Update generated code
  * Add support for `swish` payment method throughout the API
  * Add support for `relationship` on parameter classes `Account.CreateParamsIndividual` and `Token.CreateParamsAccountIndividual`
  * Add support for `jurisdiction_level` on resource `TaxRate`
  * Change type from `str` to `Literal["offline", "online"]` of `status` on field `terminal.Reader`

## 8.1.0b1 - 2024-01-25
* [#1198](https://github.com/stripe/stripe-python/pull/1198) Update generated code for beta
  * Add support for `create_preview` method on resource `Invoice`
* [#1211](https://github.com/stripe/stripe-python/pull/1211) Merge master into beta

## 8.0.0 - 2024-01-25
* [#1206](https://github.com/stripe/stripe-python/pull/1206) stripe-python v8 release
  This release introduces `StripeClient` and a service-based call pattern. This new interface allows you to easily call Stripe APIs and has several benefits over the existing resource-based pattern:

  * No global config: you can simultaneously use multiple clients with different configuration options (such as API keys)
  * No static methods for easier mocking

  For full migration instructions, please refer to the [v8 migration guide](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v8-(StripeClient)).

  "⚠️" symbol highlights breaking changes

  ### ⚠️ Changed
  * ⚠️ **Request options like `api_key`, `stripe_account`, `stripe_version`, and `idempotency_key` can no longer be passed in positionally on resource methods. Please pass these in as keyword arguments.**

  **BEFORE**
  ```python
  stripe.Customer.create(
    "sk_test_123",  # api key
    "KG5LxwFBepaKHyUD",  # idempotency key
    "2022-11-15",  # stripe version
    "acct_123",  # stripe account
  )
  ```

  **AFTER**
  ```python
  stripe.Customer.create(
    api_key="sk_test_123",
    idempotency_key="KG5LxwFBepaKHyUD",
    stripe_version="2022-11-15",
    stripe_account="acct_123",
  )
  ```
  * ⚠️ Methods that turn a response stream (`Quote.pdf`) now returns a single value of type `StripeResponseStream` instead of a tuple containing `(StripeResponseStream, api_key)`.
  * ⚠️ Removed public access to `APIRequestor`. `APIRequestor`'s main use is internal, and we don't have a good understanding of its external use cases. We had to make several breaking changes to its interface as part of this update, so rather than leaving it public we made it private. If you have a use case for `APIRequestor`, please open up a Github issue describing it. We'd rather you rely on something specifically designed for your use case than having to reach into the library's internals.


  ### ⚠️ Removed
  * ⚠️ Remove `api_version` from `File.create` parameters. Please use `stripe_version` instead.
  * ⚠️ Remove `util.read_special_variable()` utility method (importing directly from `stripe.util` is deprecated as of [v7.8.0](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#780---2023-12-07))
  * ⚠️ Remove `StripeError.construct_error_object()`. This method was intended for internal stripe-python use only.
  * ⚠️ Remove `ListObject.empty_list()`. This method was intended for internal stripe-python use only.
  * ⚠️ Remove `SearchResultObject.empty_search_result()`. This method was intended for internal stripe-python use only.
  * ⚠️ Remove `StripeObject.ReprJSONEncoder`. This class was intended for internal stripe-python use only.
  * ⚠️ Remove `StripeObject.api_base`. This property was defunct and returned `None`.

## 7.14.0 - 2024-01-25
* [#1199](https://github.com/stripe/stripe-python/pull/1199) Update generated code
  * Add support for `annual_revenue` and `estimated_worker_count` on `Account.business_profile`, `Account.CreateParams.business_profile`, and `Account.UpdateParams.business_profile`
  * Add support for new value `registered_charity` on enums `Account.CreateParams.company.structure`, `Account.UpdateParams.company.structure`, and `Token.CreateParams.account.company.structure`
  * Add support for `collection_options` on `AccountLink.CreateParams`
  * Add support for `liability` on `Checkout.Session.automatic_tax`, `PaymentLink.automatic_tax`, `PaymentLink.CreateParams.automatic_tax`, `PaymentLink.UpdateParams.automatic_tax`, `Quote.automatic_tax`, `Quote.CreateParams.automatic_tax`, `Quote.UpdateParams.automatic_tax`, `SubscriptionSchedule.default_settings.automatic_tax`, `SubscriptionSchedule.phases[].automatic_tax`, `SubscriptionSchedule.CreateParams.default_settings.automatic_tax`, `SubscriptionSchedule.CreateParams.phases[].automatic_tax`, `SubscriptionSchedule.UpdateParams.default_settings.automatic_tax`, `SubscriptionSchedule.UpdateParams.phases[].automatic_tax`, and `checkout.Session.CreateParams.automatic_tax`
  * Add support for `issuer` on `Checkout.Session.invoice_creation.invoice_data`, `PaymentLink.invoice_creation.invoice_data`, `PaymentLink.CreateParams.invoice_creation.invoice_data`, `PaymentLink.UpdateParams.invoice_creation.invoice_data`, `Quote.invoice_settings`, `Quote.CreateParams.invoice_settings`, `Quote.UpdateParams.invoice_settings`, `SubscriptionSchedule.default_settings.invoice_settings`, `SubscriptionSchedule.phases[].invoice_settings`, `SubscriptionSchedule.CreateParams.default_settings.invoice_settings`, `SubscriptionSchedule.CreateParams.phases[].invoice_settings`, `SubscriptionSchedule.UpdateParams.default_settings.invoice_settings`, `SubscriptionSchedule.UpdateParams.phases[].invoice_settings`, and `checkout.Session.CreateParams.invoice_creation.invoice_data`
  * Add support for `invoice_settings` on `PaymentLink.subscription_data`, `PaymentLink.CreateParams.subscription_data`, `PaymentLink.UpdateParams.subscription_data`, and `checkout.Session.CreateParams.subscription_data`
  * Add support for new value `challenge` on enums `Invoice.CreateParams.payment_settings.payment_method_options.card.request_three_d_secure`, `Invoice.UpdateParams.payment_settings.payment_method_options.card.request_three_d_secure`, `Subscription.CreateParams.payment_settings.payment_method_options.card.request_three_d_secure`, and `Subscription.UpdateParams.payment_settings.payment_method_options.card.request_three_d_secure`
  * Add support for `promotion_code` on `Invoice.UpcomingLinesParams.discounts[]`, `Invoice.UpcomingLinesParams.invoice_items[].discounts[]`, `Invoice.UpcomingParams.discounts[]`, and `Invoice.UpcomingParams.invoice_items[].discounts[]`
  * Add support for `account_type` on `PaymentMethod.UpdateParams.us_bank_account`

## 7.14.0b1 - 2024-01-18
* [#1197](https://github.com/stripe/stripe-python/pull/1197) Update generated code for beta
  Release specs are identical.
* [#1192](https://github.com/stripe/stripe-python/pull/1192) Update generated code for beta
  * Add support for new value `nn` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bank`
  * Add support for new value `NNBANL2G` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bic`
  * Change `Invoice.AutomaticTax.liability`, `Invoice.issuer`, and `Subscription.AutomaticTax.liability` to be required

## 7.13.0 - 2024-01-18
* [#1193](https://github.com/stripe/stripe-python/pull/1193) Update generated code
  * Add support for providing details about `BankAccount`, `Card`, and `CardToken` on `Account.CreateExternalAccountParams.external_account` and `Account.CreateParams.external_account`
  * Add support for new value `nn` on enums `Charge.PaymentMethodDetails.Ideal.bank`, `PaymentIntent.ConfirmParamsPaymentMethodDataIdeal.bank`, `PaymentIntent.CreateParamsPaymenMethodDataIdeal.bank`, `PaymentIntent.UpdateParamsPaymentMethodDataIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethod.CreateParamsIdeal.bank`, `SetupAttempt.PaymentMethodDetails.Ideal.bank`, `SetupIntent.ConfirmParamsPaymenMethodDataIdeal.bank`, `SetupIntent.CreateParamsPaymenMethodDataIdeal.bank`, and `SetupIntent.UpdateParamsPaymenMethodDataIdeal.bank`
  * Add support for new value `NNBANL2G` on enums `Charge.PaymentMethodDetails.Ideal.bic`, `PaymentMethod.Ideal.bic`, and `SetupAttempt.PaymentMethodDetails.Ideal.bic`
  * Change `CustomerSession.Components.buy_button` and `CustomerSession.Components.pricing_table` to be required
  * Add support for `issuer` on `Invoice.CreateParams`, `Invoice.UpcomingLinesParams`, `Invoice.UpcomingParams`, `Invoice.UpdateParams`, and `Invoice`
  * Add support for `liability` on `Invoice.automatic_tax`, `Invoice.CreateParams.automatic_tax`, `Invoice.UpcomingLinesParams.automatic_tax`, `Invoice.UpcomingParams.automatic_tax`, `Invoice.UpdateParams.automatic_tax`, `Subscription.automatic_tax`, `Subscription.CreateParams.automatic_tax`, and `Subscription.UpdateParams.automatic_tax`
  * Add support for `on_behalf_of` on `Invoice.UpcomingLinesParams` and `Invoice.UpcomingParams`
  * Add support for `pin` on `issuing.Card.CreateParams`
  * Add support for `revocation_reason` on `Mandate.PaymentMethodDetails.bacs_debit`
  * Add support for `customer_balance` on `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, and `PaymentMethodConfiguration`
  * Add support for `invoice_settings` on `Subscription.CreateParams` and `Subscription.UpdateParams`

## 7.13.0b1 - 2024-01-12
* [#1189](https://github.com/stripe/stripe-python/pull/1189) Update generated code for beta
* [#1191](https://github.com/stripe/stripe-python/pull/1191) Beta: report `raw_request` usage
* [#1165](https://github.com/stripe/stripe-python/pull/1165) Beta: raw_request_async with HTTPX

## 7.12.0 - 2024-01-12
* [#1188](https://github.com/stripe/stripe-python/pull/1188) Update generated code
  * Add support for new resource `CustomerSession`
  * Add support for `create` method on resource `CustomerSession`
  * Remove support for values `obligation_inbound`, `obligation_payout_failure`, `obligation_payout`, and `obligation_reversal_outbound` from enum `BalanceTransaction.type`
  * Add support for new values `eps` and `p24` on enums `Invoice.payment_settings.payment_method_types[]`, `InvoiceCreateParams.payment_settings.payment_method_types[]`, `InvoiceUpdateParams.payment_settings.payment_method_types[]`, `Subscription.payment_settings.payment_method_types[]`, `SubscriptionCreateParams.payment_settings.payment_method_types[]`, and `SubscriptionUpdateParams.payment_settings.payment_method_types[]`
  * Remove support for value `obligation` from enum `Reporting.ReportRunCreateParams.parameters.reporting_category`
  * Add support for `billing_cycle_anchor_config` on `SubscriptionCreateParams` and `Subscription`

## 7.12.0b1 - 2024-01-04
* [#1187](https://github.com/stripe/stripe-python/pull/1187) Update generated code for beta
  * Updated stable APIs to the latest version

## 7.11.0 - 2024-01-04
* [#1186](https://github.com/stripe/stripe-python/pull/1186) Update generated code
  * Add support for `retrieve` on resource `tax.Registration`
  * Change type from `Optional[PaymentDetails]` to `PaymentDetails` of `payment_details` on field `AccountSession.Components`
  * Change type from `Optional[Payments]` to `Payments` of `payments` on field `AccountSession.Components`
  * Change type from `Optional[Payouts]` to `Payouts` of `payouts` on field `AccountSession.Components`
  * Change type from `Optional[Features]` to `Features` of `features` on fields `AccountSession.Components.PaymentDetails`, `AccountSession.Components.Payments`, and `AccountSession.Components.Payouts`
  * Change type from `Optional[InvoiceSettings]` to `InvoiceSettings` of `invoice_settings` on field `SubscriptionSchedule.DefaultSettings`

## 7.11.0b1 - 2023-12-22
* [#1177](https://github.com/stripe/stripe-python/pull/1177) Update generated code for beta

## 7.10.0 - 2023-12-22
* [#1176](https://github.com/stripe/stripe-python/pull/1176) Update generated code
  * Add support for new resource `FinancialConnections.Transaction`
  * Add support for `list` and `retrieve` methods on resource `Transaction`
  * Add support for `subscribe` and `unsubscribe` methods on resource `FinancialConnections.Account`
  * Add support for `features` on `AccountSessionCreateParams.components.payouts`
  * Add support for `edit_payout_schedule`, `instant_payouts`, and `standard_payouts` on `AccountSession.components.payouts.features`
  * Change type of `Checkout.Session.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `Checkout.SessionCreateParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `Invoice.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `InvoiceCreateParams.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `InvoiceUpdateParams.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `PaymentIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `PaymentIntentConfirmParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `PaymentIntentCreateParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `PaymentIntentUpdateParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `SetupIntent.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `SetupIntentConfirmParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `SetupIntentCreateParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `SetupIntentUpdateParams.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `Subscription.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`, `SubscriptionCreateParams.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]`, and `SubscriptionUpdateParams.payment_settings.payment_method_options.us_bank_account.financial_connections.prefetch[]` from `literal('balances')` to `enum('balances'|'transactions')`
  * Add support for new value `financial_connections.account.refreshed_transactions` on enum `Event.type`
  * Add support for new value `transactions` on enum `FinancialConnections.AccountRefreshParams.features[]`
  * Add support for `subscriptions` and `transaction_refresh` on `FinancialConnections.Account`
  * Add support for `next_refresh_available_at` on `FinancialConnections.Account.balance_refresh`
  * Add support for new value `transactions` on enums `FinancialConnections.Session.prefetch[]` and `FinancialConnections.SessionCreateParams.prefetch[]`
  * Add support for new value `unknown` on enums `Issuing.Authorization.verification_data.authentication_exemption.type` and `Issuing.AuthorizationCreateParams.testHelpers.verification_data.authentication_exemption.type`
  * Add support for new value `challenge` on enums `PaymentIntent.payment_method_options.card.request_three_d_secure`, `PaymentIntentConfirmParams.payment_method_options.card.request_three_d_secure`, `PaymentIntentCreateParams.payment_method_options.card.request_three_d_secure`, `PaymentIntentUpdateParams.payment_method_options.card.request_three_d_secure`, `SetupIntent.payment_method_options.card.request_three_d_secure`, `SetupIntentConfirmParams.payment_method_options.card.request_three_d_secure`, `SetupIntentCreateParams.payment_method_options.card.request_three_d_secure`, and `SetupIntentUpdateParams.payment_method_options.card.request_three_d_secure`
  * Add support for `revolut_pay` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationUpdateParams`, and `PaymentMethodConfiguration`
  * Change type of `Quote.invoice_settings` from `InvoiceSettingQuoteSetting | null` to `InvoiceSettingQuoteSetting`
  * Add support for `destination_details` on `Refund`
  * Add support for new value `financial_connections.account.refreshed_transactions` on enums `WebhookEndpointCreateParams.enabled_events[]` and `WebhookEndpointUpdateParams.enabled_events[]`

* [#1185](https://github.com/stripe/stripe-python/pull/1185) Update generated code
* [#1184](https://github.com/stripe/stripe-python/pull/1184) Remove api_base from RequestOptions type
* [#1178](https://github.com/stripe/stripe-python/pull/1178) Support accessing reserved word resource properties via attribute

## 7.10.0b1 - 2023-12-14
* [#1166](https://github.com/stripe/stripe-python/pull/1166) Update generated code for beta
* [#1164](https://github.com/stripe/stripe-python/pull/1164) Beta: revert broken logger

## 7.9.0 - 2023-12-14
* [#1161](https://github.com/stripe/stripe-python/pull/1161) Update generated code

  * Add support for `payment_method_reuse_agreement` on resource classes `PaymentLink.ConsentCollection` and `checkout.Session.ConsentCollection` and parameter classes `PaymentLink.CreateParamsConsentCollection` and `checkout.Session.CreateParamsConsentCollection`
  * Add support for `after_submit` on parameter classes `PaymentLink.CreateParamsCustomText`, `PaymentLink.ModifyParamsCustomText`, and `checkout.Session.CreateParamsCustomText` and resource classes `PaymentLink.CustomText` and `checkout.Session.CustomText`
  * Add support for `created` on parameter class `radar.EarlyFraudWarning.ListParams`
* [#1146](https://github.com/stripe/stripe-python/pull/1146) Track usage of deprecated `save`
  * Reports uses of the deprecated `.save` in `X-Stripe-Client-Telemetry`. (You can disable telemetry via `stripe.enable_telemetry = false`, see the [README](https://github.com/stripe/stripe-python/blob/master/README.md#telemetry).)
* [#1101](https://github.com/stripe/stripe-python/pull/1101) Mark defunct and internal methods as deprecated
* [#1169](https://github.com/stripe/stripe-python/pull/1169) Add more types to _http_client.py

## 7.9.0b1 - 2023-12-08
* [#1163](https://github.com/stripe/stripe-python/pull/1163) Update generated code for beta
  * Add support for `retrieve` method on resource `FinancialConnections.Transaction`

## 7.8.2 - 2023-12-11
* [#1168](https://github.com/stripe/stripe-python/pull/1168) Do not raise a DeprecationWarning in `stripe.app_info`

## 7.8.1 - 2023-12-08
* [#1159](https://github.com/stripe/stripe-python/pull/1159) Fix __getattr__ to raise AttributeError rather than returning None. This fixes a regression in 7.8.0 that caused `stripe.checkout`/`stripe.issuing` etc. to return `None`.
* [#1157](https://github.com/stripe/stripe-python/pull/1157) Add missing explicit reexport for `OAuth`, `Webhook`, `WebhookSignature`

## 7.8.0 - 2023-12-07
* [#1155](https://github.com/stripe/stripe-python/pull/1155) Update generated code
  * Add support for `payment_details`, `payments`, and `payouts` on `AccountSession.components` and `CreateParams.components`
  * Add support for `features` on `AccountSession.components.account_onboarding` and `CreateParams.components.account_onboarding`
  * Add support for new values `customer_tax_location_invalid` and `financial_connections_no_successful_transaction_refresh` on enums `Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and `StripeError.code`
  * Add support for new values `payment_network_reserve_hold` and `payment_network_reserve_release` on enum `BalanceTransaction.type`
  * Change `Climate.Product.metric_tons_available` to be required
  * Remove support for value `various` from enum `Climate.Supplier.removal_pathway`
  * Remove support for values `challenge_only` and `challenge` from enum `PaymentIntent.payment_method_options.card.request_three_d_secure`
  * Add support for `inactive_message` and `restrictions` on `CreateParams`, `ModifyParams`, and `PaymentLink`
  * Add support for `transfer_group` on `PaymentLink.payment_intent_data`, `CreateParams.payment_intent_data`, and `ModifyParams.payment_intent_data`
  * Add support for `trial_settings` on `PaymentLink.subscription_data`, `CreateParams.subscription_data`, and `ModifyParams.subscription_data`
* [#1153](https://github.com/stripe/stripe-python/pull/1153) Move exports for more modules
  -  `stripe.app_info`, `stripe.http_client`, `stripe.oauth`, `stripe.util`, `stripe.version`, `stripe.webhook`,  modules are deprecated. All types are available directly from `stripe` module now.
     Before:
     ```python
     from stripe.util import convert_to_stripe_object
     # or
     stripe.util.convert_to_stripe_object
     ````
     After:
     ```python
     from stripe import convert_to_stripe_object
     # or
     stripe.convert_to_stripe_object
     ```
  - `stripe.api_version`, `stripe.multipart_data_generator`, `stripe.request_metrics` are deprecated and will be fully removed in the future.
* [#1142](https://github.com/stripe/stripe-python/pull/1142) Move resource type exports to stripe.___
  - `stripe.error`, `stripe.stripe_object`, `stripe.api_requestor`, `stripe.stripe_response`, `stripe.request_options`, `stripe.api_resources.*`,  `stripe.api_resources.abstract.*` modules are deprecated. All types are available directly from `stripe` module now.
     Before:
     ```python
     from stripe.error import APIError
     # or
     stripe.error.APIError
     ````
     After:
     ```python
     from stripe import APIError
     # or
     stripe.APIError
     ```

## 7.8.0b1 - 2023-11-30
* [#1148](https://github.com/stripe/stripe-python/pull/1148) Update generated code for beta

## 7.7.0 - 2023-11-30
* [#1147](https://github.com/stripe/stripe-python/pull/1147) Update generated code
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
* [#1145](https://github.com/stripe/stripe-python/pull/1145) Refactor integration test

## 7.7.0b1 - 2023-11-21
* [#1141](https://github.com/stripe/stripe-python/pull/1141) Update generated code for beta
* Rename `receipient` to `recipient` beneath `PaymentDetails` on `Charge` and `PaymentIntent` APIs.* Add support for `electronic_commerce_indicator` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure` and `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`
* Add support for `components` on parameter class `CustomerSession.CreateParams` and resource `CustomerSession`

## 7.6.0 - 2023-11-21
* [#1138](https://github.com/stripe/stripe-python/pull/1138) Update generated code
  * Add support for `electronic_commerce_indicator` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure` and `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`
  * Add support for `exemption_indicator` on resource class `Charge.PaymentMethodDetails.Card.ThreeDSecure`
  * Add support for `transaction_id` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure`, `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`, `issuing.Authorization.NetworkData`, and `issuing.Transaction.NetworkData`
  * Add support for `offline` on resource class `Charge.PaymentMethodDetails.CardPresent`
  * Add support for `transferred_to_balance` on resource `CustomerCashBalanceTransaction`
  * Add support for `three_d_secure` on parameter classes `PaymentIntent.ConfirmParamsPaymentMethodOptionsCard`, `PaymentIntent.CreateParamsPaymentMethodOptionsCard`, `PaymentIntent.ModifyParamsPaymentMethodOptionsCard`, `SetupIntent.ConfirmParamsPaymentMethodOptionsCard`, `SetupIntent.CreateParamsPaymentMethodOptionsCard`, and `SetupIntent.ModifyParamsPaymentMethodOptionsCard`
  * Add support for `system_trace_audit_number` on resource class `issuing.Authorization.NetworkData`
  * Add support for `network_risk_score` on resource classes `issuing.Authorization.PendingRequest` and `issuing.Authorization.RequestHistory`
  * Add support for `requested_at` on resource class `issuing.Authorization.RequestHistory`
  * Add support for `authorization_code` on resource class `issuing.Transaction.NetworkData`

## 7.6.0b1 - 2023-11-16
* [#1128](https://github.com/stripe/stripe-python/pull/1128) Update generated code for beta
  * Add support for `issuing_card` and `issuing_cards_list` on `AccountSession.CreateParamsComponents`
  * Add support for `event_details` and `subscription` on `payment_details` types
  * Add support for `affiliate` and `delivery` on `payment_details.flight`, `payment_details.lodging`, and `payment_details.car_rental` types
  * Add support for `drivers` on `payment_details.car_rental` types
  * Add support for `passengers` on `payment_details.flight` and `payment_details.lodging` types
  * Add support for `created` on `CustomerSession`

## 7.5.0 - 2023-11-16
* [#1127](https://github.com/stripe/stripe-python/pull/1127) Update generated code
  * Add support for `bacs_debit_payments` on `Account.CreateParamsSettings`
  * Add support for `service_user_number` on `Account.Settings.BacsDebitPayments`
  * Add support for `capture_before` on `Charge.PaymentMethodDetails.Card.capture_before`
  * Add support for `Paypal` on `Checkout.Session.PaymentMethodOptions`
  * Add support for `tax_amounts` on `CreditNote.CreateParamsLine`, `CreditNote.PreviewParamsLine`, and `CreditNote.PreviewLinesParamsLine`
  * Add support for `network_data` on `Issuing.Transaction`
  * Add support for `status` on `Checkout.Session.ListParams`
* [#1135](https://github.com/stripe/stripe-python/pull/1135) Add initial tests for exports and run them in mypy and pyright
* [#1130](https://github.com/stripe/stripe-python/pull/1130) Mention types in README.md
* [#1134](https://github.com/stripe/stripe-python/pull/1134) Run pyright via tox
* [#1131](https://github.com/stripe/stripe-python/pull/1131) Upgrade black dependency
* [#1132](https://github.com/stripe/stripe-python/pull/1132) Fix unnecessary casts from pyright 1.1.336
* [#1126](https://github.com/stripe/stripe-python/pull/1126) Suppress type errors from latest pyright
* [#1125](https://github.com/stripe/stripe-python/pull/1125) Add support for Python 3.11/3.12
* [#1123](https://github.com/stripe/stripe-python/pull/1123) Move to python3 venv and update vscode settings

## 7.5.0b1 - 2023-11-10
* [#1120](https://github.com/stripe/stripe-python/pull/1120) Update generated code for beta

## 7.4.0 - 2023-11-09
* [#1119](https://github.com/stripe/stripe-python/pull/1119) Update generated code
  * Add support for new value `terminal_reader_hardware_fault` on enums `Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and `StripeError.code`
  * Add support for `metadata` on `Quote.subscription_data`, `QuoteCreateParams.subscription_data`, and `QuoteUpdateParams.subscription_data`
* [#1121](https://github.com/stripe/stripe-python/pull/1121) [types] Remove `None` from optional param types

## 7.4.0b1 - 2023-11-02
* [#1110](https://github.com/stripe/stripe-python/pull/1110) Update generated code for beta
  * Add support for `attach_payment_intent` method on resource `Invoice`

## 7.3.0 - 2023-11-02
* [#1112](https://github.com/stripe/stripe-python/pull/1112) Update generated code
  * Add support for new resource `Tax.Registration`
  * Add support for `create`, `list`, and `modify` methods on resource `Registration`

## 7.2.0 - 2023-10-31
* [#1115](https://github.com/stripe/stripe-python/pull/1115) Types: Add types for `ErrorObject`.
* [#1116](https://github.com/stripe/stripe-python/pull/1116) Types: Use @staticmethod overloads instead of @classmethod to fix MyPy compatibility.

## 7.1.0 - 2023-10-26
* [#1104](https://github.com/stripe/stripe-python/pull/1104) Include `py.typed` and enable type annotations for the package
  * This PR includes `py.typed` and enables inline type annotations for stripe-python package. Inline type annotations will now take precedence over Typeshed for users who use a type checker or IDE.
  * See a detailed guide on the [Github Wiki](https://github.com/stripe/stripe-python/wiki/Inline-type-annotations).
* [#1103](https://github.com/stripe/stripe-python/pull/1103) Inner resource classes
  * Behavior change: nested json objects will now deserialize into instances of specific classes that subclass `StripeObject`, instead of into generic `StripeObject` instances.
  * ⚠️  Behavior change: `PromotionCode.restrictions.currency_options` will now deserialize into `dict` and not `StripeObject`.
* [#1090](https://github.com/stripe/stripe-python/pull/1090) Update generated code
  * Add support for new value `balance_invalid_parameter` on enums `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, and `SetupIntent.LastSetupError`
* [#1096](https://github.com/stripe/stripe-python/pull/1096) Add @util.deprecated decorator and deprecate `save`.
* [#1091](https://github.com/stripe/stripe-python/pull/1091) APIRequestor: don't mutate incoming multipart headers


# Changelog

## 7.2.0b1 - 2023-10-26
* [#1107](https://github.com/stripe/stripe-python/pull/1107) Update generated code for beta
  * Add support for new resource `Margin`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `Margin`

## 7.1.0b1 - 2023-10-17
* [#1084](https://github.com/stripe/stripe-python/pull/1084) Update generated code for beta
  - Update pinned API version to `2023-10-16`
* [#1083](https://github.com/stripe/stripe-python/pull/1083) Update generated code for beta

## 7.0.0 - 2023-10-16
* This release changes the pinned API version to `2023-10-16`. Please read the [API Upgrade Guide](https://stripe.com/docs/upgrades#2023-10-16) and carefully review the API changes before upgrading `stripe-python`.
* [#1085](https://github.com/stripe/stripe-python/pull/1085) Update generated code
  - Updated pinned API version

## 6.8.0b3 - 2023-10-13


## 6.8.0b2 - 2023-10-11
* [#1073](https://github.com/stripe/stripe-python/pull/1073) Update generated code for beta
  Release specs are identical.
* [#1061](https://github.com/stripe/stripe-python/pull/1061) Types: inner resource classes

## 6.8.0b1 - 2023-10-05
* [#1066](https://github.com/stripe/stripe-python/pull/1066) Update generated code for beta
  * Add support for `mark_draft` and `mark_stale` methods on resource `Quote`
  * Remove support for `draft_quote` and `mark_stale_quote` methods on resource `Quote`
  * Rename `preview_invoice_lines` to `list_preview_invoice_lines` on resource `Quote`
* [#1059](https://github.com/stripe/stripe-python/pull/1059) Update generated code for beta
  * Rename resources `Issuing.CardDesign` and `Issuing.CardBundle` to `Issuing.PersonalizationDesign` and `Issuing.PhysicalBundle`

## 6.7.0 - 2023-10-05
* [#1065](https://github.com/stripe/stripe-python/pull/1065) Update generated code
  * Add support for new resource `Issuing.Token`
  * Add support for `list`, `modify`, and `retrieve` methods on resource `Token`

## 6.7.0b2 - 2023-09-28
* [#1059](https://github.com/stripe/stripe-python/pull/1059) Update generated code for beta
  * Rename resources `Issuing.CardDesign` and `Issuing.CardBundle` to `Issuing.PersonalizationDesign` and `Issuing.PhysicalBundle`
* [#997](https://github.com/stripe/stripe-python/pull/997) Remove developer_message support

## 6.7.0b1 - 2023-09-21
* [#1053](https://github.com/stripe/stripe-python/pull/1053) Update generated code for beta

## 6.6.0 - 2023-09-21
* [#1056](https://github.com/stripe/stripe-python/pull/1056) Update generated code

* [#1055](https://github.com/stripe/stripe-python/pull/1055) Partially type resource methods (no **params)
* [#1057](https://github.com/stripe/stripe-python/pull/1057) Add optional types to non-required fields
* [#1054](https://github.com/stripe/stripe-python/pull/1054) Types: add deleted field

## 6.6.0b1 - 2023-09-14
* [#1048](https://github.com/stripe/stripe-python/pull/1048) Update generated code for beta
  * Add support for new resource `ConfirmationToken`
  * Add support for `retrieve` method on resource `ConfirmationToken`
  * Add support for `create` method on resource `Issuing.CardDesign`
  * Add support for `reject_testmode` test helper method on resource `Issuing.CardDesign`

## 6.5.0 - 2023-09-14
* [#1052](https://github.com/stripe/stripe-python/pull/1052) Update generated code
  * Add support for new resource `PaymentMethodConfiguration`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentMethodConfiguration`
* [#1047](https://github.com/stripe/stripe-python/pull/1047) Update generated code
  * Add support for `capture`, `create`, `expire`, `increment`, and `reverse` test helper methods on resource `Issuing.Authorization`
  * Add support for `create_force_capture`, `create_unlinked_refund`, and `refund` test helper methods on resource `Issuing.Transaction`
* [#1049](https://github.com/stripe/stripe-python/pull/1049) Types: datetimes to ints, add enum support
* [#1030](https://github.com/stripe/stripe-python/pull/1030) Explicitly define CRUDL methods in each resource
* [#1050](https://github.com/stripe/stripe-python/pull/1050) Generate explicit nested resource class methods

## 6.5.0b1 - 2023-09-07
* [#1045](https://github.com/stripe/stripe-python/pull/1045) Update generated code for beta
  * Release specs are identical.
* [#1034](https://github.com/stripe/stripe-python/pull/1034) Update generated code for beta
  * Remove support for `submit_card` test helper method on resource `Issuing.Card`

## 6.4.0 - 2023-09-07
* [#1033](https://github.com/stripe/stripe-python/pull/1033) Update generated code
  * Add support for new resource `PaymentMethodDomain`
  * Add support for `create`, `list`, `modify`, `retrieve`, and `validate` methods on resource `PaymentMethodDomain`
* [#1044](https://github.com/stripe/stripe-python/pull/1044) Types: ExpandableField
* [#1043](https://github.com/stripe/stripe-python/pull/1043) Types: ListObject

## 6.3.0 - 2023-09-05
* [#1042](https://github.com/stripe/stripe-python/pull/1042) Require typing_extensions >= 4.0.0
* [#1026](https://github.com/stripe/stripe-python/pull/1026) Types: annotate resource properties

## 6.3.0b1 - 2023-08-31
* [#1029](https://github.com/stripe/stripe-python/pull/1029) Update generated code for beta
  * Rename `Quote.preview_invoices` and `Quote.preview_subscription_schedules` to `Quote.list_preview_invoices` and `Quote.list_preview_schedules`.

## 6.2.0 - 2023-08-31
* [#1024](https://github.com/stripe/stripe-python/pull/1024) Update generated code
  * Add support for new resource `AccountSession`
  * Add support for `create` method on resource `AccountSession`
* [#1032](https://github.com/stripe/stripe-python/pull/1032) Types for CRUDL methods on parents

## 6.1.0 - 2023-08-24
* [#1016](https://github.com/stripe/stripe-python/pull/1016) Update generated code
* [#1020](https://github.com/stripe/stripe-python/pull/1020) Adds type annotations, and dependency on `typing_extensions`.

## 6.1.0b2 - 2023-08-23
* [#1006](https://github.com/stripe/stripe-python/pull/1006) [#1017](https://github.com/stripe/stripe-python/pull/1017) Update generated code for beta
* [#1020](https://github.com/stripe/stripe-python/pull/1020) Adds type_annotations, and dependency on `typing_extensions`.

## 6.1.0b1 - 2023-08-23
  * Updated stable APIs to the latest version

## 6.0.0 - 2023-08-16
**⚠️ ACTION REQUIRED: the breaking change in this release likely affects you ⚠️**
* [#1001](https://github.com/stripe/stripe-python/pull/1001) [#1008](https://github.com/stripe/stripe-python/pull/1008) Remove support for Python 2.
  * The last version of stripe-python that supports Python 2 is 5.5.0. [The Python Software Foundation (PSF)](https://www.python.org/psf-landing/) community [announced the end of support of Python 2](https://www.python.org/doc/sunset-python-2/) on 01 January 2020. To continue to get new features and security updates, please make sure to update your Python runtime to Python 3.6+.
* [#987](https://github.com/stripe/stripe-python/pull/987) ⚠️⚠️Pin to the latest API version⚠️⚠️

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

* [#1013](https://github.com/stripe/stripe-python/pull/1013) ⚠️Removed @test_helper decorator
  * This is technically breaking but unlikely to affect most users.
* [#1015](https://github.com/stripe/stripe-python/pull/1015) ⚠️Assert types of pagination responses
  * Pagination will raise an exception if the API response is not of the correct type. This should never happen in production use but may break tests that use mock data.

## 5.6.0b3 - 2023-08-03
* [#1004](https://github.com/stripe/stripe-python/pull/1004) Update generated code for beta
  * Add support for `submit_card` test helper method on resource `Issuing.Card`
* [#999](https://github.com/stripe/stripe-python/pull/999) Update generated code for beta

* [#997](https://github.com/stripe/stripe-python/pull/997) Remove developer_message support

## 5.6.0b2 - 2023-07-28
* [#995](https://github.com/stripe/stripe-python/pull/995) Update generated code for beta
  * Add support for new resource `Tax.Form`
  * Add support for `list`, `pdf`, and `retrieve` methods on resource `Form`
* [#992](https://github.com/stripe/stripe-python/pull/992) Update generated code for beta

## 5.6.0b1 - 2023-07-13
* [#991](https://github.com/stripe/stripe-python/pull/991) Update generated code for beta
  Release specs are identical.
* [#989](https://github.com/stripe/stripe-python/pull/989) Update generated code for beta
  * Add support for new resource `PaymentMethodConfiguration`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentMethodConfiguration`
* [#985](https://github.com/stripe/stripe-python/pull/985) Update generated code for beta

* [#986](https://github.com/stripe/stripe-python/pull/986) Consolidate beta SDKs section

## 5.5.0 - 2023-07-13
* [#990](https://github.com/stripe/stripe-python/pull/990) Update generated code
  * Add support for new resource `Tax.Settings`
  * Add support for `modify` and `retrieve` methods on resource `Settings`

## 5.5.0b5 - 2023-06-22
* [#982](https://github.com/stripe/stripe-python/pull/982) Update generated code for beta
  * Add support for new resource `CustomerSession`
  * Add support for `create` method on resource `CustomerSession`
* [#979](https://github.com/stripe/stripe-python/pull/979) Update generated code for beta
* [#976](https://github.com/stripe/stripe-python/pull/976) Update generated code for beta

## 5.5.0b4 - 2023-06-02
* [#973](https://github.com/stripe/stripe-python/pull/973) Update generated code for beta
* [#969](https://github.com/stripe/stripe-python/pull/969) Update generated code for beta
* [#971](https://github.com/stripe/stripe-python/pull/971) Handle developer message in preview error responses

## 5.5.0b3 - 2023-05-19
* [#966](https://github.com/stripe/stripe-python/pull/966) Update generated code for beta
  * Add support for `subscribe` and `unsubscribe` methods on resource `FinancialConnections.Account`
* [#965](https://github.com/stripe/stripe-python/pull/965) Add raw_request
* [#964](https://github.com/stripe/stripe-python/pull/964) Update generated code for beta
* [#961](https://github.com/stripe/stripe-python/pull/961) Update generated code for beta

## 5.5.0b2 - 2023-04-13
* [#954](https://github.com/stripe/stripe-python/pull/954) Update generated code for beta
  * Add support for `collect_payment_method` and `confirm_payment_intent` methods on resource `Terminal.Reader`
* [#953](https://github.com/stripe/stripe-python/pull/953) Update generated code for beta

## 5.5.0b1 - 2023-03-30
* [#950](https://github.com/stripe/stripe-python/pull/950) Update generated code for beta

## 5.4.0 - 2023-03-30
* [#951](https://github.com/stripe/stripe-python/pull/951) Update generated code
  * Remove support for `create` method on resource `Tax.Transaction`
    * This is not a breaking change, as this method was deprecated before the Tax Transactions API was released in favor of the `create_from_calculation` method.

## 5.4.0b1 - 2023-03-23
* [#941](https://github.com/stripe/stripe-python/pull/941) Update generated code for beta (new)
  * Add support for new resources `Tax.CalculationLineItem` and `Tax.TransactionLineItem`
  * Add support for `collect_inputs` method on resource `Terminal.Reader`

## 5.3.0 - 2023-03-23
* [#947](https://github.com/stripe/stripe-python/pull/947) Update generated code
  * Add support for new resources `Tax.CalculationLineItem`, `Tax.Calculation`, `Tax.TransactionLineItem`, and `Tax.Transaction`
  * Add support for `create` and `list_line_items` methods on resource `Calculation`
  * Add support for `create_from_calculation`, `create_reversal`, `create`, `list_line_items`, and `retrieve` methods on resource `Transaction`

## 5.3.0b4 - 2023-03-16
* [#940](https://github.com/stripe/stripe-python/pull/940) Update generated code for beta (new)
  * Add support for `create_from_calculation` method on resource `Tax.Transaction`
* [#938](https://github.com/stripe/stripe-python/pull/938) Update generated code for beta (new)
  * Remove support for resources `Capital.FinancingOffer` and `Capital.FinancingSummary`
  * Remove support for `list`, `mark_delivered`, and `retrieve` methods on resource `FinancingOffer`
  * Remove support for `retrieve` method on resource `FinancingSummary`

## 5.3.0b3 - 2023-03-09
* [#936](https://github.com/stripe/stripe-python/pull/936) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Remove support for `list_transactions` method on resource `Tax.Transaction`

## 5.3.0b2 - 2023-03-03
* [#935](https://github.com/stripe/stripe-python/pull/935) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resources `Issuing.CardBundle` and `Issuing.CardDesign`
  * Add support for `list` and `retrieve` methods on resource `CardBundle`
  * Add support for `list`, `modify`, and `retrieve` methods on resource `CardDesign`

## 5.3.0b1 - 2023-02-23
* [#931](https://github.com/stripe/stripe-python/pull/931) API Updates for beta branch
  * Updated stable APIs to the latest version

## 5.2.0 - 2023-02-16
* [#924](https://github.com/stripe/stripe-python/pull/924) API Updates
  * Add support for `refund_payment` method on resource `Terminal.Reader`

## 5.2.0b1 - 2023-02-02
* [#921](https://github.com/stripe/stripe-python/pull/921) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resource `FinancialConnections.Transaction`
  * Add support for `list` method on resource `Transaction`

## 5.1.1 - 2023-02-06
* [#923](https://github.com/stripe/stripe-python/pull/923) Bugfix: revert "Pass params into logger.{info,debug}"

## 5.1.0 - 2023-02-02
* [#920](https://github.com/stripe/stripe-python/pull/920) API Updates
  * Add support for `resume` method on resource `Subscription`
* [#913](https://github.com/stripe/stripe-python/pull/913) Pass params into logger.{info,debug}

## 5.1.0b7 - 2023-01-26
* [#917](https://github.com/stripe/stripe-python/pull/917) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `list_transactions` method on resource `Tax.Transaction`

## 5.1.0b6 - 2023-01-19
* [#915](https://github.com/stripe/stripe-python/pull/915) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `Tax.Settings` resource.

## 5.1.0b5 - 2023-01-12
* [#914](https://github.com/stripe/stripe-python/pull/914) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Change `quote.draft_quote` implementation to from calling `POST /v1/quotes/{quote}/draft` to `POST /v1/quotes/{quote}/mark_draft`
  * Add support for `tax.Registration` resource

## 5.1.0b4 - 2023-01-05
* [#912](https://github.com/stripe/stripe-python/pull/912) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `mark_stale_quote` method on resource `Quote`

## 5.1.0b3 - 2022-12-22
* [#910](https://github.com/stripe/stripe-python/pull/910) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Move `stripe.TaxCalculation` and `stripe.TaxTranscation` to `stripe.tax.Calculation` and `stripe.tax.Transaction`.

## 5.1.0b2 - 2022-12-15
* [#906](https://github.com/stripe/stripe-python/pull/906) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resources `QuoteLine`, `TaxCalculation`, and `TaxTransaction`
  * Add support for `create` and `list_line_items` methods on resource `TaxCalculation`
  * Add support for `create_reversal`, `create`, and `retrieve` methods on resource `TaxTransaction`

## 5.1.0b1 - 2022-12-08
* [#902](https://github.com/stripe/stripe-python/pull/902) API Updates for beta branch
  * Updated stable APIs to the latest version
* [#898](https://github.com/stripe/stripe-python/pull/898) API Updates for beta branch
  * Updated stable APIs to the latest version

## 5.0.0 - 2022-11-16

Breaking changes that arose during code generation of the library that we postponed for the next major version. For changes to the Stripe products, read more at https://stripe.com/docs/upgrades#2022-11-15.

"⚠️" symbol highlights breaking changes.

* [#895](https://github.com/stripe/stripe-python/pull/895) Next major release changes
* [#889](https://github.com/stripe/stripe-python/pull/889) API Updates

* [#888](https://github.com/stripe/stripe-python/pull/888) Do not run Coveralls if secret token is not available
* [#875](https://github.com/stripe/stripe-python/pull/875) hide misleading ssl security warning in python>=2.7.9

## 4.3.0b3 - 2022-11-02
* [#890](https://github.com/stripe/stripe-python/pull/890) API Updates for beta branch
  * Updated beta APIs to the latest stable version
* [#885](https://github.com/stripe/stripe-python/pull/885) Update changelog for the Gift Card API
* [#884](https://github.com/stripe/stripe-python/pull/884) API Updates for beta branch
  * Updated stable APIs to the latest version

## 4.3.0b1 - 2022-09-26
* [#878](https://github.com/stripe/stripe-python/pull/878) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add `FinancingOffer`, `FinancingSummary` and `FinancingTransaction` resources.

## 4.2.0 - 2022-09-23
* [#877](https://github.com/stripe/stripe-python/pull/877) API Updates
  * Add `upcoming_lines` method to the `Invoice` resource.
* [#873](https://github.com/stripe/stripe-python/pull/873) Add abstract methods for SearchableAPIResource
* [#867](https://github.com/stripe/stripe-python/pull/867) API Updates
  * Update links in documentation to be absolute.

## 4.2.0b2 - 2022-08-26
* [#869](https://github.com/stripe/stripe-python/pull/869) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for the beta [Gift Card API](https://stripe.com/docs/gift-cards).

## 4.2.0b1 - 2022-08-23
* [#866](https://github.com/stripe/stripe-python/pull/866) API Updates for beta branch
  - Updated stable APIs to the latest version
  - `Stripe-Version` beta headers are not pinned by-default and need to be manually specified, please refer to [beta SDKs README section](https://github.com/stripe/stripe-dotnet/blob/master/README.md#beta-sdks)

## 4.1.0 - 2022-08-19
* [#861](https://github.com/stripe/stripe-python/pull/861) API Updates
  * Add support for new resource `CustomerCashBalanceTransaction`
* [#860](https://github.com/stripe/stripe-python/pull/860) Add a support section to the readme
* [#717](https://github.com/stripe/stripe-python/pull/717) Fix test TestCharge.test_is_saveable().

## 4.1.0b2 - 2022-08-11
* [#859](https://github.com/stripe/stripe-python/pull/859) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `refund_payment` method to Terminal resource

## 4.1.0b1 - 2022-08-03
* [#848](https://github.com/stripe/stripe-python/pull/848) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Added the `Order` resource support

## 4.0.2 - 2022-08-03
* [#855](https://github.com/stripe/stripe-python/pull/855) Fix issue where auto_paging_iter failed on nested list objects.

## 4.0.1 - 2022-08-02
* [#850](https://github.com/stripe/stripe-python/pull/850) Fix incorrect handling of additional request parameters
  * Fixes issue where using special parameter like `api_key`, `idempotency_key`, `stripe_version`, `stripe_account`, `headers` can cause a `Received unknown parameter error`.

## 4.0.0 - 2022-08-02

Breaking changes that arose during code generation of the library that we postponed for the next major version. For changes to the SDK, read more detailed description at https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v4. For changes to the Stripe products, read more at https://stripe.com/docs/upgrades#2022-08-01.

"⚠️" symbol highlights breaking changes.

* [#847](https://github.com/stripe/stripe-python/pull/847) API Updates
* [#845](https://github.com/stripe/stripe-python/pull/845) Next major release changes
* [#836](https://github.com/stripe/stripe-python/pull/836) API Updates. Add Price.create tests.
* [#835](https://github.com/stripe/stripe-python/pull/835) API Updates. Use auto-generation for credit_note and invoice methods.

## 3.6.0b1 - 2022-07-22
* [#843](https://github.com/stripe/stripe-python/pull/843) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `QuotePhase` resource
* [#840](https://github.com/stripe/stripe-python/pull/840) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `SubscriptionSchedule.amend` method.
* [#837](https://github.com/stripe/stripe-python/pull/837) API Updates for beta branch
  - Include `server_side_confirmation_beta=v1` beta
  - Add `secretKeyConfirmation` to `PaymentIntent`
* [#834](https://github.com/stripe/stripe-python/pull/834) API Updates for beta branch
  - Updated stable APIs to the latest version
* [#826](https://github.com/stripe/stripe-python/pull/826) Use the generated API version

## 3.5.0 - 2022-06-30
* [#831](https://github.com/stripe/stripe-python/pull/831) API Updates
  * Add support for `deliver_card`, `fail_card`, `return_card`, and `ship_card` test helper methods on resource `Issuing.Card`
  * Switch from using `instance_url` to computing method path in place for custom methods.
  * Switch from using explicit class methods for test helpers instead of using meta-programming.

## 3.4.0 - 2022-06-17
* [#824](https://github.com/stripe/stripe-python/pull/824) API Updates
  * Add support for `fund_cash_balance` test helper method on resource `Customer`
* [#823](https://github.com/stripe/stripe-python/pull/823) Trigger workflows on beta branches

## 3.3.0 - 2022-06-08
* [#818](https://github.com/stripe/stripe-python/pull/818) fix: Update cash balance methods to no longer require nested ID.

## 3.2.0 - 2022-05-23
* [#812](https://github.com/stripe/stripe-python/pull/812) API Updates
  * Add support for new resource `Apps.Secret`

## 3.1.0 - 2022-05-19
* [#810](https://github.com/stripe/stripe-python/pull/810) API Updates
  * Add support for new resources `Treasury.CreditReversal`, `Treasury.DebitReversal`, `Treasury.FinancialAccountFeatures`, `Treasury.FinancialAccount`, `Treasury.FlowDetails`, `Treasury.InboundTransfer`, `Treasury.OutboundPayment`, `Treasury.OutboundTransfer`, `Treasury.ReceivedCredit`, `Treasury.ReceivedDebit`, `Treasury.TransactionEntry`, and `Treasury.Transaction`
  * Add support for `retrieve_payment_method` method on resource `Customer`
  * Add support for `list_owners` and `list` methods on resource `FinancialConnections.Account`
* [#719](https://github.com/stripe/stripe-python/pull/719) Set daemon attribute instead of using setDaemon method that was deprecated in Python 3.10
* [#767](https://github.com/stripe/stripe-python/pull/767) Bump vendored six to 1.16.0
* [#806](https://github.com/stripe/stripe-python/pull/806) Start testing on pypy-3.8
* [#811](https://github.com/stripe/stripe-python/pull/811) Add sanitize_id method

## 3.0.0 - 2022-05-09
* [#809](https://github.com/stripe/stripe-python/pull/809) Release of major version v3.0.0. The [migration guide](https://github.com/stripe/stripe-python/wiki/Migration-Guide-for-v3) contains more information.
  (⚠️ = breaking changes):
  * ⚠️ Replace the legacy `Order` API with the new `Order` API.
    * New methods: `cancel`, `list_line_items`, `reopen`, and `submit`
    * Removed methods: `pay` and `return_order`
    * Removed resources: `OrderItem` and `OrderReturn`
  * ⚠️ Rename `financial_connections.account.refresh` to `financial_connections.refresh_account`
  * Add support for `amount_discount`, `amount_tax`, and `product` on `LineItem`

## 2.76.0 - 2022-05-05
* [#808](https://github.com/stripe/stripe-python/pull/808) API Updates
  * Add support for new resources `FinancialConnections.AccountOwner`, `FinancialConnections.AccountOwnership`, `FinancialConnections.Account`, and `FinancialConnections.Session`

## 2.75.0 - 2022-05-03
* [#805](https://github.com/stripe/stripe-python/pull/805) API Updates
  * Add support for new resource `CashBalance`

## 2.74.0 - 2022-04-21
* [#796](https://github.com/stripe/stripe-python/pull/796) API Updates
  * Add support for `expire` test helper method on resource `Refund`

## 2.73.0 - 2022-04-18
* [#792](https://github.com/stripe/stripe-python/pull/792) [#794](https://github.com/stripe/stripe-python/pull/794) [#795](https://github.com/stripe/stripe-python/pull/795) API Updates
  * Add support for new resources `FundingInstructions` and `Terminal.Configuration`

## 2.72.0 - 2022-04-13
* [#791](https://github.com/stripe/stripe-python/pull/791) API Updates
  * Add support for `increment_authorization` method on resource `PaymentIntent`

## 2.71.0 - 2022-04-08
* [#788](https://github.com/stripe/stripe-python/pull/788) API Updates
  * Add support for `apply_customer_balance` method on resource `PaymentIntent`

## 2.70.0 - 2022-03-30
* [#785](https://github.com/stripe/stripe-python/pull/785) API Updates
  * Add support for `cancel_action`, `process_payment_intent`, `process_setup_intent`, and `set_reader_display` methods on resource `Terminal.Reader`

## 2.69.0 - 2022-03-29
* [#783](https://github.com/stripe/stripe-python/pull/783) API Updates
  * Add support for Search API
    * Add support for `search` method on resources `Charge`, `Customer`, `Invoice`, `PaymentIntent`, `Price`, `Product`, and `Subscription`
* [#784](https://github.com/stripe/stripe-python/pull/784) Pin click dependency to 8.0.4 to avoid breakage in black
* [#773](https://github.com/stripe/stripe-python/pull/773) Add infrastructure for test-helper methods
* [#782](https://github.com/stripe/stripe-python/pull/782) Revert Orders to use qualified name for upload_api_base

## 2.68.0 - 2022-03-23
* [#781](https://github.com/stripe/stripe-python/pull/781) API Updates
  * Add support for `cancel` method on resource `Refund`
* [#777](https://github.com/stripe/stripe-python/pull/777) Add support for SearchResult.

## 2.67.0 - 2022-03-01
* [#774](https://github.com/stripe/stripe-python/pull/774) API Updates
  * Add support for new resource `TestHelpers.TestClock`

## 2.66.0 - 2022-02-16
* [#771](https://github.com/stripe/stripe-python/pull/771) API Updates
  * Add support for `verify_microdeposits` method on resources `PaymentIntent` and `SetupIntent`

## 2.65.0 - 2022-01-20
* [#766](https://github.com/stripe/stripe-python/pull/766) API Updates
  * Add support for new resource `PaymentLink`
* [#763](https://github.com/stripe/stripe-python/pull/763) Start testing Python 3.10

## 2.64.0 - 2021-12-21
* [#757](https://github.com/stripe/stripe-python/pull/757) Update class custom methods to save list object parameters.
* [#756](https://github.com/stripe/stripe-python/pull/756) Introduce custom listing methods on objects.
* [#754](https://github.com/stripe/stripe-python/pull/754) Clarify metadata deletion message.

## 2.63.0 - 2021-11-16
* [#748](https://github.com/stripe/stripe-python/pull/748) API Updates
  * Add support for new resource `ShippingRate`

## 2.62.0 - 2021-11-11
* [#745](https://github.com/stripe/stripe-python/pull/745) API Updates
  * Add support for `expire` method on resource `Checkout.Session`

## 2.61.0 - 2021-10-11
* [#738](https://github.com/stripe/stripe-python/pull/738) API Updates
  * Add support for `list_payment_methods` method on resource `Customer`
* [#736](https://github.com/stripe/stripe-python/pull/736) Stop sending raw exception message as part of Stripe user agent.

## 2.60.0 - 2021-07-14
* [#728](https://github.com/stripe/stripe-python/pull/728) API Updates
  * Add support for `list_computed_upfront_line_items` method on resource `Quote`

## 2.59.0 - 2021-07-09
* [#727](https://github.com/stripe/stripe-python/pull/727) [#725](https://github.com/stripe/stripe-python/pull/725) Add support for new `Quote` API.

## 2.58.0 - 2021-06-04
* [#722](https://github.com/stripe/stripe-python/pull/722) API Updates
  * Add support for new `TaxCode` API.

## 2.57.0 - 2021-05-19
* [#720](https://github.com/stripe/stripe-python/pull/720) Add support for Identity VerificationSession and VerificationReport APIs

## 2.56.0 - 2021-02-22
* [#713](https://github.com/stripe/stripe-python/pull/713) Add support for the Billing Portal Configuration API

## 2.55.2 - 2021-02-05
* [#704](https://github.com/stripe/stripe-python/pull/704) Fix CA bundle path issue

## 2.55.1 - 2020-12-01
* [#698](https://github.com/stripe/stripe-python/pull/698) Fix issue where StripeObjects in lists would not be converted to dicts
* [#699](https://github.com/stripe/stripe-python/pull/699) Start testing Python 3.9
* [#691](https://github.com/stripe/stripe-python/pull/691) Include the examples in the built sources

## 2.55.0 - 2020-10-14
* [#684](https://github.com/stripe/stripe-python/pull/684) Add support for the Payout Reverse API

## 2.54.0 - 2020-09-29
* [#681](https://github.com/stripe/stripe-python/pull/681) Add support for the `SetupAttempt` resource and List API
* 2.52.0 and 2.53.0 were empty releases that contained no additional changes.

## 2.51.0 - 2020-09-02
* [#676](https://github.com/stripe/stripe-python/pull/676) Add support for the Issuing Dispute Submit API

## 2.50.0 - 2020-08-05
* [#669](https://github.com/stripe/stripe-python/pull/669) Add support for the `PromotionCode` resource and APIs

## 2.49.0 - 2020-07-17
* [#665](https://github.com/stripe/stripe-python/pull/665) Support stripe.File.create(stripe_version='...')

## 2.48.0 - 2020-05-11
* [#655](https://github.com/stripe/stripe-python/pull/655) Add support for the `LineItem` resource and APIs

## 2.47.0 - 2020-04-29
* [#652](https://github.com/stripe/stripe-python/pull/652) Add support for the `Price` resource and APIs

## 2.46.0 - 2020-04-22
* [#651](https://github.com/stripe/stripe-python/pull/651) Add support for `billing_portal` namespace and `Session` resource and APIs

## 2.45.0 - 2020-04-06
* [#648](https://github.com/stripe/stripe-python/pull/648) Add support for Express links in `authorize_url` for `OAuth`

## 2.44.0 - 2020-03-23
* [#646](https://github.com/stripe/stripe-python/pull/646) Allow overriding API key in OAuth methods

## 2.43.0 - 2020-02-26
* [#644](https://github.com/stripe/stripe-python/pull/644) Add support for listing Checkout `Session`

## 2.42.0 - 2020-01-14
* [#640](https://github.com/stripe/stripe-python/pull/640) Add support for `CreditNoteLineItem`
* [#639](https://github.com/stripe/stripe-python/pull/639) Pin black version
* [#637](https://github.com/stripe/stripe-python/pull/637) Start testing Python 3.8

## 2.41.1 - 2019-12-30
* [#636](https://github.com/stripe/stripe-python/pull/636) Fix uploading files with Unicode names (Python 2.7)
* [#635](https://github.com/stripe/stripe-python/pull/635) Update Python API docs inline link
* [#631](https://github.com/stripe/stripe-python/pull/631) Update `proxy.py`

## 2.41.0 - 2019-11-26
* [#630](https://github.com/stripe/stripe-python/pull/630) Add support for `CreditNote` preview

## 2.40.0 - 2019-11-08
* [#627](https://github.com/stripe/stripe-python/pull/627) Add list_usage_record_summaries and list_source_transactions

## 2.39.0 - 2019-11-06
* [#625](https://github.com/stripe/stripe-python/pull/625) Add support for `Mandate`

## 2.38.0 - 2019-10-29
* [#623](https://github.com/stripe/stripe-python/pull/623) Add support for reverse pagination
* [#624](https://github.com/stripe/stripe-python/pull/624) Contributor Convenant

## 2.37.2 - 2019-10-04
* [#621](https://github.com/stripe/stripe-python/pull/621) Implement support for stripe-should-retry and retry-after headers

## 2.37.1 - 2019-09-26
* [#620](https://github.com/stripe/stripe-python/pull/620) Check that `error` is a dict before trying to use it to create a `StripeError`

## 2.37.0 - 2019-09-26
* [#619](https://github.com/stripe/stripe-python/pull/619) Add `ErrorObject` to `StripeError` exceptions
* [#616](https://github.com/stripe/stripe-python/pull/616) Pass `CFLAGS` and `LDFLAGS` when running tests

## 2.36.2 - 2019-09-12
* [#614](https://github.com/stripe/stripe-python/pull/614) Use `OrderedDict` to maintain key order in API requests and responses

## 2.36.1 - 2019-09-11
* [#612](https://github.com/stripe/stripe-python/pull/612) Use `ListObject` properties as default values in request methods

## 2.36.0 - 2019-09-10
* [#610](https://github.com/stripe/stripe-python/pull/610) Add support for header parameters in `ListObject` request methods

## 2.35.1 - 2019-08-20
* [#605](https://github.com/stripe/stripe-python/pull/605) Fix automatic retries of failed requests
* [#606](https://github.com/stripe/stripe-python/pull/606) Clarify what `max_network_retries` does

## 2.35.0 - 2019-08-12
* [#607](https://github.com/stripe/stripe-python/pull/607) Add `SubscriptionItem.create_usage_record` method

## 2.34.0 - 2019-08-09
* [#604](https://github.com/stripe/stripe-python/pull/604) Remove subscription schedule revisions
  - This is technically a breaking change. We've chosen to release it as a minor vesion bump because the associated API is unused.

## 2.33.2 - 2019-08-06
* [#601](https://github.com/stripe/stripe-python/pull/601) Add support for passing full objects instead of IDs to custom methods
* [#603](https://github.com/stripe/stripe-python/pull/603) Bump vendored six to latest version

## 2.33.1 - 2019-08-06
* [#599](https://github.com/stripe/stripe-python/pull/599) Fix `del` statement to not raise `KeyError`

## 2.33.0 - 2019-07-30
* [#595](https://github.com/stripe/stripe-python/pull/595) Listing `BalanceTransaction` objects now uses `/v1/balance_transactions` instead of `/v1/balance/history`

## 2.32.1 - 2019-07-08
* [#592](https://github.com/stripe/stripe-python/pull/592) Fix argument name conflict

## 2.32.0 - 2019-06-27
* [#590](https://github.com/stripe/stripe-python/pull/590) Add support for the `SetupIntent` resource and APIs

## 2.31.0 - 2019-06-24
* [#587](https://github.com/stripe/stripe-python/pull/587) Enable request latency telemetry by default

## 2.30.1 - 2019-06-20
* [#589](https://github.com/stripe/stripe-python/pull/589) Fix support for `CustomerBalanceTransaction`

## 2.30.0 - 2019-06-17
* [#564](https://github.com/stripe/stripe-python/pull/564) Add support for `CustomerBalanceTransaction` resource and APIs

## 2.29.4 - 2019-06-03
* [#583](https://github.com/stripe/stripe-python/pull/583) Remove Poetry and reinstate `setup.py`

## 2.29.3 - 2019-05-31
Version 2.29.2 was non-functional due to a bugged `version.py` file. This release is identical to 2.29.2 save for the version number.

## 2.29.2 - 2019-05-31
* [#561](https://github.com/stripe/stripe-python/pull/561) Replace pipenv with poetry

## 2.29.1 - 2019-05-31
* [#578](https://github.com/stripe/stripe-python/pull/578) Verify signatures before deserializing events

## 2.29.0 - 2019-05-23
* [#575](https://github.com/stripe/stripe-python/pull/575) Add support for `radar.early_fraud_warning` resource

## 2.28.2 - 2019-05-23
* [#574](https://github.com/stripe/stripe-python/pull/574) Fix a few more code quality issues

## 2.28.1 - 2019-05-20
* [#572](https://github.com/stripe/stripe-python/pull/572) Fix a few code quality issues

## 2.28.0 - 2019-05-14
* [#566](https://github.com/stripe/stripe-python/pull/566) Add support for the `Capability` resource and APIs

## 2.27.0 - 2019-04-24
* [#554](https://github.com/stripe/stripe-python/pull/554) Add support for the `TaxRate` resource and APIs

## 2.26.0 - 2019-04-22
* [#555](https://github.com/stripe/stripe-python/pull/555) Add support for the `TaxId` resource and APIs

## 2.25.0 - 2019-04-18
* [#551](https://github.com/stripe/stripe-python/pull/551) Add support for the `CreditNote` resource and APIs

## 2.24.1 - 2019-04-08
* [#550](https://github.com/stripe/stripe-python/pull/550) Fix encoding of nested parameters in multipart requests

## 2.24.0 - 2019-04-03
* [#543](https://github.com/stripe/stripe-python/pull/543) Add `delete` class method on deletable API resources
* [#547](https://github.com/stripe/stripe-python/pull/547) Add class methods for all custom API requests (e.g. `Charge.capture`)

## 2.23.0 - 2019-03-18
* [#537](https://github.com/stripe/stripe-python/pull/537) Add support for the `PaymentMethod` resource and APIs
* [#540](https://github.com/stripe/stripe-python/pull/540) Add support for retrieving a Checkout `Session`
* [#542](https://github.com/stripe/stripe-python/pull/542) Add support for deleting a Terminal `Location` and `Reader`

## 2.22.0 - 2019-03-14
* [#541](https://github.com/stripe/stripe-python/pull/541) Add `stripe.util.convert_to_dict` method for converting `StripeObject` instances to regular `dict`s

## 2.21.0 - 2019-02-12
* [#532](https://github.com/stripe/stripe-python/pull/532) Add support for subscription schedules

## 2.20.3 - 2019-01-30
* [#530](https://github.com/stripe/stripe-python/pull/530) Fix client telemetry implementation

## 2.20.2 - 2019-01-30
* [#534](https://github.com/stripe/stripe-python/pull/534) Fix session initialization for multi-threaded environments

## 2.20.1 - 2019-01-30
* [#531](https://github.com/stripe/stripe-python/pull/531) Make `RequestsClient` thread-safe

## 2.20.0 - 2019-01-29
* [#526](https://github.com/stripe/stripe-python/pull/526) Reuse the default HTTP client by default

## 2.19.0 - 2019-01-23
* [#524](https://github.com/stripe/stripe-python/pull/524) Rename `CheckoutSession` to `Session` and move it under the `checkout` namespace. This is a breaking change, but we've reached out to affected merchants and all new merchants would use the new approach.

## 2.18.1 - 2019-01-21
* [#525](https://github.com/stripe/stripe-python/pull/525) Properly serialize `individual` on `Account` objects

## 2.18.0 - 2019-01-15
* [#518](https://github.com/stripe/stripe-python/pull/518) Add configurable telemetry to gather information on client-side request latency

## 2.17.0 - 2018-12-21
* [#510](https://github.com/stripe/stripe-python/pull/510) Add support for Checkout sessions

## 2.16.0 - 2018-12-10
* [#507](https://github.com/stripe/stripe-python/pull/507) Add support for account links

## 2.15.0 - 2018-11-30
* [#503](https://github.com/stripe/stripe-python/pull/503) Add support for providing custom CA certificate bundle

## 2.14.0 - 2018-11-28
* [#500](https://github.com/stripe/stripe-python/pull/500) Add support for `Review` for Radar

## 2.13.0 - 2018-11-27
* [#489](https://github.com/stripe/stripe-python/pull/489) Add support for `ValueList` and `ValueListItem` for Radar

## 2.12.1 - 2018-11-22
* [#495](https://github.com/stripe/stripe-python/pull/495) Make `StripeResponse` a new-style class

## 2.12.0 - 2018-11-08
* [#483](https://github.com/stripe/stripe-python/pull/483) Add new API endpoints for the `Invoice` resource.

## 2.11.1 - 2018-11-08
* [#491](https://github.com/stripe/stripe-python/pull/491) Bump minimum requests version to 2.20.0 (for [CVE-2018-18074](https://nvd.nist.gov/vuln/detail/CVE-2018-18074))

## 2.11.0 - 2018-10-30
* [#482](https://github.com/stripe/stripe-python/pull/482) Add support for the `Person` resource
* [#484](https://github.com/stripe/stripe-python/pull/484) Add support for the `WebhookEndpoint` resource

## 2.10.1 - 2018-10-02
* [#481](https://github.com/stripe/stripe-python/pull/481) Correct behavior of `stripe.max_network_retries` if it's reset after initial use

## 2.10.0 - 2018-09-24
* [#478](https://github.com/stripe/stripe-python/pull/478) Add support for Stripe Terminal

## 2.9.0 - 2018-09-24
* [#477](https://github.com/stripe/stripe-python/pull/477) Rename `FileUpload` to `File`

## 2.8.1 - 2018-09-13
* [#474](https://github.com/stripe/stripe-python/pull/474) Don't URL-encode square brackets
* [#473](https://github.com/stripe/stripe-python/pull/473) Integer-index encode all arrays

## 2.8.0 - 2018-09-10
* [#470](https://github.com/stripe/stripe-python/pull/470) Add support for automatic network retries

## 2.7.0 - 2018-09-05
* [#469](https://github.com/stripe/stripe-python/pull/469) Add support for reporting resources

## 2.6.0 - 2018-08-23
* [#467](https://github.com/stripe/stripe-python/pull/467) Add support for usage record summaries

## 2.5.0 - 2018-08-16
* [#463](https://github.com/stripe/stripe-python/pull/463) Remove unsupported Bitcoin endpoints (this is technically a breaking change, but we're releasing as a minor version because none of these APIs were usable anyway)

## 2.4.0 - 2018-08-03
* [#460](https://github.com/stripe/stripe-python/pull/460) Add cancel support for topups
* [#461](https://github.com/stripe/stripe-python/pull/461) Add support for file links

## 2.3.0 - 2018-07-27
* [#456](https://github.com/stripe/stripe-python/pull/456) Add support for Sigma scheduled query run objects

## 2.2.0 - 2018-07-26
* [#455](https://github.com/stripe/stripe-python/pull/455) Add support for Stripe Issuing

## 2.1.0 - 2018-07-25
* [#452](https://github.com/stripe/stripe-python/pull/452) Add `InvoiceLineItem` class

## 2.0.3 - 2018-07-19
* [#450](https://github.com/stripe/stripe-python/pull/450) Internal improvements to `ApiResource.class_url`

## 2.0.2 - 2018-07-18
* [#448](https://github.com/stripe/stripe-python/pull/448) Avoid duplicate dependency on `requests` with Python 2.7

## 2.0.1 - 2018-07-10
* [#445](https://github.com/stripe/stripe-python/pull/445) Fix `setup.py`

## 2.0.0 - 2018-07-10
Major version release. List of backwards incompatible changes to watch out for:
* The minimum Python versions are now 2.7 / 3.4. If you're using Python 2.6 or 3.3, consider upgrading to a more recent version.
* Stripe exception classes should now be accessed via `stripe.error` rather than just `stripe`
* Some older deprecated methods have been removed
* Trying to detach an unattached source will now raise a `stripe.error.InvalidRequestError` exception instead of a `NotImplementedError` exception

For more information, check out the [migration guide for v2](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v2)

Pull requests included in this release:
* [#385](https://github.com/stripe/stripe-python/pull/385) Drop support for Python 2.6 and 3.3
* [#384](https://github.com/stripe/stripe-python/pull/384) Use py.test for tests
* [#399](https://github.com/stripe/stripe-python/pull/399) Remove deprecated code
* [#402](https://github.com/stripe/stripe-python/pull/402) Remove `util.json` and use `json` module directly everywhere
* [#403](https://github.com/stripe/stripe-python/pull/403) Update setup.py and test flow
* [#410](https://github.com/stripe/stripe-python/pull/410) Use pipenv
* [#415](https://github.com/stripe/stripe-python/pull/415) Change exception when detaching unattached sources from `NotImplementedError` to `stripe.error.InvalidRequestError`

## 1.84.2 - 2018-07-06
* [#441](https://github.com/stripe/stripe-python/pull/441) Better (hopefully) fix for serialization of empty `ListObject`s

## 1.84.1 - 2018-07-04
* [#439](https://github.com/stripe/stripe-python/pull/439) Fix serialization of empty `ListObject`s

## 1.84.0 - 2018-06-29
* [#436](https://github.com/stripe/stripe-python/pull/436) Add support for payment intents

## 1.83.0 - 2018-06-28
* [#437](https://github.com/stripe/stripe-python/pull/437) Add support for `partner_id` in `stripe.set_app_info()`

## 1.82.2 - 2018-06-19
* [#365](https://github.com/stripe/stripe-python/pull/365) Add `__repr__` methods to `StripeError` exception classes

## 1.82.1 - 2018-05-14
* [#430](https://github.com/stripe/stripe-python/pull/430) Handle the case where request ID is `None` when formatting errors

## 1.82.0 - 2018-05-13
* [#422](https://github.com/stripe/stripe-python/pull/422) Add `user_mesage` to `StripeError` for a way in Python 3 to avoid the "Request req_...:" string normally appended to error messages

## 1.81.0 - 2018-05-10
* [#425](https://github.com/stripe/stripe-python/pull/425) Add support for issuer fraud records

## 1.80.0 - 2018-04-24
* [#421](https://github.com/stripe/stripe-python/pull/421) Add support for flexible billing and usage records

## 1.79.1 - 2018-02-27
* [#401](https://github.com/stripe/stripe-python/pull/401) Drop conditional dependencies that incorrectly led to an added `simplejson` dependency in Python 3+ after switching to universal wheel

## 1.79.0 - 2018-02-23
* [#397](https://github.com/stripe/stripe-python/pull/397) Build universal wheels by default
* [#398](https://github.com/stripe/stripe-python/pull/398) Add support for `code` attribute on all Stripe exceptions

## 1.78.0 - 2018-02-21
* [#396](https://github.com/stripe/stripe-python/pull/396) Add support for topups

## 1.77.2 - 2018-02-08
* [#394](https://github.com/stripe/stripe-python/pull/394) Make `last_response` available after calling `save()`

## 1.77.1 - 2018-01-12
* [#389](https://github.com/stripe/stripe-python/pull/389) Register unsaved attributes on assignment regardless of new value

## 1.77.0 - 2017-12-21
* [#371](https://github.com/stripe/stripe-python/pull/371) Add accessor `last_response` on `StripeObject` for accessing request ID and other metadata

## 1.76.0 - 2017-12-21
* [#382](https://github.com/stripe/stripe-python/pull/382) Add new `IdempotencyError` type

## 1.75.3 - 2017-12-05
* [#378](https://github.com/stripe/stripe-python/pull/378) Log encoded version of parameters instead of raw POST data

## 1.75.2 - 2017-12-05
* (Accidental no-op release. See 1.75.3.)

## 1.75.1 - 2017-11-29
* [#372](https://github.com/stripe/stripe-python/pull/372) Add only changed values to `_unsaved_values` in `StripeObject`
* [#375](https://github.com/stripe/stripe-python/pull/375) Use a custom JSON encoder to handle `datetime` objects when serializing `StripeObject`s

## 1.75.0 - 2017-11-08
* [#369](https://github.com/stripe/stripe-python/pull/369) Make custom actions on various resources (e.g. `Account.reject`) more consistent with other APIs

## 1.74.0 - 2017-11-07
* [#368](https://github.com/stripe/stripe-python/pull/368) Remove API that allowed the creation of new disputes (this was an erroneous addition; it never worked because the API would not allow it)

## 1.73.0 - 2017-11-02
* [#364](https://github.com/stripe/stripe-python/pull/364) Switch to vendored version of the `six` package for compatibility between Python 2 and 3

## 1.72.0 - 2017-10-31
* [#361](https://github.com/stripe/stripe-python/pull/361) Support for exchange rates APIs

## 1.71.2 - 2017-10-31
* [#362](https://github.com/stripe/stripe-python/pull/362) Fix balance transaction and invoice item conversion into `StripeObject`s

## 1.71.1 - 2017-10-27
* [#360](https://github.com/stripe/stripe-python/pull/360) Fix `BytesWarning` being issued on logging in Python 3

## 1.71.0 - 2017-10-26
* [#359](https://github.com/stripe/stripe-python/pull/359) Support for listing source transactions

## 1.70.0 - 2017-10-23
* [#356](https://github.com/stripe/stripe-python/pull/356) Support uploading files with `StringIO` in addition to a file on disk

## 1.69.0 - 2017-10-20
* [#351](https://github.com/stripe/stripe-python/pull/351) Break resource.py module into separate ones for each type of resource
    * Classes are still into resource.py for backwards compatibility
* [#353](https://github.com/stripe/stripe-python/pull/353) Fix unpickling `StripeObject` in Python 3

## 1.68.0 - 2017-10-19
* [#350](https://github.com/stripe/stripe-python/pull/350) Add static methods to manipulate resources from parent
    * `Account` gains methods for external accounts and login links (e.g. `.create_account`, `create_login_link`)
    * `ApplicationFee` gains methods for refunds
    * `Customer` gains methods for sources
    * `Transfer` gains methods for reversals

## 1.67.0 - 2017-10-11
* [#349](https://github.com/stripe/stripe-python/pull/349) Rename source `delete` to `detach` (and deprecate the former)

## 1.66.0 - 2017-09-29
* Support length reads on list objects

## 1.65.1 - 2017-09-21
* Handle `bytearray` and `bytes` (in addition to string) in `Webhook.construct_event`

## 1.65.0 - 2017-09-07
* Add support for passing a `stripe_version` argument to all API requests

## 1.64.0 - 2017-09-01
* Error when an invalid type (i.e. non-string) passed as an API method argument

## 1.63.1 - 2017-09-01
* Fix serialization of `items` on Relay order creation and order return

## 1.63.0 - 2017-08-29
* Add support for `InvalidClientError` OAuth error

## 1.62.1 - 2017-08-07
* Change serialization of subscription items on update to encoded as an integer-indexed map

## 1.62.0 - 2017-06-27
* `pay` on invoice can now take parameter

## 1.61.0 - 2017-06-24
* Expose `code` on `InvalidRequestError`

## 1.60.0 - 2017-06-19
* Add support for ephemeral keys

## 1.59.0 - 2017-06-07
* Refactor OAuth implementation to have dedicated classes for errors

## 1.58.0 - 2017-06-02
* Re-use connections with Pycurl

## 1.57.1 - 2017-05-31
* Fix the pycurl client

## 1.57.0 - 2017-05-26
* Add `api_key` parameter to webhook's `construct_event`

## 1.56.0 - 2017-05-25
* Add support for account login links

## 1.55.2 - 2017-05-11
* Remove Requests constraint from 1.55.1 now that they've patched (as of 2.14.2)

## 1.55.1 - 2017-05-10
* Constrain Requests to < 2.13.0 if on setuptools < 18.0.0

## 1.55.0 - 2017-04-28
* Support for checking webhook signatures

## 1.54.0 - 2017-04-28
* Add `stripe.set_app_info` for use by plugin creators

## 1.53.0 - 2017-04-06
* Add support for payouts and recipient transfers

## 1.52.0 - 2017-04-06
* No-op release: peg test suite to a specific API version

## 1.51.0 - 2017-03-20
* Support OAuth operations (getting a token and deauthorizing)

## 1.50.0 - 2017-03-17
* Support for detaching sources from customers

## 1.49.0 - 2017-03-13
* Accept `session` argument for `RequestsClient`

## 1.48.1 - 2017-02-21
* Fix encoding of parameters when fetching upcoming invoices

## 1.48.0 - 2017-02-21
* Add `Account.modify_external_account` to modify an account in one API call
* Add `Customer.modify_source` to modify a source in one API call

## 1.47.0 - 2017-01-18
* Allow sources to be updated

## 1.46.0 - 2017-01-06
* Use internal session for Requests for connection pooling

## 1.45.0 - 2017-01-06
* request logging goes to stderr now
* Logs properly handle unicode
* Format is now the same between logging logs, and console logs

## 1.44.0 - 2016-12-16
* Add request logging and some mechanisms to enable it when debugging

## 1.43.0 - 2016-11-30
* Add support for verifying sources

## 1.42.0 - 2016-11-21
* Add retrieve method for 3-D Secure resources

## 1.41.1 - 2016-10-26
* Implement __copy__ and __deepcopy__ on StripeObject to fix these operations

## 1.41.0 - 2016-10-12
* Add `Source` model for generic payment sources

## 1.40.1 - 2016-10-10
* Return subscription model instance on subscription create/modify

## 1.40.0 - 2016-10-07
* Add configurable timeout for Requests HTTP library

## 1.39.0 - 2016-10-06
* Add support for subscription items
* Add proxy support for pycurl, Requests, urlfetch, and urllib2 libraries

## 1.38.0 - 2016-09-15
* Add support for Apple Pay domains

## 1.37.0 - 2016-07-12
* Add `ThreeDSecure` model for 3-D secure payments

## 1.36.0 - 2016-06-29
* Add `update` class method to resources that can be updated

## 1.35.0 - 2016-05-24
* Add support for returning Relay orders

## 1.34.0 - 2016-05-20
* Add support for Alipay accounts

## 1.33.0 - 2016-05-04
* Add support for the new `/v1/subscriptions` endpoint
  * `stripe.Subscription.retrieve`
  * `stripe.Subscription.update`
  * `stripe.Subscription.create`
  * `stripe.Subscription.list`

## 1.32.2 - 2016-04-12
* Fix bug where file uploads could not be properly listed

## 1.32.1 - 2016-04-11
* Fix bug where request parameters were not passed between pages with `auto_paging_iter`

## 1.32.0 - 2016-03-31
* Update CA cert bundle for compatibility with OpenSSL versions below 1.0.1

## 1.31.1 - 2016-03-24
* Fix uploading of binary files in Python 3

## 1.31.0 - 2016-03-15
* Add `reject` on `Account` to support the new API feature

## 1.30.0 - 2016-02-27
* Add `CountrySpec` model for looking up country payment information

## 1.29.1 - 2016-02-01
* Update bundled CA certs

## 1.29.0 - 2016-01-26
* Add support for deleting Relay products and SKUs

## 1.28.0 - 2016-01-04
* Add an automatic paginating iterator to lists available via `auto_paging_iter`
* List objects are now iterable
* Error messages set to `None` are now handled properly
* The `all` method on list objects has been deprecated in favor of `list`
* Calls to `instance_url` are now side effect free

## 1.27.1 - 2015-10-02
* Official Python 3.4 & 3.5 compatibility
* Add configurable HTTP client
* Add ability to delete attributes

## 1.27.0 - 2015-09-14
* Products, SKUs, Orders resources

## 1.26.0 - 2015-09-11
* Add support for new 429 rate limit response

## 1.25.0 - 2015-08-17
* Added refund listing, creation and retrieval

## 1.24.1 - 2015-08-05
* Fix error handling for Python 2.6

## 1.24.0 - 2015-08-03
* Managed accounts can now be deleted
* Added dispute listing and retrieval

## 1.23.0 - 2015-07-06
* Include response headers in exceptions

## 1.22.3 - 2015-06-04
* Fix saving `additional_owners` on managed accounts

## 1.22.2 - 2015-04-08
* Fix saving manage accounts

## 1.22.1 - 2015-03-30
* Pass `stripe_account` to Balance.retrieve

## 1.22.0 - 2015-03-22
* Added methods for updating and saving arrays of objects

## 1.21.0 - 2015-02-19
* Added Bitcoin Receiver update and delete methods

## 1.20.2 - 2015-01-21
* Remove support for top-level bitcoin transactions

## 1.20.1 - 2015-01-07
* Adding bitcoin receiver and transaction objects

## 1.20.0 - 2014-12-23
* Adding support for file uploads resource

## 1.19.1 - 2014-10-23
* Remove redundant manual SSL blacklist preflight check

## 1.19.0 - 2014-07-26
* Application Fee refunds now a list instead of array

## 1.18.0 - 2014-06-17
* Add metadata for disputes and refunds

## 1.17.0 - 2014-06-10
* Remove official support for Python 2.5

## 1.16.0 - 2014-05-28
* Support for canceling transfers

## 1.15.1 - 2014-05-21
* Support cards for recipients.

## 1.14.1 - 2014-05-19
* Disable loading the ssl module on the Google App Engine dev server.

## 1.14.0 - 2014-04-09
* Use DER encoded certificate for checksumming
* Don't rely on SNI support in integration tests

## 1.13.0 - 2014-04-09
* Update bundled ca-certificates
* Add certificate blacklist for CVE-2014-0160 mitigation

## 1.12.2 - 2014-03-13
* Fix syntax errors in setup.py metadata

## 1.12.1 - 2014-03-13
* Added license and other metadata in setup.py
* Fix `__repr__` in Python 3
* Support pickling of responses

## 1.12.0 - 2014-01-29
* Added support for multiple subscriptions per customer

## 1.11.0 - 2013-12-05
* Added extensive unit tests
* Extended functional test coverage
* Refactored code into modules and out of stripe/__init__.py
* Abstracted http library selection and use from the `APIRequestor` into `stripe.http_client`
* Refactored `StripeObject` to inherit from `dict` and avoid direct access of `__dict__`.
* PEP8ified the codebase and enforced with a test.
* Proper encoding of timezone aware datetimes

## 1.10.8 - 2013-12-02
* Add stripe.ApplicationFee resource

## 1.9.8 - 2013-10-17
* Removed incorrect test.

## 1.9.7 - 2013-10-10
* Add support for metadata.

## 1.9.6 - 2013-10-08
* Fix issue with support for closing disputes.

## 1.9.5 - 2013-09-18
* Add support for closing disputes.

## 1.9.4 - 2013-08-13
* Add stripe.Balance and stripe.BalanceTransaction resources

## 1.9.3 - 2013-08-12
* Add support for unsetting attributes by setting to None.
  Setting properties to a blank string is now an error.

## 1.9.2 - 2013-07-12
* Add support for multiple cards API

## 1.9.1 - 2013-05-03
* Remove 'id' from the list of permanent attributes

## 1.9.0 - 2013-04-25
* Support for Python 3 (github issue #32)

## 1.8.0 - 2013-04-11
* Allow transfers to be creatable
* Add new stripe.Recipient resource

## 1.7.10 - 2013-02-21
* Add 'id' to the list of permanent attributes

## 1.7.9 - 2013-02-01
* Add support for passing options when retrieving Stripe objects; e.g., stripe.Charge.retrieve("foo", params={"expand":["customer"]})

## 1.7.8 - 2013-01-15
* Add support for setting a Stripe API version override

## 1.7.7 - 2012-12-18
* Update requests version check to work with requests 1.x.x (github issue #24)

## 1.7.6 - 2012-11-08
* Add support for updating charge disputes

## 1.7.5 - 2012-10-30
* Add support for creating invoices
* Add support for new invoice lines return format
* Add support for new List objects

## 1.7.4 - 2012-08-31
* Add update and pay methods for Invoice resource

## 1.7.3 - 2012-08-15
* Add new stripe.Account resource
* Remove uncaptured_charge tests (this has been deprecated from the API).

## 1.7.2 - 2012-05-31
* Fix a bug that would cause nested objects to be mis-rendered in __str__ and __repr__ methods (github issues #17, #18)

## 1.7.1 - 2012-05-21
* Prefer App Engine's urlfetch over requests, as that's the only thing that will work in App Engine's environment. Previously, if requests was available in the App Engine environment, we would attempt to use it.

## 1.7.0 - 2012-05-17
* Add new delete_discount method to stripe.Customer
* Add new stripe.Transfer resource
* Switch from using HTTP Basic auth to Bearer auth. (Note: Stripe will support Basic auth for the indefinite future, but recommends Bearer auth when possible going forward)
* Numerous test suite improvements

## 1.6.1 - 2011-09-14
* Parameters with value None are no longer included in API requests

