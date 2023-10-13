# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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

if TYPE_CHECKING:
    from stripe.api_resources.gift_cards.transaction import Transaction


class Card(
    CreateableAPIResource["Card"],
    ListableAPIResource["Card"],
    UpdateableAPIResource["Card"],
):
    """
    A gift card represents a single gift card owned by a customer, including the
    remaining balance, gift card code, and whether or not it is active.
    """

    OBJECT_NAME = "gift_cards.card"

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

        class CreateParams(RequestOptions):
            active: NotRequired["bool|None"]
            created_by: NotRequired["Card.CreateParamsCreatedBy|None"]
            currency: str
            expand: NotRequired["List[str]|None"]
            initial_amount: NotRequired["int|None"]
            metadata: NotRequired["Dict[str, str]|None"]

        class CreateParamsCreatedBy(TypedDict):
            payment: "Card.CreateParamsCreatedByPayment"
            type: Literal["payment"]

        class CreateParamsCreatedByPayment(TypedDict):
            payment_intent: str

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ValidateParams(RequestOptions):
            code: str
            expand: NotRequired["List[str]|None"]
            giftcard_pin: NotRequired["str|None"]

    active: bool
    amount_available: int
    amount_held: int
    code: Optional[str]
    created: int
    created_by: Optional[CreatedBy]
    currency: str
    id: str
    metadata: Optional[Dict[str, str]]
    object: Literal["gift_cards.card"]
    transactions: ListObject["Transaction"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Card.CreateParams"]
    ) -> "Card":
        return cast(
            "Card",
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
        **params: Unpack["Card.ListParams"]
    ) -> ListObject["Card"]:
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
    def modify(cls, id, **params: Unpack["Card.ModifyParams"]) -> "Card":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Card",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Card.RetrieveParams"]
    ) -> "Card":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def validate(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Card.ValidateParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/gift_cards/cards/validate",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    _inner_class_types = {"created_by": CreatedBy}
