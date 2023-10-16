# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

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
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    created: int
    data_load_time: int
    error: Optional[StripeObject]
    file: Optional["File"]
    id: str
    livemode: bool
    object: Literal["scheduled_query_run"]
    result_available_until: int
    sql: str
    status: str
    title: str

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ScheduledQueryRun.ListParams"]
    ) -> ListObject["ScheduledQueryRun"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ScheduledQueryRun.RetrieveParams"]
    ) -> "ScheduledQueryRun":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/sigma/scheduled_query_runs"
