---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1542
is_stripe_api_change: true
released_in_version: 12.6.0b1
---

* Add support for `list` and `retrieve` methods on resource `InvoicePayment`
* Add support for `list` method on resource `Mandate`
* Add support for `applied` on `V2.Core.Account.Configuration.Customer`, `V2.Core.Account.Configuration.Merchant`, `V2.Core.Account.Configuration.Recipient`, `V2.Core.Account.Configuration.Storer`, `v2.core.Account.ModifyParamsConfigurationCustomer`, `v2.core.Account.ModifyParamsConfigurationMerchant`, `v2.core.Account.ModifyParamsConfigurationRecipient`, and `v2.core.Account.ModifyParamsConfigurationStorer`
* Add support for new values `ao_nif`, `az_tin`, `bd_etin`, `cr_cpj`, `cr_nite`, `do_rcn`, `gt_nit`, `kz_bin`, `mz_nuit`, `pe_ruc`, `pk_ntn`, `sa_crn`, and `sa_tin` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.Account.CreateParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.Account.ModifyParamsIdentityBusinessDetailIdNumber.type`
* Add support for new values `ao_nif`, `az_tin`, `bd_brc`, `bd_etin`, `bd_nid`, `cr_cpf`, `cr_dimex`, `cr_nite`, `do_rcn`, `gt_nit`, `kz_iin`, `mz_nuit`, `pe_dni`, `pk_cnic`, `pk_snic`, and `sa_tin` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.Person.IdNumber.type`, `v2.core.Account.CreateParamsIdentityIndividualIdNumber.type`, `v2.core.Account.ModifyParamsIdentityIndividualIdNumber.type`, `v2.core.Person.CreateParamsIdNumber.type`, and `v2.core.Person.ModifyParamsIdNumber.type`
* Change type of `Billing.AlertTriggered.value` from `longInteger` to `decimal_string`
* Add support for `display_name` on `V2.MoneyManagement.FinancialAccount` and `v2.money_management.FinancialAccount.CreateParams`
* Add support for new value `currency_conversion` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for `currency_conversion` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* Add support for new value `currency_conversion` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Add support for `payments` on `BalanceSettings.ModifyParams` and `BalanceSettings`
* Remove support for `debit_negative_balances`, `payouts`, and `settlement_timing` on `BalanceSettings.ModifyParams` and `BalanceSettings`
* Add support for `mandate` on `Charge.PaymentMethodDetail.Pix`, `PaymentAttemptRecord.PaymentMethodDetail.Pix`, and `PaymentRecord.PaymentMethodDetail.Pix`
* Add support for `coupon_data` on `checkout.Session.CreateParamsDiscount`
* Add support for `mandate_options` on `Checkout.Session.PaymentMethodOption.Pix`, `PaymentIntent.ConfirmParamsPaymentMethodOptionPix`, `PaymentIntent.CreateParamsPaymentMethodOptionPix`, `PaymentIntent.ModifyParamsPaymentMethodOptionPix`, `PaymentIntent.PaymentMethodOption.Pix`, and `checkout.Session.CreateParamsPaymentMethodOptionPix`
* Change type of `Checkout.Session.PaymentMethodOption.Pix.setup_future_usage`, `PaymentIntent.ConfirmParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntent.CreateParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntent.ModifyParamsPaymentMethodOptionPix.setup_future_usage`, `PaymentIntent.PaymentMethodOption.Pix.setup_future_usage`, and `checkout.Session.CreateParamsPaymentMethodOptionPix.setup_future_usage` from `literal('none')` to `enum('none'|'off_session')`
* Add support for `amount` on `Mandate.MultiUse`, `PaymentAttemptRecord`, and `PaymentRecord`
* Add support for `currency` on `Mandate.MultiUse`
* Add support for `pix` on `Mandate.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.ConfirmParamsPaymentMethodOption`, `SetupIntent.CreateParamsPaymentMethodOption`, `SetupIntent.ModifyParamsPaymentMethodOption`, and `SetupIntent.PaymentMethodOption`
* Add support for `limit` on `PaymentAttemptRecord.ListParams`
* Add support for `amount_authorized`, `amount_refunded`, and `application` on `PaymentAttemptRecord` and `PaymentRecord`
* Add support for `processor_details` on `PaymentAttemptRecord`, `PaymentRecord.ReportPaymentParams`, and `PaymentRecord`
* Remove support for `payment_reference` on `PaymentAttemptRecord`, `PaymentRecord.ReportPaymentParams`, and `PaymentRecord`
* Add support for `installments` on `PaymentAttemptRecord.PaymentMethodDetail.Alma` and `PaymentRecord.PaymentMethodDetail.Alma`
* Add support for `transaction_id` on `PaymentAttemptRecord.PaymentMethodDetail.Alma`, `PaymentAttemptRecord.PaymentMethodDetail.AmazonPay`, `PaymentAttemptRecord.PaymentMethodDetail.Billie`, `PaymentAttemptRecord.PaymentMethodDetail.KakaoPay`, `PaymentAttemptRecord.PaymentMethodDetail.KrCard`, `PaymentAttemptRecord.PaymentMethodDetail.NaverPay`, `PaymentAttemptRecord.PaymentMethodDetail.Payco`, `PaymentAttemptRecord.PaymentMethodDetail.RevolutPay`, `PaymentAttemptRecord.PaymentMethodDetail.SamsungPay`, `PaymentAttemptRecord.PaymentMethodDetail.Satispay`, `PaymentRecord.PaymentMethodDetail.Alma`, `PaymentRecord.PaymentMethodDetail.AmazonPay`, `PaymentRecord.PaymentMethodDetail.Billie`, `PaymentRecord.PaymentMethodDetail.KakaoPay`, `PaymentRecord.PaymentMethodDetail.KrCard`, `PaymentRecord.PaymentMethodDetail.NaverPay`, `PaymentRecord.PaymentMethodDetail.Payco`, `PaymentRecord.PaymentMethodDetail.RevolutPay`, `PaymentRecord.PaymentMethodDetail.SamsungPay`, and `PaymentRecord.PaymentMethodDetail.Satispay`
* Add support for `location` and `reader` on `PaymentAttemptRecord.PaymentMethodDetail.Paynow` and `PaymentRecord.PaymentMethodDetail.Paynow`
* Add support for `latest_active_mandate` on `PaymentMethod`
* Change `Payout.payout_method` to be required
* Add support for `metadata` and `period` on `QuotePreviewSubscriptionSchedule.Phase.AddInvoiceItem`
* Add support for `pix_display_qr_code` on `SetupIntent.NextAction`
* Add support for `reader_security` on `Terminal.Configuration`, `terminal.Configuration.CreateParams`, and `terminal.Configuration.ModifyParams`
* Add support for error codes `customer_session_expired` and `india_recurring_payment_mandate_canceled` on `QuotePreviewInvoice.LastFinalizationError`
