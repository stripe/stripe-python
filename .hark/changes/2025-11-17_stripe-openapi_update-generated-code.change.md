---
title: Update generated code for beta
pr_url: https://github.com/stripe/stripe-python/pull/1663
is_stripe_api_change: true
released_in_version: 14.1.0b1
---

* Add support for new resources `v2.core.AccountPersonToken` and `v2.core.AccountToken`
* Remove support for resource `v2.payments.OffSessionPayment`
* Add support for `create` and `retrieve` methods on resources `v2.core.AccountPersonToken` and `v2.core.AccountToken`
* Remove support for `cancel`, `capture`, `create`, `list`, and `retrieve` methods on resource `v2.payments.OffSessionPayment`
* Change `Tax.Association.tax_transaction_attempts` to be required
* Add support for `specified_commercial_transactions_act_url` on `Account.BusinessProfile`, `AccountCreateParamsBusinessProfile`, and `AccountModifyParamsBusinessProfile`
* Add support for `paypay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
* Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.dimension_filters` from `string` to `array(string)`
* Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.tenant_filters` from `string` to `array(string)`
* Add support for `car_rental_data`, `flight_data`, and `lodging_data` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
* Add support for `supplementary_purchase_data` on `OrderCreateParamsPaymentSettingPaymentMethodOptionKlarna`, `OrderModifyParamsPaymentSettingPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsPaymentMethodOptionKlarna`
* Add support for `allow_redisplay` and `customer_account` on `PaymentMethodListParams`
* Add support for `future_requirements` on `V2.Core.Account`
* Add support for `konbini_payments` and `script_statement_descriptor` on `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchant`, and `v2.core.AccountModifyParamsConfigurationMerchant`
* Add support for `eur` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
* Add support for `requirements_collector` on `V2.Core.Account.Default.Responsibility`
* Add support for new value `ar_cuit` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`
* Add support for new value `ar_dni` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, and `v2.core.AccountPersonModifyParamsIdNumber.type`
* Remove support for `collector` on `V2.Core.Account.Requirement`
* Add support for new value `holds_currencies.eur` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new values `payment_method` and `person` on enum `V2.Core.Account.Requirement.Entry.Reference.type`
* Remove support for value `resource` from enum `V2.Core.Account.Requirement.Entry.Reference.type`
* Remove support for value `future_requirements` from enum `V2.Core.Account.Requirement.Entry.RequestedReason.code`
* Add support for `changes` on `V2.Core.Event`
* Remove support for value `sepa_bank_account` from enums `V2.MoneyManagement.FinancialAddress.Credential.type` and `v2.money_management.FinancialAddressCreateParams.type`
* Add support for `account_token` on `v2.core.AccountCreateParams` and `v2.core.AccountModifyParams`
* Add support for new value `future_requirements` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* Add support for `person_token` on `v2.core.AccountPersonCreateParams` and `v2.core.AccountPersonModifyParams`
* Add support for thin event `V2CoreHealthEventGenerationFailureResolvedEvent`
* Remove support for thin events `V2PaymentsOffSessionPaymentAuthorizationAttemptFailedEvent`, `V2PaymentsOffSessionPaymentAuthorizationAttemptStartedEvent`, `V2PaymentsOffSessionPaymentCanceledEvent`, `V2PaymentsOffSessionPaymentCreatedEvent`, `V2PaymentsOffSessionPaymentFailedEvent`, `V2PaymentsOffSessionPaymentRequiresCaptureEvent`, and `V2PaymentsOffSessionPaymentSucceededEvent` with related object `v2.payments.OffSessionPayment`
