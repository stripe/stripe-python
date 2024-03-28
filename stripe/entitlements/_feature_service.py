# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.entitlements._feature import Feature
from typing import Dict, List, cast
from typing_extensions import NotRequired, TypedDict


class FeatureService(StripeService):
    class CreateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        lookup_key: str
        """
        A unique key you provide as your own system identifier. This may be up to 80 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        name: str
        """
        The feature's name, for your own purpose, not meant to be displayable to the customer.
        """

    class ListParams(TypedDict):
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

    def list(
        self,
        params: "FeatureService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Feature]:
        """
        Retrieve a list of features
        """
        return cast(
            ListObject[Feature],
            self._request(
                "get",
                "/v1/entitlements/features",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "FeatureService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Feature]:
        """
        Retrieve a list of features
        """
        return cast(
            ListObject[Feature],
            await self._request_async(
                "get",
                "/v1/entitlements/features",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FeatureService.CreateParams",
        options: RequestOptions = {},
    ) -> Feature:
        """
        Creates a feature
        """
        return cast(
            Feature,
            self._request(
                "post",
                "/v1/entitlements/features",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FeatureService.CreateParams",
        options: RequestOptions = {},
    ) -> Feature:
        """
        Creates a feature
        """
        return cast(
            Feature,
            await self._request_async(
                "post",
                "/v1/entitlements/features",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
