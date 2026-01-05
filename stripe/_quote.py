# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._nested_resource_class_methods import nested_resource_class_methods
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import Any, ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._customer import Customer
    from stripe._discount import Discount as DiscountResource
    from stripe._invoice import Invoice
    from stripe._invoice_line_item import InvoiceLineItem
    from stripe._line_item import LineItem
    from stripe._price import Price
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
    from stripe.params._quote_accept_params import QuoteAcceptParams
    from stripe.params._quote_cancel_params import QuoteCancelParams
    from stripe.params._quote_create_params import QuoteCreateParams
    from stripe.params._quote_finalize_quote_params import (
        QuoteFinalizeQuoteParams,
    )
    from stripe.params._quote_list_computed_upfront_line_items_params import (
        QuoteListComputedUpfrontLineItemsParams,
    )
    from stripe.params._quote_list_line_items_params import (
        QuoteListLineItemsParams,
    )
    from stripe.params._quote_list_lines_params import QuoteListLinesParams
    from stripe.params._quote_list_params import QuoteListParams
    from stripe.params._quote_list_preview_invoice_lines_params import (
        QuoteListPreviewInvoiceLinesParams,
    )
    from stripe.params._quote_list_preview_invoices_params import (
        QuoteListPreviewInvoicesParams,
    )
    from stripe.params._quote_list_preview_subscription_schedules_params import (
        QuoteListPreviewSubscriptionSchedulesParams,
    )
    from stripe.params._quote_mark_draft_params import QuoteMarkDraftParams
    from stripe.params._quote_mark_stale_params import QuoteMarkStaleParams
    from stripe.params._quote_modify_params import QuoteModifyParams
    from stripe.params._quote_pdf_params import QuotePdfParams
    from stripe.params._quote_reestimate_params import QuoteReestimateParams
    from stripe.params._quote_retrieve_params import QuoteRetrieveParams
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
        provider: Optional[str]
        """
        The tax provider powering automatic tax.
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
                        A discount represents the actual application of a [coupon](https://api.stripe.com#coupons) or [promotion code](https://api.stripe.com#promotion_codes).
                        It contains information about when the discount began, when it will end, and what it is applied to.

                        Related guide: [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
                        """

                    class Tax(StripeObject):
                        amount: int
                        """
                        Amount of tax applied for this rate.
                        """
                        rate: "TaxRate"
                        """
                        Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

                        Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
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
                        A discount represents the actual application of a [coupon](https://api.stripe.com#coupons) or [promotion code](https://api.stripe.com#promotion_codes).
                        It contains information about when the discount began, when it will end, and what it is applied to.

                        Related guide: [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
                        """

                    class Tax(StripeObject):
                        amount: int
                        """
                        Amount of tax applied for this rate.
                        """
                        rate: "TaxRate"
                        """
                        Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

                        Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
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
                class LinesInvalid(StripeObject):
                    invalid_at: int
                    """
                    The timestamp at which the lines were marked as invalid.
                    """
                    lines: List[str]
                    """
                    The list of lines that became invalid at the given timestamp.
                    """

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
                lines_invalid: Optional[List[LinesInvalid]]
                """
                The IDs of the lines that are invalid if the stale reason type is `lines_invalid`.
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
                        "lines_invalid",
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
                    "lines_invalid": LinesInvalid,
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

        class BillingMode(StripeObject):
            class Flexible(StripeObject):
                proration_discounts: Optional[Literal["included", "itemized"]]
                """
                Controls how invoices and invoice items display proration amounts and discount amounts.
                """

            flexible: Optional[Flexible]
            type: Literal["classic", "flexible"]
            """
            Controls how prorations and invoices for subscriptions are calculated and orchestrated.
            """
            _inner_class_types = {"flexible": Flexible}

        class BillingSchedule(StripeObject):
            class AppliesTo(StripeObject):
                price: Optional[ExpandableField["Price"]]
                """
                The billing schedule will apply to the subscription item with the given price ID.
                """
                type: Literal["price"]
                """
                Controls which subscription items the billing schedule applies to.
                """

            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed_timestamp: Optional[int]
                """
                The time the billing schedule applies from.
                """
                line_starts_at: Optional[LineStartsAt]
                """
                Lets you bill the period starting from a particular Quote line.
                """
                timestamp: Optional[int]
                """
                Use a precise Unix timestamp for prebilling to start. Must be earlier than `bill_until`.
                """
                type: Literal[
                    "line_starts_at",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                """
                Describes how the billing schedule determines the start date. Possible values are `timestamp`, `relative`, `amendment_start`, `now`, `quote_acceptance_date`, `line_starts_at`, or `pause_collection_start`.
                """
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    Specifies billing duration. Either `day`, `week`, `month` or `year`.
                    """
                    interval_count: Optional[int]
                    """
                    The multiplier applied to the interval.
                    """

                class LineEndsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed_timestamp: Optional[int]
                """
                The timestamp the billing schedule will apply until.
                """
                duration: Optional[Duration]
                """
                Specifies the billing period.
                """
                line_ends_at: Optional[LineEndsAt]
                """
                Lets you bill the period ending at a particular Quote line.
                """
                timestamp: Optional[int]
                """
                If specified, the billing schedule will apply until the specified timestamp.
                """
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                """
                Describes how the billing schedule will determine the end date. Either `duration` or `timestamp`.
                """
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            applies_to: Optional[List[AppliesTo]]
            """
            Specifies which subscription items the billing schedule applies to.
            """
            bill_from: Optional[BillFrom]
            """
            Specifies the start of the billing period.
            """
            bill_until: BillUntil
            key: str
            """
            Unique identifier for the billing schedule.
            """
            _inner_class_types = {
                "applies_to": AppliesTo,
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
        billing_mode: BillingMode
        """
        The billing mode of the quote.
        """
        billing_schedules: Optional[List[BillingSchedule]]
        """
        Billing schedules that will be applied to the subscription or subscription schedule created from this quote.
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
        from_subscription: Optional[ExpandableField["Subscription"]]
        """
        The id of the subscription that will be updated when the quote is accepted.
        """
        metadata: Optional[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/api/metadata) that will set metadata on the subscription or subscription schedule when the quote is accepted. If a recurring price is included in `line_items`, this field will be passed to the resulting subscription's `metadata` field. If `subscription_data.effective_date` is used, this field will be passed to the resulting subscription schedule's `phases.metadata` field. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        phase_effective_at: Optional[
            Literal["billing_period_start", "phase_start"]
        ]
        """
        Configures how the subscription schedule handles billing for phase transitions when the quote is accepted.
        """
        prebilling: Optional[Prebilling]
        """
        If specified, the invoicing for the given billing cycle iterations will be processed when the quote is accepted. Cannot be used with `effective_date`.
        """
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://docs.stripe.com/subscriptions/billing-cycle#prorations) when the quote is accepted.
        """
        trial_period_days: Optional[int]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """
        _inner_class_types = {
            "bill_on_acceptance": BillOnAcceptance,
            "billing_mode": BillingMode,
            "billing_schedules": BillingSchedule,
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

        class BillingSchedule(StripeObject):
            class AppliesTo(StripeObject):
                price: Optional[ExpandableField["Price"]]
                """
                The billing schedule will apply to the subscription item with the given price ID.
                """
                type: Literal["price"]
                """
                Controls which subscription items the billing schedule applies to.
                """

            class BillFrom(StripeObject):
                class LineStartsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed_timestamp: Optional[int]
                """
                The time the billing schedule applies from.
                """
                line_starts_at: Optional[LineStartsAt]
                """
                Lets you bill the period starting from a particular Quote line.
                """
                timestamp: Optional[int]
                """
                Use a precise Unix timestamp for prebilling to start. Must be earlier than `bill_until`.
                """
                type: Literal[
                    "line_starts_at",
                    "pause_collection_start",
                    "quote_acceptance_date",
                    "timestamp",
                ]
                """
                Describes how the billing schedule determines the start date. Possible values are `timestamp`, `relative`, `amendment_start`, `now`, `quote_acceptance_date`, `line_starts_at`, or `pause_collection_start`.
                """
                _inner_class_types = {"line_starts_at": LineStartsAt}

            class BillUntil(StripeObject):
                class Duration(StripeObject):
                    interval: Literal["day", "month", "week", "year"]
                    """
                    Specifies billing duration. Either `day`, `week`, `month` or `year`.
                    """
                    interval_count: Optional[int]
                    """
                    The multiplier applied to the interval.
                    """

                class LineEndsAt(StripeObject):
                    id: str
                    """
                    Unique identifier for the object.
                    """

                computed_timestamp: Optional[int]
                """
                The timestamp the billing schedule will apply until.
                """
                duration: Optional[Duration]
                """
                Specifies the billing period.
                """
                line_ends_at: Optional[LineEndsAt]
                """
                Lets you bill the period ending at a particular Quote line.
                """
                timestamp: Optional[int]
                """
                If specified, the billing schedule will apply until the specified timestamp.
                """
                type: Literal[
                    "duration",
                    "line_ends_at",
                    "schedule_end",
                    "timestamp",
                    "upcoming_invoice",
                ]
                """
                Describes how the billing schedule will determine the end date. Either `duration` or `timestamp`.
                """
                _inner_class_types = {
                    "duration": Duration,
                    "line_ends_at": LineEndsAt,
                }

            applies_to: Optional[List[AppliesTo]]
            """
            Specifies which subscription items the billing schedule applies to.
            """
            bill_from: Optional[BillFrom]
            """
            Specifies the start of the billing period.
            """
            bill_until: BillUntil
            key: str
            """
            Unique identifier for the billing schedule.
            """
            _inner_class_types = {
                "applies_to": AppliesTo,
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
        billing_schedules: Optional[List[BillingSchedule]]
        """
        Billing schedules that will be applied to the subscription or subscription schedule created from this quote.
        """
        customer: Optional[str]
        """
        The customer who received this quote. A customer is required to finalize the quote. Once specified, you can't change it.
        """
        description: Optional[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        end_behavior: Optional[Literal["cancel", "release"]]
        """
        Behavior of the subscription schedule and underlying subscription when it ends.
        """
        phase_effective_at: Optional[
            Literal["billing_period_start", "phase_start"]
        ]
        """
        Configures how the subscription schedule handles billing for phase transitions when the quote is accepted.
        """
        proration_behavior: Optional[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://docs.stripe.com/subscriptions/billing-cycle#prorations) when the quote is accepted.
        """
        _inner_class_types = {
            "applies_to": AppliesTo,
            "bill_on_acceptance": BillOnAcceptance,
            "billing_schedules": BillingSchedule,
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
                A discount represents the actual application of a [coupon](https://api.stripe.com#coupons) or [promotion code](https://api.stripe.com#promotion_codes).
                It contains information about when the discount began, when it will end, and what it is applied to.

                Related guide: [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
                """

            class Tax(StripeObject):
                amount: int
                """
                Amount of tax applied for this rate.
                """
                rate: "TaxRate"
                """
                Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

                Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
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
    The customer who received this quote. A customer is required to finalize the quote. Once specified, you can't change it.
    """
    customer_account: Optional[str]
    """
    The account representing the customer who received this quote. A customer or account is required to finalize the quote. Once specified, you can't change it.
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
    Details of the quote that was cloned. See the [cloning documentation](https://docs.stripe.com/quotes/clone) for more details.
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
    A list of [quote lines](https://docs.stripe.com/api/quote_lines) on the quote. These lines describe changes, in the order provided, that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    number: Optional[str]
    """
    A unique number that identifies this particular quote. This number is assigned once the quote is [finalized](https://docs.stripe.com/quotes/overview#finalize).
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
        cls, quote: str, **params: Unpack["QuoteAcceptParams"]
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
    def accept(quote: str, **params: Unpack["QuoteAcceptParams"]) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @overload
    def accept(self, **params: Unpack["QuoteAcceptParams"]) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @class_method_variant("_cls_accept")
    def accept(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteAcceptParams"]
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
        cls, quote: str, **params: Unpack["QuoteAcceptParams"]
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
        quote: str, **params: Unpack["QuoteAcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @overload
    async def accept_async(
        self, **params: Unpack["QuoteAcceptParams"]
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        ...

    @class_method_variant("_cls_accept_async")
    async def accept_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteAcceptParams"]
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
        cls, quote: str, **params: Unpack["QuoteCancelParams"]
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
    def cancel(quote: str, **params: Unpack["QuoteCancelParams"]) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @overload
    def cancel(self, **params: Unpack["QuoteCancelParams"]) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteCancelParams"]
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
        cls, quote: str, **params: Unpack["QuoteCancelParams"]
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
        quote: str, **params: Unpack["QuoteCancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["QuoteCancelParams"]
    ) -> "Quote":
        """
        Cancels the quote.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteCancelParams"]
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
    def create(cls, **params: Unpack["QuoteCreateParams"]) -> "Quote":
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
        cls, **params: Unpack["QuoteCreateParams"]
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
        cls, quote: str, **params: Unpack["QuoteFinalizeQuoteParams"]
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
        quote: str, **params: Unpack["QuoteFinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @overload
    def finalize_quote(
        self, **params: Unpack["QuoteFinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @class_method_variant("_cls_finalize_quote")
    def finalize_quote(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteFinalizeQuoteParams"]
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
        cls, quote: str, **params: Unpack["QuoteFinalizeQuoteParams"]
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
        quote: str, **params: Unpack["QuoteFinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @overload
    async def finalize_quote_async(
        self, **params: Unpack["QuoteFinalizeQuoteParams"]
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        ...

    @class_method_variant("_cls_finalize_quote_async")
    async def finalize_quote_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteFinalizeQuoteParams"]
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
    def list(cls, **params: Unpack["QuoteListParams"]) -> ListObject["Quote"]:
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
        cls, **params: Unpack["QuoteListParams"]
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
        **params: Unpack["QuoteListComputedUpfrontLineItemsParams"],
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
        quote: str, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @overload
    def list_computed_upfront_line_items(
        self, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @class_method_variant("_cls_list_computed_upfront_line_items")
    def list_computed_upfront_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
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
        **params: Unpack["QuoteListComputedUpfrontLineItemsParams"],
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
        quote: str, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @overload
    async def list_computed_upfront_line_items_async(
        self, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable [computed.upfront.line_items](https://stripe.com/docs/api/quotes/object#quote_object-computed-upfront-line_items) property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of upfront line items.
        """
        ...

    @class_method_variant("_cls_list_computed_upfront_line_items_async")
    async def list_computed_upfront_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListComputedUpfrontLineItemsParams"]
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
        cls, quote: str, **params: Unpack["QuoteListLineItemsParams"]
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
        quote: str, **params: Unpack["QuoteListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self, **params: Unpack["QuoteListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListLineItemsParams"]
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
        cls, quote: str, **params: Unpack["QuoteListLineItemsParams"]
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
        quote: str, **params: Unpack["QuoteListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    async def list_line_items_async(
        self, **params: Unpack["QuoteListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a quote, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items_async")
    async def list_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListLineItemsParams"]
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
        cls, quote: str, **params: Unpack["QuoteListLinesParams"]
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
        quote: str, **params: Unpack["QuoteListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @overload
    def list_lines(
        self, **params: Unpack["QuoteListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @class_method_variant("_cls_list_lines")
    def list_lines(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListLinesParams"]
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
        cls, quote: str, **params: Unpack["QuoteListLinesParams"]
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
        quote: str, **params: Unpack["QuoteListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @overload
    async def list_lines_async(
        self, **params: Unpack["QuoteListLinesParams"]
    ) -> ListObject["QuoteLine"]:
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        ...

    @class_method_variant("_cls_list_lines_async")
    async def list_lines_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteListLinesParams"]
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
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
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
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @overload
    def list_preview_invoice_lines(
        self,
        preview_invoice: str,
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @class_method_variant("_cls_list_preview_invoice_lines")
    def list_preview_invoice_lines(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        preview_invoice: str,
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
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
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
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
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @overload
    async def list_preview_invoice_lines_async(
        self,
        preview_invoice: str,
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
    ) -> ListObject["InvoiceLineItem"]:
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        ...

    @class_method_variant("_cls_list_preview_invoice_lines_async")
    async def list_preview_invoice_lines_async(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        preview_invoice: str,
        **params: Unpack["QuoteListPreviewInvoiceLinesParams"],
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
        cls, quote: str, **params: Unpack["QuoteMarkDraftParams"]
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
        quote: str, **params: Unpack["QuoteMarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @overload
    def mark_draft(self, **params: Unpack["QuoteMarkDraftParams"]) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @class_method_variant("_cls_mark_draft")
    def mark_draft(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteMarkDraftParams"]
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
        cls, quote: str, **params: Unpack["QuoteMarkDraftParams"]
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
        quote: str, **params: Unpack["QuoteMarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @overload
    async def mark_draft_async(
        self, **params: Unpack["QuoteMarkDraftParams"]
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        ...

    @class_method_variant("_cls_mark_draft_async")
    async def mark_draft_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteMarkDraftParams"]
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
        cls, quote: str, **params: Unpack["QuoteMarkStaleParams"]
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
        quote: str, **params: Unpack["QuoteMarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @overload
    def mark_stale(self, **params: Unpack["QuoteMarkStaleParams"]) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @class_method_variant("_cls_mark_stale")
    def mark_stale(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteMarkStaleParams"]
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
        cls, quote: str, **params: Unpack["QuoteMarkStaleParams"]
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
        quote: str, **params: Unpack["QuoteMarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @overload
    async def mark_stale_async(
        self, **params: Unpack["QuoteMarkStaleParams"]
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        ...

    @class_method_variant("_cls_mark_stale_async")
    async def mark_stale_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteMarkStaleParams"]
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
    def modify(cls, id: str, **params: Unpack["QuoteModifyParams"]) -> "Quote":
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
        cls, id: str, **params: Unpack["QuoteModifyParams"]
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
    def _cls_pdf(cls, quote: str, **params: Unpack["QuotePdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
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
    def pdf(quote: str, **params: Unpack["QuotePdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        ...

    @overload
    def pdf(self, **params: Unpack["QuotePdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        ...

    @class_method_variant("_cls_pdf")
    def pdf(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuotePdfParams"]
    ) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            Any,
            self._request_stream(
                "get",
                "/v1/quotes/{quote}/pdf".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
                base_address="files",
            ),
        )

    @classmethod
    async def _cls_pdf_async(
        cls, quote: str, **params: Unpack["QuotePdfParams"]
    ) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
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
    async def pdf_async(quote: str, **params: Unpack["QuotePdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        ...

    @overload
    async def pdf_async(self, **params: Unpack["QuotePdfParams"]) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        ...

    @class_method_variant("_cls_pdf_async")
    async def pdf_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuotePdfParams"]
    ) -> Any:
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            Any,
            await self._request_stream_async(
                "get",
                "/v1/quotes/{quote}/pdf".format(
                    quote=sanitize_id(self.get("id"))
                ),
                params=params,
                base_address="files",
            ),
        )

    @classmethod
    def _cls_reestimate(
        cls, quote: str, **params: Unpack["QuoteReestimateParams"]
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
        quote: str, **params: Unpack["QuoteReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @overload
    def reestimate(self, **params: Unpack["QuoteReestimateParams"]) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @class_method_variant("_cls_reestimate")
    def reestimate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteReestimateParams"]
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
        cls, quote: str, **params: Unpack["QuoteReestimateParams"]
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
        quote: str, **params: Unpack["QuoteReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @overload
    async def reestimate_async(
        self, **params: Unpack["QuoteReestimateParams"]
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        ...

    @class_method_variant("_cls_reestimate_async")
    async def reestimate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["QuoteReestimateParams"]
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
        cls, id: str, **params: Unpack["QuoteRetrieveParams"]
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["QuoteRetrieveParams"]
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def list_preview_invoices(
        cls, quote: str, **params: Unpack["QuoteListPreviewInvoicesParams"]
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
        cls, quote: str, **params: Unpack["QuoteListPreviewInvoicesParams"]
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
        **params: Unpack["QuoteListPreviewSubscriptionSchedulesParams"],
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
        **params: Unpack["QuoteListPreviewSubscriptionSchedulesParams"],
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
