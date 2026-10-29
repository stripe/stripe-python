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
    The amount and currency to credit to the FinancialAccount.
    """
    description: NotRequired[str]
    """
    An optional, freeform description field intended to store metadata.
    """
    to: "InboundTransferCreateParamsTo"
    """
    The FinancialAccount and currency to credit with the transferred funds.
    """


class InboundTransferCreateParamsFrom(TypedDict):
    currency: NotRequired[str]
    """
    An optional currency field used to specify which currency is debited from the Payment Method.
    Since many Payment Methods support only one currency, this field is optional.
    """
    payment_method: str
    """
    ID of the verified bank account credential to debit for this InboundTransfer (for example, `usba_`), not a Payments API `pm_` PaymentMethod.
    """


class InboundTransferCreateParamsTo(TypedDict):
    currency: str
    """
    The currency to credit to the FinancialAccount.
    """
    financial_account: str
    """
    The FinancialAccount that receives the funds.
    """
