# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.billing._credit_grant import CreditGrant
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CreditGrantService(StripeService):
    class CreateParams(TypedDict):
        amount: "CreditGrantService.CreateParamsAmount"
        """
        Amount of this credit grant.
        """
        applicability_config: (
            "CreditGrantService.CreateParamsApplicabilityConfig"
        )
        """
        Configuration specifying what this credit grant applies to.
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
        The time when the billing credits become effective—when they're eligible for use. Defaults to the current timestamp if not specified.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        expires_at: NotRequired[int]
        """
        The time when the billing credits will expire. If not specified, the billing credits don't expire.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object (for example, cost basis) in a structured format.
        """
        name: NotRequired[str]
        """
        A descriptive name shown in the Dashboard.
        """

    class CreateParamsAmount(TypedDict):
        monetary: NotRequired["CreditGrantService.CreateParamsAmountMonetary"]
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
        scope: "CreditGrantService.CreateParamsApplicabilityConfigScope"
        """
        Specify the scope of this applicability config.
        """

    class CreateParamsApplicabilityConfigScope(TypedDict):
        price_type: Literal["metered"]
        """
        The price type for which credit grants can apply. We currently only support the `metered` price type.
        """

    class ExpireParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(TypedDict):
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

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
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
        Set of key-value pairs you can attach to an object. This can be useful for storing additional information about the object (for example, cost basis) in a structured format.
        """

    class VoidGrantParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "CreditGrantService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CreditGrant]:
        """
        Retrieve a list of credit grants.
        """
        return cast(
            ListObject[CreditGrant],
            self._request(
                "get",
                "/v1/billing/credit_grants",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CreditGrantService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CreditGrant]:
        """
        Retrieve a list of credit grants.
        """
        return cast(
            ListObject[CreditGrant],
            await self._request_async(
                "get",
                "/v1/billing/credit_grants",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CreditGrantService.CreateParams",
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Creates a credit grant
        """
        return cast(
            CreditGrant,
            self._request(
                "post",
                "/v1/billing/credit_grants",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CreditGrantService.CreateParams",
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Creates a credit grant
        """
        return cast(
            CreditGrant,
            await self._request_async(
                "post",
                "/v1/billing/credit_grants",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CreditGrantService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Retrieves a credit grant
        """
        return cast(
            CreditGrant,
            self._request(
                "get",
                "/v1/billing/credit_grants/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "CreditGrantService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Retrieves a credit grant
        """
        return cast(
            CreditGrant,
            await self._request_async(
                "get",
                "/v1/billing/credit_grants/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "CreditGrantService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Updates a credit grant
        """
        return cast(
            CreditGrant,
            self._request(
                "post",
                "/v1/billing/credit_grants/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "CreditGrantService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Updates a credit grant
        """
        return cast(
            CreditGrant,
            await self._request_async(
                "post",
                "/v1/billing/credit_grants/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def expire(
        self,
        id: str,
        params: "CreditGrantService.ExpireParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Expires a credit grant.
        """
        return cast(
            CreditGrant,
            self._request(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def expire_async(
        self,
        id: str,
        params: "CreditGrantService.ExpireParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Expires a credit grant.
        """
        return cast(
            CreditGrant,
            await self._request_async(
                "post",
                "/v1/billing/credit_grants/{id}/expire".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def void_grant(
        self,
        id: str,
        params: "CreditGrantService.VoidGrantParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Voids a credit grant.
        """
        return cast(
            CreditGrant,
            self._request(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def void_grant_async(
        self,
        id: str,
        params: "CreditGrantService.VoidGrantParams" = {},
        options: RequestOptions = {},
    ) -> CreditGrant:
        """
        Voids a credit grant.
        """
        return cast(
            CreditGrant,
            await self._request_async(
                "post",
                "/v1/billing/credit_grants/{id}/void".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
