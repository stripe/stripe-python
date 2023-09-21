# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from typing import Any, Dict, Optional
from typing_extensions import Literal


class ExchangeRate(ListableAPIResource["ExchangeRate"]):
    """
    `Exchange Rate` objects allow you to determine the rates that Stripe is
    currently using to convert from one currency to another. Since this number is
    variable throughout the day, there are various reasons why you might want to
    know the current rate (for example, to dynamically price an item for a user
    with a default payment in a foreign currency).

    If you want a guarantee that the charge is made with a certain exchange rate
    you expect is current, you can pass in `exchange_rate` to charges endpoints.
    If the value is no longer up to date, the charge won't go through. Please
    refer to our [Exchange Rates API](https://stripe.com/docs/exchange-rates) guide for more
    details.
    """

    OBJECT_NAME = "exchange_rate"
    id: str
    object: Literal["exchange_rate"]
    rates: Dict[str, float]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["ExchangeRate"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ExchangeRate":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
