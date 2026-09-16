---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1686
is_stripe_api_change: true
released_in_version: 14.1.0a4
---

* Add support for `check_scanning` on `AccountSession.Component`
* Add support for `client` on `V2.Core.Event.Reason.Request`
* Add support for `stripe_balance_payment` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
* Add support for new value `stripe_balance_payment` on enum `V2.MoneyManagement.ReceivedCredit.type`
* Add support for `balance_transfer` on `V2.MoneyManagement.ReceivedDebit`
* Add support for new values `balance_transfer` and `stripe_balance_payment` on enum `V2.MoneyManagement.ReceivedDebit.type`
* Add support for `include` on `v2.core.EventListParams` and `v2.core.EventRetrieveParams`
