# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class ContractTermQuantityChange(StripeObject):
    OBJECT_NAME: ClassVar[
        Literal["v2.billing.contract_term_quantity_change"]
    ] = "v2.billing.contract_term_quantity_change"
    contract: str
    """
    The ID of the parent contract.
    """
    created: str
    """
    When this quantity change was created.
    """
    effective_at: str
    """
    When the quantity change takes effect.
    """
    id: str
    """
    The ID of the quantity change.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.contract_term_quantity_change"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    quantity: Decimal
    """
    The quantity at the effective time.
    """
    term: str
    """
    The ID of the recurring-price term.
    """
    _field_encodings = {"quantity": "decimal_string"}
