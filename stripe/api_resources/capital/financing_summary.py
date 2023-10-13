# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import SingletonAPIResource
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class FinancingSummary(SingletonAPIResource["FinancingSummary"]):
    """
    A financing object describes an account's current financing state. Used by Connect
    platforms to read the state of Capital offered to their connected accounts.
    """

    OBJECT_NAME = "capital.financing_summary"

    class Details(StripeObject):
        class CurrentRepaymentInterval(StripeObject):
            due_at: int
            paid_amount: Optional[int]
            remaining_amount: int

        advance_amount: int
        advance_paid_out_at: Optional[int]
        currency: str
        current_repayment_interval: Optional[CurrentRepaymentInterval]
        fee_amount: int
        paid_amount: int
        remaining_amount: int
        repayments_begin_at: Optional[int]
        withhold_rate: float
        _inner_class_types = {
            "current_repayment_interval": CurrentRepaymentInterval,
        }

    if TYPE_CHECKING:

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    details: Optional[Details]
    financing_offer: Optional[str]
    object: Literal["capital.financing_summary"]
    status: Optional[Literal["accepted", "delivered", "none"]]

    @classmethod
    def retrieve(
        cls, **params: Unpack["FinancingSummary.RetrieveParams"]
    ) -> "FinancingSummary":
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/capital/financing_summary"

    _inner_class_types = {"details": Details}
