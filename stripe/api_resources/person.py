# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Person(UpdateableAPIResource["Person"]):
    """
    This is an object representing a person associated with a Stripe account.

    A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
    See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform prefilling and account onboarding steps.

    Related guide: [Handling identity verification with the API](https://stripe.com/docs/connect/handling-api-verification#person-information)
    """

    OBJECT_NAME: ClassVar[Literal["person"]] = "person"
    account: Optional[str]
    """
    The account the person is associated with.
    """
    additional_tos_acceptances: Optional[StripeObject]
    address: Optional[StripeObject]
    address_kana: Optional[StripeObject]
    """
    The Kana variation of the person's address (Japan only).
    """
    address_kanji: Optional[StripeObject]
    """
    The Kanji variation of the person's address (Japan only).
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    dob: Optional[StripeObject]
    email: Optional[str]
    """
    The person's email address.
    """
    first_name: Optional[str]
    """
    The person's first name.
    """
    first_name_kana: Optional[str]
    """
    The Kana variation of the person's first name (Japan only).
    """
    first_name_kanji: Optional[str]
    """
    The Kanji variation of the person's first name (Japan only).
    """
    full_name_aliases: Optional[List[str]]
    """
    A list of alternate names or aliases that the person is known by.
    """
    future_requirements: Optional[StripeObject]
    """
    Information about the [upcoming new requirements for this person](https://stripe.com/docs/connect/custom-accounts/future-requirements), including what information needs to be collected, and by when.
    """
    gender: Optional[str]
    """
    The person's gender (International regulations require either "male" or "female").
    """
    id: str
    """
    Unique identifier for the object.
    """
    id_number_provided: Optional[bool]
    """
    Whether the person's `id_number` was provided. True if either the full ID number was provided or if only the required part of the ID number was provided (ex. last four of an individual's SSN for the US indicated by `ssn_last_4_provided`).
    """
    id_number_secondary_provided: Optional[bool]
    """
    Whether the person's `id_number_secondary` was provided.
    """
    last_name: Optional[str]
    """
    The person's last name.
    """
    last_name_kana: Optional[str]
    """
    The Kana variation of the person's last name (Japan only).
    """
    last_name_kanji: Optional[str]
    """
    The Kanji variation of the person's last name (Japan only).
    """
    maiden_name: Optional[str]
    """
    The person's maiden name.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationality: Optional[str]
    """
    The country where the person is a national.
    """
    object: Literal["person"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone: Optional[str]
    """
    The person's phone number.
    """
    political_exposure: Optional[Literal["existing", "none"]]
    """
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    """
    registered_address: Optional[StripeObject]
    relationship: Optional[StripeObject]
    requirements: Optional[StripeObject]
    """
    Information about the requirements for this person, including what information needs to be collected, and by when.
    """
    ssn_last_4_provided: Optional[bool]
    """
    Whether the last four digits of the person's Social Security number have been provided (U.S. only).
    """
    verification: Optional[StripeObject]
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    def instance_url(self):
        token = self.id
        account = self.account
        base = Account.class_url()
        assert account is not None
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
