# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class QueryRunCreateParams(TypedDict):
    dataset: Union[Literal["analytical"], str]
    """
    The dataset to query.
    """
    format: Union[Literal["csv"], str]
    """
    The file format for the result.
    """
    query: "QueryRunCreateParamsQuery"
    """
    The query to execute.
    """
    result_options: NotRequired["QueryRunCreateParamsResultOptions"]
    """
    Optional settings that customize the generated result file.
    """


class QueryRunCreateParamsQuery(TypedDict):
    sql: NotRequired[str]
    """
    Ad-hoc SQL to execute.
    """


class QueryRunCreateParamsResultOptions(TypedDict):
    compress_file: NotRequired[bool]
    """
    If set, the generated result file is compressed into a ZIP archive before
    it is stored. This applies only to downloadable file results.
    """
