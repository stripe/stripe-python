# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class MeterErrorReport(StripeObject):
    OBJECT_NAME: ClassVar[Literal["billing.meter_error_report"]] = (
        "billing.meter_error_report"
    )

    class Reason(StripeObject):
        class ErrorType(StripeObject):
            class SampleError(StripeObject):
                class ApiRequest(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """
                    idempotency_key: str
                    """
                    idempotency_key of the request
                    """

                api_request: Optional[ApiRequest]
                error_message: str
                """
                message of the error
                """
                _inner_class_types = {"api_request": ApiRequest}

            sample_errors: List[SampleError]
            _inner_class_types = {"sample_errors": SampleError}

        error_count: int
        """
        The number of errors generated
        """
        error_types: List[ErrorType]
        """
        More information about errors
        """
        _inner_class_types = {"error_types": ErrorType}

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier for the object.
        """
        object: str
        """
        The type of meter error related object. Should be 'meter'
        """
        url: str
        """
        The url of the meter object
        """

    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["billing.meter_error_report"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reason: Reason
    related_object: Optional[RelatedObject]
    """
    The related objects about the error
    """
    summary: str
    """
    Summary of invalid events
    """
    validation_end: int
    """
    Time when validation ended. Measured in seconds since the Unix epoch
    """
    validation_start: int
    """
    Time when validation started. Measured in seconds since the Unix epoch
    """
    _inner_class_types = {"reason": Reason, "related_object": RelatedObject}
