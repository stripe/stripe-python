# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ReportRunCreateParams(TypedDict):
    format: Union[Literal["csv"], str]
    """
    The file format for the result.
    """
    parameters: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    A map of parameter names to values, specifying how the report should be customized.
    The accepted parameters depend on the specific `Report` being run.
    """
    report: "ReportRunCreateParamsReport"
    """
    A reference to the `Report` to run, by ID or name.
    """
    result_options: NotRequired["ReportRunCreateParamsResultOptions"]
    """
    Optional settings that customize the generated result file.
    """


class ReportRunCreateParamsReport(TypedDict):
    id: NotRequired[str]
    """
    The unique identifier of the `Report`.
    """
    name: NotRequired[str]
    """
    The human-readable name of the `Report`.
    """


class ReportRunCreateParamsResultOptions(TypedDict):
    compress_file: NotRequired[bool]
    """
    If set, the generated result file is compressed into a ZIP archive before
    it is stored. This applies only to downloadable file results.
    """
