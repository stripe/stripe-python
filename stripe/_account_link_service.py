# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_link import AccountLink
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class AccountLinkService(StripeService):
    class CreateParams(TypedDict):
        account: str
        """
        The identifier of the account to create an account link for.
        """
        collect: NotRequired["Literal['currently_due', 'eventually_due']"]
        """
        Which information the platform needs to collect from the user. One of `currently_due` or `eventually_due`. Default is `currently_due`.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        refresh_url: NotRequired["str"]
        """
        The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
        """
        return_url: NotRequired["str"]
        """
        The URL that the user will be redirected to upon leaving or completing the linked flow.
        """
        type: Literal["account_onboarding", "account_update"]
        """
        The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`.
        """

    def create(
        self,
        params: "AccountLinkService.CreateParams",
        options: RequestOptions = {},
    ) -> AccountLink:
        """
        Creates an AccountLink object that includes a single-use Stripe URL that the platform can redirect their user to in order to take them through the Connect Onboarding flow.
        """
        return cast(
            AccountLink,
            self._requestor.request(
                "post",
                "/v1/account_links",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
