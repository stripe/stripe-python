# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class OnrampSessionCheckoutParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    mandate_data: NotRequired["OnrampSessionCheckoutParamsMandateData"]
    """
    This hash contains details about the mandate to create
    """


class OnrampSessionCheckoutParamsMandateData(TypedDict):
    customer_acceptance: (
        "OnrampSessionCheckoutParamsMandateDataCustomerAcceptance"
    )
    """
    This hash contains details about the customer acceptance of the Mandate.
    """


class OnrampSessionCheckoutParamsMandateDataCustomerAcceptance(TypedDict):
    accepted_at: NotRequired[int]
    """
    The time at which the customer accepted the Mandate.
    """
    offline: NotRequired[
        "OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOffline"
    ]
    """
    If this is a Mandate accepted offline, this hash contains details about the offline acceptance.
    """
    online: NotRequired[
        "OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOnline"
    ]
    """
    If this is a Mandate accepted online, this hash contains details about the online acceptance.
    """
    type: Literal["offline", "online"]
    """
    The type of customer acceptance information included with the Mandate. One of `online` or `offline`.
    """


class OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOffline(
    TypedDict,
):
    pass


class OnrampSessionCheckoutParamsMandateDataCustomerAcceptanceOnline(
    TypedDict
):
    ip_address: str
    """
    The IP address from which the Mandate was accepted by the customer.
    """
    user_agent: str
    """
    The user agent of the browser from which the Mandate was accepted by the customer.
    """
