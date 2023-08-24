# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from urllib.parse import quote_plus


class Card(DeletableAPIResource, UpdateableAPIResource):
    """
    You can store multiple cards on a customer in order to charge the customer
    later. You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card payments with Sources](https://stripe.com/docs/sources/cards)
    """

    OBJECT_NAME = "card"

    def instance_url(self):
        token = self.id  # type: ignore
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = self.customer  # type: ignore

            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = self.account  # type: ignore

            base = Account.class_url()
            owner_extn = quote_plus(account)
            class_base = "external_accounts"

        else:
            raise error.InvalidRequestError(
                "Could not determine whether card_id %s is "
                "attached to a customer, or "
                "account." % token,
                "id",
            )

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a card without a customer or account ID. "
            "Use stripe.Customer.modify_source('customer_id', 'card_id', ...) "
            "(see https://stripe.com/docs/api/cards/update) or "
            "stripe.Account.modify_external_account('account_id', 'card_id', ...) "
            "(see https://stripe.com/docs/api/external_account_cards/update)."
        )

    @classmethod
    def retrieve(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        raise NotImplementedError(
            "Can't retrieve a card without a customer or account ID. "
            "Use stripe.Customer.retrieve_source('customer_id', 'card_id') "
            "(see https://stripe.com/docs/api/cards/retrieve) or "
            "stripe.Account.retrieve_external_account('account_id', 'card_id') "
            "(see https://stripe.com/docs/api/external_account_cards/retrieve)."
        )
