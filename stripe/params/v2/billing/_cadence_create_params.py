# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceCreateParams(TypedDict):
    billing_cycle: "CadenceCreateParamsBillingCycle"
    """
    The billing cycle is the object that defines future billing cycle dates.
    """
    include: NotRequired[
        List[Literal["invoice_discount_rules", "settings_data"]]
    ]
    """
    Additional resource to include in the response.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key used to retrieve cadences dynamically from a static string. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    payer: "CadenceCreateParamsPayer"
    """
    The payer determines the entity financially responsible for the bill.
    """
    settings: NotRequired["CadenceCreateParamsSettings"]
    """
    The settings associated with the cadence.
    """


class CadenceCreateParamsBillingCycle(TypedDict):
    interval_count: NotRequired[int]
    """
    The number of intervals (specified in the interval attribute) between
    cadence billings. For example, type=month and interval_count=3 bills every
    3 months. If this is not provided, it will default to 1.
    """
    type: Literal["day", "month", "week", "year"]
    """
    The frequency at which a cadence bills.
    """
    day: NotRequired["CadenceCreateParamsBillingCycleDay"]
    """
    Specific configuration for determining billing dates when type=day.
    """
    month: NotRequired["CadenceCreateParamsBillingCycleMonth"]
    """
    Specific configuration for determining billing dates when type=month.
    """
    week: NotRequired["CadenceCreateParamsBillingCycleWeek"]
    """
    Specific configuration for determining billing dates when type=week.
    """
    year: NotRequired["CadenceCreateParamsBillingCycleYear"]
    """
    Specific configuration for determining billing dates when type=year.
    """


class CadenceCreateParamsBillingCycleDay(TypedDict):
    time: NotRequired["CadenceCreateParamsBillingCycleDayTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class CadenceCreateParamsBillingCycleDayTime(TypedDict):
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
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class CadenceCreateParamsBillingCycleMonth(TypedDict):
    day_of_month: int
    """
    The day to anchor the billing on for a type="month" billing cycle from
    1-31. If this number is greater than the number of days in the month being
    billed, this will anchor to the last day of the month. If not provided,
    this will default to the day the cadence was created.
    """
    month_of_year: NotRequired[int]
    """
    The month to anchor the billing on for a type="month" billing cycle from
    1-12. If not provided, this will default to the month the cadence was created.
    This setting can only be used for monthly billing cycles with `interval_count` of 2, 3, 4 or 6.
    All occurrences will be calculated from month provided.
    """
    time: NotRequired["CadenceCreateParamsBillingCycleMonthTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class CadenceCreateParamsBillingCycleMonthTime(TypedDict):
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
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class CadenceCreateParamsBillingCycleWeek(TypedDict):
    day_of_week: int
    """
    The day of the week to bill the type=week billing cycle on.
    Numbered from 1-7 for Monday to Sunday respectively, based on the ISO-8601
    week day numbering. If not provided, this will default to the day the
    cadence was created.
    """
    time: NotRequired["CadenceCreateParamsBillingCycleWeekTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class CadenceCreateParamsBillingCycleWeekTime(TypedDict):
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
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class CadenceCreateParamsBillingCycleYear(TypedDict):
    day_of_month: NotRequired[int]
    """
    The day to anchor the billing on for a type="month" billing cycle from
    1-31. If this number is greater than the number of days in the month being
    billed, this will anchor to the last day of the month. If not provided,
    this will default to the day the cadence was created.
    """
    month_of_year: NotRequired[int]
    """
    The month to bill on from 1-12. If not provided, this will default to the
    month the cadence was created.
    """
    time: NotRequired["CadenceCreateParamsBillingCycleYearTime"]
    """
    The time at which the billing cycle ends.
    This field is optional, and if not provided, it will default to
    the time at which the cadence was created in UTC timezone.
    """


class CadenceCreateParamsBillingCycleYearTime(TypedDict):
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
    second: int
    """
    The second at which the billing cycle ends.
    Must be an integer between 0 and 59, inclusive.
    """


class CadenceCreateParamsPayer(TypedDict):
    billing_profile: str
    """
    The ID of the Billing Profile object which determines how a bill will be paid.
    """


class CadenceCreateParamsSettings(TypedDict):
    bill: NotRequired["CadenceCreateParamsSettingsBill"]
    """
    Settings that configure bill generation, which includes calculating totals, tax, and presenting invoices.
    If no setting is provided here, the settings from the customer referenced on the payer will be used.
    If no customer settings are present, the merchant default settings will be used.
    """
    collection: NotRequired["CadenceCreateParamsSettingsCollection"]
    """
    Settings that configure and manage the behavior of collecting payments.
    If no setting is provided here, the settings from the customer referenced from the payer will be used if they exist.
    If no customer settings are present, the merchant default settings will be used.
    """


class CadenceCreateParamsSettingsBill(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of the Settings to use.
    If not provided, this will always default to the live version any time the settings are used.
    """


class CadenceCreateParamsSettingsCollection(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of the Settings to use.
    If not provided, this will always default to the live version any time the settings are used.
    """
