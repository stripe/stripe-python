# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class FundingInstructions(StripeObject):
    """
    Each customer has a [`balance`](https://stripe.com/docs/api/customers/object#customer_object-balance) that is
    automatically applied to future invoices and payments using the `customer_balance` payment method.
    Customers can fund this balance by initiating a bank transfer to any account in the
    `financial_addresses` field.
    Related guide: [Customer balance funding instructions](https://stripe.com/docs/payments/customer-balance/funding-instructions)
    """

    OBJECT_NAME = "funding_instructions"
    bank_transfer: StripeObject
    currency: str
    funding_type: Literal["bank_transfer"]
    livemode: bool
    object: Literal["funding_instructions"]
