# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import NotRequired, TypedDict

_InboundTransferCreateParamsBase = TypedDict(
    "InboundTransferCreateParams",
    {"from": "InboundTransferCreateParamsFrom"},
)


class InboundTransferCreateParams(_InboundTransferCreateParamsBase):
    amount: AmountParam
    """
    The amount, in specified currency, by which the FinancialAccount balance will increase due to the InboundTransfer.
    """
    description: NotRequired[str]
    """
    An optional, freeform description field intended to store metadata.
    """
    to: "InboundTransferCreateParamsTo"
    """
    Object containing details about where the funds will land.
    """


class InboundTransferCreateParamsFrom(TypedDict):
    currency: NotRequired[str]
    """
    An optional currency field used to specify which currency is debited from the Payment Method.
    Since many Payment Methods support only one currency, this field is optional.
    """
    payment_method: str
    """
    ID of the Payment Method using which IBT will be made.
    """


class InboundTransferCreateParamsTo(TypedDict):
    currency: str
    """
    The currency in which funds will land in.
    """
    financial_account: str
    """
    The FinancialAccount that funds will land in.
    """
