# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.reversal import Reversal


@nested_resource_class_methods("reversal")
class Transfer(
    CreateableAPIResource["Transfer"],
    ListableAPIResource["Transfer"],
    UpdateableAPIResource["Transfer"],
):
    """
    A `Transfer` object is created when you move funds between Stripe accounts as
    part of Connect.

    Before April 6, 2017, transfers also represented movement of funds from a
    Stripe account to a card or bank account. This behavior has since been split
    out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
    information, read about the
    [transfer/payout split](https://stripe.com/docs/transfer-payout-split).

    Related guide: [Creating separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers)
    """

    OBJECT_NAME = "transfer"

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        currency: str
        description: NotRequired[Optional[str]]
        destination: str
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        source_transaction: NotRequired[Optional[str]]
        source_type: NotRequired[
            Optional[Literal["bank_account", "card", "fpx"]]
        ]
        transfer_group: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["Transfer.ListParamsCreated", int]]
        ]
        destination: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        transfer_group: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
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

    class CreateReversalParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        refund_application_fee: NotRequired[Optional[bool]]

    class RetrieveReversalParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyReversalParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ListReversalsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    amount: int
    amount_reversed: int
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    created: int
    currency: str
    description: Optional[str]
    destination: Optional[ExpandableField["Account"]]
    destination_payment: Optional[ExpandableField["Charge"]]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["transfer"]
    reversals: ListObject["Reversal"]
    reversed: bool
    source_transaction: Optional[ExpandableField["Charge"]]
    source_type: Optional[str]
    transfer_group: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transfer.CreateParams"]
    ) -> "Transfer":
        return cast(
            "Transfer",
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
        **params: Unpack["Transfer.ListParams"]
    ) -> ListObject["Transfer"]:
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
    def modify(
        cls, id, **params: Unpack["Transfer.ModifyParams"]
    ) -> "Transfer":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Transfer",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Transfer.RetrieveParams"]
    ) -> "Transfer":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def create_reversal(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transfer.CreateReversalParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/transfers/{id}/reversals".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_reversal(
        cls,
        transfer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transfer.RetrieveReversalParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/transfers/{transfer}/reversals/{id}".format(
                transfer=util.sanitize_id(transfer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_reversal(
        cls,
        transfer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transfer.ModifyReversalParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/transfers/{transfer}/reversals/{id}".format(
                transfer=util.sanitize_id(transfer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_reversals(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transfer.ListReversalsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/transfers/{id}/reversals".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
