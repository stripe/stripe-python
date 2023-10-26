# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class FinancingTransaction(ListableAPIResource["FinancingTransaction"]):
    """
    This is an object representing the details of a transaction on a Capital financing object.
    """

    OBJECT_NAME: ClassVar[
        Literal["capital.financing_transaction"]
    ] = "capital.financing_transaction"

    class Details(StripeObject):
        class Transaction(StripeObject):
            charge: Optional[str]
            """
            The linked payment ID.
            """
            treasury_transaction: Optional[str]
            """
            The linked Treasury Financing Transaction ID.
            """

        advance_amount: int
        """
        The advance amount being repaid, paid out, or reversed in minor units.
        """
        currency: str
        """
        The currency of the financing transaction.
        """
        fee_amount: int
        """
        The fee amount being repaid, paid out, or reversed in minor units.
        """
        linked_payment: Optional[str]
        """
        The linked payment for the transaction. This field only applies to financing transactions of type `paydown` and reason `automatic_withholding`.
        """
        reason: Optional[
            Literal[
                "automatic_withholding",
                "automatic_withholding_refund",
                "collection",
                "collection_failure",
                "financing_cancellation",
                "refill",
                "requested_by_user",
                "user_initiated",
            ]
        ]
        """
        The reason for the financing transaction (if applicable).
        """
        reversed_transaction: Optional[str]
        """
        The reversed transaction. This field only applies to financing
        transactions of type `reversal`.
        """
        total_amount: int
        """
        The advance and fee amount being repaid, paid out, or reversed in minor units.
        """
        transaction: Optional[Transaction]
        """
        This is an object representing a linked transaction on a Capital Financing Transaction.
        """
        _inner_class_types = {"transaction": Transaction}

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            charge: NotRequired["str|None"]
            """
            For transactions of type `paydown` and reason `automatic_withholding` only, only returns transactions that were created as a result of this charge.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            financing_offer: NotRequired["str|None"]
            """
            Returns transactions that were created that apply to this financing offer ID.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            reversed_transaction: NotRequired["str|None"]
            """
            Only returns transactions that are responsible for reversing this financing transaction ID.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            treasury_transaction: NotRequired["str|None"]
            """
            For transactions of type `paydown` and reason `automatic_withholding` only, only returns transactions that were created as a result of this Treasury Transaction.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    account: str
    """
    The ID of the merchant associated with this financing transaction.
    """
    created_at: int
    """
    Time at which the financing transaction was created. Given in seconds since unix epoch.
    """
    details: Details
    """
    This is an object representing a transaction on a Capital financing offer.
    """
    financing_offer: Optional[str]
    """
    The Capital financing offer for this financing transaction.
    """
    id: str
    """
    A unique identifier for the financing transaction object.
    """
    legacy_balance_transaction_source: Optional[str]
    """
    The Capital transaction object that predates the Financing Transactions API and
    corresponds with the balance transaction that was created as a result of this
    financing transaction.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["capital.financing_transaction"]
    """
    The object type: financing_transaction
    """
    type: Literal["payment", "payout", "reversal"]
    """
    The type of the financing transaction.
    """
    user_facing_description: Optional[str]
    """
    A human-friendly description of the financing transaction.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancingTransaction.ListParams"]
    ) -> ListObject["FinancingTransaction"]:
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
    def retrieve(
        cls, id: str, **params: Unpack["FinancingTransaction.RetrieveParams"]
    ) -> "FinancingTransaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"details": Details}
