# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class ContractTerm(StripeObject):
    """
    A commercial term. Display order is independent of billing evaluation order.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.contract_term"]] = (
        "v2.billing.contract_term"
    )

    class PricingOverride(StripeObject):
        class Criterion(StripeObject):
            terms: Optional[List[str]]
            """
            Resolved IDs of recurring or scheduled_fee terms. Override terms are not valid targets.
            """
            type: Union[Literal["exclude", "include"], str]
            """
            Whether to include or exclude the selected recurring or scheduled_fee terms.
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
            class Tier(StripeObject):
                flat_amount_decimal: Optional[Decimal]
                """
                Flat amount in minor currency units.
                """
                unit_amount_decimal: Optional[Decimal]
                """
                Per-unit amount in minor currency units.
                """
                up_to: Optional[int]
                """
                Inclusive whole-number upper bound. Omitted for an unbounded final tier.
                """
                _field_encodings = {
                    "flat_amount_decimal": "decimal_string",
                    "unit_amount_decimal": "decimal_string",
                    "up_to": "int64_string",
                }

            billing_scheme: Optional[Literal["per_unit", "tiered"]]
            """
            Whether the replacement pricing is per unit or tiered.
            """
            tiers: Optional[List[Tier]]
            """
            Replacement pricing tiers.
            """
            tiers_mode: Optional[Literal["graduated", "volume"]]
            """
            How the pricing tiers are applied.
            """
            unit_amount_decimal: Optional[Decimal]
            """
            The replacement per-unit amount in minor currency units.
            """
            _inner_class_types = {"tiers": Tier}
            _field_encodings = {"unit_amount_decimal": "decimal_string"}

        class StartsAt(StripeObject):
            timestamp: str
            """
            The timestamp when the item starts.
            """

        criteria: List[Criterion]
        """
        Recurring or scheduled_fee terms selected by this override. An override without criteria applies to all recurring and scheduled_fee terms.
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

    class ScheduledFee(StripeObject):
        class BillSchedule(StripeObject):
            class Custom(StripeObject):
                class BillAt(StripeObject):
                    timestamp: str
                    """
                    The timestamp at which the fee will be billed.
                    """

                bill_at: BillAt
                """
                The resolved bill date.
                """
                quantity: Decimal
                """
                Resolved installment quantity. Always present; defaults to 1 when omitted on input.
                """
                unit_amount_decimal: Decimal
                """
                Unit price in minor units of the contract's currency, before multiplying by quantity.
                """
                _inner_class_types = {"bill_at": BillAt}
                _field_encodings = {
                    "quantity": "decimal_string",
                    "unit_amount_decimal": "decimal_string",
                }

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
    scheduled_fee: Optional[ScheduledFee]
    """
    Present when type is scheduled_fee.
    """
    type: Union[
        Literal["pricing_override", "recurring_price", "scheduled_fee"], str
    ]
    """
    The type of this term.
    """
    _inner_class_types = {
        "pricing_override": PricingOverride,
        "recurring_price": RecurringPrice,
        "scheduled_fee": ScheduledFee,
    }
