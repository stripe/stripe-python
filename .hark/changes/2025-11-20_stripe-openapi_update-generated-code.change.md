---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1679
is_stripe_api_change: true
released_in_version: 14.1.0a2
---

* Add support for new resources `v2.core.AccountPersonToken`, `v2.core.AccountToken`, and `v2.money_management.CurrencyConversion`
* Add support for `create`, `list`, and `retrieve` methods on resource `v2.money_management.CurrencyConversion`
* Add support for `create` and `retrieve` methods on resources `v2.core.AccountPersonToken` and `v2.core.AccountToken`
* Add support for `effective_at` on `InvoiceCreatePreviewParamsScheduleDetailAmendment`, `InvoiceCreatePreviewParamsScheduleDetailPhase`, `QuoteCreateParamsLine`, `QuoteLine`, `QuoteModifyParamsLine`, `QuotePreviewSubscriptionSchedule.Phase`, `SubscriptionSchedule.Phase`, `SubscriptionScheduleAmendParamsAmendment`, `SubscriptionScheduleCreateParamsPhase`, and `SubscriptionScheduleModifyParamsPhase`
* Add support for `trial_offer` on `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSet`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItem`, `QuoteCreateParamsLineActionAddItem`, `QuoteCreateParamsLineActionSetItem`, `QuoteLine.Action.AddItem`, `QuoteLine.Action.SetItem`, `QuoteModifyParamsLineActionAddItem`, `QuoteModifyParamsLineActionSetItem`, `QuotePreviewSubscriptionSchedule.Phase.Item`, `SubscriptionSchedule.Phase.Item`, `SubscriptionScheduleAmendParamsAmendmentItemActionAdd`, `SubscriptionScheduleAmendParamsAmendmentItemActionSet`, `SubscriptionScheduleCreateParamsPhaseItem`, and `SubscriptionScheduleModifyParamsPhaseItem`
* Change type of `DelegatedCheckout.RequestedSession.amount_subtotal` from `longInteger` to `nullable(longInteger)`
* Change type of `DelegatedCheckout.RequestedSession.amount_total` from `longInteger` to `nullable(longInteger)`
* Add support for `amount_discount`, `amount_subtotal`, `amount_total`, `unit_amount_after_discount`, and `unit_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail`
* Add support for `amount_subtotal_after_discount` on `DelegatedCheckout.RequestedSession.LineItemDetail` and `DelegatedCheckout.RequestedSession.TotalDetail`
* Change type of `InvoiceCreatePreviewParamsScheduleDetail.billing_schedules` from `array(billing_schedules_update_params)` to `emptyable(array(billing_schedules_update_params))`
* Remove support for values `amendment_end`, `line_ends_at`, `schedule_end`, and `upcoming_invoice` from enums `InvoiceCreatePreviewParamsSubscriptionDetailBillingScheduleBillUntil.type`, `Subscription.BillingSchedule.BillUntil.type`, `SubscriptionCreateParamsBillingScheduleBillUntil.type`, `SubscriptionModifyParamsBillingScheduleBillUntil.type`, `SubscriptionScheduleCreateParamsBillingScheduleBillUntil.type`, and `SubscriptionScheduleModifyParamsBillingScheduleBillUntil.type`
* Add support for `current_trial` on `InvoiceCreatePreviewParamsSubscriptionDetailItem`, `SubscriptionCreateParamsItem`, `SubscriptionItemCreateParams`, `SubscriptionItemModifyParams`, `SubscriptionItem`, and `SubscriptionModifyParamsItem`
* Change type of `QuoteCreateParamsSubscriptionDataOverride.billing_schedules` and `QuoteCreateParamsSubscriptionDatum.billing_schedules` from `emptyable(array(billing_schedules_create_specs))` to `array(billing_schedules_create_specs)`
* Add support for new value `line_start` on enums `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
* Remove support for value `phase_start` from enums `QuoteCreateParamsSubscriptionDataOverride.phase_effective_at`, `QuoteCreateParamsSubscriptionDatum.phase_effective_at`, `QuoteModifyParamsSubscriptionDataOverride.phase_effective_at`, and `QuoteModifyParamsSubscriptionDatum.phase_effective_at`
* Change type of `Quote.SubscriptionDataOverride.billing_schedules` and `Quote.SubscriptionDatum.billing_schedules` from `nullable(array(SubscriptionsResourceBillingSchedules))` to `array(QuotesResourceSubscriptionDataBillingSchedules)`
* Change type of `Quote.SubscriptionDataOverride.phase_effective_at` and `Quote.SubscriptionDatum.phase_effective_at` from `nullable(enum('billing_period_start'|'phase_start'))` to `enum('billing_period_start'|'line_start')`
* Change type of `QuotePreviewSubscriptionSchedule.DefaultSetting.phase_effective_at` and `SubscriptionSchedule.DefaultSetting.phase_effective_at` from `nullable(enum('billing_period_start'|'phase_start'))` to `enum('billing_period_start'|'phase_start')`
* Change type of `QuotePreviewSubscriptionSchedule.billing_schedules` and `SubscriptionSchedule.billing_schedules` from `nullable(array(SubscriptionsResourceBillingSchedules))` to `array(SubscriptionsResourceBillingSchedules)`
* Remove support for `amendment_start`, `line_starts_at`, and `relative` on `Subscription.BillingSchedule.BillFrom`
* Change type of `Subscription.BillingSchedule.BillFrom.computed_timestamp` from `nullable(DateTime)` to `DateTime`
* Change type of `Subscription.BillingSchedule.BillFrom.type` from `enum` to `literal('timestamp')`
* Remove support for `amendment_end` and `line_ends_at` on `Subscription.BillingSchedule.BillUntil`
* Change type of `V2.Billing.ServiceAction.CreditGrant.Amount.monetary`, `V2.Billing.ServiceAction.CreditGrantPerTenant.Amount.monetary`, `v2.billing.ServiceActionCreateParamsCreditGrantAmount.monetary`, and `v2.billing.ServiceActionCreateParamsCreditGrantPerTenantAmount.monetary` from `amount` to `an object`
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
* Remove support for `v1_event_id` on `V2.Core.Event`
* Remove support for `amount_details` and `capture_method` on `V2.Payments.OffSessionPayment` and `v2.payments.OffSessionPaymentCreateParams`
* Change type of `V2.Payments.OffSessionPayment.amount_capturable` from `amount` to `an object`
* Change type of `V2.Payments.OffSessionPayment.amount_requested` from `amount` to `an object`
* Change type of `v2.payments.OffSessionPaymentCreateParams.amount` from `amount` to `an object`
* Add support for new value `best_available` on enum `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy`
* Remove support for values `heuristic`, `scheduled`, and `smart` from enum `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy`
* Change `v2.payments.OffSessionPaymentCreateParamsRetryDetail.retry_strategy` to be optional
* Remove support for `destination` on `v2.payments.OffSessionPaymentCaptureParamsTransferDatum`
* Change `v2.payments.OffSessionPaymentCaptureParams.amount_to_capture` to be optional
* Add support for `created` on `v2.core.EventListParams`
* Remove support for `gt`, `gte`, `lt`, and `lte` on `v2.core.EventListParams`
* Add support for `account_token` on `v2.core.AccountCreateParams` and `v2.core.AccountModifyParams`
* Add support for new value `future_requirements` on enums `v2.core.AccountCreateParams.include`, `v2.core.AccountModifyParams.include`, and `v2.core.AccountRetrieveParams.include`
* Add support for `person_token` on `v2.core.AccountPersonCreateParams` and `v2.core.AccountPersonModifyParams`
* Add support for `impacted_requests_percentage` on `EventsV2CoreHealthApiErrorFiringEvent.Impact`, `EventsV2CoreHealthApiErrorResolvedEvent.Impact`, `EventsV2CoreHealthApiLatencyFiringEvent.Impact`, `EventsV2CoreHealthApiLatencyResolvedEvent.Impact`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact`
* Add support for `context` and `related_object` on `EventsV2CoreHealthEventGenerationFailureResolvedEvent.Impact`
* Remove support for `account`, `livemode`, `missing_delivery_attempts`, and `related_object_id` on `EventsV2CoreHealthEventGenerationFailureResolvedEvent.Impact`
* Change type of `EventsV2CoreHealthFraudRateIncreasedEvent.Impact.realized_fraud_amount` from `amount` to `an object`
* Change type of `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.approved_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.approved_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.approved_amount`, and `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.approved_amount` from `amount` to `an object`
* Change type of `EventsV2CoreHealthIssuingAuthorizationRequestErrorsFiringEvent.Impact.declined_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestErrorsResolvedEvent.Impact.declined_amount`, `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutFiringEvent.Impact.declined_amount`, and `EventsV2CoreHealthIssuingAuthorizationRequestTimeoutResolvedEvent.Impact.declined_amount` from `amount` to `an object`
* Add support for thin events `V2PaymentsOffSessionPaymentAttemptFailedEvent` and `V2PaymentsOffSessionPaymentAttemptStartedEvent` with related object `v2.payments.OffSessionPayment`
* Remove support for thin event `V1AccountUpdatedEvent` with related object `Account`
* Remove support for thin events `V1ApplicationFeeCreatedEvent` and `V1ApplicationFeeRefundedEvent` with related object `ApplicationFee`
* Remove support for thin events `V1BillingPortalConfigurationCreatedEvent` and `V1BillingPortalConfigurationUpdatedEvent` with related object `billing_portal.Configuration`
* Remove support for thin event `V1CapabilityUpdatedEvent` with related object `Capability`
* Remove support for thin events `V1ChargeCapturedEvent`, `V1ChargeExpiredEvent`, `V1ChargeFailedEvent`, `V1ChargePendingEvent`, `V1ChargeRefundedEvent`, `V1ChargeSucceededEvent`, and `V1ChargeUpdatedEvent` with related object `Charge`
* Remove support for thin events `V1ChargeDisputeClosedEvent`, `V1ChargeDisputeCreatedEvent`, `V1ChargeDisputeFundsReinstatedEvent`, `V1ChargeDisputeFundsWithdrawnEvent`, and `V1ChargeDisputeUpdatedEvent` with related object `Dispute`
* Remove support for thin events `V1ChargeRefundUpdatedEvent`, `V1RefundCreatedEvent`, `V1RefundFailedEvent`, and `V1RefundUpdatedEvent` with related object `Refund`
* Remove support for thin events `V1CheckoutSessionAsyncPaymentFailedEvent`, `V1CheckoutSessionAsyncPaymentSucceededEvent`, `V1CheckoutSessionCompletedEvent`, and `V1CheckoutSessionExpiredEvent` with related object `checkout.Session`
* Remove support for thin events `V1ClimateOrderCanceledEvent`, `V1ClimateOrderCreatedEvent`, `V1ClimateOrderDelayedEvent`, `V1ClimateOrderDeliveredEvent`, and `V1ClimateOrderProductSubstitutedEvent` with related object `climate.Order`
* Remove support for thin events `V1ClimateProductCreatedEvent` and `V1ClimateProductPricingUpdatedEvent` with related object `climate.Product`
* Remove support for thin events `V1CouponCreatedEvent`, `V1CouponDeletedEvent`, and `V1CouponUpdatedEvent` with related object `Coupon`
* Remove support for thin events `V1CreditNoteCreatedEvent`, `V1CreditNoteUpdatedEvent`, and `V1CreditNoteVoidedEvent` with related object `CreditNote`
* Remove support for thin events `V1CustomerCreatedEvent`, `V1CustomerDeletedEvent`, and `V1CustomerUpdatedEvent` with related object `Customer`
* Remove support for thin events `V1CustomerSubscriptionCreatedEvent`, `V1CustomerSubscriptionDeletedEvent`, `V1CustomerSubscriptionPausedEvent`, `V1CustomerSubscriptionPendingUpdateAppliedEvent`, `V1CustomerSubscriptionPendingUpdateExpiredEvent`, `V1CustomerSubscriptionResumedEvent`, `V1CustomerSubscriptionTrialWillEndEvent`, and `V1CustomerSubscriptionUpdatedEvent` with related object `Subscription`
* Remove support for thin events `V1CustomerTaxIdCreatedEvent`, `V1CustomerTaxIdDeletedEvent`, and `V1CustomerTaxIdUpdatedEvent` with related object `TaxId`
* Remove support for thin event `V1FileCreatedEvent` with related object `File`
* Remove support for thin events `V1FinancialConnectionsAccountCreatedEvent`, `V1FinancialConnectionsAccountDeactivatedEvent`, `V1FinancialConnectionsAccountDisconnectedEvent`, `V1FinancialConnectionsAccountReactivatedEvent`, `V1FinancialConnectionsAccountRefreshedBalanceEvent`, `V1FinancialConnectionsAccountRefreshedOwnershipEvent`, and `V1FinancialConnectionsAccountRefreshedTransactionsEvent` with related object `financial_connections.Account`
* Remove support for thin events `V1IdentityVerificationSessionCanceledEvent`, `V1IdentityVerificationSessionCreatedEvent`, `V1IdentityVerificationSessionProcessingEvent`, `V1IdentityVerificationSessionRedactedEvent`, `V1IdentityVerificationSessionRequiresInputEvent`, and `V1IdentityVerificationSessionVerifiedEvent` with related object `identity.VerificationSession`
* Remove support for thin events `V1InvoiceCreatedEvent`, `V1InvoiceDeletedEvent`, `V1InvoiceFinalizationFailedEvent`, `V1InvoiceFinalizedEvent`, `V1InvoiceMarkedUncollectibleEvent`, `V1InvoiceOverdueEvent`, `V1InvoiceOverpaidEvent`, `V1InvoicePaidEvent`, `V1InvoicePaymentActionRequiredEvent`, `V1InvoicePaymentFailedEvent`, `V1InvoicePaymentSucceededEvent`, `V1InvoiceSentEvent`, `V1InvoiceUpcomingEvent`, `V1InvoiceUpdatedEvent`, `V1InvoiceVoidedEvent`, and `V1InvoiceWillBeDueEvent` with related object `Invoice`
* Remove support for thin event `V1InvoicePaymentPaidEvent` with related object `InvoicePayment`
* Remove support for thin events `V1InvoiceitemCreatedEvent` and `V1InvoiceitemDeletedEvent` with related object `InvoiceItem`
* Remove support for thin events `V1IssuingAuthorizationCreatedEvent`, `V1IssuingAuthorizationRequestEvent`, and `V1IssuingAuthorizationUpdatedEvent` with related object `issuing.Authorization`
* Remove support for thin events `V1IssuingCardCreatedEvent` and `V1IssuingCardUpdatedEvent` with related object `issuing.Card`
* Remove support for thin events `V1IssuingCardholderCreatedEvent` and `V1IssuingCardholderUpdatedEvent` with related object `issuing.Cardholder`
* Remove support for thin events `V1IssuingDisputeClosedEvent`, `V1IssuingDisputeCreatedEvent`, `V1IssuingDisputeFundsReinstatedEvent`, `V1IssuingDisputeFundsRescindedEvent`, `V1IssuingDisputeSubmittedEvent`, and `V1IssuingDisputeUpdatedEvent` with related object `issuing.Dispute`
* Remove support for thin events `V1IssuingPersonalizationDesignActivatedEvent`, `V1IssuingPersonalizationDesignDeactivatedEvent`, `V1IssuingPersonalizationDesignRejectedEvent`, and `V1IssuingPersonalizationDesignUpdatedEvent` with related object `issuing.PersonalizationDesign`
* Remove support for thin events `V1IssuingTokenCreatedEvent` and `V1IssuingTokenUpdatedEvent` with related object `issuing.Token`
* Remove support for thin events `V1IssuingTransactionCreatedEvent`, `V1IssuingTransactionPurchaseDetailsReceiptUpdatedEvent`, and `V1IssuingTransactionUpdatedEvent` with related object `issuing.Transaction`
* Remove support for thin event `V1MandateUpdatedEvent` with related object `Mandate`
* Remove support for thin events `V1PaymentIntentAmountCapturableUpdatedEvent`, `V1PaymentIntentCanceledEvent`, `V1PaymentIntentCreatedEvent`, `V1PaymentIntentPartiallyFundedEvent`, `V1PaymentIntentPaymentFailedEvent`, `V1PaymentIntentProcessingEvent`, `V1PaymentIntentRequiresActionEvent`, and `V1PaymentIntentSucceededEvent` with related object `PaymentIntent`
* Remove support for thin events `V1PaymentLinkCreatedEvent` and `V1PaymentLinkUpdatedEvent` with related object `PaymentLink`
* Remove support for thin events `V1PaymentMethodAttachedEvent`, `V1PaymentMethodAutomaticallyUpdatedEvent`, `V1PaymentMethodDetachedEvent`, and `V1PaymentMethodUpdatedEvent` with related object `PaymentMethod`
* Remove support for thin events `V1PayoutCanceledEvent`, `V1PayoutCreatedEvent`, `V1PayoutFailedEvent`, `V1PayoutPaidEvent`, `V1PayoutReconciliationCompletedEvent`, and `V1PayoutUpdatedEvent` with related object `Payout`
* Remove support for thin events `V1PersonCreatedEvent`, `V1PersonDeletedEvent`, and `V1PersonUpdatedEvent` with related object `Person`
* Remove support for thin events `V1PlanCreatedEvent`, `V1PlanDeletedEvent`, and `V1PlanUpdatedEvent` with related object `Plan`
* Remove support for thin events `V1PriceCreatedEvent`, `V1PriceDeletedEvent`, and `V1PriceUpdatedEvent` with related object `Price`
* Remove support for thin events `V1ProductCreatedEvent`, `V1ProductDeletedEvent`, and `V1ProductUpdatedEvent` with related object `Product`
* Remove support for thin events `V1PromotionCodeCreatedEvent` and `V1PromotionCodeUpdatedEvent` with related object `PromotionCode`
* Remove support for thin events `V1QuoteAcceptedEvent`, `V1QuoteCanceledEvent`, `V1QuoteCreatedEvent`, and `V1QuoteFinalizedEvent` with related object `Quote`
* Remove support for thin events `V1RadarEarlyFraudWarningCreatedEvent` and `V1RadarEarlyFraudWarningUpdatedEvent` with related object `radar.EarlyFraudWarning`
* Remove support for thin events `V1ReviewClosedEvent` and `V1ReviewOpenedEvent` with related object `Review`
* Remove support for thin events `V1SetupIntentCanceledEvent`, `V1SetupIntentCreatedEvent`, `V1SetupIntentRequiresActionEvent`, `V1SetupIntentSetupFailedEvent`, and `V1SetupIntentSucceededEvent` with related object `SetupIntent`
* Remove support for thin event `V1SigmaScheduledQueryRunCreatedEvent` with related object `sigma.ScheduledQueryRun`
* Remove support for thin events `V1SourceCanceledEvent`, `V1SourceChargeableEvent`, `V1SourceFailedEvent`, and `V1SourceRefundAttributesRequiredEvent` with related object `Source`
* Remove support for thin events `V1SubscriptionScheduleAbortedEvent`, `V1SubscriptionScheduleCanceledEvent`, `V1SubscriptionScheduleCompletedEvent`, `V1SubscriptionScheduleCreatedEvent`, `V1SubscriptionScheduleExpiringEvent`, `V1SubscriptionScheduleReleasedEvent`, and `V1SubscriptionScheduleUpdatedEvent` with related object `SubscriptionSchedule`
* Remove support for thin events `V1TaxRateCreatedEvent` and `V1TaxRateUpdatedEvent` with related object `TaxRate`
* Remove support for thin events `V1TerminalReaderActionFailedEvent`, `V1TerminalReaderActionSucceededEvent`, and `V1TerminalReaderActionUpdatedEvent` with related object `terminal.Reader`
* Remove support for thin events `V1TestHelpersTestClockAdvancingEvent`, `V1TestHelpersTestClockCreatedEvent`, `V1TestHelpersTestClockDeletedEvent`, `V1TestHelpersTestClockInternalFailureEvent`, and `V1TestHelpersTestClockReadyEvent` with related object `test_helpers.TestClock`
* Remove support for thin events `V1TopupCanceledEvent`, `V1TopupCreatedEvent`, `V1TopupFailedEvent`, `V1TopupReversedEvent`, and `V1TopupSucceededEvent` with related object `Topup`
* Remove support for thin events `V1TransferCreatedEvent`, `V1TransferReversedEvent`, and `V1TransferUpdatedEvent` with related object `Transfer`
