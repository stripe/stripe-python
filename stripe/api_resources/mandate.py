# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class Mandate(APIResource["Mandate"]):
    """
    A Mandate is a record of the permission that your customer gives you to debit their payment method.
    """

    OBJECT_NAME = "mandate"
    if TYPE_CHECKING:

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    customer_acceptance: StripeObject
    id: str
    livemode: bool
    multi_use: Optional[StripeObject]
    object: Literal["mandate"]
    on_behalf_of: Optional[str]
    payment_method: ExpandableField["PaymentMethod"]
    payment_method_details: StripeObject
    single_use: Optional[StripeObject]
    status: Literal["active", "inactive", "pending"]
    type: Literal["multi_use", "single_use"]

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Mandate.RetrieveParams"]
    ) -> "Mandate":
        instance = cls(id, **params)
        instance.refresh()
        return instance
