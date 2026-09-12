---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1654
is_stripe_api_change: true
released_in_version: 13.2.0a1
---

* Add support for `report_refund` method on resource `PaymentRecord`
* Add support for new value `verification_data_not_found` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
* Add support for `tenants` on `Billing.Analytics.MeterUsageRow`
* Add support for `representative_declaration` on `Account.Company`, `AccountCreateParamsCompany`, `AccountModifyParamsCompany`, and `TokenCreateParamsAccountCompany`
* Add support for `transfer` on `ApplicationFee.FeeSource`
* Add support for new value `transfer` on enum `ApplicationFee.FeeSource.type`
* Add support for `transit_balances_total` on `Balance`
* Add support for new value `transit` on enum `BalanceTransaction.balance_type`
* Add support for `tenant_group_by_keys` on `billing.analytics.MeterUsageRetrieveParamsMeter`
* Change `billing.CreditGrantCreateParams.category` to be optional
* Add support for `payment_method_configuration` on `billing_portal.ConfigurationCreateParamsFeaturePaymentMethodUpdate` and `billing_portal.ConfigurationModifyParamsFeaturePaymentMethodUpdate`
* Add support for new value `solana` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
* Add support for `payment_portal_url` on `Charge.PaymentMethodDetail.Rechnung`, `PaymentAttemptRecord.PaymentMethodDetail.Rechnung`, and `PaymentRecord.PaymentMethodDetail.Rechnung`
* Add support for `twint` on `Checkout.Session.PaymentMethodOption` and `checkout.SessionCreateParamsPaymentMethodOption`
* Add support for new value `custom` on enums `ConfirmationToken.PaymentMethodPreview.type` and `PaymentMethod.type`
* Change `CreditNote.Refund.payment_record_refund` to be required
* Change `CreditNote.Refund.type` to be required
* Add support for `customer_sheet`, `mobile_payment_element`, and `tax_id_element` on `CustomerSession.Component` and `CustomerSessionCreateParamsComponent`
* Add support for new value `custom` on enums `CustomerListPaymentMethodsParams.type`, `PaymentMethodCreateParams.type`, and `PaymentMethodListParams.type`
* Add support for `provider` on `Customer.Tax`
* Remove support for `risk_details` on `delegated_checkout.RequestedSessionCreateParams`
* Add support for `risk_details` on `delegated_checkout.RequestedSessionConfirmParams`
* Add support for new value `platform_terms_of_service` on enums `File.purpose` and `FileListParams.purpose`
* Add support for new value `platform_terms_of_service` on enum `FileCreateParams.purpose`
* Add support for `starting_after` on `PaymentAttemptRecordListParams`
* Add support for `reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionKlarna`
* Add support for `allocated_funds` on `PaymentIntent`
* Change `PaymentIntent.PaymentDetail.customer_reference` to be required
* Change `PaymentIntent.PaymentDetail.order_reference` to be required
* Add support for `subscription_reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`
* Add support for `name_collection` on `PaymentLinkCreateParams`, `PaymentLinkModifyParams`, and `PaymentLink`
* Add support for `crypto` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, `PaymentMethodConfiguration`, and `Refund.DestinationDetail`
* Add support for `mb_way` on `PaymentMethodConfigurationCreateParams`, `PaymentMethodConfigurationModifyParams`, and `PaymentMethodConfiguration`
* Add support for `custom` on `PaymentMethodCreateParams` and `PaymentMethod`
* Add support for `excluded_payment_method_types` on `SetupIntentCreateParams`, `SetupIntentModifyParams`, and `SetupIntent`
* Change `SetupIntent.flow_directions` to be optional
* Add support for `tw` on `Tax.Registration.CountryOption` and `tax.RegistrationCreateParamsCountryOption`
* Add support for `gip` on `Terminal.Configuration.Tipping`, `terminal.ConfigurationCreateParamsTipping`, and `terminal.ConfigurationModifyParamsTipping`
* Add support for `last_seen_at` on `Terminal.Reader`
* Add support for `application_fee_amount` on `TransferCreateParams` and `Transfer`
* Add support for `application_fee` on `Transfer`
* Add support for new value `2025-10-29.clover` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `high_risk_activities_description`, `high_risk_activities`, `money_services_description`, `operates_in_prohibited_countries`, `participates_in_regulated_activity`, `purpose_of_funds_description`, `purpose_of_funds`, `regulated_activity`, `source_of_funds_description`, and `source_of_funds` on `V2.Core.Account.Configuration.Storer`, `v2.core.AccountCreateParamsConfigurationStorer`, and `v2.core.AccountModifyParamsConfigurationStorer`
* Add support for `crypto_wallets` on `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityFinancialAddress`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundPayment`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityOutboundTransfer`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityFinancialAddress`, `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundPayment`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityOutboundTransfer`
* Add support for `usdc` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
* Add support for `crypto_storer` on `V2.Core.Account.Identity.Attestation.TermsOfService` and `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`
* Add support for `compliance_screening_description` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.AccountCreateParamsIdentityBusinessDetail`, and `v2.core.AccountModifyParamsIdentityBusinessDetail`
* Add support for `external_amount` on `V2.MoneyManagement.ReceivedCredit` and `V2.MoneyManagement.ReceivedDebit`
* Add support for error code `payment_intent_rate_limit_exceeded` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `QuotePreviewInvoice.LastFinalizationError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, and `StripeError`
