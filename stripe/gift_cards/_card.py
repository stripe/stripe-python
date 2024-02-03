# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.gift_cards._transaction import Transaction


class Card(
    CreateableAPIResource["Card"],
    ListableAPIResource["Card"],
    UpdateableAPIResource["Card"],
):
    """
    A gift card represents a single gift card owned by a customer, including the
    remaining balance, gift card code, and whether or not it is active.
    """

    OBJECT_NAME: ClassVar[Literal["gift_cards.card"]] = "gift_cards.card"

    class CreatedBy(StripeObject):
        class Checkout(StripeObject):
            checkout_session: str
            """
            The Stripe CheckoutSession that created this object.
            """
            line_item: Optional[str]
            """
            The Stripe CheckoutSession LineItem that created this object.
            """

        class Order(StripeObject):
            line_item: Optional[str]
            """
            The Stripe Order LineItem that created this object.
            """
            order: str
            """
            The Stripe Order that created this object.
            """

        class Payment(StripeObject):
            payment_intent: str
            """
            The PaymentIntent that created this object.
            """

        checkout: Optional[Checkout]
        order: Optional[Order]
        payment: Optional[Payment]
        type: Literal["checkout", "order", "payment"]
        """
        The type of event that created this object.
        """
        _inner_class_types = {
            "checkout": Checkout,
            "order": Order,
            "payment": Payment,
        }

    class CreateParams(RequestOptions):
        active: NotRequired["bool"]
        """
        The active state for the new gift card, defaults to false. The active state can be updated after creation.
        """
        created_by: NotRequired["Card.CreateParamsCreatedBy"]
        """
        Related objects which created this gift card.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        initial_amount: NotRequired["int"]
        """
        The initial amount to load onto the new gift card, defaults to 0.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class CreateParamsCreatedBy(TypedDict):
        payment: "Card.CreateParamsCreatedByPayment"
        """
        The details for the payment that created this object.
        """
        type: Literal["payment"]
        """
        The type of event that created this object.
        """

    class CreateParamsCreatedByPayment(TypedDict):
        payment_intent: str
        """
        The PaymentIntent used to collect payment for this object.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        active: NotRequired["bool"]
        """
        The new active state for the gift card.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ValidateParams(RequestOptions):
        code: str
        """
        The gift card code to be validated.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        giftcard_pin: NotRequired["str"]
        """
        The pin associated with the gift card. Not all gift cards have pins.
        """

    active: bool
    """
    Whether this gift card can be used or not.
    """
    amount_available: int
    """
    The amount of funds available for new transactions.
    """
    amount_held: int
    """
    The amount of funds marked as held.
    """
    code: Optional[str]
    """
    Code used to redeem this gift card.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: Optional[CreatedBy]
    """
    The related Stripe objects that created this gift card.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    id: str
    """
    Unique identifier for the object.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["gift_cards.card"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    transactions: ListObject["Transaction"]
    """
    Transactions on this gift card.
    """

    @classmethod
    def create(cls, **params: Unpack["Card.CreateParams"]) -> "Card":
        """
        Creates a new gift card object.
        """
        return cast(
            "Card",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Card.CreateParams"]
    ) -> "Card":
        """
        Creates a new gift card object.
        """
        return cast(
            "Card",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(cls, **params: Unpack["Card.ListParams"]) -> ListObject["Card"]:
        """
        List gift cards for an account
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Card.ListParams"]
    ) -> ListObject["Card"]:
        """
        List gift cards for an account
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id: str, **params: Unpack["Card.ModifyParams"]) -> "Card":
        """
        Update a gift card
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Card",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Card.ModifyParams"]
    ) -> "Card":
        """
        Update a gift card
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Card",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Card.RetrieveParams"]
    ) -> "Card":
        """
        Retrieve a gift card by id
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Card.RetrieveParams"]
    ) -> "Card":
        """
        Retrieve a gift card by id
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def validate(cls, **params: Unpack["Card.ValidateParams"]) -> "Card":
        """
        Validates a gift card code, returning the matching gift card object if it exists.
        """
        return cast(
            "Card",
            cls._static_request(
                "post",
                "/v1/gift_cards/cards/validate",
                params=params,
            ),
        )

    @classmethod
    async def validate_async(
        cls, **params: Unpack["Card.ValidateParams"]
    ) -> "Card":
        """
        Validates a gift card code, returning the matching gift card object if it exists.
        """
        return cast(
            "Card",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/cards/validate",
                params=params,
            ),
        )

    _inner_class_types = {"created_by": CreatedBy}
