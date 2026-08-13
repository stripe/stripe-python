# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class OperationsResolveAddressResult(StripeObject):
    """
    The result of resolving an address to its tax precision level.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.tax.operations_resolve_address_result"]
    ] = "v2.tax.operations_resolve_address_result"

    class Address(StripeObject):
        city: Optional[str]
        """
        The city.
        """
        country: Optional[str]
        """
        The two-letter country code.
        """
        line1: Optional[str]
        """
        The first line of the street address.
        """
        postal_code: Optional[str]
        """
        The postal code.
        """
        state: Optional[str]
        """
        The state or province.
        """

    class PrecisionDetails(StripeObject):
        class Issue(StripeObject):
            code: Literal["required_for_improved_precision"]
            """
            A code describing the issue.
            """
            field: Literal["city", "country", "line1", "postal_code", "state"]
            """
            The address field with the issue.
            """

        issues: List[Issue]
        """
        Issues preventing higher precision.
        """
        _inner_class_types = {"issues": Issue}

    address: Address
    """
    The normalized form of the input address.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.tax.operations_resolve_address_result"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    precision: Literal[
        "none", "address", "city", "country", "postal_code", "state", "street"
    ]
    """
    The precision level of the resolved address.
    """
    precision_details: PrecisionDetails
    """
    Details about the precision, including any issues.
    """
    _inner_class_types = {
        "address": Address,
        "precision_details": PrecisionDetails,
    }
