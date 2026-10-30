# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict, Union
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
    parameters: NotRequired["Dict[str, Any]|UntypedStripeObject[Any]"]
    """
    Named bind parameters for the query. Keys are parameter names referenced in
    the SQL (without any prefix). Omit this field for a non-parameterized query.
    Values are strings, integers, or booleans. Fractional numbers, timestamps,
    and dates should be passed as strings.
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
    Ad-hoc SQL to execute. The maximum length is 100,000 characters.
    """


class QueryRunCreateParamsResultOptions(TypedDict):
    compression: NotRequired["Literal['none', 'zip']|str"]
    """
    The compression applied to the generated result file. Defaults to `none`. This applies
    only to downloadable file results.
    """
