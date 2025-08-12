# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.billing.credit_balance_transaction package is deprecated, please change your
    imports to import from stripe.billing directly.
    From:
      from stripe.api_resources.billing.credit_balance_transaction import CreditBalanceTransaction
    To:
      from stripe.billing import CreditBalanceTransaction
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.billing._credit_balance_transaction import (  # noqa
        CreditBalanceTransaction,
    )
