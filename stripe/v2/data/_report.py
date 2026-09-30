# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Report(StripeObject):
    """
    The `Report` resource represents a Stripe-defined, parameterized report that provides
    insights into various aspects of your Stripe integration.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.report"]] = "v2.data.report"

    class Parameters(StripeObject):
        class ArrayDetails(StripeObject):
            class EnumDetails(StripeObject):
                allowed_values: List[str]
                """
                Allowed values of the enum.
                """

            element_type: Union[
                Literal["array", "enum", "string", "timestamp"], str
            ]
            """
            The data type of the elements in the array.
            """
            enum_details: Optional[EnumDetails]
            """
            Details about enum elements in the array.
            """
            _inner_class_types = {"enum_details": EnumDetails}

        class EnumDetails(StripeObject):
            allowed_values: List[str]
            """
            Allowed values of the enum.
            """

        array_details: Optional[ArrayDetails]
        """
        For array parameters, provides details about the array elements.
        """
        description: str
        """
        Explains the purpose and usage of the parameter.
        """
        enum_details: Optional[EnumDetails]
        """
        For enum parameters, provides the list of allowed values.
        """
        required: bool
        """
        Indicates whether the parameter must be provided.
        """
        type: Union[Literal["array", "enum", "string", "timestamp"], str]
        """
        The data type of the parameter.
        """
        _inner_class_types = {
            "array_details": ArrayDetails,
            "enum_details": EnumDetails,
        }

    default_sql: Optional[str]
    """
    Representative SQL generated using common parameter values, or an explanatory message when
    the report's SQL cannot be exposed. Only present when requested via `include[0]=default_sql`.
    """
    description: str
    """
    A human-readable description of what this report contains.
    """
    id: str
    """
    The unique identifier of the `Report`.
    """
    livemode: bool
    """
    Whether this `Report` is available in live mode.
    """
    name: str
    """
    The human-readable name of the `Report`.
    """
    object: Literal["v2.data.report"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    parameters: Optional[UntypedStripeObject[Parameters]]
    """
    Specification of the parameters that the `Report` accepts, keyed by parameter name.
    """
    _inner_class_types = {"parameters": Parameters}
