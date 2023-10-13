# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


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
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    id: str
    object: Literal["exchange_rate"]
    rates: Dict[str, float]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ExchangeRate.ListParams"]
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
        cls, id: str, **params: Unpack["ExchangeRate.RetrieveParams"]
    ) -> "ExchangeRate":
        instance = cls(id, **params)
        instance.refresh()
        return instance
