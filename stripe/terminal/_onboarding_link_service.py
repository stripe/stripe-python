# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.terminal._onboarding_link import OnboardingLink
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OnboardingLinkService(StripeService):
    class CreateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        link_options: "OnboardingLinkService.CreateParamsLinkOptions"
        """
        Specific fields needed to generate the desired link type.
        """
        link_type: Literal["apple_terms_and_conditions"]
        """
        The type of link being generated.
        """
        on_behalf_of: NotRequired[str]
        """
        Stripe account ID to generate the link for.
        """

    class CreateParamsLinkOptions(TypedDict):
        apple_terms_and_conditions: NotRequired[
            "OnboardingLinkService.CreateParamsLinkOptionsAppleTermsAndConditions"
        ]
        """
        The options associated with the Apple Terms and Conditions link type.
        """

    class CreateParamsLinkOptionsAppleTermsAndConditions(TypedDict):
        allow_relinking: NotRequired[bool]
        """
        Whether the link should also support users relinking their Apple account.
        """
        merchant_display_name: str
        """
        The business name of the merchant accepting Apple's Terms and Conditions.
        """

    def create(
        self,
        params: "OnboardingLinkService.CreateParams",
        options: RequestOptions = {},
    ) -> OnboardingLink:
        """
        Creates a new OnboardingLink object that contains a redirect_url used for onboarding onto Tap to Pay on iPhone.
        """
        return cast(
            OnboardingLink,
            self._request(
                "post",
                "/v1/terminal/onboarding_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OnboardingLinkService.CreateParams",
        options: RequestOptions = {},
    ) -> OnboardingLink:
        """
        Creates a new OnboardingLink object that contains a redirect_url used for onboarding onto Tap to Pay on iPhone.
        """
        return cast(
            OnboardingLink,
            await self._request_async(
                "post",
                "/v1/terminal/onboarding_links",
                base_address="api",
                params=params,
                options=options,
            ),
        )
