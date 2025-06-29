# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class AccountSession(CreateableAPIResource["AccountSession"]):
    """
    An AccountSession allows a Connect platform to grant access to a connected account in Connect embedded components.

    We recommend that you create an AccountSession each time you need to display an embedded component
    to your user. Do not save AccountSessions to your database as they expire relatively
    quickly, and cannot be used more than once.

    Related guide: [Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components)
    """

    OBJECT_NAME: ClassVar[Literal["account_session"]] = "account_session"

    class Components(StripeObject):
        class AccountManagement(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class AccountOnboarding(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Balances(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                edit_payout_schedule: bool
                """
                Whether to allow payout schedule to be changed. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """
                instant_payouts: bool
                """
                Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """
                standard_payouts: bool
                """
                Whether to allow creation of standard payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class CapitalFinancing(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class CapitalFinancingApplication(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class CapitalFinancingPromotion(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class DisputesList(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                """
                Whether to allow capturing and cancelling payment intents. This is `true` by default.
                """
                destination_on_behalf_of_charge_management: bool
                """
                Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
                """
                dispute_management: bool
                """
                Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether sending refunds is enabled. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Documents(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class FinancialAccount(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """
                send_money: bool
                """
                Whether to allow sending money.
                """
                transfer_balance: bool
                """
                Whether to allow transferring balance.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class FinancialAccountTransactions(StripeObject):
            class Features(StripeObject):
                card_spend_dispute_management: bool
                """
                Whether to allow card spend dispute management features.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class IssuingCard(StripeObject):
            class Features(StripeObject):
                card_management: bool
                """
                Whether to allow card management features.
                """
                card_spend_dispute_management: bool
                """
                Whether to allow card spend dispute management features.
                """
                cardholder_management: bool
                """
                Whether to allow cardholder management features.
                """
                spend_control_management: bool
                """
                Whether to allow spend control management features.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class IssuingCardsList(StripeObject):
            class Features(StripeObject):
                card_management: bool
                """
                Whether to allow card management features.
                """
                card_spend_dispute_management: bool
                """
                Whether to allow card spend dispute management features.
                """
                cardholder_management: bool
                """
                Whether to allow cardholder management features.
                """
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                spend_control_management: bool
                """
                Whether to allow spend control management features.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class NotificationBanner(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class PaymentDetails(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                """
                Whether to allow capturing and cancelling payment intents. This is `true` by default.
                """
                destination_on_behalf_of_charge_management: bool
                """
                Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
                """
                dispute_management: bool
                """
                Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether sending refunds is enabled. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class PaymentDisputes(StripeObject):
            class Features(StripeObject):
                destination_on_behalf_of_charge_management: bool
                """
                Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
                """
                dispute_management: bool
                """
                Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether sending refunds is enabled. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Payments(StripeObject):
            class Features(StripeObject):
                capture_payments: bool
                """
                Whether to allow capturing and cancelling payment intents. This is `true` by default.
                """
                destination_on_behalf_of_charge_management: bool
                """
                Whether connected accounts can manage destination charges that are created on behalf of them. This is `false` by default.
                """
                dispute_management: bool
                """
                Whether responding to disputes is enabled, including submitting evidence and accepting disputes. This is `true` by default.
                """
                refund_management: bool
                """
                Whether sending refunds is enabled. This is `true` by default.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class Payouts(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                edit_payout_schedule: bool
                """
                Whether to allow payout schedule to be changed. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """
                instant_payouts: bool
                """
                Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """
                standard_payouts: bool
                """
                Whether to allow creation of standard payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
                """

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class PayoutsList(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class TaxRegistrations(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class TaxSettings(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        account_management: AccountManagement
        account_onboarding: AccountOnboarding
        balances: Balances
        capital_financing: Optional[CapitalFinancing]
        capital_financing_application: Optional[CapitalFinancingApplication]
        capital_financing_promotion: Optional[CapitalFinancingPromotion]
        disputes_list: DisputesList
        documents: Documents
        financial_account: FinancialAccount
        financial_account_transactions: FinancialAccountTransactions
        issuing_card: IssuingCard
        issuing_cards_list: IssuingCardsList
        notification_banner: NotificationBanner
        payment_details: PaymentDetails
        payment_disputes: PaymentDisputes
        payments: Payments
        payouts: Payouts
        payouts_list: PayoutsList
        tax_registrations: TaxRegistrations
        tax_settings: TaxSettings
        _inner_class_types = {
            "account_management": AccountManagement,
            "account_onboarding": AccountOnboarding,
            "balances": Balances,
            "capital_financing": CapitalFinancing,
            "capital_financing_application": CapitalFinancingApplication,
            "capital_financing_promotion": CapitalFinancingPromotion,
            "disputes_list": DisputesList,
            "documents": Documents,
            "financial_account": FinancialAccount,
            "financial_account_transactions": FinancialAccountTransactions,
            "issuing_card": IssuingCard,
            "issuing_cards_list": IssuingCardsList,
            "notification_banner": NotificationBanner,
            "payment_details": PaymentDetails,
            "payment_disputes": PaymentDisputes,
            "payments": Payments,
            "payouts": Payouts,
            "payouts_list": PayoutsList,
            "tax_registrations": TaxRegistrations,
            "tax_settings": TaxSettings,
        }

    class CreateParams(RequestOptions):
        account: str
        """
        The identifier of the account to create an Account Session for.
        """
        components: "AccountSession.CreateParamsComponents"
        """
        Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParamsComponents(TypedDict):
        account_management: NotRequired[
            "AccountSession.CreateParamsComponentsAccountManagement"
        ]
        """
        Configuration for the [account management](https://docs.stripe.com/connect/supported-embedded-components/account-management/) embedded component.
        """
        account_onboarding: NotRequired[
            "AccountSession.CreateParamsComponentsAccountOnboarding"
        ]
        """
        Configuration for the [account onboarding](https://docs.stripe.com/connect/supported-embedded-components/account-onboarding/) embedded component.
        """
        app_install: NotRequired[
            "AccountSession.CreateParamsComponentsAppInstall"
        ]
        """
        Configuration for the [app install](https://docs.stripe.com/connect/supported-embedded-components/app-install/) embedded component.
        """
        app_viewport: NotRequired[
            "AccountSession.CreateParamsComponentsAppViewport"
        ]
        """
        Configuration for the [app viewport](https://docs.stripe.com/connect/supported-embedded-components/app-viewport/) embedded component.
        """
        balances: NotRequired["AccountSession.CreateParamsComponentsBalances"]
        """
        Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/) embedded component.
        """
        capital_financing: NotRequired[
            "AccountSession.CreateParamsComponentsCapitalFinancing"
        ]
        """
        Configuration for the [Capital financing](https://docs.stripe.com/connect/supported-embedded-components/capital-financing/) embedded component.
        """
        capital_financing_application: NotRequired[
            "AccountSession.CreateParamsComponentsCapitalFinancingApplication"
        ]
        """
        Configuration for the [Capital financing application](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-application/) embedded component.
        """
        capital_financing_promotion: NotRequired[
            "AccountSession.CreateParamsComponentsCapitalFinancingPromotion"
        ]
        """
        Configuration for the [Capital financing promotion](https://docs.stripe.com/connect/supported-embedded-components/capital-financing-promotion/) embedded component.
        """
        capital_overview: NotRequired[
            "AccountSession.CreateParamsComponentsCapitalOverview"
        ]
        """
        Configuration for the [Capital overview](https://docs.stripe.com/connect/supported-embedded-components/capital-overview/) embedded component.
        """
        disputes_list: NotRequired[
            "AccountSession.CreateParamsComponentsDisputesList"
        ]
        """
        Configuration for the [disputes list](https://docs.stripe.com/connect/supported-embedded-components/disputes-list/) embedded component.
        """
        documents: NotRequired[
            "AccountSession.CreateParamsComponentsDocuments"
        ]
        """
        Configuration for the [documents](https://docs.stripe.com/connect/supported-embedded-components/documents/) embedded component.
        """
        export_tax_transactions: NotRequired[
            "AccountSession.CreateParamsComponentsExportTaxTransactions"
        ]
        """
        Configuration for the [export tax transactions](https://docs.stripe.com/connect/supported-embedded-components/export-tax-transactions/) embedded component.
        """
        financial_account: NotRequired[
            "AccountSession.CreateParamsComponentsFinancialAccount"
        ]
        """
        Configuration for the [financial account](https://docs.stripe.com/connect/supported-embedded-components/financial-account/) embedded component.
        """
        financial_account_transactions: NotRequired[
            "AccountSession.CreateParamsComponentsFinancialAccountTransactions"
        ]
        """
        Configuration for the [financial account transactions](https://docs.stripe.com/connect/supported-embedded-components/financial-account-transactions/) embedded component.
        """
        issuing_card: NotRequired[
            "AccountSession.CreateParamsComponentsIssuingCard"
        ]
        """
        Configuration for the [issuing card](https://docs.stripe.com/connect/supported-embedded-components/issuing-card/) embedded component.
        """
        issuing_cards_list: NotRequired[
            "AccountSession.CreateParamsComponentsIssuingCardsList"
        ]
        """
        Configuration for the [issuing cards list](https://docs.stripe.com/connect/supported-embedded-components/issuing-cards-list/) embedded component.
        """
        notification_banner: NotRequired[
            "AccountSession.CreateParamsComponentsNotificationBanner"
        ]
        """
        Configuration for the [notification banner](https://docs.stripe.com/connect/supported-embedded-components/notification-banner/) embedded component.
        """
        payment_details: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentDetails"
        ]
        """
        Configuration for the [payment details](https://docs.stripe.com/connect/supported-embedded-components/payment-details/) embedded component.
        """
        payment_disputes: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentDisputes"
        ]
        """
        Configuration for the [payment disputes](https://docs.stripe.com/connect/supported-embedded-components/payment-disputes/) embedded component.
        """
        payment_method_settings: NotRequired[
            "AccountSession.CreateParamsComponentsPaymentMethodSettings"
        ]
        """
        Configuration for the [payment method settings](https://docs.stripe.com/connect/supported-embedded-components/payment-method-settings/) embedded component.
        """
        payments: NotRequired["AccountSession.CreateParamsComponentsPayments"]
        """
        Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/) embedded component.
        """
        payouts: NotRequired["AccountSession.CreateParamsComponentsPayouts"]
        """
        Configuration for the [payouts](https://docs.stripe.com/connect/supported-embedded-components/payouts/) embedded component.
        """
        payouts_list: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutsList"
        ]
        """
        Configuration for the [payouts list](https://docs.stripe.com/connect/supported-embedded-components/payouts-list/) embedded component.
        """
        product_tax_code_selector: NotRequired[
            "AccountSession.CreateParamsComponentsProductTaxCodeSelector"
        ]
        """
        Configuration for the [product tax code selector](https://docs.stripe.com/connect/supported-embedded-components/product-tax-code-selector/) embedded component.
        """
        recipients: NotRequired[
            "AccountSession.CreateParamsComponentsRecipients"
        ]
        """
        Configuration for the [recipients](https://docs.stripe.com/connect/supported-embedded-components/recipients/) embedded component.
        """
        reporting_chart: NotRequired[
            "AccountSession.CreateParamsComponentsReportingChart"
        ]
        """
        Configuration for the [reporting chart](https://docs.stripe.com/connect/supported-embedded-components/reporting-chart/) embedded component.
        """
        tax_registrations: NotRequired[
            "AccountSession.CreateParamsComponentsTaxRegistrations"
        ]
        """
        Configuration for the [tax registrations](https://docs.stripe.com/connect/supported-embedded-components/tax-registrations/) embedded component.
        """
        tax_settings: NotRequired[
            "AccountSession.CreateParamsComponentsTaxSettings"
        ]
        """
        Configuration for the [tax settings](https://docs.stripe.com/connect/supported-embedded-components/tax-settings/) embedded component.
        """
        tax_threshold_monitoring: NotRequired[
            "AccountSession.CreateParamsComponentsTaxThresholdMonitoring"
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
            "AccountSession.CreateParamsComponentsAccountManagementFeatures"
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
            "AccountSession.CreateParamsComponentsAccountOnboardingFeatures"
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
            "AccountSession.CreateParamsComponentsAppInstallFeatures"
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
            "AccountSession.CreateParamsComponentsAppViewportFeatures"
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
            "AccountSession.CreateParamsComponentsBalancesFeatures"
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
            "AccountSession.CreateParamsComponentsCapitalFinancingFeatures"
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
            "AccountSession.CreateParamsComponentsCapitalFinancingApplicationFeatures"
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
            "AccountSession.CreateParamsComponentsCapitalFinancingPromotionFeatures"
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
            "AccountSession.CreateParamsComponentsCapitalOverviewFeatures"
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
            "AccountSession.CreateParamsComponentsDisputesListFeatures"
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
            "AccountSession.CreateParamsComponentsDocumentsFeatures"
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
            "AccountSession.CreateParamsComponentsExportTaxTransactionsFeatures"
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
            "AccountSession.CreateParamsComponentsFinancialAccountFeatures"
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
            "AccountSession.CreateParamsComponentsFinancialAccountTransactionsFeatures"
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
            "AccountSession.CreateParamsComponentsIssuingCardFeatures"
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
            "AccountSession.CreateParamsComponentsIssuingCardsListFeatures"
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
            "AccountSession.CreateParamsComponentsNotificationBannerFeatures"
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
            "AccountSession.CreateParamsComponentsPaymentDetailsFeatures"
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
            "AccountSession.CreateParamsComponentsPaymentDisputesFeatures"
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
            "AccountSession.CreateParamsComponentsPaymentMethodSettingsFeatures"
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
            "AccountSession.CreateParamsComponentsPaymentsFeatures"
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
            "AccountSession.CreateParamsComponentsPayoutsFeatures"
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
            "AccountSession.CreateParamsComponentsPayoutsListFeatures"
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
            "AccountSession.CreateParamsComponentsProductTaxCodeSelectorFeatures"
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
            "AccountSession.CreateParamsComponentsRecipientsFeatures"
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
            "AccountSession.CreateParamsComponentsReportingChartFeatures"
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
            "AccountSession.CreateParamsComponentsTaxRegistrationsFeatures"
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
            "AccountSession.CreateParamsComponentsTaxSettingsFeatures"
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
            "AccountSession.CreateParamsComponentsTaxThresholdMonitoringFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsTaxThresholdMonitoringFeatures(TypedDict):
        pass

    account: str
    """
    The ID of the account the AccountSession was created for
    """
    client_secret: str
    """
    The client secret of this AccountSession. Used on the client to set up secure access to the given `account`.

    The client secret can be used to provide access to `account` from your frontend. It should not be stored, logged, or exposed to anyone other than the connected account. Make sure that you have TLS enabled on any page that includes the client secret.

    Refer to our docs to [setup Connect embedded components](https://stripe.com/docs/connect/get-started-connect-embedded-components) and learn about how `client_secret` should be handled.
    """
    components: Components
    expires_at: int
    """
    The timestamp at which this AccountSession will expire.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["account_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def create(
        cls, **params: Unpack["AccountSession.CreateParams"]
    ) -> "AccountSession":
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
        return cast(
            "AccountSession",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["AccountSession.CreateParams"]
    ) -> "AccountSession":
        """
        Creates a AccountSession object that includes a single-use token that the platform can use on their front-end to grant client-side API access.
        """
        return cast(
            "AccountSession",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"components": Components}
