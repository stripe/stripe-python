# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class MetricQueryResult(StripeObject):
    """
    The result of a metric query.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.analytics.metric_query_result"]] = (
        "v2.data.analytics.metric_query_result"
    )

    class Data(StripeObject):
        class Result(StripeObject):
            currency: Optional[str]
            """
            If this is a monetary metric, the currency it is returned in. Otherwise null.
            """
            metric: str
            """
            The Gen6 ID of this metric.
            """
            name: str
            """
            The common name of this metric.
            """
            value: int
            """
            The numeric value of this metric.
            """
            _field_encodings = {"value": "int64_string"}

        dimensions: UntypedStripeObject[str]
        """
        A hash of dimension type to dimension instance, if group_by was specified.
        """
        id: str
        """
        A unique identifier for this row.
        """
        results: List[Result]
        """
        Array of metric values returned from this query.
        """
        timestamp: str
        """
        Timestamp denoting the start of this time bucket.
        """
        _inner_class_types = {"results": Result}

    created: str
    """
    The timestamp at which this metric query result was created.
    """
    data: List[Data]
    """
    An array of timeseries data rows.
    """
    id: str
    """
    The unique identifier of this metric query result.
    """
    livemode: bool
    """
    Whether this query was run in live mode.
    """
    next_page_url: Optional[str]
    """
    Pagination future-proofing: URL to fetch the next page; always null for now.
    """
    object: Literal["v2.data.analytics.metric_query_result"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    previous_page_url: Optional[str]
    """
    Pagination future-proofing: URL to fetch the previous page; always null for now.
    """
    refreshed_at: str
    """
    A timestamp representing the freshness of the data this metric is aggregated from.
    """
    _inner_class_types = {"data": Data}
