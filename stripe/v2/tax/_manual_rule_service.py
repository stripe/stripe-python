# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.tax._manual_rule_create_params import (
        ManualRuleCreateParams,
    )
    from stripe.params.v2.tax._manual_rule_deactivate_params import (
        ManualRuleDeactivateParams,
    )
    from stripe.params.v2.tax._manual_rule_list_params import (
        ManualRuleListParams,
    )
    from stripe.params.v2.tax._manual_rule_retrieve_params import (
        ManualRuleRetrieveParams,
    )
    from stripe.params.v2.tax._manual_rule_update_params import (
        ManualRuleUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.tax._manual_rule import ManualRule


class ManualRuleService(StripeService):
    def list(
        self,
        params: Optional["ManualRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ManualRule]":
        """
        List all ManualRule objects.
        """
        return cast(
            "ListObject[ManualRule]",
            self._request(
                "get",
                "/v2/tax/manual_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ManualRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ManualRule]":
        """
        List all ManualRule objects.
        """
        return cast(
            "ListObject[ManualRule]",
            await self._request_async(
                "get",
                "/v2/tax/manual_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ManualRuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Creates a ManualRule object.
        """
        return cast(
            "ManualRule",
            self._request(
                "post",
                "/v2/tax/manual_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ManualRuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Creates a ManualRule object.
        """
        return cast(
            "ManualRule",
            await self._request_async(
                "post",
                "/v2/tax/manual_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ManualRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Retrieves a ManualRule object by ID.
        """
        return cast(
            "ManualRule",
            self._request(
                "get",
                "/v2/tax/manual_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ManualRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Retrieves a ManualRule object by ID.
        """
        return cast(
            "ManualRule",
            await self._request_async(
                "get",
                "/v2/tax/manual_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "ManualRuleUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Updates the Tax configuration for a ManualRule object.
        """
        return cast(
            "ManualRule",
            self._request(
                "post",
                "/v2/tax/manual_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "ManualRuleUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Updates the Tax configuration for a ManualRule object.
        """
        return cast(
            "ManualRule",
            await self._request_async(
                "post",
                "/v2/tax/manual_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def deactivate(
        self,
        id: str,
        params: Optional["ManualRuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Deactivates a ManualRule object.
        """
        return cast(
            "ManualRule",
            self._request(
                "post",
                "/v2/tax/manual_rules/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def deactivate_async(
        self,
        id: str,
        params: Optional["ManualRuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ManualRule":
        """
        Deactivates a ManualRule object.
        """
        return cast(
            "ManualRule",
            await self._request_async(
                "post",
                "/v2/tax/manual_rules/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
