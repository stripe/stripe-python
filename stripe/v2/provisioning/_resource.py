# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, Optional
from typing_extensions import Literal


class Resource(StripeObject):
    """
    The `Resource` resource represents a provider-managed resource provisioned on behalf of
    a `Project`.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.resource"]] = (
        "v2.provisioning.resource"
    )

    class UserMessage(StripeObject):
        message: str
        received_at: str

    catalog: Optional[Literal["dev", "prod", "testing"]]
    created: str
    environment: Literal["dev", "prod"]
    error_message: Optional[str]
    id: str
    livemode: bool
    """
    Whether this resource uses Stripe live-mode objects. This is independent of the provider
    catalog and is immutable for the lifetime of the resource.
    """
    name: Optional[str]
    needs_information_schema: Optional[UntypedStripeObject[Any]]
    object: Literal["v2.provisioning.resource"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    provider: str
    service_ref: str
    status: Literal[
        "complete", "errored", "needs_information", "pending", "removed"
    ]
    user_message: Optional[UserMessage]
    _inner_class_types = {"user_message": UserMessage}
