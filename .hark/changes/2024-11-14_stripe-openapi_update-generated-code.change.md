---
title: Update generated code for beta
pr_link: https://github.com/stripe/stripe-python/pull/1422
is_stripe_api_change: true
released_in_version: 11.3.0b3
---

* Add support for `account_holder_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin`
* Add support for `bank_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin`
* Add support for `account_holder_name` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei` and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`
* Add support for `subscribe` on enum `stripe.PaymentLink.ModifyParams.submit_type`
