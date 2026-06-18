# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class Contract(StripeObject):
    """
    Main Contract resource representing a comprehensive billing agreement
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.contract"]] = (
        "v2.billing.contract"
    )

    class BillingSettings(StripeObject):
        class ContractBillingDetails(StripeObject):
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
                collection_method: Literal[
                    "charge_automatically", "send_invoice"
                ]
                """
                The collection method.
                """
                payment_method_configuration: Optional[str]
                """
                The payment method configuration.
                """

            bill_settings_details: Optional[BillSettingsDetails]
            """
            The bill settings details.
            """
            billing_profile_details: BillingProfileDetails
            """
            The billing profile details.
            """
            collection_settings_details: CollectionSettingsDetails
            """
            The collection settings details.
            """
            _inner_class_types = {
                "bill_settings_details": BillSettingsDetails,
                "billing_profile_details": BillingProfileDetails,
                "collection_settings_details": CollectionSettingsDetails,
            }

        contract_billing_details: Optional[ContractBillingDetails]
        """
        Billing settings details for the contract.
        """
        _inner_class_types = {
            "contract_billing_details": ContractBillingDetails,
        }

    class OneTimeFees(StripeObject):
        class Data(StripeObject):
            class BillSchedule(StripeObject):
                class BillAt(StripeObject):
                    timestamp: Optional[str]
                    """
                    The datetime at which the entry will be billed. Set when `type` is `datetime`.
                    """
                    type: Literal["contract_start", "datetime"]
                    """
                    The type of the bill_at.
                    """

                bill_at: BillAt
                """
                When this entry will be billed.
                """
                value: int
                """
                The amount to bill for this entry, in the smallest currency unit.
                """
                _inner_class_types = {"bill_at": BillAt}
                _field_encodings = {"value": "int64_string"}

            class ProductDetails(StripeObject):
                product: str
                """
                The ID of the v1 Product.
                """

            bill_schedule: List[BillSchedule]
            """
            The resolved bill schedule for the fee.
            """
            billable_item_type: Literal["product"]
            """
            The type of billable item that this fee references.
            """
            id: str
            """
            The ID of the one-time fee.
            """
            lookup_key: Optional[str]
            """
            The user-provided lookup key.
            """
            product_details: Optional[ProductDetails]
            """
            Details for a product billable target. Set when `billable_item_type` is `product`.
            """
            _inner_class_types = {
                "bill_schedule": BillSchedule,
                "product_details": ProductDetails,
            }

        data: List[Data]
        """
        The one-time fees for this page.
        """
        _inner_class_types = {"data": Data}

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
                                class Tier(StripeObject):
                                    flat_amount: Optional[str]
                                    """
                                    Price for the entire tier, represented as a decimal string in minor currency units.
                                    """
                                    unit_amount: Optional[str]
                                    """
                                    Per-unit price for units included in this tier, represented as a decimal string in minor currency units.
                                    """
                                    up_to_decimal: Optional[Decimal]
                                    """
                                    Up to and including this quantity will be contained in the tier.
                                    """
                                    up_to_inf: Optional[Literal["inf"]]
                                    """
                                    No upper bound to this tier.
                                    """
                                    _field_encodings = {
                                        "up_to_decimal": "decimal_string",
                                    }

                                tiering_mode: Optional[
                                    Literal["graduated", "volume"]
                                ]
                                """
                                Defines whether the tiered price should be graduated or volume-based.
                                """
                                tiers: List[Tier]
                                """
                                Each element represents a pricing tier.
                                """
                                unit_amount: Optional[str]
                                """
                                The per-unit amount to be charged, represented as a decimal string in minor currency units.
                                """
                                _inner_class_types = {"tiers": Tier}

                            class StartsAt(StripeObject):
                                timestamp: str
                                """
                                The timestamp when the item starts.
                                """

                            ends_at: EndsAt
                            """
                            Resolved timestamp when this override ends.
                            """
                            lookup_key: Optional[str]
                            """
                            The user-provided lookup key for this override.
                            """
                            overwrite_price: Optional[OverwritePrice]
                            """
                            Details for an overwrite_price override.
                            """
                            pricing_override: str
                            """
                            The ID of the pricing line override.
                            """
                            starts_at: StartsAt
                            """
                            Resolved timestamp when this override starts.
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
            Resolved timestamp when the pricing line ends.
            """
            id: str
            """
            The ID of the pricing line.
            """
            lookup_key: Optional[str]
            """
            The user-provided lookup key for the pricing line.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Set of key-value pairs that you can attach to an object.
            """
            pricing: Pricing
            """
            The pricing configuration for the pricing line.
            """
            starts_at: StartsAt
            """
            Resolved timestamp when the pricing line starts.
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

            class Multiplier(StripeObject):
                class Criterion(StripeObject):
                    class MetadataCondition(StripeObject):
                        class AllOf(StripeObject):
                            key: str
                            """
                            The metadata key.
                            """
                            value: str
                            """
                            The metadata value.
                            """

                        all_of: List[AllOf]
                        """
                        All of these key-value conditions must match.
                        """
                        _inner_class_types = {"all_of": AllOf}

                    billable_item_ids: List[str]
                    """
                    Filter by billable item IDs.
                    """
                    billable_item_lookup_keys: List[str]
                    """
                    Filter by billable item lookup keys.
                    """
                    billable_item_types: List[Literal["licensed", "metered"]]
                    """
                    Filter by billable item type.
                    """
                    metadata_conditions: List[MetadataCondition]
                    """
                    Filter by metadata conditions.
                    """
                    rate_card_ids: List[str]
                    """
                    Filter by rate card IDs. Only applicable for `multiplier` overrides.
                    """
                    type: Literal["exclude", "include"]
                    """
                    Whether to include or exclude items matching these criteria.
                    """
                    _inner_class_types = {
                        "metadata_conditions": MetadataCondition,
                    }

                criteria: List[Criterion]
                """
                Criteria determining which rates the multiplier applies to.
                """
                factor: str
                """
                The multiplier factor, represented as a decimal string. e.g. "0.8" for a 20% reduction.
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
            multiplier: Optional[Multiplier]
            """
            Details for a multiplier override.
            """
            priority: int
            """
            The priority of this override relative to others. Lower number = higher priority.
            """
            starts_at: StartsAt
            """
            Resolved timestamp when the pricing override starts.
            """
            type: Literal["multiplier"]
            """
            The type of pricing override.
            """
            _inner_class_types = {
                "ends_at": EndsAt,
                "multiplier": Multiplier,
                "starts_at": StartsAt,
            }

        data: List[Data]
        """
        The pricing overrides for this page.
        """
        _inner_class_types = {"data": Data}

    class StatusDetails(StripeObject):
        class Active(StripeObject):
            activated_at: str
            """
            The timestamp when the contract was activated.
            """

        class Canceled(StripeObject):
            canceled_at: str
            """
            The timestamp when the contract was canceled.
            """

        active: Optional[Active]
        """
        Details of the active contract status.
        """
        canceled: Optional[Canceled]
        """
        Details of the canceled contract status.
        """
        _inner_class_types = {"active": Active, "canceled": Canceled}

    billing_settings: Optional[BillingSettings]
    """
    The billing settings for the contract.
    """
    contract_number: str
    """
    A unique user-provided contract number e.g. C-2026-0001.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    currency: str
    """
    The currency of the contract.
    """
    customer: str
    """
    The ID of the customer associated with the contract.
    """
    id: str
    """
    The ID of the contract object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object.
    """
    object: Literal["v2.billing.contract"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    one_time_fees: Optional[OneTimeFees]
    """
    The one-time fees of the contract. Only populated when `one_time_fees` is passed in the `include` parameter.
    """
    pricing_lines: Optional[PricingLines]
    """
    The pricing lines of the contract. Only populated when `pricing_lines` is passed in the `include` parameter.
    """
    pricing_overrides: Optional[PricingOverrides]
    """
    The pricing overrides of the contract. Only populated when `pricing_overrides` is passed in the `include` parameter.
    """
    status: Literal["active", "canceled", "draft", "ended"]
    """
    The current status of the contract.
    """
    status_details: StatusDetails
    """
    Information about the contract status transitions.
    """
    _inner_class_types = {
        "billing_settings": BillingSettings,
        "one_time_fees": OneTimeFees,
        "pricing_lines": PricingLines,
        "pricing_overrides": PricingOverrides,
        "status_details": StatusDetails,
    }
