# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Intent(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.billing.intent"]] = "v2.billing.intent"

    class AmountDetails(StripeObject):
        currency: str
        """
        Three-letter ISO currency code, in lowercase. Must be a supported currency.
        """
        discount: str
        """
        Amount of discount applied.
        """
        shipping: str
        """
        Amount of shipping charges.
        """
        subtotal: str
        """
        Subtotal amount before tax and discounts.
        """
        tax: str
        """
        Amount of tax.
        """
        total: str
        """
        Total amount for the Billing Intent.
        """

    class CadenceData(StripeObject):
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
                month_of_year: Optional[int]
                """
                The month to anchor the billing on for a type="month" billing cycle from
                1-12. Occurrences are calculated from the month anchor.
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

        class Payer(StripeObject):
            class BillingProfileData(StripeObject):
                customer: str
                """
                The customer to associate with the profile.
                """
                default_payment_method: Optional[str]
                """
                The default payment method to use when billing this profile.
                If none is provided, the customer `default_payment_method` will be used.
                """

            billing_profile: Optional[str]
            """
            The ID of the Billing Profile object which determines how a bill will be paid.
            """
            billing_profile_data: Optional[BillingProfileData]
            """
            Data for creating a new profile.
            """
            _inner_class_types = {"billing_profile_data": BillingProfileData}

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
        The billing cycle configuration for this Cadence.
        """
        payer: Payer
        """
        Information about the payer for this Cadence.
        """
        settings: Optional[Settings]
        """
        Settings for creating the Cadence.
        """
        _inner_class_types = {
            "billing_cycle": BillingCycle,
            "payer": Payer,
            "settings": Settings,
        }

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Time at which the Billing Intent was canceled.
        """
        committed_at: Optional[str]
        """
        Time at which the Billing Intent was committed.
        """
        drafted_at: Optional[str]
        """
        Time at which the Billing Intent was drafted.
        """
        reserved_at: Optional[str]
        """
        Time at which the Billing Intent was reserved.
        """

    amount_details: AmountDetails
    """
    Breakdown of the amount for this Billing Intent.
    """
    cadence: Optional[str]
    """
    ID of an existing Cadence to use.
    """
    cadence_data: Optional[CadenceData]
    """
    Data for creating a new Cadence.
    """
    created: str
    """
    Time at which the object was created.
    """
    currency: str
    """
    Three-letter ISO currency code, in lowercase. Must be a supported currency.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.billing.intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["canceled", "committed", "draft", "reserved"]
    """
    Current status of the Billing Intent.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for status transitions of the Billing Intent.
    """
    _inner_class_types = {
        "amount_details": AmountDetails,
        "cadence_data": CadenceData,
        "status_transitions": StatusTransitions,
    }
