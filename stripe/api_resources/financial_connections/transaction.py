# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal


class Transaction(ListableAPIResource["Transaction"]):
    """
    A Transaction represents a real transaction that affects a Financial Connections Account balance.
    """

    OBJECT_NAME = "financial_connections.transaction"

    class StatusTransitions(StripeObject):
        posted_at: Optional[int]
        void_at: Optional[int]

    account: str
    amount: int
    currency: str
    description: str
    id: str
    livemode: bool
    object: Literal["financial_connections.transaction"]
    status: Literal["pending", "posted", "void"]
    status_transitions: StatusTransitions
    transacted_at: int
    transaction_refresh: str
    updated: int

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Transaction"]:
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

    _inner_class_types = {"status_transitions": StatusTransitions}
