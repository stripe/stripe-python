# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Card(DeletableAPIResource["Card"], UpdateableAPIResource["Card"]):
    """
    You can store multiple cards on a customer in order to charge the customer
    later. You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card payments with Sources](https://stripe.com/docs/sources/cards)
    """

    OBJECT_NAME = "card"
    account: Optional[ExpandableField["Account"]]
    address_city: Optional[str]
    address_country: Optional[str]
    address_line1: Optional[str]
    address_line1_check: Optional[str]
    address_line2: Optional[str]
    address_state: Optional[str]
    address_zip: Optional[str]
    address_zip_check: Optional[str]
    available_payout_methods: Optional[List[str]]
    brand: str
    country: Optional[str]
    currency: Optional[str]
    customer: Optional[ExpandableField[Any]]
    cvc_check: Optional[str]
    default_for_currency: Optional[bool]
    description: str
    dynamic_last4: Optional[str]
    exp_month: int
    exp_year: int
    fingerprint: Optional[str]
    funding: str
    id: str
    iin: str
    issuer: str
    last4: str
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["card"]
    status: Optional[str]
    tokenization_method: Optional[str]

    def instance_url(self):
        token = self.id
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = self.customer

            base = Customer.class_url()
            assert customer is not None
            owner_extn = quote_plus(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = self.account

            base = Account.class_url()
            assert account is not None
            if isinstance(account, Account):
                account = account.id
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
