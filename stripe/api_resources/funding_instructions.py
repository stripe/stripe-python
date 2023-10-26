# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class FundingInstructions(StripeObject):
    """
    Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) that is
    automatically applied to future invoices and payments using the `customer_balance` payment method.
    Customers can fund this balance by initiating a bank transfer to any account in the
    `financial_addresses` field.
    Related guide: [Customer balance funding instructions](https://stripe.com/docs/payments/customer-balance/funding-instructions)
    """

    OBJECT_NAME: ClassVar[
        Literal["funding_instructions"]
    ] = "funding_instructions"
    bank_transfer: StripeObject
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    funding_type: Literal["bank_transfer"]
    """
    The `funding_type` of the returned instructions
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["funding_instructions"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
