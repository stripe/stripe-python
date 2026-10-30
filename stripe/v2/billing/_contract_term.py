# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class ContractTerm(StripeObject):
    """
    A commercial term. Display order is independent of billing evaluation order.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.contract_term"]] = (
        "v2.billing.contract_term"
    )

    class AdHocProduct(StripeObject):
        class BillSchedule(StripeObject):
            class Custom(StripeObject):
                class BillAt(StripeObject):
                    timestamp: str
                    """
                    The timestamp at which the fee will be billed.
                    """

                amount: Amount
                """
                Amount in the contract's currency.
                """
                bill_at: BillAt
                """
                The resolved bill date.
                """
                _inner_class_types = {"bill_at": BillAt}

            custom: List[Custom]
            """
            Scheduled installments and billed history.
            """
            type: Union[Literal["custom"], str]
            """
            The type of billing schedule.
            """
            _inner_class_types = {"custom": Custom}

        class ServicePeriod(StripeObject):
            class EndsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item ends.
                """

            class StartsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item starts.
                """

            ends_at: EndsAt
            """
            The exclusive end of the service period.
            """
            starts_at: StartsAt
            """
            The inclusive start of the service period.
            """
            _inner_class_types = {"ends_at": EndsAt, "starts_at": StartsAt}

        bill_schedule: BillSchedule
        """
        Explicit bill dates and amounts, including billed history.
        """
        product: str
        """
        The V1 Product being billed.
        """
        service_period: Optional[ServicePeriod]
        """
        Informational invoice and revenue-recognition period with timestamp objects; does not affect billing or proration.
        """
        _inner_class_types = {
            "bill_schedule": BillSchedule,
            "service_period": ServicePeriod,
        }

    class PricingOverride(StripeObject):
        class Criterion(StripeObject):
            terms: Optional[List[str]]
            """
            Resolved IDs of recurring or ad_hoc_product terms. Override terms are not valid targets.
            """
            type: Union[Literal["exclude", "include"], str]
            """
            Whether to include or exclude the selected recurring or ad_hoc_product terms.
            """

        class EndsAt(StripeObject):
            timestamp: str
            """
            The timestamp when the item ends.
            """

        class Multiply(StripeObject):
            factor: Decimal
            """
            The multiplier, for example 0.85 for a 15% discount.
            """
            _field_encodings = {"factor": "decimal_string"}

        class Overwrite(StripeObject):
            unit_amount_decimal: Optional[Decimal]
            """
            The replacement per-unit amount in minor currency units.
            """
            _field_encodings = {"unit_amount_decimal": "decimal_string"}

        class StartsAt(StripeObject):
            timestamp: str
            """
            The timestamp when the item starts.
            """

        criteria: List[Criterion]
        """
        Recurring or ad_hoc_product terms selected by this override. An override without criteria applies to all recurring and ad_hoc_product terms.
        """
        ends_at: Optional[EndsAt]
        """
        The exclusive end of the validity window. Null for an open end.
        """
        multiply: Optional[Multiply]
        """
        Present when type is multiply.
        """
        overwrite: Optional[Overwrite]
        """
        Present when type is overwrite.
        """
        priority: int
        """
        Lower numbers win. Equal priorities resolve by display order; overrides do not stack.
        """
        starts_at: StartsAt
        """
        The inclusive start of the override's validity window.
        """
        type: Union[Literal["multiply", "overwrite"], str]
        """
        The pricing operation.
        """
        _inner_class_types = {
            "criteria": Criterion,
            "ends_at": EndsAt,
            "multiply": Multiply,
            "overwrite": Overwrite,
            "starts_at": StartsAt,
        }

    class RecurringPrice(StripeObject):
        class EndsAt(StripeObject):
            timestamp: str
            """
            The timestamp when the item ends.
            """

        class StartsAt(StripeObject):
            timestamp: str
            """
            The timestamp when the item starts.
            """

        ends_at: Optional[EndsAt]
        """
        The exclusive end of the term. Null for an open end.
        """
        price: str
        """
        The V1 recurring Price.
        """
        quantity: Optional[Decimal]
        """
        Current licensed quantity. Null for metered Prices; history is available separately.
        """
        starts_at: StartsAt
        """
        The inclusive start of the term.
        """
        _inner_class_types = {"ends_at": EndsAt, "starts_at": StartsAt}
        _field_encodings = {"quantity": "decimal_string"}

    ad_hoc_product: Optional[AdHocProduct]
    """
    Present when type is ad_hoc_product.
    """
    id: str
    """
    The stable ID of the term.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    The lookup key, unique across all term types on this contract.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs attached to the term.
    """
    object: Literal["v2.billing.contract_term"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_override: Optional[PricingOverride]
    """
    Present when type is pricing_override.
    """
    recurring_price: Optional[RecurringPrice]
    """
    Present when type is recurring_price.
    """
    type: Union[
        Literal["ad_hoc_product", "pricing_override", "recurring_price"], str
    ]
    """
    The type of this term.
    """
    _inner_class_types = {
        "ad_hoc_product": AdHocProduct,
        "pricing_override": PricingOverride,
        "recurring_price": RecurringPrice,
    }
