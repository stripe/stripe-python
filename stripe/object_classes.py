# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_resources


OBJECT_CLASSES = {
    # data structures
    api_resources.ListObject.OBJECT_NAME: api_resources.ListObject,
    api_resources.SearchResultObject.OBJECT_NAME: api_resources.SearchResultObject,
    # business objects
    api_resources.Account.OBJECT_NAME: api_resources.Account,
    api_resources.AccountLink.OBJECT_NAME: api_resources.AccountLink,
    api_resources.AccountSession.OBJECT_NAME: api_resources.AccountSession,
    api_resources.ApplePayDomain.OBJECT_NAME: api_resources.ApplePayDomain,
    api_resources.Application.OBJECT_NAME: api_resources.Application,
    api_resources.ApplicationFee.OBJECT_NAME: api_resources.ApplicationFee,
    api_resources.ApplicationFeeRefund.OBJECT_NAME: api_resources.ApplicationFeeRefund,
    api_resources.apps.Secret.OBJECT_NAME: api_resources.apps.Secret,
    api_resources.Balance.OBJECT_NAME: api_resources.Balance,
    api_resources.BalanceTransaction.OBJECT_NAME: api_resources.BalanceTransaction,
    api_resources.BankAccount.OBJECT_NAME: api_resources.BankAccount,
    api_resources.billing_portal.Configuration.OBJECT_NAME: api_resources.billing_portal.Configuration,
    api_resources.billing_portal.Session.OBJECT_NAME: api_resources.billing_portal.Session,
    api_resources.Capability.OBJECT_NAME: api_resources.Capability,
    api_resources.Card.OBJECT_NAME: api_resources.Card,
    api_resources.CashBalance.OBJECT_NAME: api_resources.CashBalance,
    api_resources.Charge.OBJECT_NAME: api_resources.Charge,
    api_resources.checkout.Session.OBJECT_NAME: api_resources.checkout.Session,
    api_resources.ConnectCollectionTransfer.OBJECT_NAME: api_resources.ConnectCollectionTransfer,
    api_resources.CountrySpec.OBJECT_NAME: api_resources.CountrySpec,
    api_resources.Coupon.OBJECT_NAME: api_resources.Coupon,
    api_resources.CreditNote.OBJECT_NAME: api_resources.CreditNote,
    api_resources.CreditNoteLineItem.OBJECT_NAME: api_resources.CreditNoteLineItem,
    api_resources.Customer.OBJECT_NAME: api_resources.Customer,
    api_resources.CustomerBalanceTransaction.OBJECT_NAME: api_resources.CustomerBalanceTransaction,
    api_resources.CustomerCashBalanceTransaction.OBJECT_NAME: api_resources.CustomerCashBalanceTransaction,
    api_resources.Discount.OBJECT_NAME: api_resources.Discount,
    api_resources.Dispute.OBJECT_NAME: api_resources.Dispute,
    api_resources.EphemeralKey.OBJECT_NAME: api_resources.EphemeralKey,
    api_resources.Event.OBJECT_NAME: api_resources.Event,
    api_resources.ExchangeRate.OBJECT_NAME: api_resources.ExchangeRate,
    api_resources.File.OBJECT_NAME: api_resources.File,
    api_resources.File.OBJECT_NAME_ALT: api_resources.File,
    api_resources.FileLink.OBJECT_NAME: api_resources.FileLink,
    api_resources.financial_connections.Account.OBJECT_NAME: api_resources.financial_connections.Account,
    api_resources.financial_connections.AccountOwner.OBJECT_NAME: api_resources.financial_connections.AccountOwner,
    api_resources.financial_connections.AccountOwnership.OBJECT_NAME: api_resources.financial_connections.AccountOwnership,
    api_resources.financial_connections.Session.OBJECT_NAME: api_resources.financial_connections.Session,
    api_resources.FundingInstructions.OBJECT_NAME: api_resources.FundingInstructions,
    api_resources.identity.VerificationReport.OBJECT_NAME: api_resources.identity.VerificationReport,
    api_resources.identity.VerificationSession.OBJECT_NAME: api_resources.identity.VerificationSession,
    api_resources.Invoice.OBJECT_NAME: api_resources.Invoice,
    api_resources.InvoiceItem.OBJECT_NAME: api_resources.InvoiceItem,
    api_resources.InvoiceLineItem.OBJECT_NAME: api_resources.InvoiceLineItem,
    api_resources.issuing.Authorization.OBJECT_NAME: api_resources.issuing.Authorization,
    api_resources.issuing.Card.OBJECT_NAME: api_resources.issuing.Card,
    api_resources.issuing.Cardholder.OBJECT_NAME: api_resources.issuing.Cardholder,
    api_resources.issuing.Dispute.OBJECT_NAME: api_resources.issuing.Dispute,
    api_resources.issuing.Transaction.OBJECT_NAME: api_resources.issuing.Transaction,
    api_resources.LineItem.OBJECT_NAME: api_resources.LineItem,
    api_resources.LoginLink.OBJECT_NAME: api_resources.LoginLink,
    api_resources.Mandate.OBJECT_NAME: api_resources.Mandate,
    api_resources.PaymentIntent.OBJECT_NAME: api_resources.PaymentIntent,
    api_resources.PaymentLink.OBJECT_NAME: api_resources.PaymentLink,
    api_resources.PaymentMethod.OBJECT_NAME: api_resources.PaymentMethod,
    api_resources.PaymentMethodConfiguration.OBJECT_NAME: api_resources.PaymentMethodConfiguration,
    api_resources.PaymentMethodDomain.OBJECT_NAME: api_resources.PaymentMethodDomain,
    api_resources.Payout.OBJECT_NAME: api_resources.Payout,
    api_resources.Person.OBJECT_NAME: api_resources.Person,
    api_resources.Plan.OBJECT_NAME: api_resources.Plan,
    api_resources.PlatformTaxFee.OBJECT_NAME: api_resources.PlatformTaxFee,
    api_resources.Price.OBJECT_NAME: api_resources.Price,
    api_resources.Product.OBJECT_NAME: api_resources.Product,
    api_resources.PromotionCode.OBJECT_NAME: api_resources.PromotionCode,
    api_resources.Quote.OBJECT_NAME: api_resources.Quote,
    api_resources.radar.EarlyFraudWarning.OBJECT_NAME: api_resources.radar.EarlyFraudWarning,
    api_resources.radar.ValueList.OBJECT_NAME: api_resources.radar.ValueList,
    api_resources.radar.ValueListItem.OBJECT_NAME: api_resources.radar.ValueListItem,
    api_resources.Refund.OBJECT_NAME: api_resources.Refund,
    api_resources.reporting.ReportRun.OBJECT_NAME: api_resources.reporting.ReportRun,
    api_resources.reporting.ReportType.OBJECT_NAME: api_resources.reporting.ReportType,
    api_resources.ReserveTransaction.OBJECT_NAME: api_resources.ReserveTransaction,
    api_resources.Reversal.OBJECT_NAME: api_resources.Reversal,
    api_resources.Review.OBJECT_NAME: api_resources.Review,
    api_resources.SetupAttempt.OBJECT_NAME: api_resources.SetupAttempt,
    api_resources.SetupIntent.OBJECT_NAME: api_resources.SetupIntent,
    api_resources.ShippingRate.OBJECT_NAME: api_resources.ShippingRate,
    api_resources.sigma.ScheduledQueryRun.OBJECT_NAME: api_resources.sigma.ScheduledQueryRun,
    api_resources.Source.OBJECT_NAME: api_resources.Source,
    api_resources.SourceMandateNotification.OBJECT_NAME: api_resources.SourceMandateNotification,
    api_resources.SourceTransaction.OBJECT_NAME: api_resources.SourceTransaction,
    api_resources.Subscription.OBJECT_NAME: api_resources.Subscription,
    api_resources.SubscriptionItem.OBJECT_NAME: api_resources.SubscriptionItem,
    api_resources.SubscriptionSchedule.OBJECT_NAME: api_resources.SubscriptionSchedule,
    api_resources.tax.Calculation.OBJECT_NAME: api_resources.tax.Calculation,
    api_resources.tax.CalculationLineItem.OBJECT_NAME: api_resources.tax.CalculationLineItem,
    api_resources.tax.Settings.OBJECT_NAME: api_resources.tax.Settings,
    api_resources.tax.Transaction.OBJECT_NAME: api_resources.tax.Transaction,
    api_resources.tax.TransactionLineItem.OBJECT_NAME: api_resources.tax.TransactionLineItem,
    api_resources.TaxCode.OBJECT_NAME: api_resources.TaxCode,
    api_resources.TaxDeductedAtSource.OBJECT_NAME: api_resources.TaxDeductedAtSource,
    api_resources.TaxId.OBJECT_NAME: api_resources.TaxId,
    api_resources.TaxRate.OBJECT_NAME: api_resources.TaxRate,
    api_resources.terminal.Configuration.OBJECT_NAME: api_resources.terminal.Configuration,
    api_resources.terminal.ConnectionToken.OBJECT_NAME: api_resources.terminal.ConnectionToken,
    api_resources.terminal.Location.OBJECT_NAME: api_resources.terminal.Location,
    api_resources.terminal.Reader.OBJECT_NAME: api_resources.terminal.Reader,
    api_resources.test_helpers.TestClock.OBJECT_NAME: api_resources.test_helpers.TestClock,
    api_resources.Token.OBJECT_NAME: api_resources.Token,
    api_resources.Topup.OBJECT_NAME: api_resources.Topup,
    api_resources.Transfer.OBJECT_NAME: api_resources.Transfer,
    api_resources.treasury.CreditReversal.OBJECT_NAME: api_resources.treasury.CreditReversal,
    api_resources.treasury.DebitReversal.OBJECT_NAME: api_resources.treasury.DebitReversal,
    api_resources.treasury.FinancialAccount.OBJECT_NAME: api_resources.treasury.FinancialAccount,
    api_resources.treasury.FinancialAccountFeatures.OBJECT_NAME: api_resources.treasury.FinancialAccountFeatures,
    api_resources.treasury.InboundTransfer.OBJECT_NAME: api_resources.treasury.InboundTransfer,
    api_resources.treasury.OutboundPayment.OBJECT_NAME: api_resources.treasury.OutboundPayment,
    api_resources.treasury.OutboundTransfer.OBJECT_NAME: api_resources.treasury.OutboundTransfer,
    api_resources.treasury.ReceivedCredit.OBJECT_NAME: api_resources.treasury.ReceivedCredit,
    api_resources.treasury.ReceivedDebit.OBJECT_NAME: api_resources.treasury.ReceivedDebit,
    api_resources.treasury.Transaction.OBJECT_NAME: api_resources.treasury.Transaction,
    api_resources.treasury.TransactionEntry.OBJECT_NAME: api_resources.treasury.TransactionEntry,
    api_resources.UsageRecord.OBJECT_NAME: api_resources.UsageRecord,
    api_resources.UsageRecordSummary.OBJECT_NAME: api_resources.UsageRecordSummary,
    api_resources.WebhookEndpoint.OBJECT_NAME: api_resources.WebhookEndpoint,
}
