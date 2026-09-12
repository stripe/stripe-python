---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1719
is_stripe_api_change: true
released_in_version: 14.4.0b1
---

* Add support for new resource `financial_connections.Authorization`
* Add support for `retrieve` method on resource `financial_connections.Authorization`
* Add support for `detach_payment` method on resource `Invoice`
* Remove support for `cancel`, `list_line_items`, and `reopen` methods on resource `Order`
* Remove support for `attach_cadence` method on resource `Subscription`
* Add support for `additional_files` and `site` on `Account.Setting.PaypayPayment`, `AccountCreateParamsSettingPaypayPayment`, and `AccountModifyParamsSettingPaypayPayment`
* Remove support for `capital` on `Account.Setting`
* Change type of `Charge.PaymentMethodDetail.StripeBalance.source_type`, `ConfirmationToken.PaymentMethodPreview.StripeBalance.source_type`, `PaymentAttemptRecord.PaymentMethodDetail.StripeBalance.source_type`, `PaymentMethod.StripeBalance.source_type`, and `PaymentRecord.PaymentMethodDetail.StripeBalance.source_type` from `enum('bank_account'|'card'|'fpx')` to `nullable(enum('bank_account'|'card'|'fpx'))`
* Add support for new value `pl_nip` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Order.TaxDetail.TaxId.type`, and `QuotePreviewInvoice.CustomerTaxId.type`
* Add support for new value `capital.financing_summary.line_of_credit_update` on enum `Event.type`
* Add support for `authorization` and `status_details` on `FinancialConnections.Account`
* Add support for `relink_options` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
* Change `financial_connections.SessionCreateParams.account_holder` to be optional
* Add support for `relink_result` on `FinancialConnections.Session`
* Remove support for `billing_cadence` on `InvoiceCreatePreviewParams`, `SubscriptionCreateParams`, `SubscriptionModifyParams`, and `Subscription`
* Remove support for `billing_cadence_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
* Remove support for value `billing_cadence_details` from enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`
* Add support for new value `pl_nip` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
* Add support for `car_rental_data`, `flight_data`, and `lodging_data` on `PaymentIntent.PaymentDetail`
* Change `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.payto` to be required
* Add support for new value `capital.financing_summary.line_of_credit_update` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for new values `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, and `vn_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `alternative_reference` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod`
* Add support for `account_holder_address` and `account_holder_name` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* Add support for `fingerprint` on `V2.MoneyManagement.PayoutMethod.Card`
* Add support for snapshot event `invoice_payment.detached` with resource `InvoicePayment`
* Add support for error code `request_blocked` on `QuotePreviewInvoice.LastFinalizationError`
* Add support for error codes `blocked_payout_method` and `unsupported_payout_method` on `BlockedByStripeError`
* Add support for error code `invalid_payout_method_data` on `InvalidPayoutMethodError`
* Add support for error code `limit_payout_method` on `QuotaExceededError`
