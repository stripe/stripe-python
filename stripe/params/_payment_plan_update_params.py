# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentPlanUpdateParams(TypedDict):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    schedule: NotRequired["PaymentPlanUpdateParamsSchedule"]
    """
    The new schedule for this payment plan.
    """


class PaymentPlanUpdateParamsSchedule(TypedDict):
    amounts_due: "PaymentPlanUpdateParamsScheduleAmountsDue"
    """
    Required when type is 'amounts_due'.
    """
    type: Literal["amounts_due"]
    """
    The schedule type. Currently only 'amounts_due' is supported.
    """


class PaymentPlanUpdateParamsScheduleAmountsDue(TypedDict):
    amounts: List["PaymentPlanUpdateParamsScheduleAmountsDueAmount"]
    """
    The list of installment entries.
    """


class PaymentPlanUpdateParamsScheduleAmountsDueAmount(TypedDict):
    description: NotRequired[str]
    """
    Optional description for this installment.
    """
    due_date: NotRequired[
        "PaymentPlanUpdateParamsScheduleAmountsDueAmountDueDate"
    ]
    """
    When this installment is due.
    """
    fixed_amount: NotRequired[
        "PaymentPlanUpdateParamsScheduleAmountsDueAmountFixedAmount"
    ]
    """
    Required when type is 'fixed_amount'.
    """
    id: NotRequired[str]
    """
    Optional stable identifier for the installment entry.
    """
    percentage: NotRequired[float]
    """
    The installment percentage of the total. Required when type is 'percentage'.
    """
    type: Union[Literal["fixed_amount", "percentage"], str]
    """
    Either 'fixed_amount' or 'percentage'.
    """


class PaymentPlanUpdateParamsScheduleAmountsDueAmountDueDate(TypedDict):
    absolute: NotRequired[int]
    """
    Unix timestamp. Required when type is 'absolute'.
    """
    relative: NotRequired[
        "PaymentPlanUpdateParamsScheduleAmountsDueAmountDueDateRelative"
    ]
    """
    Required when type is 'relative'.
    """
    type: Union[Literal["absolute", "relative"], str]
    """
    Either 'absolute' or 'relative'.
    """


class PaymentPlanUpdateParamsScheduleAmountsDueAmountDueDateRelative(
    TypedDict
):
    count: int
    """
    The number of intervals after finalization.
    """
    interval: Union[Literal["day", "month", "week", "year"], str]
    """
    The interval unit.
    """


class PaymentPlanUpdateParamsScheduleAmountsDueAmountFixedAmount(TypedDict):
    amount: int
    """
    The installment amount in minor units.
    """
    currency: str
    """
    Three-letter ISO currency code.
    """
