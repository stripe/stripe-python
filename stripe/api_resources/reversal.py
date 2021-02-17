# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.transfer import Transfer
from urllib.parse import quote_plus


class Reversal(UpdateableAPIResource):
    OBJECT_NAME = "transfer_reversal"

    def instance_url(self):
        base = Transfer.class_url()
        cust_extn = quote_plus(self.transfer)
        extn = quote_plus(self.id)
        return "%s/%s/reversals/%s" % (base, cust_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a reversal without a transfer"
            "ID. Call save on transfer.reversals.retrieve('reversal_id')"
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a reversal without a transfer"
            "ID. Use transfer.reversals.retrieve('reversal_id')"
        )
