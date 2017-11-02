from __future__ import absolute_import, division, print_function

from stripe.api_resources.transfer import Transfer
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Recipient(CreateableAPIResource, UpdateableAPIResource,
                ListableAPIResource, DeletableAPIResource):
    OBJECT_NAME = 'recipient'

    def transfers(self, **params):
        params['recipient'] = self.id
        transfers = Transfer.list(self.api_key, **params)
        return transfers
