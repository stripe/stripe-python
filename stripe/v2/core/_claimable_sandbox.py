# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ClaimableSandbox(StripeObject):
    """
    A claimable sandbox represents a Stripe sandbox that is anonymous.
    When it is created, it can be prefilled with specific metadata, such as email, name, or country.
    Claimable sandboxes can be claimed through a URL. When a user claims a sandbox through this URL,
    it will prompt them to create a new Stripe account. Or, it will allow them to claim this sandbox in their
    existing Stripe account.
    Claimable sandboxes have 60 days to be claimed. After this expiration time has passed,
    if the sandbox is not claimed, it will be deleted.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.claimable_sandbox"]] = (
        "v2.core.claimable_sandbox"
    )

    class ApiKeys(StripeObject):
        mcp: Optional[str]
        """
        Used to communicate with [Stripe's MCP server](https://docs.stripe.com/mcp).
        This allows LLM agents to securely operate on a Stripe account.
        """
        publishable: str
        """
        Publicly accessible in a web or mobile app client-side code.
        """
        secret: str
        """
        Should be stored securely in server-side code (such as an environment variable).
        """

    class Prefill(StripeObject):
        country: str
        """
        Country in which the account holder resides, or in which the business is legally established.
        Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        email: str
        """
        Email that this sandbox is meant to be claimed by. Stripe will
        send an email to this email address before the sandbox expires.
        """
        name: str
        """
        Name for the sandbox.
        """

    api_keys: ApiKeys
    """
    Keys that can be used to set up an integration for this sandbox and operate on the account.
    """
    claim_url: str
    """
    URL for user to claim sandbox into their existing Stripe account.
    """
    created: str
    """
    When the sandbox is created.
    """
    id: str
    """
    Unique identifier for the Claimable sandbox.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.claimable_sandbox"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    prefill: Prefill
    """
    Values prefilled during the creation of the sandbox.
    """
    _inner_class_types = {"api_keys": ApiKeys, "prefill": Prefill}
