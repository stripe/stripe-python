# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ClaimableSandboxRenewOnboardingLinkParams(TypedDict):
    onboarding_link_details: NotRequired[
        "ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetails"
    ]
    """
    Details about the onboarding link. If omitted, existing details are reused.
    Omitted URL fields retain their existing values.
    """


class ClaimableSandboxRenewOnboardingLinkParamsOnboardingLinkDetails(
    TypedDict
):
    refresh_url: NotRequired[str]
    """
    The URL the user will be redirected to if the onboarding link is expired or invalid.
    If omitted, the existing refresh URL is retained.
    The URL should generate a new onboarding link and redirect the user to it.
    """
    return_url: NotRequired[str]
    """
    The URL offered to the user as a way back to your app after they claim the sandbox.
    If omitted, the existing return URL is retained. Set to null to clear it.
    """
