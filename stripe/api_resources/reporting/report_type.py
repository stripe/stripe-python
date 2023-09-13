# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from typing import List
from typing import Optional
from typing_extensions import Literal


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
    data_available_end: str
    data_available_start: str
    default_columns: Optional[List[str]]
    id: str
    livemode: bool
    name: str
    object: Literal["reporting.report_type"]
    updated: str
    version: int
