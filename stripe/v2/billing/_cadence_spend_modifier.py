# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class CadenceSpendModifier(StripeObject):
    """
    A Spend Modifier changes how spend is computed when billing for specific cadence.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.cadence_spend_modifier"]] = (
        "v2.billing.cadence_spend_modifier"
    )

    class MaxBillingPeriodSpend(StripeObject):
        class Amount(StripeObject):
            class CustomPricingUnit(StripeObject):
                value: str
                """
                The decimal value of custom pricing units, represented as a string.
                """

            custom_pricing_unit: Optional[CustomPricingUnit]
            """
            The custom pricing unit amount. Present if type is `custom_pricing_unit`.
            """
            type: Literal["custom_pricing_unit"]
            """
            The type of the spend modifier amount.
            """
            _inner_class_types = {"custom_pricing_unit": CustomPricingUnit}

        class CustomPricingUnitOverageRate(StripeObject):
            id: str
            """
            ID of the custom pricing unit overage rate.
            """

        alert: str
        """
        The billing alert associated with the maximum spend threshold.
        """
        amount: Amount
        """
        The maximum amount of invoice spend.
        """
        custom_pricing_unit_overage_rate: CustomPricingUnitOverageRate
        """
        The configuration for the overage rate for the custom pricing unit.
        """
        effective_from: str
        """
        The timestamp from which this spend modifier is effective.
        """
        effective_until: Optional[str]
        """
        The timestamp until which this spend modifier is effective. If not set, the modifier is effective indefinitely.
        """
        _inner_class_types = {
            "amount": Amount,
            "custom_pricing_unit_overage_rate": CustomPricingUnitOverageRate,
        }

    billing_cadence: str
    """
    The ID of the Billing Cadence this spend modifier is associated with.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    max_billing_period_spend: Optional[MaxBillingPeriodSpend]
    """
    Max invoice spend details. Present if type is `max_billing_period_spend`.
    """
    object: Literal["v2.billing.cadence_spend_modifier"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    type: Literal["max_billing_period_spend"]
    """
    The type of the spend modifier.
    """
    _inner_class_types = {"max_billing_period_spend": MaxBillingPeriodSpend}
