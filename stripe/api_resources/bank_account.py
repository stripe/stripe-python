# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources.abstract import (
    DeletableAPIResource,
    UpdateableAPIResource,
    VerifyMixin,
)
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.card import Card


class BankAccount(
    DeletableAPIResource["BankAccount"],
    UpdateableAPIResource["BankAccount"],
    VerifyMixin,
):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
    destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](https://stripe.com/docs/payments/bank-debits-transfers)
    """

    OBJECT_NAME = "bank_account"
    if TYPE_CHECKING:

        class DeleteParams(RequestOptions):
            pass

    account: Optional[ExpandableField["Account"]]
    account_holder_name: Optional[str]
    account_holder_type: Optional[str]
    account_type: Optional[str]
    available_payout_methods: Optional[List[Literal["instant", "standard"]]]
    bank_name: Optional[str]
    country: str
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    default_for_currency: Optional[bool]
    fingerprint: Optional[str]
    future_requirements: Optional[StripeObject]
    id: str
    last4: str
    metadata: Optional[Dict[str, str]]
    object: Literal["bank_account"]
    requirements: Optional[StripeObject]
    routing_number: Optional[str]
    status: str
    deleted: Optional[Literal[True]]

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["BankAccount.DeleteParams"]
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
                "Could not determine whether bank_account_id %s is "
                "attached to a customer or an account." % token,
                "id",
            )

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a bank account without a customer or account ID. "
            "Use stripe.Customer.modify_source('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/customer_bank_accounts/update) or "
            "stripe.Account.modify_external_account('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/update)."
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
            "Can't retrieve a bank account without a customer or account ID. "
            "Use stripe.customer.retrieve_source('customer_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/customer_bank_accounts/retrieve) or "
            "stripe.Account.retrieve_external_account('account_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/retrieve)."
        )
