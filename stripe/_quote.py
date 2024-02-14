# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._nested_resource_class_methods import nested_resource_class_methods
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeStreamResponseAsync
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import Any, ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._customer import Customer
    from stripe._discount import Discount as DiscountResource
    from stripe._invoice import Invoice
    from stripe._invoice_line_item import InvoiceLineItem
    from stripe._line_item import LineItem
    from stripe._quote_line import QuoteLine
    from stripe._quote_preview_invoice import QuotePreviewInvoice
    from stripe._quote_preview_subscription_schedule import (
        QuotePreviewSubscriptionSchedule,
    )
    from stripe._subscription import Subscription
    from stripe._subscription_schedule import (
        SubscriptionSchedule as SubscriptionScheduleResource,
    )
    from stripe._tax_rate import TaxRate
    from stripe.test_helpers._test_clock import TestClock


@nested_resource_class_methods("preview_invoice")
@nested_resource_class_methods("preview_subscription_schedule")
class Quote(
    CreateableAPIResource["Quote"],
    ListableAPIResource["Quote"],
    UpdateableAPIResource["Quote"],
):
    """
    A Quote is a way to model prices that you'd like to provide to a customer.
    Once accepted, it will automatically create an invoice, subscription or subscription schedule.
    """

    OBJECT_NAME: ClassVar[Literal["quote"]] = "quote"

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced.
            """

        enabled: bool
        """
        Automatically calculate taxes
        """
        liability: Optional[Liability]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        """
        The status of the most recent automated tax calculation for this quote.
        """
        _inner_class_types = {"liability": Liability}

    class Computed(StripeObject):
        class LastReestimationDetails(StripeObject):
            class Failed(StripeObject):
                failure_code: Optional[str]
                """
                The failure `code` is more granular than the `reason` provided and may correspond to a Stripe error code. For automation errors, this field is one of: `reverse_api_failure`, `reverse_api_deadline_exceeeded`, or `reverse_api_response_validation_error`, which are Stripe error codes and map to the error `message` field.
                """
                message: Optional[str]
                """
                Information derived from the `failure_code` or a freeform message that explains the error as a human-readable English string. For example, "margin ID is not a valid ID".
                """
                reason: Literal["automation_failure", "internal_error"]
                """
                The reason the reestimation failed.
                """

            failed: Optional[Failed]
            """
            When `status` is `failed`, provides details about the quote reestimation failure.
            """
            status: Literal["failed", "in_progress", "succeeded"]
            """
            Latest status of the reestimation.
            """
            _inner_class_types = {"failed": Failed}

        class Recurring(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        """
                        The amount discounted.
                        """
                        discount: "DiscountResource"
                        """
                        A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
                        It contains information about when the discount began, when it will end, and what it is applied to.

                        Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
                        """

                    class Tax(StripeObject):
                        amount: int
                        """
                        Amount of tax applied for this rate.
                        """
                        rate: "TaxRate"
                        """
                        Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

                        Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
                        """
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        """
                        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
                        """
                        taxable_amount: Optional[int]
                        """
                        The amount on which tax is calculated, in cents (or local equivalent).
                        """

                    discounts: List[Discount]
                    """
                    The aggregated discounts.
                    """
                    taxes: List[Tax]
                    """
                    The aggregated tax amounts by rate.
                    """
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                """
                This is the sum of all the discounts.
                """
                amount_shipping: Optional[int]
                """
                This is the sum of all the shipping amounts.
                """
                amount_tax: int
                """
                This is the sum of all the tax amounts.
                """
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            """
            Total before any discounts or taxes are applied.
            """
            amount_total: int
            """
            Total after discounts and taxes are applied.
            """
            interval: Literal["day", "month", "week", "year"]
            """
            The frequency at which a subscription is billed. One of `day`, `week`, `month` or `year`.
            """
            interval_count: int
            """
            The number of intervals (specified in the `interval` attribute) between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months.
            """
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        class Upfront(StripeObject):
            class TotalDetails(StripeObject):
                class Breakdown(StripeObject):
                    class Discount(StripeObject):
                        amount: int
                        """
                        The amount discounted.
                        """
                        discount: "DiscountResource"
                        """
                        A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
                        It contains information about when the discount began, when it will end, and what it is applied to.

                        Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
                        """

                    class Tax(StripeObject):
                        amount: int
                        """
                        Amount of tax applied for this rate.
                        """
                        rate: "TaxRate"
                        """
                        Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

                        Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
                        """
                        taxability_reason: Optional[
                            Literal[
                                "customer_exempt",
                                "not_collecting",
                                "not_subject_to_tax",
                                "not_supported",
                                "portion_product_exempt",
                                "portion_reduced_rated",
                                "portion_standard_rated",
                                "product_exempt",
                                "product_exempt_holiday",
                                "proportionally_rated",
                                "reduced_rated",
                                "reverse_charge",
                                "standard_rated",
                                "taxable_basis_reduced",
                                "zero_rated",
                            ]
                        ]
                        """
                        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
                        """
                        taxable_amount: Optional[int]
                        """
                        The amount on which tax is calculated, in cents (or local equivalent).
                        """

                    discounts: List[Discount]
                    """
                    The aggregated discounts.
                    """
                    taxes: List[Tax]
                    """
                    The aggregated tax amounts by rate.
                    """
                    _inner_class_types = {"discounts": Discount, "taxes": Tax}

                amount_discount: int
                """
                This is the sum of all the discounts.
                """
                amount_shipping: Optional[int]
                """
                This is the sum of all the shipping amounts.
                """
                amount_tax: int
                """
                This is the sum of all the tax amounts.
                """
                breakdown: Optional[Breakdown]
                _inner_class_types = {"breakdown": Breakdown}

            amount_subtotal: int
            """
            Total before any discounts or taxes are applied.
            """
            amount_total: int
            """
            Total after discounts and taxes are applied.
            """
            line_items: Optional[ListObject["LineItem"]]
            """
            The line items that will appear on the next invoice after this quote is accepted. This does not include pending invoice items that exist on the customer but may still be included in the next invoice.
            """
            total_details: TotalDetails
            _inner_class_types = {"total_details": TotalDetails}

        last_reestimation_details: Optional[LastReestimationDetails]
        """
        Details of the most recent reestimate of the quote's preview schedules and upcoming invoices, including the status of Stripe's calculation.
        """
        recurring: Optional[Recurring]
        """
        The definitive totals and line items the customer will be charged on a recurring basis. Takes into account the line items with recurring prices and discounts with `duration=forever` coupons only. Defaults to `null` if no inputted line items with recurring prices.
        """
        updated_at: Optional[int]
        """
        The time at which the quote's estimated schedules and upcoming invoices were generated.
        """
        upfront: Upfront
        _inner_class_types = {
            "last_reestimation_details": LastReestimationDetails,
            "recurring": Recurring,
            "upfront": Upfront,
        }

    class FromQuote(StripeObject):
        is_revision: bool
        """
        Whether this quote is a revision of a different quote.
        """
        quote: ExpandableField["Quote"]
        """
        The quote that was cloned.
        """

    class InvoiceSettings(StripeObject):
        class Issuer(StripeObject):
            account: Optional[ExpandableField["Account"]]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced.
            """

        days_until_due: Optional[int]
        """
        Number of days within which a customer must pay invoices generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
        """
        issuer: Issuer
        _inner_class_types = {"issuer": Issuer}

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Optional[
                Literal[
                    "canceled",
                    "quote_accepted",
                    "quote_expired",
                    "quote_superseded",
                    "subscription_canceled",
                ]
            ]
            """
            The reason this quote was marked as canceled.
            """
            transitioned_at: Optional[int]
            """
            Time at which the quote was marked as canceled. Measured in seconds since the Unix epoch.
            """

        class Stale(StripeObject):
            class LastReason(StripeObject):
                class SubscriptionChanged(StripeObject):
                    previous_subscription: Optional["Subscription"]
                    """
                    The subscription's state before the quote was marked as stale.
                    """

                class SubscriptionScheduleChanged(StripeObject):
                    previous_subscription_schedule: Optional[
                        "SubscriptionScheduleResource"
                    ]
                    """
                    The subscription schedule's state before the quote was marked as stale.
                    """

                line_invalid: Optional[str]
                """
                The ID of the line that is invalid if the stale reason type is `line_invalid`.
                """
                marked_stale: Optional[str]
                """
                The user supplied mark stale reason.
                """
                subscription_canceled: Optional[str]
                """
                The ID of the subscription that was canceled.
                """
                subscription_changed: Optional[SubscriptionChanged]
                subscription_expired: Optional[str]
                """
                The ID of the subscription that was expired.
                """
                subscription_schedule_canceled: Optional[str]
                """
                The ID of the subscription schedule that was canceled.
                """
                subscription_schedule_changed: Optional[
                    SubscriptionScheduleChanged
                ]
                subscription_schedule_released: Optional[str]
                """
                The ID of the subscription schedule that was released.
                """
                type: Optional[
                    Literal[
                        "accept_failed_validations",
                        "bill_on_acceptance_invalid",
                        "line_invalid",
                        "marked_stale",
                        "subscription_canceled",
                        "subscription_changed",
                        "subscription_expired",
                        "subscription_schedule_canceled",
                        "subscription_schedule_changed",
                        "subscription_schedule_released",
                    ]
                ]
                """
                The reason the quote was marked as stale.
                """
                _inner_class_types = {
                    "subscription_changed": SubscriptionChanged,
                    "subscription_schedule_changed": SubscriptionScheduleChanged,
                }

            expires_at: Optional[int]
            """
            Time at which the quote expires. Measured in seconds since the Unix epoch.
            """
            last_reason: Optional[LastReason]
            """
            The most recent reason this quote was marked as stale.
            """
            last_updated_at: Optional[int]
            """
            Time at which the stale reason was updated. Measured in seconds since the Unix epoch.
            """
            transitioned_at: Optional[int]
            """
            Time at which the quote was marked as stale. Measured in seconds since the Unix epoch.
            """
            _inner_class_types = {"last_reason": LastReason}

        canceled: Optional[Canceled]
        stale: Optional[Stale]
        _inner_class_types = {"canceled": Canceled, "stale": Stale}

    class StatusTransitions(StripeObject):
        accepted_at: Optional[int]
        """
        The time that the quote was accepted. Measured in seconds since Unix epoch.
        """
        canceled_at: Optional[int]
        """
        The time that the quote was canceled. Measured in seconds since Unix epoch.
        """
        finalized_at: Optional[int]
        """
        The time that the quote was finalized. Measured in seconds since Unix epoch.
        """

    class SubscriptionData(StripeObject):
        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed: Optional[int]
                """
                The materialized time.
                """
                line_starts_at: Optional[LineStartsAt]
                """
                The timestamp the given line starts at.
                """
                timestamp: Optional[int]
                """
                A precise Unix timestamp.
                """
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                """
                The type of method to specify the `bill_from` time.
                """
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
                    """
                    interval_count: int
                    """
                    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
                    """

                class LineEndsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed: Optional[int]
                """
                The materialized time.
                """
                duration: Optional[Duration]
                """
                Time span for the quote line starting from the `starts_at` date.
                """
                line_ends_at: Optional[LineEndsAt]
                """
                The timestamp the given line ends at.
                """
                timestamp: Optional[int]
                """
                A precise Unix timestamp.
                """
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                """
                The type of method to specify the `bill_until` time.
                """
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            """
            The start of the period to bill from when the Quote is accepted.
            """
            bill_until: Optional[BillUntil]
            """
            The end of the period to bill until when the Quote is accepted.
            """
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        class Prebilling(StripeObject):
            iterations: int

        bill_on_acceptance: Optional[BillOnAcceptance]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        billing_cycle_anchor: Optional[Literal["reset"]]
        """
        Whether the subscription will always start a new billing period when the quote is accepted.
        """
        description: Optional[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        effective_date: Optional[int]
        """
        When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. This date is ignored if it is in the past when the quote is accepted. Measured in seconds since the Unix epoch.
        """
        end_behavior: Optional[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        from_schedule: Optional[
            ExpandableField["SubscriptionScheduleResource"]
        ]
        """
        The id of the subscription schedule that will be updated when the quote is accepted.
        """
        from_subscription: Optional[ExpandableField["Subscription"]]
        """
        The id of the subscription that will be updated when the quote is accepted.
        """
        metadata: Optional[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        prebilling: Optional[Prebilling]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations) when the quote is accepted.
        """
        trial_period_days: Optional[int]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """
        _inner_class_types = {
            "bill_on_acceptance": BillOnAcceptance,
            "prebilling": Prebilling,
        }

    class SubscriptionDataOverride(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            """
            A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
            """
            subscription_schedule: Optional[str]
            """
            The ID of the schedule the line applies to.
            """
            type: Literal["new_reference", "subscription_schedule"]
            """
            Describes whether the quote line is affecting a new schedule or an existing schedule.
            """

        class BillOnAcceptance(StripeObject):
            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed: Optional[int]
                """
                The materialized time.
                """
                line_starts_at: Optional[LineStartsAt]
                """
                The timestamp the given line starts at.
                """
                timestamp: Optional[int]
                """
                A precise Unix timestamp.
                """
                type: Literal[
                    "line_starts_at",
                    "now",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                """
                The type of method to specify the `bill_from` time.
                """
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
                    """
                    interval_count: int
                    """
                    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
                    """

                class LineEndsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed: Optional[int]
                """
                The materialized time.
                """
                duration: Optional[Duration]
                """
                Time span for the quote line starting from the `starts_at` date.
                """
                line_ends_at: Optional[LineEndsAt]
                """
                The timestamp the given line ends at.
                """
                timestamp: Optional[int]
                """
                A precise Unix timestamp.
                """
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                """
                The type of method to specify the `bill_until` time.
                """
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            bill_from: Optional[BillFrom]
            """
            The start of the period to bill from when the Quote is accepted.
            """
            bill_until: Optional[BillUntil]
            """
            The end of the period to bill until when the Quote is accepted.
            """
            _inner_class_types = {
                "bill_from": BillFrom,
                "bill_until": BillUntil,
            }

        applies_to: AppliesTo
        bill_on_acceptance: Optional[BillOnAcceptance]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: Optional[
            Literal["prorate_on_next_phase", "prorate_up_front"]
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: Optional[str]
        """
        The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
        """
        description: Optional[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: Optional[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations) when the quote is accepted.
        """
        _inner_class_types = {
            "applies_to": AppliesTo,
            "bill_on_acceptance": BillOnAcceptance,
        }

    class SubscriptionSchedule(StripeObject):
        class AppliesTo(StripeObject):
            new_reference: Optional[str]
            """
            A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
            """
            subscription_schedule: Optional[str]
            """
            The ID of the schedule the line applies to.
            """
            type: Literal["new_reference", "subscription_schedule"]
            """
            Describes whether the quote line is affecting a new schedule or an existing schedule.
            """

        applies_to: AppliesTo
        subscription_schedule: str
        """
        The subscription schedule that was created or updated from this quote.
        """
        _inner_class_types = {"applies_to": AppliesTo}

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                """
                The amount discounted.
                """
                discount: "DiscountResource"
                """
                A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
                It contains information about when the discount began, when it will end, and what it is applied to.

                Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
                """

            class Tax(StripeObject):
                amount: int
                """
                Amount of tax applied for this rate.
                """
                rate: "TaxRate"
                """
                Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

                Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
                """
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                """
                The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
                """
                taxable_amount: Optional[int]
                """
                The amount on which tax is calculated, in cents (or local equivalent).
                """

            discounts: List[Discount]
            """
            The aggregated discounts.
            """
            taxes: List[Tax]
            """
            The aggregated tax amounts by rate.
            """
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        """
        This is the sum of all the discounts.
        """
        amount_shipping: Optional[int]
        """
        This is the sum of all the shipping amounts.
        """
        amount_tax: int
        """
        This is the sum of all the tax amounts.
        """
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    class TransferData(StripeObject):
        amount: Optional[int]
        """
        The amount in cents (or local equivalent) that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination.
        """
        amount_percent: Optional[float]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount will be transferred to the destination.
        """
        destination: ExpandableField["Account"]
        """
        The account where funds from the payment will be transferred to upon payment success.
        """

    class AcceptParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CancelParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        allow_backdated_lines: NotRequired["bool"]
        """
        Set to true to allow quote lines to have `starts_at` in the past if collection is paused between `starts_at` and now.
        """
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
        """
        application_fee_percent: NotRequired["Literal['']|float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
        """
        automatic_tax: NotRequired["Quote.CreateParamsAutomaticTax"]
        """
        Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
        """
        customer: NotRequired["str"]
        """
        The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that will apply to any line item that does not have `tax_rates` set.
        """
        description: NotRequired["Literal['']|str"]
        """
        A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        discounts: NotRequired["Literal['']|List[Quote.CreateParamsDiscount]"]
        """
        The discounts applied to the quote. You can only set up to one discount.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired["int"]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        footer: NotRequired["Literal['']|str"]
        """
        A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        from_quote: NotRequired["Quote.CreateParamsFromQuote"]
        """
        Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
        """
        header: NotRequired["Literal['']|str"]
        """
        A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
        """
        invoice_settings: NotRequired["Quote.CreateParamsInvoiceSettings"]
        """
        All invoices will be billed using the specified settings.
        """
        line_items: NotRequired["List[Quote.CreateParamsLineItem]"]
        """
        A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        lines: NotRequired["List[Quote.CreateParamsLine]"]
        """
        A list of lines on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge.
        """
        phases: NotRequired["List[Quote.CreateParamsPhase]"]
        """
        List representing phases of the Quote. Each phase can be customized to have different durations, prices, and coupons.
        """
        subscription_data: NotRequired["Quote.CreateParamsSubscriptionData"]
        """
        When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
        """
        subscription_data_overrides: NotRequired[
            "List[Quote.CreateParamsSubscriptionDataOverride]"
        ]
        """
        List representing overrides for `subscription_data` configurations for specific subscription schedules.
        """
        test_clock: NotRequired["str"]
        """
        ID of the test clock to attach to the quote.
        """
        transfer_data: NotRequired[
            "Literal['']|Quote.CreateParamsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the invoices.
        """

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
        """
        liability: NotRequired["Quote.CreateParamsAutomaticTaxLiability"]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class CreateParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired["Quote.CreateParamsDiscountDiscountEnd"]
        """
        Details to determine how long the discount should be applied for.
        """

    class CreateParamsDiscountDiscountEnd(TypedDict):
        duration: NotRequired["Quote.CreateParamsDiscountDiscountEndDuration"]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsFromQuote(TypedDict):
        is_revision: NotRequired["bool"]
        """
        Whether this quote is a revision of the previous quote.
        """
        quote: str
        """
        The `id` of the quote that will be cloned.
        """

    class CreateParamsInvoiceSettings(TypedDict):
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
        """
        issuer: NotRequired["Quote.CreateParamsInvoiceSettingsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class CreateParamsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class CreateParamsLine(TypedDict):
        actions: NotRequired["List[Quote.CreateParamsLineAction]"]
        """
        An array of operations the quote line performs.
        """
        applies_to: NotRequired["Quote.CreateParamsLineAppliesTo"]
        """
        Details to identify the subscription schedule the quote line applies to.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'line_starts_at']"
        ]
        """
        For a point-in-time operation, this attribute lets you set or update whether the subscription's billing cycle anchor is reset at the `starts_at` timestamp.
        """
        ends_at: NotRequired["Quote.CreateParamsLineEndsAt"]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the quote line is considered a point-in-time operation that only affects the exact timestamp at `starts_at`, and a restricted set of attributes is supported on the quote line.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Changes to how Stripe handles prorations during the quote line's time span. Affects if and how prorations are created when a future phase starts.
        """
        set_pause_collection: NotRequired[
            "Quote.CreateParamsLineSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            "Literal['line_ends_at', 'line_starts_at']"
        ]
        """
        Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
        """
        starts_at: NotRequired["Quote.CreateParamsLineStartsAt"]
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        trial_settings: NotRequired["Quote.CreateParamsLineTrialSettings"]
        """
        Settings related to subscription trials.
        """

    class CreateParamsLineAction(TypedDict):
        add_discount: NotRequired["Quote.CreateParamsLineActionAddDiscount"]
        """
        Details for the `add_discount` type.
        """
        add_item: NotRequired["Quote.CreateParamsLineActionAddItem"]
        """
        Details for the `add_item` type.
        """
        add_metadata: NotRequired["Dict[str, str]"]
        """
        Details for the `add_metadata` type: specify a hash of key-value pairs.
        """
        remove_discount: NotRequired[
            "Quote.CreateParamsLineActionRemoveDiscount"
        ]
        """
        Details for the `remove_discount` type.
        """
        remove_item: NotRequired["Quote.CreateParamsLineActionRemoveItem"]
        """
        Details for the `remove_item` type.
        """
        remove_metadata: NotRequired["List[str]"]
        """
        Details for the `remove_metadata` type: specify an array of metadata keys.
        """
        set_discounts: NotRequired[
            "List[Quote.CreateParamsLineActionSetDiscount]"
        ]
        """
        Details for the `set_discounts` type.
        """
        set_items: NotRequired["List[Quote.CreateParamsLineActionSetItem]"]
        """
        Details for the `set_items` type.
        """
        set_metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Details for the `set_metadata` type: specify an array of key-value pairs.
        """
        type: Literal[
            "add_discount",
            "add_item",
            "add_metadata",
            "clear_discounts",
            "clear_metadata",
            "remove_discount",
            "remove_item",
            "remove_metadata",
            "set_discounts",
            "set_items",
            "set_metadata",
        ]
        """
        The type of action the quote line performs.
        """

    class CreateParamsLineActionAddDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to redeem.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "Quote.CreateParamsLineActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired["int"]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """

    class CreateParamsLineActionAddDiscountDiscountEnd(TypedDict):
        type: Literal["line_ends_at"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionAddItem(TypedDict):
        discounts: NotRequired[
            "List[Quote.CreateParamsLineActionAddItemDiscount]"
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["List[str]"]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired["Quote.CreateParamsLineActionAddItemTrial"]
        """
        Options that configure the trial on the subscription item.
        """

    class CreateParamsLineActionAddItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.CreateParamsLineActionAddItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsLineActionAddItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionAddItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineActionAddItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class CreateParamsLineActionRemoveDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired["str"]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class CreateParamsLineActionRemoveItem(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class CreateParamsLineActionSetDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired["str"]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class CreateParamsLineActionSetItem(TypedDict):
        discounts: NotRequired[
            "List[Quote.CreateParamsLineActionSetItemDiscount]"
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired["List[str]"]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired["Quote.CreateParamsLineActionSetItemTrial"]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class CreateParamsLineActionSetItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.CreateParamsLineActionSetItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsLineActionSetItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineActionSetItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineActionSetItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class CreateParamsLineAppliesTo(TypedDict):
        new_reference: NotRequired["str"]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired["str"]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CreateParamsLineEndsAt(TypedDict):
        discount_end: NotRequired["Quote.CreateParamsLineEndsAtDiscountEnd"]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired["Quote.CreateParamsLineEndsAtDuration"]
        """
        Time span for the quote line starting from the `starts_at` date.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "duration",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `ends_at`.
        """

    class CreateParamsLineEndsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class CreateParamsLineEndsAtDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[Quote.CreateParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["Quote.CreateParamsLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class CreateParamsLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.CreateParamsLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """

    class CreateParamsLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: NotRequired["Quote.CreateParamsLineItemPriceDataRecurring"]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class CreateParamsLineSetPauseCollection(TypedDict):
        set: NotRequired["Quote.CreateParamsLineSetPauseCollectionSet"]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class CreateParamsLineSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class CreateParamsLineStartsAt(TypedDict):
        discount_end: NotRequired["Quote.CreateParamsLineStartsAtDiscountEnd"]
        """
        Use the `end` time of a given discount.
        """
        line_ends_at: NotRequired["Quote.CreateParamsLineStartsAtLineEndsAt"]
        """
        The timestamp the given line ends at.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "line_ends_at",
            "now",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `starts_at`.
        """

    class CreateParamsLineStartsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class CreateParamsLineStartsAtLineEndsAt(TypedDict):
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsLineTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "Quote.CreateParamsLineTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class CreateParamsLineTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class CreateParamsPhase(TypedDict):
        billing_cycle_anchor: NotRequired["Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
        """
        discounts: NotRequired[
            "Literal['']|List[Quote.CreateParamsPhaseDiscount]"
        ]
        """
        The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription's customer. Pass an empty string to avoid inheriting any discounts.
        """
        end_date: NotRequired["int"]
        """
        The date at which this phase of the quote ends. If set, `iterations` must not be set.
        """
        invoice_settings: NotRequired["Quote.CreateParamsPhaseInvoiceSettings"]
        """
        All invoices will be billed using the specified settings.
        """
        iterations: NotRequired["int"]
        """
        Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
        """
        line_items: List["Quote.CreateParamsPhaseLineItem"]
        """
        A list of line items the customer is being quoted for within this phase. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on the subscription schedule's phases when the quote is accepted.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`.
        """
        trial: NotRequired["bool"]
        """
        If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
        """
        trial_end: NotRequired["int"]
        """
        Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`.
        """

    class CreateParamsPhaseDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired["Quote.CreateParamsPhaseDiscountDiscountEnd"]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsPhaseDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsPhaseDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsPhaseDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsPhaseInvoiceSettings(TypedDict):
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """

    class CreateParamsPhaseLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[Quote.CreateParamsPhaseLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["Quote.CreateParamsPhaseLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class CreateParamsPhaseLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.CreateParamsPhaseLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """

    class CreateParamsPhaseLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsPhaseLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class CreateParamsPhaseLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsPhaseLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: NotRequired[
            "Quote.CreateParamsPhaseLineItemPriceDataRecurring"
        ]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsPhaseLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class CreateParamsSubscriptionData(TypedDict):
        bill_on_acceptance: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        billing_cycle_anchor: NotRequired["Literal['']|Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        description: NotRequired["str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        effective_date: NotRequired[
            "Literal['']|Literal['current_period_end']|int"
        ]
        """
        When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
        """
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        from_schedule: NotRequired["str"]
        """
        The id of a subscription schedule the quote will update. The quote will inherit the state of the subscription schedule, such as `phases`. Cannot be combined with other parameters.
        """
        from_subscription: NotRequired["str"]
        """
        The id of a subscription that the quote will update. By default, the quote will contain the state of the subscription (such as line items, collection method and billing thresholds) unless overridden.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        prebilling: NotRequired[
            "Literal['']|Quote.CreateParamsSubscriptionDataPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """
        trial_period_days: NotRequired["Literal['']|int"]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
        line_starts_at: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
        duration: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "Quote.CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataOverride(TypedDict):
        applies_to: "Quote.CreateParamsSubscriptionDataOverrideAppliesTo"
        """
        Whether the override applies to an existing Subscription Schedule or a new Subscription Schedule.
        """
        bill_on_acceptance: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: NotRequired["str"]
        """
        The customer the Subscription Data override applies to. This is only relevant when `applies_to.type=new_reference`.
        """
        description: NotRequired["str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """

    class CreateParamsSubscriptionDataOverrideAppliesTo(TypedDict):
        new_reference: NotRequired["str"]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired["str"]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
        TypedDict,
    ):
        line_starts_at: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
        TypedDict,
    ):
        duration: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "Quote.CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class CreateParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class CreateParamsSubscriptionDataPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class FinalizeQuoteParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired["int"]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
        """

    class ListComputedUpfrontLineItemsParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListLinesParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParams(RequestOptions):
        customer: NotRequired["str"]
        """
        The ID of the customer whose quotes will be retrieved.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        from_subscription: NotRequired["str"]
        """
        The subscription which the quote updates.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            "Literal['accepted', 'accepting', 'canceled', 'draft', 'open', 'stale']"
        ]
        """
        The status of the quote.
        """
        test_clock: NotRequired["str"]
        """
        Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set.
        """

    class ListPreviewInvoiceLinesParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListPreviewInvoicesParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListPreviewSubscriptionSchedulesParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class MarkDraftParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class MarkStaleParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        reason: NotRequired["str"]
        """
        Reason the Quote is being marked stale.
        """

    class ModifyParams(RequestOptions):
        allow_backdated_lines: NotRequired["bool"]
        """
        Set to true to allow quote lines to have `starts_at` in the past if collection is paused between `starts_at` and now.
        """
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
        """
        application_fee_percent: NotRequired["Literal['']|float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
        """
        automatic_tax: NotRequired["Quote.ModifyParamsAutomaticTax"]
        """
        Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
        """
        customer: NotRequired["str"]
        """
        The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that will apply to any line item that does not have `tax_rates` set.
        """
        description: NotRequired["Literal['']|str"]
        """
        A description that will be displayed on the quote PDF.
        """
        discounts: NotRequired["Literal['']|List[Quote.ModifyParamsDiscount]"]
        """
        The discounts applied to the quote. You can only set up to one discount.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired["int"]
        """
        A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
        """
        footer: NotRequired["Literal['']|str"]
        """
        A footer that will be displayed on the quote PDF.
        """
        header: NotRequired["Literal['']|str"]
        """
        A header that will be displayed on the quote PDF.
        """
        invoice_settings: NotRequired["Quote.ModifyParamsInvoiceSettings"]
        """
        All invoices will be billed using the specified settings.
        """
        line_items: NotRequired["List[Quote.ModifyParamsLineItem]"]
        """
        A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        lines: NotRequired["List[Quote.ModifyParamsLine]"]
        """
        A list of lines on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account on behalf of which to charge.
        """
        phases: NotRequired["List[Quote.ModifyParamsPhase]"]
        """
        List representing phases of the Quote. Each phase can be customized to have different durations, prices, and coupons.
        """
        subscription_data: NotRequired["Quote.ModifyParamsSubscriptionData"]
        """
        When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
        """
        subscription_data_overrides: NotRequired[
            "Literal['']|List[Quote.ModifyParamsSubscriptionDataOverride]"
        ]
        """
        List representing overrides for `subscription_data` configurations for specific subscription schedules.
        """
        transfer_data: NotRequired[
            "Literal['']|Quote.ModifyParamsTransferData"
        ]
        """
        The data with which to automatically create a Transfer for each of the invoices.
        """

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Controls whether Stripe will automatically compute tax on the resulting invoices or subscriptions as well as the quote itself.
        """
        liability: NotRequired["Quote.ModifyParamsAutomaticTaxLiability"]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class ModifyParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ModifyParamsDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired["Quote.ModifyParamsDiscountDiscountEnd"]
        """
        Details to determine how long the discount should be applied for.
        """

    class ModifyParamsDiscountDiscountEnd(TypedDict):
        duration: NotRequired["Quote.ModifyParamsDiscountDiscountEndDuration"]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsInvoiceSettings(TypedDict):
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay the invoice generated by this quote. This value will be `null` for quotes where `collection_method=charge_automatically`.
        """
        issuer: NotRequired["Quote.ModifyParamsInvoiceSettingsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """

    class ModifyParamsInvoiceSettingsIssuer(TypedDict):
        account: NotRequired["str"]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ModifyParamsLine(TypedDict):
        actions: NotRequired["List[Quote.ModifyParamsLineAction]"]
        """
        An array of operations the quote line performs.
        """
        applies_to: NotRequired["Quote.ModifyParamsLineAppliesTo"]
        """
        Details to identify the subscription schedule the quote line applies to.
        """
        billing_cycle_anchor: NotRequired[
            "Literal['automatic', 'line_starts_at']"
        ]
        """
        For a point-in-time operation, this attribute lets you set or update whether the subscription's billing cycle anchor is reset at the `starts_at` timestamp.
        """
        ends_at: NotRequired["Quote.ModifyParamsLineEndsAt"]
        """
        Details to identify the end of the time range modified by the proposed change. If not supplied, the quote line is considered a point-in-time operation that only affects the exact timestamp at `starts_at`, and a restricted set of attributes is supported on the quote line.
        """
        id: NotRequired["str"]
        """
        The ID of an existing line on the quote.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Changes to how Stripe handles prorations during the quote line's time span. Affects if and how prorations are created when a future phase starts.
        """
        set_pause_collection: NotRequired[
            "Quote.ModifyParamsLineSetPauseCollection"
        ]
        """
        Defines how to pause collection for the underlying subscription throughout the duration of the amendment.
        """
        set_schedule_end: NotRequired[
            "Literal['line_ends_at', 'line_starts_at']"
        ]
        """
        Timestamp helper to end the underlying schedule early, based on the acompanying line's start or end date.
        """
        starts_at: NotRequired["Quote.ModifyParamsLineStartsAt"]
        """
        Details to identify the earliest timestamp where the proposed change should take effect.
        """
        trial_settings: NotRequired["Quote.ModifyParamsLineTrialSettings"]
        """
        Settings related to subscription trials.
        """

    class ModifyParamsLineAction(TypedDict):
        add_discount: NotRequired["Quote.ModifyParamsLineActionAddDiscount"]
        """
        Details for the `add_discount` type.
        """
        add_item: NotRequired["Quote.ModifyParamsLineActionAddItem"]
        """
        Details for the `add_item` type.
        """
        add_metadata: NotRequired["Dict[str, str]"]
        """
        Details for the `add_metadata` type: specify a hash of key-value pairs.
        """
        remove_discount: NotRequired[
            "Quote.ModifyParamsLineActionRemoveDiscount"
        ]
        """
        Details for the `remove_discount` type.
        """
        remove_item: NotRequired["Quote.ModifyParamsLineActionRemoveItem"]
        """
        Details for the `remove_item` type.
        """
        remove_metadata: NotRequired["List[str]"]
        """
        Details for the `remove_metadata` type: specify an array of metadata keys.
        """
        set_discounts: NotRequired[
            "List[Quote.ModifyParamsLineActionSetDiscount]"
        ]
        """
        Details for the `set_discounts` type.
        """
        set_items: NotRequired["List[Quote.ModifyParamsLineActionSetItem]"]
        """
        Details for the `set_items` type.
        """
        set_metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Details for the `set_metadata` type: specify an array of key-value pairs.
        """
        type: Literal[
            "add_discount",
            "add_item",
            "add_metadata",
            "clear_discounts",
            "clear_metadata",
            "remove_discount",
            "remove_item",
            "remove_metadata",
            "set_discounts",
            "set_items",
            "set_metadata",
        ]
        """
        The type of action the quote line performs.
        """

    class ModifyParamsLineActionAddDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to redeem.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount for a coupon that was already redeemed.
        """
        discount_end: NotRequired[
            "Quote.ModifyParamsLineActionAddDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        index: NotRequired["int"]
        """
        The index, starting at 0, at which to position the new discount. When not supplied, Stripe defaults to appending the discount to the end of the `discounts` array.
        """

    class ModifyParamsLineActionAddDiscountDiscountEnd(TypedDict):
        type: Literal["line_ends_at"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsLineActionAddItem(TypedDict):
        discounts: NotRequired[
            "List[Quote.ModifyParamsLineActionAddItemDiscount]"
        ]
        """
        The discounts applied to the item. Subscription item discounts are applied before subscription discounts.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["List[str]"]
        """
        The tax rates that apply to this subscription item. When set, the `default_tax_rates` on the subscription do not apply to this `subscription_item`.
        """
        trial: NotRequired["Quote.ModifyParamsLineActionAddItemTrial"]
        """
        Options that configure the trial on the subscription item.
        """

    class ModifyParamsLineActionAddItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.ModifyParamsLineActionAddItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ModifyParamsLineActionAddItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsLineActionAddItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsLineActionAddItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsLineActionAddItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class ModifyParamsLineActionRemoveDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to remove from the `discounts` array.
        """
        discount: NotRequired["str"]
        """
        The ID of a discount to remove from the `discounts` array.
        """
        promotion_code: NotRequired["str"]
        """
        The ID of a promotion code to remove from the `discounts` array.
        """

    class ModifyParamsLineActionRemoveItem(TypedDict):
        price: str
        """
        ID of a price to remove.
        """

    class ModifyParamsLineActionSetDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        The coupon code to replace the `discounts` array with.
        """
        discount: NotRequired["str"]
        """
        An ID of an existing discount to replace the `discounts` array with.
        """
        promotion_code: NotRequired["str"]
        """
        An ID of an existing promotion code to replace the `discounts` array with.
        """

    class ModifyParamsLineActionSetItem(TypedDict):
        discounts: NotRequired[
            "List[Quote.ModifyParamsLineActionSetItemDiscount]"
        ]
        """
        If an item with the `price` already exists, passing this will override the `discounts` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `discounts`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        If an item with the `price` already exists, passing this will override the `metadata` on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `metadata`.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired["int"]
        """
        If an item with the `price` already exists, passing this will override the quantity on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `quantity`.
        """
        tax_rates: NotRequired["List[str]"]
        """
        If an item with the `price` already exists, passing this will override the `tax_rates` array on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `tax_rates`.
        """
        trial: NotRequired["Quote.ModifyParamsLineActionSetItemTrial"]
        """
        If an item with the `price` already exists, passing this will override the `trial` configuration on the subscription item that matches that price. Otherwise, the `items` array is cleared and a single new item is added with the supplied `trial`.
        """

    class ModifyParamsLineActionSetItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.ModifyParamsLineActionSetItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ModifyParamsLineActionSetItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsLineActionSetItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsLineActionSetItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsLineActionSetItemTrial(TypedDict):
        converts_to: NotRequired["List[str]"]
        """
        List of price IDs which, if present on the subscription following a paid trial, constitute opting-in to the paid trial.
        """
        type: Literal["free", "paid"]
        """
        Determines the type of trial for this item.
        """

    class ModifyParamsLineAppliesTo(TypedDict):
        new_reference: NotRequired["str"]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired["str"]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class ModifyParamsLineEndsAt(TypedDict):
        discount_end: NotRequired["Quote.ModifyParamsLineEndsAtDiscountEnd"]
        """
        Use the `end` time of a given discount.
        """
        duration: NotRequired["Quote.ModifyParamsLineEndsAtDuration"]
        """
        Time span for the quote line starting from the `starts_at` date.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "duration",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `ends_at`.
        """

    class ModifyParamsLineEndsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class ModifyParamsLineEndsAtDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[Quote.ModifyParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        id: NotRequired["str"]
        """
        The ID of an existing line item on the quote.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["Quote.ModifyParamsLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class ModifyParamsLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.ModifyParamsLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """

    class ModifyParamsLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: NotRequired["Quote.ModifyParamsLineItemPriceDataRecurring"]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ModifyParamsLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class ModifyParamsLineSetPauseCollection(TypedDict):
        set: NotRequired["Quote.ModifyParamsLineSetPauseCollectionSet"]
        """
        Details of the pause_collection behavior to apply to the amendment.
        """
        type: Literal["remove", "set"]
        """
        Determines the type of the pause_collection amendment.
        """

    class ModifyParamsLineSetPauseCollectionSet(TypedDict):
        behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
        """
        The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
        """

    class ModifyParamsLineStartsAt(TypedDict):
        discount_end: NotRequired["Quote.ModifyParamsLineStartsAtDiscountEnd"]
        """
        Use the `end` time of a given discount.
        """
        line_ends_at: NotRequired["Quote.ModifyParamsLineStartsAtLineEndsAt"]
        """
        The timestamp the given line ends at.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "discount_end",
            "line_ends_at",
            "now",
            "quote_acceptance_date",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        Select a way to pass in `starts_at`.
        """

    class ModifyParamsLineStartsAtDiscountEnd(TypedDict):
        discount: str
        """
        The ID of a specific discount.
        """

    class ModifyParamsLineStartsAtLineEndsAt(TypedDict):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class ModifyParamsLineTrialSettings(TypedDict):
        end_behavior: NotRequired[
            "Quote.ModifyParamsLineTrialSettingsEndBehavior"
        ]
        """
        Defines how the subscription should behave when a trial ends.
        """

    class ModifyParamsLineTrialSettingsEndBehavior(TypedDict):
        prorate_up_front: NotRequired["Literal['defer', 'include']"]
        """
        Configure how an opt-in following a paid trial is billed when using `billing_behavior: prorate_up_front`.
        """

    class ModifyParamsPhase(TypedDict):
        billing_cycle_anchor: NotRequired["Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        collection_method: NotRequired[
            "Literal['charge_automatically', 'send_invoice']"
        ]
        """
        Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay the underlying subscription at the end of each billing cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically` on creation.
        """
        default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will set the Subscription's [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates), which means they will be the Invoice's [`default_tax_rates`](https://stripe.com/docs/api/invoices/create#create_invoice-default_tax_rates) for any Invoices issued by the Subscription during this Phase.
        """
        discounts: NotRequired[
            "Literal['']|List[Quote.ModifyParamsPhaseDiscount]"
        ]
        """
        The coupons to redeem into discounts for the schedule phase. If not specified, inherits the discount from the subscription's customer. Pass an empty string to avoid inheriting any discounts.
        """
        end_date: NotRequired["int"]
        """
        The date at which this phase of the quote ends. If set, `iterations` must not be set.
        """
        invoice_settings: NotRequired["Quote.ModifyParamsPhaseInvoiceSettings"]
        """
        All invoices will be billed using the specified settings.
        """
        iterations: NotRequired["int"]
        """
        Integer representing the multiplier applied to the price interval. For example, `iterations=2` applied to a price with `interval=month` and `interval_count=3` results in a phase of duration `2 * 3 months = 6 months`. If set, `end_date` must not be set.
        """
        line_items: List["Quote.ModifyParamsPhaseLineItem"]
        """
        A list of line items the customer is being quoted for within this phase. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on the subscription schedule's phases when the quote is accepted. After a quote has been finalized, this field can be updated by specifying an identical set of quote phases to what was on the quote originally, excluding changes in metadata and phases that are now in the past.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        If the update changes the current phase, indicates whether the changes should be prorated. The default value is `create_prorations`.
        """
        trial: NotRequired["bool"]
        """
        If set to true the entire phase is counted as a trial and the customer will not be charged for any fees.
        """
        trial_end: NotRequired["int"]
        """
        Sets the phase to trialing from the start date to this date. Must be before the phase end date, can not be combined with `trial`.
        """

    class ModifyParamsPhaseDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired["Quote.ModifyParamsPhaseDiscountDiscountEnd"]
        """
        Details to determine how long the discount should be applied for.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ModifyParamsPhaseDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsPhaseDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsPhaseDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsPhaseInvoiceSettings(TypedDict):
        days_until_due: NotRequired["int"]
        """
        Number of days within which a customer must pay invoices generated by this subscription schedule. This value will be `null` for subscription schedules where `billing=charge_automatically`.
        """

    class ModifyParamsPhaseLineItem(TypedDict):
        discounts: NotRequired[
            "Literal['']|List[Quote.ModifyParamsPhaseLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired["str"]
        """
        The ID of the price object. One of `price` or `price_data` is required.
        """
        price_data: NotRequired["Quote.ModifyParamsPhaseLineItemPriceData"]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates which apply to the line item. When set, the `default_tax_rates` on the quote do not apply to this line item.
        """

    class ModifyParamsPhaseLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        discount_end: NotRequired[
            "Quote.ModifyParamsPhaseLineItemDiscountDiscountEnd"
        ]
        """
        Details to determine how long the discount should be applied for.
        """

    class ModifyParamsPhaseLineItemDiscountDiscountEnd(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsPhaseLineItemDiscountDiscountEndDuration"
        ]
        """
        Time span for the redeemed discount.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp for the discount to end. Must be in the future.
        """
        type: Literal["duration", "timestamp"]
        """
        The type of calculation made to determine when the discount ends.
        """

    class ModifyParamsPhaseLineItemDiscountDiscountEndDuration(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsPhaseLineItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: NotRequired[
            "Quote.ModifyParamsPhaseLineItemPriceDataRecurring"
        ]
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ModifyParamsPhaseLineItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired["int"]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    class ModifyParamsSubscriptionData(TypedDict):
        bill_on_acceptance: NotRequired[
            "Literal['']|Quote.ModifyParamsSubscriptionDataBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        billing_cycle_anchor: NotRequired["Literal['']|Literal['reset']"]
        """
        When specified as `reset`, the subscription will always start a new billing period when the quote is accepted.
        """
        description: NotRequired["Literal['']|str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        effective_date: NotRequired[
            "Literal['']|Literal['current_period_end']|int"
        ]
        """
        When creating a new subscription, the date of which the subscription schedule will start after the quote is accepted. When updating a subscription, the date of which the subscription will be updated using a subscription schedule. The special value `current_period_end` can be provided to update a subscription at the end of its current period. The `effective_date` is ignored if it is in the past when the quote is accepted.
        """
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        prebilling: NotRequired[
            "Literal['']|Quote.ModifyParamsSubscriptionDataPrebilling"
        ]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """
        trial_period_days: NotRequired["Literal['']|int"]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptanceBillFrom(TypedDict):
        line_starts_at: NotRequired[
            "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntil(TypedDict):
        duration: NotRequired[
            "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "Quote.ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsSubscriptionDataBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class ModifyParamsSubscriptionDataOverride(TypedDict):
        applies_to: "Quote.ModifyParamsSubscriptionDataOverrideAppliesTo"
        """
        Whether the override applies to an existing Subscription Schedule or a new Subscription Schedule.
        """
        bill_on_acceptance: NotRequired[
            "Literal['']|Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptance"
        ]
        """
        Describes the period to bill for upon accepting the quote.
        """
        billing_behavior: NotRequired[
            "Literal['prorate_on_next_phase', 'prorate_up_front']"
        ]
        """
        Configures when the subscription schedule generates prorations for phase transitions. Possible values are `prorate_on_next_phase` or `prorate_up_front` with the default being `prorate_on_next_phase`. `prorate_on_next_phase` will apply phase changes and generate prorations at transition time. `prorate_up_front` will bill for all phases within the current billing cycle up front.
        """
        customer: NotRequired["str"]
        """
        The customer the Subscription Data override applies to.
        """
        description: NotRequired["Literal['']|str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: NotRequired["Literal['cancel', 'release']"]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        proration_behavior: NotRequired[
            "Literal['always_invoice', 'create_prorations', 'none']"
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/subscriptions/billing-cycle#prorations). When creating a subscription, valid values are `create_prorations` or `none`.

        When updating a subscription, valid values are `create_prorations`, `none`, or `always_invoice`.

        Passing `create_prorations` will cause proration invoice items to be created when applicable. These proration items will only be invoiced immediately under [certain conditions](https://stripe.com/docs/subscriptions/upgrading-downgrading#immediate-payment). In order to always invoice immediately for prorations, pass `always_invoice`.

        Prorations can be disabled by passing `none`.
        """

    class ModifyParamsSubscriptionDataOverrideAppliesTo(TypedDict):
        new_reference: NotRequired["str"]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: NotRequired["str"]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptance(TypedDict):
        bill_from: NotRequired[
            "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom"
        ]
        """
        The start of the period to bill from when the Quote is accepted.
        """
        bill_until: NotRequired[
            "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil"
        ]
        """
        The end of the period to bill until when the Quote is accepted.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFrom(
        TypedDict,
    ):
        line_starts_at: NotRequired[
            "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt"
        ]
        """
        Details of a Quote line to start the bill period from.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "line_starts_at",
            "now",
            "pause_collection_start",
            "quote_acceptance_date",
            "timestamp",
        ]
        """
        The type of method to specify the `bill_from` time.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillFromLineStartsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntil(
        TypedDict,
    ):
        duration: NotRequired[
            "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration"
        ]
        """
        Details of the duration over which to bill.
        """
        line_ends_at: NotRequired[
            "Quote.ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt"
        ]
        """
        Details of a Quote line item from which to bill until.
        """
        timestamp: NotRequired["int"]
        """
        A precise Unix timestamp.
        """
        type: Literal[
            "duration",
            "line_ends_at",
            "schedule_end",
            "timestamp",
            "upcoming_invoice",
        ]
        """
        The type of method to specify the `bill_until` time.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilDuration(
        TypedDict,
    ):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """
        interval_count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """

    class ModifyParamsSubscriptionDataOverrideBillOnAcceptanceBillUntilLineEndsAt(
        TypedDict,
    ):
        id: NotRequired["str"]
        """
        The ID of a quote line.
        """
        index: NotRequired["int"]
        """
        The position of the previous quote line in the `lines` array after which this line should begin. Indexes start from 0 and must be less than the index of the current line in the array.
        """

    class ModifyParamsSubscriptionDataPrebilling(TypedDict):
        iterations: int
        """
        This is used to determine the number of billing cycles to prebill.
        """

    class ModifyParamsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when the invoice is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        amount_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the destination account. By default, the entire amount is transferred to the destination. There must be at least 1 line item with a recurring price to use this field.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class PdfParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReestimateParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    allow_backdated_lines: Optional[bool]
    """
    Allow quote lines to have `starts_at` in the past if collection is paused between `starts_at` and now.
    """
    amount_subtotal: int
    """
    Total before any discounts or taxes are applied.
    """
    amount_total: int
    """
    Total after discounts and taxes are applied.
    """
    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the quote.
    """
    application_fee_amount: Optional[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Only applicable if there are no line items with recurring prices on the quote.
    """
    application_fee_percent: Optional[float]
    """
    A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. Only applicable if there are line items with recurring prices on the quote.
    """
    automatic_tax: AutomaticTax
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or on finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    """
    computed: Computed
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The customer which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    """
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    """
    The tax rates applied to this quote.
    """
    description: Optional[str]
    """
    A description that will be displayed on the quote PDF.
    """
    discounts: List[ExpandableField["DiscountResource"]]
    """
    The discounts applied to this quote.
    """
    expires_at: int
    """
    The date on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
    """
    footer: Optional[str]
    """
    A footer that will be displayed on the quote PDF.
    """
    from_quote: Optional[FromQuote]
    """
    Details of the quote that was cloned. See the [cloning documentation](https://stripe.com/docs/quotes/clone) for more details.
    """
    header: Optional[str]
    """
    A header that will be displayed on the quote PDF.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice: Optional[ExpandableField["Invoice"]]
    """
    The invoice that was created from this quote.
    """
    invoice_settings: InvoiceSettings
    line_items: Optional[ListObject["LineItem"]]
    """
    A list of items the customer is being quoted for.
    """
    lines: Optional[List[str]]
    """
    A list of lines on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: Optional[str]
    """
    A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://stripe.com/docs/quotes/overview#finalize).
    """
    object: Literal["quote"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.
    """
    status: Literal[
        "accepted", "accepting", "canceled", "draft", "open", "stale"
    ]
    """
    The status of the quote.
    """
    status_details: Optional[StatusDetails]
    """
    Details on when and why a quote has been marked as stale or canceled.
    """
    status_transitions: StatusTransitions
    subscription: Optional[ExpandableField["Subscription"]]
    """
    The subscription that was created or updated from this quote.
    """
    subscription_data: SubscriptionData
    subscription_data_overrides: Optional[List[SubscriptionDataOverride]]
    """
    List representing overrides for `subscription_data` configurations for specific subscription schedules.
    """
    subscription_schedule: Optional[
        ExpandableField["SubscriptionScheduleResource"]
    ]
    """
    The subscription schedule that was created or updated from this quote.
    """
    subscription_schedules: Optional[List[SubscriptionSchedule]]
    """
    The subscription schedules that were created or updated from this quote.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this quote belongs to.
    """
    total_details: TotalDetails
    transfer_data: Optional[TransferData]
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to for each of the invoices.
    """

    @classmethod
    def _cls_accept(
        cls, quote: str, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/accept".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def accept(quote: str, **params: Unpack["Quote.AcceptParams"]) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @overload
    def accept(self, **params: Unpack["Quote.AcceptParams"]) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @class_method_variant("_cls_accept")
    def accept(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/accept".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_accept_async(
        cls, quote: str, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/accept".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def accept_async(
        quote: str, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @overload
    async def accept_async(
        self, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @class_method_variant("_cls_accept_async")
    async def accept_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.AcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/accept".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_cancel(
        cls, quote: str, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/cancel".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(quote: str, **params: Unpack["Quote.CancelParams"]) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @overload
    def cancel(self, **params: Unpack["Quote.CancelParams"]) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/cancel".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_async(
        cls, quote: str, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/cancel".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cancel_async(
        quote: str, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.CancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/cancel".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(cls, **params: Unpack["Quote.CreateParams"]) -> "Quote":
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Quote.CreateParams"]
    ) -> "Quote":
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_finalize_quote(
        cls, quote: str, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/finalize".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def finalize_quote(
        quote: str, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @overload
    def finalize_quote(
        self, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @class_method_variant("_cls_finalize_quote")
    def finalize_quote(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/finalize".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_finalize_quote_async(
        cls, quote: str, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/finalize".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def finalize_quote_async(
        quote: str, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @overload
    async def finalize_quote_async(
        self, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @class_method_variant("_cls_finalize_quote_async")
    async def finalize_quote_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.FinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/finalize".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(cls, **params: Unpack["Quote.ListParams"]) -> ListObject["Quote"]:
        """
        Returns a list of your quotes.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Quote.ListParams"]
    ) -> ListObject["Quote"]:
        """
        Returns a list of your quotes.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_computed_upfront_line_items(
        cls,
        quote: str,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_computed_upfront_line_items(
        quote: str,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @overload
    def list_computed_upfront_line_items(
        self, **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @class_method_variant("_cls_list_computed_upfront_line_items")
    def list_computed_upfront_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_computed_upfront_line_items_async(
        cls,
        quote: str,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        return cast(
            ListObject["LineItem"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_computed_upfront_line_items_async(
        quote: str,
        **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @overload
    async def list_computed_upfront_line_items_async(
        self, **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @class_method_variant("_cls_list_computed_upfront_line_items_async")
    async def list_computed_upfront_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        return cast(
            ListObject["LineItem"],
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/computed_upfront_line_items".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_list_line_items(
        cls, quote: str, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_line_items(
        quote: str, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_line_items_async(
        cls, quote: str, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_line_items_async(
        quote: str, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    async def list_line_items_async(
        self, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items_async")
    async def list_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/line_items".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_list_lines(
        cls, quote: str, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            ListObject["QuoteLine"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/lines".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_lines(
        quote: str, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @overload
    def list_lines(
        self, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @class_method_variant("_cls_list_lines")
    def list_lines(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            ListObject["QuoteLine"],
            self._request(
                "get",
                "/v1/quotes/{quote}/lines".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_lines_async(
        cls, quote: str, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            ListObject["QuoteLine"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/lines".format(quote=sanitize_id(quote)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_lines_async(
        quote: str, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @overload
    async def list_lines_async(
        self, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @class_method_variant("_cls_list_lines_async")
    async def list_lines_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            ListObject["QuoteLine"],
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/lines".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_list_preview_invoice_lines(
        cls,
        quote: str,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject["InvoiceLineItem"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(quote),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_preview_invoice_lines(
        quote: str,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @overload
    def list_preview_invoice_lines(
        self,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @class_method_variant("_cls_list_preview_invoice_lines")
    def list_preview_invoice_lines(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject["InvoiceLineItem"],
            self._request(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(self.get("id")),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_preview_invoice_lines_async(
        cls,
        quote: str,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject["InvoiceLineItem"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(quote),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_preview_invoice_lines_async(
        quote: str,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @overload
    async def list_preview_invoice_lines_async(
        self,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @class_method_variant("_cls_list_preview_invoice_lines_async")
    async def list_preview_invoice_lines_async(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        preview_invoice: str,
        **params: Unpack["Quote.ListPreviewInvoiceLinesParams"]
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            ListObject["InvoiceLineItem"],
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/preview_invoices/{preview_invoice}/lines".format(
                    quote=sanitize_id(self.get("id")),
                    preview_invoice=sanitize_id(preview_invoice),
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_mark_draft(
        cls, quote: str, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def mark_draft(
        quote: str, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @overload
    def mark_draft(self, **params: Unpack["Quote.MarkDraftParams"]) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @class_method_variant("_cls_mark_draft")
    def mark_draft(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_mark_draft_async(
        cls, quote: str, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def mark_draft_async(
        quote: str, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @overload
    async def mark_draft_async(
        self, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @class_method_variant("_cls_mark_draft_async")
    async def mark_draft_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.MarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/mark_draft".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_mark_stale(
        cls, quote: str, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def mark_stale(
        quote: str, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @overload
    def mark_stale(self, **params: Unpack["Quote.MarkStaleParams"]) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @class_method_variant("_cls_mark_stale")
    def mark_stale(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_mark_stale_async(
        cls, quote: str, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def mark_stale_async(
        quote: str, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @overload
    async def mark_stale_async(
        self, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @class_method_variant("_cls_mark_stale_async")
    async def mark_stale_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.MarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/mark_stale".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Quote.ModifyParams"]
    ) -> "Quote":
        """
        A quote models prices and services for a customer.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Quote",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Quote.ModifyParams"]
    ) -> "Quote":
        """
        A quote models prices and services for a customer.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def _cls_pdf(cls, quote: str, **params: Unpack["Quote.PdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote
        """
        return cast(
            Any,
            cls._static_request_stream(
                "get",
                "/v1/quotes/{quote}/pdf".format(quote=sanitize_id(quote)),
                params=params,
                base_address="files",
            ),
        )

    @overload
    @staticmethod
    def pdf(quote: str, **params: Unpack["Quote.PdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote
        """
        ...

    @overload
    def pdf(self, **params: Unpack["Quote.PdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote
        """
        ...

    @class_method_variant("_cls_pdf")
    def pdf(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.PdfParams"]
    ) -> Any:
        """
        Download the PDF for a finalized quote
        """
        return cast(
            Any,
            self._request_stream(
                "get",
                "/v1/quotes/{quote}/pdf".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_pdf_async(
        cls, quote: str, **params: Unpack["Quote.PdfParams"]
    ) -> Any:
        """
        Download the PDF for a finalized quote
        """
        return cast(
            Any,
            await cls._static_request_stream_async(
                "get",
                "/v1/quotes/{quote}/pdf".format(quote=sanitize_id(quote)),
                params=params,
                base_address="files",
            ),
        )

    @overload
    @staticmethod
    async def pdf_async(
        quote: str, **params: Unpack["Quote.PdfParams"]
    ) -> StripeStreamResponseAsync:
        """
        Download the PDF for a finalized quote
        """
        ...

    @overload
    async def pdf_async(
        self, **params: Unpack["Quote.PdfParams"]
    ) -> StripeStreamResponseAsync:
        """
        Download the PDF for a finalized quote
        """
        ...

    @class_method_variant("_cls_pdf_async")
    async def pdf_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.PdfParams"]
    ) -> StripeStreamResponseAsync:
        """
        Download the PDF for a finalized quote
        """
        return await self._request_stream_async(
            "get",
            "/v1/quotes/{quote}/pdf".format(quote=sanitize_id(self.get("id"))),
            params=params,
        )

    @classmethod
    def _cls_reestimate(
        cls, quote: str, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            cls._static_request(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def reestimate(
        quote: str, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @overload
    def reestimate(
        self, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @class_method_variant("_cls_reestimate")
    def reestimate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_reestimate_async(
        cls, quote: str, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            await cls._static_request_async(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def reestimate_async(
        quote: str, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @overload
    async def reestimate_async(
        self, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @class_method_variant("_cls_reestimate_async")
    async def reestimate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Quote.ReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{quote}/reestimate".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Quote.RetrieveParams"]
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Quote.RetrieveParams"]
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def list_preview_invoices(
        cls, quote: str, **params: Unpack["Quote.ListPreviewInvoicesParams"]
    ) -> ListObject["QuotePreviewInvoice"]:
        """
        Preview the invoices that would be generated by accepting the quote.
        """
        return cast(
            ListObject["QuotePreviewInvoice"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/preview_invoices".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @classmethod
    async def list_preview_invoices_async(
        cls, quote: str, **params: Unpack["Quote.ListPreviewInvoicesParams"]
    ) -> ListObject["QuotePreviewInvoice"]:
        """
        Preview the invoices that would be generated by accepting the quote.
        """
        return cast(
            ListObject["QuotePreviewInvoice"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/preview_invoices".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @classmethod
    def list_preview_subscription_schedules(
        cls,
        quote: str,
        **params: Unpack["Quote.ListPreviewSubscriptionSchedulesParams"]
    ) -> ListObject["QuotePreviewSubscriptionSchedule"]:
        """
        Preview the schedules that would be generated by accepting the quote
        """
        return cast(
            ListObject["QuotePreviewSubscriptionSchedule"],
            cls._static_request(
                "get",
                "/v1/quotes/{quote}/preview_subscription_schedules".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    @classmethod
    async def list_preview_subscription_schedules_async(
        cls,
        quote: str,
        **params: Unpack["Quote.ListPreviewSubscriptionSchedulesParams"]
    ) -> ListObject["QuotePreviewSubscriptionSchedule"]:
        """
        Preview the schedules that would be generated by accepting the quote
        """
        return cast(
            ListObject["QuotePreviewSubscriptionSchedule"],
            await cls._static_request_async(
                "get",
                "/v1/quotes/{quote}/preview_subscription_schedules".format(
                    quote=sanitize_id(quote)
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "computed": Computed,
        "from_quote": FromQuote,
        "invoice_settings": InvoiceSettings,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "subscription_data": SubscriptionData,
        "subscription_data_overrides": SubscriptionDataOverride,
        "subscription_schedules": SubscriptionSchedule,
        "total_details": TotalDetails,
        "transfer_data": TransferData,
    }
