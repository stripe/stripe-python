# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.gift_cards._card_service import CardService
from stripe.gift_cards._transaction_service import TransactionService


class GiftCardsService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.cards = CardService(self._requestor)
        self.transactions = TransactionService(self._requestor)
