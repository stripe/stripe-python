---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1276
is_stripe_api_change: true
released_in_version: 8.9.0
---

* Add support for new resources `Billing.MeterEventAdjustment`, `Billing.MeterEvent`, and `Billing.Meter`
* Add support for `create`, `deactivate`, `list`, `modify`, `reactivate`, and `retrieve` methods on resource `Meter`
* Add support for `create` method on resources `MeterEventAdjustment` and `MeterEvent`
* Add support for `amazon_pay_payments` on `Account.Capabilities`, `Account.CreateParamsCapabilities`, `Account.UpdateParamsCapabilities`,`AccountService.CreateParamsCapabilities`, and `AccountService.UpdateParamsCapabilities`
* Add support for new value `verification_failed_representative_authority` on enums `Account.FutureRequirements.Error.code`, `Account.Requirements.Errors.code`, `BankAccount.FutureRequirements.Error.code`, `BankAccount.Requirements.Errors.code`, `Capability.FutureRequirements.Error.code`, `Capability.Requirements.Errors.code`, `Person.FutureRequirements.Error.code`, `Person.Requirements.Errors.code`,
* Add support for `destination_on_behalf_of_charge_management` on `AccountSession.Components.PaymentDetails.Features`, `AccountSession.Components.Payments.Features`, `AccountSession.CreateParamsComponentsPaymentDetailsFeatures`, `AccountSession.CreateParamsComponentsPaymentsFeatures`, `AccountSessionService.CreateParamsComponentsPaymentDetailsFeatures` and `AccountSessionService.CreateParamsComponentsPaymentsFeatures`
* Add support for `meter` on `Plan.CreateParams`, `Plan`, `PlanService.CreateParams`, `Price.Recurring`, `Price.CreateParamsRecurring`, `Price.ListParamsRecurring`, `PriceService.CreateParamsRecurring`, and `PriceService.ListParamsRecurring`
* Add support for `mandate` on `Charge.PaymentMethodDetails.USBankAccount`, `Treasury.InboundTransfer.OriginPaymentMethodDetails.USBankAccount`, `Treasury.OutboundPayment.DestinationPaymentMethodDetails.USBankAccount`, and `Treasury.OutboundTransfer.DestinationPaymentMethodDetails.USBankAccount`
* Add support for `second_line` on `Issuing.Card.CreateParams`
