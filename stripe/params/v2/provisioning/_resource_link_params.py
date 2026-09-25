# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ResourceLinkParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition of the existing resource.
    """
    environment: NotRequired[Literal["dev", "prod"]]
    """
    Environment the existing resource runs in.
    """
    livemode: NotRequired[bool]
    """
    Whether the resource should use Stripe live-mode objects. When omitted, this resolves to false
    for a sandbox target and true otherwise. Sandbox targets cannot link live-mode resources.
    """
    project: NotRequired[str]
    """
    Identifier of the project to link the resource to.
    """
    provider: str
    """
    Identifier of the provider that hosts the existing resource.
    """
    service_ref: str
    """
    Identifier of the provider service the existing resource belongs to.
    """
