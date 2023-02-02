# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error
from stripe import util
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import VerifyMixin
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.six.moves.urllib.parse import quote_plus


class BankAccount(DeletableAPIResource, UpdateableAPIResource, VerifyMixin):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
    destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank Debits and Transfers](https://stripe.com/docs/payments/bank-debits-transfers).
    """

    OBJECT_NAME = "bank_account"

    def instance_url(self):
        token = util.utf8(self.id)
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = util.utf8(self.customer)

            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = util.utf8(self.account)

            base = Account.class_url()
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
