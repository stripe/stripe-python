# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class BalanceTransferCreateParams(RequestOptions):
    amount: int
    """
    A positive integer representing how much to transfer in the smallest currency unit.
    """
    currency: Literal["eur", "gbp", "usd"]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    destination_balance: "BalanceTransferCreateParamsDestinationBalance"
    """
    The balance to which funds are transferred.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    source_balance: "BalanceTransferCreateParamsSourceBalance"
    """
    The balance from which funds are transferred, including details specific to the balance you choose.
    """


class BalanceTransferCreateParamsDestinationBalance(TypedDict):
    type: Literal["issuing", "payments"]
    """
    Destination balance type to push funds into for the Balance Transfer.
    """


class BalanceTransferCreateParamsSourceBalance(TypedDict):
    allocated_funds: NotRequired[
        "BalanceTransferCreateParamsSourceBalanceAllocatedFunds"
    ]
    type: Literal["allocated_funds", "issuing", "payments"]
    """
    Source balance type to pull funds from for the Balance Transfer.
    """


class BalanceTransferCreateParamsSourceBalanceAllocatedFunds(TypedDict):
    charge: str
    """
    The charge ID that the funds are originally sourced from. Required if `type` is `charge`.
    """
    type: Literal["charge"]
    """
    The type of object that the funds are originally sourced from. One of `charge`.
    """
