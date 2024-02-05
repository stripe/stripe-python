# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack


class Margin(
    CreateableAPIResource["Margin"],
    ListableAPIResource["Margin"],
    UpdateableAPIResource["Margin"],
):
    """
    A (partner) margin represents a specific discount distributed in partner reseller programs to business partners who
    resell products and services and earn a discount (margin) for doing so.
    """

    OBJECT_NAME: ClassVar[Literal["margin"]] = "margin"

    class CreateParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Whether the margin can be applied to invoices, invoice items, or invoice line items or not. Defaults to `true`.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired["str"]
        """
        Name of the margin, which is displayed to customers, such as on invoices.
        """
        percent_off: float
        """
        Percent that will be taken off the subtotal before tax (after all other discounts and promotions) of any invoice to which the margin is applied.
        """

    class ListParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Only return margins that are active or inactive, i.e., pass false to list all inactive margins.
        """
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

    class ModifyParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Whether the margin can be applied to invoices, invoice items, or invoice line items or not.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired["str"]
        """
        Name of the margin, which is displayed to customers, such as on invoices.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    active: bool
    """
    Whether the margin can be applied to invoices, invoice items, or invoice line items. Defaults to `true`.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    Name of the margin that's displayed on, for example, invoices.
    """
    object: Literal["margin"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percent_off: float
    """
    Percent that will be taken off the subtotal before tax (after all other discounts and promotions) of any invoice to which the margin is applied.
    """
    updated: int
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """

    @classmethod
    def create(cls, **params: Unpack["Margin.CreateParams"]) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount.A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            "Margin",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Margin.CreateParams"]
    ) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount.A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
        """
        return cast(
            "Margin",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["Margin.ListParams"]
    ) -> ListObject["Margin"]:
        """
        Retrieve a list of your margins.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Margin.ListParams"]
    ) -> ListObject["Margin"]:
        """
        Retrieve a list of your margins.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Margin.ModifyParams"]
    ) -> "Margin":
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Margin",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Margin.ModifyParams"]
    ) -> "Margin":
        """
        Update the specified margin object. Certain fields of the margin object are not editable.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Margin",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Margin.RetrieveParams"]
    ) -> "Margin":
        """
        Retrieve a margin object with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Margin.RetrieveParams"]
    ) -> "Margin":
        """
        Retrieve a margin object with the given ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/billing/margins"
