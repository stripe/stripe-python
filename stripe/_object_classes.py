# -*- coding: utf-8 -*-
import stripe  # noqa: IMP101

OBJECT_CLASSES = {
    # data structures
    stripe.ListObject.OBJECT_NAME: stripe.ListObject,
    stripe.SearchResultObject.OBJECT_NAME: stripe.SearchResultObject,
    stripe.File.OBJECT_NAME_ALT: stripe.File,
    # Object classes: The beginning of the section generated from our OpenAPI spec
    stripe.Account.OBJECT_NAME: stripe.Account,
    stripe.AccountLink.OBJECT_NAME: stripe.AccountLink,
    stripe.AccountSession.OBJECT_NAME: stripe.AccountSession,
    stripe.ApplePayDomain.OBJECT_NAME: stripe.ApplePayDomain,
    stripe.Application.OBJECT_NAME: stripe.Application,
    stripe.ApplicationFee.OBJECT_NAME: stripe.ApplicationFee,
    stripe.ApplicationFeeRefund.OBJECT_NAME: stripe.ApplicationFeeRefund,
    stripe.apps.Secret.OBJECT_NAME: stripe.apps.Secret,
    stripe.Balance.OBJECT_NAME: stripe.Balance,
    stripe.BalanceTransaction.OBJECT_NAME: stripe.BalanceTransaction,
    stripe.BankAccount.OBJECT_NAME: stripe.BankAccount,
    stripe.billing_portal.Configuration.OBJECT_NAME: stripe.billing_portal.Configuration,
    stripe.billing_portal.Session.OBJECT_NAME: stripe.billing_portal.Session,
    stripe.billing.Alert.OBJECT_NAME: stripe.billing.Alert,
    stripe.billing.AlertTriggered.OBJECT_NAME: stripe.billing.AlertTriggered,
    stripe.billing.CreditBalanceSummary.OBJECT_NAME: stripe.billing.CreditBalanceSummary,
    stripe.billing.CreditBalanceTransaction.OBJECT_NAME: stripe.billing.CreditBalanceTransaction,
    stripe.billing.CreditGrant.OBJECT_NAME: stripe.billing.CreditGrant,
    stripe.billing.Meter.OBJECT_NAME: stripe.billing.Meter,
    stripe.billing.MeterEvent.OBJECT_NAME: stripe.billing.MeterEvent,
    stripe.billing.MeterEventAdjustment.OBJECT_NAME: stripe.billing.MeterEventAdjustment,
    stripe.billing.MeterEventSummary.OBJECT_NAME: stripe.billing.MeterEventSummary,
    stripe.Capability.OBJECT_NAME: stripe.Capability,
    stripe.Card.OBJECT_NAME: stripe.Card,
    stripe.CashBalance.OBJECT_NAME: stripe.CashBalance,
    stripe.Charge.OBJECT_NAME: stripe.Charge,
    stripe.checkout.Session.OBJECT_NAME: stripe.checkout.Session,
    stripe.climate.Order.OBJECT_NAME: stripe.climate.Order,
    stripe.climate.Product.OBJECT_NAME: stripe.climate.Product,
    stripe.climate.Supplier.OBJECT_NAME: stripe.climate.Supplier,
    stripe.ConfirmationToken.OBJECT_NAME: stripe.ConfirmationToken,
    stripe.ConnectCollectionTransfer.OBJECT_NAME: stripe.ConnectCollectionTransfer,
    stripe.CountrySpec.OBJECT_NAME: stripe.CountrySpec,
    stripe.Coupon.OBJECT_NAME: stripe.Coupon,
    stripe.CreditNote.OBJECT_NAME: stripe.CreditNote,
    stripe.CreditNoteLineItem.OBJECT_NAME: stripe.CreditNoteLineItem,
    stripe.Customer.OBJECT_NAME: stripe.Customer,
    stripe.CustomerBalanceTransaction.OBJECT_NAME: stripe.CustomerBalanceTransaction,
    stripe.CustomerCashBalanceTransaction.OBJECT_NAME: stripe.CustomerCashBalanceTransaction,
    stripe.CustomerSession.OBJECT_NAME: stripe.CustomerSession,
    stripe.Discount.OBJECT_NAME: stripe.Discount,
    stripe.Dispute.OBJECT_NAME: stripe.Dispute,
    stripe.entitlements.ActiveEntitlement.OBJECT_NAME: stripe.entitlements.ActiveEntitlement,
    stripe.entitlements.ActiveEntitlementSummary.OBJECT_NAME: stripe.entitlements.ActiveEntitlementSummary,
    stripe.entitlements.Feature.OBJECT_NAME: stripe.entitlements.Feature,
    stripe.EphemeralKey.OBJECT_NAME: stripe.EphemeralKey,
    stripe.Event.OBJECT_NAME: stripe.Event,
    stripe.ExchangeRate.OBJECT_NAME: stripe.ExchangeRate,
    stripe.File.OBJECT_NAME: stripe.File,
    stripe.FileLink.OBJECT_NAME: stripe.FileLink,
    stripe.financial_connections.Account.OBJECT_NAME: stripe.financial_connections.Account,
    stripe.financial_connections.AccountOwner.OBJECT_NAME: stripe.financial_connections.AccountOwner,
    stripe.financial_connections.AccountOwnership.OBJECT_NAME: stripe.financial_connections.AccountOwnership,
    stripe.financial_connections.Session.OBJECT_NAME: stripe.financial_connections.Session,
    stripe.financial_connections.Transaction.OBJECT_NAME: stripe.financial_connections.Transaction,
    stripe.forwarding.Request.OBJECT_NAME: stripe.forwarding.Request,
    stripe.FundingInstructions.OBJECT_NAME: stripe.FundingInstructions,
    stripe.identity.VerificationReport.OBJECT_NAME: stripe.identity.VerificationReport,
    stripe.identity.VerificationSession.OBJECT_NAME: stripe.identity.VerificationSession,
    stripe.Invoice.OBJECT_NAME: stripe.Invoice,
    stripe.InvoiceItem.OBJECT_NAME: stripe.InvoiceItem,
    stripe.InvoiceLineItem.OBJECT_NAME: stripe.InvoiceLineItem,
    stripe.InvoiceRenderingTemplate.OBJECT_NAME: stripe.InvoiceRenderingTemplate,
    stripe.issuing.Authorization.OBJECT_NAME: stripe.issuing.Authorization,
    stripe.issuing.Card.OBJECT_NAME: stripe.issuing.Card,
    stripe.issuing.Cardholder.OBJECT_NAME: stripe.issuing.Cardholder,
    stripe.issuing.Dispute.OBJECT_NAME: stripe.issuing.Dispute,
    stripe.issuing.PersonalizationDesign.OBJECT_NAME: stripe.issuing.PersonalizationDesign,
    stripe.issuing.PhysicalBundle.OBJECT_NAME: stripe.issuing.PhysicalBundle,
    stripe.issuing.Token.OBJECT_NAME: stripe.issuing.Token,
    stripe.issuing.Transaction.OBJECT_NAME: stripe.issuing.Transaction,
    stripe.LineItem.OBJECT_NAME: stripe.LineItem,
    stripe.LoginLink.OBJECT_NAME: stripe.LoginLink,
    stripe.Mandate.OBJECT_NAME: stripe.Mandate,
    stripe.PaymentIntent.OBJECT_NAME: stripe.PaymentIntent,
    stripe.PaymentLink.OBJECT_NAME: stripe.PaymentLink,
    stripe.PaymentMethod.OBJECT_NAME: stripe.PaymentMethod,
    stripe.PaymentMethodConfiguration.OBJECT_NAME: stripe.PaymentMethodConfiguration,
    stripe.PaymentMethodDomain.OBJECT_NAME: stripe.PaymentMethodDomain,
    stripe.Payout.OBJECT_NAME: stripe.Payout,
    stripe.Person.OBJECT_NAME: stripe.Person,
    stripe.Plan.OBJECT_NAME: stripe.Plan,
    stripe.Price.OBJECT_NAME: stripe.Price,
    stripe.Product.OBJECT_NAME: stripe.Product,
    stripe.ProductFeature.OBJECT_NAME: stripe.ProductFeature,
    stripe.PromotionCode.OBJECT_NAME: stripe.PromotionCode,
    stripe.Quote.OBJECT_NAME: stripe.Quote,
    stripe.radar.EarlyFraudWarning.OBJECT_NAME: stripe.radar.EarlyFraudWarning,
    stripe.radar.ValueList.OBJECT_NAME: stripe.radar.ValueList,
    stripe.radar.ValueListItem.OBJECT_NAME: stripe.radar.ValueListItem,
    stripe.Refund.OBJECT_NAME: stripe.Refund,
    stripe.reporting.ReportRun.OBJECT_NAME: stripe.reporting.ReportRun,
    stripe.reporting.ReportType.OBJECT_NAME: stripe.reporting.ReportType,
    stripe.ReserveTransaction.OBJECT_NAME: stripe.ReserveTransaction,
    stripe.Reversal.OBJECT_NAME: stripe.Reversal,
    stripe.Review.OBJECT_NAME: stripe.Review,
    stripe.SetupAttempt.OBJECT_NAME: stripe.SetupAttempt,
    stripe.SetupIntent.OBJECT_NAME: stripe.SetupIntent,
    stripe.ShippingRate.OBJECT_NAME: stripe.ShippingRate,
    stripe.sigma.ScheduledQueryRun.OBJECT_NAME: stripe.sigma.ScheduledQueryRun,
    stripe.Source.OBJECT_NAME: stripe.Source,
    stripe.SourceMandateNotification.OBJECT_NAME: stripe.SourceMandateNotification,
    stripe.SourceTransaction.OBJECT_NAME: stripe.SourceTransaction,
    stripe.Subscription.OBJECT_NAME: stripe.Subscription,
    stripe.SubscriptionItem.OBJECT_NAME: stripe.SubscriptionItem,
    stripe.SubscriptionSchedule.OBJECT_NAME: stripe.SubscriptionSchedule,
    stripe.tax.Calculation.OBJECT_NAME: stripe.tax.Calculation,
    stripe.tax.CalculationLineItem.OBJECT_NAME: stripe.tax.CalculationLineItem,
    stripe.tax.Registration.OBJECT_NAME: stripe.tax.Registration,
    stripe.tax.Settings.OBJECT_NAME: stripe.tax.Settings,
    stripe.tax.Transaction.OBJECT_NAME: stripe.tax.Transaction,
    stripe.tax.TransactionLineItem.OBJECT_NAME: stripe.tax.TransactionLineItem,
    stripe.TaxCode.OBJECT_NAME: stripe.TaxCode,
    stripe.TaxDeductedAtSource.OBJECT_NAME: stripe.TaxDeductedAtSource,
    stripe.TaxId.OBJECT_NAME: stripe.TaxId,
    stripe.TaxRate.OBJECT_NAME: stripe.TaxRate,
    stripe.terminal.Configuration.OBJECT_NAME: stripe.terminal.Configuration,
    stripe.terminal.ConnectionToken.OBJECT_NAME: stripe.terminal.ConnectionToken,
    stripe.terminal.Location.OBJECT_NAME: stripe.terminal.Location,
    stripe.terminal.Reader.OBJECT_NAME: stripe.terminal.Reader,
    stripe.test_helpers.TestClock.OBJECT_NAME: stripe.test_helpers.TestClock,
    stripe.Token.OBJECT_NAME: stripe.Token,
    stripe.Topup.OBJECT_NAME: stripe.Topup,
    stripe.Transfer.OBJECT_NAME: stripe.Transfer,
    stripe.treasury.CreditReversal.OBJECT_NAME: stripe.treasury.CreditReversal,
    stripe.treasury.DebitReversal.OBJECT_NAME: stripe.treasury.DebitReversal,
    stripe.treasury.FinancialAccount.OBJECT_NAME: stripe.treasury.FinancialAccount,
    stripe.treasury.FinancialAccountFeatures.OBJECT_NAME: stripe.treasury.FinancialAccountFeatures,
    stripe.treasury.InboundTransfer.OBJECT_NAME: stripe.treasury.InboundTransfer,
    stripe.treasury.OutboundPayment.OBJECT_NAME: stripe.treasury.OutboundPayment,
    stripe.treasury.OutboundTransfer.OBJECT_NAME: stripe.treasury.OutboundTransfer,
    stripe.treasury.ReceivedCredit.OBJECT_NAME: stripe.treasury.ReceivedCredit,
    stripe.treasury.ReceivedDebit.OBJECT_NAME: stripe.treasury.ReceivedDebit,
    stripe.treasury.Transaction.OBJECT_NAME: stripe.treasury.Transaction,
    stripe.treasury.TransactionEntry.OBJECT_NAME: stripe.treasury.TransactionEntry,
    stripe.UsageRecord.OBJECT_NAME: stripe.UsageRecord,
    stripe.UsageRecordSummary.OBJECT_NAME: stripe.UsageRecordSummary,
    stripe.WebhookEndpoint.OBJECT_NAME: stripe.WebhookEndpoint,
    # Object classes: The end of the section generated from our OpenAPI spec
}

V2_OBJECT_CLASSES = {
    # V2 Object classes: The beginning of the section generated from our OpenAPI spec
    stripe.v2.billing.MeterEvent.OBJECT_NAME: stripe.v2.billing.MeterEvent,
    stripe.v2.billing.MeterEventAdjustment.OBJECT_NAME: stripe.v2.billing.MeterEventAdjustment,
    stripe.v2.billing.MeterEventSession.OBJECT_NAME: stripe.v2.billing.MeterEventSession,
    stripe.v2.Event.OBJECT_NAME: stripe.v2.Event,
    stripe.v2.EventDestination.OBJECT_NAME: stripe.v2.EventDestination,
    # V2 Object classes: The end of the section generated from our OpenAPI spec
}
