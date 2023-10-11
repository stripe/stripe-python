# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.source import Source


class Topup(
    CreateableAPIResource["Topup"],
    ListableAPIResource["Topup"],
    UpdateableAPIResource["Topup"],
):
    """
    To top up your Stripe balance, you create a top-up object. You can retrieve
    individual top-ups, as well as list all top-ups. Top-ups are identified by a
    unique, random ID.

    Related guide: [Topping up your platform account](https://stripe.com/docs/connect/top-ups)
    """

    OBJECT_NAME = "topup"

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        amount: int
        currency: str
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        source: NotRequired[Optional[str]]
        statement_descriptor: NotRequired[Optional[str]]
        transfer_group: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        amount: NotRequired[Optional[Union["Topup.ListAmountParams", int]]]
        created: NotRequired[Optional[Union["Topup.ListCreatedParams", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[Literal["canceled", "failed", "pending", "succeeded"]]
        ]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ListAmountParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    amount: int
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    created: int
    currency: str
    description: Optional[str]
    expected_availability_date: Optional[int]
    failure_code: Optional[str]
    failure_message: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["topup"]
    source: Optional["Source"]
    statement_descriptor: Optional[str]
    status: Literal["canceled", "failed", "pending", "reversed", "succeeded"]
    transfer_group: Optional[str]

    @classmethod
    def _cls_cancel(
        cls,
        topup: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Topup.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/topups/{topup}/cancel".format(topup=util.sanitize_id(topup)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Topup.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/topups/{topup}/cancel".format(
                topup=util.sanitize_id(self.get("id"))
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
        **params: Unpack["Topup.CreateParams"]
    ) -> "Topup":
        return cast(
            "Topup",
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
        **params: Unpack["Topup.ListParams"]
    ) -> ListObject["Topup"]:
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
    def modify(cls, id, **params: Unpack["Topup.ModifyParams"]) -> "Topup":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Topup",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Topup.RetrieveParams"]
    ) -> "Topup":
        instance = cls(id, **params)
        instance.refresh()
        return instance
