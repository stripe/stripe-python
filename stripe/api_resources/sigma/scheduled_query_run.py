# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class ScheduledQueryRun(ListableAPIResource):
    """
    If you have [scheduled a Sigma query](https://stripe.com/docs/sigma/scheduled-queries), you'll
    receive a `sigma.scheduled_query_run.created` webhook each time the query
    runs. The webhook contains a `ScheduledQueryRun` object, which you can use to
    retrieve the query results.
    """

    OBJECT_NAME = "scheduled_query_run"

    @classmethod
    def class_url(cls):
        return "/v1/sigma/scheduled_query_runs"
