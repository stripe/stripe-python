# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Any, Dict
from typing_extensions import NotRequired, TypedDict


class ReportRunCreateParams(TypedDict):
    report: str
    """
    The unique identifier of the `Report` being requested.
    """
    report_parameters: Dict[str, "Any"]
    """
    A map of parameter names to values, specifying how the report should be customized.
    The accepted parameters depend on the specific `Report` being run.
    """
    result_options: NotRequired["ReportRunCreateParamsResultOptions"]
    """
    Optional settings to customize the results of the `ReportRun`.
    """


class ReportRunCreateParamsResultOptions(TypedDict):
    compress_file: NotRequired[bool]
    """
    If set, the generated report file will be compressed into a ZIP folder.
    This is useful for reducing file size and download time for large reports.
    """
