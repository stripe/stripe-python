# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Capability(UpdateableAPIResource["Capability"]):
    """
    This is an object representing a capability for a Stripe account.

    Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities)
    """

    OBJECT_NAME = "capability"
    account: ExpandableField["Account"]
    future_requirements: StripeObject
    id: str
    object: Literal["capability"]
    requested: bool
    requested_at: Optional[str]
    requirements: StripeObject
    status: str

    def instance_url(self):
        token = self.id
        account = self.account
        base = Account.class_url()
        if isinstance(account, Account):
            account = account.id
        acct_extn = quote_plus(account)
        extn = quote_plus(token)
        return "%s/%s/capabilities/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't update a capability without an account ID. Update a capability using "
            "account.modify_capability('acct_123', 'acap_123', params)"
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a capability without an account ID. Retrieve a capability using "
            "account.retrieve_capability('acct_123', 'acap_123')"
        )
