# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class TransactionEntry(ListableAPIResource):
    OBJECT_NAME = "treasury.transaction_entry"

    @classmethod
    def class_url(cls):
        return "/v1/treasury/transaction_entries"
