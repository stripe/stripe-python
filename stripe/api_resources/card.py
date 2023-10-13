# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources.abstract import (
    DeletableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.bank_account import BankAccount


class Card(DeletableAPIResource["Card"], UpdateableAPIResource["Card"]):
    """
    You can store multiple cards on a customer in order to charge the customer
    later. You can also store multiple debit cards on a recipient in order to
    transfer to those cards later.

    Related guide: [Card payments with Sources](https://stripe.com/docs/sources/cards)
    """

    OBJECT_NAME = "card"
    if TYPE_CHECKING:

        class DeleteParams(RequestOptions):
            pass

    account: Optional[ExpandableField["Account"]]
    address_city: Optional[str]
    address_country: Optional[str]
    address_line1: Optional[str]
    address_line1_check: Optional[str]
    address_line2: Optional[str]
    address_state: Optional[str]
    address_zip: Optional[str]
    address_zip_check: Optional[str]
    available_payout_methods: Optional[List[Literal["instant", "standard"]]]
    brand: str
    country: Optional[str]
    currency: Optional[str]
    customer: Optional[ExpandableField["Customer"]]
    cvc_check: Optional[str]
    default_for_currency: Optional[bool]
    description: Optional[str]
    dynamic_last4: Optional[str]
    exp_month: int
    exp_year: int
    fingerprint: Optional[str]
    funding: str
    id: str
    iin: Optional[str]
    issuer: Optional[str]
    last4: str
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["card"]
    status: Optional[str]
    tokenization_method: Optional[str]
    deleted: Optional[Literal[True]]

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Card.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["Card.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    def instance_url(self):
        token = self.id
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = self.customer

            base = Customer.class_url()
            assert customer is not None
            if isinstance(customer, Customer):
                customer = customer.id
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
