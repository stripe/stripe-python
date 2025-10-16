# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, cast, overload
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
        pass

    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[str]
    """
    The customer for this requested session.
    """
    fulfillment_details: Optional[FulfillmentDetails]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["delegated_checkout.requested_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
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

    _inner_class_types = {"fulfillment_details": FulfillmentDetails}
