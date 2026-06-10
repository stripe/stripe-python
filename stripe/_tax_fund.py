# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe.params._tax_fund_list_params import TaxFundListParams
    from stripe.params._tax_fund_retrieve_params import TaxFundRetrieveParams


class TaxFund(ListableAPIResource["TaxFund"]):
    """
    A TaxFund object represents a single tax float sweep event — funds moved between
    a merchant's payments balance and their tax fund financial account for Stripe Tax obligations.
    """

    OBJECT_NAME: ClassVar[Literal["tax_fund"]] = "tax_fund"

    class Context(StripeObject):
        checkout_session: Optional[str]
        credit_note: Optional[str]
        invoice: Optional[str]
        payment_intent: Optional[str]
        refund: Optional[str]
        tax_transaction: Optional[str]

    class Destination(StripeObject):
        class PaymentsBalance(StripeObject):
            balance_transaction: ExpandableField["BalanceTransaction"]

        class TaxFundAccount(StripeObject):
            financial_account: Optional[str]
            transaction: Optional[str]

        payments_balance: Optional[PaymentsBalance]
        """
        Details about the payments balance side of the sweep.
        """
        tax_fund_account: Optional[TaxFundAccount]
        """
        Details about the tax fund financial account side of the sweep.
        """
        type: str
        _inner_class_types = {
            "payments_balance": PaymentsBalance,
            "tax_fund_account": TaxFundAccount,
        }

    class Source(StripeObject):
        class PaymentsBalance(StripeObject):
            balance_transaction: ExpandableField["BalanceTransaction"]

        class TaxFundAccount(StripeObject):
            financial_account: Optional[str]
            transaction: Optional[str]

        payments_balance: Optional[PaymentsBalance]
        """
        Details about the payments balance side of the sweep.
        """
        tax_fund_account: Optional[TaxFundAccount]
        """
        Details about the tax fund financial account side of the sweep.
        """
        type: str
        _inner_class_types = {
            "payments_balance": PaymentsBalance,
            "tax_fund_account": TaxFundAccount,
        }

    class Trigger(StripeObject):
        balance_transaction: ExpandableField["BalanceTransaction"]
        type: str

    amount: int
    """
    Amount swept, in the smallest currency unit. Always positive.
    """
    context: Optional[Context]
    """
    Associated billing or tax documents for this sweep.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    destination: Destination
    """
    Where funds moved to.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["tax_fund"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    source: Source
    """
    Where funds moved from.
    """
    trigger: Trigger
    """
    What caused the sweep.
    """

    @classmethod
    def list(
        cls, **params: Unpack["TaxFundListParams"]
    ) -> ListObject["TaxFund"]:
        """
        Returns a list of tax funds in reverse chronological order.
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
        cls, **params: Unpack["TaxFundListParams"]
    ) -> ListObject["TaxFund"]:
        """
        Returns a list of tax funds in reverse chronological order.
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
        cls, id: str, **params: Unpack["TaxFundRetrieveParams"]
    ) -> "TaxFund":
        """
        Retrieves a tax fund object by its ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["TaxFundRetrieveParams"]
    ) -> "TaxFund":
        """
        Retrieves a tax fund object by its ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "context": Context,
        "destination": Destination,
        "source": Source,
        "trigger": Trigger,
    }
