# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import ClassVar, List, Optional
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

    OBJECT_NAME: ClassVar[
        Literal["reporting.report_type"]
    ] = "reporting.report_type"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    data_available_end: int
    """
    Most recent time for which this Report Type is available. Measured in seconds since the Unix epoch.
    """
    data_available_start: int
    """
    Earliest time for which this Report Type is available. Measured in seconds since the Unix epoch.
    """
    default_columns: Optional[List[str]]
    """
    List of column names that are included by default when this Report Type gets run. (If the Report Type doesn't support the `columns` parameter, this will be null.)
    """
    id: str
    """
    The [ID of the Report Type](https://stripe.com/docs/reporting/statements/api#available-report-types), such as `balance.summary.1`.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str
    """
    Human-readable name of the Report Type
    """
    object: Literal["reporting.report_type"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    updated: int
    """
    When this Report Type was latest updated. Measured in seconds since the Unix epoch.
    """
    version: int
    """
    Version of the Report Type. Different versions report with the same ID will have the same purpose, but may take different run parameters or have different result schemas.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ReportType.ListParams"]
    ) -> ListObject["ReportType"]:
        """
        Returns a full list of Report Types.
        """
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
        """
        Retrieves the details of a Report Type. (Certain report types require a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).)
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance
