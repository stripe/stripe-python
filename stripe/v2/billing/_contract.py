# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Contract(StripeObject):
    """
    Contract resource representing a comprehensive sales agreement
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.contract"]] = (
        "v2.billing.contract"
    )

    class BillingCycleAnchor(StripeObject):
        timestamp: str
        """
        The billing cycle anchor as a UTC timestamp.
        """

    class BillingSettings(StripeObject):
        class BillSettingsDetails(StripeObject):
            class Calculation(StripeObject):
                class Tax(StripeObject):
                    type: Literal["automatic", "manual"]
                    """
                    The type of tax calculation.
                    """

                tax: Optional[Tax]
                """
                Tax calculation settings.
                """
                _inner_class_types = {"tax": Tax}

            class Invoice(StripeObject):
                class TimeUntilDue(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    The interval unit.
                    """
                    interval_count: int
                    """
                    The number of intervals.
                    """

                time_until_due: Optional[TimeUntilDue]
                """
                The number of time units before the invoice is past due.
                """
                _inner_class_types = {"time_until_due": TimeUntilDue}

            calculation: Optional[Calculation]
            """
            Calculation settings.
            """
            invoice: Optional[Invoice]
            """
            Invoice settings.
            """
            _inner_class_types = {
                "calculation": Calculation,
                "invoice": Invoice,
            }

        class BillingProfileDetails(StripeObject):
            customer: str
            """
            The customer who pays for the contract invoice.
            """
            default_payment_method: Optional[str]
            """
            The default payment method for the contract.
            """

        class CollectionSettingsDetails(StripeObject):
            collection_method: Literal["charge_automatically", "send_invoice"]
            """
            The collection method.
            """
            payment_method_configuration: Optional[str]
            """
            The payment method configuration.
            """

        bill_settings_details: Optional[BillSettingsDetails]
        """
        The bill settings details configures invoice and tax settings for the contract.
        """
        billing_profile_details: BillingProfileDetails
        """
        The billing profile details configures who is charged for the contract.
        """
        collection_settings_details: CollectionSettingsDetails
        """
        The collection settings details configures how payments are collected on the contract.
        """
        _inner_class_types = {
            "bill_settings_details": BillSettingsDetails,
            "billing_profile_details": BillingProfileDetails,
            "collection_settings_details": CollectionSettingsDetails,
        }

    class PricingLines(StripeObject):
        class Data(StripeObject):
            class EndsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item ends.
                """

            class Pricing(StripeObject):
                class PriceDetails(StripeObject):
                    class PricingOverrides(StripeObject):
                        class Data(StripeObject):
                            class EndsAt(StripeObject):
                                timestamp: str
                                """
                                The timestamp when the item ends.
                                """

                            class OverwritePrice(StripeObject):
                                unit_amount: Optional[str]
                                """
                                The per-unit amount to be charged, represented as a decimal string in minor currency units.
                                """

                            class StartsAt(StripeObject):
                                timestamp: str
                                """
                                The timestamp when the item starts.
                                """

                            ends_at: EndsAt
                            """
                            Timestamp when this override ends.
                            """
                            id: str
                            """
                            The ID of the pricing override.
                            """
                            lookup_key: Optional[str]
                            """
                            The user-provided lookup key for this override.
                            """
                            overwrite_price: Optional[OverwritePrice]
                            """
                            Details for an overwrite_price override.
                            """
                            priority: int
                            """
                            The priority of this override relative to others. Lower number = higher priority.
                            """
                            starts_at: StartsAt
                            """
                            Timestamp when this override starts.
                            """
                            type: Literal["overwrite_price"]
                            """
                            The type of override.
                            """
                            _inner_class_types = {
                                "ends_at": EndsAt,
                                "overwrite_price": OverwritePrice,
                                "starts_at": StartsAt,
                            }

                        data: List[Data]
                        """
                        The pricing line overrides.
                        """
                        _inner_class_types = {"data": Data}

                    current_quantity: Decimal
                    """
                    The current quantity on this pricing line.
                    """
                    price: str
                    """
                    The ID of the V1 price.
                    """
                    pricing_overrides: Optional[PricingOverrides]
                    """
                    The overwrite_price overrides embedded directly on this pricing line.
                    """
                    _inner_class_types = {
                        "pricing_overrides": PricingOverrides
                    }
                    _field_encodings = {"current_quantity": "decimal_string"}

                price_details: Optional[PriceDetails]
                """
                V1 price details. Present when `type` is `price`.
                """
                type: Literal["price"]
                """
                The type of pricing.
                """
                _inner_class_types = {"price_details": PriceDetails}

            class StartsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item starts.
                """

            ends_at: EndsAt
            """
            Timestamp when the pricing line ends.
            """
            id: str
            """
            The id of the pricing line.
            """
            lookup_key: Optional[str]
            """
            The user-provided lookup key for the pricing line.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Set of key-value pairs.
            """
            pricing: Pricing
            """
            The pricing configuration for the pricing line.
            """
            starts_at: StartsAt
            """
            Timestamp when the pricing line starts.
            """
            _inner_class_types = {
                "ends_at": EndsAt,
                "pricing": Pricing,
                "starts_at": StartsAt,
            }

        data: List[Data]
        """
        The pricing lines for this page.
        """
        _inner_class_types = {"data": Data}

    class PricingOverrides(StripeObject):
        class Data(StripeObject):
            class EndsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item ends.
                """

            class MultiplyPricing(StripeObject):
                class Criterion(StripeObject):
                    pricing_line_ids: Optional[List[str]]
                    """
                    Filter by pricing line IDs.
                    """
                    pricing_line_lookup_keys: Optional[List[str]]
                    """
                    Filter by pricing line lookup keys.
                    """
                    type: Union[Literal["exclude", "include"], str]
                    """
                    Whether to include or exclude items matching these criteria.
                    """

                criteria: List[Criterion]
                """
                Criteria determining which rates the multiply_pricing override applies to.
                """
                factor: str
                """
                The multiply_pricing factor, represented as a decimal string. e.g. "0.8" for a 20% reduction.
                """
                _inner_class_types = {"criteria": Criterion}

            class StartsAt(StripeObject):
                timestamp: str
                """
                The timestamp when the item starts.
                """

            ends_at: EndsAt
            """
            Resolved timestamp when the pricing override ends.
            """
            id: str
            """
            The ID of the pricing override.
            """
            lookup_key: Optional[str]
            """
            The user-provided lookup key for the pricing override.
            """
            multiply_pricing: Optional[MultiplyPricing]
            """
            Details for a multiply_pricing override.
            """
            priority: int
            """
            The priority of this override relative to others. Lower number = higher priority.
            """
            starts_at: StartsAt
            """
            Resolved timestamp when the pricing override starts.
            """
            type: Literal["multiply_pricing"]
            """
            The type of pricing override.
            """
            _inner_class_types = {
                "ends_at": EndsAt,
                "multiply_pricing": MultiplyPricing,
                "starts_at": StartsAt,
            }

        data: List[Data]
        """
        The pricing overrides for this page.
        """
        _inner_class_types = {"data": Data}

    class StatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        The timestamp when the contract was activated.
        """
        canceled_at: Optional[str]
        """
        The timestamp when the contract was canceled.
        """
        ended_at: Optional[str]
        """
        The timestamp when the contract ended.
        """

    billing_cycle_anchor: Optional[BillingCycleAnchor]
    """
    The billing cycle anchor.
    """
    billing_settings: Optional[BillingSettings]
    """
    The billing settings.
    """
    contract_number: str
    """
    A unique user-provided contract number e.g. C-2026-0001.
    """
    created: str
    """
    Timestamp of when the contract was created.
    """
    currency: str
    """
    The currency.
    """
    customer: str
    """
    The customer id.
    """
    id: str
    """
    The contract id.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs.
    """
    object: Literal["v2.billing.contract"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    pricing_lines: Optional[PricingLines]
    """
    The pricing lines. Only populated when `pricing_lines` is passed in the `include` parameter.
    """
    pricing_overrides: Optional[PricingOverrides]
    """
    The pricing overrides. Only populated when `pricing_overrides` is passed in the `include` parameter.
    """
    status: Union[Literal["active", "canceled", "draft", "ended"], str]
    """
    The current status of the contract.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Historical timestamps of when the contract transitioned into each status.
    """
    _inner_class_types = {
        "billing_cycle_anchor": BillingCycleAnchor,
        "billing_settings": BillingSettings,
        "pricing_lines": PricingLines,
        "pricing_overrides": PricingOverrides,
        "status_transitions": StatusTransitions,
    }
