---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1727
is_stripe_api_change: true
released_in_version: 14.5.0b1
---

* Add support for `smart_disputes` on `Account.Setting`, `AccountCreateParamsSetting`, `AccountModifyParamsSetting`, `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
* Add support for `email_customers_on_successful_payment` on `Account.Setting.Payment`, `AccountCreateParamsSettingPayment`, and `AccountModifyParamsSettingPayment`
* Add support for `managed_payments` on `Checkout.Session`, `PaymentIntent`, `SetupIntent`, `Subscription`, and `checkout.SessionCreateParams`
* Add support for new value `lk_vat` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Order.TaxDetail.TaxId.type`, and `QuotePreviewInvoice.CustomerTaxId.type`
* Add support for new value `lk_vat` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
* Add support for new value `pay_by_bank` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Add support for new values `bt_bank_account`, `cr_bank_account`, `do_bank_account`, `gt_bank_account`, `md_bank_account`, `mk_bank_account`, `mo_bank_account`, `mz_bank_account`, `pe_bank_account`, `pk_bank_account`, `tw_bank_account`, and `uz_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `purpose` on `V2.MoneyManagement.OutboundPayment` and `v2.money_management.OutboundPaymentCreateParams`
* Add support for `branch_number` and `swift_code` on `V2.MoneyManagement.PayoutMethod.BankAccount`
* Change `V2.MoneyManagement.Transaction.flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.flow` to be optional
* Add support for error codes `storer_capability_missing` and `storer_capability_not_active` on `QuotePreviewInvoice.LastFinalizationError`
