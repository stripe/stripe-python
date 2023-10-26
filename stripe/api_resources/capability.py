# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Capability(UpdateableAPIResource["Capability"]):
    """
    This is an object representing a capability for a Stripe account.

    Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities)
    """

    OBJECT_NAME: ClassVar[Literal["capability"]] = "capability"
    account: ExpandableField["Account"]
    """
    The account for which the capability enables functionality.
    """
    future_requirements: Optional[StripeObject]
    id: str
    """
    The identifier for the capability.
    """
    object: Literal["capability"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requested: bool
    """
    Whether the capability has been requested.
    """
    requested_at: Optional[int]
    """
    Time at which the capability was requested. Measured in seconds since the Unix epoch.
    """
    requirements: Optional[StripeObject]
    status: Literal["active", "disabled", "inactive", "pending", "unrequested"]
    """
    The status of the capability. Can be `active`, `inactive`, `pending`, or `unrequested`.
    """

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
