# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class ReportType(ListableAPIResource["ReportType"]):
    """
    The Report Type resource corresponds to a particular type of report, such as
    the "Activity summary" or "Itemized payouts" reports. These objects are
    identified by an ID belonging to a set of enumerated values. See
    [API Access to Reports documentation](https://stripe.com/docs/reporting/statements/api)
    for those Report Type IDs, along with required and optional parameters.

    Note that certain report types can only be run based on your live-mode data (not test-mode
    data), and will error when queried without a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).
    """

    OBJECT_NAME = "reporting.report_type"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    data_available_end: int
    data_available_start: int
    default_columns: Optional[List[str]]
    id: str
    livemode: bool
    name: str
    object: Literal["reporting.report_type"]
    updated: int
    version: int

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ReportType.ListParams"]
    ) -> ListObject["ReportType"]:
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
        cls, id: str, **params: Unpack["ReportType.RetrieveParams"]
    ) -> "ReportType":
        instance = cls(id, **params)
        instance.refresh()
        return instance
