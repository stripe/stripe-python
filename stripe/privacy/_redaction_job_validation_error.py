# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class RedactionJobValidationError(StripeObject):
    """
    Validation errors
    """

    OBJECT_NAME: ClassVar[
        Literal["privacy.redaction_job_validation_error"]
    ] = "privacy.redaction_job_validation_error"
    code: str
    erroring_object: Optional[Dict[str, str]]
    id: str
    """
    Unique identifier for the object.
    """
    message: str
    object: Literal["privacy.redaction_job_validation_error"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
