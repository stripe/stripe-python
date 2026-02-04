# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ConnectionSession(StripeObject):
    """
    The ConnectionSession resource.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.connection_session"]] = (
        "v2.core.connection_session"
    )

    class Connection(StripeObject):
        granted_access: Optional[List[Literal["payout_methods"]]]
        """
        The access granted to the Account by the Connection.
        """
        type: Literal["link"]
        """
        The type of the Connection.
        """

    account: str
    """
    The Account this Connection Session was created for.
    """
    allowed_connection_types: Optional[List[Literal["link"]]]
    """
    The Connection types that the Connection Session is allowed to establish.
    """
    client_secret: str
    """
    The client secret of this Connection Session. Used on the client to set up secure access to the given Account.
    """
    connection: Optional[Connection]
    """
    The Connection created by the ConnectionSession.
    """
    created: str
    """
    Time at which the ConnectionSession was created.
    """
    id: str
    """
    The unique identifier for this ConnectionSession.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.connection_session"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    requested_access: Optional[List[Literal["payout_methods"]]]
    """
    The access that is collected with the Connection Session.
    """
    _inner_class_types = {"connection": Connection}
