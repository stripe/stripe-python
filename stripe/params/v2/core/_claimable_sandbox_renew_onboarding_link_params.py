# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ClaimableSandboxRenewOnboardingLinkParams(TypedDict):
    onboarding_link_details: NotRequired[
        "ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetails"
    ]
    """
    Details about the onboarding link.
    If omitted, the existing onboarding link details will be reused.
    """


class ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetails(
    TypedDict
):
    refresh_url: str
    """
    The URL the user will be redirected to if the onboarding link is expired or invalid.
    The URL specified should attempt to generate a new onboarding link,
    and re-direct the user to this new onboarding link so that they can proceed with the onboarding flow.
    """
