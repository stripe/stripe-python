# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ClaimableSandboxCreateParams(TypedDict):
    channel: NotRequired[Literal["public", "testing"]]
    """
    The distribution channel used to pre-install your Stripe App on the claimable sandbox.
    Use `testing` to install your app's external test version or `public` to install its published version.
    This field defaults to `public` if omitted.
    """
    enable_mcp_access: bool
    """
    If true, returns a key that can be used with [Stripe's MCP server](https://docs.stripe.com/mcp).
    """
    onboarding_link_details: (
        "ClaimableSandboxCreateParamsOnboardingLinkDetails"
    )
    """
    Details about the onboarding link.
    """
    prefill: "ClaimableSandboxCreateParamsPrefill"
    """
    Values that are prefilled when a user claims the sandbox. When a user claims the sandbox, they will be able to update these values.
    """


class ClaimableSandboxCreateParamsOnboardingLinkDetails(TypedDict):
    refresh_url: str
    """
    The URL the user will be redirected to if the onboarding link is expired or invalid.
    The URL specified should attempt to generate a new onboarding link,
    and re-direct the user to this new onboarding link so that they can proceed with the onboarding flow.
    """
    return_url: NotRequired[str]
    """
    The URL offered to the user as a way back to your app after they claim the sandbox.
    """


class ClaimableSandboxCreateParamsPrefill(TypedDict):
    country: str
    """
    Country in which the account holder resides, or in which the business is legally established.
    Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    email: str
    """
    Email address of the user who will claim the sandbox.
    Stripe sends this address an invitation to claim the sandbox and a reminder before the unclaimed sandbox expires.
    """
    name: NotRequired[str]
    """
    Name for the sandbox.
    """
