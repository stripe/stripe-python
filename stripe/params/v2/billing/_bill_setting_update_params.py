# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class BillSettingUpdateParams(TypedDict):
    calculation: NotRequired["BillSettingUpdateParamsCalculation"]
    """
    Settings related to calculating a bill.
    """
    display_name: NotRequired[str]
    """
    An optional customer-facing display name for the BillSetting object.
    To remove the display name, set it to an empty string in the request.
    Maximum length of 250 characters.
    """
    invoice: NotRequired["BillSettingUpdateParamsInvoice"]
    """
    Settings related to invoice behavior.
    """
    invoice_rendering_template: NotRequired[str]
    """
    The ID of the invoice rendering template to be used when generating invoices.
    """
    live_version: NotRequired[str]
    """
    Optionally change the live version of the BillSetting. Providing `live_version = "latest"` will set the
    BillSetting' `live_version` to its latest version.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key used to retrieve settings dynamically from a static string.
    This may be up to 200 characters.
    """


class BillSettingUpdateParamsCalculation(TypedDict):
    tax: NotRequired["BillSettingUpdateParamsCalculationTax"]
    """
    Settings for calculating tax.
    """


class BillSettingUpdateParamsCalculationTax(TypedDict):
    type: Literal["automatic", "manual"]
    """
    Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
    """


class BillSettingUpdateParamsInvoice(TypedDict):
    time_until_due: NotRequired["BillSettingUpdateParamsInvoiceTimeUntilDue"]
    """
    The amount of time until the invoice will be overdue for payment.
    """


class BillSettingUpdateParamsInvoiceTimeUntilDue(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    The interval unit for the time until due.
    """
    interval_count: int
    """
    The number of interval units. For example, if interval=day and interval_count=30,
    the invoice will be due in 30 days.
    """
