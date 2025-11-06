# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class Report(StripeObject):
    """
    The Report resource represents a customizable report template that provides insights into various aspects of your Stripe integration.
    """

    OBJECT_NAME: ClassVar[Literal["v2.reporting.report"]] = (
        "v2.reporting.report"
    )

    class Parameters(StripeObject):
        class ArrayDetails(StripeObject):
            class EnumDetails(StripeObject):
                allowed_values: List[str]
                """
                Allowed values of the enum.
                """

            element_type: Literal["enum"]
            """
            Data type of the elements in the array.
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

        class TimestampDetails(StripeObject):
            max: str
            """
            Maximum permitted timestamp which can be requested.
            """
            min: str
            """
            Minimum permitted timestamp which can be requested.
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
        timestamp_details: Optional[TimestampDetails]
        """
        For timestamp parameters, specifies the allowed date range.
        """
        type: Literal["array", "enum", "string", "timestamp"]
        """
        The data type of the parameter.
        """
        _inner_class_types = {
            "array_details": ArrayDetails,
            "enum_details": EnumDetails,
            "timestamp_details": TimestampDetails,
        }

    id: str
    """
    The unique identifier of the `Report` object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str
    """
    The human-readable name of the `Report`.
    """
    object: Literal["v2.reporting.report"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    parameters: Dict[str, Parameters]
    """
    Specification of the parameters that the `Report` accepts. It details each parameter's
    name, description, whether it is required, and any validations performed.
    """
    _inner_class_types = {"parameters": Parameters}
