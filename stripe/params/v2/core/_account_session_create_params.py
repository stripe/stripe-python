# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountSessionCreateParams(TypedDict):
    account: str
    """
    The ID of the account to create an Account Session for.
    """
    components: "AccountSessionCreateParamsComponents"
    """
    The embedded components to enable for this Account Session.
    """
    scopes: NotRequired["AccountSessionCreateParamsScopes"]
    """
    Permissions to grant across the enabled components.
    """


class AccountSessionCreateParamsComponents(TypedDict):
    account_management: NotRequired[
        "AccountSessionCreateParamsComponentsAccountManagement"
    ]
    """
    Settings for the Account Management embedded component.
    """
    account_onboarding: NotRequired[
        "AccountSessionCreateParamsComponentsAccountOnboarding"
    ]
    """
    Settings for the Account Onboarding embedded component.
    """
    agentic_commerce_settings: NotRequired[
        "AccountSessionCreateParamsComponentsAgenticCommerceSettings"
    ]
    """
    Settings for the Agentic Commerce Settings embedded component.
    """
    app_install: NotRequired["AccountSessionCreateParamsComponentsAppInstall"]
    """
    Settings for the App Install embedded component.
    """
    app_viewport: NotRequired[
        "AccountSessionCreateParamsComponentsAppViewport"
    ]
    """
    Settings for the App Viewport embedded component.
    """
    balance_report: NotRequired[
        "AccountSessionCreateParamsComponentsBalanceReport"
    ]
    """
    Settings for the Balance Report embedded component.
    """
    balances: NotRequired["AccountSessionCreateParamsComponentsBalances"]
    """
    Settings for the Balances embedded component.
    """
    bills: NotRequired["AccountSessionCreateParamsComponentsBills"]
    """
    Settings for the Bills embedded component.
    """
    capital_financing: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancing"
    ]
    """
    Settings for the Capital Financing embedded component.
    """
    capital_financing_application: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingApplication"
    ]
    """
    Settings for the Capital Financing Application embedded component.
    """
    capital_financing_promotion: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingPromotion"
    ]
    """
    Settings for the Capital Financing Promotion embedded component.
    """
    check_scanning: NotRequired[
        "AccountSessionCreateParamsComponentsCheckScanning"
    ]
    """
    Settings for the Check Scanning embedded component.
    """
    disputes_list: NotRequired[
        "AccountSessionCreateParamsComponentsDisputesList"
    ]
    """
    Settings for the Disputes List embedded component.
    """
    documents: NotRequired["AccountSessionCreateParamsComponentsDocuments"]
    """
    Settings for the Documents embedded component.
    """
    export_tax_transactions: NotRequired[
        "AccountSessionCreateParamsComponentsExportTaxTransactions"
    ]
    """
    Settings for the Export Tax Transactions embedded component.
    """
    financial_account_rewards: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccountRewards"
    ]
    """
    Settings for the Financial Account Rewards embedded component.
    """
    financial_accounts: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccounts"
    ]
    """
    Settings for the Financial Accounts embedded component.
    """
    financial_accounts_transactions: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccountsTransactions"
    ]
    """
    Settings for the Financial Accounts Transactions embedded component.
    """
    instant_payouts_promotion: NotRequired[
        "AccountSessionCreateParamsComponentsInstantPayoutsPromotion"
    ]
    """
    Settings for the Instant Payouts Promotion embedded component.
    """
    invoice_history: NotRequired[
        "AccountSessionCreateParamsComponentsInvoiceHistory"
    ]
    """
    Settings for the Invoice History embedded component.
    """
    issuing_card: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCard"
    ]
    """
    Settings for the Issuing Card embedded component.
    """
    issuing_cards_list: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCardsList"
    ]
    """
    Settings for the Issuing Cards List embedded component.
    """
    network_cost_passthrough_report: NotRequired[
        "AccountSessionCreateParamsComponentsNetworkCostPassthroughReport"
    ]
    """
    Settings for the Network Cost Passthrough Report embedded component.
    """
    notification_banner: NotRequired[
        "AccountSessionCreateParamsComponentsNotificationBanner"
    ]
    """
    Settings for the Notification Banner embedded component.
    """
    payment_details: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDetails"
    ]
    """
    Settings for the Payment Details embedded component.
    """
    payment_disputes: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDisputes"
    ]
    """
    Settings for the Payment Disputes embedded component.
    """
    payment_method_settings: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentMethodSettings"
    ]
    """
    Settings for the Payment Method Settings embedded component.
    """
    payments: NotRequired["AccountSessionCreateParamsComponentsPayments"]
    """
    Settings for the Payments embedded component.
    """
    payout_details: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutDetails"
    ]
    """
    Settings for the Payout Details embedded component.
    """
    payout_reconciliation_report: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutReconciliationReport"
    ]
    """
    Settings for the Payout Reconciliation Report embedded component.
    """
    payouts: NotRequired["AccountSessionCreateParamsComponentsPayouts"]
    """
    Settings for the Payouts embedded component.
    """
    payouts_list: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutsList"
    ]
    """
    Settings for the Payouts List embedded component.
    """
    product_tax_code_selector: NotRequired[
        "AccountSessionCreateParamsComponentsProductTaxCodeSelector"
    ]
    """
    Settings for the Product Tax Code Selector embedded component.
    """
    reporting_chart: NotRequired[
        "AccountSessionCreateParamsComponentsReportingChart"
    ]
    """
    Settings for the Reporting Chart embedded component.
    """
    tax_registrations: NotRequired[
        "AccountSessionCreateParamsComponentsTaxRegistrations"
    ]
    """
    Settings for the Tax Registrations embedded component.
    """
    tax_settings: NotRequired[
        "AccountSessionCreateParamsComponentsTaxSettings"
    ]
    """
    Settings for the Tax Settings embedded component.
    """
    tax_threshold_monitoring: NotRequired[
        "AccountSessionCreateParamsComponentsTaxThresholdMonitoring"
    ]
    """
    Settings for the Tax Threshold Monitoring embedded component.
    """
    terminal_hardware_orders: NotRequired[
        "AccountSessionCreateParamsComponentsTerminalHardwareOrders"
    ]
    """
    Settings for the Terminal Hardware Orders embedded component.
    """
    terminal_hardware_shop: NotRequired[
        "AccountSessionCreateParamsComponentsTerminalHardwareShop"
    ]
    """
    Settings for the Terminal Hardware Shop embedded component.
    """


class AccountSessionCreateParamsComponentsAccountManagement(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsAccountOnboarding(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsAgenticCommerceSettings(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsAppInstall(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsAppViewport(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsBalanceReport(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsBalances(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsBills(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsCapitalFinancing(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsCapitalFinancingApplication(
    TypedDict,
):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsCapitalFinancingPromotion(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsCheckScanning(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsDisputesList(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsDocuments(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsExportTaxTransactions(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsFinancialAccountRewards(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsFinancialAccounts(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsFinancialAccountsTransactions(
    TypedDict,
):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsInstantPayoutsPromotion(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsInvoiceHistory(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsIssuingCard(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsIssuingCardsList(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsNetworkCostPassthroughReport(
    TypedDict,
):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsNotificationBanner(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPaymentDetails(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPaymentDisputes(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPaymentMethodSettings(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPayments(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPayoutDetails(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPayoutReconciliationReport(
    TypedDict
):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPayouts(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsPayoutsList(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsProductTaxCodeSelector(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsReportingChart(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsTaxRegistrations(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsTaxSettings(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsTaxThresholdMonitoring(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsTerminalHardwareOrders(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsComponentsTerminalHardwareShop(TypedDict):
    enabled: bool
    """
    Whether this embedded component is enabled.
    """


class AccountSessionCreateParamsScopes(TypedDict):
    allowed_stripe_app_ids: NotRequired[List[str]]
    """
    The Stripe App IDs allowed in the enabled app components.
    """
    capture_payments: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow capturing payments.
    """
    create_instant_payouts: NotRequired[
        Literal["disabled", "enabled", "use_dashboard_rules"]
    ]
    """
    Controls whether creating instant payouts is enabled, disabled, or determined by Dashboard rules.
    """
    create_outbound_payments: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow creating outbound payments.
    """
    create_payout_schedule: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow changing the payout schedule.
    """
    create_standard_payouts: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow creating standard payouts.
    """
    create_us_paper_check_on_application: NotRequired[
        Literal["disabled", "enabled"]
    ]
    """
    Whether to allow creating US paper checks on the application.
    """
    disable_stripe_user_authentication: NotRequired[
        Literal["disabled", "enabled"]
    ]
    """
    Whether to disable Stripe user authentication in the enabled components.
    """
    manage_bills: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing bills.
    """
    manage_destination_on_behalf_of_charges: NotRequired[
        Literal["disabled", "enabled"]
    ]
    """
    Whether to allow managing destination and on-behalf-of charges.
    """
    manage_issuing_cardholders: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing Issuing cardholders.
    """
    manage_issuing_cards: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing Issuing cards.
    """
    manage_issuing_disputes: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing Issuing disputes.
    """
    manage_issuing_spending_controls: NotRequired[
        Literal["disabled", "enabled"]
    ]
    """
    Whether to allow managing Issuing spending controls.
    """
    manage_payment_disputes: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing payment disputes.
    """
    manage_payout_methods: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing payout methods.
    """
    manage_refund_payments: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow refunding payments.
    """
    manage_smart_disputes: NotRequired[Literal["disabled", "enabled"]]
    """
    Whether to allow managing Smart Disputes.
    """
