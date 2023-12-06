# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.capital package is deprecated, please change your
    imports to import from stripe.capital directly.
    From:
      from stripe.api_resources.capital import ...
    To:
      from stripe.capital import ...
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.api_resources.capital.financing_offer import FinancingOffer
    from stripe.api_resources.capital.financing_summary import FinancingSummary
    from stripe.api_resources.capital.financing_transaction import (
        FinancingTransaction,
    )
