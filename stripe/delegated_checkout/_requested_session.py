# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.delegated_checkout._requested_session_confirm_params import (
        RequestedSessionConfirmParams,
    )
    from stripe.params.delegated_checkout._requested_session_create_params import (
        RequestedSessionCreateParams,
    )
    from stripe.params.delegated_checkout._requested_session_expire_params import (
        RequestedSessionExpireParams,
    )
    from stripe.params.delegated_checkout._requested_session_modify_params import (
        RequestedSessionModifyParams,
    )
    from stripe.params.delegated_checkout._requested_session_retrieve_params import (
        RequestedSessionRetrieveParams,
    )


class RequestedSession(
    CreateableAPIResource["RequestedSession"],
    UpdateableAPIResource["RequestedSession"],
):
    """
    A requested session is a session that has been requested by a customer.
    """

    OBJECT_NAME: ClassVar[Literal["delegated_checkout.requested_session"]] = (
        "delegated_checkout.requested_session"
    )

    class FulfillmentDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1, such as the street, PO Box, or company name.
            """
            line2: Optional[str]
            """
            Address line 2, such as the apartment, suite, unit, or building.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        class FulfillmentOption(StripeObject):
            class Shipping(StripeObject):
                class ShippingOption(StripeObject):
                    description: Optional[str]
                    """
                    The description of the shipping option.
                    """
                    display_name: str
                    """
                    The display name of the shipping option.
                    """
                    earliest_delivery_time: Optional[int]
                    """
                    The earliest delivery time of the shipping option.
                    """
                    key: str
                    """
                    The key of the shipping option.
                    """
                    latest_delivery_time: Optional[int]
                    """
                    The latest delivery time of the shipping option.
                    """
                    shipping_amount: int
                    """
                    The shipping amount of the shipping option.
                    """

                shipping_options: Optional[List[ShippingOption]]
                """
                The shipping options.
                """
                _inner_class_types = {"shipping_options": ShippingOption}

            shipping: Optional[Shipping]
            """
            The shipping option.
            """
            type: str
            """
            The type of the fulfillment option.
            """
            _inner_class_types = {"shipping": Shipping}

        class SelectedFulfillmentOption(StripeObject):
            class Shipping(StripeObject):
                shipping_option: Optional[str]
                """
                The shipping option.
                """

            shipping: Optional[Shipping]
            """
            The shipping option.
            """
            type: str
            """
            The type of the selected fulfillment option.
            """
            _inner_class_types = {"shipping": Shipping}

        address: Optional[Address]
        """
        The fulfillment address.
        """
        email: Optional[str]
        """
        The email address for the fulfillment details.
        """
        fulfillment_options: Optional[List[FulfillmentOption]]
        """
        The fulfillment options.
        """
        name: Optional[str]
        """
        The name for the fulfillment details.
        """
        phone: Optional[str]
        """
        The phone number for the fulfillment details.
        """
        selected_fulfillment_option: Optional[SelectedFulfillmentOption]
        """
        The fulfillment option.
        """
        _inner_class_types = {
            "address": Address,
            "fulfillment_options": FulfillmentOption,
            "selected_fulfillment_option": SelectedFulfillmentOption,
        }

    class LineItemDetail(StripeObject):
        description: Optional[str]
        """
        The description of the line item.
        """
        images: Optional[List[str]]
        """
        The images of the line item.
        """
        key: str
        """
        The key of the line item.
        """
        name: str
        """
        The name of the line item.
        """
        quantity: int
        """
        The quantity of the line item.
        """
        sku_id: str
        """
        The SKU ID of the line item.
        """
        unit_amount: int
        """
        The unit amount of the line item.
        """

    class OrderDetails(StripeObject):
        order_status_url: Optional[str]
        """
        The URL to the order status.
        """

    class SellerDetails(StripeObject):
        pass

    class TotalDetails(StripeObject):
        amount_discount: Optional[int]
        """
        The amount discount of the total details.
        """
        amount_fulfillment: Optional[int]
        """
        The amount fulfillment of the total details.
        """
        amount_tax: Optional[int]
        """
        The amount tax of the total details.
        """

    amount_subtotal: int
    """
    The subtotal amount of the requested session.
    """
    amount_total: int
    """
    The total amount of the requested session.
    """
    created_at: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[str]
    """
    The customer for this requested session.
    """
    expires_at: int
    """
    Time at which the requested session expires. Measured in seconds since the Unix epoch.
    """
    fulfillment_details: Optional[FulfillmentDetails]
    """
    The details of the fulfillment.
    """
    id: str
    """
    Unique identifier for the object.
    """
    line_item_details: List[LineItemDetail]
    """
    The line items to be purchased.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["delegated_checkout.requested_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    order_details: Optional[OrderDetails]
    """
    The details of the order.
    """
    payment_method: Optional[str]
    """
    The payment method used for the requested session.
    """
    seller_details: SellerDetails
    setup_future_usage: Optional[Literal["on_session"]]
    """
    Whether or not the payment method should be saved for future use.
    """
    shared_metadata: Optional[Dict[str, str]]
    """
    The metadata shared with the seller.
    """
    shared_payment_issued_token: Optional[str]
    """
    The SPT used for payment.
    """
    status: Literal["completed", "expired", "open"]
    """
    The status of the requested session.
    """
    total_details: TotalDetails
    updated_at: int
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """

    @classmethod
    def _cls_confirm(
        cls,
        requested_session: str,
        **params: Unpack["RequestedSessionConfirmParams"],
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            cls._static_request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(requested_session)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def confirm(
        requested_session: str,
        **params: Unpack["RequestedSessionConfirmParams"],
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        ...

    @overload
    def confirm(
        self, **params: Unpack["RequestedSessionConfirmParams"]
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        ...

    @class_method_variant("_cls_confirm")
    def confirm(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RequestedSessionConfirmParams"]
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_confirm_async(
        cls,
        requested_session: str,
        **params: Unpack["RequestedSessionConfirmParams"],
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            await cls._static_request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(requested_session)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def confirm_async(
        requested_session: str,
        **params: Unpack["RequestedSessionConfirmParams"],
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        ...

    @overload
    async def confirm_async(
        self, **params: Unpack["RequestedSessionConfirmParams"]
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        ...

    @class_method_variant("_cls_confirm_async")
    async def confirm_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RequestedSessionConfirmParams"]
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(
        cls, **params: Unpack["RequestedSessionCreateParams"]
    ) -> "RequestedSession":
        """
        Creates a requested session
        """
        return cast(
            "RequestedSession",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["RequestedSessionCreateParams"]
    ) -> "RequestedSession":
        """
        Creates a requested session
        """
        return cast(
            "RequestedSession",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_expire(
        cls,
        requested_session: str,
        **params: Unpack["RequestedSessionExpireParams"],
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            cls._static_request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(requested_session)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def expire(
        requested_session: str,
        **params: Unpack["RequestedSessionExpireParams"],
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        ...

    @overload
    def expire(
        self, **params: Unpack["RequestedSessionExpireParams"]
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        ...

    @class_method_variant("_cls_expire")
    def expire(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RequestedSessionExpireParams"]
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_expire_async(
        cls,
        requested_session: str,
        **params: Unpack["RequestedSessionExpireParams"],
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            await cls._static_request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(requested_session)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def expire_async(
        requested_session: str,
        **params: Unpack["RequestedSessionExpireParams"],
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        ...

    @overload
    async def expire_async(
        self, **params: Unpack["RequestedSessionExpireParams"]
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        ...

    @class_method_variant("_cls_expire_async")
    async def expire_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RequestedSessionExpireParams"]
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["RequestedSessionModifyParams"]
    ) -> "RequestedSession":
        """
        Updates a requested session
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "RequestedSession",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["RequestedSessionModifyParams"]
    ) -> "RequestedSession":
        """
        Updates a requested session
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "RequestedSession",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["RequestedSessionRetrieveParams"]
    ) -> "RequestedSession":
        """
        Retrieves a requested session
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["RequestedSessionRetrieveParams"]
    ) -> "RequestedSession":
        """
        Retrieves a requested session
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "fulfillment_details": FulfillmentDetails,
        "line_item_details": LineItemDetail,
        "order_details": OrderDetails,
        "seller_details": SellerDetails,
        "total_details": TotalDetails,
    }
