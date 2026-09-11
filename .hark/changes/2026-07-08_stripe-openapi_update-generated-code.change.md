---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1842
is_breaking: true
is_stripe_api_change: true
released_in_version: 15.4.0a3
---

* Add support for `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, and `reload_gift_card` methods on resource `terminal.Reader`
* Add support for `aggregation_period` on `Billing.AlertRecovered`
* ⚠️ Add support for new values `mass_transit_parking_tax` and `parking_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
* Add support for `administrative_address` and `principal_place_of_business` on `Account.Company`
* ⚠️ Add support for new values `bnp_paribas`, `citibank`, and `mbsb_bank` on enums `Charge.PaymentMethodDetail.Fpx.bank`, `ConfirmationToken.PaymentMethodPreview.Fpx.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Fpx.bank`, `PaymentMethod.Fpx.bank`, `PaymentRecord.PaymentMethodDetail.Fpx.bank`, and `SharedPayment.GrantedToken.PaymentMethodDetail.Fpx.bank`
* Add support for `address_collection_precision` on `Checkout.Session.AutomaticTax`
* Add support for `tax_id` on `Checkout.Session.CollectedInformation`
* ⚠️ Remove support for `tax_ids` on `Checkout.Session.CollectedInformation`
* Add support for `setup_future_usage` on `Checkout.Session.PaymentMethodOption.Payco`, `Checkout.Session.PaymentMethodOption.SamsungPay`, `PaymentIntent.PaymentMethodOption.Payco`, `PaymentIntent.PaymentMethodOption.Paypay`, `PaymentIntent.PaymentMethodOption.SamsungPay`, `PaymentIntentConfirmParamsPaymentMethodOptionPaypay`, `PaymentIntentCreateParamsPaymentMethodOptionPaypay`, and `PaymentIntentModifyParamsPaymentMethodOptionPaypay`
* Add support for `network` on `Dispute.PaymentMethodDetail.Card`
* Add support for `require_payment_method_support` on `FinancialConnections.Session.Filter`
* Add support for `network_data` on `Issuing.Authorization.RequestHistory`
* Add support for `acquiring_institution_country`, `acquiring_institution_id`, `retrieval_reference_number`, `routed_network`, and `trace_id` on `Issuing.Transaction.NetworkDatum`
* Add support for new values `boku_promptpay`, `capchase_pay`, `check_scan`, `click_to_pay`, `demo_pay`, `duitnow`, `dummy_auth_push`, `dummy_passthrough_card`, `edenred`, `gcash`, `getbalance`, `knet`, `kr_market`, `kriya`, `momo`, `mondu`, `netbanking`, `ng_bank_transfer`, `ng_bank`, `ng_card`, `ng_market`, `ng_ussd`, `ng_wallet`, `octopus`, `paper_check`, `sequra`, `shop_pay`, `south_korea_market`, `test_pay`, `truemoney`, `us_cash_voucher`, `vipps`, and `wero` on enums `PaymentIntentConfirmParams.allowed_payment_method_types`, `PaymentIntentCreateParams.allowed_payment_method_types`, and `PaymentIntentModifyParams.allowed_payment_method_types`
* Add support for `custom_fields`, `description`, and `footer` on `Quote.InvoiceSetting`, `QuotePreviewSubscriptionSchedule.DefaultSetting.InvoiceSetting`, `QuotePreviewSubscriptionSchedule.Phase.InvoiceSetting`, `SubscriptionSchedule.DefaultSetting.InvoiceSetting`, and `SubscriptionSchedule.Phase.InvoiceSetting`
* Add support for `paypay` on `SetupAttempt.PaymentMethodDetail`
* Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `tax.RegistrationCreateParamsCountryOptionMe.type`
* Add support for `mass_transit_parking_tax` and `parking_tax` on `Tax.Registration.CountryOption.Me`
* ⚠️ Add support for new values `mass_transit_parking_tax` and `parking_tax` on enum `Tax.Registration.CountryOption.Me.type`
* Add support for `gift_card_brand` on `terminal.ReaderCollectPaymentMethodParamsCollectConfig` and `terminal.ReaderProcessPaymentIntentParamsProcessConfig`
* Add support for `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, `deactivate_gift_card`, and `reload_gift_card` on `Terminal.Reader.Action`
* ⚠️ Add support for new values `activate_gift_card`, `cashout_gift_card`, `check_gift_card_balance`, `deactivate_gift_card`, and `reload_gift_card` on enum `Terminal.Reader.Action.type`
* Add support for `status_transitions` on `V2.Billing.Contract`
* ⚠️ Remove support for `one_time_fees` on `V2.Billing.Contract` and `v2.billing.ContractCreateParams`
* ⚠️ Remove support for `status_details` on `V2.Billing.Contract`
* Add support for `id` and `priority` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`
* ⚠️ Remove support for `pricing_override` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum`
* ⚠️ Remove support for `tiering_mode` and `tiers` on `V2.Billing.Contract.PricingLine.Datum.Pricing.PriceDetail.PricingOverride.Datum.OverwritePrice`, `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideOverwritePrice`, `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideOverwritePrice`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddOverwritePrice`, and `v2.billing.ContractModifyParamsPricingOverrideActionAddOverwritePrice`
* Add support for `multiply_pricing` on `V2.Billing.Contract.PricingOverride.Datum`, `v2.billing.ContractCreateParamsPricingOverride`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd`
* ⚠️ Remove support for `multiplier` on `V2.Billing.Contract.PricingOverride.Datum`, `v2.billing.ContractCreateParamsPricingOverride`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd`
* ⚠️ Change type of `V2.Billing.Contract.PricingOverride.Datum.type`, `v2.billing.ContractCreateParamsPricingOverride.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.type` from `literal('multiplier')` to `literal('multiply_pricing')`
* Add support for `related_network_object` on `V2.Core.Account` and `v2.core.AccountListParams`
* ⚠️ Add support for new value `network_business_profile_wallet` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `network_business_profile_wallet` on `V2.MoneyManagement.PayoutMethod`
* Add support for new value `network_business_profile_wallet` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatum.type`
* Add support for `stripe_network_transfer` on `V2.MoneyManagement.ReceivedCredit`
* Add support for new value `stripe_network_transfer` on enum `V2.MoneyManagement.ReceivedCredit.type`
* ⚠️ Remove support for value `one_time_fees` from enums `v2.billing.ContractActivateParams.include`, `v2.billing.ContractCancelParams.include`, `v2.billing.ContractCreateParams.include`, `v2.billing.ContractListParams.include`, `v2.billing.ContractModifyParams.include`, and `v2.billing.ContractRetrieveParams.include`
* ⚠️ Change type of `v2.billing.ContractCreateParamsPricingLineEndsAt.type`, `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideEndsAt.type`, `v2.billing.ContractCreateParamsPricingOverrideEndsAt.type`, and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideEndsAt.type` from `enum('contract_end'|'timestamp')` to `literal('timestamp')`
* ⚠️ Change type of `v2.billing.ContractCreateParamsPricingLinePricingPriceDetailPricingOverrideStartsAt.type`, `v2.billing.ContractCreateParamsPricingLineStartsAt.type`, `v2.billing.ContractCreateParamsPricingOverrideStartsAt.type`, and `v2.billing.ContractModifyParamsPricingLineActionAddPricingPriceDetailPricingOverrideStartsAt.type` from `enum('contract_start'|'timestamp')` to `literal('timestamp')`
* Change `v2.billing.ContractCreateParamsPricingOverride.priority` and `v2.billing.ContractModifyParamsPricingOverrideActionAdd.priority` to be optional
* ⚠️ Change type of `v2.billing.ContractModifyParamsPricingLineActionAddEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdateEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddEndsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdateEndsAt.type`, `v2.billing.ContractModifyParamsPricingOverrideActionAddEndsAt.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionUpdateEndsAt.type` from `enum('billing_period_end'|'timestamp')` to `literal('timestamp')`
* ⚠️ Change type of `v2.billing.ContractModifyParamsPricingLineActionAddStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionAddStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdatePricingPriceDetailPricingOverrideActionUpdateStartsAt.type`, `v2.billing.ContractModifyParamsPricingLineActionUpdateStartsAt.type`, `v2.billing.ContractModifyParamsPricingOverrideActionAddStartsAt.type`, and `v2.billing.ContractModifyParamsPricingOverrideActionUpdateStartsAt.type` from `enum('billing_period_start'|'timestamp')` to `literal('timestamp')`
* Add support for event notifications `V2BillingContractActivatedEvent`, `V2BillingContractCanceledEvent`, `V2BillingContractCreatedEvent`, `V2BillingContractEndedEvent`, and `V2BillingContractUpdatedEvent` with related object `v2.billing.Contract`
