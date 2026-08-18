# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentPlanCreateParams(RequestOptions):
    collects_on: List["PaymentPlanCreateParamsCollectsOn"]
    """
    The invoice(s) this payment plan collects on. Currently must contain exactly one invoice entry.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    schedule: "PaymentPlanCreateParamsSchedule"
    """
    The schedule defining how to split the invoice total into installments.
    """


class PaymentPlanCreateParamsCollectsOn(TypedDict):
    invoice_details: "PaymentPlanCreateParamsCollectsOnInvoiceDetails"
    """
    Details of the invoice this payment plan collects on.
    """
    type: Literal["invoice_details"]
    """
    The type of object this plan collects on. Currently always `invoice_details`.
    """


class PaymentPlanCreateParamsCollectsOnInvoiceDetails(TypedDict):
    invoice: str
    """
    The ID of the invoice.
    """


class PaymentPlanCreateParamsSchedule(TypedDict):
    amounts_due: "PaymentPlanCreateParamsScheduleAmountsDue"
    """
    Required when type is 'amounts_due'.
    """
    type: Literal["amounts_due"]
    """
    The schedule type. Currently only 'amounts_due' is supported.
    """


class PaymentPlanCreateParamsScheduleAmountsDue(TypedDict):
    amounts: List["PaymentPlanCreateParamsScheduleAmountsDueAmount"]
    """
    The list of installment entries.
    """


class PaymentPlanCreateParamsScheduleAmountsDueAmount(TypedDict):
    description: NotRequired[str]
    """
    Optional description for this installment.
    """
    due_date: NotRequired[
        "PaymentPlanCreateParamsScheduleAmountsDueAmountDueDate"
    ]
    """
    When this installment is due.
    """
    fixed_amount: NotRequired[
        "PaymentPlanCreateParamsScheduleAmountsDueAmountFixedAmount"
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


class PaymentPlanCreateParamsScheduleAmountsDueAmountDueDate(TypedDict):
    absolute: NotRequired[int]
    """
    Unix timestamp. Required when type is 'absolute'.
    """
    relative: NotRequired[
        "PaymentPlanCreateParamsScheduleAmountsDueAmountDueDateRelative"
    ]
    """
    Required when type is 'relative'.
    """
    type: Union[Literal["absolute", "relative"], str]
    """
    Either 'absolute' or 'relative'.
    """


class PaymentPlanCreateParamsScheduleAmountsDueAmountDueDateRelative(
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


class PaymentPlanCreateParamsScheduleAmountsDueAmountFixedAmount(TypedDict):
    amount: int
    """
    The installment amount in minor units.
    """
    currency: str
    """
    Three-letter ISO currency code.
    """
