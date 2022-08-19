# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class BalanceTransaction(ListableAPIResource):
    """
    Balance transactions represent funds moving through your Stripe account.
    They're created for every type of transaction that comes into or flows out of your Stripe account balance.

    Related guide: [Balance Transaction Types](https://stripe.com/docs/reports/balance-transaction-types).
    """

    OBJECT_NAME = "balance_transaction"
