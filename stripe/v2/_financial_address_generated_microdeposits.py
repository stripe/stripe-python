# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class FinancialAddressGeneratedMicrodeposits(StripeObject):
    OBJECT_NAME: ClassVar[
        Literal["financial_address_generated_microdeposits"]
    ] = "financial_address_generated_microdeposits"

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    amounts: List[Amount]
    """
    The amounts of the microdeposits that were generated.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["financial_address_generated_microdeposits"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["accepted"]
    """
    Closed Enum. The status of the request.
    """
    _inner_class_types = {"amounts": Amount}
