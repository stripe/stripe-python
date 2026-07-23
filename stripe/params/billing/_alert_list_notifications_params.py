# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AlertListNotificationsParams(RequestOptions):
    action: NotRequired[Literal["recovered", "triggered"]]
    """
    Filter results to only include triggered or recovered notifications.
    """
    cadence: NotRequired[str]
    """
    Filter results to only include notifications for the given billing cadence.
    """
    customer: str
    """
    The customer to list notifications for.
    """
    ending_before: NotRequired[str]
    """
    A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    limit: NotRequired[int]
    """
    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    """
    meter: NotRequired[str]
    """
    Filter results to only include notifications for the given meter.
    """
    notified_at: NotRequired["AlertListNotificationsParamsNotifiedAt|int"]
    """
    Filter results according to when the notification was sent.
    """
    starting_after: NotRequired[str]
    """
    A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    """
    subscription: NotRequired[str]
    """
    Filter results to only include notifications for the given subscription.
    """


class AlertListNotificationsParamsNotifiedAt(TypedDict):
    gt: NotRequired[int]
    """
    Minimum value to filter by (exclusive)
    """
    gte: NotRequired[int]
    """
    Minimum value to filter by (inclusive)
    """
    lt: NotRequired[int]
    """
    Maximum value to filter by (exclusive)
    """
    lte: NotRequired[int]
    """
    Maximum value to filter by (inclusive)
    """
