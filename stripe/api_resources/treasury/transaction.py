# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction_entry import (
        TransactionEntry,
    )


class Transaction(ListableAPIResource["Transaction"]):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.transaction"]
    ] = "treasury.transaction"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired["Transaction.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            financial_account: str
            """
            Returns objects associated with this FinancialAccount.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            order_by: NotRequired["Literal['created', 'posted_at']|None"]
            """
            The results are in reverse chronological order by `created` or `posted_at`. The default is `created`.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired["Literal['open', 'posted', 'void']|None"]
            """
            Only return Transactions that have the given status: `open`, `posted`, or `void`.
            """
            status_transitions: NotRequired[
                "Transaction.ListParamsStatusTransitions|None"
            ]
            """
            A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified.
            """

        class ListParamsStatusTransitions(TypedDict):
            posted_at: NotRequired[
                "Transaction.ListParamsStatusTransitionsPostedAt|int|None"
            ]
            """
            Returns Transactions with `posted_at` within the specified range.
            """

        class ListParamsStatusTransitionsPostedAt(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: int
    """
    Amount (in cents) transferred.
    """
    balance_impact: StripeObject
    """
    Change to a FinancialAccount's balance
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: str
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    entries: Optional[ListObject["TransactionEntry"]]
    """
    A list of TransactionEntries that are part of this Transaction. This cannot be expanded in any list endpoints.
    """
    financial_account: str
    """
    The FinancialAccount associated with this object.
    """
    flow: Optional[str]
    """
    ID of the flow that created the Transaction.
    """
    flow_details: Optional[StripeObject]
    """
    Details of the flow that created the Transaction.
    """
    flow_type: Literal[
        "credit_reversal",
        "debit_reversal",
        "inbound_transfer",
        "issuing_authorization",
        "other",
        "outbound_payment",
        "outbound_transfer",
        "received_credit",
        "received_debit",
    ]
    """
    Type of the flow that created the Transaction.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["treasury.transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["open", "posted", "void"]
    """
    Status of the Transaction.
    """
    status_transitions: StripeObject

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
    def retrieve(
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance
