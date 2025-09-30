# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class BillSettingCreateParams(TypedDict):
    calculation: NotRequired["BillSettingCreateParamsCalculation"]
    """
    Settings related to calculating a bill.
    """
    display_name: NotRequired[str]
    """
    An optional customer-facing display name for the CollectionSetting object.
    Maximum length of 250 characters.
    """
    invoice: NotRequired["BillSettingCreateParamsInvoice"]
    """
    Settings related to invoice behavior.
    """
    invoice_rendering_template: NotRequired[str]
    """
    The ID of the invoice rendering template to be used when generating invoices.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key used to retrieve settings dynamically from a static string.
    This may be up to 200 characters.
    """


class BillSettingCreateParamsCalculation(TypedDict):
    tax: NotRequired["BillSettingCreateParamsCalculationTax"]
    """
    Settings for calculating tax.
    """


class BillSettingCreateParamsCalculationTax(TypedDict):
    type: Literal["automatic", "manual"]
    """
    Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
    """


class BillSettingCreateParamsInvoice(TypedDict):
    time_until_due: NotRequired["BillSettingCreateParamsInvoiceTimeUntilDue"]
    """
    The amount of time until the invoice will be overdue for payment.
    """


class BillSettingCreateParamsInvoiceTimeUntilDue(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit for the time until due.
    """
    interval_count: int
    """
    The number of interval units. For example, if interval=day and interval_count=30,
    the invoice will be due in 30 days.
    """
