# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class SettlementAllocationIntent(StripeObject):
    """
    SettlementAllocationIntent resource.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.payments.settlement_allocation_intent"]
    ] = "v2.payments.settlement_allocation_intent"

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    class StatusDetails(StripeObject):
        class Errored(StripeObject):
            doc_url: Optional[str]
            """
            Stripe doc link to debug the issue.
            """
            message: str
            """
            User Message detailing the reason code and possible resolution .
            """
            reason_code: Literal["amount_mismatch"]
            """
            Open Enum. The `errored` status reason.
            """

        errored: Optional[Errored]
        """
        Hash that provides additional information regarding the reason behind a `errored` SettlementAllocationIntent status. It is only present when the SettlementAllocationIntent status is `errored`.
        """
        _inner_class_types = {"errored": Errored}

    amount: Amount
    """
    The amount and currency of the SettlementAllocationIntent.
    """
    created: str
    """
    Timestamp at which SettlementAllocationIntent was created .
    """
    expected_settlement_date: str
    """
    Date when we expect to receive the funds.
    """
    financial_account: str
    """
    FinancialAccount ID where the funds are expected.
    """
    id: str
    """
    Unique identifier for the SettlementAllocationIntent.
    """
    linked_credits: List[str]
    """
    List of ReceivedCredits that matched with the SettlementAllocationIntent.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Metadata associated with the SettlementAllocationIntent.
    """
    object: Literal["v2.payments.settlement_allocation_intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reference: str
    """
    Reference for the SettlementAllocationIntent. This is the transaction reference used by payments processor to send funds to Stripe .
    """
    status: Literal[
        "canceled", "errored", "matched", "pending", "settled", "submitted"
    ]
    """
    SettlementAllocationIntent status.
    """
    status_details: Optional[StatusDetails]
    """
    Status details for a SettlementAllocationIntent in `errored` state.
    """
    _inner_class_types = {"amount": Amount, "status_details": StatusDetails}
