# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class PaymentProfile(StripeObject):
    """
    A customer's payment method and its usage limits.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.payment_profile"]] = (
        "v2.provisioning.payment_profile"
    )

    class Provider(StripeObject):
        class UsageLimits(StripeObject):
            currency: str
            """
            Three-letter ISO currency code for `max_amount`.
            """
            max_amount: int
            """
            Maximum amount that can be charged per recurring interval.
            """
            recurring_interval: Literal["month", "week", "year"]
            """
            Interval over which `max_amount` applies.
            """
            _field_encodings = {"max_amount": "int64_string"}

        provider: str
        """
        Provider the payment method is shared with.
        """
        usage_limits: Optional[UsageLimits]
        """
        Usage limit applied to the payment method for this provider.
        """
        _inner_class_types = {"usage_limits": UsageLimits}

    class UsageLimits(StripeObject):
        currency: str
        """
        Three-letter ISO currency code for `max_amount`.
        """
        max_amount: int
        """
        Maximum amount that can be charged per recurring interval.
        """
        recurring_interval: Literal["month", "week", "year"]
        """
        Interval over which `max_amount` applies.
        """
        _field_encodings = {"max_amount": "int64_string"}

    card_last4: str
    """
    Last 4 digits of the card on the payment method.
    """
    livemode: bool
    """
    Whether the payment method is in live mode.
    """
    object: Literal["v2.provisioning.payment_profile"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payment_method_owner: Optional[Literal["platform"]]
    """
    Owner of the payment method.
    """
    providers: List[Provider]
    """
    Providers the payment method is shared with, and their usage limits.
    """
    shared_with_providers: List[str]
    """
    Deprecated: use providers instead.
    """
    usage_limits: Optional[UsageLimits]
    """
    Usage limit applied to the payment method.
    """
    _inner_class_types = {"providers": Provider, "usage_limits": UsageLimits}
