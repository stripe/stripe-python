## 11.3.0 - 2024-11-20
* [#1424](https://github.com/stripe/stripe-python/pull/1424) This release changes the pinned API version to `2024-11-20.acacia`.
  * Add support for `authorizer` on parameter classes `stripe.Account.CreatePersonParamsRelationship`, `stripe.Account.ListPersonsParamsRelationship`, `stripe.Account.ModifyPersonParamsRelationship`, `stripe.Account.PersonsParamsRelationship`, and `stripe.Token.CreateParamsPersonRelationship` and resource class `stripe.Person.Relationship`
  * Add support for `account_holder_address`, `account_holder_name`, `account_type` and `bank_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Aba`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Swift`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Aba`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Swift`
  * Add support for `submit_type` on parameter class `stripe.PaymentLink.ModifyParams`
  * Add support for `trace_id` on resource `stripe.Payout`
  * Add support for `network_decline_code` on resource classes `stripe.Refund.DestinationDetails.Blik` and `stripe.Refund.DestinationDetails.Swish`
  * Add support for `adaptive_pricing` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
  * Add support for `mandate_options` on parameter classes `stripe.checkout.Session.CreateParamsPaymentMethodOptionsBacsDebit` and `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSepaDebit` and resource classes `stripe.checkout.Session.PaymentMethodOptions.BacsDebit` and `stripe.checkout.Session.PaymentMethodOptions.SepaDebit`
  * Add support for `request_extended_authorization`, `request_incremental_authorization`, `request_multicapture` and `request_overcapture` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `capture_method` on parameter classes `stripe.checkout.Session.CreateParamsPaymentMethodOptionsKakaoPay`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsKrCard`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsNaverPay`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsPayco`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSamsungPay`
  * Add support for `merchant_amount` and `merchant_currency` on parameter class `stripe.issuing.Authorization.CreateParams`
  * Add support for `fraud_challenges`, `verified_by_fraud_challenge` and `respond` on resource `stripe.issuing.Authorization`
  * Change type of `disabled_reason` on  `stripe.Account.FutureRequirements` and `stripe.Account.Requirements` from `str` to `Literal['action_required.requested_capabilities', 'listed', 'other', 'platform_paused', 'rejected.fraud', 'rejected.incomplete_verification', 'rejected.listed', 'rejected.other', 'rejected.platform_fraud', 'rejected.platform_other', 'rejected.platform_terms_of_service', 'rejected.terms_of_service', 'requirements.past_due', 'requirements.pending_verification', 'under_review']`
  * Change type of `disable_stripe_user_authentication` on  `stripe.AccountSession.Components.AccountManagement.Features`, `stripe.AccountSession.Components.AccountOnboarding.Features`, `stripe.AccountSession.Components.Balances.Features`, `stripe.AccountSession.Components.NotificationBanner.Features`, and `stripe.AccountSession.Components.Payouts.Features` from `Optional[bool]` to `bool`
  * Add support for `subscribe` on enums `stripe.checkout.Session.submit_type`, `stripe.checkout.Session.CreateParams.submit_type`, `stripe.PaymentLink.submit_type`, and `stripe.PaymentLink.CreateParams.submit_type`
  * Add support for `li_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `financial_account_statement` on enums `stripe.File.purpose` and `stripe.File.ListParams.purpose`
  * Add support for `service_tax` on enums `stripe.Invoice.AddLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.Invoice.UpdateLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`, `stripe.tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.CalculationLineItem.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.TaxRate.tax_type`, `stripe.TaxRate.CreateParams.tax_type`, and `stripe.TaxRate.ModifyParams.tax_type`
  * Add support for `link` on enums `stripe.PaymentIntent.PaymentMethodOptions.Card.network`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.PaymentMethodOptions.Card.network`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.Card.network`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard.network`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard.network`
  * Add support for `2024-11-20.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
  * Change type of `amount` on  `stripe.issuing.Authorization.CreateParams` from `int` to `NotRequired[int]`
  * Change type of `origin_payment_method` on  `stripe.treasury.InboundTransfer` from `str` to `Optional[str]`

## 11.2.0 - 2024-10-29
* [#1411](https://github.com/stripe/stripe-python/pull/1411) This release changes the pinned API version to `2024-10-28.acacia`.
  * Add support for resource `stripe.v2.EventDestinations`
  * Add support for `create`, `retrieve`, `update`, `list`, `delete`, `disable`, `enable` and `ping` methods on resource `V2.EventDestinations`
  * Add support for `alma_payments`, `kakao_pay_payments`, `kr_card_payments`, `naver_pay_payments`, `payco_payments`, `samsung_pay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `groups` on parameter class `stripe.Account.CreateParams` and resource `stripe.Account`
  * Add support for `disable_stripe_user_authentication` on resource classes `stripe.AccountSession.Components.AccountManagement.Features`, `stripe.AccountSession.Components.AccountOnboarding.Features`, `stripe.AccountSession.Components.Balances.Features`, `stripe.AccountSession.Components.NotificationBanner.Features`, and `stripe.AccountSession.Components.Payouts.Features` and parameter classes `stripe.AccountSession.CreateParamsComponentsAccountManagementFeatures`, `stripe.AccountSession.CreateParamsComponentsAccountOnboardingFeatures`, `stripe.AccountSession.CreateParamsComponentsBalancesFeatures`, `stripe.AccountSession.CreateParamsComponentsNotificationBannerFeatures`, and `stripe.AccountSession.CreateParamsComponentsPayoutsFeatures`
  * Add support for `alma` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, and `stripe.Refund.DestinationDetails`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `kakao_pay`, `kr_card` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.Mandate.PaymentMethodDetails`, `stripe.PaymentIntent.PaymentMethodOptions`, `stripe.SetupAttempt.PaymentMethodDetails`, and `stripe.checkout.Session.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resource `stripe.PaymentMethod`
  * Add support for `naver_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, and `stripe.checkout.Session.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resource `stripe.PaymentMethod`
  * Add support for `payco`, `samsung_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, and `stripe.checkout.Session.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resource `stripe.PaymentMethod`
  * Add support for `enhanced_evidence` on resource class `stripe.Dispute.Evidence` and parameter class `stripe.Dispute.ModifyParamsEvidence`
  * Add support for `enhanced_eligibility` on resource class `stripe.Dispute.EvidenceDetails`
  * Add support for `enhanced_eligibility_types` on resource `stripe.Dispute`
  * Add support for `automatically_finalizes_at` on parameter classes `stripe.Invoice.CreateParams` and `stripe.Invoice.ModifyParams`
  * Add support for `amazon_pay` on resource `stripe.PaymentMethodDomain`
  * Add support for `flat_amount`, `rate_type` on resource `stripe.TaxRate` and resource class `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails`
  * Add support for `schedule_at_period_end` on parameter classes `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionUpdate` and resource class `stripe.billing_portal.Configuration.Features.SubscriptionUpdate`
  * Add support for `metadata` on parameter class `stripe.forwarding.Request.CreateParams` and resource `stripe.forwarding.Request`
  * Add support for `_cls_submit_card` on resource `stripe.issuing.Card`
  * Add support for `submit_card` on resource `stripe.issuing.Card`
  * Add support for `by`, `cr`, `ec`, `ma`, `md`, `rs`, `ru`, `tz`, `uz` on resource class `stripe.tax.Registration.CountryOptions` and parameter class `stripe.tax.Registration.CreateParamsCountryOptions`
  * Add support for `pln` on parameter classes `stripe.terminal.Configuration.CreateParamsTipping` and `stripe.terminal.Configuration.ModifyParamsTipping` and resource class `stripe.terminal.Configuration.Tipping`
  * Change type of `business_profile` on  `stripe.billing_portal.Configuration.CreateParams` from `Configuration.CreateParamsBusinessProfile` to `NotRequired[Configuration.CreateParamsBusinessProfile]`
  * Add support for `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `alma`, `kakao_pay`, `kr_card`, `naver_pay`, `payco` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `samsung_pay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `auto` on enum `stripe.Customer.ModifyParamsTax.validate_location`
  * Add support for `issuing_transaction.purchase_details_receipt_updated`, `refund.failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `jp_credit_transfer` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `retail_delivery_fee` on enums `stripe.Invoice.AddLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.Invoice.UpdateLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`, `stripe.tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.CalculationLineItem.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.TaxRate.tax_type`, `stripe.TaxRate.CreateParams.tax_type`, and `stripe.TaxRate.ModifyParams.tax_type`
  * Add support for `state_retail_delivery_fee` on enums `stripe.tax.Registration.CountryOptions.Us.type` and `stripe.tax.Registration.CreateParamsCountryOptionsUs.type`
  * Add support for `2024-10-28.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`

## 11.1.1 - 2024-10-18
* [#1414](https://github.com/stripe/stripe-python/pull/1414) Deserialize into correct v2 EventData types
  * Fixes a bug where v2 EventData was not being deserialized into the appropriate type for `V1BillingMeterErrorReportTriggeredEvent` and `V1BillingMeterNoMeterFoundEvent`
* [#1415](https://github.com/stripe/stripe-python/pull/1415) update object tags for meter-related classes

  - fixes a bug where the `object` property of the `MeterEvent`, `MeterEventAdjustment`, and `MeterEventSession` didn't match the server.
* [#1412](https://github.com/stripe/stripe-python/pull/1412) Clean up examples

## 11.1.0 - 2024-10-03
* [#1409](https://github.com/stripe/stripe-python/pull/1409) Update the class for `ThinEvent` to include `livemode`
* [#1408](https://github.com/stripe/stripe-python/pull/1408) Update generated code
  * Remove the support for resource `Margin` that was accidentally made public in the last release

## 11.0.0 - 2024-10-01
* [#1404](https://github.com/stripe/stripe-python/pull/1404) Support for APIs in the new API version 2024-09-30.acacia

  This release changes the pinned API version to `2024-09-30.acacia`. Please read the [API Upgrade Guide](https://stripe.com/docs/upgrades#2024-09-30.acacia) and carefully review the API changes before upgrading.

  ### ⚠️ Breaking changes due to changes in the API


  * Rename for `usage_threshold_config` to `usage_threshold` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`
  * Remove support for `filter` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`. Use the filters on the `usage_threshold` instead
  * * Remove support for `customer_consent_collected` on parameter class `stripe.terminal.Reader.ProcessSetupIntentParams`

  ### ⚠️ Other Breaking changes in the SDK
  * Adjusted default values for HTTP requests. You can use the old defaults by setting them explicitly. New values are:
    - max retries: `0` -> `2`
    - max timeout (seconds): `2` -> `5`
  * Add method `parse_thin_event()` on the `StripeClient` class to parse [thin events](https://docs.corp.stripe.com/event-destinations#events-overview).  Rename `construct_event()` method on the same class to `parse_snapshot_event()` to clearly distinguish between the two kinds of events.

  ### Additions

  * Add support for `custom_unit_amount` on parameter class `stripe.Product.CreateParamsDefaultPriceData`
  * Add support for `usage_threshold` on parameter class `stripe.billing.Alert.CreateParams` and resource `stripe.billing.Alert`
  * Add support for `allow_redisplay` on parameter classes `stripe.terminal.Reader.ProcessPaymentIntentParamsProcessConfig` and `stripe.terminal.Reader.ProcessSetupIntentParams`
  * Add support for `international_transaction` on enum `stripe.treasury.ReceivedCredit.failure_code`
  * Add support for `2024-09-30.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`
  * Add support for new Usage Billing APIs `stripe.v2.billing.MeterEvent`, `stripe.v2.billing.MeterEventAdjustments`, `stripe.v2.billing.MeterEventSession`, `stripe.v2.billing.MeterEventStream` and the new Events API `stripe.v2.core.Events` under the [v2 namespace ](https://docs.corp.stripe.com/api-v2-overview)
  * Add method [rawRequest()](https://github.com/stripe/stripe-python/tree/master?tab=readme-ov-file#custom-requests) on the `StripeClient` class that takes a HTTP method type, url and relevant parameters to make requests to the Stripe API that are not yet supported in the SDK.

  ### Other changes
  * Change type of `default_allowed_updates` on  `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` from `Union[Literal[''], List[Literal['price', 'promotion_code', 'quantity']]]` to `NotRequired[Literal['']|List[Literal['price', 'promotion_code', 'quantity']]]`
  * Change type of `products` on  `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` from `Union[Literal[''], List[Configuration.CreateParamsFeaturesSubscriptionUpdateProduct]]` to `NotRequired[Literal['']|List[Configuration.CreateParamsFeaturesSubscriptionUpdateProduct]]`


## 10.12.0 - 2024-09-18
* [#1394](https://github.com/stripe/stripe-python/pull/1394) Update generated code
  * Add support for `international_transaction` on enum `stripe.treasury.ReceivedDebit.failure_code`
* [#1393](https://github.com/stripe/stripe-python/pull/1393) Update generated code
  * Add support for `payer_details` on resource class `stripe.Charge.PaymentMethodDetails.Klarna`
  * Add support for `amazon_pay` on resource class `stripe.Dispute.PaymentMethodDetails`
  * Add support for `automatically_finalizes_at` on resource `stripe.Invoice`
  * Add support for `state_sales_tax` on resource class `stripe.tax.Registration.CountryOptions.Us` and parameter class `stripe.tax.Registration.CreateParamsCountryOptionsUs`
  * Add support for `verification_supportability` on enums `stripe.Account.FutureRequirements.Error.code`, `stripe.Account.Requirements.Error.code`, `stripe.BankAccount.FutureRequirements.Error.code`, `stripe.BankAccount.Requirements.Error.code`, `stripe.Capability.FutureRequirements.Error.code`, `stripe.Capability.Requirements.Error.code`, `stripe.Person.FutureRequirements.Error.code`, and `stripe.Person.Requirements.Error.code`
  * Add support for `amazon_pay` on enum `stripe.Dispute.PaymentMethodDetails.type`
  * Add support for `terminal_reader_invalid_location_for_activation` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 10.11.0 - 2024-09-12
* [#1391](https://github.com/stripe/stripe-python/pull/1391) Update generated code
  * Add support for `template` on parameter classes `stripe.Customer.CreateParamsInvoiceSettingsRenderingOptions`, `stripe.Customer.ModifyParamsInvoiceSettingsRenderingOptions`, `stripe.Invoice.CreateParamsRendering`, and `stripe.Invoice.ModifyParamsRendering` and resource classes `stripe.Customer.InvoiceSettings.RenderingOptions` and `stripe.Invoice.Rendering`
  * Add support for resource `stripe.InvoiceRenderingTemplate`
  * Add support for `required` on parameter classes `stripe.PaymentLink.CreateParamsTaxIdCollection`, `stripe.PaymentLink.ModifyParamsTaxIdCollection`, and `stripe.checkout.Session.CreateParamsTaxIdCollection` and resource classes `stripe.PaymentLink.TaxIdCollection` and `stripe.checkout.Session.TaxIdCollection`
  * Add support for `submitted` on enum `stripe.issuing.Card.Shipping.status`
  * Change type of `tax_amounts` on  `stripe.InvoiceLineItem` from `Optional[List[TaxAmount]]` to `List[TaxAmount]`
  * Change type of `tax_rates` on  `stripe.InvoiceLineItem` from `Optional[List[TaxRate]]` to `List[TaxRate]`
  * Change type of `status_details` on  `stripe.test_helpers.TestClock` from `Optional[StatusDetails]` to `StatusDetails`

## 10.10.0 - 2024-09-05
* [#1376](https://github.com/stripe/stripe-python/pull/1376) Update generated code
  * Add support for `subscription` on parameter class `stripe.billing.Alert.CreateParamsFilter`
  * Change type of `customer_consent_collected` on  `stripe.terminal.Reader.ProcessSetupIntentParams` from `bool` to `NotRequired[bool]`

## 10.9.0 - 2024-08-29
* [#1385](https://github.com/stripe/stripe-python/pull/1385) Generate SDK for OpenAPI spec version 1230
  * Add support for `status_details` on resource `stripe.test_helpers.TestClock`
  * Change type of `fields` on  `stripe.AccountLink.CreateParamsCollectionOptions` from `Literal['currently_due', 'eventually_due']` to `NotRequired[Literal['currently_due', 'eventually_due']]`
  * Add support for `hr_oib` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `issuing_regulatory_reporting` on enums `stripe.File.purpose`, `stripe.File.CreateParams.purpose`, and `stripe.File.ListParams.purpose`

## 10.8.0 - 2024-08-15
* [#1373](https://github.com/stripe/stripe-python/pull/1373) Update generated code
  * Add support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`
  * Add support for `wallet` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.CardPresent`
  * Add support for `mandate_options` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsBacsDebit`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsBacsDebit`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsBacsDebit` and resource class `stripe.PaymentIntent.PaymentMethodOptions.BacsDebit`
  * Add support for `bacs_debit` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
  * Add support for `chips` on resource classes `stripe.treasury.OutboundPayment.TrackingDetails.UsDomesticWire` and `stripe.treasury.OutboundTransfer.TrackingDetails.UsDomesticWire` and parameter classes `stripe.treasury.OutboundPayment.UpdateParamsTrackingDetailsUsDomesticWire` and `stripe.treasury.OutboundTransfer.UpdateParamsTrackingDetailsUsDomesticWire`
  * Change type of `imad` on  `stripe.treasury.OutboundPayment.TrackingDetails.UsDomesticWire` and `stripe.treasury.OutboundTransfer.TrackingDetails.UsDomesticWire` from `str` to `Optional[str]`

## 10.7.0 - 2024-08-08
* [#1371](https://github.com/stripe/stripe-python/pull/1371) Update generated code
  * Add support for `type` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent.Offline`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent.Offline`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent.Offline`, and `stripe.SetupAttempt.PaymentMethodDetails.CardPresent.Offline`
  * Add support for `offline` on resource classes `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent` and `stripe.PaymentMethod.CardPresent`
  * Add support for `_cls_activate` on resource `stripe.billing.Alert`
  * Add support for `_cls_archive` on resource `stripe.billing.Alert`
  * Add support for `_cls_deactivate` on resource `stripe.billing.Alert`
  * Add support for `activate` on resource `stripe.billing.Alert`
  * Add support for `archive` on resource `stripe.billing.Alert`
  * Add support for `create` on resource `stripe.billing.Alert`
  * Add support for `deactivate` on resource `stripe.billing.Alert`
  * Add support for `list` on resource `stripe.billing.Alert`
  * Add support for `retrieve` on resources `stripe.billing.Alert` and `stripe.tax.Calculation`
  * Add support for `related_customer` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ListParams` and resource `stripe.identity.VerificationSession`
  * Add support for `invalid_mandate_reference_prefix_format` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `girocard` on enums `stripe.PaymentIntent.PaymentMethodOptions.Card.network`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.PaymentMethodOptions.Card.network`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.Card.network`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard.network`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard.network`
  * Add support for `financial_addresses.aba.forwarding` on enums `stripe.treasury.FinancialAccount.active_features`, `stripe.treasury.FinancialAccount.pending_features`, and `stripe.treasury.FinancialAccount.restricted_features`
  * Change type of `count` on  `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan` from `int` to `NotRequired[int]`
  * Change type of `interval` on  `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan` from `Literal['month']` to `NotRequired[Literal['month']]`
  * Change type of `account` on  `stripe.Person.AdditionalTosAcceptances` from `Account` to `Optional[Account]`

## 10.6.0 - 2024-08-01
* [#1369](https://github.com/stripe/stripe-python/pull/1369) Update generated code
  * Add support for resource `stripe.billing.Alert`
  * ⚠️ Remove support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`. This was accidentally released last week.
  * Add support for `billing.alert.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `charge_exceeds_transaction_limit` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 10.5.0 - 2024-07-25
* [#1368](https://github.com/stripe/stripe-python/pull/1368) Update generated code
  * Add support for `tax_registrations` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `tax_settings` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
* [#1364](https://github.com/stripe/stripe-python/pull/1364) Update generated code
  * Add support for `transaction_id` on resource class `stripe.Charge.PaymentMethodDetails.Affirm`
  * Add support for `buyer_id` on resource class `stripe.Charge.PaymentMethodDetails.Blik`
  * Add support for `authorization_code` on resource class `stripe.Charge.PaymentMethodDetails.Card`
  * Add support for `brand_product` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.CardPresent`
  * Add support for `network_transaction_id` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.Charge.PaymentMethodDetails.InteracPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`, and `stripe.PaymentMethod.Card.GeneratedFrom.PaymentMethodDetails.CardPresent`
  * Add support for `case_type` on resource class `stripe.Dispute.PaymentMethodDetails.Card`
  * Add support for `twint` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `modify` on resource `stripe.checkout.Session`
  * Add support for `invoice.overdue` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `invoice.will_be_due` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`

## 10.4.0 - 2024-07-18
* [#1362](https://github.com/stripe/stripe-python/pull/1362) Update generated code
  * Add support for `customer` on resource class `stripe.ConfirmationToken.PaymentMethodPreview`
  * Add support for `issuing_dispute.funds_rescinded` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `multibanco` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `stripe_s700` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
* [#1360](https://github.com/stripe/stripe-python/pull/1360) Update changelog

## 10.3.0 - 2024-07-11
* [#1358](https://github.com/stripe/stripe-python/pull/1358) Update generated code
  * Add support for `payment_method_options` on resource `stripe.ConfirmationToken`
  * Add support for `payment_element` on resource class `stripe.CustomerSession.Components` and parameter class `stripe.CustomerSession.CreateParamsComponents`
  * Add support for `address_validation` on parameter class `stripe.issuing.Card.CreateParamsShipping` and resource class `stripe.issuing.Card.Shipping`
  * Add support for `shipping` on parameter class `stripe.issuing.Card.ModifyParams`
  * ⚠️ Remove support for `billing_policy_remote_function_response_invalid`, `billing_policy_remote_function_timeout`, `billing_policy_remote_function_unexpected_status_code`, and `billing_policy_remote_function_unreachable` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * ⚠️ Remove support for `payment_intent_fx_quote_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`. The property was mistakenly released last week.
  * [#1357](https://github.com/stripe/stripe-python/pull/1357) don't auto-organize imports

## 10.2.0 - 2024-07-05
* [#1354](https://github.com/stripe/stripe-python/pull/1354) Update generated code
  * Add support for `_cls_add_lines`, `_cls_remove_lines`, `_cls_update_lines`, `add_lines`, `remove_lines`, `update_lines` on resource `stripe.Invoice`
  * Add support for `posted_at` on parameter class `stripe.tax.Transaction.CreateFromCalculationParams` and resource `stripe.tax.Transaction`
  * Add support for `payment_intent_fx_quote_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 10.1.0 - 2024-06-27
* [#1353](https://github.com/stripe/stripe-python/pull/1353) Update generated code
  * Add support for `email_type` on parameter classes `stripe.CreditNote.CreateParams`, `stripe.CreditNote.PreviewLinesParams`, and `stripe.CreditNote.PreviewParams`
  * Add support for `filters` on parameter classes `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections` and resource classes `stripe.Invoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.PaymentIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.SetupIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`, and `stripe.checkout.Session.PaymentMethodOptions.UsBankAccount.FinancialConnections`
  * Add support for `account_subcategories` on parameter class `stripe.financial_connections.Session.CreateParamsFilters` and resource class `stripe.financial_connections.Session.Filters`
  * Add support for `reboot_window` on parameter classes `stripe.terminal.Configuration.CreateParams` and `stripe.terminal.Configuration.ModifyParams` and resource `stripe.terminal.Configuration`
  * Add support for `day` on enum `stripe.billing.Meter.ListEventSummariesParams.value_grouping_window`
  * Add support for `multibanco` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
  * Add support for `twint` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
  * Add support for `zip` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`

## 10.0.0 - 2024-06-24
* [#1350](https://github.com/stripe/stripe-python/pull/1350) Update generated code

  This release changes the pinned API version to 2024-06-20. Please read the [API Upgrade Guide](https://stripe.com/docs/upgrades#2024-06-20) and carefully review the API changes before upgrading.

  ### ⚠️ Breaking changes

    * Remove the unused resource `PlatformTaxFee`
    * Rename `volume_decimal` to `quantity_decimal` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`

  ### Additions

  * Add support for `fleet` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetails`, `stripe.issuing.Authorization.CreateParams`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetails`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetails`, resource `stripe.issuing.Authorization`, and resource class `stripe.issuing.Transaction.PurchaseDetails`
  * Add support for new values `platform_disabled`, `paused.inactivity` and `other` on enums `Capability.Requirements.disabled_reason` and `Capability.FutureRequirements.disabled_reason`
  * Add support for `industry_product_code` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`
  * Add support for `quantity_decimal` on parameter classes `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel` and resource class `stripe.issuing.Transaction.PurchaseDetails.Fuel`
  * Add support for `fuel` on parameter class `stripe.issuing.Authorization.CreateParams` and resource `stripe.issuing.Authorization`
  * Add support for `_cls_finalize_amount` on resource `stripe.issuing.Authorization`
  * Add support for `finalize_amount` on resource `stripe.issuing.Authorization`
  * Change type of `disabled_reason` on  `stripe.Capability.FutureRequirements` and `stripe.Capability.Requirements` from `str` to `Literal['other', 'paused.inactivity', 'pending.onboarding', 'pending.review', 'platform_disabled', 'platform_paused', 'rejected.inactivity', 'rejected.other', 'rejected.unsupported_business', 'requirements.fields_needed']`
  * Add support for `ch_uid` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `card_canceled`, `card_expired`,  `cardholder_blocked`, `insecure_authorization_method` and `pin_blocked`  on enum `stripe.issuing.Authorization.RequestHistory.reason`
  * Add support for `charging_minute`, `imperial_gallon`, `kilogram`,  `kilowatt_hour`, `pound`, on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`
  * Add support for `2024-06-20` on enum `stripe.WebhookEndpoint.CreateParams.api_version`

## 9.12.0 - 2024-06-17
* [#1348](https://github.com/stripe/stripe-python/pull/1348) Update generated code
  * Add support for `tax_id_collection` on parameter class `stripe.PaymentLink.ModifyParams`
  * Add support for `mobilepay` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`

## 9.11.0 - 2024-06-13
* [#1342](https://github.com/stripe/stripe-python/pull/1342) Update generated code
  * Add support for `multibanco_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `twint_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `twint` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `multibanco` on parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, resource classes `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, `stripe.Refund.DestinationDetails`, and `stripe.checkout.Session.PaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `multibanco_display_details` on resource class `stripe.PaymentIntent.NextAction`
  * Add support for `invoice_settings` on resource `stripe.Subscription`
  * Add support for `de_stn` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `multibanco` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `twint` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`

## 9.10.0 - 2024-06-06
* [#1340](https://github.com/stripe/stripe-python/pull/1340) Update generated code
  * Add support for `gb_bank_transfer_payments`, `jp_bank_transfer_payments`, `mx_bank_transfer_payments`, `sepa_bank_transfer_payments`, `us_bank_transfer_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `swish` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`

## 9.9.0 - 2024-05-30
* [#1335](https://github.com/stripe/stripe-python/pull/1335) Add method to list invoice line items
  * Add methods `list_lines()` and `list_lines_async()` on the class `Invoice` to list the invoice line items
* [#1336](https://github.com/stripe/stripe-python/pull/1336) Update generated code
  * Add support for `generated_from` on resource classes `stripe.ConfirmationToken.PaymentMethodPreview.Card` and `stripe.PaymentMethod.Card`
  * Add support for `default_value` on parameter classes `stripe.checkout.Session.CreateParamsCustomFieldDropdown`, `stripe.checkout.Session.CreateParamsCustomFieldNumeric`, and `stripe.checkout.Session.CreateParamsCustomFieldText` and resource classes `stripe.checkout.Session.CustomField.Dropdown`, `stripe.checkout.Session.CustomField.Numeric`, and `stripe.checkout.Session.CustomField.Text`
  * Add support for `verification_requires_additional_proof_of_registration` on enums `stripe.Account.FutureRequirements.Error.code`, `stripe.Account.Requirements.Error.code`, `stripe.BankAccount.FutureRequirements.Error.code`, `stripe.BankAccount.Requirements.Error.code`, `stripe.Capability.FutureRequirements.Error.code`, `stripe.Capability.Requirements.Error.code`, `stripe.Person.FutureRequirements.Error.code`, and `stripe.Person.Requirements.Error.code`
  * Add support for `issuing_personalization_design.activated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_personalization_design.deactivated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_personalization_design.rejected` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_personalization_design.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `en-RO` on enums `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna.preferred_locale`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsKlarna.preferred_locale`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna.preferred_locale`
  * Add support for `ro-RO` on enums `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna.preferred_locale`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsKlarna.preferred_locale`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna.preferred_locale`
  * Change type of `features` on  `stripe.issuing.PhysicalBundle` from `Optional[Features]` to `Features`

## 9.8.0 - 2024-05-23
* [#1332](https://github.com/stripe/stripe-python/pull/1332) Update generated code
  * Add support for `external_account_collection` on resource classes `stripe.AccountSession.Components.Balances.Features` and `stripe.AccountSession.Components.Payouts.Features` and parameter classes `stripe.AccountSession.CreateParamsComponentsBalancesFeatures` and `stripe.AccountSession.CreateParamsComponentsPayoutsFeatures`
  * Add support for `payment_method_remove` on resource class `stripe.checkout.Session.SavedPaymentMethodOptions`
  * Add support for `terminal_reader_invalid_location_for_payment` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 9.7.0 - 2024-05-16
* [#1328](https://github.com/stripe/stripe-python/pull/1328) Update generated code
  * Add support for `fee_source` on resource `stripe.ApplicationFee`
  * Add support for `net_available` on resource class `stripe.Balance.InstantAvailable`
  * Add support for `preferred_locales` on resource classes `stripe.Charge.PaymentMethodDetails.CardPresent`, `stripe.ConfirmationToken.PaymentMethodPreview.CardPresent`, and `stripe.PaymentMethod.CardPresent`
  * Add support for `klarna` on resource class `stripe.Dispute.PaymentMethodDetails`
  * Add support for `routing` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent` and resource class `stripe.PaymentIntent.PaymentMethodOptions.CardPresent`
  * Add support for `application_fee` on resource `stripe.Payout`
  * Add support for `archived` on parameter class `stripe.entitlements.Feature.ListParams`
  * Add support for `lookup_key` on parameter class `stripe.entitlements.Feature.ListParams`
  * Add support for `no_valid_authorization` on parameter classes `stripe.issuing.Dispute.CreateParamsEvidence` and `stripe.issuing.Dispute.ModifyParamsEvidence` and resource class `stripe.issuing.Dispute.Evidence`
  * Add support for `loss_reason` on resource `stripe.issuing.Dispute`
  * Add support for `stripe_s700` on parameter classes `stripe.terminal.Configuration.CreateParams` and `stripe.terminal.Configuration.ModifyParams` and resource `stripe.terminal.Configuration`
  * Add support for `klarna` on enum `stripe.Dispute.PaymentMethodDetails.type`
  * Add support for `no_valid_authorization` on enums `stripe.issuing.Dispute.Evidence.reason`, `stripe.issuing.Dispute.CreateParamsEvidence.reason`, and `stripe.issuing.Dispute.ModifyParamsEvidence.reason`
  * Change type of `countries` on  `stripe.financial_connections.Session.CreateParamsFilters` from `List[str]` to `NotRequired[List[str]]`
* [#1329](https://github.com/stripe/stripe-python/pull/1329) Switch from `black` to `ruff` for formatting

## 9.6.0 - 2024-05-09
* [#1323](https://github.com/stripe/stripe-python/pull/1323) Update generated code
  * Add support for `allow_redisplay` on resource class `stripe.ConfirmationToken.PaymentMethodPreview` and resource `stripe.PaymentMethod`
  * Add support for `preview_mode` on parameter classes `stripe.Invoice.CreatePreviewParams`, `stripe.Invoice.UpcomingLinesParams`, and `stripe.Invoice.UpcomingParams`
  * Add support for `_cls_update` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
  * Add support for `tracking_details` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
  * Add support for `update` on resources `stripe.treasury.OutboundPayment` and `stripe.treasury.OutboundTransfer`
  * Add support for `treasury.outbound_payment.tracking_details_updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `treasury.outbound_transfer.tracking_details_updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`

## 9.5.0 - 2024-05-02
* [#1317](https://github.com/stripe/stripe-python/pull/1317) Update generated code
  * Add support for `paypal` on resource class `stripe.Dispute.PaymentMethodDetails`
  * Add support for `payment_method_types` on parameter class `stripe.PaymentIntent.ConfirmParams`
  * Add support for `ship_from_details` on parameter class `stripe.tax.Calculation.CreateParams` and resources `stripe.tax.Calculation` and `stripe.tax.Transaction`
  * Add support for `bh`, `eg`, `ge`, `ke`, `kz`, `ng`, `om` on resource class `stripe.tax.Registration.CountryOptions` and parameter class `stripe.tax.Registration.CreateParamsCountryOptions`
  * Add support for `paypal` on enum `stripe.Dispute.PaymentMethodDetails.type`
  * Add support for `shipping_address_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Change type of `metadata` on  `stripe.entitlements.Feature.ModifyParams` from `Dict[str, str]` to `Literal['']|Dict[str, str]`
* [#1319](https://github.com/stripe/stripe-python/pull/1319) Fix type change entries in Python Changelog

## 9.4.0 - 2024-04-25
* [#1316](https://github.com/stripe/stripe-python/pull/1316) Update generated code
  * Add support for `amazon_pay` on resource classes `stripe.Mandate.PaymentMethodDetails` and `stripe.SetupAttempt.PaymentMethodDetails`
  * Add support for `revolut_pay` on resource classes `stripe.Mandate.PaymentMethodDetails` and `stripe.SetupAttempt.PaymentMethodDetails`
  * Add support for `setup_future_usage` on resource classes `stripe.PaymentIntent.PaymentMethodOptions.AmazonPay`, `stripe.PaymentIntent.PaymentMethodOptions.RevolutPay`, `stripe.checkout.Session.PaymentMethodOptions.AmazonPay`, and `stripe.checkout.Session.PaymentMethodOptions.RevolutPay`
  * Add support for `mobilepay` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `ending_before` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
  * Add support for `limit` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
  * Add support for `starting_after` on parameter class `stripe.PaymentMethodConfiguration.ListParams`
  * Change type of `feature` on  `stripe.entitlements.ActiveEntitlement` from `str` to `ExpandableField[Feature]`
  * Add support for `amazon_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `revolut_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Remove support for inadvertently released identity verification features `email` and `phone` on parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`
* [#1307](https://github.com/stripe/stripe-python/pull/1307) Bump aiohttp from 3.9.2 to 3.9.4

## 9.3.0 - 2024-04-18
* [#1305](https://github.com/stripe/stripe-python/pull/1305) Update generated code
  * Add support for `allow_redisplay` on parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.Customer.ListPaymentMethodsParams`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`
  * Add support for `schedule_details` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
  * Add support for `subscription_details` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
  * Add support for `create_preview` on resource `stripe.Invoice`
  * Add support for `payment_method_data` on parameter class `stripe.checkout.Session.CreateParams`
  * Add support for `saved_payment_method_options` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
  * Add support for `mobilepay` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
  * Add support for `mobilepay` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
  * Add support for `other` on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`
* [#1306](https://github.com/stripe/stripe-python/pull/1306) Update `Quote.pdf()` to use the right base address i.e. files.stripe.com instead of api.stripe.com. Fixes [#1303](https://github.com/stripe/stripe-python/issues/1303)

## 9.2.0 - 2024-04-16
* [#1301](https://github.com/stripe/stripe-python/pull/1301) Update generated code
  * Add support for `balances` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `payouts_list` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `capture_method` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsRevolutPay`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsRevolutPay`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsRevolutPay` and resource class `stripe.PaymentIntent.PaymentMethodOptions.RevolutPay`
  * Add support for `swish` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for resource `stripe.entitlements.ActiveEntitlementSummary`
  * Remove support for `config` on parameter class `stripe.forwarding.Request.CreateParams` and resource `stripe.forwarding.Request`. This field is no longer used by the Forwarding Request API.
  * Change type of `destination_on_behalf_of_charge_management` on  `stripe.AccountSession.Components.PaymentDetails.Features` and `stripe.AccountSession.Components.Payments.Features` from `Optional[bool]` to `bool`
  * Change type of `timestamp` on  `stripe.billing.MeterEvent.CreateParams` from `int` to `NotRequired[int]`
  * Add support for `entitlements.active_entitlement_summary.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`

## 9.1.0 - 2024-04-11
* [#1300](https://github.com/stripe/stripe-python/pull/1300) Update generated code
  * Add support for `external_account_collection` on resource class `stripe.AccountSession.Components.AccountOnboarding.Features` and parameter class `stripe.AccountSession.CreateParamsComponentsAccountOnboardingFeatures`
  * Add support for `account_management` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `notification_banner` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `amazon_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, `stripe.Refund.DestinationDetails`, `stripe.SetupIntent.PaymentMethodOptions`, and `stripe.checkout.Session.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptions`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `next_refresh_available_at` on resource class `stripe.financial_connections.Account.OwnershipRefresh`
  * Change type of `cancel` on  `stripe.billing.MeterEventAdjustment` from `Cancel` to `Optional[Cancel]`
  * Change type of `identifier` on  `stripe.billing.MeterEventAdjustment.Cancel` from `str` to `Optional[str]`
  * Change type of `identifier` on  `stripe.billing.MeterEventAdjustment.CreateParamsCancel` from `str` to `NotRequired[str]`
  * Change type of `cancel` on  `stripe.billing.MeterEventAdjustment.CreateParams` from `MeterEventAdjustment.CreateParamsCancel` to `NotRequired[MeterEventAdjustment.CreateParamsCancel]`
  * Change type of `type` on  `stripe.billing.MeterEventAdjustment.CreateParams` from `NotRequired[Literal['cancel']]` to `Literal['cancel']`
  * Add support for `bh_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `kz_bin` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `ng_tin` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `om_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `ownership` on enums `stripe.checkout.Session.PaymentMethodOptions.UsBankAccount.FinancialConnections.prefetch`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.Invoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.permissions`, `stripe.Invoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.prefetch`, `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.PaymentIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections.prefetch`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.SetupIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections.prefetch`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.permissions`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.prefetch`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections.prefetch`
  * Add support for `amazon_pay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `billing_policy_remote_function_response_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_timeout` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_unexpected_status_code` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_unreachable` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
* [#1297](https://github.com/stripe/stripe-python/pull/1297) Use stdlib AsyncMock when available

## 9.0.0 - 2024-04-10
* [#1286](https://github.com/stripe/stripe-python/pull/1286)

  * This release changes the pinned API version to `2024-04-10`. Please read the [API Upgrade Guide](https://stripe.com/docs/upgrades#2024-04-10) and carefully review the API changes before upgrading.

  ### ⚠️ Breaking changes

  * Remove `FinancialAccountFeaturesService.CreateParams`, `FinancialAccountFeaturesService.ListParams`, `FinancialAccountFeaturesService.create()`, `FinancialAccountFeaturesService.list()` as Financial account features is a singleton and so should have retrieve and update methods instead of create and list methods.
  * Rename `features` to `marketing_features` on parameter classes `stripe.Product.CreateParams` and `stripe.Product.ModifyParams` and resource `stripe.Product`.

  #### ⚠️ Removal of enum values, properties and events that are no longer part of the publicly documented Stripe API
   * Remove `.subscription_pause` from the below as the feature to pause subscription on the portal has been deprecated
      * `Configuration.Features`
      * `ConfigurationService.CreateParamsFeatures`
      * `ConfigurationService.UpdateParamsFeatures`
   * Remove the below deprecated values for `BalanceTransaction.type`
      * `obligation_inbound`
      * `obligation_payout`
      * `obligation_payout_failure`
      * `obligation_reversal_outbound`
   * Remove the below deprecated events from `Event.type`, `WebhookEndpoint.CreateParams.enabled_events`, `WebhookEndpoint.ModifyParams.enabled_events`, `WebhookEndpointService.CreateParams.enabled_events`, `WebhookEndpointService.ModifyParams.enabled_events`
     * `invoiceitem.updated`
     * `order.created`
     * `recipient.created`
     * `recipient.deleted`
     * `recipient.updated`
     * `sku.created`
     * `sku.deleted`
     * `sku.updated`
   * Remove the deprecated value `include_and_require` for `Invoice.CreateParams.pending_invoice_items_behavior` and `InvoiceService.CreateParams.pending_invoice_items_behavior`
   * Remove the deprecated value `service_tax` for
     * `TaxRate.RetrieveParams.tax_type`
     * `TaxRate.CreateParams.tax_type`
     * `TaxRate.ModifyParams.tax_type`
     * `TaxRateService.CreateParams.tax_type`
     * `TaxRateService.UpdateParams.tax_type`
     * `InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`
     * `InvoiceLineItemService.UpdateParamsTaxAmountTaxRateData.tax_type`
   * Remove `request_incremental_authorization` from
     * `PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent`
     * `PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent`
     * `PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent`
     * `PaymentIntentService.ConfirmParamsPaymentMethodOptionsCardPresent`
     * `PaymentIntentService.CreateParamsPaymentMethodOptionsCardPresent`
     * `PaymentIntentService.ModifyParamsPaymentMethodOptionsCardPresent`
   * Remove support for `id_bank_transfer`, `multibanco`, `netbanking`, `pay_by_bank`, and `upi` on `PaymentMethodConfiguration`
   * Remove the deprecated value `challenge_only` from `SetupIntent.PaymentMethodOptions.Card.request_three_d_secure`
   * Remove deprecated value `various` for `Climate.Supplier.removal_pathway`
   * Remove the deprecated value `obligation` for `ReportRun.CreateParamsParameters.reporting_category` and `ReportRunService.CreateParamsParameters.reporting_category`
   * Remove the legacy field `rendering_options` on parameter classes `stripe.Invoice.CreateParams` and `stripe.Invoice.ModifyParams` and resource `stripe.Invoice`. Use `rendering` instead.




## 8.11.0 - 2024-04-09
* [#1295](https://github.com/stripe/stripe-python/pull/1295) Update generated code
  * Add support for `fees`, `losses`, `requirement_collection` & `stripe_dashboard` on resource class `stripe.Account.Controller`
  * Add support for `controller` on parameter class `stripe.Account.CreateParams`
  * Add support for `create_feature`, `delete_feature`, `list_features`, `retrieve_feature` on resource `stripe.Product`
  * Add support for resource `stripe.ProductFeature`
  * Add support for `event_name` on parameter class `stripe.billing.MeterEventAdjustment.CreateParams` and resource `stripe.billing.MeterEventAdjustment`
  * Add support for `cancel` and `type` on resource `stripe.billing.MeterEventAdjustment`
  * Add support for resource `stripe.entitlements.ActiveEntitlement`
  * Add support for resource `stripe.entitlements.Feature`
  * Add support for `none` on enum `stripe.Account.type`

* [#1299](https://github.com/stripe/stripe-python/pull/1299) Fix README.md
* [#1292](https://github.com/stripe/stripe-python/pull/1292) Tweak changelog for python async note

## 8.10.0 - 2024-04-04

* [#1288](https://github.com/stripe/stripe-python/pull/1288) Port **async support** from beta to the stable channel. To use it, add an `_async` suffix to any request-making method.

    ```diff
    - cus = stripe.Customer.create(...)
    + cus = await stripe.Customer.create_async(...)
    ```

    See the [README](./README.md#async) for detailed usage instructions. Support is provided out of the box for async requests via the HTTPX (used by default) and aiohttp libraries. For other libraries, you can also provide your own `stripe.HTTPClient` implementation. Please do not hesitate to [open a Github issue](https://github.com/stripe/stripe-python/issues/new/choose) if you have any feedback on this feature.
* [#1284](https://github.com/stripe/stripe-python/pull/1284) Update generated code
  * Add support for `subscription_item` on resource `stripe.Discount`
  * Add support for `promotion_code` on parameter classes `stripe.Invoice.CreateParamsDiscount`, `stripe.Invoice.ModifyParamsDiscount`, `stripe.InvoiceItem.CreateParamsDiscount`, `stripe.InvoiceItem.ModifyParamsDiscount`, `stripe.InvoiceLineItem.ModifyParamsDiscount`, `stripe.Quote.CreateParamsDiscount`, and `stripe.Quote.ModifyParamsDiscount`
  * Add support for `discounts` on parameter classes `stripe.Invoice.UpcomingLinesParamsSubscriptionItem`, `stripe.Invoice.UpcomingParamsSubscriptionItem`, `stripe.Quote.CreateParamsLineItem`, `stripe.Quote.ModifyParamsLineItem`, `stripe.Subscription.CreateParams`, `stripe.Subscription.CreateParamsAddInvoiceItem`, `stripe.Subscription.CreateParamsItem`, `stripe.Subscription.ModifyParams`, `stripe.Subscription.ModifyParamsAddInvoiceItem`, `stripe.Subscription.ModifyParamsItem`, `stripe.SubscriptionItem.CreateParams`, `stripe.SubscriptionItem.ModifyParams`, `stripe.SubscriptionSchedule.CreateParamsPhase`, `stripe.SubscriptionSchedule.CreateParamsPhaseAddInvoiceItem`, `stripe.SubscriptionSchedule.CreateParamsPhaseItem`, `stripe.SubscriptionSchedule.ModifyParamsPhase`, `stripe.SubscriptionSchedule.ModifyParamsPhaseAddInvoiceItem`, and `stripe.SubscriptionSchedule.ModifyParamsPhaseItem`, resources `stripe.Subscription` and `stripe.SubscriptionItem`, and resource classes `stripe.SubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.SubscriptionSchedule.Phase.Item`, and `stripe.SubscriptionSchedule.Phase`
  * Add support for `zip` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `offline` on resource class `stripe.SetupAttempt.PaymentMethodDetails.CardPresent`
  * Add support for `card_present` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
  * Add support for `email` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
  * Add support for `phone` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
  * Add support for `verification_flow` on resources `stripe.identity.VerificationReport` and `stripe.identity.VerificationSession` and parameter class `stripe.identity.VerificationSession.CreateParams`
  * Add support for `provided_details` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ModifyParams` and resource `stripe.identity.VerificationSession`
  * Add support for `allowed_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
  * Add support for `blocked_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
  * Change type of `reference` on  `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSwish` from `Literal['']|str` to `str`
  * Add support for `verification_flow` on enums `stripe.identity.VerificationReport.type` and `stripe.identity.VerificationSession.type`
  * Add support for `email_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `email_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `phone_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `phone_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `mobile_phone_reader` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
  * Change type of `type` on  `stripe.identity.VerificationSession.CreateParams` from `Literal['document', 'id_number']` to `NotRequired[Literal['document', 'id_number']]`
  * Change type of `discounts` on  `stripe.Invoice` and `stripe.InvoiceLineItem` from `Optional[List[ExpandableField[Discount]]]` to `List[ExpandableField[Discount]]`
  * Change type of `data` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
  * Change type of `image_url_png` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
  * Change type of `image_url_svg` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str`
  * Change type of `hosted_instructions_url` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str`
  * Change type of `mobile_auth_url` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str`
  * Change type of `qr_code` on  `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[QrCode]` to `QrCode`
* [#1289](https://github.com/stripe/stripe-python/pull/1289) Bump aiohttp from 3.9.0 to 3.9.2


## 8.9.0 - 2024-03-28
* [#1276](https://github.com/stripe/stripe-python/pull/1276) Update generated code
  * Add support for new resources `Billing.MeterEventAdjustment`, `Billing.MeterEvent`, and `Billing.Meter`
  * Add support for `create`, `deactivate`, `list`, `modify`, `reactivate`, and `retrieve` methods on resource `Meter`
  * Add support for `create` method on resources `MeterEventAdjustment` and `MeterEvent`
  * Add support for `amazon_pay_payments` on `Account.Capabilities`, `Account.CreateParamsCapabilities`, `Account.UpdateParamsCapabilities`,`AccountService.CreateParamsCapabilities`, and `AccountService.UpdateParamsCapabilities`
  * Add support for new value `verification_failed_representative_authority` on enums `Account.FutureRequirements.Error.code`, `Account.Requirements.Errors.code`, `BankAccount.FutureRequirements.Error.code`, `BankAccount.Requirements.Errors.code`, `Capability.FutureRequirements.Error.code`, `Capability.Requirements.Errors.code`, `Person.FutureRequirements.Error.code`, `Person.Requirements.Errors.code`,
  * Add support for `destination_on_behalf_of_charge_management` on `AccountSession.Components.PaymentDetails.Features`, `AccountSession.Components.Payments.Features`, `AccountSession.CreateParamsComponentsPaymentDetailsFeatures`, `AccountSession.CreateParamsComponentsPaymentsFeatures`, `AccountSessionService.CreateParamsComponentsPaymentDetailsFeatures` and `AccountSessionService.CreateParamsComponentsPaymentsFeatures`
  * Add support for `meter` on `Plan.CreateParams`, `Plan`, `PlanService.CreateParams`, `Price.Recurring`, `Price.CreateParamsRecurring`, `Price.ListParamsRecurring`, `PriceService.CreateParamsRecurring`, and `PriceService.ListParamsRecurring`
  * Add support for `mandate` on `Charge.PaymentMethodDetails.USBankAccount`, `Treasury.InboundTransfer.OriginPaymentMethodDetails.USBankAccount`, `Treasury.OutboundPayment.DestinationPaymentMethodDetails.USBankAccount`, and `Treasury.OutboundTransfer.DestinationPaymentMethodDetails.USBankAccount`
  * Add support for `second_line` on `Issuing.Card.CreateParams`
* [#1278](https://github.com/stripe/stripe-python/pull/1278) Types: remove unnecessary quotes
* [#1279](https://github.com/stripe/stripe-python/pull/1279) Update README.md

## 8.8.0 - 2024-03-21
* [#1273](https://github.com/stripe/stripe-python/pull/1273) Update generated code
  * Add support for new resources `ConfirmationToken` and `Forwarding.Request`
  * Add support for `retrieve` method on resource `ConfirmationToken`
  * Add support for `create`, `list`, and `retrieve` methods on resource `Request`
  * Add support for `mobilepay_payments` on `Account.Capabilities`, `Account.CreateParamsCapabilities`, and `Account.UpdateParamsCapabilities`
  * Add support for new values `forwarding_api_inactive`, `forwarding_api_invalid_parameter`, `forwarding_api_upstream_connection_error`, and `forwarding_api_upstream_connection_timeout` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `SetupAttempt.SetupError.code`, `SetupIntent.LastSetupError.code`, and `StripeError.code`
  * Add support for `payment_reference` on `Charge.PaymentMethodDetails.UsBankAccount`
  * Add support for `payout` on `Treasury.ReceivedDebit.LinkedFlows`
  * Add support for `name` on `ConfigurationService.CreateParams`, `ConfigurationService.UpdateParams`, and `Configuration` for terminal
   * Add support for `confirmation_token` on `PaymentIntentService.ConfirmParams`, `PaymentIntentService.CreateParams`, `SetupIntentService.ConfirmParams`, and `SetupIntentService.CreateParams`
   * Add support for new value `mobilepay` on enums `Customer.ListPaymentMethodsParams.type`, `PaymentMethod.CreateParams.type`, and `PaymentMethod.ListParams.type`
   * Add support for `mobilepay` on `Charge.PaymentMethodDetails`, `PaymentIntent.PaymentMethodOptions`, `PaymentIntentService.ConfirmParamsPaymentMethodData`, `PaymentIntentService.ConfirmParamsPaymentMethodOptions`, `PaymentIntentService.CreateParamsPaymentMethodData`, `PaymentIntentService.CreateParamsPaymentMethodOptions`, `PaymentIntentService.UpdateParamsPaymentMethodData`, `PaymentIntentService.UpdateParamsPaymentMethodOptions`, `PaymentMethod.CreateParams`, `PaymentMethod`, `SetupIntentService.ConfirmParamsPaymentMethodData`, `SetupIntentService.CreateParamsPaymentMethodData`, and `SetupIntentService.UpdateParamsPaymentMethodData`
   * Add support for new value `mobilepay` on enums `PaymentIntentService.ConfirmParamsPaymentMethodData.type`, `PaymentIntentService.CreateParamsPaymentMethodData.type`, `PaymentIntentService.UpdateParamsPaymentMethodData.type`, `SetupIntentService.ConfirmParamsPaymentMethodData.type`, `SetupIntentService.CreateParamsPaymentMethodData.type`, and `SetupIntentService.UpdateParamsPaymentMethodData.type`
   * Add support for new value `mobilepay` on enum `PaymentMethod.type`



## 8.7.0 - 2024-03-14
* [#1269](https://github.com/stripe/stripe-python/pull/1269) Update generated code
  * Add support for `personalization_design` on parameter classes `CardService.CreateParams`, `CardService.ListParams`, `CardService.UpdateParams`, `stripe.issuing.Card.CreateParams`, `stripe.issuing.Card.ListParams`, and `stripe.issuing.Card.ModifyParams` and resource `stripe.issuing.Card`
  * Add support for `sepa_debit` on parameter classes `SubscriptionService.CreateParamsPaymentSettingsPaymentMethodOptions`, `SubscriptionService.UpdateParamsPaymentSettingsPaymentMethodOptions`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptions`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions` and resource class `stripe.Subscription.PaymentSettings.PaymentMethodOptions`
  * Add support for resource `stripe.issuing.PersonalizationDesign`
  * Add support for resource `stripe.issuing.PhysicalBundle`
  * Change type from `float` to `Literal['']|float` of `application_fee_percent` on fields `stripe.Subscription.CreateParams`, `stripe.Subscription.ModifyParams`, `SubscriptionService.UpdateParams`, and `SubscriptionService.CreateParams`


## 8.6.0 - 2024-03-07
* [#1267](https://github.com/stripe/stripe-python/pull/1267) Update generated code
  * Add support for `documents` on `AccountSession.Components`
  * Add support for `request_three_d_secure` on `Checkout.Session.PaymentMethodOptionsCard` and `Checkout.Session.CreateParams.PaymentMethodOptionsCard`
  * Add support for `created` on `CreditNote.ListParams`
  * Add support for `sepa_debit` on `Invoice.PaymentSettings.PaymentMethodOptions`, `InvoiceCreateParams.PaymentSettings.PaymentMethodOptions`, and `InvoiceUpdateParams.PaymentSettings.PaymentMethodOptions`
* [#1268](https://github.com/stripe/stripe-python/pull/1268) Update README.md

## 8.5.0 - 2024-02-29
* [#1255](https://github.com/stripe/stripe-python/pull/1255) Update generated code
  * Change `identity.VerificationReport.type` to be required
  * Change type of `identity.VerificationSession.type` from `Optional[Literal["document", "id_number"]]` to `Literal["document", "id_number"]`
  * Add support for `number` on `Invoice.CreateParams` and `Invoice.ModifyParams`
  * Add support for `enable_customer_cancellation` on `terminal.Reader.Action.ProcessPaymentIntent.process_config`, `Terminal.Reader.Action.ProcessSetupIntent.process_config`, `Terminal.Reader.ProcessPaymentIntentParams.process_config`, and `Terminal.Reader.ProcessSetupIntentParams.process_config`
  * Add support for `refund_payment_config` on `Terminal.Reader.Action.refund_payment` and `Terminal.Reader.RefundPaymentParams`
  * Add support for `payment_method` on `Token.CreateParams.bank_account`
  * Add `list_refunds` and `retrieve_refund` methods on resource `Charge`.
* [#1260](https://github.com/stripe/stripe-python/pull/1260) Update README to use add_beta_version
* [#1250](https://github.com/stripe/stripe-python/pull/1250) Fix type of ErrorObject.code

## 8.4.0 - 2024-02-22
* [#1241](https://github.com/stripe/stripe-python/pull/1241) Update generated code
  - Add `InvoiceLineItem.modify` method.
* [#1244](https://github.com/stripe/stripe-python/pull/1244) Add TaxIds API
  * Add support for `create`, `retrieve`, `delete`, and `list` methods on resource `TaxId`
  * The `instance_url` function on resource `TaxId` now returns the top-level `/v1/tax_ids/{id}` path instead of the `/v1/customers/{customer}/tax_ids/{id}` path.
* [#1243](https://github.com/stripe/stripe-python/pull/1243) Remove http client base
* [#1242](https://github.com/stripe/stripe-python/pull/1242) Testing: unify http client mock

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

## 8.2.0 - 2024-02-08
* [#1225](https://github.com/stripe/stripe-python/pull/1225) Update generated code
  * Add support for `invoices` on `Account.Settings`
  * Add support for new value `velobank` on various enums `PaymentMethodDetails.P24.bank`
  * Add support for `setup_future_usage` on `PaymentMethodOptions.Blik`
  * Add support for `require_cvc_recollection` on `PaymentMethodOptions.Card`
  * Add support for `account_tax_ids` on various `InvoiceSettings` request parameters
* [#1223](https://github.com/stripe/stripe-python/pull/1223) Move StripeClient usage collection onto StripeService
* [#1220](https://github.com/stripe/stripe-python/pull/1220) Measure StripeClient usage

## 8.1.0 - 2024-02-01
* [#1213](https://github.com/stripe/stripe-python/pull/1213) Update generated code
  * Add support for `swish` payment method throughout the API
  * Add support for `relationship` on parameter classes `Account.CreateParamsIndividual` and `Token.CreateParamsAccountIndividual`
  * Add support for `jurisdiction_level` on resource `TaxRate`
  * Change type from `str` to `Literal["offline", "online"]` of `status` on field `terminal.Reader`

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

## 7.12.0 - 2024-01-12
* [#1188](https://github.com/stripe/stripe-python/pull/1188) Update generated code
  * Add support for new resource `CustomerSession`
  * Add support for `create` method on resource `CustomerSession`
  * Remove support for values `obligation_inbound`, `obligation_payout_failure`, `obligation_payout`, and `obligation_reversal_outbound` from enum `BalanceTransaction.type`
  * Add support for new values `eps` and `p24` on enums `Invoice.payment_settings.payment_method_types[]`, `InvoiceCreateParams.payment_settings.payment_method_types[]`, `InvoiceUpdateParams.payment_settings.payment_method_types[]`, `Subscription.payment_settings.payment_method_types[]`, `SubscriptionCreateParams.payment_settings.payment_method_types[]`, and `SubscriptionUpdateParams.payment_settings.payment_method_types[]`
  * Remove support for value `obligation` from enum `Reporting.ReportRunCreateParams.parameters.reporting_category`
  * Add support for `billing_cycle_anchor_config` on `SubscriptionCreateParams` and `Subscription`

## 7.11.0 - 2024-01-04
* [#1186](https://github.com/stripe/stripe-python/pull/1186) Update generated code
  * Add support for `retrieve` on resource `tax.Registration`
  * Change type from `Optional[PaymentDetails]` to `PaymentDetails` of `payment_details` on field `AccountSession.Components`
  * Change type from `Optional[Payments]` to `Payments` of `payments` on field `AccountSession.Components`
  * Change type from `Optional[Payouts]` to `Payouts` of `payouts` on field `AccountSession.Components`
  * Change type from `Optional[Features]` to `Features` of `features` on fields `AccountSession.Components.PaymentDetails`, `AccountSession.Components.Payments`, and `AccountSession.Components.Payouts`
  * Change type from `Optional[InvoiceSettings]` to `InvoiceSettings` of `invoice_settings` on field `SubscriptionSchedule.DefaultSettings`


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

## 7.9.0 - 2023-12-14
* [#1161](https://github.com/stripe/stripe-python/pull/1161) Update generated code

  * Add support for `payment_method_reuse_agreement` on resource classes `PaymentLink.ConsentCollection` and `checkout.Session.ConsentCollection` and parameter classes `PaymentLink.CreateParamsConsentCollection` and `checkout.Session.CreateParamsConsentCollection`
  * Add support for `after_submit` on parameter classes `PaymentLink.CreateParamsCustomText`, `PaymentLink.ModifyParamsCustomText`, and `checkout.Session.CreateParamsCustomText` and resource classes `PaymentLink.CustomText` and `checkout.Session.CustomText`
  * Add support for `created` on parameter class `radar.EarlyFraudWarning.ListParams`
* [#1146](https://github.com/stripe/stripe-python/pull/1146) Track usage of deprecated `save`
  * Reports uses of the deprecated `.save` in `X-Stripe-Client-Telemetry`. (You can disable telemetry via `stripe.enable_telemetry = false`, see the [README](https://github.com/stripe/stripe-python/blob/master/README.md#telemetry).)
* [#1101](https://github.com/stripe/stripe-python/pull/1101) Mark defunct and internal methods as deprecated
* [#1169](https://github.com/stripe/stripe-python/pull/1169) Add more types to _http_client.py

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

## 7.4.0 - 2023-11-09
* [#1119](https://github.com/stripe/stripe-python/pull/1119) Update generated code
  * Add support for new value `terminal_reader_hardware_fault` on enums `Invoice.last_finalization_error.code`, `PaymentIntent.last_payment_error.code`, `SetupAttempt.setup_error.code`, `SetupIntent.last_setup_error.code`, and `StripeError.code`
  * Add support for `metadata` on `Quote.subscription_data`, `QuoteCreateParams.subscription_data`, and `QuoteUpdateParams.subscription_data`
* [#1121](https://github.com/stripe/stripe-python/pull/1121) [types] Remove `None` from optional param types

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
## 7.0.0 - 2023-10-16
* This release changes the pinned API version to `2023-10-16`. Please read the [API Upgrade Guide](https://stripe.com/docs/upgrades#2023-10-16) and carefully review the API changes before upgrading `stripe-python`.
* [#1085](https://github.com/stripe/stripe-python/pull/1085) Update generated code
  - Updated pinned API version

## 6.7.0 - 2023-10-05
* [#1065](https://github.com/stripe/stripe-python/pull/1065) Update generated code
  * Add support for new resource `Issuing.Token`
  * Add support for `list`, `modify`, and `retrieve` methods on resource `Token`

## 6.6.0 - 2023-09-21
* [#1056](https://github.com/stripe/stripe-python/pull/1056) Update generated code

* [#1055](https://github.com/stripe/stripe-python/pull/1055) Partially type resource methods (no **params)
* [#1057](https://github.com/stripe/stripe-python/pull/1057) Add optional types to non-required fields
* [#1054](https://github.com/stripe/stripe-python/pull/1054) Types: add deleted field

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

## 6.4.0 - 2023-09-07
* [#1033](https://github.com/stripe/stripe-python/pull/1033) Update generated code
  * Add support for new resource `PaymentMethodDomain`
  * Add support for `create`, `list`, `modify`, `retrieve`, and `validate` methods on resource `PaymentMethodDomain`
* [#1044](https://github.com/stripe/stripe-python/pull/1044) Types: ExpandableField
* [#1043](https://github.com/stripe/stripe-python/pull/1043) Types: ListObject

## 6.3.0 - 2023-09-05
* [#1042](https://github.com/stripe/stripe-python/pull/1042) Require typing_extensions >= 4.0.0
* [#1026](https://github.com/stripe/stripe-python/pull/1026) Types: annotate resource properties

## 6.2.0 - 2023-08-31
* [#1024](https://github.com/stripe/stripe-python/pull/1024) Update generated code
  * Add support for new resource `AccountSession`
  * Add support for `create` method on resource `AccountSession`
* [#1032](https://github.com/stripe/stripe-python/pull/1032) Types for CRUDL methods on parents

## 6.1.0 - 2023-08-24
* [#1016](https://github.com/stripe/stripe-python/pull/1016) Update generated code
* [#1020](https://github.com/stripe/stripe-python/pull/1020) Adds type annotations, and dependency on `typing_extensions`.


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

## 5.5.0 - 2023-07-13
* [#990](https://github.com/stripe/stripe-python/pull/990) Update generated code
  * Add support for new resource `Tax.Settings`
  * Add support for `modify` and `retrieve` methods on resource `Settings`

## 5.4.0 - 2023-03-30
* [#951](https://github.com/stripe/stripe-python/pull/951) Update generated code
  * Remove support for `create` method on resource `Tax.Transaction`
    * This is not a breaking change, as this method was deprecated before the Tax Transactions API was released in favor of the `create_from_calculation` method.

## 5.3.0 - 2023-03-23
* [#947](https://github.com/stripe/stripe-python/pull/947) Update generated code
  * Add support for new resources `Tax.CalculationLineItem`, `Tax.Calculation`, `Tax.TransactionLineItem`, and `Tax.Transaction`
  * Add support for `create` and `list_line_items` methods on resource `Calculation`
  * Add support for `create_from_calculation`, `create_reversal`, `create`, `list_line_items`, and `retrieve` methods on resource `Transaction`

## 5.2.0 - 2023-02-16
* [#924](https://github.com/stripe/stripe-python/pull/924) API Updates
  * Add support for `refund_payment` method on resource `Terminal.Reader`

## 5.1.1 - 2023-02-06
* [#923](https://github.com/stripe/stripe-python/pull/923) Bugfix: revert "Pass params into logger.{info,debug}"

## 5.1.0 - 2023-02-02
* [#920](https://github.com/stripe/stripe-python/pull/920) API Updates
  * Add support for `resume` method on resource `Subscription`
* [#913](https://github.com/stripe/stripe-python/pull/913) Pass params into logger.{info,debug}

## 5.0.0 - 2022-11-16

Breaking changes that arose during code generation of the library that we postponed for the next major version. For changes to the Stripe products, read more at https://stripe.com/docs/upgrades#2022-11-15.

"⚠️" symbol highlights breaking changes.

* [#895](https://github.com/stripe/stripe-python/pull/895) Next major release changes
* [#889](https://github.com/stripe/stripe-python/pull/889) API Updates

* [#888](https://github.com/stripe/stripe-python/pull/888) Do not run Coveralls if secret token is not available
* [#875](https://github.com/stripe/stripe-python/pull/875) hide misleading ssl security warning in python>=2.7.9

### ⚠️ Changed
- Dropped support for Python version 3.4 and 3.5 (#881). We now support Python 2.7 or 3.6+.
- Fixed mistyped names for two OAuth exceptions: `UnsupportedGrantTypError`->`UnsupportedGrantTypeError` and `UnsupportedResponseTypError`->`UnsupportedResponseTypeError` (#872).

### Deprecated
- Deprecate `save` method on resources (#887). Use `modify` instead.
   ```python
  # Before
  customer = stripe.Customer.retrieve("cus_123")
  customer.email = "example@test.com"
  customer.save()

  # After
  stripe.Customer.modify("cus_123", email="example@test.com")
   ```

### ⚠️ Removed
- Removed `Orders` resource (#882).
- Removed `SKU` resource (#883).

## 4.2.0 - 2022-09-23
* [#877](https://github.com/stripe/stripe-python/pull/877) API Updates
  * Add `upcoming_lines` method to the `Invoice` resource.
* [#873](https://github.com/stripe/stripe-python/pull/873) Add abstract methods for SearchableAPIResource
* [#867](https://github.com/stripe/stripe-python/pull/867) API Updates
  * Update links in documentation to be absolute.

## 4.1.0 - 2022-08-19
* [#861](https://github.com/stripe/stripe-python/pull/861) API Updates
  * Add support for new resource `CustomerCashBalanceTransaction`
* [#860](https://github.com/stripe/stripe-python/pull/860) Add a support section to the readme
* [#717](https://github.com/stripe/stripe-python/pull/717) Fix test TestCharge.test_is_saveable().

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

### ⚠️ Removed
- Removed deprecated `AlipayAccount`, `BitcoinReceiver`, `BitcoinTransaction`, `IssuerFraudRecord`, `Recipient`, `RecipientTransfer`, and  `ThreeDSecure` classes.
- Removed deprecated `Charge.update_dispute` and `Charge.close_dispute` methods that were using legacy REST API endpoint. Prefer [Dispute.modify](https://stripe.com/docs/api/disputes/update?lang=python) and [Dispute.close](https://stripe.com/docs/api/disputes/close?lang=python)
- Removed deprecated `Card.details` method and `CardDetails` resource. The REST API endpoint is not longer supported.
- Removed the deprecated `Source.source_transactions` method. Prefer `SubscriptionItem.list_source_transactions`
- Removed the deprecated `SubscriptionItem.usage_record_summaries` method. Prefer `SubscriptionItem.list_usage_record_summaries`
- Removed the deprecated `Charge.refund` method. Prefer [Refund.create](https://stripe.com/docs/api/refunds/create)

### ⚠️ Changed
- To be consistent with other resource methods, `ApplicationFee.refund` returns an instance of `ApplicationFee` and doesn't mutate the instance of `ApplicationFee`.
- To be consistent with other resource methods, the `Customer.delete_discount` no longer resets the `discount` property to `None` and returns the deleted discount instead. If you were relying on this behavior, reset the discount property manually:
- The `LineItem` resource now inherits from `StripeObject` as it has no methods of it's own.
- To be consistent with other resource methods, the `Subscription.delete_discount` returns an instance of deleted discount and doesn't mutate the instance of `Subscription`.
- Update the CA certificate bundle.
- Request sending logic unified across standard and custom methods (https://github.com/stripe/stripe-python/pull/832)

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

### Backwards incompatible changes
* The `to_dict` and `values` methods on resources no longer recursively convert objects to plain `dict`s.  All resources now inherit from `dict` but are functionally different in that you cannot set a value to an empty string and cannot delete items.
* The `previous_metadata` attribute on resources is now protected.
* Timezone aware `datetime` objects passed to the API will now be encoded in a way that does not depend on the local system time.  If you are passing timezone-aware datetimes to our API and your server time is not already in UTC, this will change the value passed to our API.

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
