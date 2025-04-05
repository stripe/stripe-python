# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
<<<<<<<< HEAD:stripe/api_resources/margin.py
    The stripe.api_resources.margin package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.margin import Margin
    To:
      from stripe import Margin
========
    The stripe.api_resources.invoice_payment package is deprecated, please change your
    imports to import from stripe directly.
    From:
      from stripe.api_resources.invoice_payment import InvoicePayment
    To:
      from stripe import InvoicePayment
>>>>>>>> a47da3f0f8bc948761079c1f31eae014ae5250b7:stripe/api_resources/invoice_payment.py
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
<<<<<<<< HEAD:stripe/api_resources/margin.py
    from stripe._margin import (  # noqa
        Margin,
========
    from stripe._invoice_payment import (  # noqa
        InvoicePayment,
>>>>>>>> a47da3f0f8bc948761079c1f31eae014ae5250b7:stripe/api_resources/invoice_payment.py
    )
