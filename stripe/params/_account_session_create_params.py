# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountSessionCreateParams(RequestOptions):
    account: str
    """
    The identifier of the account to create an Account Session for.
    """
    components: "AccountSessionCreateParamsComponents"
    """
    Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class AccountSessionCreateParamsComponents(TypedDict):
    account_management: NotRequired[
        "AccountSessionCreateParamsComponentsAccountManagement"
    ]
    """
    Configuration for the [account management](https://docs.stripe.com/connect/supported-embedded-components/account-management/) embedded component.
    """
    account_onboarding: NotRequired[
        "AccountSessionCreateParamsComponentsAccountOnboarding"
    ]
    """
    Configuration for the [account onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding/) embedded component.
    """
    app_install: NotRequired["AccountSessionCreateParamsComponentsAppInstall"]
    """
    Configuration for the [app install](https://docs.stripe.com/connect/supported-embedded-components/app-install/) embedded component.
    """
    app_viewport: NotRequired[
        "AccountSessionCreateParamsComponentsAppViewport"
    ]
    """
    Configuration for the [app viewport](https://docs.stripe.com/connect/supported-embedded-components/app-viewport/) embedded component.
    """
    balances: NotRequired["AccountSessionCreateParamsComponentsBalances"]
    """
    Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/) embedded component.
    """
    capital_financing: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancing"
    ]
    """
    Configuration for the [Capital financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing/) embedded component.
    """
    capital_financing_application: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingApplication"
    ]
    """
    Configuration for the [Capital financing application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application/) embedded component.
    """
    capital_financing_promotion: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingPromotion"
    ]
    """
    Configuration for the [Capital financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion/) embedded component.
    """
    capital_overview: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalOverview"
    ]
    """
    Configuration for the [Capital overview](https://docs.stripe.com/connect/supported-embedded-components/capital-overview/) embedded component.
    """
    check_scanning: NotRequired[
        "AccountSessionCreateParamsComponentsCheckScanning"
    ]
    """
    Configuration for the [check scanning](https://docs.stripe.com/connect/supported-embedded-components/check-scanning/) embedded component.
    """
    disputes_list: NotRequired[
        "AccountSessionCreateParamsComponentsDisputesList"
    ]
    """
    Configuration for the [disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list/) embedded component.
    """
    documents: NotRequired["AccountSessionCreateParamsComponentsDocuments"]
    """
    Configuration for the [documents](https://docs.stripe.com/connect/supported-embedded-components/documents/) embedded component.
    """
    export_tax_transactions: NotRequired[
        "AccountSessionCreateParamsComponentsExportTaxTransactions"
    ]
    """
    Configuration for the [export tax transactions](https://docs.stripe.com/connect/supported-embedded-components/export-tax-transactions/) embedded component.
    """
    financial_account: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccount"
    ]
    """
    Configuration for the [financial account](https://docs.stripe.com/connect/supported-embedded-components/financial-account/) embedded component.
    """
    financial_account_transactions: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccountTransactions"
    ]
    """
    Configuration for the [financial account transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions/) embedded component.
    """
    instant_payouts_promotion: NotRequired[
        "AccountSessionCreateParamsComponentsInstantPayoutsPromotion"
    ]
    """
    Configuration for the [instant payouts promotion](https://docs.stripe.com/connect/supported-embedded-components/instant-payouts-promotion/) embedded component.
    """
    issuing_card: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCard"
    ]
    """
    Configuration for the [issuing card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card/) embedded component.
    """
    issuing_cards_list: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCardsList"
    ]
    """
    Configuration for the [issuing cards list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list/) embedded component.
    """
    notification_banner: NotRequired[
        "AccountSessionCreateParamsComponentsNotificationBanner"
    ]
    """
    Configuration for the [notification banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner/) embedded component.
    """
    payment_details: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDetails"
    ]
    """
    Configuration for the [payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details/) embedded component.
    """
    payment_disputes: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDisputes"
    ]
    """
    Configuration for the [payment disputes](https://docs.stripe.com/connect/supported-embedded-components/payment-disputes/) embedded component.
    """
    payment_method_settings: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentMethodSettings"
    ]
    """
    Configuration for the [payment method settings](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings/) embedded component.
    """
    payments: NotRequired["AccountSessionCreateParamsComponentsPayments"]
    """
    Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/) embedded component.
    """
    payout_details: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutDetails"
    ]
    """
    Configuration for the [payout details](https://docs.stripe.com/connect/supported-embedded-components/payout-details/) embedded component.
    """
    payouts: NotRequired["AccountSessionCreateParamsComponentsPayouts"]
    """
    Configuration for the [payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts/) embedded component.
    """
    payouts_list: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutsList"
    ]
    """
    Configuration for the [payouts list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list/) embedded component.
    """
    product_tax_code_selector: NotRequired[
        "AccountSessionCreateParamsComponentsProductTaxCodeSelector"
    ]
    """
    Configuration for the [product tax code selector](https://docs.stripe.com/connect/supported-embedded-components/product-tax-code-selector/) embedded component.
    """
    recipients: NotRequired["AccountSessionCreateParamsComponentsRecipients"]
    """
    Configuration for the [recipients](https://docs.stripe.com/connect/supported-embedded-components/recipients/) embedded component.
    """
    reporting_chart: NotRequired[
        "AccountSessionCreateParamsComponentsReportingChart"
    ]
    """
    Configuration for the [reporting chart](https://docs.stripe.com/connect/supported-embedded-components/reporting-chart/) embedded component.
    """
    tax_registrations: NotRequired[
        "AccountSessionCreateParamsComponentsTaxRegistrations"
    ]
    """
    Configuration for the [tax registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations/) embedded component.
    """
    tax_settings: NotRequired[
        "AccountSessionCreateParamsComponentsTaxSettings"
    ]
    """
    Configuration for the [tax settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings/) embedded component.
    """
    tax_threshold_monitoring: NotRequired[
        "AccountSessionCreateParamsComponentsTaxThresholdMonitoring"
    ]
    """
    Configuration for the [tax threshold monitoring](https://docs.stripe.com/connect/supported-embedded-components/tax-threshold-monitoring/) embedded component.
    """


class AccountSessionCreateParamsComponentsAccountManagement(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsAccountManagementFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsAccountManagementFeatures(TypedDict):
    disable_stripe_user_authentication: NotRequired[bool]
    """
    Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
    """
    external_account_collection: NotRequired[bool]
    """
    Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
    """


class AccountSessionCreateParamsComponentsAccountOnboarding(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsAccountOnboardingFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsAccountOnboardingFeatures(TypedDict):
    disable_stripe_user_authentication: NotRequired[bool]
    """
    Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
    """
    external_account_collection: NotRequired[bool]
    """
    Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
    """


class AccountSessionCreateParamsComponentsAppInstall(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsAppInstallFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsAppInstallFeatures(TypedDict):
    allowed_apps: NotRequired["Literal['']|List[str]"]
    """
    The list of apps allowed to be enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsAppViewport(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsAppViewportFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsAppViewportFeatures(TypedDict):
    allowed_apps: NotRequired["Literal['']|List[str]"]
    """
    The list of apps allowed to be enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsBalances(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsBalancesFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsBalancesFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsCapitalFinancing(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsCapitalFinancingFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsCapitalFinancingApplication(
    TypedDict,
):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingApplicationFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsCapitalFinancingApplicationFeatures(
    TypedDict,
):
    pass


class AccountSessionCreateParamsComponentsCapitalFinancingPromotion(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalFinancingPromotionFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsCapitalFinancingPromotionFeatures(
    TypedDict,
):
    pass


class AccountSessionCreateParamsComponentsCapitalOverview(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsCapitalOverviewFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsCapitalOverviewFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsCheckScanning(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsCheckScanningFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsCheckScanningFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsDisputesList(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsDisputesListFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsDisputesListFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsDocuments(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsDocumentsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsDocumentsFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsExportTaxTransactions(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsExportTaxTransactionsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsExportTaxTransactionsFeatures(
    TypedDict,
):
    pass


class AccountSessionCreateParamsComponentsFinancialAccount(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccountFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsFinancialAccountFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsFinancialAccountTransactions(
    TypedDict,
):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsFinancialAccountTransactionsFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsFinancialAccountTransactionsFeatures(
    TypedDict,
):
    card_spend_dispute_management: NotRequired[bool]
    """
    Whether to allow card spend dispute management features.
    """


class AccountSessionCreateParamsComponentsInstantPayoutsPromotion(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsInstantPayoutsPromotionFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsInstantPayoutsPromotionFeatures(
    TypedDict,
):
    disable_stripe_user_authentication: NotRequired[bool]
    """
    Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
    """
    external_account_collection: NotRequired[bool]
    """
    Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
    """
    instant_payouts: NotRequired[bool]
    """
    Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
    """


class AccountSessionCreateParamsComponentsIssuingCard(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCardFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsIssuingCardFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsIssuingCardsList(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsIssuingCardsListFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsIssuingCardsListFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsNotificationBanner(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsNotificationBannerFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsNotificationBannerFeatures(
    TypedDict
):
    disable_stripe_user_authentication: NotRequired[bool]
    """
    Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
    """
    external_account_collection: NotRequired[bool]
    """
    Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
    """


class AccountSessionCreateParamsComponentsPaymentDetails(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDetailsFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsPaymentDetailsFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsPaymentDisputes(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentDisputesFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsPaymentDisputesFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsPaymentMethodSettings(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentMethodSettingsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsPaymentMethodSettingsFeatures(
    TypedDict,
):
    pass


class AccountSessionCreateParamsComponentsPayments(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPaymentsFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsPaymentsFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsPayoutDetails(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutDetailsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsPayoutDetailsFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsPayouts(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutsFeatures"
    ]
    """
    The list of features enabled in the embedded component.
    """


class AccountSessionCreateParamsComponentsPayoutsFeatures(TypedDict):
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


class AccountSessionCreateParamsComponentsPayoutsList(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsPayoutsListFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsPayoutsListFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsProductTaxCodeSelector(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsProductTaxCodeSelectorFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsProductTaxCodeSelectorFeatures(
    TypedDict,
):
    pass


class AccountSessionCreateParamsComponentsRecipients(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsRecipientsFeatures"
    ]


class AccountSessionCreateParamsComponentsRecipientsFeatures(TypedDict):
    send_money: NotRequired[bool]
    """
    Whether to allow sending money.
    """


class AccountSessionCreateParamsComponentsReportingChart(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsReportingChartFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsReportingChartFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsTaxRegistrations(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsTaxRegistrationsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsTaxRegistrationsFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsTaxSettings(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsTaxSettingsFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsTaxSettingsFeatures(TypedDict):
    pass


class AccountSessionCreateParamsComponentsTaxThresholdMonitoring(TypedDict):
    enabled: bool
    """
    Whether the embedded component is enabled.
    """
    features: NotRequired[
        "AccountSessionCreateParamsComponentsTaxThresholdMonitoringFeatures"
    ]
    """
    An empty list, because this embedded component has no features.
    """


class AccountSessionCreateParamsComponentsTaxThresholdMonitoringFeatures(
    TypedDict,
):
    pass
