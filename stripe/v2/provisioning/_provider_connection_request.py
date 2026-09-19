# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.provisioning._provider_connection import ProviderConnection


class ProviderConnectionRequest(StripeObject):
    """
    A ProviderConnectionRequest represents an in-progress account-linking workflow. Once the
    workflow completes, `provider_connection` is populated with the resulting ProviderConnection.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.provisioning.provider_connection_request"]
    ] = "v2.provisioning.provider_connection_request"

    class Error(StripeObject):
        code: str
        """
        Machine-readable error code.
        """
        message: str
        """
        Human-readable error message.
        """

    created: Optional[str]
    """
    Time at which the provider connection request was created.
    """
    error: Optional[Error]
    """
    Error from the account-linking workflow, set when request_status is ERROR.
    """
    id: str
    """
    Unique identifier for the provider connection request.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    needs_information_schema: Optional[UntypedStripeObject[Any]]
    """
    Schema describing the information the provider still needs, set when request_status is
    NEEDS_INFORMATION.
    """
    object: Literal["v2.provisioning.provider_connection_request"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    provider: str
    """
    Identifier of the provider this connection request is linked to.
    """
    provider_connection: Optional["ProviderConnection"]
    """
    A ProviderConnection represents a link between a project and a provider account that
    resources can be created against; unlinking it prevents further resource creation.
    """
    redirect_url: Optional[str]
    """
    URL the caller should redirect to in order to continue the account-linking workflow.
    """
    request_status: Literal[
        "complete", "error", "needs_information", "pending_auth", "requested"
    ]
    """
    Status of the underlying account-linking workflow. Unset once the workflow completes; see
    provider_connection for the resulting connection's status.
    """
    scopes: List[str]
    """
    Scopes requested for the account-linking workflow.
    """
    _inner_class_types = {"error": Error}
