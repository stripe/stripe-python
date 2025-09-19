# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing._licensed_item import LicensedItem


class LicenseFee(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.license_fee"]] = (
        "v2.billing.license_fee"
    )

    class Tier(StripeObject):
        flat_amount: Optional[str]
        """
        Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
        """
        unit_amount: Optional[str]
        """
        Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
        most 12 decimal places.
        """
        up_to_decimal: Optional[str]
        """
        Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
        be set.
        """
        up_to_inf: Optional[Literal["inf"]]
        """
        No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
        """

    class TransformQuantity(StripeObject):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, round the result up or down.
        """

    active: bool
    """
    Whether this License Fee is active. Inactive License Fees cannot be used in new activations or be modified.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    display_name: str
    """
    A customer-facing name for the license fee.
    This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
    Maximum length of 250 characters.
    """
    id: str
    """
    Unique identifier for the object.
    """
    latest_version: str
    """
    The ID of the license fee's most recently created version.
    """
    licensed_item: "LicensedItem"
    """
    A Licensed Item represents a billable item whose pricing is based on license fees. You can use license fees
    to specify the pricing and create subscriptions to these items.
    """
    live_version: str
    """
    The ID of the License Fee Version that will be used by all subscriptions when no specific version is specified.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    An internal key you can use to search for a particular License Fee. Maximum length of 200 characters.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["v2.billing.license_fee"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    service_interval: Literal["day", "month", "week", "year"]
    """
    The interval for assessing service.
    """
    service_interval_count: int
    """
    The length of the interval for assessing service. For example, set this to 3 and `service_interval` to `"month"` in
    order to specify quarterly service.
    """
    tax_behavior: Literal["exclusive", "inclusive"]
    """
    The Stripe Tax tax behavior - whether the license fee is inclusive or exclusive of tax.
    """
    tiering_mode: Optional[Literal["graduated", "volume"]]
    """
    Defines whether the tiering price should be graduated or volume-based. In volume-based tiering, the maximum
    quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
    grows into new tiers. Can only be set if `tiers` is set.
    """
    tiers: List[Tier]
    """
    Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
    """
    transform_quantity: Optional[TransformQuantity]
    """
    Apply a transformation to the reported usage or set quantity before computing the amount billed.
    """
    unit_amount: Optional[str]
    """
    The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
    places. Cannot be set if `tiers` is provided.
    """
    _inner_class_types = {
        "tiers": Tier,
        "transform_quantity": TransformQuantity,
    }
