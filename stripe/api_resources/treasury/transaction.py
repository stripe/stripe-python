# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class Transaction(ListableAPIResource):
    """
    Transactions represent changes to a [FinancialAccount's](https://stripe.com/docs/api#financial_accounts) balance.
    """

    OBJECT_NAME = "treasury.transaction"
