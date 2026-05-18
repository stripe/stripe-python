# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._payment_location_capability_list_params import (
        PaymentLocationCapabilityListParams,
    )
    from stripe.params._payment_location_capability_modify_params import (
        PaymentLocationCapabilityModifyParams,
    )
    from stripe.params._payment_location_capability_retrieve_params import (
        PaymentLocationCapabilityRetrieveParams,
    )


class PaymentLocationCapability(
    ListableAPIResource["PaymentLocationCapability"],
    UpdateableAPIResource["PaymentLocationCapability"],
):
    """
    A Payment Location Capability represents a capability for a Stripe account at a Payment Location.
    """

    OBJECT_NAME: ClassVar[Literal["payment_location_capability"]] = (
        "payment_location_capability"
    )

    class Requirements(StripeObject):
        class Error(StripeObject):
            code: Literal["information_missing", "invalid_value_other"]
            """
            The code for the type of error.
            """
            reason: str
            """
            An informative message that indicates the error type and provides additional details about the error.
            """
            requirement: str
            """
            The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.
            """

        currently_due: List[str]
        """
        Fields that need to be collected to keep the capability enabled.
        """
        disabled_reason: Optional[
            Literal[
                "account.capability_required",
                "pending.onboarding",
                "pending.review",
                "rejected.other",
                "rejected.unsupported_business",
                "requirements.fields_needed",
            ]
        ]
        """
        Description of why the capability is disabled.
        """
        errors: List[Error]
        """
        Fields that are `currently_due` and need to be collected again because validation or verification failed.
        """
        _inner_class_types = {"errors": Error}

    account: str
    """
    The account for which the capability enables functionality.
    """
    capability: Literal["fr_meal_vouchers_conecs_payments"]
    """
    The identifier for the capability.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    location: str
    """
    The payment location for which the capability enables functionality.
    """
    object: Literal["payment_location_capability"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requested: bool
    """
    Whether the capability has been requested.
    """
    requested_at: Optional[int]
    """
    Time at which the capability was requested. Measured in seconds since the Unix epoch.
    """
    requirements: Requirements
    status: Literal["active", "inactive", "pending", "unrequested"]
    """
    The status of the capability.
    """

    @classmethod
    def list(
        cls, **params: Unpack["PaymentLocationCapabilityListParams"]
    ) -> ListObject["PaymentLocationCapability"]:
        """
        Returns a list of PaymentLocationCapability objects associated with the location.
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
        cls, **params: Unpack["PaymentLocationCapabilityListParams"]
    ) -> ListObject["PaymentLocationCapability"]:
        """
        Returns a list of PaymentLocationCapability objects associated with the location.
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
        cls, id: str, **params: Unpack["PaymentLocationCapabilityModifyParams"]
    ) -> "PaymentLocationCapability":
        """
        Updates a specified Payment Location Capability. Request or remove a payment location capability by updating its requested parameter.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentLocationCapability",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["PaymentLocationCapabilityModifyParams"]
    ) -> "PaymentLocationCapability":
        """
        Updates a specified Payment Location Capability. Request or remove a payment location capability by updating its requested parameter.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentLocationCapability",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["PaymentLocationCapabilityRetrieveParams"],
    ) -> "PaymentLocationCapability":
        """
        Retrieves information about the specified Payment Location Capability.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["PaymentLocationCapabilityRetrieveParams"],
    ) -> "PaymentLocationCapability":
        """
        Retrieves information about the specified Payment Location Capability.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/payment_location_capabilities"

    _inner_class_types = {"requirements": Requirements}
