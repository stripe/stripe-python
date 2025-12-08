# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe.params._balance_transfer_create_params import (
        BalanceTransferCreateParams,
    )


class BalanceTransfer(CreateableAPIResource["BalanceTransfer"]):
    """
    Balance transfers represent funds moving between balance types on your Stripe account.
    They currently support moving funds between your Stripe balance and your [Issuing](https://docs.stripe.com/issuing) balance and between your [Allocated Funds](https://docs.stripe.com/connect/funds-segregation) balance and your Stripe balance.
    """

    OBJECT_NAME: ClassVar[Literal["balance_transfer"]] = "balance_transfer"

    class DestinationBalance(StripeObject):
        class Issuing(StripeObject):
            balance_transaction: Optional[
                ExpandableField["BalanceTransaction"]
            ]
            """
            Identifier for the balance_transaction that increased the destination balance.
            """

        class Payments(StripeObject):
            balance_transaction: Optional[
                ExpandableField["BalanceTransaction"]
            ]
            """
            Identifier for the balance_transaction that increased the destination balance.
            """

        issuing: Optional[Issuing]
        payments: Optional[Payments]
        type: str
        """
        Destination balance type to adjust for the Balance Transfer. One of `payments`, `issuing`, or `allocated_funds`.
        """
        _inner_class_types = {"issuing": Issuing, "payments": Payments}

    class SourceBalance(StripeObject):
        class Issuing(StripeObject):
            balance_transaction: Optional[
                ExpandableField["BalanceTransaction"]
            ]
            """
            Identifier for the balance_transaction that decreased the source balance.
            """

        class Payments(StripeObject):
            balance_transaction: ExpandableField["BalanceTransaction"]
            """
            Identifier for the balance_transaction that decreased the source balance.
            """
            source_type: Optional[str]
            """
            The payments balance type that this BalanceTransfer pulled funds from. One of `card`, `fpx`, or `bank_account`.
            """

        issuing: Optional[Issuing]
        payments: Optional[Payments]
        type: str
        """
        Source balance type to adjust for the Balance Transfer. One of `payments`, `issuing`, or `allocated_funds`.
        """
        _inner_class_types = {"issuing": Issuing, "payments": Payments}

    amount: int
    """
    A positive integer representing how much was transferred in the smallest currency unit.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    destination_balance: Optional[DestinationBalance]
    """
    The balance that funds were transferred to.
    """
    hosted_regulatory_receipt_url: Optional[str]
    """
    A [hosted transaction receipt](https://docs.stripe.com/treasury/moving-money/regulatory-receipts) URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["balance_transfer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    source_balance: Optional[SourceBalance]
    """
    The balance that funds were transferred from. One of `card`, `fpx`, or `bank_account`.
    """

    @classmethod
    def create(
        cls, **params: Unpack["BalanceTransferCreateParams"]
    ) -> "BalanceTransfer":
        """
        Creates a balance transfer. For Issuing use cases, funds will be debited immediately from the source balance and credited to the destination balance immediately (if your account is based in the US) or next-business-day (if your account is based in the EU). For Segregated Separate Charges and Transfers use cases, funds will be debited immediately from the source balance and credited immediately to the destination balance.
        """
        return cast(
            "BalanceTransfer",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["BalanceTransferCreateParams"]
    ) -> "BalanceTransfer":
        """
        Creates a balance transfer. For Issuing use cases, funds will be debited immediately from the source balance and credited to the destination balance immediately (if your account is based in the US) or next-business-day (if your account is based in the EU). For Segregated Separate Charges and Transfers use cases, funds will be debited immediately from the source balance and credited immediately to the destination balance.
        """
        return cast(
            "BalanceTransfer",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {
        "destination_balance": DestinationBalance,
        "source_balance": SourceBalance,
    }
