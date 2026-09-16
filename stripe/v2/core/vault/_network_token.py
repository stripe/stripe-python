# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class NetworkToken(StripeObject):
    """
    A NetworkToken object represents a network token provisioned for a card.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.vault.network_token"]] = (
        "v2.core.vault.network_token"
    )

    class Cryptogram(StripeObject):
        eci: Optional[str]
        """
        The electronic commerce indicator associated with the cryptogram.
        """
        type: str
        """
        The cryptogram type.
        """
        value: str
        """
        The cryptogram value.
        """

    created: str
    """
    Created timestamp.
    """
    cryptogram: Optional[Cryptogram]
    """
    This field is unset in create and retrieve responses. It is populated only after a successful generate_cryptogram request.
    """
    exp_month: Optional[str]
    """
    The month the network token expires.
    """
    exp_year: Optional[str]
    """
    The year the network token expires.
    """
    id: str
    """
    ID of the NetworkToken object.
    """
    livemode: bool
    """
    Whether the object exists in live mode or in test mode.
    """
    number: Optional[str]
    """
    The network token number.
    """
    object: Literal["v2.core.vault.network_token"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["active", "deactivated", "suspended"]
    """
    Closed Enum. The status of the network token.
    """
    _inner_class_types = {"cryptogram": Cryptogram}
