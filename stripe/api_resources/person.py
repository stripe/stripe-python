# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from urllib.parse import quote_plus


class Person(UpdateableAPIResource):
    OBJECT_NAME = "person"

    def instance_url(self):
        base = Account.class_url()
        acct_extn = quote_plus(self.account)
        extn = quote_plus(self.id)
        return "%s/%s/persons/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a person without an account"
            "ID. Call save on account.persons.retrieve('person_id')"
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a person without an account"
            "ID. Use account.persons.retrieve('person_id')"
        )
