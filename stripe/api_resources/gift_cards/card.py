# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.gift_cards.card package is deprecated, please change your
    imports to import from stripe.gift_cards directly.
    From:
      from stripe.api_resources.gift_cards.card import Card
    To:
      from stripe.gift_cards import Card
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.gift_cards._card import (  # noqa
        Card,
    )
