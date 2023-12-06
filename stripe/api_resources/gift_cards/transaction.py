# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.gift_cards.transaction package is deprecated, please change your
    imports to import from stripe.gift_cards directly.
    From:
      from stripe.api_resources.gift_cards.transaction import Transaction
    To:
      from stripe.gift_cards import Transaction
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.gift_cards._transaction import (  # noqa
        Transaction,
    )
