# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Person(UpdateableAPIResource["Person"]):
    """
    This is an object representing a person associated with a Stripe account.

    A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
    See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform prefilling and account onboarding steps.

    Related guide: [Handling identity verification with the API](https://stripe.com/docs/connect/identity-verification-api#person-information)
    """

    OBJECT_NAME = "person"
    account: str
    address: StripeObject
    address_kana: Optional[StripeObject]
    address_kanji: Optional[StripeObject]
    created: str
    dob: StripeObject
    email: Optional[str]
    first_name: Optional[str]
    first_name_kana: Optional[str]
    first_name_kanji: Optional[str]
    full_name_aliases: List[str]
    future_requirements: Optional[StripeObject]
    gender: Optional[str]
    id: str
    id_number_provided: bool
    id_number_secondary_provided: bool
    last_name: Optional[str]
    last_name_kana: Optional[str]
    last_name_kanji: Optional[str]
    maiden_name: Optional[str]
    metadata: Dict[str, str]
    nationality: Optional[str]
    object: Literal["person"]
    phone: Optional[str]
    political_exposure: str
    registered_address: StripeObject
    relationship: StripeObject
    requirements: Optional[StripeObject]
    ssn_last_4_provided: bool
    verification: StripeObject

    def instance_url(self):
        token = self.id
        account = self.account
        base = Account.class_url()
        acct_extn = quote_plus(account)
        extn = quote_plus(token)
        return "%s/%s/persons/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a person without an account ID. "
            "Use stripe.Account.modify_person('account_id', 'person_id', ...) "
            "(see https://stripe.com/docs/api/persons/update)."
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a person without an account ID. "
            "Use stripe.Account.retrieve_person('account_id', 'person_id') "
            "(see https://stripe.com/docs/api/persons/retrieve)."
        )
