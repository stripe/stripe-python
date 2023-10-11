# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import SingletonAPIResource
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal


class Balance(SingletonAPIResource["Balance"]):
    """
    This is an object representing your Stripe balance. You can retrieve it to see
    the balance currently on your Stripe account.

    You can also retrieve the balance history, which contains a list of
    [transactions](https://stripe.com/docs/reporting/balance-transaction-types) that contributed to the balance
    (charges, payouts, and so forth).

    The available and pending amounts for each currency are broken down further by
    payment source types.

    Related guide: [Understanding Connect account balances](https://stripe.com/docs/connect/account-balances)
    """

    OBJECT_NAME = "balance"

    class Available(StripeObject):
        class SourceTypes(StripeObject):
            bank_account: Optional[int]
            card: Optional[int]
            fpx: Optional[int]

        amount: int
        currency: str
        source_types: Optional[SourceTypes]
        _inner_class_types = {"source_types": SourceTypes}

    class ConnectReserved(StripeObject):
        class SourceTypes(StripeObject):
            bank_account: Optional[int]
            card: Optional[int]
            fpx: Optional[int]

        amount: int
        currency: str
        source_types: Optional[SourceTypes]
        _inner_class_types = {"source_types": SourceTypes}

    class InstantAvailable(StripeObject):
        class SourceTypes(StripeObject):
            bank_account: Optional[int]
            card: Optional[int]
            fpx: Optional[int]

        amount: int
        currency: str
        source_types: Optional[SourceTypes]
        _inner_class_types = {"source_types": SourceTypes}

    class Issuing(StripeObject):
        class Available(StripeObject):
            class SourceTypes(StripeObject):
                bank_account: Optional[int]
                card: Optional[int]
                fpx: Optional[int]

            amount: int
            currency: str
            source_types: Optional[SourceTypes]
            _inner_class_types = {"source_types": SourceTypes}

        available: List[Available]
        _inner_class_types = {"available": Available}

    class Pending(StripeObject):
        class SourceTypes(StripeObject):
            bank_account: Optional[int]
            card: Optional[int]
            fpx: Optional[int]

        amount: int
        currency: str
        source_types: Optional[SourceTypes]
        _inner_class_types = {"source_types": SourceTypes}

    available: List[Available]
    connect_reserved: Optional[List[ConnectReserved]]
    instant_available: Optional[List[InstantAvailable]]
    issuing: Optional[Issuing]
    livemode: bool
    object: Literal["balance"]
    pending: List[Pending]

    @classmethod
    def retrieve(cls, **params: Any) -> "Balance":
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/balance"

    _inner_class_types = {
        "available": Available,
        "connect_reserved": ConnectReserved,
        "instant_available": InstantAvailable,
        "issuing": Issuing,
        "pending": Pending,
    }
