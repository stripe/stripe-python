# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, TypedDict


class BatchJobCreateParams(TypedDict):
    endpoint: Literal[
        "/v1/subscription_schedules",
        "/v1/customers/:customer",
        "/v1/subscriptions/:subscription_exposed_id",
    ]
    """
    The API endpoint to batch (e.g., /v1/customers/:id for batch customer updates).
    """
