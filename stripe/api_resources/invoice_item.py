# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class InvoiceItem(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Sometimes you want to add a charge or credit to a customer, but actually
    charge or credit the customer's card only at the end of a regular billing
    cycle. This is useful for combining several charges (to minimize
    per-transaction fees), or for having Stripe tabulate your usage-based billing
    totals.

    Related guide: [Subscription Invoices](https://stripe.com/docs/billing/invoices/subscription#adding-upcoming-invoice-items).
    """

    OBJECT_NAME = "invoiceitem"
