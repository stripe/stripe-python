# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class MeterUsageRow(StripeObject):
    OBJECT_NAME: ClassVar[Literal["billing.meter_usage_row"]] = (
        "billing.meter_usage_row"
    )
    bucket_end_time: int
    """
    Timestamp indicating the end of the bucket. Measured in seconds since the Unix epoch.
    """
    bucket_start_time: int
    """
    Timestamp indicating the start of the bucket. Measured in seconds since the Unix epoch.
    """
    bucket_value: float
    """
    The aggregated meter usage value for the specified bucket.
    """
    dimensions: Optional[Dict[str, str]]
    """
    A set of key-value pairs representing the dimensions of the meter usage.
    """
    id: str
    """
    Unique identifier for the object.
    """
    meter_id: Optional[str]
    """
    The unique identifier for the meter. Null if no meters were provided and usage was aggregated across all meters.
    """
    object: Literal["billing.meter_usage_row"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
