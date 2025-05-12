# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class RedactionJobValidationError(StripeObject):
    """
    The Redaction Job validation error object contains information about
    errors that affect the ability to redact a specific object in a
    redaction job.
    """

    OBJECT_NAME: ClassVar[
        Literal["privacy.redaction_job_validation_error"]
    ] = "privacy.redaction_job_validation_error"
    code: Literal[
        "invalid_cascading_source",
        "invalid_file_purpose",
        "invalid_state",
        "locked_by_other_job",
        "too_many_objects",
    ]
    """
    A code indicating the reason for the error.
    """
    erroring_object: Optional[Dict[str, str]]
    """
    If the error is related to a specific object, this field will include the object's identifier in `id` and object type in `object`.
    """
    id: str
    """
    Unique identifier for the object.
    """
    message: str
    """
    A human-readable message providing more details about the error.
    """
    object: Literal["privacy.redaction_job_validation_error"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
