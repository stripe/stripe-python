# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressCreditParams(TypedDict):
    amount: AmountParam
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
