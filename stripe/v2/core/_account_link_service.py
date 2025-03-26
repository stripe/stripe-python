# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.v2.core._account_link import AccountLink
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class AccountLinkService(StripeService):
    class CreateParams(TypedDict):
        account: str
        """
        The ID of the Account to create link for.
        """
        use_case: "AccountLinkService.CreateParamsUseCase"
        """
        The use case of the AccountLink.
        """

    class CreateParamsUseCase(TypedDict):
        type: Literal["account_onboarding", "account_update"]
        """
        Open Enum. The type of AccountLink the user is requesting.
        """
        account_onboarding: NotRequired[
            "AccountLinkService.CreateParamsUseCaseAccountOnboarding"
        ]
        """
        Indicates that the AccountLink provided should onboard an account.
        """
        account_update: NotRequired[
            "AccountLinkService.CreateParamsUseCaseAccountUpdate"
        ]
        """
        Indicates that the AccountLink provided should update a previously onboarded account.
        """

    class CreateParamsUseCaseAccountOnboarding(TypedDict):
        configurations: List[Literal["recipient"]]
        """
        Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
        """
        refresh_url: str
        """
        The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
        """
        return_url: NotRequired[str]
        """
        The URL that the user will be redirected to upon completing the linked flow.
        """

    class CreateParamsUseCaseAccountUpdate(TypedDict):
        configurations: List[Literal["recipient"]]
        """
        Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
        """
        refresh_url: str
        """
        The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
        """
        return_url: NotRequired[str]
        """
        The URL that the user will be redirected to upon completing the linked flow.
        """

    def create(
        self,
        params: "AccountLinkService.CreateParams",
        options: RequestOptions = {},
    ) -> AccountLink:
        """
        Creates an AccountLink object that includes a single-use Stripe URL that the merchant can redirect their user to in order to take them to a Stripe-hosted application such as Recipient Onboarding.
        """
        return cast(
            AccountLink,
            self._request(
                "post",
                "/v2/core/account_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountLinkService.CreateParams",
        options: RequestOptions = {},
    ) -> AccountLink:
        """
        Creates an AccountLink object that includes a single-use Stripe URL that the merchant can redirect their user to in order to take them to a Stripe-hosted application such as Recipient Onboarding.
        """
        return cast(
            AccountLink,
            await self._request_async(
                "post",
                "/v2/core/account_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )
