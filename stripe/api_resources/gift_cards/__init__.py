# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.gift_cards package is deprecated, please change your
    imports to import from stripe.gift_cards directly.
    From:
      from stripe.api_resources.gift_cards import ...
    To:
      from stripe.gift_cards import ...
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.api_resources.gift_cards.card import Card
    from stripe.api_resources.gift_cards.transaction import Transaction
