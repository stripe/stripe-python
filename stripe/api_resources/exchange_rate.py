# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import ClassVar, Dict, List, Optional
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

    OBJECT_NAME: ClassVar[Literal["exchange_rate"]] = "exchange_rate"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with the exchange rate for currency X your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and total number of supported payout currencies, and the default is the max.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with the exchange rate for currency X, your subsequent call can include `starting_after=X` in order to fetch the next page of the list.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    id: str
    """
    Unique identifier for the object. Represented as the three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) in lowercase.
    """
    object: Literal["exchange_rate"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    rates: Dict[str, float]
    """
    Hash where the keys are supported currencies and the values are the exchange rate at which the base id currency converts to the key currency.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ExchangeRate.ListParams"]
    ) -> ListObject["ExchangeRate"]:
        """
        Returns a list of objects that contain the rates at which foreign currencies are converted to one another. Only shows the currencies for which Stripe supports.
        """
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
        """
        Retrieves the exchange rates from the given currency to every supported currency.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance
