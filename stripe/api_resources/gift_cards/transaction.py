# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Transaction(
    CreateableAPIResource["Transaction"],
    ListableAPIResource["Transaction"],
    UpdateableAPIResource["Transaction"],
):
    """
    A gift card transaction represents a single transaction on a referenced gift card.
    A transaction is in one of three states, `confirmed`, `held` or `canceled`. A `confirmed`
    transaction is one that has added/deducted funds. A `held` transaction has created a
    temporary hold on funds, which can then be cancelled or confirmed. A `held` transaction
    can be confirmed into a `confirmed` transaction, or canceled into a `canceled` transaction.
    A `canceled` transaction has no effect on a gift card's balance.
    """

    OBJECT_NAME = "gift_cards.transaction"

    class CreatedBy(StripeObject):
        class Checkout(StripeObject):
            checkout_session: str
            line_item: Optional[str]

        class Order(StripeObject):
            line_item: Optional[str]
            order: str

        class Payment(StripeObject):
            payment_intent: str

        checkout: Optional[Checkout]
        order: Optional[Order]
        payment: Optional[Payment]
        type: Literal["checkout", "order", "payment"]
        _inner_class_types = {
            "checkout": Checkout,
            "order": Order,
            "payment": Payment,
        }

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ConfirmParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            confirm: NotRequired["bool|None"]
            created_by: NotRequired["Transaction.CreateParamsCreatedBy|None"]
            currency: str
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            gift_card: str
            metadata: NotRequired["Dict[str, str]|None"]
            transfer_group: NotRequired["str|None"]

        class CreateParamsCreatedBy(TypedDict):
            payment: "Transaction.CreateParamsCreatedByPayment"
            type: Literal["payment"]

        class CreateParamsCreatedByPayment(TypedDict):
            payment_intent: str

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            gift_card: NotRequired["str|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            transfer_group: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount: Optional[int]
    confirmed_at: Optional[int]
    created: Optional[int]
    created_by: Optional[CreatedBy]
    currency: Optional[str]
    description: Optional[str]
    gift_card: Optional[str]
    id: str
    metadata: Optional[Dict[str, str]]
    object: Literal["gift_cards.transaction"]
    status: Optional[Literal["canceled", "confirmed", "held", "invalid"]]
    transfer_group: Optional[str]

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/transactions/{id}/cancel".format(
                id=util.sanitize_id(id)
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
        **params: Unpack["Transaction.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/gift_cards/transactions/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/transactions/{id}/confirm".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ):
        return self._request(
            "post",
            "/v1/gift_cards/transactions/{id}/confirm".format(
                id=util.sanitize_id(self.get("id"))
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
        **params: Unpack["Transaction.CreateParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
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
        **params: Unpack["Transaction.ListParams"]
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

    @classmethod
    def modify(
        cls, id, **params: Unpack["Transaction.ModifyParams"]
    ) -> "Transaction":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Transaction",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"created_by": CreatedBy}
