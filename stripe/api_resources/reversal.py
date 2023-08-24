# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.transfer import Transfer
from urllib.parse import quote_plus


class Reversal(UpdateableAPIResource):
    """
    [Stripe Connect](https://stripe.com/docs/connect) platforms can reverse transfers made to a
    connected account, either entirely or partially, and can also specify whether
    to refund any related application fees. Transfer reversals add to the
    platform's balance and subtract from the destination account's balance.

    Reversing a transfer that was made for a [destination
    charge](https://stripe.com/docs/connect/destination-charges) is allowed only up to the amount of
    the charge. It is possible to reverse a
    [transfer_group](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options)
    transfer only if the destination account has enough balance to cover the
    reversal.

    Related guide: [Reversing transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#reversing-transfers)
    """

    OBJECT_NAME = "transfer_reversal"

    def instance_url(self):
        token = self.id  # type: ignore
        transfer = self.transfer  # type: ignore
        base = Transfer.class_url()
        cust_extn = quote_plus(transfer)
        extn = quote_plus(token)
        return "%s/%s/reversals/%s" % (base, cust_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a reversal without a transfer ID. "
            "Use stripe.Transfer.modify_reversal('transfer_id', 'reversal_id', ...) "
            "(see https://stripe.com/docs/api/transfer_reversals/update)."
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a reversal without a transfer ID. "
            "Use stripe.Transfer.retrieve_reversal('transfer_id', 'reversal_id') "
            "(see https://stripe.com/docs/api/transfer_reversals/retrieve)."
        )
