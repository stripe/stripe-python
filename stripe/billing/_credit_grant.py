# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._customer import Customer
    from stripe.test_helpers._test_clock import TestClock


class CreditGrant(
    CreateableAPIResource["CreditGrant"],
    ListableAPIResource["CreditGrant"],
    UpdateableAPIResource["CreditGrant"],
):
    """
    A credit grant is an API resource that documents the allocation of some billing credits to a customer.

    Related guide: [Billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits)
    """

    OBJECT_NAME: ClassVar[Literal["billing.credit_grant"]] = (
        "billing.credit_grant"
    )

    class Amount(StripeObject):
        class Monetary(StripeObject):
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: int
            """
            A positive integer representing the amount.
            """

        monetary: Optional[Monetary]
        """
        The monetary amount.
        """
        type: Literal["monetary"]
        """
        The type of this amount. We currently only support `monetary` billing credits.
        """
        _inner_class_types = {"monetary": Monetary}

    class ApplicabilityConfig(StripeObject):
        class Scope(StripeObject):
            class Price(StripeObject):
                id: Optional[str]
                """
                Unique identifier for the object.
                """

            price_type: Optional[Literal["metered"]]
            """
            The price type that credit grants can apply to. We currently only support the `metered` price type. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
            """
            prices: Optional[List[Price]]
            """
            The prices that credit grants can apply to. We currently only support `metered` prices. This refers to prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
            """
            _inner_class_types = {"prices": Price}

        scope: Scope
        _inner_class_types = {"scope": Scope}

    class CreateParams(RequestOptions):
        amount: "CreditGrant.CreateParamsAmount"
        """
        Amount of this credit grant.
        """
        applicability_config: "CreditGrant.CreateParamsApplicabilityConfig"
        """
        Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
        """
        category: Literal["paid", "promotional"]
        """
        The category of this credit grant.
        """
        customer: str
        """
        ID of the customer to receive the billing credits.
        """
        effective_at: NotRequired[int]
        """
        The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        The time when the billing credits expire. If not specified, the billing credits don't expire.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
        """
        name: NotRequired[str]
        """
        A descriptive name shown in the Dashboard.
        """
        priority: NotRequired[int]
        """
        The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100.
        """

    class CreateParamsAmount(TypedDict):
        monetary: NotRequired["CreditGrant.CreateParamsAmountMonetary"]
        """
        The monetary amount.
        """
        type: Literal["monetary"]
        """
        Specify the type of this amount. We currently only support `monetary` billing credits.
        """

    class CreateParamsAmountMonetary(TypedDict):
        currency: str
        """
        Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `value` parameter.
        """
        value: int
        """
        A positive integer representing the amount of the credit grant.
        """

    class CreateParamsApplicabilityConfig(TypedDict):
        scope: "CreditGrant.CreateParamsApplicabilityConfigScope"
        """
        Specify the scope of this applicability config.
        """

    class CreateParamsApplicabilityConfigScope(TypedDict):
        price_type: NotRequired[Literal["metered"]]
        """
        The price type that credit grants can apply to. We currently only support the `metered` price type.
        """
        prices: NotRequired[
            List["CreditGrant.CreateParamsApplicabilityConfigScopePrice"]
        ]
        """
        A list of prices that the credit grant can apply to. We currently only support the `metered` prices.
        """

    class CreateParamsApplicabilityConfigScopePrice(TypedDict):
        id: str
        """
        The price ID this credit grant should apply to.
        """

    class ExpireParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(RequestOptions):
        customer: NotRequired[str]
        """
        Only return credit grants for this customer.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired["Literal['']|int"]
        """
        The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class VoidGrantParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    amount: Amount
    applicability_config: ApplicabilityConfig
    category: Literal["paid", "promotional"]
    """
    The category of this credit grant. This is for tracking purposes and isn't displayed to the customer.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: ExpandableField["Customer"]
    """
    ID of the customer receiving the billing credits.
    """
    effective_at: Optional[int]
    """
    The time when the billing credits become effective-when they're eligible for use.
    """
    expires_at: Optional[int]
    """
    The time when the billing credits expire. If not present, the billing credits don't expire.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    A descriptive name shown in dashboard.
    """
    object: Literal["billing.credit_grant"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    priority: Optional[int]
    """
    The priority for applying this credit grant. The highest priority is 0 and the lowest is 100.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this credit grant belongs to.
    """
    updated: int
    """
    Time at which the object was last updated. Measured in seconds since the Unix epoch.
    """
    voided_at: Optional[int]
    """
    The time when this credit grant was voided. If not present, the credit grant hasn't been voided.
    """

    @classmethod
    def create(
        cls, **params: Unpack["CreditGrant.CreateParams"]
    ) -> "CreditGrant":
        """
        Creates a credit grant.
        """
        return cast(
            "CreditGrant",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["CreditGrant.CreateParams"]
    ) -> "CreditGrant":
        """
        Creates a credit grant.
        """
        return cast(
            "CreditGrant",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_expire(
        cls, id: str, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        return cast(
            "CreditGrant",
            cls._static_request(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def expire(
        id: str, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        ...

    @overload
    def expire(
        self, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        ...

    @class_method_variant("_cls_expire")
    def expire(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        return cast(
            "CreditGrant",
            self._request(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_expire_async(
        cls, id: str, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        return cast(
            "CreditGrant",
            await cls._static_request_async(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def expire_async(
        id: str, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        ...

    @overload
    async def expire_async(
        self, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        ...

    @class_method_variant("_cls_expire_async")
    async def expire_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditGrant.ExpireParams"]
    ) -> "CreditGrant":
        """
        Expires a credit grant.
        """
        return cast(
            "CreditGrant",
            await self._request_async(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["CreditGrant.ListParams"]
    ) -> ListObject["CreditGrant"]:
        """
        Retrieve a list of credit grants.
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
        cls, **params: Unpack["CreditGrant.ListParams"]
    ) -> ListObject["CreditGrant"]:
        """
        Retrieve a list of credit grants.
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
        cls, id: str, **params: Unpack["CreditGrant.ModifyParams"]
    ) -> "CreditGrant":
        """
        Updates a credit grant.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "CreditGrant",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["CreditGrant.ModifyParams"]
    ) -> "CreditGrant":
        """
        Updates a credit grant.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "CreditGrant",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["CreditGrant.RetrieveParams"]
    ) -> "CreditGrant":
        """
        Retrieves a credit grant.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["CreditGrant.RetrieveParams"]
    ) -> "CreditGrant":
        """
        Retrieves a credit grant.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_void_grant(
        cls, id: str, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        return cast(
            "CreditGrant",
            cls._static_request(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def void_grant(
        id: str, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        ...

    @overload
    def void_grant(
        self, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        ...

    @class_method_variant("_cls_void_grant")
    def void_grant(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        return cast(
            "CreditGrant",
            self._request(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_void_grant_async(
        cls, id: str, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        return cast(
            "CreditGrant",
            await cls._static_request_async(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def void_grant_async(
        id: str, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        ...

    @overload
    async def void_grant_async(
        self, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        ...

    @class_method_variant("_cls_void_grant_async")
    async def void_grant_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditGrant.VoidGrantParams"]
    ) -> "CreditGrant":
        """
        Voids a credit grant.
        """
        return cast(
            "CreditGrant",
            await self._request_async(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "amount": Amount,
        "applicability_config": ApplicabilityConfig,
    }
