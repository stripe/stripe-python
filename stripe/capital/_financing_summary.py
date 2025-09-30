# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._singleton_api_resource import SingletonAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.capital._financing_summary_retrieve_params import (
        FinancingSummaryRetrieveParams,
    )


class FinancingSummary(SingletonAPIResource["FinancingSummary"]):
    """
    A financing object describes an account's current financing state. Used by Connect
    platforms to read the state of Capital offered to their connected accounts.
    """

    OBJECT_NAME: ClassVar[Literal["capital.financing_summary"]] = (
        "capital.financing_summary"
    )

    class Details(StripeObject):
        class CurrentRepaymentInterval(StripeObject):
            due_at: float
            """
            The time at which the minimum payment amount will be due. If not met through withholding, the Connected account's linked bank account or account balance will be debited.
            Given in seconds since unix epoch.
            """
            paid_amount: Optional[int]
            """
            The amount that has already been paid in the current repayment interval, in minor units. For example, $100 USD will be represented as 10000.
            """
            remaining_amount: int
            """
            The amount that is yet to be paid in the current repayment interval, in minor units. For example, $100 USD will be represented as 10000.
            """

        advance_amount: int
        """
        Amount of financing offered, in minor units. For example, $1,000 USD will be represented as 100000.
        """
        advance_paid_out_at: Optional[float]
        """
        The time at which the funds were paid out to the connected account's Stripe balance. Given in milliseconds since unix epoch.
        """
        currency: str
        """
        Currency that the financing offer is transacted in. For example, `usd`.
        """
        current_repayment_interval: Optional[CurrentRepaymentInterval]
        """
        The chronologically current repayment interval for the financing offer.
        """
        fee_amount: int
        """
        Fixed fee amount, in minor units. For example, $100 USD will be represented as 10000.
        """
        paid_amount: int
        """
        The amount the Connected account has paid toward the financing debt so far, in minor units. For example, $1,000 USD will be represented as 100000.
        """
        remaining_amount: int
        """
        The balance remaining to be paid on the financing, in minor units. For example, $1,000 USD will be represented as 100000.
        """
        repayments_begin_at: Optional[float]
        """
        The time at which Capital will begin withholding from payments. Given in seconds since unix epoch.
        """
        withhold_rate: float
        """
        Per-transaction rate at which Stripe will withhold funds to repay the financing.
        """
        _inner_class_types = {
            "current_repayment_interval": CurrentRepaymentInterval,
        }

    details: Optional[Details]
    """
    Additional information about the financing summary. Describes currency, advance amount,
    fee amount, withhold rate, remaining amount, paid amount, current repayment interval,
    repayment start date, and advance payout date.
    """
    financing_offer: Optional[str]
    """
    The Financing Offer ID this Financing Summary corresponds to
    """
    object: Literal["capital.financing_summary"]
    """
    The object type: financing_summary
    """
    status: Optional[Literal["accepted", "delivered", "none"]]
    """
    Status of the Connected Account's financing. [/v1/capital/financing_summary](https://stripe.com/docs/api/capital/financing_summary) will only return `details` for `paid_out` financing.
    """

    @classmethod
    def retrieve(
        cls, **params: Unpack["FinancingSummaryRetrieveParams"]
    ) -> "FinancingSummary":
        """
        Retrieve the financing state for the account that was authenticated in the request.
        """
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, **params: Unpack["FinancingSummaryRetrieveParams"]
    ) -> "FinancingSummary":
        """
        Retrieve the financing state for the account that was authenticated in the request.
        """
        instance = cls(None, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/capital/financing_summary"

    _inner_class_types = {"details": Details}
