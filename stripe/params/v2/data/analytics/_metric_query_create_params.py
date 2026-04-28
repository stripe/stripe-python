# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class MetricQueryCreateParams(TypedDict):
    currency: NotRequired[str]
    """
    Which currency to return monetary metric results in.
    """
    ends_at: str
    """
    Timestamp denoting the end of the time range to request data for.
    """
    filters: NotRequired["Dict[str, Any]|UntypedStripeObject[Any]"]
    """
    Which dimension values to filter on; keys are dimension names, values are arrays of dimension values to filter on.
    """
    granularity: Literal["day", "month", "week", "year"]
    """
    The time granularity to aggregate results by.
    """
    group_by: NotRequired[List[str]]
    """
    Which dimension keys to group by; if not specified no grouping is performed.
    """
    limit: NotRequired[int]
    """
    The maximum number of rows in the response.
    """
    metrics: List["MetricQueryCreateParamsMetric"]
    """
    A list of the metrics to be returned; all metrics must share the same metric namespace.
    """
    page: NotRequired[str]
    """
    Pagination future-proofing: page token for navigating to next/previous batch of rows.
    """
    starts_at: str
    """
    Timestamp denoting the beginning of the time range to request data for.
    """
    timezone: NotRequired[str]
    """
    The timezone results should be in; defaults to the merchant's timezone.
    """


class MetricQueryCreateParamsMetric(TypedDict):
    id: NotRequired[str]
    """
    The Gen6 ID for this metric, e.g. metric_61Sud3n5oAGVCWiSr5.
    """
    name: NotRequired[str]
    """
    The common name for this metric, e.g. mrr_minor_units.
    """
