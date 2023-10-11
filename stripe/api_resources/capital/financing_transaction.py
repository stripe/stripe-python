# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal


class FinancingTransaction(ListableAPIResource["FinancingTransaction"]):
    """
    This is an object representing the details of a transaction on a Capital financing object.
    """

    OBJECT_NAME = "capital.financing_transaction"

    class Details(StripeObject):
        class Transaction(StripeObject):
            charge: Optional[str]
            treasury_transaction: Optional[str]

        advance_amount: int
        currency: str
        fee_amount: int
        linked_payment: Optional[str]
        reason: Optional[
            Literal[
                "automatic_withholding",
                "automatic_withholding_refund",
                "collection",
                "collection_failure",
                "financing_cancellation",
                "refill",
                "requested_by_user",
                "user_initiated",
            ]
        ]
        reversed_transaction: Optional[str]
        total_amount: int
        transaction: Optional[Transaction]
        _inner_class_types = {"transaction": Transaction}

    account: str
    created_at: int
    details: Details
    financing_offer: Optional[str]
    id: str
    legacy_balance_transaction_source: Optional[str]
    livemode: bool
    object: Literal["capital.financing_transaction"]
    type: Literal["payment", "payout", "reversal"]
    user_facing_description: Optional[str]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["FinancingTransaction"]:
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
    ) -> "FinancingTransaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"details": Details}
