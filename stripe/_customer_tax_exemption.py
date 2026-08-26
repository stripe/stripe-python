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
    created: int
    customer: str
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
    livemode: bool
    object: Literal["customer_tax_exemption"]
    us: Optional[Us]
    _inner_class_types = {"ca": Ca, "us": Us}
