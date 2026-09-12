---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1857
is_stripe_api_change: true
released_in_version: 15.4.0
---

* Add support for new resource `financial_connections.Authorization`
* Add support for `unreject` method on resource `Account`
* Add support for `list` method on resource `PaymentRecord`
* Add support for new values `mass_transit_parking_tax` and `parking_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
* Add support for new value `chaps` on enums `FundingInstructions.BankTransfer.FinancialAddress.supported_networks` and `PaymentIntent.NextAction.DisplayBankTransferInstruction.FinancialAddress.supported_networks`
* Add support for `smart_disputes_management` on `AccountSession.Component.DisputesList.Feature`, `AccountSession.Component.Payment.Feature`, `AccountSession.Component.PaymentDetail.Feature`, `AccountSession.Component.PaymentDispute.Feature`, `AccountSessionCreateParamsComponentDisputesListFeature`, `AccountSessionCreateParamsComponentPaymentDetailFeature`, `AccountSessionCreateParamsComponentPaymentDisputeFeature`, and `AccountSessionCreateParamsComponentPaymentFeature`
* Add support for `administrative_address` and `principal_place_of_business` on `Account.Company`, `AccountCreateParamsCompany`, `AccountModifyParamsCompany`, and `TokenCreateParamsAccountCompany`
* Add support for `sepa_debit_payments` on `AccountModifyParamsSetting`
* Remove support for `proof_of_registration` on `AccountCreateParamsDocument`.  This field was limited-use and is being deprecated.
* Add support for `payouts_action` on `AccountRejectParams`
* Add support for new value `data_share_only` on enums `Charge.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, `PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure.result`, and `SetupAttempt.PaymentMethodDetail.Card.ThreeDSecure.result`
* Add support for new values `bnp_paribas`, `citibank`, and `mbsb_bank` on enums `Charge.PaymentMethodDetail.Fpx.bank`, `ConfirmationToken.PaymentMethodPreview.Fpx.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Fpx.bank`, `PaymentMethod.Fpx.bank`, and `PaymentRecord.PaymentMethodDetail.Fpx.bank`
* Remove support for `dynamic_tax_rates` on `checkout.SessionCreateParamsLineItem`.  This field was limited-use and is being deprecated.
* Add support for `setup_future_usage` on `Checkout.Session.PaymentMethodOption.Payco`, `Checkout.Session.PaymentMethodOption.SamsungPay`, `PaymentIntent.PaymentMethodOption.Payco`, `PaymentIntent.PaymentMethodOption.SamsungPay`, `PaymentIntentConfirmParamsPaymentMethodOptionPayco`, `PaymentIntentConfirmParamsPaymentMethodOptionSamsungPay`, `PaymentIntentCreateParamsPaymentMethodOptionPayco`, `PaymentIntentCreateParamsPaymentMethodOptionSamsungPay`, `PaymentIntentModifyParamsPaymentMethodOptionPayco`, `PaymentIntentModifyParamsPaymentMethodOptionSamsungPay`, `PaymentLinkModifyParamsPaymentIntentDatum`, `checkout.SessionCreateParamsPaymentMethodOptionPayco`, and `checkout.SessionCreateParamsPaymentMethodOptionSamsungPay`
* Add support for new value `ic_nif` on enums `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
* Add support for new values `bnp_paribas`, `citibank`, and `mbsb_bank` on enums `ConfirmationTokenCreateParamsPaymentMethodDatumFpx.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumFpx.bank`, `PaymentIntentCreateParamsPaymentMethodDatumFpx.bank`, `PaymentIntentModifyParamsPaymentMethodDatumFpx.bank`, `PaymentMethodCreateParamsFpx.bank`, `SetupIntentConfirmParamsPaymentMethodDatumFpx.bank`, `SetupIntentCreateParamsPaymentMethodDatumFpx.bank`, and `SetupIntentModifyParamsPaymentMethodDatumFpx.bank`
* Add support for new value `ic_nif` on enums `CustomerCreateParamsTaxIdDatum.type`, `CustomerCreateTaxIdParams.type`, `InvoiceCreatePreviewParamsCustomerDetailTaxId.type`, `TaxIdCreateParams.type`, and `tax.CalculationCreateParamsCustomerDetailTaxId.type`
* Add support for `network` on `Dispute.PaymentMethodDetail.Card`
* Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enum `Event.type`
* Add support for `limits` and `manual_entry` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
* Add support for `require_payment_method_support` on `FinancialConnections.Session.Filter` and `financial_connections.SessionCreateParamsFilter`
* Add support for `bank_account_token` on `FinancialConnections.Session`
* Add support for new values `alipay` and `mb_way` on enums `Invoice.PaymentSetting.payment_method_types`, `InvoiceCreateParamsPaymentSetting.payment_method_types`, `InvoiceModifyParamsPaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, `SubscriptionCreateParamsPaymentSetting.payment_method_types`, and `SubscriptionModifyParamsPaymentSetting.payment_method_types`
* Add support for new values `mass_transit_parking_tax` and `parking_tax` on enums `InvoiceAddLinesParamsLineTaxAmountTaxRateDatum.tax_type`, `InvoiceLineItemModifyParamsTaxAmountTaxRateDatum.tax_type`, `InvoiceUpdateLinesParamsLineTaxAmountTaxRateDatum.tax_type`, `TaxRate.tax_type`, `TaxRateCreateParams.tax_type`, and `TaxRateModifyParams.tax_type`
* Add support for `metadata` on `InvoiceCreatePreviewParamsSubscriptionDetail`
* Add support for new value `stripe_internal_error` on enum `Issuing.Authorization.RequestHistory.reason`
* Add support for `business_name` on `Issuing.Card.Shipping`, `issuing.CardCreateParamsShipping`, and `issuing.CardModifyParamsShipping`
* Add support for new value `correos` on enum `Issuing.Card.Shipping.carrier`
* Add support for `allowed_payment_method_types` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentModifyParams`, `PaymentIntent`, `SetupIntentConfirmParams`, `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
* Add support for `referrer` on `PaymentIntentConfirmParamsRadarOption` and `PaymentIntentCreateParamsRadarOption`
* Add support for `consent_collection` and `shipping_options` on `PaymentLinkModifyParams`
* Add support for `custom_fields`, `description`, and `footer` on `Quote.InvoiceSetting`, `QuoteCreateParamsInvoiceSetting`, `QuoteModifyParamsInvoiceSetting`, `SubscriptionSchedule.DefaultSetting.InvoiceSetting`, `SubscriptionSchedule.Phase.InvoiceSetting`, `SubscriptionScheduleCreateParamsDefaultSettingInvoiceSetting`, `SubscriptionScheduleCreateParamsPhaseInvoiceSetting`, `SubscriptionScheduleModifyParamsDefaultSettingInvoiceSetting`, and `SubscriptionScheduleModifyParamsPhaseInvoiceSetting`
* Add support for `customer_account` and `customer` on `Refund`
* Add support for `payment_method` on `Refund` and `Topup`
* Add support for `trial` on `SubscriptionSchedule.Phase`
* Add support for `mass_transit_parking_tax` and `parking_tax` on `Tax.Registration.CountryOption.Me` and `tax.RegistrationCreateParamsCountryOptionMe`
* Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `tax.RegistrationCreateParamsCountryOptionMe.type`
* Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `Tax.Registration.CountryOption.Me.type`
* Add support for `initiated_by` and `payment_method_options` on `Topup`
* Add support for new values `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, `financial_connections.account.upcoming_deactivation`, `financial_connections.authorization.expected_deactivation_date_updated`, and `financial_connections.authorization.upcoming_deactivation` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for new value `2026-07-29.dahlia` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `additional_addresses` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, `v2.core.AccountModifyParamsIdentityBusinessDetail`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetail`
* Add support for snapshot events `financial_connections.account.expected_deactivation_date_updated`, `financial_connections.account.supported_payment_method_types_updated`, and `financial_connections.account.upcoming_deactivation` with resource `financial_connections.Account`
* Add support for snapshot events `financial_connections.authorization.expected_deactivation_date_updated` and `financial_connections.authorization.upcoming_deactivation` with resource `financial_connections.Authorization`
* Enum type annotations for non-exhaustive ("open") enums are now typed as `Union[Literal[...], str]` instead of plain `Literal[...]`. Many Stripe enums are open, meaning new values may appear in new versions of the API. This change ensures these fields have the correct type for both the values known at SDK release time and other values that may be added later. Refer to the [API Reference](https://docs.stripe.com) for the latest set of allowed values.
