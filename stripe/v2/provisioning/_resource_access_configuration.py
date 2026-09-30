# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ResourceAccessConfiguration(StripeObject):
    """
    The current provider-issued access configuration for a Provisioning Resource.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.provisioning.resource_access_configuration"]
    ] = "v2.provisioning.resource_access_configuration"
    configuration: UntypedStripeObject[str]
    """
    Provider-defined configuration names mapped to their secret string values.
    """
    created: str
    """
    Time at which this credential generation became current.
    """
    expires_at: Optional[str]
    """
    Time at which these credentials cease to be valid, when supplied by the Provider.
    """
    livemode: bool
    """
    Whether the referenced Resource uses Stripe live-mode objects.
    """
    object: Literal["v2.provisioning.resource_access_configuration"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    resource: str
    """
    Provisioning Resource to which this access configuration belongs.
    """
