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
        """
        Message from the provider to display to the user.
        """
        received_at: str
        """
        Time at which Stripe received the message from the provider.
        """

    catalog: Optional[Literal["dev", "prod", "testing"]]
    """
    Catalog partition containing the resource's provider service.
    """
    created: str
    """
    Time at which the resource was created.
    """
    environment: Literal["dev", "prod"]
    """
    Provider environment in which the resource runs.
    """
    error_message: Optional[str]
    """
    Error reported when provisioning the resource fails.
    """
    id: str
    """
    Unique identifier for the resource.
    """
    livemode: bool
    """
    Whether this resource uses Stripe live-mode objects. This is independent of the provider
    catalog and is immutable for the lifetime of the resource.
    """
    name: Optional[str]
    """
    Human-readable name of the resource.
    """
    needs_information_schema: Optional[UntypedStripeObject[Any]]
    """
    Schema describing additional information the provider requires to finish provisioning.
    """
    object: Literal["v2.provisioning.resource"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    provider: str
    """
    Identifier of the provider that manages the resource.
    """
    service_ref: str
    """
    Identifier of the provider service used to provision the resource.
    """
    status: Literal[
        "complete", "errored", "needs_information", "pending", "removed"
    ]
    """
    Current provisioning status of the resource.
    """
    user_message: Optional[UserMessage]
    """
    Message supplied by the provider when the resource becomes ready.
    """
    _inner_class_types = {"user_message": UserMessage}
