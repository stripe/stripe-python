# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional
from typing_extensions import Literal


class Provider(StripeObject):
    """
    The `Provider` resource represents a third-party provider available in the
    provisioning catalog.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.provider"]] = (
        "v2.provisioning.provider"
    )
    capabilities: List[str]
    """
    Capabilities supported by the provider.
    """
    categories: List[str]
    """
    Categories the provider belongs to.
    """
    configuration_schema: UntypedStripeObject[Any]
    """
    Schema describing the configuration accepted by this provider.
    """
    created: str
    """
    Time at which the provider was created.
    """
    deep_link_purposes: List[str]
    """
    Deep-link purposes supported by the provider.
    """
    description: str
    """
    Description of the provider.
    """
    development: bool
    """
    proto3 scalar defaults apply: if unset, this value is `false`.
    """
    id: str
    """
    Unique identifier for the provider.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    llm_context: Optional[str]
    """
    URL of additional context about the provider intended for LLM consumption.
    """
    name: str
    """
    Human-readable name of the provider.
    """
    object: Literal["v2.provisioning.provider"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    privacy_policy_url: Optional[str]
    """
    URL of the provider's privacy policy.
    """
    tos_url: Optional[str]
    """
    URL of the provider's terms of service.
    """
    website_url: Optional[str]
    """
    URL of the provider's website.
    """
