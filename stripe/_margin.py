# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._margin_create_params import MarginCreateParams
    from stripe.params._margin_list_params import MarginListParams
    from stripe.params._margin_modify_params import MarginModifyParams
    from stripe.params._margin_retrieve_params import MarginRetrieveParams


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
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
    def create(cls, **params: Unpack["MarginCreateParams"]) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
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
        cls, **params: Unpack["MarginCreateParams"]
    ) -> "Margin":
        """
        Create a margin object to be used with invoices, invoice items, and invoice line items for a customer to represent a partner discount. A margin has a percent_off which is the percent that will be taken off the subtotal after all items and other discounts and promotions) of any invoices for a customer. Calculation of prorations do not include any partner margins applied on the original invoice item.
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
        cls, **params: Unpack["MarginListParams"]
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
        cls, **params: Unpack["MarginListParams"]
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
        cls, id: str, **params: Unpack["MarginModifyParams"]
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
        cls, id: str, **params: Unpack["MarginModifyParams"]
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
        cls, id: str, **params: Unpack["MarginRetrieveParams"]
    ) -> "Margin":
        """
        Retrieve a margin object with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["MarginRetrieveParams"]
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
