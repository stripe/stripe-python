---
title: Update generated code
pr_url: https://github.com/stripe/stripe-python/pull/1998
semver_level: minor
is_stripe_api_change: true
---

* Add support for new resource `v2.core.ClaimableSandbox`
* Add support for `create`, `renew_onboarding_link`, and `retrieve` methods on resource `v2.core.ClaimableSandbox`
* Add support for `funding_sources` on `Charge.PaymentMethodDetail.Card.Wallet.Link` and `Charge.PaymentMethodDetail.Link`
* Add support for new value `tron` on enums `Charge.PaymentMethodDetail.Crypto.network`, `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network`, and `PaymentRecord.PaymentMethodDetail.Crypto.network`
* Add support for `fingerprint` on `Charge.PaymentMethodDetail.Paypay`, `PaymentAttemptRecord.PaymentMethodDetail.Paypay`, and `PaymentRecord.PaymentMethodDetail.Paypay`
* Add support for `address_collection_precision` on `Checkout.Session.AutomaticTax` and `checkout.SessionCreateParamsAutomaticTax`
* Change `Dispute.Evidence.appeal` to be required
* Change `Issuing.Card.Shipping.delivered_at` to be required
* Change `Issuing.Card.Shipping.shipped_at` to be required
* Change `PaymentAttemptRecord.PaymentMethodDetail.Card.stored_credential_usage` and `PaymentRecord.PaymentMethodDetail.Card.stored_credential_usage` to be required
* Add support for `car_rental_data` and `lodging_data` on `PaymentIntent.PaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
* Change type of `PaymentLinkCreateParamsPaymentIntentDatum.capture_method` from `enum('automatic'|'automatic_async'|'manual')` to `emptyable(enum('automatic'|'automatic_async'|'manual'))`
* Add support for `capture_method` on `PaymentLinkModifyParamsPaymentIntentDatum`
* Add support for `loss_message` on `Product.MarketingFeature`, `ProductCreateParamsMarketingFeature`, and `ProductModifyParamsMarketingFeature`
* Add support for `application` on `Refund`
* Add support for `bizum` and `upi` on `Refund.DestinationDetail`
* Add support for `tax_invoice_month` on `Reporting.ReportRun.Parameter` and `reporting.ReportRunCreateParamsParameter`
* Add support for `igic` on `Tax.Registration.CountryOption.E` and `tax.RegistrationCreateParamsCountryOptionE`
* Add support for new value `igic` on enums `Tax.Registration.CountryOption.E.type` and `tax.RegistrationCreateParamsCountryOptionE.type`
* Add support for new values `stripe_s700_devkit`, `stripe_s710_devkit`, `stripe_t600_devkit`, `verifone_ux700_devkit`, and `verifone_v660p_devkit` on enums `Terminal.Reader.device_type` and `terminal.ReaderListParams.device_type`
* Add support for `network_details` on `Treasury.InboundTransfer.FailureDetail`, `Treasury.OutboundPayment.ReturnedDetail`, `Treasury.OutboundTransfer.ReturnedDetail`, and `treasury.InboundTransferFailParamsFailureDetail`
* Add support for `failure_details` on `treasury.InboundTransferReturnInboundTransferParams`
* Add support for new value `2026-11-18.endive` on enum `WebhookEndpointCreateParams.api_version`
* Add support for `account_dashboard` on `V2.Core.AccountLink.UseCase` and `v2.core.AccountLinkCreateParamsUseCase`
* Add support for new value `account_dashboard` on enums `V2.Core.AccountLink.UseCase.type` and `v2.core.AccountLinkCreateParamsUseCase.type`
* Add support for `paypay_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `V2.Core.Account.Configuration.Merchant`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, `v2.core.AccountCreateParamsConfigurationMerchant`, `v2.core.AccountModifyParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchant`
* Add support for `billie_payments`, `mb_way_payments`, `nz_bank_account_becs_debit_payments`, and `pix_payments` on `V2.Core.Account.Configuration.Merchant.Capability`, `v2.core.AccountCreateParamsConfigurationMerchantCapability`, and `v2.core.AccountModifyParamsConfigurationMerchantCapability`
* Add support for `additional_material` on `V2.Core.Account.Configuration.Merchant.KonbiniPayment`, `v2.core.AccountCreateParamsConfigurationMerchantKonbiniPayment`, and `v2.core.AccountModifyParamsConfigurationMerchantKonbiniPayment`
* Add support for new values `billie_payments`, `mb_way_payments`, `nz_bank_account_becs_debit_payments`, `paypay_payments`, and `pix_payments` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for new values `billie_payments`, `mb_way_payments`, `nz_bank_account_becs_debit_payments`, `paypay_payments`, and `pix_payments` on enum `EventsV2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent.updated_capability`
* Add support for event notifications `V2CoreClaimableSandboxClaimedEvent`, `V2CoreClaimableSandboxCreatedEvent`, `V2CoreClaimableSandboxExpiredEvent`, `V2CoreClaimableSandboxExpiringEvent`, and `V2CoreClaimableSandboxUpdatedEvent` with related object `v2.core.ClaimableSandbox`
* Add support for error code `inactive_api_operation_confirmation_required` on `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, and `Terminal.Reader.Action.ApiError`
* Add support for error codes `claimable_sandbox_creation_rate_limit_exceeded` and `claimable_sandbox_testing_creation_rate_limit_exceeded` on `RateLimitError`
