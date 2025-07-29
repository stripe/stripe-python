# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_session import AccountSession
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


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
        balances: NotRequired[
            "AccountSessionService.CreateParamsComponentsBalances"
        ]
        """
        Configuration for the [balances](https://docs.stripe.com/connect/supported-embedded-components/balances/) embedded component.
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
        instant_payouts_promotion: NotRequired[
            "AccountSessionService.CreateParamsComponentsInstantPayoutsPromotion"
        ]
        """
        Configuration for the [instant payouts promotion](https://docs.stripe.com/connect/supported-embedded-components/instant-payouts-promotion/) embedded component.
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

    class CreateParamsComponentsInstantPayoutsPromotion(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsInstantPayoutsPromotionFeatures"
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
