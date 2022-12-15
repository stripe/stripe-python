# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Price(
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    """
    Prices define the unit cost, currency, and (optional) billing cycle for both recurring and one-time purchases of products.
    [Products](https://stripe.com/docs/api#products) help you track inventory or provisioning, and prices help you track payment terms. Different physical goods or levels of service should be represented by products, and pricing options should be represented by prices. This approach lets you change prices without having to change your provisioning scheme.

    For example, you might have a single "gold" product that has prices for $10/month, $100/year, and €9 once.

    Related guides: [Set up a subscription](https://stripe.com/docs/billing/subscriptions/set-up-subscription), [create an invoice](https://stripe.com/docs/billing/invoices/create), and more about [products and prices](https://stripe.com/docs/products-prices/overview).
    """

    OBJECT_NAME = "price"

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/prices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
