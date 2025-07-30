# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class OnboardingLink(CreateableAPIResource["OnboardingLink"]):
    """
    Returns redirect links used for onboarding onto Tap to Pay on iPhone.
    """

    OBJECT_NAME: ClassVar[Literal["terminal.onboarding_link"]] = (
        "terminal.onboarding_link"
    )

    class LinkOptions(StripeObject):
        class AppleTermsAndConditions(StripeObject):
            allow_relinking: Optional[bool]
            """
            Whether the link should also support users relinking their Apple account.
            """
            merchant_display_name: str
            """
            The business name of the merchant accepting Apple's Terms and Conditions.
            """

        apple_terms_and_conditions: Optional[AppleTermsAndConditions]
        """
        The options associated with the Apple Terms and Conditions link type.
        """
        _inner_class_types = {
            "apple_terms_and_conditions": AppleTermsAndConditions,
        }

    class CreateParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        link_options: "OnboardingLink.CreateParamsLinkOptions"
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
            "OnboardingLink.CreateParamsLinkOptionsAppleTermsAndConditions"
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

    link_options: LinkOptions
    """
    Link type options associated with the current onboarding link object.
    """
    link_type: Literal["apple_terms_and_conditions"]
    """
    The type of link being generated.
    """
    object: Literal["terminal.onboarding_link"]
    on_behalf_of: Optional[str]
    """
    Stripe account ID to generate the link for.
    """
    redirect_url: str
    """
    The link passed back to the user for their onboarding.
    """

    @classmethod
    def create(
        cls, **params: Unpack["OnboardingLink.CreateParams"]
    ) -> "OnboardingLink":
        """
        Creates a new OnboardingLink object that contains a redirect_url used for onboarding onto Tap to Pay on iPhone.
        """
        return cast(
            "OnboardingLink",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["OnboardingLink.CreateParams"]
    ) -> "OnboardingLink":
        """
        Creates a new OnboardingLink object that contains a redirect_url used for onboarding onto Tap to Pay on iPhone.
        """
        return cast(
            "OnboardingLink",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"link_options": LinkOptions}
