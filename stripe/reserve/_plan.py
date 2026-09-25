# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.reserve._plan_list_params import PlanListParams
    from stripe.params.reserve._plan_retrieve_params import PlanRetrieveParams


class Plan(ListableAPIResource["Plan"]):
    """
    ReservePlans are used to automatically place holds on a merchant's funds until the plan expires. It takes a portion of each incoming Charge (including those resulting from a Transfer from a platform account).
    """

    OBJECT_NAME: ClassVar[Literal["reserve.plan"]] = "reserve.plan"

    class FixedRelease(StripeObject):
        release_after: int
        """
        The time after which all reserved funds are requested for release.
        """
        scheduled_release: int
        """
        The time at which reserved funds are scheduled for release, automatically set to midnight UTC of the day after `release_after`.
        """

    class ManualRelease(StripeObject):
        pass

    class RollingRelease(StripeObject):
        days_after_charge: int
        """
        The number of days to reserve funds before releasing.
        """
        expires_on: Optional[int]
        """
        The time at which the ReservePlan expires.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_by: Union[Literal["application", "stripe"], str]
    """
    Indicates which party created this ReservePlan.
    """
    currency: Optional[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). An unset currency indicates that the plan applies to all currencies.
    """
    destination: Literal["other", "risk_reserved", "settlement_reserved"]
    """
    The balance destination to which the reserved funds are sent.
    """
    disabled_at: Optional[int]
    """
    Time at which the ReservePlan was disabled.
    """
    fixed_release: Optional[FixedRelease]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    manual_release: Optional[ManualRelease]
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["reserve.plan"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    percent: int
    """
    The percent of each Charge to reserve.
    """
    rolling_release: Optional[RollingRelease]
    status: Literal["active", "disabled", "expired", "other"]
    """
    The current status of the ReservePlan. The ReservePlan only affects charges if it is `active`.
    """
    type: Literal[
        "fixed_release", "manual_release", "other", "rolling_release"
    ]
    """
    The type of the ReservePlan.
    """

    @classmethod
    def list(cls, **params: Unpack["PlanListParams"]) -> ListObject["Plan"]:
        """
        Returns a list of ReservePlans previously created. The ReservePlans are returned in sorted order, with the most recent ReservePlans appearing first.
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
        cls, **params: Unpack["PlanListParams"]
    ) -> ListObject["Plan"]:
        """
        Returns a list of ReservePlans previously created. The ReservePlans are returned in sorted order, with the most recent ReservePlans appearing first.
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
    def retrieve(
        cls, id: str, **params: Unpack["PlanRetrieveParams"]
    ) -> "Plan":
        """
        Retrieve a ReservePlan.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PlanRetrieveParams"]
    ) -> "Plan":
        """
        Retrieve a ReservePlan.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "fixed_release": FixedRelease,
        "manual_release": ManualRelease,
        "rolling_release": RollingRelease,
    }
