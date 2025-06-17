# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_session import AccountSession
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class AccountSessionService(StripeService):
    class CreateParams(TypedDict):
        account: str
        """
        The identifier of the account to create an Account Session for.
        """
        components: "AccountSessionService.CreateParamsComponents"
        """
        Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParamsComponents(TypedDict):
        account_management: NotRequired[
            "AccountSessionService.CreateParamsComponentsAccountManagement"
        ]
        """
        Configuration for the [account management](https://docs.stripe.com/connect/supported-embedded-components/account-management/) embedded component.
        """
        account_onboarding: NotRequired[
            "AccountSessionService.CreateParamsComponentsAccountOnboarding"
        ]
        """
        Configuration for the [account onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding/) embedded component.
        """
        app_install: NotRequired[
            "AccountSessionService.CreateParamsComponentsAppInstall"
        ]
        """
        Configuration for the [app install](https://docs.stripe.com/connect/supported-embedded-components/app-install/) embedded component.
        """
        app_viewport: NotRequired[
            "AccountSessionService.CreateParamsComponentsAppViewport"
        ]
        """
        Configuration for the [app viewport](https://docs.stripe.com/connect/supported-embedded-components/app-viewport/) embedded component.
        """
        balances: NotRequired[
            "AccountSessionService.CreateParamsComponentsBalances"
        ]
        """
        Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/) embedded component.
        """
        capital_financing: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancing"
        ]
        """
        Configuration for the [Capital financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing/) embedded component.
        """
        capital_financing_application: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingApplication"
        ]
        """
        Configuration for the [Capital financing application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application/) embedded component.
        """
        capital_financing_promotion: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingPromotion"
        ]
        """
        Configuration for the [Capital financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion/) embedded component.
        """
        capital_overview: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalOverview"
        ]
        """
        Configuration for the [Capital overview](https://docs.stripe.com/connect/supported-embedded-components/capital-overview/) embedded component.
        """
        disputes_list: NotRequired[
            "AccountSessionService.CreateParamsComponentsDisputesList"
        ]
        """
        Configuration for the [disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list/) embedded component.
        """
        documents: NotRequired[
            "AccountSessionService.CreateParamsComponentsDocuments"
        ]
        """
        Configuration for the [documents](https://docs.stripe.com/connect/supported-embedded-components/documents/) embedded component.
        """
        export_tax_transactions: NotRequired[
            "AccountSessionService.CreateParamsComponentsExportTaxTransactions"
        ]
        """
        Configuration for the [export tax transactions](https://docs.stripe.com/connect/supported-embedded-components/export-tax-transactions/) embedded component.
        """
        financial_account: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccount"
        ]
        """
        Configuration for the [financial account](https://docs.stripe.com/connect/supported-embedded-components/financial-account/) embedded component.
        """
        financial_account_transactions: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccountTransactions"
        ]
        """
        Configuration for the [financial account transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions/) embedded component.
        """
        issuing_card: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCard"
        ]
        """
        Configuration for the [issuing card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card/) embedded component.
        """
        issuing_cards_list: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCardsList"
        ]
        """
        Configuration for the [issuing cards list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list/) embedded component.
        """
        notification_banner: NotRequired[
            "AccountSessionService.CreateParamsComponentsNotificationBanner"
        ]
        """
        Configuration for the [notification banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner/) embedded component.
        """
        payment_details: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentDetails"
        ]
        """
        Configuration for the [payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details/) embedded component.
        """
        payment_disputes: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentDisputes"
        ]
        """
        Configuration for the [payment disputes](https://docs.stripe.com/connect/supported-embedded-components/payment-disputes/) embedded component.
        """
        payment_method_settings: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentMethodSettings"
        ]
        """
        Configuration for the [payment method settings](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings/) embedded component.
        """
        payments: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayments"
        ]
        """
        Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/) embedded component.
        """
        payouts: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayouts"
        ]
        """
        Configuration for the [payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts/) embedded component.
        """
        payouts_list: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayoutsList"
        ]
        """
        Configuration for the [payouts list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list/) embedded component.
        """
        product_tax_code_selector: NotRequired[
            "AccountSessionService.CreateParamsComponentsProductTaxCodeSelector"
        ]
        """
        Configuration for the [product tax code selector](https://docs.stripe.com/connect/supported-embedded-components/product-tax-code-selector/) embedded component.
        """
        recipients: NotRequired[
            "AccountSessionService.CreateParamsComponentsRecipients"
        ]
        """
        Configuration for the [recipients](https://docs.stripe.com/connect/supported-embedded-components/recipients/) embedded component.
        """
        reporting_chart: NotRequired[
            "AccountSessionService.CreateParamsComponentsReportingChart"
        ]
        """
        Configuration for the [reporting chart](https://docs.stripe.com/connect/supported-embedded-components/reporting-chart/) embedded component.
        """
        tax_registrations: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxRegistrations"
        ]
        """
        Configuration for the [tax registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations/) embedded component.
        """
        tax_settings: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxSettings"
        ]
        """
        Configuration for the [tax settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings/) embedded component.
        """
        tax_threshold_monitoring: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxThresholdMonitoring"
        ]
        """
        Configuration for the [tax threshold monitoring](https://docs.stripe.com/connect/supported-embedded-components/tax-threshold-monitoring/) embedded component.
        """

    class CreateParamsComponentsAccountManagement(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsAccountManagementFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsAccountManagementFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """

    class CreateParamsComponentsAccountOnboarding(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsAccountOnboardingFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsAccountOnboardingFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """

    class CreateParamsComponentsAppInstall(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsAppInstallFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsAppInstallFeatures(TypedDict):
        allowed_apps: NotRequired["Literal['']|List[str]"]
        """
        The list of apps allowed to be enabled in the embedded component.
        """

    class CreateParamsComponentsAppViewport(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsAppViewportFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsAppViewportFeatures(TypedDict):
        allowed_apps: NotRequired["Literal['']|List[str]"]
        """
        The list of apps allowed to be enabled in the embedded component.
        """

    class CreateParamsComponentsBalances(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsBalancesFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsBalancesFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        edit_payout_schedule: NotRequired[bool]
        """
        Whether to allow payout schedule to be changed. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """
        instant_payouts: NotRequired[bool]
        """
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """
        standard_payouts: NotRequired[bool]
        """
        Whether to allow creation of standard payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """

    class CreateParamsComponentsCapitalFinancing(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsCapitalFinancingApplication(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingApplicationFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsCapitalFinancingApplicationFeatures(TypedDict):
        pass

    class CreateParamsComponentsCapitalFinancingFeatures(TypedDict):
        pass

    class CreateParamsComponentsCapitalFinancingPromotion(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingPromotionFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsCapitalFinancingPromotionFeatures(TypedDict):
        pass

    class CreateParamsComponentsCapitalOverview(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalOverviewFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsCapitalOverviewFeatures(TypedDict):
        pass

    class CreateParamsComponentsDisputesList(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsDisputesListFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsDisputesListFeatures(TypedDict):
        capture_payments: NotRequired[bool]
        """
        Whether to allow capturing and cancelling payment intents. This is `true` by default.
        """
        destination_on_behalf_of_charge_management: NotRequired[bool]
        """
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether sending refunds is enabled. This is `true` by default.
        """

    class CreateParamsComponentsDocuments(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsDocumentsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsDocumentsFeatures(TypedDict):
        pass

    class CreateParamsComponentsExportTaxTransactions(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsExportTaxTransactionsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsExportTaxTransactionsFeatures(TypedDict):
        pass

    class CreateParamsComponentsFinancialAccount(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccountFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsFinancialAccountFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """
        send_money: NotRequired[bool]
        """
        Whether to allow sending money.
        """
        transfer_balance: NotRequired[bool]
        """
        Whether to allow transferring balance.
        """

    class CreateParamsComponentsFinancialAccountTransactions(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccountTransactionsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsFinancialAccountTransactionsFeatures(
        TypedDict
    ):
        card_spend_dispute_management: NotRequired[bool]
        """
        Whether to allow card spend dispute management features.
        """

    class CreateParamsComponentsIssuingCard(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCardFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsIssuingCardFeatures(TypedDict):
        card_management: NotRequired[bool]
        """
        Whether to allow card management features.
        """
        card_spend_dispute_management: NotRequired[bool]
        """
        Whether to allow card spend dispute management features.
        """
        cardholder_management: NotRequired[bool]
        """
        Whether to allow cardholder management features.
        """
        spend_control_management: NotRequired[bool]
        """
        Whether to allow spend control management features.
        """

    class CreateParamsComponentsIssuingCardsList(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCardsListFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsIssuingCardsListFeatures(TypedDict):
        card_management: NotRequired[bool]
        """
        Whether to allow card management features.
        """
        card_spend_dispute_management: NotRequired[bool]
        """
        Whether to allow card spend dispute management features.
        """
        cardholder_management: NotRequired[bool]
        """
        Whether to allow cardholder management features.
        """
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        spend_control_management: NotRequired[bool]
        """
        Whether to allow spend control management features.
        """

    class CreateParamsComponentsNotificationBanner(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsNotificationBannerFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsNotificationBannerFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """

    class CreateParamsComponentsPaymentDetails(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentDetailsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentDetailsFeatures(TypedDict):
        capture_payments: NotRequired[bool]
        """
        Whether to allow capturing and cancelling payment intents. This is `true` by default.
        """
        destination_on_behalf_of_charge_management: NotRequired[bool]
        """
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether sending refunds is enabled. This is `true` by default.
        """

    class CreateParamsComponentsPaymentDisputes(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentDisputesFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentDisputesFeatures(TypedDict):
        destination_on_behalf_of_charge_management: NotRequired[bool]
        """
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether sending refunds is enabled. This is `true` by default.
        """

    class CreateParamsComponentsPaymentMethodSettings(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentMethodSettingsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentMethodSettingsFeatures(TypedDict):
        pass

    class CreateParamsComponentsPayments(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPaymentsFeatures(TypedDict):
        capture_payments: NotRequired[bool]
        """
        Whether to allow capturing and cancelling payment intents. This is `true` by default.
        """
        destination_on_behalf_of_charge_management: NotRequired[bool]
        """
        Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether sending refunds is enabled. This is `true` by default.
        """

    class CreateParamsComponentsPayouts(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayoutsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPayoutsFeatures(TypedDict):
        disable_stripe_user_authentication: NotRequired[bool]
        """
        Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
        """
        edit_payout_schedule: NotRequired[bool]
        """
        Whether to allow payout schedule to be changed. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """
        external_account_collection: NotRequired[bool]
        """
        Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
        """
        instant_payouts: NotRequired[bool]
        """
        Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """
        standard_payouts: NotRequired[bool]
        """
        Whether to allow creation of standard payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
        """

    class CreateParamsComponentsPayoutsList(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayoutsListFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsPayoutsListFeatures(TypedDict):
        pass

    class CreateParamsComponentsProductTaxCodeSelector(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsProductTaxCodeSelectorFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsProductTaxCodeSelectorFeatures(TypedDict):
        pass

    class CreateParamsComponentsRecipients(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsRecipientsFeatures"
        ]

    class CreateParamsComponentsRecipientsFeatures(TypedDict):
        send_money: NotRequired[bool]
        """
        Whether to allow sending money.
        """

    class CreateParamsComponentsReportingChart(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsReportingChartFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsReportingChartFeatures(TypedDict):
        pass

    class CreateParamsComponentsTaxRegistrations(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxRegistrationsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsTaxRegistrationsFeatures(TypedDict):
        pass

    class CreateParamsComponentsTaxSettings(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxSettingsFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsTaxSettingsFeatures(TypedDict):
        pass

    class CreateParamsComponentsTaxThresholdMonitoring(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsTaxThresholdMonitoringFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsTaxThresholdMonitoringFeatures(TypedDict):
        pass

    def create(
        self,
        params: "AccountSessionService.CreateParams",
        options: RequestOptions = {},
    ) -> AccountSession:
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
        return cast(
            AccountSession,
            self._request(
                "post",
                "/v1/account_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountSessionService.CreateParams",
        options: RequestOptions = {},
    ) -> AccountSession:
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
        return cast(
            AccountSession,
            await self._request_async(
                "post",
                "/v1/account_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )
