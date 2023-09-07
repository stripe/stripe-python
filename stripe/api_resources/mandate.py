# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class Mandate(APIResource["Mandate"]):
    """
    A Mandate is a record of the permission a customer has given you to debit their payment method.
    """

    OBJECT_NAME = "mandate"
    customer_acceptance: StripeObject
    id: str
    livemode: bool
    multi_use: StripeObject
    object: Literal["mandate"]
    on_behalf_of: str
    payment_method: ExpandableField["PaymentMethod"]
    payment_method_details: StripeObject
    single_use: StripeObject
    status: str
    type: str
