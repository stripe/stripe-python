# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ClaimableSandboxCreateParams(TypedDict):
    enable_mcp_access: bool
    """
    If true, returns a key that can be used with [Stripe's MCP server](https://docs.stripe.com/mcp).
    """
    prefill: "ClaimableSandboxCreateParamsPrefill"
    """
    Values that are prefilled when a user claims the sandbox. When a user claims the sandbox, they will be able to update these values.
    """


class ClaimableSandboxCreateParamsPrefill(TypedDict):
    country: str
    """
    Country in which the account holder resides, or in which the business is legally established.
    Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    email: str
    """
    Email that this sandbox is meant to be claimed by. Stripe will
    notify this email address before the sandbox expires.
    """
    name: NotRequired[str]
    """
    Name for the sandbox.
    """
