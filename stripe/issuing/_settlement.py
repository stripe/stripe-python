# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class Settlement(StripeObject):
    """
    When a non-stripe BIN is used, any use of an [issued card](https://stripe.com/docs/issuing) must be settled directly with the card network. The net amount owed is represented by an Issuing `Settlement` object.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.settlement"]] = "issuing.settlement"
    bin: str
    """
    The Bank Identification Number reflecting this settlement record.
    """
    clearing_date: int
    """
    The date that the transactions are cleared and posted to user's accounts.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    id: str
    """
    Unique identifier for the object.
    """
    interchange_fees_amount: int
    """
    The total interchange received as reimbursement for the transactions.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    net_total_amount: int
    """
    The total net amount required to settle with the network.
    """
    network: Literal["maestro", "visa"]
    """
    The card network for this settlement report. One of ["visa", "maestro"]
    """
    network_fees_amount: int
    """
    The total amount of fees owed to the network.
    """
    network_settlement_identifier: str
    """
    The Settlement Identification Number assigned by the network.
    """
    object: Literal["issuing.settlement"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    other_fees_amount: Optional[int]
    """
    The total amount of any additional fees assessed by the card network.
    """
    other_fees_count: Optional[int]
    """
    The total number of additional fees assessed by the card network.
    """
    settlement_service: str
    """
    One of `international` or `uk_national_net`.
    """
    status: Literal["complete", "pending"]
    """
    The current processing status of this settlement.
    """
    transaction_amount: int
    """
    The total transaction amount reflected in this settlement.
    """
    transaction_count: int
    """
    The total number of transactions reflected in this settlement.
    """
