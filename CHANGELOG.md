<!--
THIS IS A GENERATED FILE. Any changes you make to it directly will be blown away.
Instead, edit a corresponding `.change.md` file and run `hark build`.
-->

# Changelog

> This changelog only covers the **public preview** releases. Each release builds on the most recent GA release; see those notes in [the GA changelog](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md).

## 15.7.0b1 - 2026-08-26
This release changes the pinned API version to `2026-08-26.preview`.

* [#1878](https://github.com/stripe/stripe-python/pull/1878) Add non-verified methods to managed handlers
* ⚠️ [#1858](https://github.com/stripe/stripe-python/pull/1858) Update generated code for beta
  * Add support for new resources `v2.core.ApprovalRequest`, `v2.signals.AccountActivity`, `v2.signals.AccountEvaluation`, and `v2.signals.AccountSignal`
  * Add support for `list` and `retrieve` methods on resource `v2.signals.AccountSignal`
  * Add support for `create` and `retrieve` methods on resource `v2.signals.AccountEvaluation`
  * Add support for `create`, `delete`, and `retrieve` methods on resource `v2.signals.AccountActivity`
  * Add support for `cancel`, `list`, `modify`, and `retrieve` methods on resource `v2.core.ApprovalRequest`
  * Add support for `disable` method on resource `v2.money_management.PayoutMethod`
  * Add support for `disable_stripe_user_authentication` on `AccountSessionCreateParamsComponentPaymentMethodSettingFeature`
  * ⚠️ Remove support for `payment_method_types` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, `PaymentIntentModifyParams`, `SetupIntentCreateParams`, and `SetupIntentModifyParams`
  * ⚠️ Change type of `ProductCatalog.TrialOffer.EndBehavior.Transition.price` and `ProductCatalog.TrialOffer.price` from `$Price` to `deletable($Price)`
  * Add support for `billie` on `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`
  * Add support for new value `billie` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Add support for `payout_methods` on `V2.Core.Account.Default` and `v2.core.AccountModifyParamsDefault`
  * Add support for `restricted` on `V2.Core.Vault.GbBankAccount` and `V2.Core.Vault.UsBankAccount`
  * Add support for `enabled_delivery_schemes` on `V2.MoneyManagement.PayoutMethod.BankAccount`
  * ⚠️ Remove support for `enabled_delivery_options` on `V2.MoneyManagement.PayoutMethod.BankAccount`
  * ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.payments`
  * ⚠️ Add support for new value `disabled` on enum `V2.MoneyManagement.PayoutMethod.UsageStatus.transfers`
  * Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.payments`
  * Add support for new value `disabled` on enum `v2.money_management.PayoutMethodListParamsUsageStatus.transfers`
  * Add support for event notifications `V2CoreApprovalRequestApprovedEvent`, `V2CoreApprovalRequestCanceledEvent`, `V2CoreApprovalRequestCreatedEvent`, `V2CoreApprovalRequestExpiredEvent`, `V2CoreApprovalRequestFailedEvent`, `V2CoreApprovalRequestRejectedEvent`, and `V2CoreApprovalRequestSucceededEvent` with related object `v2.core.ApprovalRequest`
  * Add support for event notification `V2SignalsAccountEvaluationCompleteEvent` with related object `v2.signals.AccountEvaluation`
  * Add support for error codes `authentication_failure`, `capability_not_active`, `expired_payment_method`, `incorrect_postal_code`, `invalid_canceled_subscription_fields`, and `payment_method_restricted` on `QuotePreviewInvoice.LastFinalizationError`
  * Add support for error code `default_payout_method_cannot_be_disabled` on `CannotProceedError`

## 15.5.0b1 - 2026-07-29
This release changes the pinned API version to `2026-07-29.preview`.

* ⚠️ [#1838](https://github.com/stripe/stripe-python/pull/1838) Update generated code for beta
  * Add support for `list` and `retrieve` methods on resource `product_catalog.TrialOffer`
  * Add support for `tax_items` on `ChargeCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeCaptureParamsPaymentDetailFlightDatumTotalTax`, `ChargeCaptureParamsPaymentDetailLodgingDatumTotalTax`, `ChargeModifyParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeModifyParamsPaymentDetailFlightDatumTotalTax`, `ChargeModifyParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`, `PaymentIntentCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailFlightDatumTotalTax`, and `PaymentIntentModifyParamsPaymentDetailLodgingDatumTotalTax`
  * ⚠️ Remove support for `taxes` on `ChargeCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeCaptureParamsPaymentDetailFlightDatumTotalTax`, `ChargeCaptureParamsPaymentDetailLodgingDatumTotalTax`, `ChargeModifyParamsPaymentDetailCarRentalDatumTotalTax`, `ChargeModifyParamsPaymentDetailFlightDatumTotalTax`, `ChargeModifyParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntent.PaymentDetail.CarRentalDatum.Total.Tax`, `PaymentIntent.PaymentDetail.FlightDatum.Total.Tax`, `PaymentIntent.PaymentDetail.LodgingDatum.Total.Tax`, `PaymentIntentCaptureParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCaptureParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentConfirmParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailFlightDatumTotalTax`, `PaymentIntentCreateParamsPaymentDetailLodgingDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailCarRentalDatumTotalTax`, `PaymentIntentModifyParamsPaymentDetailFlightDatumTotalTax`, and `PaymentIntentModifyParamsPaymentDetailLodgingDatumTotalTax`
  * Add support for `tax_id` on `Checkout.Session.CollectedInformation`
  * ⚠️ Remove support for `tax_ids` on `Checkout.Session.CollectedInformation`
  * Add support for new value `disabled` on enum `financial_connections.SessionCreateParamsManualEntry.mode`
  * Add support for `mode` on `FinancialConnections.Session.ManualEntry`
  * Add support for `name` on `issuing.CardholderModifyParams`
  * Add support for new value `ic_nif` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
  * ⚠️ Add support for new value `ic_nif` on enums `Order.TaxDetail.TaxId.type` and `QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for new values `alipay` and `mb_way` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Add support for `custom_fields`, `description`, and `footer` on `QuotePreviewSubscriptionSchedule.DefaultSetting.InvoiceSetting` and `QuotePreviewSubscriptionSchedule.Phase.InvoiceSetting`
  * Add support for `trial` on `QuotePreviewSubscriptionSchedule.Phase`
  * ⚠️ Remove support for `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `customer_balance`, `eps`, `fpx`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` on `SharedPayment.GrantedToken.PaymentMethodDetail`
  * ⚠️ Remove support for values `acss_debit`, `afterpay_clearpay`, `alipay`, `alma`, `amazon_pay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `billie`, `bizum`, `blik`, `boleto`, `card_present`, `cashapp`, `crypto`, `custom`, `customer_balance`, `eps`, `fpx`, `giropay`, `gopay`, `grabpay`, `id_bank_transfer`, `ideal`, `interac_present`, `kakao_pay`, `konbini`, `kr_card`, `mb_way`, `mobilepay`, `multibanco`, `naver_pay`, `nz_bank_account`, `oxxo`, `p24`, `pay_by_bank`, `payco`, `paynow`, `paypal`, `paypay`, `payto`, `pix`, `promptpay`, `qris`, `rechnung`, `revolut_pay`, `samsung_pay`, `satispay`, `scalapay`, `sepa_debit`, `shopeepay`, `sofort`, `stripe_balance`, `sunbit`, `swish`, `twint`, `upi`, `us_bank_account`, `wechat_pay`, and `zip` from enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * Add support for `use_stripe_sdk` on `SharedPayment.IssuedToken` and `shared_payment.IssuedTokenCreateParams`
  * Add support for `redirect_to_url` on `SharedPayment.IssuedToken.NextAction`
  * ⚠️ Change type of `SharedPayment.IssuedToken.NextAction.type` from `literal('use_stripe_sdk')` to `enum('redirect_to_url'|'use_stripe_sdk')`
  * Add support for `livemode` on `Tax.Location`
  * Add support for `source` on `V2.Iam.ActivityLog.Detail.UserRole`
  * Add support for `payout` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
  * ⚠️ Remove support for `payout_v1` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
  * Add support for new value `payout` on enum `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type`
  * ⚠️ Change `V2.MoneyManagement.ReceivedDebit.BankTransfer.us_bank_account` to be optional
  * Add support for error codes `us_bank_account_microdeposits_cannot_be_confirmed` and `us_bank_account_microdeposits_cannot_be_sent` on `ControlledByAlternateResourceError`

## 15.4.0b1 - 2026-06-24
This release changes the pinned API version to `2026-06-24.preview`.

* ⚠️ [#1819](https://github.com/stripe/stripe-python/pull/1819) Update generated code for beta
  * Add support for `redaction` on `Card`, `Charge`, `Checkout.Session`, `Customer`, `Issuing.Authorization`, `Issuing.Card`, `Issuing.Cardholder`, `Issuing.Dispute`, `Issuing.Transaction`, `PaymentIntent`, `PaymentMethod`, `SetupIntent`, `Source`, and `Token`
  * Add support for `disclaimer_variant` on `Capital.FinancingOffer` and `Capital.FinancingSummary.Detail`
  * Add support for `active` on `FinancialConnections.Account.StatusDetail` and `FinancialConnections.Authorization.StatusDetail`
  * ⚠️ Add support for new value `institution_requirement` on enum `FinancialConnections.Account.StatusDetail.Inactive.cause`
  * Change type of `financial_connections.SessionCreateParamsLimit.accounts` from `longInteger` to `emptyable(longInteger)`
  * Add support for `pause` on `InvoiceCreatePreviewParamsSubscriptionDetail`
  * ⚠️ Add support for new value `satispay` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Add support for `release_details` on `Reserve.Hold`
  * Add support for `buyer_id` on `SharedPayment.GrantedToken.PaymentMethodDetail.Bizum` and `SharedPayment.GrantedToken.PaymentMethodDetail.Blik`
  * Add support for `fingerprint` on `SharedPayment.GrantedToken.PaymentMethodDetail.Pix`
  * ⚠️ Remove support for value `invoice_payment.detached` from enum `WebhookEndpointModifyParams.enabled_events`
  * ⚠️ Add support for new value `money_manager` on enums `EventsV2CoreAccountLinkReturnedEvent.configurations`, `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, and `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`
  * ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
  * ⚠️ Remove support for value `storer` from enums `V2.Core.Account.applied_configurations`, `v2.core.AccountCloseParams.applied_configurations`, and `v2.core.AccountListParams.applied_configurations`
  * Add support for `money_manager` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * ⚠️ Remove support for `storer` on `V2.Core.Account.Configuration`, `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.AccountCreateParamsConfiguration`, `v2.core.AccountCreateParamsIdentityAttestationTermsOfService`, `v2.core.AccountModifyParamsConfiguration`, and `v2.core.AccountTokenCreateParamsIdentityAttestationTermsOfService`
  * ⚠️ Add support for new values `business_storage.inbound.eur`, `business_storage.inbound.gbp`, `business_storage.inbound.usd`, `business_storage.outbound.eur`, `business_storage.outbound.gbp`, `business_storage.outbound.usd`, `received_credits.bank_accounts`, and `received_debits.bank_accounts` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * ⚠️ Add support for new value `money_manager` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.configuration` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
  * ⚠️ Remove support for `maximum_rps` on `V2.Core.BatchJob` and `v2.core.BatchJobCreateParams`
  * Add support for `bic` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
  * ⚠️ Remove support for `swift_code` on `V2.MoneyManagement.FinancialAddress.Credential.UsBankAccount`
  * Add support for `processing` on `V2.MoneyManagement.OutboundPayment.StatusDetail` and `V2.MoneyManagement.OutboundTransfer.StatusDetail`
  * ⚠️ Add support for new values `fx_rate_drift_exceeded_after_review`, `payout_method_amount_limit_exceeded`, and `review_rejected` on enum `V2.MoneyManagement.OutboundPayment.StatusDetail.Failed.reason`
  * ⚠️ Add support for new values `fx_rate_drift_exceeded_after_review` and `review_rejected` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
  * Add support for `account_holder_name` on `V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount`
  * ⚠️ Add support for new value `capability_inactive` on enum `V2.MoneyManagement.ReceivedDebit.StatusDetail.Failed.reason`
  * Add support for `statuses` on `v2.money_management.FinancialAccountListParams`
  * ⚠️ Remove support for `status` on `v2.money_management.FinancialAccountListParams`
  * Change `v2.core.BatchJobCreateParams.metadata` to be optional
  * Add support for new value `money_manager` on enums `v2.core.AccountLinkCreateParamsUseCaseAccountOnboarding.configurations` and `v2.core.AccountLinkCreateParamsUseCaseAccountUpdate.configurations`
  * ⚠️ Add support for new value `configuration.money_manager` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * ⚠️ Remove support for value `configuration.storer` from enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
  * Add support for event notifications `V2CoreAccountIncludingConfigurationMoneyManagerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationMoneyManagerUpdatedEvent` with related object `v2.core.Account`
  * Add support for event notification `V2MoneyManagementOutboundPaymentUnderReviewEvent` with related object `v2.money_management.OutboundPayment`
  * Add support for event notification `V2MoneyManagementOutboundTransferUnderReviewEvent` with related object `v2.money_management.OutboundTransfer`
  * ⚠️ Remove support for event notifications `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
  * Add support for error codes `anomalous_money_movement_request`, `failed_tax_calculation`, `financial_account_balance_does_not_support_currency`, `financial_account_capability_not_enabled`, and `financial_account_capability_restricted` on `QuotePreviewInvoice.LastFinalizationError`
  * Add support for error code `default_us_bank_account_cannot_be_archived` on `CannotProceedError`

## 15.3.0b1 - 2026-05-27
This release changes the pinned API version to `2026-05-27.preview`.

* ⚠️ [#1801](https://github.com/stripe/stripe-python/pull/1801) Update generated code for beta
  * Add support for `pause` method on resource `Subscription`
  * Add support for `retrieve` method on resource `v2.iam.ActivityLog`
  * ⚠️ Add support for new value `mastercard` on enum `Issuing.Settlement.network`
  * ⚠️ Change type of `ProductCatalog.TrialOffer.EndBehavior.Transition.price` from `string` to `expandable($Price)`
  * Add support for `amount_paid_off_stripe` on `QuotePreviewInvoice`
  * ⚠️ Add support for new value `twint` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Add support for `discountable` on `QuotePreviewSubscriptionSchedule.Phase.AddInvoiceItem`
  * Add support for `bizum` and `scalapay` on `SharedPayment.GrantedToken.PaymentMethodDetail`
  * ⚠️ Add support for new values `bizum` and `scalapay` on enum `SharedPayment.GrantedToken.PaymentMethodDetail.type`
  * Change `SharedPayment.GrantedToken.agent_details` to be required
  * Change type of `SubscriptionItem.billed_until` from `nullable(DateTime)` to `DateTime`
  * Add support for `payment_behavior` on `SubscriptionResumeParams`
  * Add support for `status_details` on `Subscription`
  * Change `Subscription.billing_schedules` to be required
  * ⚠️ Add support for new values `ao_bank_account`, `az_bank_account`, `bd_bank_account`, `bo_bank_account`, `br_bank_account`, `cl_bank_account`, `ga_bank_account`, `gh_bank_account`, `gi_bank_account`, `hn_bank_account`, `kr_bank_account`, `kz_bank_account`, `la_bank_account`, `ne_bank_account`, `ng_bank_account`, `ni_bank_account`, `py_bank_account`, `sa_bank_account`, `sm_bank_account`, and `uy_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * ⚠️ Change type of `V2.MoneyManagement.ReceivedCredit.BankTransfer.GbBankAccount.network` from `literal('fps')` to `enum('chaps'|'fps')`
  * Add support for new value `chaps` on enum `v2.FinancialAddressCreditSimulationCreditParams.network`
  * Add support for error codes `payment_method_microdeposit_processing_error` and `siret_invalid` on `QuotePreviewInvoice.LastFinalizationError`

## 15.2.0b2 - 2026-04-24
* ⚠️ [#1797](https://github.com/stripe/stripe-python/pull/1797) Update generated code for beta
  * Add support for new resources `v2.commerce.ProductCatalogImport`, `v2.data.reporting.QueryRun`, `v2.extend.WorkflowRun`, `v2.extend.Workflow`, `v2.iam.ActivityLog`, `v2.network.BusinessProfile`, and `v2.orchestrated_commerce.Agreement`
  * Add support for `confirm`, `create`, `list`, `retrieve`, and `terminate` methods on resource `v2.orchestrated_commerce.Agreement`
  * Add support for `me` and `retrieve` methods on resource `v2.network.BusinessProfile`
  * Add support for `list` method on resource `v2.iam.ActivityLog`
  * Add support for `list` and `retrieve` methods on resource `v2.extend.WorkflowRun`
  * Add support for `invoke`, `list`, and `retrieve` methods on resource `v2.extend.Workflow`
  * Add support for `create` and `retrieve` methods on resources `v2.commerce.ProductCatalogImport` and `v2.data.reporting.QueryRun`
  * ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.konbini`, `V2.Billing.CollectionSetting.PaymentMethodOption.konbini`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.konbini`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.konbini`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.konbini` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSetting.PaymentMethodOption.sepa_debit`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.sepa_debit`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOption.sepa_debit`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOption.sepa_debit` from `map(string: dynamic)` to `an object`
  * ⚠️ Add support for new values `cn_bank_account` and `jp_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * ⚠️ Add support for new values `futsu` and `toza` on enums `V2.Core.Vault.GbBankAccount.bank_account_type` and `V2.MoneyManagement.PayoutMethod.BankAccount.bank_account_type`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_processing` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_queued` from `map(string: dynamic)` to `an object`
  * ⚠️ Change type of `V2.MoneyManagement.InboundTransfer.TransferHistory.bank_debit_succeeded` from `map(string: dynamic)` to `an object`
  * ⚠️ Add support for new value `payout_method_amount_limit_exceeded` on enum `V2.MoneyManagement.OutboundTransfer.StatusDetail.Failed.reason`
  * ⚠️ Add support for new values `inbound_transfer_reversal`, `outbound_payment_reversal`, `outbound_transfer_reversal`, `received_credit_reversal`, `received_debit_reversal`, and `stripe_fee_tax` on enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * ⚠️ Remove support for value `return` from enums `V2.MoneyManagement.Transaction.category` and `V2.MoneyManagement.TransactionEntry.TransactionDetail.category`
  * Add support for new values `futsu` and `toza` on enums `v2.core.vault.GbBankAccountCreateParams.bank_account_type`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount.bank_account_type`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount.bank_account_type`
  * Change type of `v2.core.BatchJobCreateParamsEndpoint.http_method` from `literal('post')` to `enum('delete'|'post')`
  * ⚠️ Add support for new value `meter_event_value_too_many_digits` on enums `EventsV1BillingMeterErrorReportTriggeredEvent.Reason.ErrorType.code` and `EventsV1BillingMeterNoMeterFoundEvent.Reason.ErrorType.code`
  * Add support for `treasury_transaction` on `EventsV2MoneyManagementTransactionCreatedEvent`
  * Add support for event notifications `V2CommerceProductCatalogImportsFailedEvent`, `V2CommerceProductCatalogImportsProcessingEvent`, `V2CommerceProductCatalogImportsSucceededEvent`, and `V2CommerceProductCatalogImportsSucceededWithErrorsEvent` with related object `v2.commerce.ProductCatalogImport`
  * Add support for event notifications `V2DataReportingQueryRunCreatedEvent`, `V2DataReportingQueryRunFailedEvent`, `V2DataReportingQueryRunSucceededEvent`, and `V2DataReportingQueryRunUpdatedEvent` with related object `v2.data.reporting.QueryRun`
  * Add support for event notifications `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, and `V2ExtendWorkflowRunSucceededEvent` with related object `v2.extend.WorkflowRun`
  * Add support for event notifications `V2OrchestratedCommerceAgreementConfirmedEvent`, `V2OrchestratedCommerceAgreementCreatedEvent`, `V2OrchestratedCommerceAgreementPartiallyConfirmedEvent`, and `V2OrchestratedCommerceAgreementTerminatedEvent` with related object `v2.orchestrated_commerce.Agreement`
  * Add support for error type `CannotProceedError`

## 15.2.0b1 - 2026-04-23
This release changes the pinned API version to `2026-04-22.preview`.

* ⚠️ [#1777](https://github.com/stripe/stripe-python/pull/1777) Update generated code for beta
  * Add support for new resources `shared_payment.GrantedToken` and `shared_payment.IssuedToken`
  * Add support for `retrieve` method on resource `shared_payment.GrantedToken`
  * Add support for `create` and `revoke` test helper methods on resource `shared_payment.GrantedToken`
  * Add support for `create`, `retrieve`, and `revoke` methods on resource `shared_payment.IssuedToken`
  * Add support for `blik` on `Invoice.PaymentSetting.PaymentMethodOption`, `InvoiceCreateParamsPaymentSettingPaymentMethodOption`, `InvoiceModifyParamsPaymentSettingPaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.PaymentSetting.PaymentMethodOption`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOption`, `SubscriptionModifyParamsPaymentSettingPaymentMethodOption`, and `checkout.SessionCreateParamsPaymentMethodOption`
  * ⚠️ Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Order.TaxDetail.TaxId.type`, and `QuotePreviewInvoice.CustomerTaxId.type`
  * Change `Checkout.Session.managed_payments`, `PaymentIntent.managed_payments`, `PaymentLink.managed_payments`, and `Subscription.managed_payments` to be required
  * Add support for `shared_payment_granted_token` on `ConfirmationTokenCreateParamsPaymentMethodDatum`, `PaymentIntentConfirmParamsPaymentMethodDatum`, `PaymentIntentCreateParamsPaymentMethodDatum`, `PaymentIntentModifyParamsPaymentMethodDatum`, `PaymentMethod`, `SetupIntentConfirmParamsPaymentMethodDatum`, `SetupIntentCreateParamsPaymentMethodDatum`, and `SetupIntentModifyParamsPaymentMethodDatum`
  * Change `Invoice.PaymentSetting.PaymentMethodOption.pix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.pix`, and `Subscription.PaymentSetting.PaymentMethodOption.pix` to be required
  * Change `Invoice.PaymentSetting.PaymentMethodOption.upi`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.upi`, and `Subscription.PaymentSetting.PaymentMethodOption.upi` to be required
  * Add support for new values `fo_vat`, `gi_tin`, `it_cf`, and `py_ruc` on enums `OrderCreateParamsTaxDetailTaxId.type` and `OrderModifyParamsTaxDetailTaxId.type`
  * Add support for `validation_errors` on `Privacy.RedactionJob`
  * Add support for `tax_details` on `Product`
  * ⚠️ Add support for new value `blik` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * ⚠️ Change type of `QuotePreviewInvoice.TotalTax.TaxRateDetail.tax_rate` from `string` to `expandable($TaxRate)`
  * ⚠️ Change type of `Radar.PaymentEvaluation.ClientDeviceMetadataDetail.radar_session` from `string` to `nullable(string)`
  * Change `SetupIntent.NextAction.PixDisplayQrCode.data` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.expires_at` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.hosted_instructions_url` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_png` to be required
  * Change `SetupIntent.NextAction.PixDisplayQrCode.image_url_svg` to be required
  * Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `tax.RegistrationCreateParamsCountryOptionMe`
  * Add support for `purpose` on `Treasury.OutboundPayment` and `treasury.OutboundPaymentCreateParams`
  * Add support for error codes `action_blocked` and `approval_required` on `QuotePreviewInvoice.LastFinalizationError`

## 15.1.0b2 - 2026-04-01
* Please refer to the changelog for [v15.0.1](https://github.com/stripe/stripe-python/blob/v15.0.1/CHANGELOG.md#1501---2026-04-01)

## 15.1.0b1 - 2026-03-25
This release changes the pinned API version to `2026-03-25.preview`.

It is built on top of SDK version 15.0.0 which contains breaking changes. Please review the [changelog for 15.0.0](https://github.com/stripe/stripe-python/blob/master/CHANGELOG.md#1500---2026-03-25) if upgrading from older SDK versions.

* [#1713](https://github.com/stripe/stripe-python/pull/1713) Delete API_VERSION file as it is no longer needed
* ⚠️ [#1742](https://github.com/stripe/stripe-python/pull/1742) Update generated code for beta
  * Add support for new resources `product_catalog.TrialOffer`, `tax.Location`, and `v2.core.BatchJob`
  * Add support for `create` method on resource `product_catalog.TrialOffer`
  * Add support for `create`, `list`, and `retrieve` methods on resource `tax.Location`
  * Add support for `cancel`, `create`, and `retrieve` methods on resource `v2.core.BatchJob`
  * Add support for `performance_location` on `Tax.CalculationLineItem` and `tax.CalculationCreateParamsLineItem`
  * ⚠️ Add support for new value `performance` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.sourcing`, `Tax.CalculationLineItem.TaxBreakdown.sourcing`, and `Tax.Transaction.ShippingCost.TaxBreakdown.sourcing`
  * ⚠️ Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type`, `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type`, and `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type`
  * Add support for `trial_offer` on `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSet`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItem`, `QuoteCreateParamsLineActionAddItem`, `QuoteCreateParamsLineActionSetItem`, `QuoteLine.Action.AddItem`, `QuoteLine.Action.SetItem`, `QuoteModifyParamsLineActionAddItem`, `QuoteModifyParamsLineActionSetItem`, `QuotePreviewSubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase.Item`, `SubscriptionScheduleAmendParamsAmendmentItemActionAdd`, `SubscriptionScheduleAmendParamsAmendmentItemActionSet`, `SubscriptionScheduleCreateParamsPhaseItem`, and `SubscriptionScheduleModifyParamsPhaseItem`
  * Add support for `risk_reserved` on `Balance`
  * ⚠️ Remove support for `source_type` on `Charge.PaymentMethodDetail.StripeBalance`, `ConfirmationToken.PaymentMethodPreview.StripeBalance`, `ConfirmationTokenCreateParamsPaymentMethodDatumStripeBalance`, `PaymentAttemptRecord.PaymentMethodDetail.StripeBalance`, `PaymentIntentConfirmParamsPaymentMethodDatumStripeBalance`, `PaymentIntentCreateParamsPaymentMethodDatumStripeBalance`, `PaymentIntentModifyParamsPaymentMethodDatumStripeBalance`, `PaymentMethod.StripeBalance`, `PaymentMethodCreateParamsStripeBalance`, `PaymentRecord.PaymentMethodDetail.StripeBalance`, `SetupIntentConfirmParamsPaymentMethodDatumStripeBalance`, `SetupIntentCreateParamsPaymentMethodDatumStripeBalance`, and `SetupIntentModifyParamsPaymentMethodDatumStripeBalance`
  * Add support for `tax_details` on `InvoiceAddLinesParamsLinePriceDatumProductDatum`, `InvoiceLineItemModifyParamsPriceDatumProductDatum`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatum`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatum`, `PlanCreateParamsProduct`, `PriceCreateParamsProductDatum`, `ProductCreateParams`, `ProductModifyParams`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatum`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatum`
  * Add support for `pending_invoice_item_interval` on `checkout.SessionModifyParamsSubscriptionDatum`
  * Add support for `hosted` and `ui_mode` on `FinancialConnections.Session` and `financial_connections.SessionCreateParams`
  * Add support for `url` on `FinancialConnections.Session`
  * Add support for `expires_after_seconds` on `Invoice.PaymentSetting.PaymentMethodOption.Pix`, `InvoiceCreateParamsPaymentSettingPaymentMethodOptionPix`, `InvoiceModifyParamsPaymentSettingPaymentMethodOptionPix`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption.Pix`, `Subscription.PaymentSetting.PaymentMethodOption.Pix`, `SubscriptionCreateParamsPaymentSettingPaymentMethodOptionPix`, and `SubscriptionModifyParamsPaymentSettingPaymentMethodOptionPix`
  * Add support for `current_trial` on `InvoiceCreatePreviewParamsSubscriptionDetailItem`, `SubscriptionCreateParamsItem`, `SubscriptionItemCreateParams`, `SubscriptionItemModifyParams`, `SubscriptionItem`, and `SubscriptionModifyParamsItem`
  * Add support for `surcharge` on `PaymentIntent.AmountDetail`, `PaymentIntentCaptureParamsAmountDetail`, `PaymentIntentConfirmParamsAmountDetail`, `PaymentIntentCreateParamsAmountDetail`, `PaymentIntentIncrementAuthorizationParamsAmountDetail`, and `PaymentIntentModifyParamsAmountDetail`
  * Add support for `amount_details` and `payment_details` on `PaymentIntentDecrementAuthorizationParams`
  * Add support for `mandate_options` on `PaymentIntent.PaymentMethodOption.StripeBalance`
  * Add support for `managed_payments` on `PaymentLinkCreateParams` and `PaymentLink`
  * Add support for `stripe_balance` on `SetupIntent.PaymentMethodOption`, `SetupIntentConfirmParamsPaymentMethodOption`, `SetupIntentCreateParamsPaymentMethodOption`, and `SetupIntentModifyParamsPaymentMethodOption`
  * Add support for `billing_cycle_anchor` on `Subscription.TrialSetting.EndBehavior`, `SubscriptionCreateParamsTrialSettingEndBehavior`, and `SubscriptionModifyParamsTrialSettingEndBehavior`
  * ⚠️ Add support for new values `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on enums `Tax.Registration.CountryOption.Me.type` and `tax.RegistrationCreateParamsCountryOptionMe.type`
  * Add support for `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, and `tourism_tax` on `Tax.Registration.CountryOption.Me`
  * Add support for `requirements` on `TaxCode`
  * ⚠️ Change type of `V2.Billing.Cadence.SettingsDatum.Collection.PaymentMethodOption.Card.MandateOption.amount`, `V2.Billing.CollectionSetting.PaymentMethodOption.Card.MandateOption.amount`, `V2.Billing.CollectionSettingVersion.PaymentMethodOption.Card.MandateOption.amount`, `v2.billing.CollectionSettingCreateParamsPaymentMethodOptionCardMandateOption.amount`, and `v2.billing.CollectionSettingModifyParamsPaymentMethodOptionCardMandateOption.amount` from `longInteger` to `int64_string`
  * ⚠️ Add support for new values `ar_bank_account`, `co_bank_account`, and `eg_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Add support for `timezone` on `V2.Core.Account.Default`, `v2.core.AccountCreateParamsDefault`, and `v2.core.AccountModifyParamsDefault`
  * Add support for `azure_event_grid` on `V2.Core.EventDestination` and `v2.core.EventDestinationCreateParams`
  * ⚠️ Add support for new value `no_azure_partner_topic_exists` on enum `V2.Core.EventDestination.StatusDetail.Disabled.reason`
  * ⚠️ Add support for new value `azure_event_grid` on enums `V2.Core.EventDestination.type` and `v2.core.EventDestinationCreateParams.type`
  * Add support for `supported_currencies` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod.Card`
  * ⚠️ Change `V2.Core.Vault.GbBankAccount.sort_code` and `v2.core.vault.GbBankAccountCreateParams.sort_code` to be optional
  * Add support for `restricted` on `V2.MoneyManagement.PayoutMethod`
  * Add support for `currencies` on `V2.MoneyManagement.PayoutMethodsBankAccountSpec.Country.Field`
  * Add support for `counterparty` and `description` on `V2.MoneyManagement.Transaction`
  * ⚠️ Add support for `currency` on `v2.core.vault.GbBankAccountCreateParams`, `v2.core.vault.UsBankAccountCreateParams`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount`, `v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumCard`, `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount`, and `v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumCard`
  * Add support for `iban` on `v2.core.vault.GbBankAccountCreateParams`
  * Change `v2.core.vault.GbBankAccountCreateParams.account_number` to be optional
  * ⚠️ Add support for new value `currency` on enum `InvalidPaymentMethodError.invalid_param`
  * Add support for event notifications `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, and `V2CoreBatchJobValidationFailedEvent` with related object `v2.core.BatchJob`
  * Add support for error code `service_period_coupon_with_metered_tiered_item_unsupported` on `QuotePreviewInvoice.LastFinalizationError`
* [#1772](https://github.com/stripe/stripe-python/pull/1772) Update generated code for beta
  * Release specs are identical.
* [#1774](https://github.com/stripe/stripe-python/pull/1774) Update generated code for beta

## 14.5.0b1 - 2026-02-25
This release changes the pinned API version to `2026-02-25.preview`.

* [#1727](https://github.com/stripe/stripe-python/pull/1727) Update generated code for beta
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

## 14.4.0b1 - 2026-01-28
This release changes the pinned API version to `2026-01-28.preview`.

* [#1701](https://github.com/stripe/stripe-python/pull/1701) Add EventNotificationHandler example
* [#1719](https://github.com/stripe/stripe-python/pull/1719) Update generated code for beta
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

## 14.2.0b1 - 2025-12-16
This release changes the pinned API version to `2025-12-15.preview`.

* [#1653](https://github.com/stripe/stripe-python/pull/1653) Add EventNotificationHandler
  * This is a new, simplified way to handle event notifications (AKA thin event webhooks). Learn more in the docs: https://docs.stripe.com/webhooks/event-notification-handlers
* [#1680](https://github.com/stripe/stripe-python/pull/1680) Update generated code for beta
  * Add support for new resources `reserve.Hold`, `reserve.Plan`, and `reserve.Release`
  * Add support for `list` and `retrieve` methods on resources `reserve.Hold` and `reserve.Release`
  * Add support for `retrieve` method on resource `reserve.Plan`
  * Change `Billing.CreditBalanceSummary.customer_account`, `Billing.CreditGrant.customer_account`, `BillingPortal.Session.customer_account`, `CashBalance.customer_account`, `Checkout.Session.customer_account`, `ConfirmationToken.PaymentMethodPreview.customer_account`, `CreditNote.customer_account`, `CustomerBalanceTransaction.customer_account`, `CustomerCashBalanceTransaction.customer_account`, `CustomerSession.customer_account`, `Discount.customer_account`, `Invoice.customer_account`, `InvoiceItem.customer_account`, `PaymentIntent.customer_account`, `PaymentMethod.customer_account`, `PromotionCode.customer_account`, `Quote.customer_account`, `QuotePreviewInvoice.customer_account`, `QuotePreviewSubscriptionSchedule.customer_account`, `SetupAttempt.customer_account`, `Subscription.customer_account`, `SubscriptionSchedule.customer_account`, `TaxId.Owner.customer_account`, and `TaxId.customer_account` to be required
  * Change type of `V2.FinancialAddressGeneratedMicrodeposits.amounts` from `amount` to `an object`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.amount`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.amount`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.amount`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.amount`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.amount`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.amount`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.amount` from `longInteger` to `emptyable(longInteger)`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.amount_type`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.amount_type`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.amount_type`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.amount_type`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.amount_type`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.amount_type`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.amount_type` from `enum('fixed'|'maximum')` to `emptyable(enum('fixed'|'maximum'))`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.end_date`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.end_date`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.end_date`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.end_date`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.end_date`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.end_date`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.end_date` from `string` to `emptyable(string)`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.payment_schedule`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.payment_schedule` from `enum` to `emptyable(enum)`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.payments_per_period`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.payments_per_period` from `longInteger` to `emptyable(longInteger)`
  * Change type of `PaymentIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.purpose`, `PaymentIntentCreateParamsPaymentMethodOptionPaytoMandateOption.purpose`, `PaymentIntentModifyParamsPaymentMethodOptionPaytoMandateOption.purpose`, `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.purpose`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.purpose`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.purpose`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.purpose` from `enum` to `emptyable(enum)`
  * Change type of `SetupIntentConfirmParamsPaymentMethodOptionPaytoMandateOption.start_date`, `SetupIntentCreateParamsPaymentMethodOptionPaytoMandateOption.start_date`, `SetupIntentModifyParamsPaymentMethodOptionPaytoMandateOption.start_date`, and `checkout.SessionCreateParamsPaymentMethodOptionPaytoMandateOption.start_date` from `string` to `emptyable(string)`
  * Change `Identity.VerificationSession.related_customer_account` to be required
  * Add support for `async_workflows` on `PaymentIntent`
  * Add support for `payto` on `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`
  * Add support for new value `payto` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Remove support for `requested` on `V2.Core.Account.Configuration.Customer.Capability.AutomaticIndirectTax`, `V2.Core.Account.Configuration.Merchant.Capability.AchDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AcssDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AffirmPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AfterpayClearpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AlmaPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AmazonPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.AuBecsDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BacsDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BancontactPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BlikPayment`, `V2.Core.Account.Configuration.Merchant.Capability.BoletoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CardPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CartesBancairesPayment`, `V2.Core.Account.Configuration.Merchant.Capability.CashappPayment`, `V2.Core.Account.Configuration.Merchant.Capability.EpsPayment`, `V2.Core.Account.Configuration.Merchant.Capability.FpxPayment`, `V2.Core.Account.Configuration.Merchant.Capability.GbBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.GrabpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.IdealPayment`, `V2.Core.Account.Configuration.Merchant.Capability.JcbPayment`, `V2.Core.Account.Configuration.Merchant.Capability.JpBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KakaoPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KlarnaPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KonbiniPayment`, `V2.Core.Account.Configuration.Merchant.Capability.KrCardPayment`, `V2.Core.Account.Configuration.Merchant.Capability.LinkPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MobilepayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MultibancoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.MxBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.NaverPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.OxxoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.P24Payment`, `V2.Core.Account.Configuration.Merchant.Capability.PayByBankPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PaycoPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PaynowPayment`, `V2.Core.Account.Configuration.Merchant.Capability.PromptpayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.RevolutPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SamsungPayPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SepaBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.SepaDebitPayment`, `V2.Core.Account.Configuration.Merchant.Capability.StripeBalance.Payout`, `V2.Core.Account.Configuration.Merchant.Capability.SwishPayment`, `V2.Core.Account.Configuration.Merchant.Capability.TwintPayment`, `V2.Core.Account.Configuration.Merchant.Capability.UsBankTransferPayment`, `V2.Core.Account.Configuration.Merchant.Capability.ZipPayment`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Local`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Wire`, `V2.Core.Account.Configuration.Recipient.Capability.Card`, `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.Payout`, `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.StripeTransfer`, `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Eur`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Gbp`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Usd`, `V2.Core.Account.Configuration.Storer.Capability.InboundTransfer.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.BankAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.Card`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.FinancialAccount`, `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.BankAccount`, and `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.FinancialAccount`
  * Add support for new values `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, and `tz_bank_account` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Change type of `V2.Core.Account.Identity.BusinessDetail.AnnualRevenue.amount`, `V2.Core.Account.Identity.BusinessDetail.MonthlyEstimatedRevenue.amount`, `V2.MoneyManagement.Adjustment.amount`, `V2.MoneyManagement.InboundTransfer.amount`, `V2.MoneyManagement.OutboundPayment.amount`, `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.amount`, `V2.MoneyManagement.OutboundPaymentQuote.amount`, `V2.MoneyManagement.OutboundTransfer.amount`, `V2.MoneyManagement.ReceivedCredit.amount`, `V2.MoneyManagement.ReceivedDebit.amount`, `V2.MoneyManagement.Transaction.amount`, `v2.FinancialAddressCreditSimulationCreditParams.amount`, `v2.core.AccountCreateParamsIdentityBusinessDetailAnnualRevenue.amount`, `v2.core.AccountCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenue.amount`, `v2.core.AccountModifyParamsIdentityBusinessDetailAnnualRevenue.amount`, `v2.core.AccountModifyParamsIdentityBusinessDetailMonthlyEstimatedRevenue.amount`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailAnnualRevenue.amount`, `v2.core.AccountTokenCreateParamsIdentityBusinessDetailMonthlyEstimatedRevenue.amount`, `v2.money_management.InboundTransferCreateParams.amount`, `v2.money_management.OutboundPaymentCreateParams.amount`, `v2.money_management.OutboundPaymentQuoteCreateParams.amount`, and `v2.money_management.OutboundTransferCreateParams.amount` from `amount` to `an object`
  * Add support for new values `at_stn`, `at_vat`, `be_vat`, `bg_vat`, `ca_gst_hst`, `cy_he`, `cy_vat`, `cz_vat`, `de_stn`, `dk_vat`, `ee_vat`, `es_vat`, `fi_vat`, `fr_rna`, `gr_afm`, `gr_vat`, `hr_mbs`, `hr_oib`, `hr_vat`, `hu_tin`, `hu_vat`, `ie_trn`, `ie_vat`, `lt_vat`, `lu_nif`, `lu_vat`, `lv_vat`, `mt_tin`, `mt_vat`, `my_itn`, `nl_rsin`, `nl_vat`, `nz_ird`, `pl_nip`, `pl_vat`, `ro_orc`, `ro_vat`, `se_vat`, `si_tin`, `si_vat`, `sk_dic`, and `sk_vat` on enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * Remove support for value `hk_mbs` from enums `V2.Core.Account.Identity.BusinessDetail.IdNumber.type`, `v2.core.AccountCreateParamsIdentityBusinessDetailIdNumber.type`, `v2.core.AccountModifyParamsIdentityBusinessDetailIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityBusinessDetailIdNumber.type`
  * Add support for new values `ar_cuil`, `at_stn`, `be_nrn`, `bg_ucn`, `bn_nric`, `ca_sin`, `ch_oasi`, `cl_rut`, `cn_pp`, `co_nuip`, `cr_ci`, `cy_tic`, `cz_rc`, `dk_cpr`, `do_cie`, `ec_ci`, `ee_ik`, `es_nif`, `fi_hetu`, `fr_nir`, `gb_nino`, `gr_afm`, `hr_oib`, `hu_ad`, `id_nik`, `ie_ppsn`, `is_kt`, `it_cf`, `jp_inc`, `ke_pin`, `li_peid`, `lt_ak`, `lu_nif`, `lv_pk`, `ng_nin`, `no_nin`, `nz_ird`, `pl_pesel`, `pt_nif`, `ro_cnp`, `se_pin`, `sk_dic`, `tr_tin`, `uy_dni`, and `za_id` on enums `V2.Core.Account.Identity.Individual.IdNumber.type`, `V2.Core.AccountPerson.IdNumber.type`, `v2.core.AccountCreateParamsIdentityIndividualIdNumber.type`, `v2.core.AccountModifyParamsIdentityIndividualIdNumber.type`, `v2.core.AccountPersonCreateParamsIdNumber.type`, `v2.core.AccountPersonModifyParamsIdNumber.type`, `v2.core.AccountPersonTokenCreateParamsIdNumber.type`, and `v2.core.AccountTokenCreateParamsIdentityIndividualIdNumber.type`
  * Change `V2.Core.Account.Default.responsibilities` to be required
  * Change `V2.Core.Account.Default.Responsibility.fees_collector` to be optional
  * Change `V2.Core.Account.Default.Responsibility.losses_collector` to be optional
  * Add support for `financial_connections_account` on `V2.Core.Vault.UsBankAccount` and `V2.MoneyManagement.PayoutMethod.BankAccount`
  * Change type of `V2.MoneyManagement.FinancialAccount.Balance.available`, `V2.MoneyManagement.Transaction.BalanceImpact.available`, and `V2.MoneyManagement.TransactionEntry.BalanceImpact.available` from `amount` to `an object`
  * Change type of `V2.MoneyManagement.FinancialAccount.Balance.inbound_pending`, `V2.MoneyManagement.Transaction.BalanceImpact.inbound_pending`, and `V2.MoneyManagement.TransactionEntry.BalanceImpact.inbound_pending` from `amount` to `an object`
  * Change type of `V2.MoneyManagement.FinancialAccount.Balance.outbound_pending`, `V2.MoneyManagement.Transaction.BalanceImpact.outbound_pending`, and `V2.MoneyManagement.TransactionEntry.BalanceImpact.outbound_pending` from `amount` to `an object`
  * Change type of `V2.MoneyManagement.InboundTransfer.From.debited`, `V2.MoneyManagement.OutboundPayment.From.debited`, `V2.MoneyManagement.OutboundPaymentQuote.From.debited`, and `V2.MoneyManagement.OutboundTransfer.From.debited` from `amount` to `an object`
  * Change type of `V2.MoneyManagement.InboundTransfer.To.credited`, `V2.MoneyManagement.OutboundPayment.To.credited`, `V2.MoneyManagement.OutboundPaymentQuote.To.credited`, and `V2.MoneyManagement.OutboundTransfer.To.credited` from `amount` to `an object`
  * Add support for `transfer` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
  * Add support for new value `transfer` on enum `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type`
  * Change `v2.core.AccountTokenCreateParams.identity` to be optional
  * Change type of `v2.core.AccountListParams.applied_configurations` from `string` to `enum('customer'|'merchant'|'recipient'|'storer')`
  * Add support for event notification `V2MoneyManagementPayoutMethodCreatedEvent` with related object `v2.money_management.PayoutMethod`
  * Add support for error type `ControlledByAlternateResourceError`
  * Remove support for error type `RateLimitError`
  * Add support for error code `account_token_required_for_v2_account` on `QuotePreviewInvoice.LastFinalizationError`

## 14.1.0b1 - 2025-11-18
This release changes the pinned API version to `2025-11-17.preview`.

* [#1663](https://github.com/stripe/stripe-python/pull/1663) Update generated code for beta
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

## 13.2.0b1 - 2025-10-29
This release changes the pinned API version to `2025-10-29.preview`.

* [#1617](https://github.com/stripe/stripe-python/pull/1617) Update generated code for beta
  * Add support for `last_seen_at` on `Terminal.Reader`
  * Add support for new value `2025-10-29.clover` on enum `WebhookEndpointCreateParams.api_version`
* [#1624](https://github.com/stripe/stripe-python/pull/1624) Update generated code for beta
  * Add support for `modify` method on resource `v2.money_management.FinancialAccount`
  * Add support for `confirm_microdeposits`, `list`, and `send_microdeposits` methods on resource `v2.core.vault.UsBankAccount`
  * Add support for `list` method on resource `v2.core.vault.GbBankAccount`
  * Add support for new value `verification_data_not_found` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, `BankAccount.Requirement.Error.code`, `Capability.FutureRequirement.Error.code`, `Capability.Requirement.Error.code`, `Person.FutureRequirement.Error.code`, and `Person.Requirement.Error.code`
  * Add support for `payment_portal_url` on `Charge.PaymentMethodDetail.Rechnung`, `PaymentAttemptRecord.PaymentMethodDetail.Rechnung`, and `PaymentRecord.PaymentMethodDetail.Rechnung`
  * Add support for `tax_id_element` on `CustomerSession.Component` and `CustomerSessionCreateParamsComponent`
  * Add support for `starting_after` on `PaymentAttemptRecordListParams`
  * Add support for new value `solana` on enums `PaymentAttemptRecord.PaymentMethodDetail.Crypto.network` and `PaymentRecord.PaymentMethodDetail.Crypto.network`
  * Add support for `reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`, `PaymentIntentCaptureParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsAmountDetailLineItemPaymentMethodOptionKlarna`, `PaymentIntentIncrementAuthorizationParamsAmountDetailLineItemPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsAmountDetailLineItemPaymentMethodOptionKlarna`
  * Change `PaymentIntent.PaymentDetail.customer_reference` to be required
  * Change `PaymentIntent.PaymentDetail.order_reference` to be required
  * Add support for `subscription_reference` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption.Klarna`
  * Add support for `closed` on `V2.Core.Account` and `v2.core.AccountListParams`
  * Add support for new value `payment_method` on enums `V2.Core.Account.Configuration.Customer.AutomaticIndirectTax.location_source`, `v2.core.AccountCreateParamsConfigurationCustomerAutomaticIndirectTax.location_source`, and `v2.core.AccountModifyParamsConfigurationCustomerAutomaticIndirectTax.location_source`
  * Add support for `usd` on `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency`, `v2.core.AccountCreateParamsConfigurationStorerCapabilityHoldsCurrency`, and `v2.core.AccountModifyParamsConfigurationStorerCapabilityHoldsCurrency`
  * Add support for new values `application_custom` and `application_express` on enums `V2.Core.Account.Default.Responsibility.fees_collector`, `v2.core.AccountCreateParamsDefaultResponsibility.fees_collector`, and `v2.core.AccountModifyParamsDefaultResponsibility.fees_collector`
  * Add support for `representative_declaration` on `V2.Core.Account.Identity.Attestation`, `v2.core.AccountCreateParamsIdentityAttestation`, and `v2.core.AccountModifyParamsIdentityAttestation`
  * Add support for new value `holds_currencies.usd` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for `verification` on `V2.Core.Vault.UsBankAccount`
  * Add support for `v1_id` on `EventsV2MoneyManagementTransactionCreatedEvent`
  * Remove support for thin event `V2BillingBillSettingUpdatedEvent` with related object `v2.billing.BillSetting`
  * Add support for error code `payment_intent_rate_limit_exceeded` on `QuotePreviewInvoice.LastFinalizationError`
  * Add support for error codes `blocked_payout_method_crypto_wallet` and `unsupported_payout_method_crypto_wallet` on `BlockedByStripeError`
  * Add support for error code `outbound_flow_from_closed_financial_account_unsupported` on `FeatureNotEnabledError`
  * Add support for error code `limit_payout_method_crypto_wallet` on `QuotaExceededError`
* [#1655](https://github.com/stripe/stripe-python/pull/1655) Update generated code for beta
  * Add support for `crypto_storer` on `v2.core.AccountModifyParamsIdentityAttestationTermsOfService`

## 13.1.1b1 - 2025-10-03
* [#1617](https://github.com/stripe/stripe-python/pull/1617) Update generated code for beta
  * Add support for `last_seen_at` on `Terminal.Reader`
  * Add support for new value `2025-10-29.clover` on enum `WebhookEndpointCreateParams.api_version`

## 13.1.0b1 - 2025-09-30
This release changes the pinned API version to `2025-09-30.preview`.

It is built on top of SDK version 13.0.0 which contains breaking changes. Please review the [changelog for 13.0.0](https://github.com/stripe/stripe-go/blob/master/CHANGELOG.md#1300---2025-09-30) if upgrading from older SDK versions.

* [#1555](https://github.com/stripe/stripe-python/pull/1555) Update generated code for beta
  * Add support for new resources `billing.analytics.MeterUsageRow` and `billing.analytics.MeterUsage`
  * Remove support for resources `billing.MeterUsageRow` and `billing.MeterUsage`
  * Add support for `retrieve` method on resource `billing.analytics.MeterUsage`
  * Remove support for `retrieve` method on resource `billing.MeterUsage`
  * Add support for `report_payment_attempt_informational` method on resource `PaymentRecord`
  * Add support for `minimum_balance_by_currency` on `BalanceSettings.ModifyParamsPaymentPayout` and `BalanceSettings.Payment.Payout`
  * Remove support for values `saturday` and `sunday` from enums `BalanceSettings.ModifyParamsPaymentPayoutSchedule.weekly_payout_days` and `BalanceSettings.Payment.Payout.Schedule.weekly_payout_days`
  * Change type of `BalanceSettings.ModifyParamsPaymentSettlementTiming.delay_days_override` from `longInteger` to `emptyable(longInteger)`
  * Change `BalanceSettings.ModifyParams.payments` to be optional
  * Add support for `delay_days_override` on `BalanceSettings.Payment.SettlementTiming`
  * Add support for `automatic_tax` and `invoice_creation` on `checkout.Session.ModifyParams`
  * Add support for `unit_label` on `checkout.Session.ModifyParamsLineItemPriceDatumProductDatum`
  * Add support for `invoice_settings` on `checkout.Session.ModifyParamsSubscriptionDatum`
  * Change `Checkout.Session.CollectedInformation.business_name` to be required
  * Add support for `intended_submission_method` on `Dispute.ModifyParams` and `Dispute`
  * Change type of `Dispute.SmartDispute.recommended_evidence` from `string` to `array(string)`
  * Add support for `pix` on `Invoice.CreateParamsPaymentSettingPaymentMethodOption`, `Invoice.ModifyParamsPaymentSettingPaymentMethodOption`, `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.CreateParamsPaymentSettingPaymentMethodOption`, `Subscription.ModifyParamsPaymentSettingPaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
  * Add support for new value `pix` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.ModifyParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.ModifyParamsPaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
  * Add support for `billing_schedules` on `Invoice.CreatePreviewParamsSubscriptionDetail`, `Subscription.CreateParams`, `Subscription.ModifyParams`, and `Subscription`
  * Add support for `paypay` on `PaymentAttemptRecord.PaymentMethodDetail` and `PaymentRecord.PaymentMethodDetail`
  * Add support for `wallet` on `PaymentAttemptRecord.PaymentMethodDetail.Card` and `PaymentRecord.PaymentMethodDetail.Card`
  * Change type of `PaymentAttemptRecord.ProcessorDetail.Custom.payment_reference` and `PaymentRecord.ProcessorDetail.Custom.payment_reference` from `string` to `nullable(string)`
  * Add support for `flexible` on `QuotePreviewSubscriptionSchedule.BillingMode`
  * Add support for `billed_until` on `SubscriptionItem`
  * Add support for error codes `financial_connections_account_pending_account_numbers` and `financial_connections_account_unavailable_account_numbers` on `QuotePreviewInvoice.LastFinalizationError`
* [#1584](https://github.com/stripe/stripe-python/pull/1584) Update generated code for beta
  * Add support for new resources `v2.billing.BillSettingVersion`, `v2.billing.BillSetting`, `v2.billing.Cadence`, `v2.billing.CollectionSettingVersion`, `v2.billing.CollectionSetting`, and `v2.billing.Profile`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resources `v2.billing.BillSetting`, `v2.billing.CollectionSetting`, and `v2.billing.Profile`
  * Add support for `list` and `retrieve` methods on resources `v2.billing.BillSettingVersion` and `v2.billing.CollectionSettingVersion`
  * Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `v2.billing.Cadence`
  * Add support for new value `crypto_wallet` on enum `V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination.type`
  * Add support for `profile` on `V2.Core.Account.Default`, `v2.core.Account.CreateParamsDefault`, and `v2.core.Account.ModifyParamsDefault`
  * Add support for `i_p` on `V2.Core.Account.Identity.Attestation.DirectorshipDeclaration`, `V2.Core.Account.Identity.Attestation.OwnershipDeclaration`, `V2.Core.Account.Identity.Attestation.TermsOfService.Account`, `V2.Core.Account.Identity.Attestation.TermsOfService.Storer`, `V2.Core.Account.Identity.Individual.AdditionalTermsOfService.Account`, `V2.Core.Person.AdditionalTermsOfService.Account`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Person.CreateParamsAdditionalTermsOfServiceAccount`, and `v2.core.Person.ModifyParamsAdditionalTermsOfServiceAccount`
  * Remove support for `ip` on `V2.Core.Account.Identity.Attestation.DirectorshipDeclaration`, `V2.Core.Account.Identity.Attestation.OwnershipDeclaration`, `V2.Core.Account.Identity.Attestation.TermsOfService.Account`, `V2.Core.Account.Identity.Attestation.TermsOfService.Storer`, `V2.Core.Account.Identity.Individual.AdditionalTermsOfService.Account`, `V2.Core.Person.AdditionalTermsOfService.Account`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceAccount`, `v2.core.Account.ModifyParamsIdentityAttestationTermsOfServiceStorer`, `v2.core.Person.CreateParamsAdditionalTermsOfServiceAccount`, and `v2.core.Person.ModifyParamsAdditionalTermsOfServiceAccount`
  * Remove support for `doing_business_as`, `product_description`, and `url` on `V2.Core.Account.Identity.BusinessDetail`, `v2.core.Account.CreateParamsIdentityBusinessDetail`, and `v2.core.Account.ModifyParamsIdentityBusinessDetail`
  * Add support for `settlement_currency` on `V2.MoneyManagement.FinancialAddress`
  * Add support for `sepa_bank_account` on `V2.MoneyManagement.FinancialAddress.Credential` and `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * Add support for new value `sepa_bank_account` on enum `V2.MoneyManagement.FinancialAddress.Credential.type`
  * Add support for `amount_details` and `payments_orchestration` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPayment.CreateParams`
  * Add support for new value `authorization_expired` on enum `V2.Payments.OffSessionPayment.failure_reason`
  * Add support for `retry_policy` on `V2.Payments.OffSessionPayment.RetryDetail` and `v2.payments.OffSessionPayment.CreateParamsRetryDetail`
  * Add support for new values `heuristic` and `scheduled` on enums `V2.Payments.OffSessionPayment.RetryDetail.retry_strategy` and `v2.payments.OffSessionPayment.CreateParamsRetryDetail.retry_strategy`
  * Change type of `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_duration` from `literal('five_minutes')` to `enum('five_minutes'|'none')`
  * Change type of `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_expires_at` from `DateTime` to `nullable(DateTime)`
  * Add support for new value `none` on enum `V2.MoneyManagement.OutboundPaymentQuote.FxQuote.lock_status`
  * Add support for new value `crypto_wallet` on enums `V2.MoneyManagement.PayoutMethod.type`, `v2.money_management.OutboundSetupIntent.CreateParamsPayoutMethodDatum.type`, and `v2.money_management.OutboundSetupIntent.ModifyParamsPayoutMethodDatum.type`
  * Add support for `origin_type` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * Remove support for `payment_method_type` on `V2.MoneyManagement.ReceivedCredit.BankTransfer`
  * Add support for `mandate_data` and `payment_method_options` on `v2.payments.OffSessionPayment.CreateParams`
  * Add support for `type` on `v2.money_management.FinancialAddress.CreateParams`
  * Remove support for `currency` on `v2.money_management.FinancialAddress.CreateParams`
  * Add support for new values `financial_addressses.crypto_wallets`, `holds_currencies.usdc`, `outbound_payments.crypto_wallets`, and `outbound_transfers.crypto_wallets` on enum `EventsV2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent.updated_capability`
  * Add support for thin event `V2BillingBillSettingUpdatedEvent` with related object `v2.billing.BillSetting`
  * Add support for error type `RateLimitError`
  * Add support for error code `invalid_payout_method_crypto_wallet` on `InvalidPayoutMethodError`
* [#1597](https://github.com/stripe/stripe-python/pull/1597) Update generated code for beta
  * Add support for `attach_cadence` method on resource `Subscription`
  * Add support for `billing_cadence` on `Invoice.CreatePreviewParams`, `Subscription.CreateParams`, `Subscription.ModifyParams`, and `Subscription`
  * Add support for `billing_cadence_details` on `Invoice.Parent` and `QuotePreviewInvoice.Parent`
  * Add support for new value `billing_cadence_details` on enums `Invoice.Parent.type` and `QuotePreviewInvoice.Parent.type`

## 12.6.0b1 - 2025-08-27
This release changes the pinned API version to `2025-08-27.preview`.

* [#1542](https://github.com/stripe/stripe-python/pull/1542) Update generated code for beta
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

## 12.5.0b2 - 2025-08-08
* [#1545](https://github.com/stripe/stripe-python/pull/1545) Bring back invoice payments APIs that were missing in the public preview SDKs
  * Add support for new resource `InvoicePayment`
  * Add support for `list` and `retrieve` methods on resource `InvoicePayment`

## 12.5.0b1 - 2025-07-30
This release changes the pinned API version to `2025-07-30.preview`.

* [#1535](https://github.com/stripe/stripe-python/pull/1535) Update generated code for beta
  * Add support for new resources `billing.MeterUsageRow`, `billing.MeterUsage`, and `terminal.OnboardingLink`
  * Add support for `retrieve` method on resource `billing.MeterUsage`
  * Add support for `create` method on resource `terminal.OnboardingLink`
  * Add support for `monthly_payout_days` and `weekly_payout_days` on `BalanceSettings.ModifyParamsPayoutSchedule` and `BalanceSettings.Payout.Schedule`
  * Remove support for `monthly_anchor` and `weekly_anchor` on `BalanceSettings.ModifyParamsPayoutSchedule` and `BalanceSettings.Payout.Schedule`
  * Add support for `delay_days_override` on `BalanceSettings.ModifyParamsSettlementTiming`
  * Remove support for `delay_days` on `BalanceSettings.ModifyParamsSettlementTiming`
  * Add support for `update_discounts` on `checkout.Session.CreateParamsPermission`
  * Add support for `discounts` and `subscription_data` on `checkout.Session.ModifyParams`
  * Add support for `smart_disputes` on `Dispute`
  * Add support for `upi` on `Invoice.CreateParamsPaymentSettingPaymentMethodOption`, `Invoice.ModifyParamsPaymentSettingPaymentMethodOption`, `Invoice.PaymentSetting.PaymentMethodOption`, `QuotePreviewInvoice.PaymentSetting.PaymentMethodOption`, `Subscription.CreateParamsPaymentSettingPaymentMethodOption`, `Subscription.ModifyParamsPaymentSettingPaymentMethodOption`, and `Subscription.PaymentSetting.PaymentMethodOption`
  * Add support for new value `upi` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.ModifyParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.ModifyParamsPaymentSetting.payment_method_types`, and `Subscription.PaymentSetting.payment_method_types`
  * Add support for `transaction_id` on `PaymentAttemptRecord.PaymentMethodDetail.Cashapp` and `PaymentRecord.PaymentMethodDetail.Cashapp`
  * Add support for `amount_details` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.IncrementAuthorizationParams`, and `PaymentIntent.ModifyParams`
  * Add support for `payment_details` on `PaymentIntent.IncrementAuthorizationParams`
  * Add support for `storer` on `V2.Core.Account.Identity.Attestation.TermsOfService`, `v2.core.Account.CreateParamsIdentityAttestationTermsOfService`, and `v2.core.Account.ModifyParamsIdentityAttestationTermsOfService`
  * Add support for `collection_options` on `V2.Core.AccountLink.UseCase.AccountOnboarding`, `V2.Core.AccountLink.UseCase.AccountUpdate`, `v2.core.AccountLink.CreateParamsUseCaseAccountOnboarding`, and `v2.core.AccountLink.CreateParamsUseCaseAccountUpdate`
  * Change type of `V2.Core.AccountLink.UseCase.AccountOnboarding.configurations`, `V2.Core.AccountLink.UseCase.AccountUpdate.configurations`, `v2.core.AccountLink.CreateParamsUseCaseAccountOnboarding.configurations`, and `v2.core.AccountLink.CreateParamsUseCaseAccountUpdate.configurations` from `literal('recipient')` to `enum('customer'|'merchant'|'recipient'|'storer')`
  * Add support for `bank_account_type` on `V2.MoneyManagement.PayoutMethod.BankAccount`
  * Add support for thin event `V2CoreAccountLinkReturnedEvent`
  * Add support for thin event `V2MoneyManagementPayoutMethodUpdatedEvent` with related object `v2.money_management.PayoutMethod`
  * Remove support for thin event `V2CoreAccountLinkCompletedEvent`
  * Remove support for thin event `V2OffSessionPaymentRequiresCaptureEvent` with related object `v2.payments.OffSessionPayment`

## 12.4.0b2 - 2025-07-09
* [#1536](https://github.com/stripe/stripe-python/pull/1536) Pull in V2 FinancialAccount changes for June release
  * Add support for `close` and `create` methods on resource `v2.money_management.FinancialAccount`
  * Add support for new value `storer` on enums `V2.Core.Account.applied_configurations` and `v2.core.Account.CloseParams.applied_configurations`
  * Add support for `storer` on `V2.Core.Account.Configuration`, `v2.core.Account.CreateParamsConfiguration`, and `v2.core.Account.ModifyParamsConfiguration`
  * Add support for new values `financial_addresses.bank_accounts`, `holds_currencies.gbp`, `inbound_transfers.financial_accounts`, `outbound_payments.bank_accounts`, `outbound_payments.cards`, `outbound_payments.financial_accounts`, `outbound_transfers.bank_accounts`, and `outbound_transfers.financial_accounts` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
  * Add support for new value `storer` on enum `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.configuration`
  * Add support for `status_details` on `V2.MoneyManagement.FinancialAccount`
  * Add support for `status` on `v2.money_management.FinancialAccount.ListParams`
  * Add support for new value `configuration.storer` on enums `v2.core.Account.CreateParams.include`, `v2.core.Account.ModifyParams.include`, and `v2.core.Account.RetrieveParams.include`
  * Add support for thin events `V2CoreAccountIncludingConfigurationStorerCapabilityStatusUpdatedEvent` and `V2CoreAccountIncludingConfigurationStorerUpdatedEvent` with related object `v2.core.Account`
  * Add support for error types `AlreadyExistsError` and `NonZeroBalanceError`

## 12.4.0b1 - 2025-07-01
This release changes the pinned API version to `2025-06-30.preview`.

* [#1520](https://github.com/stripe/stripe-python/pull/1520) Update generated code for beta
  * Change type of `Invoice.CreatePreviewParamsScheduleDetail.billing_mode`, `Invoice.CreatePreviewParamsSubscriptionDetail.billing_mode`, `Quote.CreateParamsSubscriptionDatum.billing_mode`, `Quote.SubscriptionDatum.billing_mode`, `Subscription.CreateParams.billing_mode`, `SubscriptionSchedule.CreateParams.billing_mode`, and `checkout.Session.CreateParamsSubscriptionDatum.billing_mode` from `enum('classic'|'flexible')` to `billing_mode`
  * Add support for `submission_method` on `Dispute.EvidenceDetail`
  * Add support for `on_demand` and `subscriptions` on `Order.CreateParamsPaymentSettingPaymentMethodOptionKlarna` and `Order.ModifyParamsPaymentSettingPaymentMethodOptionKlarna`
  * Change type of `Order.CreateParamsPaymentSettingPaymentMethodOptionKlarna.setup_future_usage`, `Order.ModifyParamsPaymentSettingPaymentMethodOptionKlarna.setup_future_usage`, and `Order.Payment.Setting.PaymentMethodOption.Klarna.setup_future_usage` from `literal('none')` to `enum('none'|'off_session'|'on_session')`
  * Add support for `crypto` on `PaymentAttemptRecord.PaymentMethodDetail` and `PaymentRecord.PaymentMethodDetail`
  * Add support for new value `buut` on enums `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bank` and `PaymentRecord.PaymentMethodDetail.Ideal.bank`
  * Add support for new value `BUUTNL2A` on enums `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bic` and `PaymentRecord.PaymentMethodDetail.Ideal.bic`
  * Change type of `PaymentIntent.ConfirmParamsPaymentMethodOptionGopay.setup_future_usage`, `PaymentIntent.CreateParamsPaymentMethodOptionGopay.setup_future_usage`, `PaymentIntent.ModifyParamsPaymentMethodOptionGopay.setup_future_usage`, and `PaymentIntent.PaymentMethodOption.Gopay.setup_future_usage` from `literal('none')` to `enum('none'|'off_session')`
  * Change `Quote.SubscriptionDatum.billing_mode`, `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.billing_mode`, and `SubscriptionSchedule.billing_mode` to be required
  * Add support for new value `crypto` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
  * Change type of `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.billing_mode`, and `SubscriptionSchedule.billing_mode` from `enum('classic'|'flexible')` to `SubscriptionsResourceBillingMode`
  * Change type of `Subscription.MigrateParams.billing_mode` from `literal('flexible')` to `billing_mode_migrate`
  * Remove support for `billing_mode_details` on `Subscription`
  * Add support for new value `xx` on enums `V2.Core.Account.Configuration.Customer.AutomaticIndirectTax.Location.country`, `V2.Core.Account.Configuration.Customer.Shipping.Address.country`, `V2.Core.Account.Configuration.Merchant.Support.Address.country`, `V2.Core.Account.Identity.BusinessDetail.Address.country`, `V2.Core.Account.Identity.BusinessDetail.ScriptAddress.Kana.country`, `V2.Core.Account.Identity.BusinessDetail.ScriptAddress.Kanji.country`, `V2.Core.Account.Identity.Individual.AdditionalAddress.country`, `V2.Core.Account.Identity.Individual.Address.country`, `V2.Core.Account.Identity.Individual.ScriptAddress.Kana.country`, `V2.Core.Account.Identity.Individual.ScriptAddress.Kanji.country`, `V2.Core.Account.Identity.country`, `V2.Core.Person.AdditionalAddress.country`, `V2.Core.Person.Address.country`, `V2.Core.Person.ScriptAddress.Kana.country`, `V2.Core.Person.ScriptAddress.Kanji.country`, `V2.MoneyManagement.FinancialAccount.country`, `v2.core.Account.CreateParamsConfigurationCustomerShippingAddress.country`, `v2.core.Account.CreateParamsConfigurationMerchantSupportAddress.country`, `v2.core.Account.CreateParamsIdentity.country`, `v2.core.Account.CreateParamsIdentityBusinessDetailAddress.country`, `v2.core.Account.CreateParamsIdentityBusinessDetailScriptAddressKana.country`, `v2.core.Account.CreateParamsIdentityBusinessDetailScriptAddressKanji.country`, `v2.core.Account.CreateParamsIdentityIndividualAdditionalAddress.country`, `v2.core.Account.CreateParamsIdentityIndividualAddress.country`, `v2.core.Account.CreateParamsIdentityIndividualScriptAddressKana.country`, `v2.core.Account.CreateParamsIdentityIndividualScriptAddressKanji.country`, `v2.core.Account.ModifyParamsConfigurationCustomerShippingAddress.country`, `v2.core.Account.ModifyParamsConfigurationMerchantSupportAddress.country`, `v2.core.Account.ModifyParamsIdentity.country`, `v2.core.Account.ModifyParamsIdentityBusinessDetailAddress.country`, `v2.core.Account.ModifyParamsIdentityBusinessDetailScriptAddressKana.country`, `v2.core.Account.ModifyParamsIdentityBusinessDetailScriptAddressKanji.country`, `v2.core.Account.ModifyParamsIdentityIndividualAdditionalAddress.country`, `v2.core.Account.ModifyParamsIdentityIndividualAddress.country`, `v2.core.Account.ModifyParamsIdentityIndividualScriptAddressKana.country`, `v2.core.Account.ModifyParamsIdentityIndividualScriptAddressKanji.country`, `v2.core.Person.CreateParamsAdditionalAddress.country`, `v2.core.Person.CreateParamsAddress.country`, `v2.core.Person.CreateParamsScriptAddressKana.country`, `v2.core.Person.CreateParamsScriptAddressKanji.country`, `v2.core.Person.ModifyParamsAdditionalAddress.country`, `v2.core.Person.ModifyParamsAddress.country`, `v2.core.Person.ModifyParamsScriptAddressKana.country`, and `v2.core.Person.ModifyParamsScriptAddressKanji.country`
  * Add support for new value `unsupported_entity_type` on enums `V2.Core.Account.Configuration.Customer.Capability.AutomaticIndirectTax.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AchDebitPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AcssDebitPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AffirmPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AfterpayClearpayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AlmaPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AmazonPayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.AuBecsDebitPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.BacsDebitPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.BancontactPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.BlikPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.BoletoPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.CardPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.CartesBancairesPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.CashappPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.EpsPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.FpxPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.GbBankTransferPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.GrabpayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.IdealPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.JcbPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.JpBankTransferPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.KakaoPayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.KlarnaPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.KonbiniPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.KrCardPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.LinkPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.MobilepayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.MultibancoPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.MxBankTransferPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.NaverPayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.OxxoPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.P24Payment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.PayByBankPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.PaycoPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.PaynowPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.PromptpayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.RevolutPayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.SamsungPayPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.SepaBankTransferPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.SepaDebitPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.StripeBalance.Payout.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.SwishPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.TwintPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.UsBankTransferPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Merchant.Capability.ZipPayment.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Local.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount.Wire.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.Card.StatusDetail.code`, `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.Payout.StatusDetail.code`, and `V2.Core.Account.Configuration.Recipient.Capability.StripeBalance.StripeTransfer.StatusDetail.code`
  * Add support for `proof_of_address` on `V2.Core.Account.Identity.BusinessDetail.Document`, `v2.core.Account.CreateParamsIdentityBusinessDetailDocument`, and `v2.core.Account.ModifyParamsIdentityBusinessDetailDocument`
  * Add support for new value `xx` on enums `V2.Core.Account.Identity.Individual.nationalities`, `V2.Core.Person.nationalities`, `v2.core.Account.CreateParamsIdentityIndividual.nationalities`, `v2.core.Account.ModifyParamsIdentityIndividual.nationalities`, `v2.core.Person.CreateParams.nationalities`, and `v2.core.Person.ModifyParams.nationalities`
  * Add support for `metadata` on `V2.MoneyManagement.FinancialAccount`
  * Remove support for `description` on `V2.MoneyManagement.FinancialAccount`
  * Add support for new value `pending` on enum `V2.MoneyManagement.FinancialAccount.status`
  * Remove support for `attempts` on `V2.Payments.OffSessionPayment`
  * Change type of `V2.Payments.OffSessionPayment.TransferDatum.amount` from `integer` to `nullable(integer)`
  * Add support for `from_account`, `outbound_payment`, and `outbound_transfer` on `V2.MoneyManagement.ReceivedCredit.BalanceTransfer`
  * Change type of `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type` from `literal('payout_v1')` to `enum('outbound_payment'|'outbound_transfer'|'payout_v1')`
  * Change type of `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.payout_v1` from `string` to `nullable(string)`
  * Change `v2.payments.OffSessionPayment.CreateParamsTransferDatum.amount` to be optional
  * Add support for error codes `recipient_feature_not_active`, `storer_capability_missing`, and `storer_capability_not_active` on `FeatureNotEnabledError`
  * Remove support for error code `outbound_payment_recipient_feature_not_active` on `FeatureNotEnabledError`
  * Add support for error code `insufficient_funds` on `InsufficientFundsError`
  * Remove support for error codes `outbound_payment_insufficient_funds` and `outbound_transfer_insufficient_funds` on `InsufficientFundsError`
  * Add support for error codes `recipient_amount_limit_exceeded` and `recipient_count_limit_exceeded` on `QuotaExceededError`
  * Remove support for error codes `outbound_payment_recipient_amount_limit_exceeded` and `outbound_payment_recipient_count_limit_exceeded` on `QuotaExceededError`
  * Add support for error code `recipient_email_does_not_exist` on `RecipientNotNotifiableError`
  * Remove support for error code `outbound_payment_recipient_email_does_not_exist` on `RecipientNotNotifiableError`

## 12.3.0b2 - 2025-06-26
* [#1531](https://github.com/stripe/stripe-python/pull/1531) Pull in OffSessionPayment changes for the May release

## 12.3.0b1 - 2025-05-29
This release changes the pinned API version to `2025-05-28.preview`.

* [#1509](https://github.com/stripe/stripe-python/pull/1509) Update generated code for beta
  ### Breaking changes
  * Remove support for deprecated previews
    * Remove support for resources `billing.MeterErrorReport`, `gift_cards.Card`, `gift_cards.Transaction`, and `privacy.RedactionJobRootObjects`
    * Remove support for `create`, `list`, `modify`, `retrieve`, and `validate` methods on resource `gift_cards.Card`
    * Remove support for `cancel`, `confirm`, `create`, `list`, `modify`, and `retrieve` methods on resource `gift_cards.Transaction`
    * Remove support for `provisioning` on `Product.CreateParams` and `Product`
    * Remove support for snapshot event `billing.meter_error_report.triggered` with resource `billing.MeterErrorReport`
    * Remove support for error codes `gift_card_balance_insufficient`, `gift_card_code_exists`, and `gift_card_inactive` on `QuotePreviewInvoice.LastFinalizationError` and `StripeError`
  * Remove support for values `credits_attributed_to_debits` and `legacy_prorations` from enums `Invoice.CreatePreviewParamsScheduleDetail.billing_mode`, `Invoice.CreatePreviewParamsSubscriptionDetail.billing_mode`, `Quote.CreateParamsSubscriptionDatum.billing_mode`, `Quote.SubscriptionDatum.billing_mode`, `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.CreateParams.billing_mode`, `Subscription.billing_mode`, `SubscriptionSchedule.CreateParams.billing_mode`, `SubscriptionSchedule.billing_mode`, and `checkout.Session.CreateParamsSubscriptionDatum.billing_mode`
  * Change type of `checkout.Session.ModifyParamsLineItem.quantity` from `emptyable(longInteger)` to `longInteger`
  * Change `CreditNote.post_payment_amount` to be required
  * Change `CreditNote.pre_payment_amount` to be required
  * Remove support for `credits` on `Order.CreateParams`, `Order.ModifyParams`, and `Order`
  * Remove support for `amount_remaining` on `Order`
  * Remove support for `amount_credit` on `Order.TotalDetail`
  * Change type of `PaymentAttemptRecord.metadata` and `PaymentRecord.metadata` from `nullable(map(string: string))` to `map(string: string)`
  * Remove support for `async_workflows` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.DecrementAuthorizationParams`, `PaymentIntent.IncrementAuthorizationParams`, `PaymentIntent.ModifyParams`, and `PaymentIntent`
  * Change type of `PaymentRecord.ReportPaymentAttemptCanceledParams.metadata`, `PaymentRecord.ReportPaymentAttemptFailedParams.metadata`, `PaymentRecord.ReportPaymentAttemptGuaranteedParams.metadata`, `PaymentRecord.ReportPaymentAttemptParams.metadata`, and `PaymentRecord.ReportPaymentParams.metadata` from `map(string: string)` to `emptyable(map(string: string))`
  * Change type of `Privacy.RedactionJob.objects` from `$Privacy.RedactionJobRootObjects` to `RedactionResourceRootObjects`
  * Change type of `Privacy.RedactionJob.status` from `string` to `enum`
  * Change type of `Privacy.RedactionJob.validation_behavior` from `string` to `enum('error'|'fix')`
  * Change type of `Privacy.RedactionJobValidationError.code` from `string` to `enum`
  * Change type of `Privacy.RedactionJobValidationError.erroring_object` from `map(string: string)` to `RedactionResourceErroringObject`
  * Remove support for `status_details` and `status` on `Tax.Association`

  ### Other changes
  * Add support for `migrate` method on resource `Subscription`
  * Add support for `distance`, `pickup_location_name`, `return_location_name`, and `vehicle_identification_number` on `Charge.CaptureParamsPaymentDetailCarRental`, `Charge.ModifyParamsPaymentDetailCarRental`, `PaymentIntent.CaptureParamsPaymentDetailCarRental`, `PaymentIntent.ConfirmParamsPaymentDetailCarRental`, `PaymentIntent.CreateParamsPaymentDetailCarRental`, `PaymentIntent.ModifyParamsPaymentDetailCarRental`, and `PaymentIntent.PaymentDetail.CarRental`
  * Add support for `driver_identification_number` and `driver_tax_number` on `Charge.CaptureParamsPaymentDetailCarRentalDriver`, `Charge.ModifyParamsPaymentDetailCarRentalDriver`, `PaymentIntent.CaptureParamsPaymentDetailCarRentalDriver`, `PaymentIntent.ConfirmParamsPaymentDetailCarRentalDriver`, `PaymentIntent.CreateParamsPaymentDetailCarRentalDriver`, `PaymentIntent.ModifyParamsPaymentDetailCarRentalDriver`, and `PaymentIntent.PaymentDetail.CarRental.Driver`
  * Add support for new values `classic` and `flexible` on enums `Invoice.CreatePreviewParamsScheduleDetail.billing_mode`, `Invoice.CreatePreviewParamsSubscriptionDetail.billing_mode`, `Quote.CreateParamsSubscriptionDatum.billing_mode`, `Quote.SubscriptionDatum.billing_mode`, `QuotePreviewSubscriptionSchedule.billing_mode`, `Subscription.CreateParams.billing_mode`, `Subscription.billing_mode`, `SubscriptionSchedule.CreateParams.billing_mode`, `SubscriptionSchedule.billing_mode`, and `checkout.Session.CreateParamsSubscriptionDatum.billing_mode`
  * Add support for `institution` on `FinancialConnections.Account`
  * Add support for `countries` on `FinancialConnections.Institution`
  * Change type of `Invoice.CreatePreviewParamsSubscriptionDetail.cancel_at`, `Subscription.CreateParams.cancel_at`, and `Subscription.ModifyParams.cancel_at` from `DateTime` to `DateTime | enum('max_period_end'|'min_period_end')`
  * Add support for `location` and `reader` on `PaymentAttemptRecord.PaymentMethodDetail.Affirm`, `PaymentAttemptRecord.PaymentMethodDetail.WechatPay`, `PaymentRecord.PaymentMethodDetail.Affirm`, and `PaymentRecord.PaymentMethodDetail.WechatPay`
  * Add support for `hooks` on `PaymentIntent.CaptureParams`, `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.DecrementAuthorizationParams`, `PaymentIntent.IncrementAuthorizationParams`, `PaymentIntent.ModifyParams`, and `PaymentIntent`
  * Add support for `card_present` on `PaymentIntentAmountDetailsLineItem.PaymentMethodOption`
  * Add support for `livemode` on `Privacy.RedactionJob`
  * Add support for `billing_thresholds` on `QuotePreviewSubscriptionSchedule.DefaultSetting`, `QuotePreviewSubscriptionSchedule.Phase.Item`, and `QuotePreviewSubscriptionSchedule.Phase`
  * Add support for `billing_mode_details` on `Subscription`
  * Add support for `tax_transaction_attempts` on `Tax.Association`
  * Add support for `confirm_config` on `Terminal.Reader.Action.ConfirmPaymentIntent` and `terminal.Reader.ConfirmPaymentIntentParams`  
  * Add support for error code `forwarding_api_upstream_error` on `QuotePreviewInvoice.LastFinalizationError`

## 12.2.0b1 - 2025-04-30
This release changes the pinned API version to `2025-04-30.preview`.

* [#1498](https://github.com/stripe/stripe-python/pull/1498) Update generated code for beta
  * Add support for new values `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, and `la_tin` on enums `Checkout.Session.CollectedInformation.TaxId.type`, `Checkout.Session.CustomerDetail.TaxId.type`, `Invoice.CustomerTaxId.type`, `Order.TaxDetail.TaxId.type`, `QuotePreviewInvoice.CustomerTaxId.type`, `Tax.Calculation.CustomerDetail.TaxId.type`, `Tax.Transaction.CustomerDetail.TaxId.type`, and `TaxId.type`
  * Change `Checkout.Session.AutomaticTax.provider`, `Invoice.AutomaticTax.provider`, `Quote.AutomaticTax.provider`, and `QuotePreviewInvoice.AutomaticTax.provider` to be required
  * Add support for `account_number` on `ConfirmationToken.PaymentMethodPreview.AcssDebit` and `PaymentMethod.AcssDebit`
  * Add support for new values `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, and `la_tin` on enums `Customer.CreateParams.type`, `Customer.CreateParamsTaxIdDatum.type`, `CustomerService.CreateParamsTaxIdDatum.type`, `CustomerTaxIdService.CreateParams.type`, `Invoice.CreatePreviewParamsCustomerDetailTaxId.type`, `InvoiceService.CreatePreviewParamsCustomerDetailTaxId.type`, `Order.CreateParamsTaxDetailTaxId.type`, `Order.ModifyParamsTaxDetailTaxId.type`, `OrderService.CreateParamsTaxDetailTaxId.type`, `OrderService.UpdateParamsTaxDetailTaxId.type`, `TaxId.CreateParams.type`, `TaxIdService.CreateParams.type`, `tax.Calculation.CreateParamsCustomerDetailTaxId.type`, and `tax.CalculationService.CreateParamsCustomerDetailTaxId.type`
  * Change type of `InvoiceLineItem.Parent.SubscriptionItemDetail.subscription` from `string` to `nullable(string)`
  * Add support for `billing_mode` on `Quote.CreateParamsSubscriptionDatum`, `QuoteService.CreateParamsSubscriptionDatum`, `Subscription.CreateParams`, `SubscriptionSchedule.CreateParams`, `SubscriptionScheduleService.CreateParams`, and `SubscriptionService.CreateParams`
  * Add support for `bf`, `cm`, and `cv` on `Tax.Registration.CountryOption`, `tax.Registration.CreateParamsCountryOption`, and `tax.RegistrationService.CreateParamsCountryOption`
  * Add support for new value `2025-04-30.basil` on enums `WebhookEndpoint.CreateParams.api_version` and `WebhookEndpointService.CreateParams.api_version`
* [#1501](https://github.com/stripe/stripe-python/pull/1501) Update generated code for beta
  * Add support for `billing_mode` on `Invoice.CreatePreviewParamsScheduleDetail`, `Invoice.CreatePreviewParamsSubscriptionDetail`, `InvoiceService.CreatePreviewParamsScheduleDetail`, `InvoiceService.CreatePreviewParamsSubscriptionDetail`, `Quote.SubscriptionDatum`, `QuotePreviewSubscriptionSchedule`, `SubscriptionSchedule`, `Subscription`, `checkout.Session.CreateParamsSubscriptionDatum`, and `checkout.SessionService.CreateParamsSubscriptionDatum`
  * Add support for new value `balance_settings.updated` on enum `Event.type`
  * Add support for new value `balance_settings.updated` on enums `WebhookEndpoint.ModifyParams.enabled_events` and `WebhookEndpointService.UpdateParams.enabled_events`

## 12.1.0b3 - 2025-04-17
* [#1495](https://github.com/stripe/stripe-python/pull/1495) Update generated code for beta
  * Add support for new resources `FxQuote` and `PaymentIntentAmountDetailsLineItem`
  * Add support for `create`, `list`, and `retrieve` methods on resource `FxQuote`
  * Remove support for `attach_payment_intent` method on resource `Invoice`
  * Add support for `registration_date` on `Account.Company`, `Account.CreateParamsCompany`, `Account.UpdateParamsCompany`, and `Token.CreateParamsAccountCompany`
  * Add support for `customer_reference` and `order_reference` on `Charge.CaptureParamsPaymentDetail`, `Charge.UpdateParamsPaymentDetail`, `PaymentIntent.CaptureParamsPaymentDetail`, `PaymentIntent.ConfirmParamsPaymentDetail`, `PaymentIntent.CreateParamsPaymentDetail`, `PaymentIntent.PaymentDetail`, and `PaymentIntent.UpdateParamsPaymentDetail`
  * Add support for `tax_id` on `Charge.BillingDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatumBillingDetail`, `ConfirmationToken.PaymentMethodPreview.BillingDetail`, `PaymentIntent.ConfirmParamsPaymentMethodDatumBillingDetail`, `PaymentIntent.CreateParamsPaymentMethodDatumBillingDetail`, `PaymentIntent.UpdateParamsPaymentMethodDatumBillingDetail`, `PaymentMethod.BillingDetail`, `PaymentMethod.CreateParamsBillingDetail`, `PaymentMethod.UpdateParamsBillingDetail`, `SetupIntent.ConfirmParamsPaymentMethodDatumBillingDetail`, `SetupIntent.CreateParamsPaymentMethodDatumBillingDetail`, `SetupIntent.UpdateParamsPaymentMethodDatumBillingDetail`, and `treasury.OutboundPayment.CreateParamsDestinationPaymentMethodDatumBillingDetail`
  * Add support for `price_data` on `checkout.Session.UpdateParamsLineItem`
  * Change type of `checkout.Session.UpdateParamsLineItem.quantity` from `longInteger` to `emptyable(longInteger)`
  * Add support for `script` on `Coupon.CreateParams` and `Coupon`
  * Add support for `type` on `Coupon`
  * Add support for new value `fx_quote.expired` on enum `Event.type`
  * Add support for new value `affirm` on enums `Invoice.CreateParamsPaymentSetting.payment_method_types`, `Invoice.PaymentSetting.payment_method_types`, `Invoice.UpdateParamsPaymentSetting.payment_method_types`, `QuotePreviewInvoice.PaymentSetting.payment_method_types`, `Subscription.CreateParamsPaymentSetting.payment_method_types`, `Subscription.PaymentSetting.payment_method_types`, and `Subscription.UpdateParamsPaymentSetting.payment_method_types`
  * Add support for `fx_quote` on `PaymentIntent.ConfirmParams`, `PaymentIntent.CreateParams`, `PaymentIntent.UpdateParams`, `PaymentIntent`, `Transfer.CreateParams`, and `Transfer`
  * Add support for `discount_amount`, `line_items`, `shipping`, and `tax` on `PaymentIntent.AmountDetail`
  * Add support for `pix` on `PaymentMethodConfiguration.CreateParams`, `PaymentMethodConfiguration.UpdateParams`, and `PaymentMethodConfiguration`
  * Add support for `us_cfpb_data` on `Person` and `Token.CreateParamsPerson`
  * Add support for `pending_reason` on `Refund`
  * Add support for `aw`, `az`, `bd`, `bj`, `et`, `kg`, `la`, and `ph` on `TaxRegistration.CountryOption` and `tax.Registration.CreateParamsCountryOption`
  * Add support for new value `fx_quote.expired` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.UpdateParams.enabled_events`
  * Add support for snapshot event `fx_quote.expired` with resource `FxQuote`

## 12.1.0b2 - 2025-04-10
* [#1490](https://github.com/stripe/stripe-python/pull/1490) Handle external account
  - Changes `external_account` field in `external_account_service.create` from `string` to a union type.
* [#1489](https://github.com/stripe/stripe-python/pull/1489) Update generated code for beta
  ### Breaking changes
  * Change type of `V2MoneyManagementReceivedDebit.status_transitions` from `an object` to `nullable(an object)`
  * Remove support for values `bank_accounts.local_uk`, `bank_accounts.wire_uk`, `cards_uk`, and `crypto_wallets_v2` from enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`

  ### Additions
  * Add support for new resources `Privacy.RedactionJobRootObjects`, `Privacy.RedactionJobValidationError`, and `Privacy.RedactionJob`
  * Add support for `cancel`, `create`, `list`, `modify`, `retrieve`, `run`, and `validate` methods on resource `RedactionJob`
  * Add support for `list` and `retrieve` methods on resource `RedactionJobValidationError`
  * Add support for `minority_owned_business_designation` on `Account.BusinessProfile`, `Account.CreateParamsBusinessProfile`, and `Account.UpdateParamsBusinessProfile`
  * Add support for new value `verification_legal_entity_structure_mismatch` on enums `Account.FutureRequirement.Error.code`, `Account.Requirement.Error.code`, `AccountCapability.FutureRequirement.Error.code`, `AccountCapability.Requirement.Error.code`, `AccountPerson.FutureRequirement.Error.code`, `AccountPerson.Requirement.Error.code`, `BankAccount.FutureRequirement.Error.code`, and `BankAccount.Requirement.Error.code`
  * Add support for `export_tax_transactions` and `payment_disputes` on `AccountSession.CreateParamsComponent`
  * Add support for new value `tax_id_prohibited` on enums `Invoice.LastFinalizationError.code`, `PaymentIntent.LastPaymentError.code`, `QuotePreviewInvoice.LastFinalizationError.code`, `SetupAttempt.SetupError.code`, `SetupIntent.LastSetupError.code`, and `StripeError.code`
  * Add support for new value `fixed_term_loan` on enum `CapitalFinancingOffer.type`
  * Add support for `wallet_options` on `CheckoutSession` and `checkout.Session.CreateParams`
  * Add support for new values `privacy.redaction_job.canceled`, `privacy.redaction_job.created`, `privacy.redaction_job.ready`, `privacy.redaction_job.succeeded`, and `privacy.redaction_job.validation_error` on enum `Event.type`
  * Add support for `klarna` on `PaymentMethodDomain`
  * Change type of `TaxCalculationLineItem.reference` from `nullable(string)` to `string`
  * Add support for `in` on `TaxRegistration.CountryOption` and `tax.Registration.CreateParamsCountryOption`
  * Add support for new values `privacy.redaction_job.canceled`, `privacy.redaction_job.created`, `privacy.redaction_job.ready`, `privacy.redaction_job.succeeded`, and `privacy.redaction_job.validation_error` on enums `WebhookEndpoint.CreateParams.enabled_events` and `WebhookEndpoint.UpdateParams.enabled_events`

## 12.1.0b1 - 2025-04-02
This release changes the pinned API version to `2025-03-31.preview`.

#### New APIs for Accounts v2 in private preview

See [SaaS platform payments with subscription billing using Accounts v2](https://docs.stripe.com/connect/accounts-v2/saas-platform-payments-billing)

* [#1455](https://github.com/stripe/stripe-python/pull/1455) , [#1477](https://github.com/stripe/stripe-python/pull/1477), [#1482](https://github.com/stripe/stripe-python/pull/1482) Update generated code for beta

### Breaking changes:
* ⚠️ Change `CheckoutSession.Permission.update` to be optional
* ⚠️ Change `PaymentAttemptRecord.PaymentMethodDetail.custom` and `PaymentRecord.PaymentMethodDetail.custom` to be optional
* ⚠️ Change type of `Order.CreateParamsPaymentSettingPaymentMethodOptionWechatPay.client` and `Order.UpdateParamsPaymentSettingPaymentMethodOptionWechatPay.client` to be optional
* ⚠️ Change type of `PaymentAttemptRecord.PaymentMethodDetail.type` and `PaymentRecord.PaymentMethodDetail.type` from `literal('custom')` to `string`
* ⚠️ Change type of `PaymentAttemptRecord.payment_record` from `string` to `nullable(string)`
* ⚠️ Change type of `PaymentRecord.latest_payment_attempt_record` from `string` to `nullable(string)`
* ⚠️ Change type of `QuotePreviewInvoice.Parent.SubscriptionDetail.subscription` from `string` to `expandable($Subscription)`
* ⚠️ Remove support for `AmountOverpaid` on `InvoicePayment`
* ⚠️ Remove support for `ApplicationFeeAmount`, `PaidOutOfBand`, and `Paid` on `QuotePreviewInvoice`
* ⚠️ Remove support for `billing_thresholds` on `QuotePreviewSubscriptionSchedule.DefaultSetting`, `QuotePreviewSubscriptionSchedule.Phase.Item`, and `QuotePreviewSubscriptionSchedule.Phase`
* ⚠️ Remove support for `coupon` on `QuotePreviewSubscriptionSchedule.Phase`
* ⚠️ Remove support for `RateCardSubscriptionDetails` on `InvoiceItemParent`
* ⚠️ Remove support for values `out_of_band_payment` and `payment_record` from enum `InvoicePayment.Payment.type`

### Additions
* Add support for `billie` on `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, and `PaymentIntent.UpdateParamsPaymentMethodOption`
* Add support for `confirmation_secret`, `parent`, and `total_taxes` on `QuotePreviewInvoice`
* Add support for `context` on `Event`
* Add support for `create`, `delete`, `list`, `modify`, and `retrieve` methods on a new `ExternalAccountService` to access cards and bank accounts made available in the new path `v1/external_accounts`
* Add support for `customer_account` on `BillingCreditBalanceSummary`, `BillingCreditGrant`, `BillingPortalSession`, `CheckoutSession`, `ConfirmationToken.PaymentMethodPreview`, `CreditNote.ListParams`, `CreditNote`, `CustomerBalanceTransaction`, `CustomerCashBalanceTransaction`, `CustomerCashBalance`, `CustomerPaymentMethod`, `CustomerSession.CreateParams`, `CustomerSession`, `CustomerTaxId.Owner`, `CustomerTaxId`, `Customer`, `Discount`, `FinancialConnectionsAccount.AccountHolder`, `FinancialConnectionsSession.AccountHolder`, `Invoice.CreateParams`, `Invoice.CreatePreviewParams`, `Invoice.ListParams`, `InvoiceItem.CreateParams`, `InvoiceItem.ListParams`, `InvoiceItem`, `Invoice`, `PaymentIntent.CreateParams`, `PaymentIntent.ListParams`, `PaymentIntent.UpdateParams`, `PaymentIntent`, `PaymentMethod.AttachParams`, `PaymentMethod`, `PromotionCode.CreateParams`, `PromotionCode.ListParams`, `PromotionCode`, `Quote.CreateParams`, `Quote.ListParams`, `Quote.UpdateParams`, `QuotePreviewInvoice`, `QuotePreviewSubscriptionSchedule`, `Quote`, `SetupAttempt`, `SetupIntent.CreateParams`, `SetupIntent.ListParams`, `SetupIntent.UpdateParams`, `SetupIntent`, `Subscription.CreateParams`, `Subscription.ListParams`, `SubscriptionSchedule.CreateParams`, `SubscriptionSchedule.ListParams`, `SubscriptionSchedule`, `Subscription`, `TaxId.CreateParamsOwner`, `TaxId.ListParamsOwner`, `TaxId.Owner`, `TaxId`, `billing.CreditBalanceSummary.RetrieveParams`, `billing.CreditBalanceTransaction.ListParams`, `billing.CreditGrant.CreateParams`, `billing.CreditGrant.ListParams`, `billingportal.Session.CreateParams`, `checkout.Session.CreateParams`, `checkout.Session.ListParams`, `financialconnections.Account.ListParamsAccountHolder`, and `financialconnections.Session.CreateParamsAccountHolder`
* Add support for `id` and `text` on `TerminalReader.Action.CollectInput.Input.Selection.Choice`, `TerminalReader.Action.CollectInput.Input.Selection`, and `terminal.Reader.CollectInputsParamsInputSelectionChoice`
* Add support for `installments` on `ConfirmationToken.PaymentMethodOption.Card`
* Add support for `interchange_fees_amount`, `net_total_amount`, `network_fees_amount`, `other_fees_amount`, `other_fees_count`, and `transaction_amount` on `IssuingSettlement`
* Add support for `modify` and `retrieve` methods on resource `BalanceSettings`
* Add support for `network_data` on `IssuingDisputeSettlementDetail`
* Add support for `new resources` BalanceSettings
* Add support for new values `stripe_balance_payment_debit_reversal` and `stripe_balance_payment_debit` on enum `BalanceTransaction.type`
* Add support for new values `forwarding_api_retryable_upstream_error`, `setup_intent_mobile_wallet_unsupported`, `v2_account_disconnection_unsupported`, and `v2_account_missing_configuration` on enum `QuotePreviewInvoice.LastFinalizationError.code`
* Add support for new values `klarna`, `nz_bank_account`, and `stripe_balance` on enum `QuotePreviewInvoice.PaymentSetting.payment_method_types`
* Add support for `payment_method_options` on `ConfirmationToken.CreateParams`
* Add support for `payout_method` on `Payout.CreateParams` and `Payout`
* Add support for `provider` on `CheckoutSession.AutomaticTax`, `Invoice.AutomaticTax`, `Quote.AutomaticTax`, and `QuotePreviewInvoice.AutomaticTax`
* Add support for `related_customer_account` on `IdentityVerificationSession`, `identity.VerificationSession.CreateParams`, and `identity.VerificationSession.ListParams`
* Add support for `reported_by` on `PaymentAttemptRecord`
* Add support for `stripe_balance_payments` on `Account.Capability`, `Account.CreateParamsCapability`, and `Account.UpdateParamsCapability`
* Add support for `stripe_balance` on `Charge.PaymentMethodDetail`, `ConfirmationToken.CreateParamsPaymentMethodDatum`, `ConfirmationToken.PaymentMethodPreview`, `CustomerPaymentMethod`, `PaymentAttemptRecord.PaymentMethodDetail`, `PaymentIntent.ConfirmParamsPaymentMethodDatum`, `PaymentIntent.ConfirmParamsPaymentMethodOption`, `PaymentIntent.CreateParamsPaymentMethodDatum`, `PaymentIntent.CreateParamsPaymentMethodOption`, `PaymentIntent.PaymentMethodOption`, `PaymentIntent.UpdateParamsPaymentMethodDatum`, `PaymentIntent.UpdateParamsPaymentMethodOption`, `PaymentMethod.CreateParams`, `PaymentMethod`, `PaymentRecord.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail`, `SetupIntent.ConfirmParamsPaymentMethodDatum`, `SetupIntent.CreateParamsPaymentMethodDatum`, and `SetupIntent.UpdateParamsPaymentMethodDatum`
* Add support for `tax_calculation_reference` on `CreditNoteLineItem`, `CreditNotePreviewLines`, `InvoiceLineItem`, `LineItem`, `PaymentLinkLineItem`, `QuoteComputedUpfrontLineItems`, `QuoteLineItem`, and `SessionLineItem`
* Add support for `update_line_items` on `CheckoutSession.Permission` and `checkout.Session.CreateParamsPermission`
* Add support for `update_shipping_details` on `CheckoutSession.Permission` and `checkout.Session.CreateParamsPermission`

### Changes
* ⚠️ [#1476](https://github.com/stripe/stripe-python/pull/1476) Update add_beta_version logic
  * ⚠️ stripe.add_beta_version` will use the highest version number used for a beta feature instead of raising an `Exception` on a conflict as it had done previously.
* Change `CreditNote.refunds` to be required
* Change `CustomerSession.CreateParams.customer`, `InvoiceItem.CreateParams.customer`, `PaymentMethod.AttachParams.customer`, `Subscription.CreateParams.customer`, `billing.CreditBalanceSummary.RetrieveParams.customer`, `billing.CreditBalanceTransaction.ListParams.customer`, `billing.CreditGrant.CreateParams.customer`, and `billingportal.Session.CreateParams.customer` to be optional
* Change `Invoice.amount_overpaid` and `QuotePreviewInvoice.amount_overpaid` to be required
* Change `PaymentRecord.ReportPaymentParams.payment_reference` to be optional
* Change type of `Invoice.Parent.SubscriptionDetail.PauseCollection.behavior` and `QuotePreviewInvoice.Parent.SubscriptionDetail.PauseCollection.behavior` from `string` to `enum('keep_as_draft'|'mark_uncollectible'|'void')`
* Change type of `InvoicePayment.is_default` from `nullable(boolean)` to `boolean`
* Change type of `PaymentAttemptRecord.PaymentMethodDetail.custom` and `PaymentRecord.PaymentMethodDetail.custom` from `nullable(PaymentsPrimitivesPaymentRecordsResourcePaymentMethodCustomDetails)` to `PaymentsPrimitivesPaymentRecordsResourcePaymentMethodCustomDetails`

### New APIs for Accounts v2 in private preview
* Add support for `close`, `create`, `list`, `modify`, and `retrieve` methods on resource `V2.Core.Account`
* Add support for `create` method on resource `V2.Core.AccountLink`
* Add support for new resources `V2.Core.AccountLink`, `V2.Core.Account`, `V2.Core.Person`, `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`
* Add support for new thin events `V2CoreAccountIncludingConfigurationCustomerCapabilityStatusUpdatedEvent`, `V2CoreAccountIncludingConfigurationCustomerUpdatedEvent`, `V2CoreAccountIncludingConfigurationMerchantCapabilityStatusUpdatedEvent`, `V2CoreAccountIncludingConfigurationMerchantUpdatedEvent`, `V2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent`, `V2CoreAccountIncludingConfigurationRecipientUpdatedEvent`, `V2CoreAccountIncludingIdentityUpdatedEvent`, and `V2CoreAccountIncludingRequirementsUpdatedEvent`
* Add support for new thin event `V2CoreAccountLinkCompletedEvent` with related object `V2.Core.AccountLink`
* Add support for new thin events `V2CoreAccountPersonCreatedEvent`, `V2CoreAccountPersonDeletedEvent`, and `V2CoreAccountPersonUpdatedEvent` with related object `V2.Core.Person`

### New APIs for Money CardManagement
* Add support for `acknowledge_confirmation_of_payee`, `archive`, `create`, `initiate_confirmation_of_payee`, and `retrieve` methods on resource `V2.Core.Vault.GbBankAccount`
* Add support for `archive`, `list`, `retrieve`, and `unarchive` methods on resource `V2.MoneyManagement.PayoutMethod`
* Add support for `archive`, `create`, `modify`, and `retrieve` methods on resource `V2.Core.Vault.UsBankAccount`
* Add support for `cancel`, `create`, `list`, and `retrieve` methods on resources `V2.MoneyManagement.OutboundPayment` and `V2.MoneyManagement.OutboundTransfer`
* Add support for `cancel`, `create`, `list`, `modify`, and `retrieve` methods on resource `V2.MoneyManagement.OutboundSetupIntent`
* Add support for `create` method on resource `V2.MoneyManagement.OutboundPaymentQuote`
* Add support for `create`, `list`, and `retrieve` methods on resources `V2.MoneyManagement.FinancialAddress` and `V2.MoneyManagement.InboundTransfer`
* Add support for `list` and `retrieve` methods on resources `V2.MoneyManagement.Adjustment`, `V2.MoneyManagement.FinancialAccount`, `V2.MoneyManagement.ReceivedCredit`, `V2.MoneyManagement.ReceivedDebit`, `V2.MoneyManagement.TransactionEntry`, and `V2.MoneyManagement.Transaction`
* Add support for new thin events `V2MoneyManagementOutboundPaymentCanceledEvent`, `V2MoneyManagementOutboundPaymentCreatedEvent`, `V2MoneyManagementOutboundPaymentFailedEvent`, `V2MoneyManagementOutboundPaymentPostedEvent`, and `V2MoneyManagementOutboundPaymentReturnedEvent` with related object `V2.MoneyManagement.OutboundPayment`
* Add support for new thin events `V2MoneyManagementOutboundTransferCanceledEvent`, `V2MoneyManagementOutboundTransferCreatedEvent`, `V2MoneyManagementOutboundTransferFailedEvent`, `V2MoneyManagementOutboundTransferPostedEvent`, and `V2MoneyManagementOutboundTransferReturnedEvent` with related object `V2.MoneyManagement.OutboundTransfer`
* Add support for new thin events `V2MoneyManagementReceivedCreditAvailableEvent`, `V2MoneyManagementReceivedCreditFailedEvent`, `V2MoneyManagementReceivedCreditReturnedEvent`, and `V2MoneyManagementReceivedCreditSucceededEvent` with related object `V2.MoneyManagement.ReceivedCredit`
* Add support for new thin events `V2MoneyManagementReceivedDebitCanceledEvent`, `V2MoneyManagementReceivedDebitFailedEvent`, `V2MoneyManagementReceivedDebitPendingEvent`, `V2MoneyManagementReceivedDebitSucceededEvent`, and `V2MoneyManagementReceivedDebitUpdatedEvent` with related object `V2.MoneyManagement.ReceivedDebit`
* Add support for new error types `AlreadyCanceledError`, `BlockedByStripeError`, `ControlledByDashboardError`, `FeatureNotEnabledError`, `FinancialAccountNotOpenError`, `InsufficientFundsError`, `InvalidPayoutMethodError`, `NotCancelableError`, and `RecipientNotNotifiableError`
* Add support for new resources `V2.FinancialAddressCreditSimulation`, `V2.FinancialAddressGeneratedMicrodeposits`, `V2.MoneyManagement.Adjustment`, `V2.MoneyManagement.FinancialAccount`, `V2.MoneyManagement.FinancialAddress`, `V2.MoneyManagement.InboundTransfer`, `V2.MoneyManagement.OutboundPaymentQuote`, `V2.MoneyManagement.OutboundPayment`, `V2.MoneyManagement.OutboundSetupIntent`, `V2.MoneyManagement.OutboundTransfer`, `V2.MoneyManagement.PayoutMethod`, `V2.MoneyManagement.PayoutMethodsBankAccountSpec`, `V2.MoneyManagement.ReceivedCredit`, `V2.MoneyManagement.ReceivedDebit`, `V2.MoneyManagement.TransactionEntry`, and `V2.MoneyManagement.Transaction`
* Add support for new values `account_number`, `fedwire_routing_number`, and `routing_number` on enum `InvalidPaymentMethod.invalid_param`
* Add support for new thin event `V2MoneyManagementFinancialAccountCreatedEvent` with related object `V2.MoneyManagement.FinancialAccount`
* Add support for new thin events `V2MoneyManagementFinancialAddressActivatedEvent` and `V2MoneyManagementFinancialAddressFailedEvent` with related object `V2.MoneyManagement.FinancialAddress`
* Add support for new thin events `V2MoneyManagementInboundTransferAvailableEvent`, `V2MoneyManagementInboundTransferBankDebitFailedEvent`, `V2MoneyManagementInboundTransferBankDebitProcessingEvent`, `V2MoneyManagementInboundTransferBankDebitQueuedEvent`, `V2MoneyManagementInboundTransferBankDebitReturnedEvent`, and `V2MoneyManagementInboundTransferBankDebitSucceededEvent` with related object `V2.MoneyManagement.InboundTransfer`
* Add support for `retrieve` method on resource `V2.MoneyManagement.PayoutMethodsBankAccountSpec`

## 11.7.0b1 - 2025-03-18
This release changes the pinned API version to `2025-02-24.acacia`.

* [#1469](https://github.com/stripe/stripe-python/pull/1469) Beta SDK updates between Open API versions 1473 and 1505
  * Add support for `target_date` on parameter classes `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit`, `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit`, `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit`, and `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit` and resource classes `stripe.Order.Payment.Settings.PaymentMethodOptions.AcssDebit` and `stripe.Order.Payment.Settings.PaymentMethodOptions.SepaDebit`
  * Add support for `succeed_input_collection` and `timeout_input_collection` on resource `stripe.terminal.Reader`

## 11.6.0b1 - 2025-02-07
* [#1449](https://github.com/stripe/stripe-python/pull/1449) Update generated code for beta
  * Add support for `rejected_reason` on resource class `stripe.Account.RiskControls`
  * Add support for `product_tax_code_selector` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `brand_product` on resource classes `stripe.Charge.PaymentMethodDetails.AmazonPay.Funding.Card` and `stripe.Charge.PaymentMethodDetails.RevolutPay.Funding.Card`
  * Add support for `prices` on parameter classes `stripe.billing.CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope` and `stripe.billing.CreditGrant.CreateParamsApplicabilityConfigScope` and resource class `stripe.billing.CreditGrant.ApplicabilityConfig.Scope`
  * Add support for `restrictions` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Change type of `political_exposure` on  `stripe.Account.CreatePersonParams`, `stripe.Account.ModifyPersonParams`, and `stripe.Token.CreateParamsPerson` from `str` to `Literal['existing', 'none']`
  * Change type of `price_type` on  `stripe.billing.CreditGrant.ApplicabilityConfig.Scope` from `Literal['metered']` to `Optional[Literal['metered']]`

## 11.5.0b3 - 2025-01-23
* [#1447](https://github.com/stripe/stripe-python/pull/1447) Update generated code for beta
  * Remove support for `stripe_account` on resource classes `stripe.terminal.Reader.Action.CollectPaymentMethod`, `stripe.terminal.Reader.Action.ConfirmPaymentIntent`, `stripe.terminal.Reader.Action.ProcessPaymentIntent`, and `stripe.terminal.Reader.Action.RefundPayment`

## 11.5.0b2 - 2025-01-17
This release changes the pinned API version to `2025-01-27.acacia`.

* [#1439](https://github.com/stripe/stripe-python/pull/1439) Update generated code for beta
  * Add support for `pay_by_bank_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `directorship_declaration` on parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
  * Add support for `proof_of_ultimate_beneficial_ownership` on parameter class `stripe.Account.CreateParamsDocuments`
  * Add support for `financial_account` on resource class `stripe.AccountSession.Components`
  * Add support for `issuing_card` on resource class `stripe.AccountSession.Components`
  * Add support for `tax_threshold_monitoring` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `pay_by_bank` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `discounts` on resource `stripe.checkout.Session`
  * Add support for `jpy` on parameter classes `stripe.terminal.Configuration.CreateParamsTipping` and `stripe.terminal.Configuration.ModifyParamsTipping` and resource class `stripe.terminal.Configuration.Tipping`
  * Add support for `always_invoice` on enums `stripe.billing_portal.Configuration.Features.SubscriptionCancel.proration_behavior`, `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionCancel.proration_behavior`, and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionCancel.proration_behavior`
  * Add support for `SD` on enums `stripe.checkout.Session.ShippingAddressCollection.allowed_countries`, `stripe.checkout.Session.CreateParamsShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.ShippingAddressCollection.allowed_countries`, `stripe.PaymentLink.CreateParamsShippingAddressCollection.allowed_countries`, and `stripe.PaymentLink.ModifyParamsShippingAddressCollection.allowed_countries`
  * Add support for `pay_by_bank` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `2025-01-27.acacia` on enum `stripe.WebhookEndpoint.CreateParams.api_version`

## 11.5.0b1 - 2025-01-09
* [#1433](https://github.com/stripe/stripe-python/pull/1433) Update generated code for beta
  * Add support for `directorship_declaration` on resource class `stripe.Account.Company`
  * Add support for `ownership_exemption_reason` on resource class `stripe.Account.Company` and parameter classes `stripe.Account.CreateParamsCompany` and `stripe.Token.CreateParamsAccountCompany`
  * Add support for `brand_product` on resource `stripe.Card` and resource classes `stripe.Source.Card`, `stripe.Source.CardPresent`, and `stripe.Source.ThreeDSecure`
  * Add support for `advice_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
  * Add support for `country` on resource classes `stripe.Charge.PaymentMethodDetails.Paypal`, `stripe.ConfirmationToken.PaymentMethodPreview.Paypal`, and `stripe.PaymentMethod.Paypal`
  * Add support for `phone_number_collection` on parameter class `stripe.PaymentLink.ModifyParams`
  * Add support for `nickname` on parameter classes `stripe.treasury.FinancialAccount.CreateParams` and `stripe.treasury.FinancialAccount.ModifyParams` and resource `stripe.treasury.FinancialAccount`
  * Add support for `forwarding_settings` on parameter class `stripe.treasury.FinancialAccount.ModifyParams`
  * Add support for `_cls_close` on resource `stripe.treasury.FinancialAccount`
  * Add support for `close` on resource `stripe.treasury.FinancialAccount`
  * Add support for `is_default` on resource `stripe.treasury.FinancialAccount`
  * Add support for `destination_payment_method_data` on parameter class `stripe.treasury.OutboundTransfer.CreateParams`
  * Add support for `financial_account` on resource class `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails`
  * Add support for `outbound_transfer` on resource class `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails`
  * Remove support for `always_invoice` on enums `stripe.billing_portal.Configuration.Features.SubscriptionCancel.proration_behavior`, `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionCancel.proration_behavior`, and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionCancel.proration_behavior`
  * Add support for `al_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `financial_account` on enum `stripe.treasury.OutboundTransfer.DestinationPaymentMethodDetails.type`
  * Add support for `outbound_transfer` on enums `stripe.treasury.ReceivedCredit.LinkedFlows.SourceFlowDetails.type` and `stripe.treasury.ReceivedCredit.ListParamsLinkedFlows.source_flow_type`
  * Change type of `pretax_credit_amounts` on  `stripe.CreditNote` and `stripe.CreditNoteLineItem` from `Optional[List[PretaxCreditAmount]]` to `List[PretaxCreditAmount]`

## 11.4.0b3 - 2024-12-12
This release changes the pinned API version to `2024-12-18.acacia`.

* [#1429](https://github.com/stripe/stripe-python/pull/1429) Update generated code for beta
  * Add support for `allow_redisplay` on resources `stripe.Card` and `stripe.Source`
  * Add support for `account` on resource classes `stripe.terminal.Reader.Action.CollectPaymentMethod`, `stripe.terminal.Reader.Action.ConfirmPaymentIntent`, `stripe.terminal.Reader.Action.ProcessPaymentIntent`, and `stripe.terminal.Reader.Action.RefundPayment`
  * Remove support for `amount_refunded` on resource `stripe.PaymentRecord`
  * Add support for `am_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `ao_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `ba_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `bb_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `bs_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `cd_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `gn_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `kh_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `me_pib` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `mk_vat` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `mr_nif` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `np_pan` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `sn_ninea` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `sr_fin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `tj_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `ug_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `zm_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `zw_tin` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Add support for `network_fallback` on enum `stripe.issuing.Authorization.RequestHistory.reason`

## 11.4.0b2 - 2024-12-05
* [#1426](https://github.com/stripe/stripe-python/pull/1426) Update generated code for beta
  * Add support for `automatic_indirect_tax` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `disabled_reason` on resource classes `stripe.Invoice.AutomaticTax`, `stripe.QuotePreviewInvoice.AutomaticTax`, `stripe.QuotePreviewSubscriptionSchedule.DefaultSettings.AutomaticTax`, `stripe.QuotePreviewSubscriptionSchedule.Phase.AutomaticTax`, `stripe.Subscription.AutomaticTax`, `stripe.SubscriptionSchedule.DefaultSettings.AutomaticTax`, and `stripe.SubscriptionSchedule.Phase.AutomaticTax`
  * Add support for `reference_prefix` on parameter classes `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsBacsDebitMandateOptions`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsBacsDebitMandateOptions`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions` and resource classes `stripe.Order.Payment.Settings.PaymentMethodOptions.SepaDebit.MandateOptions`, `stripe.PaymentIntent.PaymentMethodOptions.BacsDebit.MandateOptions`, `stripe.PaymentIntent.PaymentMethodOptions.SepaDebit.MandateOptions`, `stripe.SetupIntent.PaymentMethodOptions.BacsDebit.MandateOptions`, `stripe.SetupIntent.PaymentMethodOptions.SepaDebit.MandateOptions`, `stripe.checkout.Session.PaymentMethodOptions.BacsDebit.MandateOptions`, and `stripe.checkout.Session.PaymentMethodOptions.SepaDebit.MandateOptions`
  * Add support for `trial_period_days` on parameter class `stripe.PaymentLink.ModifyParamsSubscriptionData`
  * Add support for `payout_minimum_balance_hold` on enum `stripe.BalanceTransaction.type`
  * Add support for `payout_minimum_balance_release` on enum `stripe.BalanceTransaction.type`

## 11.4.0b1 - 2024-11-21
* [#1425](https://github.com/stripe/stripe-python/pull/1425) Update generated code for beta
  * Add support for `network_advice_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
  * Add support for `network_decline_code` on resource classes `stripe.Charge.Outcome`, `stripe.Invoice.LastFinalizationError`, `stripe.PaymentIntent.LastPaymentError`, `stripe.QuotePreviewInvoice.LastFinalizationError`, `stripe.SetupAttempt.SetupError`, and `stripe.SetupIntent.LastSetupError`
  * Add support for `funding` on resource classes `stripe.Charge.PaymentMethodDetails.AmazonPay` and `stripe.Charge.PaymentMethodDetails.RevolutPay`
  * Add support for `amount_requested` on resource class `stripe.Charge.PaymentMethodDetails.Card`
  * Add support for `partial_authorization` on resource class `stripe.Charge.PaymentMethodDetails.Card`
  * Add support for `adjustable_quantity` on resource `stripe.LineItem`
  * Add support for `display` on resource `stripe.LineItem`
  * Add support for `metadata` on resource `stripe.LineItem` and parameter class `stripe.checkout.Session.CreateParamsLineItem`
  * Add support for `request_partial_authorization` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard` and resource class `stripe.PaymentIntent.PaymentMethodOptions.Card`
  * Add support for `payment_method_options` on parameter class `stripe.PaymentIntent.IncrementAuthorizationParams`
  * Add support for `line_items` on parameter classes `stripe.checkout.Session.CreateParamsPermissionsUpdate` and `stripe.checkout.Session.ModifyParams` and resource class `stripe.checkout.Session.Permissions.Update`
  * Change type of `schedule_at_period_end` on  `stripe.billing_portal.Configuration.Features.SubscriptionUpdate` from `Optional[ScheduleAtPeriodEnd]` to `ScheduleAtPeriodEnd`
  * Add support for `invoice.overpaid` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`

## 11.3.0b3 - 2024-11-14
This release changes the pinned API version to `2024-11-20.acacia`.

* [#1422](https://github.com/stripe/stripe-python/pull/1422) Update generated code for beta
  * Add support for `account_holder_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin`
  * Add support for `bank_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin`
  * Add support for `account_holder_name` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei` and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei`
  * Add support for `subscribe` on enum `stripe.PaymentLink.ModifyParams.submit_type`

## 11.3.0b2 - 2024-11-07
* [#1421](https://github.com/stripe/stripe-python/pull/1421) Update generated code for beta
  * Add support for `card_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardFeatures`
  * Add support for `card_spend_dispute_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardFeatures`
  * Add support for `cardholder_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardFeatures`
  * Add support for `spend_control_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardFeatures`
  * Add support for `disable_stripe_user_authentication` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardsListFeatures`
  * Add support for `account_holder_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Aba`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Swift`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Aba`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Swift`
  * Add support for `account_holder_name` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Aba`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Swift`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Aba`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Swift`
  * Add support for `account_type` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Aba`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Swift`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Aba`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Swift`
  * Add support for `bank_address` on resource classes `stripe.FundingInstructions.BankTransfer.FinancialAddress.Aba`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Swift`, `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Aba`, and `stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Swift`
  * Add support for `payment_record` on parameter class `stripe.Invoice.AttachPaymentParams` and resource class `stripe.InvoicePayment.Payment`
  * Add support for `amount_overpaid` on resources `stripe.Invoice` and `stripe.QuotePreviewInvoice`
  * Add support for resource `stripe.PaymentAttemptRecord`
  * Add support for `submit_type` on parameter class `stripe.PaymentLink.ModifyParams`
  * Add support for resource `stripe.PaymentRecord`
  * Add support for `adaptive_pricing` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
  * Add support for `mandate_options` on parameter classes `stripe.checkout.Session.CreateParamsPaymentMethodOptionsBacsDebit` and `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSepaDebit` and resource classes `stripe.checkout.Session.PaymentMethodOptions.BacsDebit` and `stripe.checkout.Session.PaymentMethodOptions.SepaDebit`
  * Add support for `request_decremental_authorization` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `request_extended_authorization` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `request_incremental_authorization` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `request_multicapture` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `request_overcapture` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard` and resource class `stripe.checkout.Session.PaymentMethodOptions.Card`
  * Add support for `capture_method` on parameter classes `stripe.checkout.Session.CreateParamsPaymentMethodOptionsKakaoPay`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsKrCard`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsNaverPay`, `stripe.checkout.Session.CreateParamsPaymentMethodOptionsPayco`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSamsungPay`
  * Add support for `merchant_amount` on parameter class `stripe.issuing.Authorization.CreateParams`
  * Add support for `merchant_currency` on parameter class `stripe.issuing.Authorization.CreateParams`
  * Add support for resource `stripe.issuing.FraudLiabilityDebit`
  * Remove support for `money_movement` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
  * Remove support for `out_of_band_payment` on parameter class `stripe.Invoice.AttachPaymentParams` and resource class `stripe.InvoicePayment.Payment`
  * Change type of `disabled_reason` on  `stripe.Account.FutureRequirements` and `stripe.Account.Requirements` from `str` to `Literal['action_required.requested_capabilities', 'listed', 'other', 'platform_paused', 'rejected.fraud', 'rejected.incomplete_verification', 'rejected.listed', 'rejected.other', 'rejected.platform_fraud', 'rejected.platform_other', 'rejected.platform_terms_of_service', 'rejected.terms_of_service', 'requirements.past_due', 'requirements.pending_verification', 'under_review']`
  * Change type of `disable_stripe_user_authentication` on  `stripe.AccountSession.Components.AccountManagement.Features`, `stripe.AccountSession.Components.AccountOnboarding.Features`, `stripe.AccountSession.Components.Balances.Features`, `stripe.AccountSession.Components.NotificationBanner.Features`, and `stripe.AccountSession.Components.Payouts.Features` from `Optional[bool]` to `bool`
  * Add support for `li_vat` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `invoice.payment_attempt_required` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_fraud_liability_debit.created` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `custom` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `service_tax` on enums `stripe.Invoice.AddLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.Invoice.UpdateLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`, `stripe.tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.CalculationLineItem.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.TaxRate.tax_type`, `stripe.TaxRate.CreateParams.tax_type`, and `stripe.TaxRate.ModifyParams.tax_type`
  * Add support for `payment_record` on enum `stripe.InvoicePayment.Payment.type`
  * Add support for `link` on enums `stripe.PaymentIntent.PaymentMethodOptions.Card.network`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.PaymentMethodOptions.Card.network`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsCard.network`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsCard.network`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.Card.network`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsCard.network`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsCard.network`
  * Change type of `amount` on  `stripe.issuing.Authorization.CreateParams` from `int` to `NotRequired[int]`
  * Change type of `origin_payment_method` on  `stripe.treasury.InboundTransfer` from `str` to `Optional[str]`

## 11.3.0b1 - 2024-10-29
This release changes the pinned API version to `2024-10-28.acacia`.

* [#1417](https://github.com/stripe/stripe-python/pull/1417) Update generated code for beta
  * Add support for `id_bank_transfer_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `bank_bca_onboarding` on parameter class `stripe.Account.CreateParamsSettings` and resource class `stripe.Account.Settings`
  * Add support for `send_money` on parameter class `stripe.AccountSession.CreateParamsComponentsRecipientsFeatures`
  * Add support for `id_bank_transfer` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.Invoice.PaymentSettings.PaymentMethodOptions`, `stripe.PaymentIntent.PaymentMethodOptions`, `stripe.QuotePreviewInvoice.PaymentSettings.PaymentMethodOptions`, `stripe.Refund.DestinationDetails`, `stripe.SetupAttempt.PaymentMethodDetails`, and `stripe.Subscription.PaymentSettings.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptions`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptions`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptions`, and `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `_cls_trigger_action` on resource `stripe.PaymentIntent`
  * Add support for `trigger_action` on resource `stripe.PaymentIntent`
  * Add support for `gopay` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `qris` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `shopeepay` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `id_bank_transfer` on enums `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Change type of `enhanced_eligibility_types` on  `stripe.Dispute` from `Optional[List[Literal['visa_compelling_evidence_3']]]` to `List[Literal['visa_compelling_evidence_3']]`
  * Change type of `enhanced_evidence` on  `stripe.Dispute.Evidence` from `Optional[EnhancedEvidence]` to `EnhancedEvidence`
  * Change type of `enhanced_eligibility` on  `stripe.Dispute.EvidenceDetails` from `Optional[EnhancedEligibility]` to `EnhancedEligibility`
  * Remove support for `payout_statement_descriptor_profanity` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 11.2.0b3 - 2024-10-18
* [#1413](https://github.com/stripe/stripe-python/pull/1413) Update generated code for beta
  * Add support for `alma_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `gopay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `kakao_pay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `kr_card_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `naver_pay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `payco_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `qris_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `samsung_pay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `shopeepay_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `treasury_evolve` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `treasury_fifth_third` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `treasury_goldman_sachs` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `alma` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, and `stripe.Refund.DestinationDetails`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `gopay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `qris` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `shopeepay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `amazon_pay` on resource `stripe.PaymentMethodDomain`
  * Add support for `schedule_at_period_end` on parameter classes `stripe.billing_portal.Configuration.CreateParamsFeaturesSubscriptionUpdate` and `stripe.billing_portal.Configuration.ModifyParamsFeaturesSubscriptionUpdate` and resource class `stripe.billing_portal.Configuration.Features.SubscriptionUpdate`
  * Add support for `metadata` on parameter class `stripe.forwarding.Request.CreateParams`
  * Add support for `external_reference` on parameter class `stripe.tax.Form.ListParamsPayee` and resource class `stripe.tax.Form.Payee`
  * Add support for `au_serr` on resource `stripe.tax.Form`
  * Add support for `ca_mrdp` on resource `stripe.tax.Form`
  * Add support for `eu_dac7` on resource `stripe.tax.Form`
  * Add support for `gb_mrdp` on resource `stripe.tax.Form`
  * Add support for `nz_mrdp` on resource `stripe.tax.Form`
  * Add support for `pln` on parameter classes `stripe.terminal.Configuration.CreateParamsTipping` and `stripe.terminal.Configuration.ModifyParamsTipping` and resource class `stripe.terminal.Configuration.Tipping`
  * Add support for `bank` on parameter classes `stripe.treasury.FinancialAccount.CreateParamsFeaturesFinancialAddressesAba`, `stripe.treasury.FinancialAccount.ModifyParamsFeaturesFinancialAddressesAba`, and `stripe.treasury.FinancialAccount.UpdateFeaturesParamsFinancialAddressesAba` and resource class `stripe.treasury.FinancialAccountFeatures.FinancialAddresses.Aba`
  * Change type of `business_profile` on  `stripe.billing_portal.Configuration.CreateParams` from `Configuration.CreateParamsBusinessProfile` to `NotRequired[Configuration.CreateParamsBusinessProfile]`
  * Add support for `alma` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `gopay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `qris` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `shopeepay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, `stripe.PaymentLink.ModifyParams.payment_method_types`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `auto` on enum `stripe.Customer.ModifyParamsTax.validate_location`
  * Add support for `jp_credit_transfer` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `kakao_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `kr_card` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `naver_pay` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `payco` on enums `stripe.Invoice.PaymentSettings.payment_method_types`, `stripe.Invoice.CreateParamsPaymentSettings.payment_method_types`, `stripe.Invoice.ModifyParamsPaymentSettings.payment_method_types`, `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`, `stripe.Subscription.PaymentSettings.payment_method_types`, `stripe.Subscription.CreateParamsPaymentSettings.payment_method_types`, and `stripe.Subscription.ModifyParamsPaymentSettings.payment_method_types`
  * Add support for `au_serr` on enums `stripe.tax.Form.type` and `stripe.tax.Form.ListParams.type`
  * Add support for `ca_mrdp` on enums `stripe.tax.Form.type` and `stripe.tax.Form.ListParams.type`
  * Add support for `eu_dac7` on enums `stripe.tax.Form.type` and `stripe.tax.Form.ListParams.type`
  * Add support for `gb_mrdp` on enums `stripe.tax.Form.type` and `stripe.tax.Form.ListParams.type`
  * Add support for `nz_mrdp` on enums `stripe.tax.Form.type` and `stripe.tax.Form.ListParams.type`
  * Add support for `external_reference` on enums `stripe.tax.Form.Payee.type` and `stripe.tax.Form.ListParamsPayee.type`
  * Remove support for `expired` on enums `stripe.issuing.Authorization.status` and `stripe.issuing.Authorization.ListParams.status`

## 11.2.0b2 - 2024-10-08
* [#1396](https://github.com/stripe/stripe-python/pull/1396) Update generated code for beta
  * Add support for `groups` on parameter class `stripe.Account.CreateParams` and resource `stripe.Account`
  * Add support for `disable_stripe_user_authentication` on resource classes `stripe.AccountSession.Components.AccountManagement.Features`, `stripe.AccountSession.Components.AccountOnboarding.Features`, `stripe.AccountSession.Components.Balances.Features`, `stripe.AccountSession.Components.NotificationBanner.Features`, and `stripe.AccountSession.Components.Payouts.Features` and parameter classes `stripe.AccountSession.CreateParamsComponentsAccountManagementFeatures`, `stripe.AccountSession.CreateParamsComponentsAccountOnboardingFeatures`, `stripe.AccountSession.CreateParamsComponentsBalancesFeatures`, `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`, `stripe.AccountSession.CreateParamsComponentsNotificationBannerFeatures`, and `stripe.AccountSession.CreateParamsComponentsPayoutsFeatures`
  * Add support for `card_spend_dispute_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardsListFeatures`
  * Add support for `spend_control_management` on parameter class `stripe.AccountSession.CreateParamsComponentsIssuingCardsListFeatures`
  * Add support for `kakao_pay` and `kr_card` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.Mandate.PaymentMethodDetails`, `stripe.PaymentIntent.PaymentMethodOptions`, and `stripe.SetupAttempt.PaymentMethodDetails`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `naver_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `payco` and `samsung_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `line_items` on parameter classes `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsPaypal`, `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsPaypal`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsPaypal`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsPaypal`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsPaypal` and resource classes `stripe.Order.Payment.Settings.PaymentMethodOptions.Paypal` and `stripe.PaymentIntent.PaymentMethodOptions.Paypal`
  * Add support for `flat_amount` on resource `stripe.TaxRate` and resource class `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails`
  * Add support for `rate_type` on resource `stripe.TaxRate` and resource class `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails`
  * Add support for `metadata` on resource `stripe.forwarding.Request`
  * Add support for `_cls_submit_card` on resource `stripe.issuing.Card`
  * Add support for `submit_card` on resource `stripe.issuing.Card`
  * Add support for `by`, `cr`, `ec`, `ma`, `md`, `rs`, `ru`, `tz`, and `uz` on resource class `stripe.tax.Registration.CountryOptions` and parameter class `stripe.tax.Registration.CreateParamsCountryOptions`
  * Add support for `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, and `uz_vat` on enums `stripe.checkout.Session.CollectedInformation.TaxId.type`, `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `kakao_pay`, `kr_card`, `naver_pay`, `payco`, and `samsung_pay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `refund.failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `payout_statement_descriptor_profanity` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `retail_delivery_fee` on enums `stripe.Invoice.AddLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.Invoice.UpdateLinesParamsLineTaxAmountTaxRateData.tax_type`, `stripe.InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type`, `stripe.tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Calculation.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.CalculationLineItem.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type`, `stripe.TaxRate.tax_type`, `stripe.TaxRate.CreateParams.tax_type`, and `stripe.TaxRate.ModifyParams.tax_type`
  * Add support for `expired` on enums `stripe.issuing.Authorization.status` and `stripe.issuing.Authorization.ListParams.status`
  * Add support for `state_retail_delivery_fee` on enums `stripe.tax.Registration.CountryOptions.Us.type` and `stripe.tax.Registration.CreateParamsCountryOptionsUs.type`

## 11.2.0b1 - 2024-10-03
This release changes the pinned API version to `2024-09-30.acacia`.

* [#1407](https://github.com/stripe/stripe-python/pull/1407) Updates beta branch with changes in master & update generated code
  * Add support for `reporting_chart` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `total_pretax_credit_amounts` on resource `stripe.QuotePreviewInvoice`
  * Add support for `allow_redisplay` on parameter class `stripe.terminal.Reader.CollectPaymentMethodParamsCollectConfig`
  * Remove support for `from_schedule` on resource class `stripe.Quote.SubscriptionData`
  * Move `raw_request` and related methods from `_raw_request` module to the `StripeClient` class
  * Remove `_preview` module; use raw request methods in the `StripeClient` class instead

## 10.13.0b1 - 2024-09-18
* [#1395](https://github.com/stripe/stripe-python/pull/1395) Update generated code for beta
  * Add support for `send_money` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
  * Add support for `transfer_balance` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
  * Add support for `automatically_finalizes_at` on resource `stripe.QuotePreviewInvoice`
  * Remove support for resource `stripe.QuotePhase`
  * Add support for `rechnung` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
  * Add support for `terminal_reader_invalid_location_for_activation` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 10.12.0b1 - 2024-09-13
* [#1389](https://github.com/stripe/stripe-python/pull/1389) Update generated code for beta
  * Add support for `template` on resource class `stripe.QuotePreviewInvoice.Rendering`
  * Add support for resource `stripe.issuing.DisputeSettlementDetail`
  * Add support for resource `stripe.issuing.Settlement`
  * Add support for `settlement` on parameter class `stripe.issuing.Transaction.ListParams` and resource `stripe.issuing.Transaction`
  * Remove support for `list` on resource `stripe.QuotePhase`
  * Add support for `rechnung` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
  * Add support for `issuing_dispute_settlement_detail.created` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_dispute_settlement_detail.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_settlement.created` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `issuing_settlement.updated` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`

## 10.11.0b1 - 2024-09-05
* [#1380](https://github.com/stripe/stripe-python/pull/1380) Update generated code for beta
  * Add support for `email` on resource class `stripe.checkout.Session.CollectedInformation`
  * Add support for `phone` on resource class `stripe.checkout.Session.CollectedInformation`
  * Add support for `regulatory_reporting_file` on parameter classes `stripe.issuing.CreditUnderwritingRecord.CorrectParams`, `stripe.issuing.CreditUnderwritingRecord.CreateFromProactiveReviewParams`, and `stripe.issuing.CreditUnderwritingRecord.ReportDecisionParams` and resource `stripe.issuing.CreditUnderwritingRecord`
  * Add support for resource `stripe.terminal.ReaderCollectedData`
  * Remove support for `rechnung` on parameter class `stripe.PaymentMethod.ModifyParams`
  * Add support for `mb_way` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
  * Add support for `terminal_reader_collected_data_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
* [#1387](https://github.com/stripe/stripe-python/pull/1387) Update generated code for beta
  * Add support for `recipients` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for resource `stripe.billing.MeterErrorReport`
  * Add support for `business_name` on resource class `stripe.checkout.Session.CollectedInformation`
  * Add support for `tax_ids` on resource class `stripe.checkout.Session.CollectedInformation`
  * Add support for `billing.meter_error_report.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `mb_way` on enums `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`

## 10.9.0b2 - 2024-08-22
* [#1377](https://github.com/stripe/stripe-python/pull/1377) Update generated code for beta
  * Add support for `mb_way_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `mb_way` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Remove support for `phases` on parameter classes `stripe.Quote.CreateParams` and `stripe.Quote.ModifyParams`
  * Remove support for `from_schedule` on parameter class `stripe.Quote.CreateParamsSubscriptionData`
  * Add support for `mb_way` on enums `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `hr_oib` on enums `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`
  * Remove support for `accepted` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
  * Remove support for `partner_rejected` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
  * Remove support for `submitted` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`

## 10.9.0b1 - 2024-08-15
* [#1375](https://github.com/stripe/stripe-python/pull/1375) Update generated code for beta
  * Add support for `capital_financing` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `permissions` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
  * Add support for `collected_information` on parameter class `stripe.checkout.Session.ModifyParams` and resource `stripe.checkout.Session`
  * Add support for `shipping_options` on parameter class `stripe.checkout.Session.ModifyParams`

## 10.8.0b1 - 2024-08-12
* ⚠️ [#1372](https://github.com/stripe/stripe-python/pull/1372) Update generated code for beta
  * Add support for `capital_financing` on resource class `stripe.AccountSession.Components`
  * Add support for `payto` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
  * ⚠️  Remove support for `risk_correlation_id` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsRechnung`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsRechnung`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsRechnung` and resource class `stripe.PaymentIntent.PaymentMethodOptions.Rechnung`
  * Add support for `custom` on enums `stripe.checkout.Session.ui_mode` and `stripe.checkout.Session.CreateParams.ui_mode`
  * Add support for `payto` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.PaymentLink.payment_method_types`, `stripe.PaymentLink.CreateParams.payment_method_types`, and `stripe.PaymentLink.ModifyParams.payment_method_types`
  * Add support for `invalid_mandate_reference_prefix_format` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 10.7.0b1 - 2024-08-01
* [#1370](https://github.com/stripe/stripe-python/pull/1370) Update generated code for beta
  * Add support for `app_install` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `app_viewport` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `_cls_attach_payment` on resource `stripe.Invoice`
  * Add support for `attach_payment` on resource `stripe.Invoice`
  * Add support for `lines_invalid` on resource class `stripe.Quote.StatusDetails.Stale.LastReason`
  * Add support for `last_price_migration_error` on resources `stripe.QuotePreviewSubscriptionSchedule`, `stripe.Subscription`, and `stripe.SubscriptionSchedule`
  * Remove support for `partner_rejected_details` on resource class `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3`
  * Add support for `customer.subscription.price_migration_failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `subscription_schedule.price_migration_failed` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `lines_invalid` on enum `stripe.Quote.StatusDetails.Stale.LastReason.type`
  * Add support for `charge_exceeds_transaction_limit` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 10.6.0b1 - 2024-07-25
* [#1361](https://github.com/stripe/stripe-python/pull/1361) Update generated code for beta
  * Add support for `capital` on parameter class `stripe.Account.CreateParamsSettings` and resource class `stripe.Account.Settings`
  * Add support for `payment` on resource `stripe.InvoicePayment`
  * Add support for `async_workflows` on parameter classes `stripe.PaymentIntent.CaptureParams`, `stripe.PaymentIntent.ConfirmParams`, `stripe.PaymentIntent.CreateParams`, `stripe.PaymentIntent.DecrementAuthorizationParams`, `stripe.PaymentIntent.IncrementAuthorizationParams`, and `stripe.PaymentIntent.ModifyParams` and resource `stripe.PaymentIntent`
  * Add support for `payto` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for resource `stripe.billing.Alert`
  * Add support for resource `stripe.tax.Association`
  * Add support for `display_name` on parameter classes `stripe.treasury.FinancialAccount.CreateParams` and `stripe.treasury.FinancialAccount.ModifyParams` and resource `stripe.treasury.FinancialAccount`
  * Remove support for `charge` on resource `stripe.InvoicePayment`
  * Remove support for `payment_intent` on resource `stripe.InvoicePayment`
  * Add support for `issuing.account_closed_for_not_providing_business_model_clarification` on enum `stripe.AccountNotice.reason`
  * Add support for `issuing.account_closed_for_not_providing_url_clarification` on enum `stripe.AccountNotice.reason`
  * Add support for `issuing.account_closed_for_not_providing_use_case_clarification` on enum `stripe.AccountNotice.reason`
  * Add support for `billing.alert.triggered` on enums `stripe.Event.type`, `stripe.WebhookEndpoint.CreateParams.enabled_events`, and `stripe.WebhookEndpoint.ModifyParams.enabled_events`
  * Add support for `multibanco` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`

## 10.4.0b1 - 2024-07-11
* [#1356](https://github.com/stripe/stripe-python/pull/1356) Update generated code for beta
  * Change type of `payment_element` on  `stripe.CustomerSession.Components` from `Optional[PaymentElement]` to `PaymentElement`
  * Add support for `not_qualified` on enum `stripe.Dispute.EvidenceDetails.EnhancedEligibility.VisaCompellingEvidence3.status`
  * Remove support for `billing_policy_remote_function_response_invalid` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
  * Remove support for `billing_policy_remote_function_timeout` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
  * Remove support for `billing_policy_remote_function_unexpected_status_code` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
  * Remove support for `billing_policy_remote_function_unreachable` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`
  * Remove support for `payment_intent_fx_quote_invalid` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 10.3.0b1 - 2024-07-05
* ⚠️ [#1355](https://github.com/stripe/stripe-python/pull/1355) Update generated code for beta
  * ⚠️ Remove support for `payment_method_update` on resource class `stripe.CustomerSession.Components.PaymentElement.Features` and parameter class `stripe.CustomerSession.CreateParamsComponentsPaymentElementFeatures`. Users are expected to completely migrate from using payment_method_update.
  * Add support for `payment_method_allow_redisplay_filters`, `payment_method_redisplay`, `payment_method_save_usage` on resource class `stripe.CustomerSession.Components.PaymentElement.Features` and parameter class `stripe.CustomerSession.CreateParamsComponentsPaymentElementFeatures`
  * Add support for `institution` on parameter classes `stripe.Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.Subscription.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, `stripe.Subscription.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters`, and `stripe.financial_connections.Session.CreateParamsFilters` and resource classes `stripe.Invoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, `stripe.PaymentIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, `stripe.QuotePreviewInvoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, `stripe.SetupIntent.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, `stripe.Subscription.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, `stripe.checkout.Session.PaymentMethodOptions.UsBankAccount.FinancialConnections.Filters`, and `stripe.financial_connections.Session.Filters`
  * Add support for resource `stripe.financial_connections.Institution`
  * Add support for `balance` on enums `stripe.financial_connections.Account.subscriptions`, `stripe.financial_connections.Account.SubscribeParams.features`, and `stripe.financial_connections.Account.UnsubscribeParams.features`
  * Add support for `financial_connections_institution_unavailable` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `payment_intent_fx_quote_invalid` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 10.2.0b1 - 2024-06-27
This release changes the pinned API version to `2024-06-20`.

* [#1349](https://github.com/stripe/stripe-python/pull/1349) Update generated code for beta
  * Add support for `filters` on resource class `stripe.QuotePreviewInvoice.PaymentSettings.PaymentMethodOptions.UsBankAccount.FinancialConnections`
  * Remove support for `payment_method_set_as_default` on resource class `stripe.CustomerSession.Components.PaymentElement.Features` and parameter class `stripe.CustomerSession.CreateParamsComponentsPaymentElementFeatures`
  * Add support for `ch_uid` on enums `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`

## 9.12.0b1 - 2024-06-13
* [#1343](https://github.com/stripe/stripe-python/pull/1343) Update generated code for beta
  * Add support for `de_stn` on enums `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, and `stripe.QuotePreviewInvoice.CustomerTaxId.type`

## 9.11.0b1 - 2024-06-06
* [#1339](https://github.com/stripe/stripe-python/pull/1339) Update generated code for beta
  * Add support for `twint` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.PaymentIntent.PaymentMethodOptions`
  * Add support for `swish` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`

## 9.10.0b1 - 2024-05-30
* [#1334](https://github.com/stripe/stripe-python/pull/1334) Update generated code for beta
  * Add support for `en-RO` on enums `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsKlarna.preferred_locale` and `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna.preferred_locale`
  * Add support for `ro-RO` on enums `stripe.Order.CreateParamsPaymentSettingsPaymentMethodOptionsKlarna.preferred_locale` and `stripe.Order.ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna.preferred_locale`

## 9.9.0b1 - 2024-05-23
* [#1331](https://github.com/stripe/stripe-python/pull/1331) Update generated code for beta
  * Change type of `refund` on  `stripe.CreditNote.CreateParamsRefund`, `stripe.CreditNote.PreviewParamsRefund`, and `stripe.CreditNote.PreviewLinesParamsRefund` from `str` to `NotRequired[str]`
  * Add support for `terminal_reader_invalid_location_for_payment` on enum `stripe.QuotePreviewInvoice.LastFinalizationError.code`

## 9.8.0b1 - 2024-05-16
* [#1330](https://github.com/stripe/stripe-python/pull/1330) (beta) swap from `black` to `ruff` for formatting
* [#1327](https://github.com/stripe/stripe-python/pull/1327) Update generated code for beta

## 9.7.0b1 - 2024-05-09
* [#1321](https://github.com/stripe/stripe-python/pull/1321) Update generated code for beta
  * No new beta features. Merging changes from the main branch.

## 9.6.0b1 - 2024-05-02
* [#1318](https://github.com/stripe/stripe-python/pull/1318) Update generated code for beta
  * Add support for `rechnung_payments` on resource class `stripe.Account.Capabilities` and parameter class `stripe.Account.CreateParamsCapabilities`
  * Add support for `rechnung` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, and `stripe.PaymentIntent.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`, and resource `stripe.PaymentMethod`
  * Add support for `multibanco` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
  * Add support for `multibanco` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
  * Add support for `rechnung` on enums `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Change type of `transactions` on  `stripe.gift_cards.Card` from `ListObject[Transaction]` to `Optional[ListObject[Transaction]]`

## 9.5.0b1 - 2024-04-25
* [#1308](https://github.com/stripe/stripe-python/pull/1308) Update generated code for beta
  * Add support for `payment_method_settings` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `cancel_subscription_schedule` on parameter classes `stripe.Quote.CreateParamsLine` and `stripe.Quote.ModifyParamsLine` and resource `stripe.QuoteLine`
  * Add support for `amazon_pay` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`
  * Add support for `revolut_pay` on enum `stripe.QuotePreviewInvoice.PaymentSettings.payment_method_types`

## 9.4.0b1 - 2024-04-18
* [#1302](https://github.com/stripe/stripe-python/pull/1302) Update generated code for beta
  * Add support for `balances` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `payouts_list` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `capital_overview` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `tax_registrations` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `tax_settings` on parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `external_account_collection` on parameter class `stripe.AccountSession.CreateParamsComponentsFinancialAccountFeatures`
  * Add support for `allow_redisplay` on parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.Customer.ListPaymentMethodsParams`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethod.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData`
  * Add support for `subscription_trial_from_plan` on parameter classes `stripe.Invoice.UpcomingLinesParams` and `stripe.Invoice.UpcomingParams`
  * Add support for `swish` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `payment_method_data` on parameter class `stripe.checkout.Session.CreateParams`
  * Add support for `saved_payment_method_options` on parameter class `stripe.checkout.Session.CreateParams` and resource `stripe.checkout.Session`
  * Add support for `mobilepay` on parameter class `stripe.checkout.Session.CreateParamsPaymentMethodOptions` and resource class `stripe.checkout.Session.PaymentMethodOptions`
  * Remove support for `config` on parameter class `stripe.forwarding.Request.CreateParams` and resource `stripe.forwarding.Request`
  * Change type of fields `stripe.AccountSession.Components.PaymentDetails.Features` and `stripe.AccountSession.Components.Payments.Features` from `Optional[bool]` to `bool` of `destination_on_behalf_of_charge_management`
  * Change type of field `stripe.billing.MeterEvent.CreateParams` from `int` to `NotRequired[int]` of `timestamp`
  * Add support for `mobilepay` on enum `stripe.checkout.Session.CreateParams.payment_method_types`
  * Add support for `other` on enums `stripe.issuing.Authorization.CaptureParamsPurchaseDetailsFuel.unit`, `stripe.issuing.Transaction.CreateForceCaptureParamsPurchaseDetailsFuel.unit`, and `stripe.issuing.Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel.unit`

## 9.2.0b1 - 2024-04-11
This release changes the pinned API version to `2024-04-10`.

* [#1296](https://github.com/stripe/stripe-python/pull/1296) Update generated code for beta
  * Add support for `external_account_collection` on resource class `stripe.AccountSession.Components.AccountOnboarding.Features` and parameter class `stripe.AccountSession.CreateParamsComponentsAccountOnboardingFeatures`
  * Add support for `account_management` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `notification_banner` on resource class `stripe.AccountSession.Components` and parameter class `stripe.AccountSession.CreateParamsComponents`
  * Add support for `amazon_pay` on resource classes `stripe.Charge.PaymentMethodDetails`, `stripe.ConfirmationToken.PaymentMethodPreview`, `stripe.PaymentIntent.PaymentMethodOptions`, `stripe.Refund.DestinationDetails`, `stripe.SetupIntent.PaymentMethodOptions`, and `stripe.checkout.Session.PaymentMethodOptions`, parameter classes `stripe.ConfirmationToken.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptions`, `stripe.PaymentIntent.CreateParamsPaymentMethodData`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptions`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData`, `stripe.PaymentIntent.ModifyParamsPaymentMethodOptions`, `stripe.PaymentMethod.CreateParams`, `stripe.PaymentMethodConfiguration.CreateParams`, `stripe.PaymentMethodConfiguration.ModifyParams`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData`, `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodData`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, `stripe.SetupIntent.ModifyParamsPaymentMethodData`, `stripe.SetupIntent.ModifyParamsPaymentMethodOptions`, and `stripe.checkout.Session.CreateParamsPaymentMethodOptions`, and resources `stripe.PaymentMethod` and `stripe.PaymentMethodConfiguration`
  * Add support for `capture_method` on parameter classes `stripe.PaymentIntent.ConfirmParamsPaymentMethodOptionsRevolutPay`, `stripe.PaymentIntent.CreateParamsPaymentMethodOptionsRevolutPay`, and `stripe.PaymentIntent.ModifyParamsPaymentMethodOptionsRevolutPay` and resource class `stripe.PaymentIntent.PaymentMethodOptions.RevolutPay`
  * Change type of field `stripe.billing.MeterEventAdjustment` from `Cancel` to `Optional[Cancel]` of `cancel`
  * Change type of field `stripe.billing.MeterEventAdjustment.Cancel` from `str` to `Optional[str]` of `identifier`
  * Change type of field `stripe.billing.MeterEventAdjustment.CreateParamsCancel` from `str` to `NotRequired[str]` of `identifier`
  * Change type of field `stripe.billing.MeterEventAdjustment.CreateParams` from `MeterEventAdjustment.CreateParamsCancel` to `NotRequired[MeterEventAdjustment.CreateParamsCancel]` of `cancel`
  * Change type of field `stripe.billing.MeterEventAdjustment.CreateParams` from `NotRequired[Literal['cancel']]` to `Literal['cancel']` of `type`
  * Add support for `bh_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `kz_bin` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `ng_tin` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `om_vat` on enums `stripe.checkout.Session.CustomerDetails.TaxId.type`, `stripe.Customer.CreateParamsTaxIdDatum.type`, `stripe.Customer.CreateTaxIdParams.type`, `stripe.Invoice.CustomerTaxId.type`, `stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type`, `stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type`, `stripe.Order.TaxDetails.TaxId.type`, `stripe.Order.CreateParamsTaxDetailsTaxId.type`, `stripe.Order.ModifyParamsTaxDetailsTaxId.type`, `stripe.QuotePreviewInvoice.CustomerTaxId.type`, `stripe.tax.Calculation.CustomerDetails.TaxId.type`, `stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type`, `stripe.tax.Transaction.CustomerDetails.TaxId.type`, `stripe.TaxId.type`, and `stripe.TaxId.CreateParams.type`
  * Add support for `amazon_pay` on enums `stripe.checkout.Session.CreateParams.payment_method_types`, `stripe.ConfirmationToken.PaymentMethodPreview.type`, `stripe.ConfirmationToken.CreateParamsPaymentMethodData.type`, `stripe.Customer.ListPaymentMethodsParams.type`, `stripe.PaymentIntent.ConfirmParamsPaymentMethodData.type`, `stripe.PaymentIntent.CreateParamsPaymentMethodData.type`, `stripe.PaymentIntent.ModifyParamsPaymentMethodData.type`, `stripe.PaymentMethod.type`, `stripe.PaymentMethod.CreateParams.type`, `stripe.PaymentMethod.ListParams.type`, `stripe.SetupIntent.ConfirmParamsPaymentMethodData.type`, `stripe.SetupIntent.CreateParamsPaymentMethodData.type`, and `stripe.SetupIntent.ModifyParamsPaymentMethodData.type`
  * Add support for `billing_policy_remote_function_response_invalid` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_timeout` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_unexpected_status_code` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`
  * Add support for `billing_policy_remote_function_unreachable` on enums `stripe.Invoice.LastFinalizationError.code`, `stripe.PaymentIntent.LastPaymentError.code`, `stripe.QuotePreviewInvoice.LastFinalizationError.code`, `stripe.SetupAttempt.SetupError.code`, and `stripe.SetupIntent.LastSetupError.code`

## 8.11.0b1 - 2024-04-04
* [#1293](https://github.com/stripe/stripe-python/pull/1293) Update generated code for beta
  * Add support for `risk_controls` on parameter class `stripe.Account.CreateParams` and resource `stripe.Account`
  * Add support for `promotion_code` on parameter classes `stripe.Invoice.AddLinesParamsLineDiscount`, `stripe.Invoice.CreateParamsDiscount`, `stripe.Invoice.ModifyParamsDiscount`, `stripe.Invoice.UpdateLinesParamsLineDiscount`, `stripe.InvoiceItem.CreateParamsDiscount`, `stripe.InvoiceItem.ModifyParamsDiscount`, `stripe.InvoiceLineItem.ModifyParamsDiscount`, `stripe.Quote.CreateParamsDiscount`, `stripe.Quote.CreateParamsLineActionAddDiscount`, `stripe.Quote.CreateParamsLineItemDiscount`, `stripe.Quote.CreateParamsPhaseLineItemDiscount`, `stripe.Quote.ModifyParamsDiscount`, `stripe.Quote.ModifyParamsLineActionAddDiscount`, `stripe.Quote.ModifyParamsLineItemDiscount`, and `stripe.Quote.ModifyParamsPhaseLineItemDiscount`
  * Add support for `zip` on parameter classes `stripe.PaymentMethodConfiguration.CreateParams` and `stripe.PaymentMethodConfiguration.ModifyParams` and resource `stripe.PaymentMethodConfiguration`
  * Add support for `offline` on resource class `stripe.SetupAttempt.PaymentMethodDetails.CardPresent`
  * Add support for `card_present` on parameter classes `stripe.SetupIntent.ConfirmParamsPaymentMethodOptions`, `stripe.SetupIntent.CreateParamsPaymentMethodOptions`, and `stripe.SetupIntent.ModifyParamsPaymentMethodOptions` and resource class `stripe.SetupIntent.PaymentMethodOptions`
  * Add support for `modify` on resource `stripe.entitlements.Feature`
  * Add support for `email` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
  * Add support for `phone` on resource `stripe.identity.VerificationReport`, parameter classes `stripe.identity.VerificationSession.CreateParamsOptions` and `stripe.identity.VerificationSession.ModifyParamsOptions`, and resource classes `stripe.identity.VerificationSession.Options` and `stripe.identity.VerificationSession.VerifiedOutputs`
  * Add support for `verification_flow` on resources `stripe.identity.VerificationReport` and `stripe.identity.VerificationSession` and parameter class `stripe.identity.VerificationSession.CreateParams`
  * Add support for `provided_details` on parameter classes `stripe.identity.VerificationSession.CreateParams` and `stripe.identity.VerificationSession.ModifyParams` and resource `stripe.identity.VerificationSession`
  * Add support for `allowed_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
  * Add support for `blocked_merchant_countries` on parameter classes `stripe.issuing.Card.CreateParamsSpendingControls`, `stripe.issuing.Card.ModifyParamsSpendingControls`, `stripe.issuing.Cardholder.CreateParamsSpendingControls`, and `stripe.issuing.Cardholder.ModifyParamsSpendingControls` and resource classes `stripe.issuing.Card.SpendingControls` and `stripe.issuing.Cardholder.SpendingControls`
  * Change type of field `stripe.checkout.Session.CreateParamsPaymentMethodOptionsSwish` from `Literal['']|str` to `str` of `reference`
  * Add support for `verification_flow` on enums `stripe.identity.VerificationReport.type` and `stripe.identity.VerificationSession.type`
  * Add support for `email_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `email_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `phone_unverified_other` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `phone_verification_declined` on enum `stripe.identity.VerificationSession.LastError.code`
  * Add support for `mobile_phone_reader` on enums `stripe.terminal.Reader.device_type` and `stripe.terminal.Reader.ListParams.device_type`
  * Change type of field `stripe.identity.VerificationSession.CreateParams` from `Literal['document', 'id_number']` to `NotRequired[Literal['document', 'id_number']]` of `type`
  * Change type of fields `stripe.Invoice`, `stripe.InvoiceLineItem`, `stripe.QuotePreviewInvoice`, `stripe.Subscription`, and `stripe.SubscriptionItem` from `Optional[List[ExpandableField[Discount]]]` to `List[ExpandableField[Discount]]` of `discounts`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `data`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `image_url_png`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode` from `Optional[str]` to `str` of `image_url_svg`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str` of `hosted_instructions_url`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[str]` to `str` of `mobile_auth_url`
  * Change type of field `stripe.PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode` from `Optional[QrCode]` to `QrCode` of `qr_code`
  * Change type of fields `stripe.QuoteLine.Action.AddItem`, `stripe.QuoteLine.Action.SetItem`, `stripe.QuotePreviewSubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.QuotePreviewSubscriptionSchedule.Phase.Item`, `stripe.QuotePreviewSubscriptionSchedule.Phase`, `stripe.SubscriptionSchedule.Phase.AddInvoiceItem`, `stripe.SubscriptionSchedule.Phase.Item`, and `stripe.SubscriptionSchedule.Phase` from `Optional[List[Discount]]` to `List[Discount]` of `discounts`

## 8.10.0b1 - 2024-03-28
* [#1283](https://github.com/stripe/stripe-python/pull/1283) Fix unneccessary quotes
* [#1277](https://github.com/stripe/stripe-python/pull/1277) Update generated code for beta
  * Add support for `financial_account_transactions`, `financial_account`, `issuing_card`, and `issuing_cards_list` on `AccountSession.CreateParamsComponents` and `AccountSessionService.CreateParamsComponents`
  * Remove support for `subscription_billing_cycle_anchor`, `subscription_cancel_at_period_end`, `subscription_cancel_at`, `subscription_cancel_now`, `subscription_default_tax_rates`, `subscription_items`, `subscription_prebilling`, `subscription_proration_behavior`, `subscription_proration_date`, `subscription_resume_at`, `subscription_start_date`, and `subscription_trial_end` on `Invoice.CreatePreviewParams` and `InvoiceService.CreatePreviewParams`

## 8.9.0b1 - 2024-03-21
* [#1271](https://github.com/stripe/stripe-python/pull/1271) Support AIOHTTPClient init without running event loop
* [#1272](https://github.com/stripe/stripe-python/pull/1272) Update generated code for beta
  * Add support for new resources `Entitlements.ActiveEntitlementSummary` and `Entitlements.ActiveEntitlement`
  * Add support for `list` method on resource `ActiveEntitlement`

## 8.8.0b1 - 2024-03-14
* [#1266](https://github.com/stripe/stripe-python/pull/1266) Beta: record usage of async interface
* [#1270](https://github.com/stripe/stripe-python/pull/1270) Update generated code for beta
  * Add support for new resources `Billing.MeterEventAdjustment`, `Billing.MeterEvent`, and `Billing.Meter`
  * Add support for `create`, `deactivate`, `list`, `modify`, `reactivate`, and `retrieve` methods on resource `Meter`
  * Add support for `create` method on resources `MeterEventAdjustment` and `MeterEvent`
  * Add support for `create` test helper method on resource `ConfirmationToken`
  * Add support for `add_lines`, `remove_lines`, and `update_lines` methods on resource `Invoice`

## 8.7.0b1 - 2024-03-07
* [#1265](https://github.com/stripe/stripe-python/pull/1265) Update generated code for beta
  * Add support for new value `billing_period_end` on enums `Quote.CreateParamsLineEndsAt.type`, `QuoteLine.EndsAt.type`, and `Quote.ModifyParamsLineEndsAt.type`

## 8.6.0b1 - 2024-02-29
* [#1259](https://github.com/stripe/stripe-python/pull/1259) Add helper to add beta version
* [#1264](https://github.com/stripe/stripe-python/pull/1264) Remove unconditional import of TCPConnector from aiohttp in _http_client
* [#1251](https://github.com/stripe/stripe-python/pull/1251) Update generated code for beta
  * Remove support for resource `Entitlements.Event`

## 8.5.0b3 - 2024-02-27
* [#1262](https://github.com/stripe/stripe-python/pull/1262) Beta: fix ssl for AIOHTTP client

## 8.5.0b2 - 2024-02-27
* **Python async** - In this beta release, async support is now "feature complete". If you notice missing async support for something, it's probably a bug! Usage instructions for the async interface are available in the [README.md](https://github.com/stripe/stripe-python/blob/beta/README.md#async).
  * [#1253](https://github.com/stripe/stripe-python/pull/1253) Beta: Support 'allow_sync_methods=False' in HTTPXClient
  * [#1254](https://github.com/stripe/stripe-python/pull/1254) Beta: add AIOHTTP http client
  * [#1247](https://github.com/stripe/stripe-python/pull/1247) Make `ListObject.auto_paging_iter()` implement `AsyncIterator`

## 8.5.0b1 - 2024-02-22
* ⚠️ [#1239](https://github.com/stripe/stripe-python/pull/1239) Beta: Collapse HTTPClientAsync into HTTPClient
  * ⚠️ Removes the `stripe.default_http_client_async` global and the `stripe.HTTPClientAsync` class.
    * To set your own async-enabled http client, set `stripe.default_http_client` to a subclass of `stripe.HTTPClient` such as `stripe.HTTPXClient` that implements `.request_async`, `.sleep_async`, `.request_stream_async`, and `.close_async`.
    * The default http client of the library is still `RequestsClient` for synchronous methods, that "falls back" to a `HTTPXClient` when asynchronous methods are called.
* [#1246](https://github.com/stripe/stripe-python/pull/1246) Update generated code for beta

## 8.4.0b1 - 2024-02-16
* [#1233](https://github.com/stripe/stripe-python/pull/1233) Beta: async streaming
* [#1236](https://github.com/stripe/stripe-python/pull/1236) Beta: StripeStreamResponseAsync.read helper
* [#1235](https://github.com/stripe/stripe-python/pull/1235) Update generated code for beta
  * Add support for `payto` and `twint` payment methods throughout the API
  * Add support for `decrement_authorization` method on resource `PaymentIntent`

## 8.3.0b1 - 2024-02-08
* [#1228](https://github.com/stripe/stripe-python/pull/1228) Beta: add `_async` methods for StripeClient
* [#1226](https://github.com/stripe/stripe-python/pull/1226) Update generated code for beta
  * Add support for `payment_method_options` on `ConfirmationToken`

## 8.2.0b1 - 2024-02-05
* [#1210](https://github.com/stripe/stripe-python/pull/1210) Beta: better support for trio in HTTPClientAsync
  * Fixes support for `trio` on HttpClientAsync.
* [#1209](https://github.com/stripe/stripe-python/pull/1209) Beta: Fix HTTPXClient retries
* [#1171](https://github.com/stripe/stripe-python/pull/1171) Beta: codegenned async methods on resources
* [#1219](https://github.com/stripe/stripe-python/pull/1219) Beta: more async infrastructure
* [#1218](https://github.com/stripe/stripe-python/pull/1218) Update generated code for beta
  * Add support for new resources `Entitlements.Event` and `Entitlements.Feature`
  * Add support for `create` method on resource `Event`
  * Add support for `create` and `list` methods on resource `Feature`

## 8.1.0b1 - 2024-01-25
* [#1198](https://github.com/stripe/stripe-python/pull/1198) Update generated code for beta
  * Add support for `create_preview` method on resource `Invoice`

## 7.14.0b1 - 2024-01-18
* [#1197](https://github.com/stripe/stripe-python/pull/1197) Update generated code for beta
  Release specs are identical.
* [#1192](https://github.com/stripe/stripe-python/pull/1192) Update generated code for beta
  * Add support for new value `nn` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bank`
  * Add support for new value `NNBANL2G` on enum `ConfirmationToken.PaymentMethodPreview.Ideal.bic`
  * Change `Invoice.AutomaticTax.liability`, `Invoice.issuer`, and `Subscription.AutomaticTax.liability` to be required

## 7.13.0b1 - 2024-01-12
* [#1165](https://github.com/stripe/stripe-python/pull/1165) Beta: raw_request_async with HTTPX
* [#1191](https://github.com/stripe/stripe-python/pull/1191) Beta: report `raw_request` usage
* [#1189](https://github.com/stripe/stripe-python/pull/1189) Update generated code for beta

## 7.12.0b1 - 2024-01-04
* [#1187](https://github.com/stripe/stripe-python/pull/1187) Update generated code for beta
  * Updated stable APIs to the latest version

## 7.11.0b1 - 2023-12-22
* [#1177](https://github.com/stripe/stripe-python/pull/1177) Update generated code for beta

## 7.10.0b1 - 2023-12-14
* [#1164](https://github.com/stripe/stripe-python/pull/1164) Beta: revert broken logger
* [#1166](https://github.com/stripe/stripe-python/pull/1166) Update generated code for beta

## 7.9.0b1 - 2023-12-08
* [#1163](https://github.com/stripe/stripe-python/pull/1163) Update generated code for beta
  * Add support for `retrieve` method on resource `FinancialConnections.Transaction`

## 7.8.0b1 - 2023-11-30
* [#1148](https://github.com/stripe/stripe-python/pull/1148) Update generated code for beta

## 7.7.0b1 - 2023-11-21
* Add support for `components` on parameter class `CustomerSession.CreateParams` and resource `CustomerSession`
* Rename `receipient` to `recipient` beneath `PaymentDetails` on `Charge` and `PaymentIntent` APIs.* Add support for `electronic_commerce_indicator` on resource classes `Charge.PaymentMethodDetails.Card.ThreeDSecure` and `SetupAttempt.PaymentMethodDetails.Card.ThreeDSecure`
* [#1141](https://github.com/stripe/stripe-python/pull/1141) Update generated code for beta

## 7.6.0b1 - 2023-11-16
* [#1128](https://github.com/stripe/stripe-python/pull/1128) Update generated code for beta
  * Add support for `issuing_card` and `issuing_cards_list` on `AccountSession.CreateParamsComponents`
  * Add support for `event_details` and `subscription` on `payment_details` types
  * Add support for `affiliate` and `delivery` on `payment_details.flight`, `payment_details.lodging`, and `payment_details.car_rental` types
  * Add support for `drivers` on `payment_details.car_rental` types
  * Add support for `passengers` on `payment_details.flight` and `payment_details.lodging` types
  * Add support for `created` on `CustomerSession`

## 7.5.0b1 - 2023-11-10
* [#1120](https://github.com/stripe/stripe-python/pull/1120) Update generated code for beta

## 7.4.0b1 - 2023-11-02
* [#1110](https://github.com/stripe/stripe-python/pull/1110) Update generated code for beta
  * Add support for `attach_payment_intent` method on resource `Invoice`

## 7.2.0b1 - 2023-10-26
* [#1107](https://github.com/stripe/stripe-python/pull/1107) Update generated code for beta
  * Add support for new resource `Margin`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `Margin`

## 7.1.0b1 - 2023-10-17
This release changes the pinned API version to `2023-10-16`.

* [#1083](https://github.com/stripe/stripe-python/pull/1083) Update generated code for beta
* [#1084](https://github.com/stripe/stripe-python/pull/1084) Update generated code for beta
  - Update pinned API version to `2023-10-16`

## 6.8.0b3 - 2023-10-13

## 6.8.0b2 - 2023-10-11
* [#1061](https://github.com/stripe/stripe-python/pull/1061) Types: inner resource classes
* [#1073](https://github.com/stripe/stripe-python/pull/1073) Update generated code for beta
  Release specs are identical.

## 6.8.0b1 - 2023-10-05
* [#1059](https://github.com/stripe/stripe-python/pull/1059) Update generated code for beta
  * Rename resources `Issuing.CardDesign` and `Issuing.CardBundle` to `Issuing.PersonalizationDesign` and `Issuing.PhysicalBundle`
* [#1066](https://github.com/stripe/stripe-python/pull/1066) Update generated code for beta
  * Add support for `mark_draft` and `mark_stale` methods on resource `Quote`
  * Remove support for `draft_quote` and `mark_stale_quote` methods on resource `Quote`
  * Rename `preview_invoice_lines` to `list_preview_invoice_lines` on resource `Quote`

## 6.7.0b2 - 2023-09-28
* [#997](https://github.com/stripe/stripe-python/pull/997) Remove developer_message support
* [#1059](https://github.com/stripe/stripe-python/pull/1059) Update generated code for beta
  * Rename resources `Issuing.CardDesign` and `Issuing.CardBundle` to `Issuing.PersonalizationDesign` and `Issuing.PhysicalBundle`

## 6.7.0b1 - 2023-09-21
* [#1053](https://github.com/stripe/stripe-python/pull/1053) Update generated code for beta

## 6.6.0b1 - 2023-09-14
* [#1048](https://github.com/stripe/stripe-python/pull/1048) Update generated code for beta
  * Add support for new resource `ConfirmationToken`
  * Add support for `retrieve` method on resource `ConfirmationToken`
  * Add support for `create` method on resource `Issuing.CardDesign`
  * Add support for `reject_testmode` test helper method on resource `Issuing.CardDesign`

## 6.5.0b1 - 2023-09-07
* [#1045](https://github.com/stripe/stripe-python/pull/1045) Update generated code for beta
  * Release specs are identical.
* [#1034](https://github.com/stripe/stripe-python/pull/1034) Update generated code for beta
  * Remove support for `submit_card` test helper method on resource `Issuing.Card`

## 6.3.0b1 - 2023-08-31
* [#1029](https://github.com/stripe/stripe-python/pull/1029) Update generated code for beta
  * Rename `Quote.preview_invoices` and `Quote.preview_subscription_schedules` to `Quote.list_preview_invoices` and `Quote.list_preview_schedules`.

## 6.1.0b2 - 2023-08-23
This release changes the pinned API version to `2023-08-16`.

* [#1020](https://github.com/stripe/stripe-python/pull/1020) Adds type_annotations, and dependency on `typing_extensions`.
* [#1006](https://github.com/stripe/stripe-python/pull/1006) [#1017](https://github.com/stripe/stripe-python/pull/1017) Update generated code for beta

## 6.1.0b1 - 2023-08-23
  * Updated stable APIs to the latest version

## 5.6.0b3 - 2023-08-03
* [#997](https://github.com/stripe/stripe-python/pull/997) Remove developer_message support
* [#999](https://github.com/stripe/stripe-python/pull/999) Update generated code for beta
* [#1004](https://github.com/stripe/stripe-python/pull/1004) Update generated code for beta
  * Add support for `submit_card` test helper method on resource `Issuing.Card`

## 5.6.0b2 - 2023-07-28
* [#992](https://github.com/stripe/stripe-python/pull/992) Update generated code for beta
* [#995](https://github.com/stripe/stripe-python/pull/995) Update generated code for beta
  * Add support for new resource `Tax.Form`
  * Add support for `list`, `pdf`, and `retrieve` methods on resource `Form`

## 5.6.0b1 - 2023-07-13
* [#986](https://github.com/stripe/stripe-python/pull/986) Consolidate beta SDKs section
* [#985](https://github.com/stripe/stripe-python/pull/985) Update generated code for beta
* [#991](https://github.com/stripe/stripe-python/pull/991) Update generated code for beta
  Release specs are identical.
* [#989](https://github.com/stripe/stripe-python/pull/989) Update generated code for beta
  * Add support for new resource `PaymentMethodConfiguration`
  * Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `PaymentMethodConfiguration`

## 5.5.0b5 - 2023-06-22
* [#976](https://github.com/stripe/stripe-python/pull/976) Update generated code for beta
* [#979](https://github.com/stripe/stripe-python/pull/979) Update generated code for beta
* [#982](https://github.com/stripe/stripe-python/pull/982) Update generated code for beta
  * Add support for new resource `CustomerSession`
  * Add support for `create` method on resource `CustomerSession`

## 5.5.0b4 - 2023-06-02
* [#971](https://github.com/stripe/stripe-python/pull/971) Handle developer message in preview error responses
* [#969](https://github.com/stripe/stripe-python/pull/969) Update generated code for beta
* [#973](https://github.com/stripe/stripe-python/pull/973) Update generated code for beta

## 5.5.0b3 - 2023-05-19
* [#965](https://github.com/stripe/stripe-python/pull/965) Add raw_request
* [#961](https://github.com/stripe/stripe-python/pull/961) Update generated code for beta
* [#964](https://github.com/stripe/stripe-python/pull/964) Update generated code for beta
* [#966](https://github.com/stripe/stripe-python/pull/966) Update generated code for beta
  * Add support for `subscribe` and `unsubscribe` methods on resource `FinancialConnections.Account`

## 5.5.0b2 - 2023-04-13
* [#953](https://github.com/stripe/stripe-python/pull/953) Update generated code for beta
* [#954](https://github.com/stripe/stripe-python/pull/954) Update generated code for beta
  * Add support for `collect_payment_method` and `confirm_payment_intent` methods on resource `Terminal.Reader`

## 5.5.0b1 - 2023-03-30
* [#950](https://github.com/stripe/stripe-python/pull/950) Update generated code for beta

## 5.4.0b1 - 2023-03-23
* [#941](https://github.com/stripe/stripe-python/pull/941) Update generated code for beta (new)
  * Add support for new resources `Tax.CalculationLineItem` and `Tax.TransactionLineItem`
  * Add support for `collect_inputs` method on resource `Terminal.Reader`

## 5.3.0b4 - 2023-03-16
* [#938](https://github.com/stripe/stripe-python/pull/938) Update generated code for beta (new)
  * Remove support for resources `Capital.FinancingOffer` and `Capital.FinancingSummary`
  * Remove support for `list`, `mark_delivered`, and `retrieve` methods on resource `FinancingOffer`
  * Remove support for `retrieve` method on resource `FinancingSummary`
* [#940](https://github.com/stripe/stripe-python/pull/940) Update generated code for beta (new)
  * Add support for `create_from_calculation` method on resource `Tax.Transaction`

## 5.3.0b3 - 2023-03-09
* [#936](https://github.com/stripe/stripe-python/pull/936) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Remove support for `list_transactions` method on resource `Tax.Transaction`

## 5.3.0b2 - 2023-03-03
* [#935](https://github.com/stripe/stripe-python/pull/935) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resources `Issuing.CardBundle` and `Issuing.CardDesign`
  * Add support for `list` and `retrieve` methods on resource `CardBundle`
  * Add support for `list`, `modify`, and `retrieve` methods on resource `CardDesign`

## 5.3.0b1 - 2023-02-23
* [#931](https://github.com/stripe/stripe-python/pull/931) API Updates for beta branch
  * Updated stable APIs to the latest version

## 5.2.0b1 - 2023-02-02
* [#921](https://github.com/stripe/stripe-python/pull/921) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resource `FinancialConnections.Transaction`
  * Add support for `list` method on resource `Transaction`

## 5.1.0b7 - 2023-01-26
* [#917](https://github.com/stripe/stripe-python/pull/917) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `list_transactions` method on resource `Tax.Transaction`

## 5.1.0b6 - 2023-01-19
* [#915](https://github.com/stripe/stripe-python/pull/915) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `Tax.Settings` resource.

## 5.1.0b5 - 2023-01-12
* [#914](https://github.com/stripe/stripe-python/pull/914) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Change `quote.draft_quote` implementation to from calling `POST /v1/quotes/{quote}/draft` to `POST /v1/quotes/{quote}/mark_draft`
  * Add support for `tax.Registration` resource

## 5.1.0b4 - 2023-01-05
* [#912](https://github.com/stripe/stripe-python/pull/912) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for `mark_stale_quote` method on resource `Quote`

## 5.1.0b3 - 2022-12-22
* [#910](https://github.com/stripe/stripe-python/pull/910) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Move `stripe.TaxCalculation` and `stripe.TaxTranscation` to `stripe.tax.Calculation` and `stripe.tax.Transaction`.

## 5.1.0b2 - 2022-12-15
* [#906](https://github.com/stripe/stripe-python/pull/906) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for new resources `QuoteLine`, `TaxCalculation`, and `TaxTransaction`
  * Add support for `create` and `list_line_items` methods on resource `TaxCalculation`
  * Add support for `create_reversal`, `create`, and `retrieve` methods on resource `TaxTransaction`

## 5.1.0b1 - 2022-12-08
This release changes the pinned API version to `2022-11-15`.

* [#898](https://github.com/stripe/stripe-python/pull/898) API Updates for beta branch
  * Updated stable APIs to the latest version
* [#902](https://github.com/stripe/stripe-python/pull/902) API Updates for beta branch
  * Updated stable APIs to the latest version

## 4.3.0b3 - 2022-11-02
* [#885](https://github.com/stripe/stripe-python/pull/885) Update changelog for the Gift Card API
* [#884](https://github.com/stripe/stripe-python/pull/884) API Updates for beta branch
  * Updated stable APIs to the latest version
* [#890](https://github.com/stripe/stripe-python/pull/890) API Updates for beta branch
  * Updated beta APIs to the latest stable version

## 4.3.0b2 - 2022-10-07

## 4.3.0b1 - 2022-09-26
* [#878](https://github.com/stripe/stripe-python/pull/878) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add `FinancingOffer`, `FinancingSummary` and `FinancingTransaction` resources.

## 4.2.0b2 - 2022-08-26
* [#869](https://github.com/stripe/stripe-python/pull/869) API Updates for beta branch
  * Updated stable APIs to the latest version
  * Add support for the beta [Gift Card API](https://stripe.com/docs/gift-cards).

## 4.2.0b1 - 2022-08-23
* [#866](https://github.com/stripe/stripe-python/pull/866) API Updates for beta branch
  - Updated stable APIs to the latest version
  - `Stripe-Version` beta headers are not pinned by-default and need to be manually specified, please refer to [beta SDKs README section](https://github.com/stripe/stripe-dotnet/blob/master/README.md#beta-sdks)

## 4.1.0b2 - 2022-08-11
* [#859](https://github.com/stripe/stripe-python/pull/859) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `refund_payment` method to Terminal resource

## 4.1.0b1 - 2022-08-03
* [#848](https://github.com/stripe/stripe-python/pull/848) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Added the `Order` resource support

## 3.6.0b1 - 2022-07-22
* [#826](https://github.com/stripe/stripe-python/pull/826) Use the generated API version
* [#834](https://github.com/stripe/stripe-python/pull/834) API Updates for beta branch
  - Updated stable APIs to the latest version
* [#837](https://github.com/stripe/stripe-python/pull/837) API Updates for beta branch
  - Include `server_side_confirmation_beta=v1` beta
  - Add `secretKeyConfirmation` to `PaymentIntent`
* [#840](https://github.com/stripe/stripe-python/pull/840) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `SubscriptionSchedule.amend` method.
* [#843](https://github.com/stripe/stripe-python/pull/843) API Updates for beta branch
  - Updated stable APIs to the latest version
  - Add `QuotePhase` resource
