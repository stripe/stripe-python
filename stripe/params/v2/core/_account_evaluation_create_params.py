# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountEvaluationCreateParams(TypedDict):
    account: NotRequired[str]
    """
    The account ID to evaluate. Exactly one of account or account_data must be provided.
    """
    account_data: NotRequired["AccountEvaluationCreateParamsAccountData"]
    """
    Account data for entity-less evaluation. Exactly one of account or account_data must be provided.
    """
    signals: List[Literal["fraudulent_website"]]
    """
    List of signals to evaluate.
    """


class AccountEvaluationCreateParamsAccountData(TypedDict):
    defaults: NotRequired["AccountEvaluationCreateParamsAccountDataDefaults"]
    """
    Default account settings.
    """
    identity: NotRequired["AccountEvaluationCreateParamsAccountDataIdentity"]
    """
    Identity data.
    """


class AccountEvaluationCreateParamsAccountDataDefaults(TypedDict):
    profile: "AccountEvaluationCreateParamsAccountDataDefaultsProfile"
    """
    Account profile data.
    """


class AccountEvaluationCreateParamsAccountDataDefaultsProfile(TypedDict):
    business_url: str
    """
    The business URL.
    """
    doing_business_as: NotRequired[str]
    """
    Doing business as (DBA) name.
    """
    product_description: NotRequired[str]
    """
    Description of the account's product or service.
    """


class AccountEvaluationCreateParamsAccountDataIdentity(TypedDict):
    business_details: (
        "AccountEvaluationCreateParamsAccountDataIdentityBusinessDetails"
    )
    """
    Business details for identity data.
    """


class AccountEvaluationCreateParamsAccountDataIdentityBusinessDetails(
    TypedDict,
):
    registered_name: NotRequired[str]
    """
    Registered business name.
    """
