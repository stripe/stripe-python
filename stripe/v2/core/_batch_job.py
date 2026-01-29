# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class BatchJob(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.core.batch_job"]] = "v2.core.batch_job"
    id: str
    """
    Unique identifier for the batch job.
    """
    object: Literal["v2.core.batch_job"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    url: str
    """
    The URL to upload the JSONL file to.
    """
