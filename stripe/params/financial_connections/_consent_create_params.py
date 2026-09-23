# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ConsentCreateParams(RequestOptions):
    account_holder: "ConsentCreateParamsAccountHolder"
    """
    The account holder for whom the Consent is issued.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    locale: NotRequired[str]
    """
    The customer's preferred locale for the consent text, expressed as a BCP 47 language tag. If omitted, Stripe uses the default locale.
    """


class ConsentCreateParamsAccountHolder(TypedDict):
    account: NotRequired[str]
    """
    The ID of the Account for whom the Consent is issued. Required when `type` is `account`.
    """
    customer: NotRequired[str]
    """
    The ID of the Customer for whom the Consent is issued. Required when `type` is `customer` unless `customer_account` is provided.
    """
    customer_account: NotRequired[str]
    """
    The ID of an Account representing the Customer for whom the Consent is issued. Required when `type` is `customer` unless `customer` is provided.
    """
    type: Union[Literal["account", "customer"], str]
    """
    The type of account holder for whom the Consent is issued.
    """
