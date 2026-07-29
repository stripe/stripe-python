# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class Authorization(StripeObject):
    """
    An Authorization represents the set of credentials used to connect a group of Financial Connections Accounts.
    """

    OBJECT_NAME: ClassVar[Literal["financial_connections.authorization"]] = (
        "financial_connections.authorization"
    )

    class StatusDetails(StripeObject):
        class Active(StripeObject):
            action: Union[Literal["none", "relink_required"], str]
            """
            The action (if any) to proactively relink the Authorization.
            """
            expected_deactivation_date: int
            """
            When the Authorization is expected to become inactive, if applicable.
            """

        class Inactive(StripeObject):
            action: Union[Literal["none", "relink_required"], str]
            """
            The action (if any) to relink the inactive Authorization.
            """

        active: Optional[Active]
        inactive: Optional[Inactive]
        _inner_class_types = {"active": Active, "inactive": Inactive}

    id: str
    """
    Unique identifier for the object.
    """
    institution_name: str
    """
    The name of the institution that this authorization belongs to.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["financial_connections.authorization"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Union[Literal["active", "inactive"], str]
    """
    The status of the connection to the Authorization.
    """
    status_details: StatusDetails
    _inner_class_types = {"status_details": StatusDetails}
