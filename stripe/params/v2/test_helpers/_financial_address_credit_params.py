# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreditParams(TypedDict):
    amount: "FinancialAddressCreditParamsAmount"
    """
    Object containing the amount value and currency to credit.
    """
    network: Literal["ach", "fps", "rtp", "sepa_credit_transfer", "wire"]
    """
    Open Enum. The network to use in simulating the funds flow. This will be the reflected in the resulting ReceivedCredit.
    """
    statement_descriptor: NotRequired[str]
    """
    String explaining funds flow. Use this field to populate the statement descriptor of the ReceivedCredit created as an eventual result of this simulation.
    """


class FinancialAddressCreditParamsAmount(TypedDict):
    value: NotRequired[int]
    """
    A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
