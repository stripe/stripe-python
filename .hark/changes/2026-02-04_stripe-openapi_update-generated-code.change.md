---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1728
is_stripe_api_change: true
released_in_version: 14.4.0a2
---

* Add support for new resource `v2.core.ConnectionSession`
* Add support for `create` and `retrieve` methods on resource `v2.core.ConnectionSession`
* Add support for `list` method on resources `v2.payments.SettlementAllocationIntentSplit` and `v2.payments.SettlementAllocationIntent`
* Add support for `agentic_commerce_settings` on `AccountSessionCreateParamsComponent`
* Add support for `terminal_hardware_orders` and `terminal_hardware_shop` on `AccountSession.Component` and `AccountSessionCreateParamsComponent`
* Add support for `network_cost_passthrough_report` on `AccountSession.Component`
* Add support for new values `ae_bank_account`, `ag_bank_account`, `bh_bank_account`, `gm_bank_account`, `hk_bank_account`, `kh_bank_account`, `lc_bank_account`, `mc_bank_account`, `mg_bank_account`, `my_bank_account`, `qa_bank_account`, `rw_bank_account`, `th_bank_account`, `tt_bank_account`, and `vn_bank_account` on enums `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type` and `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
* Add support for `cadence_data` on `V2.Billing.Intent` and `v2.billing.IntentCreateParams`
* Add support for `cancellation_details` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.PricingPlanSubscription`, and `v2.billing.IntentCreateParamsActionDeactivate`
* Add support for `contact_phone` on `V2.Core.Account`, `v2.core.AccountCreateParams`, `v2.core.AccountModifyParams`, and `v2.core.AccountTokenCreateParams`
* Add support for `registration_date` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, `v2.core.AccountModifyParamsIdentityBusinessDetail`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetail`
* Add support for new value `gb_vat` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
* Add support for `reference` on `V2.MoneyManagement.Adjustment`
* Add support for `accrued_fees` on `V2.MoneyManagement.FinancialAccount`
* Add support for `starting_balance` on `V2.MoneyManagement.FinancialAccount.Payment`
* Add support for new value `accrued_fees` on enum `V2.MoneyManagement.FinancialAccount.type`
* Add support for `account_holder_address` and `account_holder_name` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
* Add support for `fingerprint` on `V2.MoneyManagement.PayoutMethod.Card`
* Add support for `card_spend` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
* Add support for new value `card_spend` on enum `V2.MoneyManagement.ReceivedCredit.type`
* Add support for new value `card_spend` on enum `V2.MoneyManagement.ReceivedDebit.type`
* Add support for new values `advance`, `anticipation_repayment`, `balance_transfer`, `charge_failure`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `connect_reserved_funds`, `contribution`, `dispute_reversal`, `financing_paydown_reversal`, `financing_paydown`, `inbound_transfer_reversal`, `issuing_dispute_fraud_liability_debit`, `issuing_dispute_provisional_credit_reversal`, `issuing_dispute_provisional_credit`, `issuing_dispute`, `minimum_balance_hold`, `network_cost`, `obligation`, `outbound_payment_reversal`, `outbound_transfer_reversal`, `partial_capture_reversal`, `payment_network_reserved_funds`, `platform_earning_refund`, `platform_earning`, `platform_fee`, `received_credit_reversal`, `received_debit_reversal`, `refund_failure`, `risk_reserved_funds`, `stripe_balance_payment_debit_reversal`, `stripe_balance_payment_debit`, `stripe_fee_tax`, `transfer_reversal`, and `unreconciled_customer_funds` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
* Add support for `application_fee_refund`, `application_fee`, `charge`, `dispute`, `payout`, `refund`, `reserve_hold`, `reserve_release`, `topup`, `transfer_reversal`, and `transfer` on `V2.MoneyManagement.Transaction.Flow` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow`
* Add support for new values `application_fee_refund`, `application_fee`, `charge`, `dispute`, `payout`, `refund`, `reserve_hold`, `reserve_release`, `topup`, `transfer_reversal`, and `transfer` on enums `V2.MoneyManagement.Transaction.Flow.type` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.Flow.type`
* Change `V2.Payments.SettlementAllocationIntentSplit.flow` to be optional
* Add support for new value `accrued_fees` on enum `v2.money_management.FinancialAccountListParams.types`
* Change `v2.billing.RateCardRateCreateParams.metered_item` to be required
* Add support for error codes `blocked_payout_method` and `unsupported_payout_method` on `BlockedByStripeError`
* Add support for error code `invalid_payout_method_data` on `InvalidPayoutMethodError`
* Add support for error code `limit_payout_method` on `QuotaExceededError`
