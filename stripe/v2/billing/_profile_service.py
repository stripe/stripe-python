# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._profile import Profile
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ProfileService(StripeService):
    class CreateParams(TypedDict):
        customer: str
        """
        The ID of the customer object.
        """
        default_payment_method: NotRequired[str]
        """
        The ID of the payment method object.
        """
        display_name: NotRequired[str]
        """
        A customer-facing name for the billing profile.
        Maximum length of 250 characters.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular billing profile. It must be unique among billing profiles for a given customer.
        Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    class ListParams(TypedDict):
        customer: NotRequired[str]
        """
        Filter billing profiles by a customer. Mutually exclusive
        with `lookup_keys` and `default_payment_method`.
        """
        default_payment_method: NotRequired[str]
        """
        Filter billing profiles by a default payment method. Mutually exclusive
        with `customer` and `lookup_keys`.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 10.
        """
        lookup_keys: List[str]
        """
        Filter billing profiles by lookup keys. Mutually exclusive
        with `customer` and `default_payment_method`.
        You can specify up to 10 lookup_keys.
        """
        status: NotRequired[Literal["active", "inactive"]]
        """
        Filter billing profiles by status. Can be combined
        with all other filters. If not provided, all billing profiles will be returned.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        default_payment_method: NotRequired[str]
        """
        The ID of the payment method object.
        """
        display_name: NotRequired[Optional[str]]
        """
        A customer-facing name for the billing profile.
        Maximum length of 250 characters.
        To remove the display_name from the object, set it to null in the request.
        """
        lookup_key: NotRequired[Optional[str]]
        """
        An internal key you can use to search for a particular billing profile. It must be unique among billing profiles for a given customer.
        Maximum length of 200 characters.
        To remove the lookup_key from the object, set it to null in the request.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    def list(
        self, params: "ProfileService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Profile]:
        """
        List Billing Profiles.
        """
        return cast(
            ListObject[Profile],
            self._request(
                "get",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self, params: "ProfileService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Profile]:
        """
        List Billing Profiles.
        """
        return cast(
            ListObject[Profile],
            await self._request_async(
                "get",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ProfileService.CreateParams",
        options: RequestOptions = {},
    ) -> Profile:
        """
        Create a BillingProfile object.
        """
        return cast(
            Profile,
            self._request(
                "post",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ProfileService.CreateParams",
        options: RequestOptions = {},
    ) -> Profile:
        """
        Create a BillingProfile object.
        """
        return cast(
            Profile,
            await self._request_async(
                "post",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ProfileService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Profile:
        """
        Retrieve a BillingProfile object.
        """
        return cast(
            Profile,
            self._request(
                "get",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "ProfileService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Profile:
        """
        Retrieve a BillingProfile object.
        """
        return cast(
            Profile,
            await self._request_async(
                "get",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "ProfileService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Profile:
        """
        Update a BillingProfile object.
        """
        return cast(
            Profile,
            self._request(
                "post",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "ProfileService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Profile:
        """
        Update a BillingProfile object.
        """
        return cast(
            Profile,
            await self._request_async(
                "post",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
