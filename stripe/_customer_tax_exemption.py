# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class CustomerTaxExemption(StripeObject):
    """
    Location specific customer tax exemptions.
    """

    OBJECT_NAME: ClassVar[Literal["customer_tax_exemption"]] = (
        "customer_tax_exemption"
    )

    class Ca(StripeObject):
        state: Optional[str]
        """
        Two-letter Canadian province code (ISO 3166-2). Null for country-wide GST/HST exemptions.
        """
        tax_type: str
        """
        The type of Canadian tax (gst_hst, PST, QST, RST).
        """

    class Us(StripeObject):
        state: str
        """
        Two-letter US state code (ISO 3166-2).
        """

    ca: Optional[Ca]
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: str
    """
    ID of the customer this tax exemption belongs to.
    """
    deleted: Optional[bool]
    """
    Present and true when the exemption has been deleted.
    """
    effective_date: str
    """
    ISO 8601 date (YYYY-MM-DD) when the exemption becomes effective.
    """
    expiration_date: Optional[str]
    """
    ISO 8601 date (YYYY-MM-DD) when the exemption expires.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["customer_tax_exemption"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    us: Optional[Us]
    _inner_class_types = {"ca": Ca, "us": Us}
