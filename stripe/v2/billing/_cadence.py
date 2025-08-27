# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class Cadence(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.cadence"]] = "v2.billing.cadence"

    class BillingCycle(StripeObject):
        class Day(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Month(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_month: int
            """
            The day to anchor the billing on for a type="month" billing cycle from 1-31.
            If this number is greater than the number of days in the month being billed,
            this will anchor to the last day of the month.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Week(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_week: int
            """
            The day of the week to bill the type=week billing cycle on.
            Numbered from 1-7 for Monday to Sunday respectively, based on the ISO-8601 week day numbering.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        class Year(StripeObject):
            class Time(StripeObject):
                hour: int
                """
                The hour at which the billing cycle ends.
                This must be an integer between 0 and 23, inclusive.
                0 represents midnight, and 23 represents 11 PM.
                """
                minute: int
                """
                The minute at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """
                second: Optional[int]
                """
                The second at which the billing cycle ends.
                Must be an integer between 0 and 59, inclusive.
                """

            day_of_month: int
            """
            The day to anchor the billing on for a type="month" billing cycle from 1-31.
            If this number is greater than the number of days in the month being billed,
            this will anchor to the last day of the month.
            """
            month_of_year: int
            """
            The month to bill on from 1-12. If not provided, this will default to the month the cadence was created.
            """
            time: Time
            """
            The time at which the billing cycle ends.
            """
            _inner_class_types = {"time": Time}

        day: Optional[Day]
        """
        Specific configuration for determining billing dates when type=day.
        """
        interval_count: int
        """
        The number of intervals (specified in the interval attribute) between cadence billings. For example, type=month and interval_count=3 bills every 3 months.
        """
        month: Optional[Month]
        """
        Specific configuration for determining billing dates when type=month.
        """
        type: Literal["day", "month", "week", "year"]
        """
        The frequency at which a cadence bills.
        """
        week: Optional[Week]
        """
        Specific configuration for determining billing dates when type=week.
        """
        year: Optional[Year]
        """
        Specific configuration for determining billing dates when type=year.
        """
        _inner_class_types = {
            "day": Day,
            "month": Month,
            "week": Week,
            "year": Year,
        }

    class InvoiceDiscountRule(StripeObject):
        class PercentOff(StripeObject):
            class MaximumApplications(StripeObject):
                type: Literal["indefinite"]
                """
                Max applications type of this discount, ex: indefinite.
                """

            maximum_applications: MaximumApplications
            """
            The maximum applications configuration for this discount.
            """
            percent_off: str
            """
            Percent that will be taken off of the amount. For example, percent_off of 50.0 will make $100 amount $50 instead.
            """
            _inner_class_types = {"maximum_applications": MaximumApplications}

        id: str
        """
        Unique identifier for the object.
        """
        percent_off: Optional[PercentOff]
        """
        Details if the discount is a percentage off.
        """
        type: Literal["percent_off"]
        """
        The type of the discount.
        """
        _inner_class_types = {"percent_off": PercentOff}

    class Payer(StripeObject):
        billing_profile: Optional[str]
        """
        The ID of the Billing Profile object which determines how a bill will be paid.
        """
        customer: Optional[str]
        """
        The ID of the Customer object.
        """
        type: Literal["customer"]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class Settings(StripeObject):
        class Bill(StripeObject):
            id: str
            """
            The ID of the referenced settings object.
            """
            version: Optional[str]
            """
            Returns the Settings Version when the cadence is pinned to a specific version.
            """

        class Collection(StripeObject):
            id: str
            """
            The ID of the referenced settings object.
            """
            version: Optional[str]
            """
            Returns the Settings Version when the cadence is pinned to a specific version.
            """

        bill: Optional[Bill]
        """
        Settings that configure bills generation, which includes calculating totals, tax, and presenting invoices.
        """
        collection: Optional[Collection]
        """
        Settings that configure and manage the behavior of collecting payments.
        """
        _inner_class_types = {"bill": Bill, "collection": Collection}

    billing_cycle: BillingCycle
    """
    The billing cycle is the object that defines future billing cycle dates.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_discount_rules: Optional[List[InvoiceDiscountRule]]
    """
    The discount rules applied to all invoices for the cadence.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_billing_date: Optional[str]
    """
    The date that the billing cadence will next bill. Null if the cadence is not active.
    """
    object: Literal["v2.billing.cadence"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payer: Payer
    """
    The payer determines the entity financially responsible for the bill.
    """
    settings: Optional[Settings]
    """
    The settings associated with the cadence.
    """
    status: Literal["active", "canceled"]
    """
    The current status of the cadence.
    """
    test_clock: Optional[str]
    """
    The ID of the Test Clock.
    """
    _inner_class_types = {
        "billing_cycle": BillingCycle,
        "invoice_discount_rules": InvoiceDiscountRule,
        "payer": Payer,
        "settings": Settings,
    }
