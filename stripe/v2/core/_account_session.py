# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class AccountSession(StripeObject):
    """
    An Account Session grants access to an account through Connect embedded components for a limited time.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.account_session"]] = (
        "v2.core.account_session"
    )

    class Components(StripeObject):
        class AccountManagement(StripeObject):
            class Scopes(StripeObject):
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class AccountOnboarding(StripeObject):
            class Scopes(StripeObject):
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class AgenticCommerceSettings(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class AppInstall(StripeObject):
            class Scopes(StripeObject):
                allowed_stripe_app_ids: List[str]
                """
                The Stripe App IDs allowed in the enabled app components.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class AppViewport(StripeObject):
            class Scopes(StripeObject):
                allowed_stripe_app_ids: List[str]
                """
                The Stripe App IDs allowed in the enabled app components.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class BalanceReport(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class Balances(StripeObject):
            class Scopes(StripeObject):
                create_instant_payouts: Optional[
                    Literal["disabled", "enabled", "use_dashboard_rules"]
                ]
                """
                Controls whether creating instant payouts is enabled, disabled, or determined by Dashboard rules.
                """
                create_payout_schedule: Literal["disabled", "enabled"]
                """
                Whether to allow changing the payout schedule.
                """
                create_standard_payouts: Literal["disabled", "enabled"]
                """
                Whether to allow creating standard payouts.
                """
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class Bills(StripeObject):
            class Scopes(StripeObject):
                create_outbound_payments: Literal["disabled", "enabled"]
                """
                Whether to allow creating outbound payments.
                """
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_bills: Literal["disabled", "enabled"]
                """
                Whether to allow managing bills.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class CapitalFinancing(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class CapitalFinancingApplication(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class CapitalFinancingPromotion(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class CheckScanning(StripeObject):
            class Scopes(StripeObject):
                create_us_paper_check_on_application: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow creating US paper checks on the application.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class DisputesList(StripeObject):
            class Scopes(StripeObject):
                capture_payments: Literal["disabled", "enabled"]
                """
                Whether to allow capturing payments.
                """
                manage_destination_on_behalf_of_charges: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing destination and on-behalf-of charges.
                """
                manage_payment_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing payment disputes.
                """
                manage_refund_payments: Literal["disabled", "enabled"]
                """
                Whether to allow refunding payments.
                """
                manage_smart_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Smart Disputes.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class Documents(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class ExportTaxTransactions(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class FinancialAccountRewards(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class FinancialAccounts(StripeObject):
            class Scopes(StripeObject):
                create_outbound_payments: Literal["disabled", "enabled"]
                """
                Whether to allow creating outbound payments.
                """
                create_payout_schedule: Literal["disabled", "enabled"]
                """
                Whether to allow changing the payout schedule.
                """
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_bills: Literal["disabled", "enabled"]
                """
                Whether to allow managing bills.
                """
                manage_issuing_cards: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cards.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class FinancialAccountsTransactions(StripeObject):
            class Scopes(StripeObject):
                capture_payments: Literal["disabled", "enabled"]
                """
                Whether to allow capturing payments.
                """
                manage_destination_on_behalf_of_charges: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing destination and on-behalf-of charges.
                """
                manage_issuing_cards: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cards.
                """
                manage_issuing_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing disputes.
                """
                manage_payment_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing payment disputes.
                """
                manage_refund_payments: Literal["disabled", "enabled"]
                """
                Whether to allow refunding payments.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class InstantPayoutsPromotion(StripeObject):
            class Scopes(StripeObject):
                create_instant_payouts: Optional[
                    Literal["disabled", "enabled", "use_dashboard_rules"]
                ]
                """
                Controls whether creating instant payouts is enabled, disabled, or determined by Dashboard rules.
                """
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class InvoiceHistory(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class IssuingCard(StripeObject):
            class Scopes(StripeObject):
                manage_issuing_cardholders: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cardholders.
                """
                manage_issuing_cards: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cards.
                """
                manage_issuing_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing disputes.
                """
                manage_issuing_spending_controls: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing Issuing spending controls.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class IssuingCardsList(StripeObject):
            class Scopes(StripeObject):
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_issuing_cardholders: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cardholders.
                """
                manage_issuing_cards: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing cards.
                """
                manage_issuing_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Issuing disputes.
                """
                manage_issuing_spending_controls: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing Issuing spending controls.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class NetworkCostPassthroughReport(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class NotificationBanner(StripeObject):
            class Scopes(StripeObject):
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PaymentDetails(StripeObject):
            class Scopes(StripeObject):
                capture_payments: Literal["disabled", "enabled"]
                """
                Whether to allow capturing payments.
                """
                manage_destination_on_behalf_of_charges: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing destination and on-behalf-of charges.
                """
                manage_payment_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing payment disputes.
                """
                manage_refund_payments: Literal["disabled", "enabled"]
                """
                Whether to allow refunding payments.
                """
                manage_smart_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Smart Disputes.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PaymentDisputes(StripeObject):
            class Scopes(StripeObject):
                manage_destination_on_behalf_of_charges: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing destination and on-behalf-of charges.
                """
                manage_payment_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing payment disputes.
                """
                manage_refund_payments: Literal["disabled", "enabled"]
                """
                Whether to allow refunding payments.
                """
                manage_smart_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Smart Disputes.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PaymentMethodSettings(StripeObject):
            class Scopes(StripeObject):
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class Payments(StripeObject):
            class Scopes(StripeObject):
                capture_payments: Literal["disabled", "enabled"]
                """
                Whether to allow capturing payments.
                """
                manage_destination_on_behalf_of_charges: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to allow managing destination and on-behalf-of charges.
                """
                manage_payment_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing payment disputes.
                """
                manage_refund_payments: Literal["disabled", "enabled"]
                """
                Whether to allow refunding payments.
                """
                manage_smart_disputes: Literal["disabled", "enabled"]
                """
                Whether to allow managing Smart Disputes.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PayoutDetails(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PayoutReconciliationReport(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class Payouts(StripeObject):
            class Scopes(StripeObject):
                create_instant_payouts: Optional[
                    Literal["disabled", "enabled", "use_dashboard_rules"]
                ]
                """
                Controls whether creating instant payouts is enabled, disabled, or determined by Dashboard rules.
                """
                create_payout_schedule: Literal["disabled", "enabled"]
                """
                Whether to allow changing the payout schedule.
                """
                create_standard_payouts: Literal["disabled", "enabled"]
                """
                Whether to allow creating standard payouts.
                """
                disable_stripe_user_authentication: Literal[
                    "disabled", "enabled"
                ]
                """
                Whether to disable Stripe user authentication in the enabled components.
                """
                manage_payout_methods: Literal["disabled", "enabled"]
                """
                Whether to allow managing payout methods.
                """

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class PayoutsList(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class ProductTaxCodeSelector(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class ReportingChart(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class TaxRegistrations(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class TaxSettings(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class TaxThresholdMonitoring(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class TerminalHardwareOrders(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        class TerminalHardwareShop(StripeObject):
            class Scopes(StripeObject):
                pass

            enabled: bool
            """
            Whether this embedded component is enabled.
            """
            scopes: Scopes
            """
            The scopes available to this embedded component.
            """
            _inner_class_types = {"scopes": Scopes}

        account_management: AccountManagement
        """
        Settings for the Account Management embedded component.
        """
        account_onboarding: AccountOnboarding
        """
        Settings for the Account Onboarding embedded component.
        """
        agentic_commerce_settings: AgenticCommerceSettings
        """
        Settings for the Agentic Commerce Settings embedded component.
        """
        app_install: AppInstall
        """
        Settings for the App Install embedded component.
        """
        app_viewport: AppViewport
        """
        Settings for the App Viewport embedded component.
        """
        balance_report: BalanceReport
        """
        Settings for the Balance Report embedded component.
        """
        balances: Balances
        """
        Settings for the Balances embedded component.
        """
        bills: Bills
        """
        Settings for the Bills embedded component.
        """
        capital_financing: CapitalFinancing
        """
        Settings for the Capital Financing embedded component.
        """
        capital_financing_application: CapitalFinancingApplication
        """
        Settings for the Capital Financing Application embedded component.
        """
        capital_financing_promotion: CapitalFinancingPromotion
        """
        Settings for the Capital Financing Promotion embedded component.
        """
        check_scanning: CheckScanning
        """
        Settings for the Check Scanning embedded component.
        """
        disputes_list: DisputesList
        """
        Settings for the Disputes List embedded component.
        """
        documents: Documents
        """
        Settings for the Documents embedded component.
        """
        export_tax_transactions: ExportTaxTransactions
        """
        Settings for the Export Tax Transactions embedded component.
        """
        financial_account_rewards: FinancialAccountRewards
        """
        Settings for the Financial Account Rewards embedded component.
        """
        financial_accounts: FinancialAccounts
        """
        Settings for the Financial Accounts embedded component.
        """
        financial_accounts_transactions: FinancialAccountsTransactions
        """
        Settings for the Financial Accounts Transactions embedded component.
        """
        instant_payouts_promotion: InstantPayoutsPromotion
        """
        Settings for the Instant Payouts Promotion embedded component.
        """
        invoice_history: InvoiceHistory
        """
        Settings for the Invoice History embedded component.
        """
        issuing_card: IssuingCard
        """
        Settings for the Issuing Card embedded component.
        """
        issuing_cards_list: IssuingCardsList
        """
        Settings for the Issuing Cards List embedded component.
        """
        network_cost_passthrough_report: NetworkCostPassthroughReport
        """
        Settings for the Network Cost Passthrough Report embedded component.
        """
        notification_banner: NotificationBanner
        """
        Settings for the Notification Banner embedded component.
        """
        payment_details: PaymentDetails
        """
        Settings for the Payment Details embedded component.
        """
        payment_disputes: PaymentDisputes
        """
        Settings for the Payment Disputes embedded component.
        """
        payment_method_settings: PaymentMethodSettings
        """
        Settings for the Payment Method Settings embedded component.
        """
        payments: Payments
        """
        Settings for the Payments embedded component.
        """
        payout_details: PayoutDetails
        """
        Settings for the Payout Details embedded component.
        """
        payout_reconciliation_report: PayoutReconciliationReport
        """
        Settings for the Payout Reconciliation Report embedded component.
        """
        payouts: Payouts
        """
        Settings for the Payouts embedded component.
        """
        payouts_list: PayoutsList
        """
        Settings for the Payouts List embedded component.
        """
        product_tax_code_selector: ProductTaxCodeSelector
        """
        Settings for the Product Tax Code Selector embedded component.
        """
        reporting_chart: ReportingChart
        """
        Settings for the Reporting Chart embedded component.
        """
        tax_registrations: TaxRegistrations
        """
        Settings for the Tax Registrations embedded component.
        """
        tax_settings: TaxSettings
        """
        Settings for the Tax Settings embedded component.
        """
        tax_threshold_monitoring: TaxThresholdMonitoring
        """
        Settings for the Tax Threshold Monitoring embedded component.
        """
        terminal_hardware_orders: TerminalHardwareOrders
        """
        Settings for the Terminal Hardware Orders embedded component.
        """
        terminal_hardware_shop: TerminalHardwareShop
        """
        Settings for the Terminal Hardware Shop embedded component.
        """
        _inner_class_types = {
            "account_management": AccountManagement,
            "account_onboarding": AccountOnboarding,
            "agentic_commerce_settings": AgenticCommerceSettings,
            "app_install": AppInstall,
            "app_viewport": AppViewport,
            "balance_report": BalanceReport,
            "balances": Balances,
            "bills": Bills,
            "capital_financing": CapitalFinancing,
            "capital_financing_application": CapitalFinancingApplication,
            "capital_financing_promotion": CapitalFinancingPromotion,
            "check_scanning": CheckScanning,
            "disputes_list": DisputesList,
            "documents": Documents,
            "export_tax_transactions": ExportTaxTransactions,
            "financial_account_rewards": FinancialAccountRewards,
            "financial_accounts": FinancialAccounts,
            "financial_accounts_transactions": FinancialAccountsTransactions,
            "instant_payouts_promotion": InstantPayoutsPromotion,
            "invoice_history": InvoiceHistory,
            "issuing_card": IssuingCard,
            "issuing_cards_list": IssuingCardsList,
            "network_cost_passthrough_report": NetworkCostPassthroughReport,
            "notification_banner": NotificationBanner,
            "payment_details": PaymentDetails,
            "payment_disputes": PaymentDisputes,
            "payment_method_settings": PaymentMethodSettings,
            "payments": Payments,
            "payout_details": PayoutDetails,
            "payout_reconciliation_report": PayoutReconciliationReport,
            "payouts": Payouts,
            "payouts_list": PayoutsList,
            "product_tax_code_selector": ProductTaxCodeSelector,
            "reporting_chart": ReportingChart,
            "tax_registrations": TaxRegistrations,
            "tax_settings": TaxSettings,
            "tax_threshold_monitoring": TaxThresholdMonitoring,
            "terminal_hardware_orders": TerminalHardwareOrders,
            "terminal_hardware_shop": TerminalHardwareShop,
        }

    account: str
    """
    The ID of the account this Account Session grants access to.
    """
    client_secret: str
    """
    The client secret used to initialize Connect embedded components. Do not log it or expose it to
    anyone other than the intended user.
    """
    components: Components
    """
    Settings and scopes for each embedded component in this Account Session.
    """
    created: str
    """
    The time at which the Account Session was created.
    """
    expires_at: str
    """
    The time at which the Account Session expires.
    """
    id: str
    """
    Unique identifier for the Account Session.
    """
    livemode: bool
    """
    Has the value true if the object exists in live mode or false if the object exists in test mode.
    """
    object: Literal["v2.core.account_session"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"components": Components}
