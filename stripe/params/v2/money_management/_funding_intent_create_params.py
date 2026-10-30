# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, Union
from typing_extensions import Literal, NotRequired, TypedDict


class FundingIntentCreateParams(TypedDict):
    amount: AmountParam
    """
    The amount to add to the destination.
    """
    check: NotRequired["FundingIntentCreateParamsCheck"]
    """
    Details for a check FundingIntent.
    """
    confirmation_method: NotRequired["Literal['automatic', 'manual']|str"]
    """
    How to confirm the FundingIntent after validation.
    """
    description: NotRequired[str]
    """
    An arbitrary string to attach to the FundingIntent.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of key-value pairs to attach to the FundingIntent.
    """
    settlement_timing: NotRequired["FundingIntentCreateParamsSettlementTiming"]
    """
    Controls when the funds become available after processing.
    """
    to: "FundingIntentCreateParamsTo"
    """
    The destination for the funds.
    """
    type: Union[Literal["check"], str]
    """
    The type of FundingIntent to create.
    """


class FundingIntentCreateParamsCheck(TypedDict):
    back_image: NotRequired[str]
    """
    The ID of a File containing the back image of the check.
    """
    front_image: NotRequired[str]
    """
    The ID of a File containing the front image of the check.
    """


class FundingIntentCreateParamsSettlementTiming(TypedDict):
    delay_days_override: NotRequired[int]
    """
    The number of days to delay the availability of funds after processing completes.
    """


class FundingIntentCreateParamsTo(TypedDict):
    currency: str
    """
    The currency of the destination FinancialAccount balance.
    """
    financial_account: str
    """
    The ID of the FinancialAccount that receives the funds.
    """
