# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class Mandate(APIResource["Mandate"]):
    """
    A Mandate is a record of the permission that your customer gives you to debit their payment method.
    """

    OBJECT_NAME: ClassVar[Literal["mandate"]] = "mandate"
    if TYPE_CHECKING:

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    customer_acceptance: StripeObject
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    multi_use: Optional[StripeObject]
    object: Literal["mandate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[str]
    """
    The account (if any) that the mandate is intended for.
    """
    payment_method: ExpandableField["PaymentMethod"]
    """
    ID of the payment method associated with this mandate.
    """
    payment_method_details: StripeObject
    single_use: Optional[StripeObject]
    status: Literal["active", "inactive", "pending"]
    """
    The mandate status indicates whether or not you can use it to initiate a payment.
    """
    type: Literal["multi_use", "single_use"]
    """
    The type of the mandate.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Mandate.RetrieveParams"]
    ) -> "Mandate":
        instance = cls(id, **params)
        instance.refresh()
        return instance
