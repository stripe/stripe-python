# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class BatchJobCreateParams(TypedDict):
    endpoint: "BatchJobCreateParamsEndpoint"
    """
    The endpoint configuration for the batch job.
    """
    maximum_rps: NotRequired[int]
    """
    Optional field that allows the user to control how fast they want this batch job to run.
    Gives them a control over the number of webhooks they receive.
    """
    metadata: "Dict[str, str]|UntypedStripeObject[str]"
    """
    The metadata of the `batch_job`.
    """
    notification_suppression: NotRequired[
        "BatchJobCreateParamsNotificationSuppression"
    ]
    """
    Notification suppression settings for the batch job.
    """
    skip_validation: bool
    """
    Allows the user to skip validation.
    """


class BatchJobCreateParamsEndpoint(TypedDict):
    http_method: Literal["post"]
    """
    The HTTP method to use when calling the endpoint.
    """
    path: Literal[
        "/v1/accounts/:account",
        "/v1/credit_notes",
        "/v1/customers/:customer",
        "/v1/invoices/:invoice",
        "/v1/invoices/:invoice/pay",
        "/v1/promotion_codes",
        "/v1/promotion_codes/:promotion_code",
        "/v1/subscriptions/:subscription_exposed_id",
        "/v1/subscriptions/:subscription/migrate",
        "/v1/subscription_schedules",
        "/v1/subscription_schedules/:schedule",
        "/v1/subscription_schedules/:schedule/cancel",
    ]
    """
    The path of the endpoint to run this batch job against.
    In the form used in the documentation. For instance, for
    subscription migration this would be `/v1/subscriptions/:id/migrate`.
    """


class BatchJobCreateParamsNotificationSuppression(TypedDict):
    scope: Literal["all", "none"]
    """
    The scope of notification suppression.
    """
