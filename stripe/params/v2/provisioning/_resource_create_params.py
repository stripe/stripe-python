# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import Literal, NotRequired, TypedDict


class ResourceCreateParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition to create the resource in.
    """
    configuration: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    Provider-specific configuration payload for the resource.
    """
    environment: NotRequired[Literal["dev", "prod"]]
    """
    Environment the resource should be created in.
    """
    livemode: NotRequired[bool]
    """
    Whether the resource should use Stripe live-mode objects. When omitted, this resolves to true.
    """
    name: NotRequired[str]
    """
    Human-readable name for the resource.
    """
    project: NotRequired[str]
    """
    Identifier of the project to create the resource in.
    """
    provider: str
    """
    Identifier of the provider to create the resource with.
    """
    service_ref: str
    """
    Identifier of the provider service to create the resource from.
    """
