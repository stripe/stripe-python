# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._invoice import Invoice
    from stripe.billing._credit_grant import CreditGrant
    from stripe.test_helpers._test_clock import TestClock


class CreditBalanceTransaction(
    ListableAPIResource["CreditBalanceTransaction"]
):
    """
    A credit balance transaction is a resource representing a transaction (either a credit or a debit) against an existing credit grant.
    """

    OBJECT_NAME: ClassVar[Literal["billing.credit_balance_transaction"]] = (
        "billing.credit_balance_transaction"
    )

    class Credit(StripeObject):
        class Amount(StripeObject):
            class Monetary(StripeObject):
                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: int
                """
                A positive integer representing the amount.
                """

            monetary: Optional[Monetary]
            """
            The monetary amount.
            """
            type: Literal["monetary"]
            """
            The type of this amount. We currently only support `monetary` billing credits.
            """
            _inner_class_types = {"monetary": Monetary}

        amount: Amount
        type: Literal["credits_granted"]
        """
        The type of credit transaction.
        """
        _inner_class_types = {"amount": Amount}

    class Debit(StripeObject):
        class Amount(StripeObject):
            class Monetary(StripeObject):
                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                value: int
                """
                A positive integer representing the amount.
                """

            monetary: Optional[Monetary]
            """
            The monetary amount.
            """
            type: Literal["monetary"]
            """
            The type of this amount. We currently only support `monetary` billing credits.
            """
            _inner_class_types = {"monetary": Monetary}

        class CreditsApplied(StripeObject):
            invoice: ExpandableField["Invoice"]
            """
            The invoice to which the billing credits were applied.
            """
            invoice_line_item: str
            """
            The invoice line item to which the billing credits were applied.
            """

        amount: Amount
        credits_applied: Optional[CreditsApplied]
        """
        Details of how the billing credits were applied to an invoice. Only present if `type` is `credits_applied`.
        """
        type: Literal["credits_applied", "credits_expired", "credits_voided"]
        """
        The type of debit transaction.
        """
        _inner_class_types = {
            "amount": Amount,
            "credits_applied": CreditsApplied,
        }

    class ListParams(RequestOptions):
        credit_grant: NotRequired[str]
        """
        The credit grant for which to fetch credit balance transactions.
        """
        customer: str
        """
        The customer for which to fetch credit balance transactions.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    credit: Optional[Credit]
    """
    Credit details for this credit balance transaction. Only present if type is `credit`.
    """
    credit_grant: ExpandableField["CreditGrant"]
    """
    The credit grant associated with this credit balance transaction.
    """
    debit: Optional[Debit]
    """
    Debit details for this credit balance transaction. Only present if type is `debit`.
    """
    effective_at: int
    """
    The effective time of this credit balance transaction.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["billing.credit_balance_transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this credit balance transaction belongs to.
    """
    type: Optional[Literal["credit", "debit"]]
    """
    The type of credit balance transaction (credit or debit).
    """

    @classmethod
    def list(
        cls, **params: Unpack["CreditBalanceTransaction.ListParams"]
    ) -> ListObject["CreditBalanceTransaction"]:
        """
        Retrieve a list of credit balance transactions
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
        cls, **params: Unpack["CreditBalanceTransaction.ListParams"]
    ) -> ListObject["CreditBalanceTransaction"]:
        """
        Retrieve a list of credit balance transactions
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
    def retrieve(
        cls,
        id: str,
        **params: Unpack["CreditBalanceTransaction.RetrieveParams"],
    ) -> "CreditBalanceTransaction":
        """
        Retrieves a credit balance transaction
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["CreditBalanceTransaction.RetrieveParams"],
    ) -> "CreditBalanceTransaction":
        """
        Retrieves a credit balance transaction
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"credit": Credit, "debit": Debit}
