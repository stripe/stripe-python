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
        account_onboarding: NotRequired[
            "AccountSessionService.CreateParamsComponentsAccountOnboarding"
        ]
        """
        Configuration for the account onboarding embedded component.
        """
        capital_financing_promotion: NotRequired[
            "AccountSessionService.CreateParamsComponentsCapitalFinancingPromotion"
        ]
        documents: NotRequired[
            "AccountSessionService.CreateParamsComponentsDocuments"
        ]
        """
        Configuration for the documents embedded component.
        """
        financial_account: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccount"
        ]
        """
        Configuration for the financial account component.
        """
        financial_account_transactions: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccountTransactions"
        ]
        """
        Configuration for the financial account transactions component.
        """
        issuing_card: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCard"
        ]
        """
        Configuration for the issuing card component.
        """
        issuing_cards_list: NotRequired[
            "AccountSessionService.CreateParamsComponentsIssuingCardsList"
        ]
        """
        Configuration for the issuing cards list component.
        """
        payment_details: NotRequired[
            "AccountSessionService.CreateParamsComponentsPaymentDetails"
        ]
        """
        Configuration for the payment details embedded component.
        """
        payments: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayments"
        ]
        """
        Configuration for the payments embedded component.
        """
        payouts: NotRequired[
            "AccountSessionService.CreateParamsComponentsPayouts"
        ]
        """
        Configuration for the payouts embedded component.
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

    class CreateParamsComponentsFinancialAccountFeatures(TypedDict):
        money_movement: NotRequired[bool]
        """
        Whether to allow money movement features.
        """

    class CreateParamsComponentsFinancialAccountTransactions(TypedDict):
        enabled: bool
        """
        Whether the embedded component is enabled.
        """
        features: NotRequired[
            "AccountSessionService.CreateParamsComponentsFinancialAccountTransactionsFeatures"
        ]

    class CreateParamsComponentsFinancialAccountTransactionsFeatures(
        TypedDict
    ):
        card_spend_dispute_management: NotRequired[bool]
        """
        Whether to allow card spend dispute features.
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
        pass

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
        cardholder_management: NotRequired[bool]
        """
        Whether to allow cardholder management features.
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
        Whether to allow connected accounts to manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether to allow sending refunds. This is `true` by default.
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
        Whether to allow connected accounts to manage destination charges that are created on behalf of them. This is `false` by default.
        """
        dispute_management: NotRequired[bool]
        """
        Whether to allow responding to disputes, including submitting evidence and accepting disputes. This is `true` by default.
        """
        refund_management: NotRequired[bool]
        """
        Whether to allow sending refunds. This is `true` by default.
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
        edit_payout_schedule: NotRequired[bool]
        """
        Whether to allow payout schedule to be changed. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
        """
        instant_payouts: NotRequired[bool]
        """
        Whether to allow creation of instant payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
        """
        standard_payouts: NotRequired[bool]
        """
        Whether to allow creation of standard payouts. Default `true` when Stripe owns Loss Liability, default `false` otherwise.
        """

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
                api_mode="V1",
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
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
