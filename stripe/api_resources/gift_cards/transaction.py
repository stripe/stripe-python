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
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
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

    OBJECT_NAME: ClassVar[
        Literal["gift_cards.transaction"]
    ] = "gift_cards.transaction"

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

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ConfirmParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreateParams(RequestOptions):
            amount: int
            """
            The amount of the transaction. A negative amount deducts funds, and a positive amount adds funds.
            """
            confirm: NotRequired["bool|None"]
            """
            Whether this is a confirmed transaction. A confirmed transaction immediately deducts from/adds to the `amount_available` on the gift card. Otherwise, it creates a held transaction that increments the `amount_held` on the gift card.
            """
            created_by: NotRequired["Transaction.CreateParamsCreatedBy|None"]
            """
            Related objects which created this transaction.
            """
            currency: str
            """
            The currency of the transaction. This must match the currency of the gift card.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            gift_card: str
            """
            The gift card to create a new transaction on.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            transfer_group: NotRequired["str|None"]
            """
            A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
            """

        class CreateParamsCreatedBy(TypedDict):
            payment: "Transaction.CreateParamsCreatedByPayment"
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
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            gift_card: NotRequired["str|None"]
            """
            The gift card to list transactions for.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            transfer_group: NotRequired["str|None"]
            """
            A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
            """

        class ModifyParams(RequestOptions):
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: Optional[int]
    """
    The amount of this transaction. A positive value indicates that funds were added to the gift card. A negative value indicates that funds were removed from the gift card.
    """
    confirmed_at: Optional[int]
    """
    Time at which the transaction was confirmed. Measured in seconds since the Unix epoch.
    """
    created: Optional[int]
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: Optional[CreatedBy]
    """
    The related Stripe objects that created this gift card transaction.
    """
    currency: Optional[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    gift_card: Optional[str]
    """
    The gift card that this transaction occurred on
    """
    id: str
    """
    Unique identifier for the object.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["gift_cards.transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Optional[Literal["canceled", "confirmed", "held", "invalid"]]
    """
    Status of this transaction, one of `held`, `confirmed`, or `canceled`.
    """
    transfer_group: Optional[str]
    """
    A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
    """

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CancelParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            cls._static_request(
                "post",
                "/v1/gift_cards/transactions/{id}/cancel".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.CancelParams"]
    ) -> "Transaction":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.CancelParams"]
    ) -> "Transaction":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.CancelParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            self._request(
                "post",
                "/v1/gift_cards/transactions/{id}/cancel".format(
                    id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_confirm(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            cls._static_request(
                "post",
                "/v1/gift_cards/transactions/{id}/confirm".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def confirm(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ) -> "Transaction":
        ...

    @overload
    def confirm(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ) -> "Transaction":
        ...

    @class_method_variant("_cls_confirm")
    def confirm(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Transaction.ConfirmParams"]
    ) -> "Transaction":
        return cast(
            "Transaction",
            self._request(
                "post",
                "/v1/gift_cards/transactions/{id}/confirm".format(
                    id=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
        cls, id: str, **params: Unpack["Transaction.ModifyParams"]
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
