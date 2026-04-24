# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class QueryRunCreateParams(TypedDict):
    result_options: NotRequired["QueryRunCreateParamsResultOptions"]
    """
    Optional settings to customize the results of the `QueryRun`.
    """
    sql: str
    """
    The SQL to execute.
    """


class QueryRunCreateParamsResultOptions(TypedDict):
    compress_file: NotRequired[bool]
    """
    If set, the generated results file will be compressed into a ZIP folder.
    This is useful for reducing file size and download time for large results.
    """
