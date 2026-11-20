# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class EvaluationOutcomeListParams(TypedDict):
    account_details: "EvaluationOutcomeListParamsAccountDetails"
    """
    Account selector for the historical outcomes requested.
    """
    limit: NotRequired[int]
    """
    Maximum number of results per page. Defaults to 10; use 1 for the latest matching outcome.
    """
    origin: NotRequired["Literal['rule_outcome', 'stripe_recommendation']|str"]
    """
    Evaluation origin to filter by. Omit to match all origins.
    """
    type: NotRequired["Literal['delinquency']|str"]
    """
    Evaluation type to filter by. Omit to match all types.
    """


class EvaluationOutcomeListParamsAccountDetails(TypedDict):
    account: NotRequired[str]
    """
    The v2 account ID to list evaluation outcomes for.
    """
