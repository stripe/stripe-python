# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.file import File


class ReportRun(
    CreateableAPIResource["ReportRun"],
    ListableAPIResource["ReportRun"],
):
    """
    The Report Run object represents an instance of a report type generated with
    specific run parameters. Once the object is created, Stripe begins processing the report.
    When the report has finished running, it will give you a reference to a file
    where you can retrieve your results. For an overview, see
    [API Access to Reports](https://stripe.com/docs/reporting/statements/api).

    Note that certain report types can only be run based on your live-mode data (not test-mode
    data), and will error when queried without a [live-mode API key](https://stripe.com/docs/keys#test-live-modes).
    """

    OBJECT_NAME = "reporting.report_run"

    class Parameters(StripeObject):
        columns: Optional[List[str]]
        connected_account: Optional[str]
        currency: Optional[str]
        interval_end: Optional[int]
        interval_start: Optional[int]
        payout: Optional[str]
        reporting_category: Optional[str]
        timezone: Optional[str]

    created: int
    error: Optional[str]
    id: str
    livemode: bool
    object: Literal["reporting.report_run"]
    parameters: Parameters
    report_type: str
    result: Optional["File"]
    status: str
    succeeded_at: Optional[int]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "ReportRun":
        return cast(
            "ReportRun",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["ReportRun"]:
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ReportRun":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"parameters": Parameters}
