# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.file import File


class ScheduledQueryRun(ListableAPIResource["ScheduledQueryRun"]):
    """
    If you have [scheduled a Sigma query](https://stripe.com/docs/sigma/scheduled-queries), you'll
    receive a `sigma.scheduled_query_run.created` webhook each time the query
    runs. The webhook contains a `ScheduledQueryRun` object, which you can use to
    retrieve the query results.
    """

    OBJECT_NAME = "scheduled_query_run"
    created: str
    data_load_time: str
    error: StripeObject
    file: Optional["File"]
    id: str
    livemode: bool
    object: Literal["scheduled_query_run"]
    result_available_until: str
    sql: str
    status: str
    title: str

    @classmethod
    def class_url(cls):
        return "/v1/sigma/scheduled_query_runs"
