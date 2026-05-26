# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import json
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from uuid import uuid4
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._product_feature import ProductFeature
    from stripe._request_options import RequestOptions
    from stripe.params._product_feature_create_params import (
        ProductFeatureCreateParams,
    )
    from stripe.params._product_feature_delete_params import (
        ProductFeatureDeleteParams,
    )
    from stripe.params._product_feature_list_params import (
        ProductFeatureListParams,
    )
    from stripe.params._product_feature_retrieve_params import (
        ProductFeatureRetrieveParams,
    )


class ProductFeatureService(StripeService):
    def delete(
        self,
        product: str,
        id: str,
        params: Optional["ProductFeatureDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Deletes the feature attachment to a product
        """
        return cast(
            "ProductFeature",
            self._request(
                "delete",
                "/v1/products/{product}/features/{id}".format(
                    product=sanitize_id(product),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        product: str,
        id: str,
        params: Optional["ProductFeatureDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Deletes the feature attachment to a product
        """
        return cast(
            "ProductFeature",
            await self._request_async(
                "delete",
                "/v1/products/{product}/features/{id}".format(
                    product=sanitize_id(product),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        product: str,
        id: str,
        params: Optional["ProductFeatureRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Retrieves a product_feature, which represents a feature attachment to a product
        """
        return cast(
            "ProductFeature",
            self._request(
                "get",
                "/v1/products/{product}/features/{id}".format(
                    product=sanitize_id(product),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        product: str,
        id: str,
        params: Optional["ProductFeatureRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Retrieves a product_feature, which represents a feature attachment to a product
        """
        return cast(
            "ProductFeature",
            await self._request_async(
                "get",
                "/v1/products/{product}/features/{id}".format(
                    product=sanitize_id(product),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        product: str,
        params: Optional["ProductFeatureListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProductFeature]":
        """
        Retrieve a list of features for a product
        """
        return cast(
            "ListObject[ProductFeature]",
            self._request(
                "get",
                "/v1/products/{product}/features".format(
                    product=sanitize_id(product),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        product: str,
        params: Optional["ProductFeatureListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProductFeature]":
        """
        Retrieve a list of features for a product
        """
        return cast(
            "ListObject[ProductFeature]",
            await self._request_async(
                "get",
                "/v1/products/{product}/features".format(
                    product=sanitize_id(product),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        product: str,
        params: "ProductFeatureCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Creates a product_feature, which represents a feature attachment to a product
        """
        return cast(
            "ProductFeature",
            self._request(
                "post",
                "/v1/products/{product}/features".format(
                    product=sanitize_id(product),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        product: str,
        params: "ProductFeatureCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProductFeature":
        """
        Creates a product_feature, which represents a feature attachment to a product
        """
        return cast(
            "ProductFeature",
            await self._request_async(
                "post",
                "/v1/products/{product}/features".format(
                    product=sanitize_id(product),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_delete(
        self,
        product: str,
        id: str,
        params: Optional["ProductFeatureDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a ProductFeature delete request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        batch_request = {
            "id": item_id,
            "path_params": {"product": product, "id": id},
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            batch_request["context"] = context
        return json.dumps(batch_request)

    def serialize_batch_create(
        self,
        product: str,
        params: Optional["ProductFeatureCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a ProductFeature create request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        batch_request = {
            "id": item_id,
            "path_params": {"product": product},
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            batch_request["context"] = context
        return json.dumps(batch_request)
