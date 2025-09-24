# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, cast
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

        class BalanceReport(StripeObject):
            class Features(StripeObject):
                pass

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

        class InstantPayoutsPromotion(StripeObject):
            class Features(StripeObject):
                disable_stripe_user_authentication: bool
                """
                Whether Stripe user authentication is disabled. This value can only be `true` for accounts where `controller.requirement_collection` is `application` for the account. The default value is the opposite of the `external_account_collection` value. For example, if you don't set `external_account_collection`, it defaults to `true` and `disable_stripe_user_authentication` defaults to `false`.
                """
                external_account_collection: bool
                """
                Whether external account collection is enabled. This feature can only be `false` for accounts where you're responsible for collecting updated information when requirements are due or change, like Custom accounts. The default value for this feature is `true`.
                """
                instant_payouts: bool
                """
                Whether to allow creation of instant payouts. Defaults to `true` when `controller.losses.payments` is set to `stripe` for the account, otherwise `false`.
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

        class PayoutDetails(StripeObject):
            class Features(StripeObject):
                pass

            enabled: bool
            """
            Whether the embedded component is enabled.
            """
            features: Features
            _inner_class_types = {"features": Features}

        class PayoutReconciliationReport(StripeObject):
            class Features(StripeObject):
                pass

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
        balance_report: BalanceReport
        balances: Balances
        disputes_list: DisputesList
        documents: Documents
        financial_account: FinancialAccount
        financial_account_transactions: FinancialAccountTransactions
        instant_payouts_promotion: InstantPayoutsPromotion
        issuing_card: IssuingCard
        issuing_cards_list: IssuingCardsList
        notification_banner: NotificationBanner
        payment_details: PaymentDetails
        payment_disputes: PaymentDisputes
        payments: Payments
        payout_details: PayoutDetails
        payout_reconciliation_report: PayoutReconciliationReport
        payouts: Payouts
        payouts_list: PayoutsList
        tax_registrations: TaxRegistrations
        tax_settings: TaxSettings
        _inner_class_types = {
            "account_management": AccountManagement,
            "account_onboarding": AccountOnboarding,
            "balance_report": BalanceReport,
            "balances": Balances,
            "disputes_list": DisputesList,
            "documents": Documents,
            "financial_account": FinancialAccount,
            "financial_account_transactions": FinancialAccountTransactions,
            "instant_payouts_promotion": InstantPayoutsPromotion,
            "issuing_card": IssuingCard,
            "issuing_cards_list": IssuingCardsList,
            "notification_banner": NotificationBanner,
            "payment_details": PaymentDetails,
            "payment_disputes": PaymentDisputes,
            "payments": Payments,
            "payout_details": PayoutDetails,
            "payout_reconciliation_report": PayoutReconciliationReport,
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
        balance_report: NotRequired[
            "AccountSession.CreateParamsComponentsBalanceReport"
        ]
        """
        Configuration for the [balance report](https://docs.stripe.com/connect/supported-embedded-components/financial-reports#balance-report) embedded component.
        """
        balances: NotRequired["AccountSession.CreateParamsComponentsBalances"]
        """
        Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/) embedded component.
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
        instant_payouts_promotion: NotRequired[
            "AccountSession.CreateParamsComponentsInstantPayoutsPromotion"
        ]
        """
        Configuration for the [instant payouts promotion](https://docs.stripe.com/connect/supported-embedded-components/instant-payouts-promotion/) embedded component.
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
        payments: NotRequired["AccountSession.CreateParamsComponentsPayments"]
        """
        Configuration for the [payments](https://docs.stripe.com/connect/supported-embedded-components/payments/) embedded component.
        """
        payout_details: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutDetails"
        ]
        """
        Configuration for the [payout details](https://docs.stripe.com/connect/supported-embedded-components/payout-details/) embedded component.
        """
        payout_reconciliation_report: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutReconciliationReport"
        ]
        """
        Configuration for the [payout reconciliation report](https://docs.stripe.com/connect/supported-embedded-components/financial-reports#payout-reconciliation-report) embedded component.
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

    class CreateParamsComponentsBalanceReport(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsBalanceReportFeatures"
        ]
        """
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsBalanceReportFeatures(TypedDict):
        pass

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
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsDocumentsFeatures(TypedDict):
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

    class CreateParamsComponentsInstantPayoutsPromotion(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsInstantPayoutsPromotionFeatures"
        ]
        """
        The list of features enabled in the embedded component.
        """

    class CreateParamsComponentsInstantPayoutsPromotionFeatures(TypedDict):
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

    class CreateParamsComponentsPayoutDetails(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutDetailsFeatures"
        ]
        """
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsPayoutDetailsFeatures(TypedDict):
        pass

    class CreateParamsComponentsPayoutReconciliationReport(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSession.CreateParamsComponentsPayoutReconciliationReportFeatures"
        ]
        """
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsPayoutReconciliationReportFeatures(TypedDict):
        pass

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
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsPayoutsListFeatures(TypedDict):
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
        An empty list, because this embedded component has no features.
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
        An empty list, because this embedded component has no features.
        """

    class CreateParamsComponentsTaxSettingsFeatures(TypedDict):
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
