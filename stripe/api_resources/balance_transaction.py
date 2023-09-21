# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal


class BalanceTransaction(ListableAPIResource["BalanceTransaction"]):
    """
    Balance transactions represent funds moving through your Stripe account.
    Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

    Related guide: [Balance transaction types](https://stripe.com/docs/reports/balance-transaction-types)
    """

    OBJECT_NAME = "balance_transaction"
    amount: int
    available_on: int
    created: int
    currency: str
    description: Optional[str]
    exchange_rate: Optional[float]
    fee: int
    fee_details: List[StripeObject]
    id: str
    net: int
    object: Literal["balance_transaction"]
    reporting_category: str
    source: Optional[ExpandableField[Any]]
    status: str
    type: Literal[
        "adjustment",
        "advance",
        "advance_funding",
        "anticipation_repayment",
        "application_fee",
        "application_fee_refund",
        "charge",
        "connect_collection_transfer",
        "contribution",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "issuing_dispute",
        "issuing_transaction",
        "obligation_inbound",
        "obligation_outbound",
        "obligation_payout",
        "obligation_payout_failure",
        "obligation_reversal_inbound",
        "obligation_reversal_outbound",
        "payment",
        "payment_failure_refund",
        "payment_refund",
        "payment_reversal",
        "payout",
        "payout_cancel",
        "payout_failure",
        "refund",
        "refund_failure",
        "reserve_transaction",
        "reserved_funds",
        "stripe_fee",
        "stripe_fx_fee",
        "tax_fee",
        "topup",
        "topup_reversal",
        "transfer",
        "transfer_cancel",
        "transfer_failure",
        "transfer_refund",
    ]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["BalanceTransaction"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "BalanceTransaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
