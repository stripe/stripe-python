# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            currency: str
            description: NotRequired["str|None"]
            destination: str
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            source_transaction: NotRequired["str|None"]
            source_type: NotRequired[
                "Literal['bank_account', 'card', 'fpx']|None"
            ]
            transfer_group: NotRequired["str|None"]

        class ListParams(RequestOptions):
            created: NotRequired["Transfer.ListParamsCreated|int|None"]
            destination: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            transfer_group: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateReversalParams(RequestOptions):
            amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            refund_application_fee: NotRequired["bool|None"]

        class RetrieveReversalParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyReversalParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ListReversalsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

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
