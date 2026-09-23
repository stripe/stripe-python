# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import Literal, NotRequired, TypedDict


class ResourceUpdateParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition of the resource.
    """
    configuration: NotRequired["Dict[str, Any]|UntypedStripeObject[Any]"]
    """
    New provider-specific configuration payload for the resource.
    """
    service_ref: NotRequired[str]
    """
    Provider's service id to switch the resource to. If omitted, the resource's existing service
    is retained and this is treated as a config-only update.
    """
