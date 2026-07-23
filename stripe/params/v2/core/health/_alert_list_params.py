# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AlertListParams(TypedDict):
    created: NotRequired[str]
    """
    Filter for alerts created at the specified timestamp.
    """
    created_gt: NotRequired[str]
    """
    Filter for alerts created after the specified timestamp.
    """
    created_gte: NotRequired[str]
    """
    Filter for alerts created on or after the specified timestamp.
    """
    created_lt: NotRequired[str]
    """
    Filter for alerts created before the specified timestamp.
    """
    created_lte: NotRequired[str]
    """
    Filter for alerts created on or before the specified timestamp.
    """
    limit: NotRequired[int]
    """
    The page limit.
    """
    severity: NotRequired["Literal['critical', 'non_critical']|str"]
    """
    Filter by alert severity.
    """
    status: NotRequired["Literal['open', 'resolved']|str"]
    """
    Filter by alert status.
    """
    types: NotRequired[
        List[
            Union[
                Literal[
                    "api_error",
                    "api_latency",
                    "authorization_rate_drop",
                    "elements_error",
                    "event_generation_failure",
                    "fraud_rate",
                    "invoice_count_dropped",
                    "issuing_authorization_request_errors",
                    "issuing_authorization_request_timeout",
                    "meter_event_summaries_delayed",
                    "metronome_notification_latency",
                    "payment_method_error",
                    "sepa_debit_delayed",
                    "traffic_volume_drop",
                    "webhook_latency",
                ],
                str,
            ]
        ]
    ]
    """
    Filter by alert types.
    """
