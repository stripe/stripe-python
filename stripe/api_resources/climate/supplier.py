# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack


class Supplier(ListableAPIResource["Supplier"]):
    """
    A supplier of carbon removal.
    """

    OBJECT_NAME: ClassVar[Literal["climate.supplier"]] = "climate.supplier"

    class Location(StripeObject):
        city: Optional[str]
        """
        The city where the supplier is located.
        """
        country: str
        """
        Two-letter ISO code representing the country where the supplier is located.
        """
        latitude: Optional[float]
        """
        The geographic latitude where the supplier is located.
        """
        longitude: Optional[float]
        """
        The geographic longitude where the supplier is located.
        """
        region: Optional[str]
        """
        The state/county/province/region where the supplier is located.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    id: str
    """
    Unique identifier for the object.
    """
    info_url: str
    """
    Link to a webpage to learn more about the supplier.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    locations: List[Location]
    """
    The locations in which this supplier operates.
    """
    name: str
    """
    Name of this carbon removal supplier.
    """
    object: Literal["climate.supplier"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    removal_pathway: Literal[
        "biomass_carbon_removal_and_storage",
        "direct_air_capture",
        "enhanced_weathering",
        "various",
    ]
    """
    The scientific pathway used for carbon removal.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Supplier.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Supplier"]:
        """
        Lists all available Climate supplier objects.
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
        cls, id: str, **params: Unpack["Supplier.RetrieveParams"]
    ) -> "Supplier":
        """
        Retrieves a Climate supplier object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"locations": Location}
