---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1693
is_stripe_api_change: true
released_in_version: 14.2.0a1
---

* Add support for new resources `shared_payment.GrantedToken`, `v2.iam.ApiKey`, `v2.payments.SettlementAllocationIntentSplit`, `v2.payments.SettlementAllocationIntent`, and `v2.tax.ManualRule`
* Add support for `retrieve` method on resource `shared_payment.GrantedToken`
* Add support for `create` and `modify` test helper methods on resource `shared_payment.GrantedToken`
* Add support for `create`, `deactivate`, `list`, `modify`, and `retrieve` methods on resource `v2.tax.ManualRule`
* Add support for `cancel`, `create`, `modify`, `retrieve`, and `submit` methods on resource `v2.payments.SettlementAllocationIntent`
* Add support for `cancel`, `create`, and `retrieve` methods on resource `v2.payments.SettlementAllocationIntentSplit`
* Add support for `create`, `expire`, `list`, `modify`, `retrieve`, and `rotate` methods on resource `v2.iam.ApiKey`
* Add support for `check_scanning` on `AccountSessionCreateParamsComponent`
* Add support for `tax_details` on `InvoiceAddLinesParamsLinePriceDatumProductDatum`, `InvoiceLineItemModifyParamsPriceDatumProductDatum`, `InvoiceUpdateLinesParamsLinePriceDatumProductDatum`, `PaymentLinkCreateParamsLineItemPriceDatumProductDatum`, `ProductCreateParams`, `ProductModifyParams`, `checkout.SessionCreateParamsLineItemPriceDatumProductDatum`, and `checkout.SessionModifyParamsLineItemPriceDatumProductDatum`
* Add support for `payment_method_data` on `delegated_checkout.RequestedSessionConfirmParams`
* Add support for `product_details` on `DelegatedCheckout.RequestedSession.LineItemDetail`
* Add support for `wallets` on `issuing.CardListParams`
* Add support for `primary_account_identifier` on `Issuing.Card.Wallet.ApplePay` and `Issuing.Card.Wallet.GooglePay`
* Add support for `shared_payment_granted_token` on `PaymentIntentConfirmParams`, `PaymentIntentCreateParams`, and `PaymentIntent`
* Change `ProductCatalog.TrialOffer.Duration.relative` to be optional
* Add support for new values `al_bank_account`, `am_bank_account`, `bn_bank_account`, `bw_bank_account`, `dz_bank_account`, `gy_bank_account`, `jm_bank_account`, `jo_bank_account`, `kw_bank_account`, `lk_bank_account`, `ma_bank_account`, `om_bank_account`, and `tz_bank_account` on enum `V2.Account.Configuration.RecipientDatum.DefaultOutboundDestination.type`
* Add support for `instant` on `V2.Account.Configuration.RecipientDatum.Feature.BankAccount`, `V2.Core.Account.Configuration.Recipient.Capability.BankAccount`, `v2.AccountCreateParamsConfigurationRecipientDatumFeatureBankAccount`, `v2.AccountModifyParamsConfigurationRecipientDatumFeatureBankAccount`, `v2.core.AccountCreateParamsConfigurationRecipientCapabilityBankAccount`, and `v2.core.AccountModifyParamsConfigurationRecipientCapabilityBankAccount`
* Add support for new value `bank_accounts.instant` on enum `V2.Account.Requirement.Impact.required_for_features`
* Add support for `collect_at` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.IntentAction.Modify`, `V2.Billing.IntentAction.Subscribe`, `v2.billing.IntentCreateParamsActionDeactivate`, `v2.billing.IntentCreateParamsActionModify`, and `v2.billing.IntentCreateParamsActionSubscribe`
* Remove support for `billing_details` on `V2.Billing.IntentAction.Deactivate`, `V2.Billing.IntentAction.Modify`, `V2.Billing.IntentAction.Subscribe`, `v2.billing.IntentCreateParamsActionDeactivate`, `v2.billing.IntentCreateParamsActionModify`, and `v2.billing.IntentCreateParamsActionSubscribe`
* Add support for `overrides` on `V2.Billing.IntentAction.Deactivate.PricingPlanSubscriptionDetail`, `V2.Billing.IntentAction.Modify.PricingPlanSubscriptionDetail`, `V2.Billing.IntentAction.Subscribe.PricingPlanSubscriptionDetail`, `v2.billing.IntentCreateParamsActionDeactivatePricingPlanSubscriptionDetail`, `v2.billing.IntentCreateParamsActionModifyPricingPlanSubscriptionDetail`, and `v2.billing.IntentCreateParamsActionSubscribePricingPlanSubscriptionDetail`
* Remove support for `requested` on `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Celtic.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.CrossRiverBank.SpendCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Lead.PrepaidCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.ChargeCard`, `V2.Core.Account.Configuration.CardCreator.Capability.Commercial.Stripe.PrepaidCard`, `V2.Core.Account.Configuration.Recipient.Capability.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.FinancialAddress.CryptoWallet`, `V2.Core.Account.Configuration.Storer.Capability.HoldsCurrency.Usdc`, `V2.Core.Account.Configuration.Storer.Capability.OutboundPayment.CryptoWallet`, and `V2.Core.Account.Configuration.Storer.Capability.OutboundTransfer.CryptoWallet`
* Add support for new value `bank_accounts.instant` on enums `V2.Core.Account.FutureRequirement.Entry.Impact.RestrictsCapability.capability` and `V2.Core.Account.Requirement.Entry.Impact.RestrictsCapability.capability`
* Add support for `alternative_reference` on `V2.Core.Vault.GbBankAccount`, `V2.Core.Vault.UsBankAccount`, and `V2.MoneyManagement.PayoutMethod`
* Add support for `managed_by` and `payments` on `V2.MoneyManagement.FinancialAccount`
* Add support for new value `payments` on enum `V2.MoneyManagement.FinancialAccount.type`
* Add support for `speed` on `V2.MoneyManagement.OutboundPayment.DeliveryOption`, `V2.MoneyManagement.OutboundPaymentQuote.DeliveryOption`, `v2.money_management.OutboundPaymentCreateParamsDeliveryOption`, and `v2.money_management.OutboundPaymentQuoteCreateParamsDeliveryOption`
* Add support for new value `real_time_payout_fee` on enum `V2.MoneyManagement.OutboundPaymentQuote.EstimatedFee.type`
* Add support for `types` on `v2.money_management.FinancialAccountListParams`
* Change type of `v2.core.AccountListParams.applied_configurations` from `string` to `enum`
* Add support for new value `bank_accounts.instant` on enum `EventsV2CoreAccountIncludingConfigurationRecipientCapabilityStatusUpdatedEvent.updated_capability`
* Add support for `top_impacted_accounts` on `EventsV2CoreHealthApiErrorFiringEvent.Impact`, `EventsV2CoreHealthApiErrorResolvedEvent.Impact`, `EventsV2CoreHealthApiLatencyFiringEvent.Impact`, `EventsV2CoreHealthApiLatencyResolvedEvent.Impact`, `EventsV2CoreHealthPaymentMethodErrorFiringEvent.Impact`, and `EventsV2CoreHealthPaymentMethodErrorResolvedEvent.Impact`
* Add support for event notifications `V2CoreHealthSepaDebitDelayedFiringEvent`, `V2CoreHealthSepaDebitDelayedResolvedEvent`, and `V2PaymentsSettlementAllocationIntentNotFoundEvent`
* Add support for event notifications `V2PaymentsSettlementAllocationIntentCanceledEvent`, `V2PaymentsSettlementAllocationIntentCreatedEvent`, `V2PaymentsSettlementAllocationIntentErroredEvent`, `V2PaymentsSettlementAllocationIntentFundsNotReceivedEvent`, `V2PaymentsSettlementAllocationIntentMatchedEvent`, `V2PaymentsSettlementAllocationIntentSettledEvent`, and `V2PaymentsSettlementAllocationIntentSubmittedEvent` with related object `v2.payments.SettlementAllocationIntent`
* Add support for event notifications `V2PaymentsSettlementAllocationIntentSplitCanceledEvent`, `V2PaymentsSettlementAllocationIntentSplitCreatedEvent`, and `V2PaymentsSettlementAllocationIntentSplitSettledEvent` with related object `v2.payments.SettlementAllocationIntentSplit`
* Remove support for error code `account_rate_limit_exceeded` on `RateLimitError`
