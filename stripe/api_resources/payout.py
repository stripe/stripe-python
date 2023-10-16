# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card


class Payout(
    CreateableAPIResource["Payout"],
    ListableAPIResource["Payout"],
    UpdateableAPIResource["Payout"],
):
    """
    A `Payout` object is created when you receive funds from Stripe, or when you
    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](https://stripe.com/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    and list all payouts. Payouts are made on [varying
    schedules](https://stripe.com/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving payouts](https://stripe.com/docs/payouts)
    """

    OBJECT_NAME = "payout"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            currency: str
            description: NotRequired["str|None"]
            destination: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            method: NotRequired["Literal['instant', 'standard']|None"]
            source_type: NotRequired[
                "Literal['bank_account', 'card', 'fpx']|None"
            ]
            statement_descriptor: NotRequired["str|None"]

        class ListParams(RequestOptions):
            arrival_date: NotRequired["Payout.ListParamsArrivalDate|int|None"]
            created: NotRequired["Payout.ListParamsCreated|int|None"]
            destination: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsArrivalDate(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ReverseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]

    amount: int
    arrival_date: int
    automatic: bool
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    created: int
    currency: str
    description: Optional[str]
    destination: Optional[ExpandableField[Union["BankAccount", "Card"]]]
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_code: Optional[str]
    failure_message: Optional[str]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    method: str
    object: Literal["payout"]
    original_payout: Optional[ExpandableField["Payout"]]
    reconciliation_status: Literal[
        "completed", "in_progress", "not_applicable"
    ]
    reversed_by: Optional[ExpandableField["Payout"]]
    source_type: str
    statement_descriptor: Optional[str]
    status: str
    type: Literal["bank_account", "card"]

    @classmethod
    def _cls_cancel(
        cls,
        payout: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Payout.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payouts/{payout}/cancel".format(
                payout=util.sanitize_id(payout)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Payout.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/payouts/{payout}/cancel".format(
                payout=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Payout.CreateParams"]
    ) -> "Payout":
        return cast(
            "Payout",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Payout.ListParams"]
    ) -> ListObject["Payout"]:
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
    def modify(cls, id, **params: Unpack["Payout.ModifyParams"]) -> "Payout":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Payout",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Payout.RetrieveParams"]
    ) -> "Payout":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_reverse(
        cls,
        payout: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Payout.ReverseParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payouts/{payout}/reverse".format(
                payout=util.sanitize_id(payout)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reverse")
    def reverse(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Payout.ReverseParams"]
    ):
        return self._request(
            "post",
            "/v1/payouts/{payout}/reverse".format(
                payout=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
