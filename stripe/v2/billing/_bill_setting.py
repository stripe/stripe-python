# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class BillSetting(StripeObject):
    """
    BillSetting is responsible for settings which dictate generating bills, which include settings for calculating totals on bills, tax on bill items, as well as how to generate and present invoices.
    """

    OBJECT_NAME: ClassVar[Literal["v2.billing.bill_setting"]] = (
        "v2.billing.bill_setting"
    )

    class Calculation(StripeObject):
        class Tax(StripeObject):
            type: Literal["automatic", "manual"]
            """
            Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
            """

        tax: Optional[Tax]
        """
        Settings for calculating tax.
        """
        _inner_class_types = {"tax": Tax}

    class Invoice(StripeObject):
        class TimeUntilDue(StripeObject):
            interval: Literal["day", "month", "week", "year"]
            """
            The interval unit for the time until due.
            """
            interval_count: int
            """
            The number of interval units. For example, if interval=day and interval_count=30,
            the invoice will be due in 30 days.
            """

        time_until_due: Optional[TimeUntilDue]
        """
        The amount of time until the invoice will be overdue for payment.
        """
        _inner_class_types = {"time_until_due": TimeUntilDue}

    calculation: Optional[Calculation]
    """
    Settings related to calculating a bill.
    """
    created: str
    """
    Timestamp of when the object was created.
    """
    display_name: Optional[str]
    """
    An optional field for adding a display name for the BillSetting object.
    """
    id: str
    """
    The ID of the BillSetting object.
    """
    invoice: Optional[Invoice]
    """
    Settings related to invoice behavior.
    """
    invoice_rendering_template: Optional[str]
    """
    The ID of the invoice rendering template to be used when generating invoices.
    """
    latest_version: str
    """
    The latest version of the current settings object. This will be
    Updated every time an attribute of the settings is updated.
    """
    live_version: str
    """
    The current live version of the settings object. This can be different from
    latest_version if settings are updated without setting live_version='latest'.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    lookup_key: Optional[str]
    """
    A lookup key used to retrieve settings dynamically from a static string.
    This may be up to 200 characters.
    """
    object: Literal["v2.billing.bill_setting"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"calculation": Calculation, "invoice": Invoice}
