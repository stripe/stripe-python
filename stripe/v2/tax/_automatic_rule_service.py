# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.tax._automatic_rule_create_params import (
        AutomaticRuleCreateParams,
    )
    from stripe.params.v2.tax._automatic_rule_deactivate_params import (
        AutomaticRuleDeactivateParams,
    )
    from stripe.params.v2.tax._automatic_rule_find_params import (
        AutomaticRuleFindParams,
    )
    from stripe.params.v2.tax._automatic_rule_retrieve_params import (
        AutomaticRuleRetrieveParams,
    )
    from stripe.params.v2.tax._automatic_rule_update_params import (
        AutomaticRuleUpdateParams,
    )
    from stripe.v2.tax._automatic_rule import AutomaticRule


class AutomaticRuleService(StripeService):
    def create(
        self,
        params: "AutomaticRuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Creates an AutomaticRule object.
        """
        return cast(
            "AutomaticRule",
            self._request(
                "post",
                "/v2/tax/automatic_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AutomaticRuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Creates an AutomaticRule object.
        """
        return cast(
            "AutomaticRule",
            await self._request_async(
                "post",
                "/v2/tax/automatic_rules",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def find(
        self,
        params: "AutomaticRuleFindParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Finds an AutomaticRule object by BillableItem ID.
        """
        return cast(
            "AutomaticRule",
            self._request(
                "get",
                "/v2/tax/automatic_rules/find",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def find_async(
        self,
        params: "AutomaticRuleFindParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Finds an AutomaticRule object by BillableItem ID.
        """
        return cast(
            "AutomaticRule",
            await self._request_async(
                "get",
                "/v2/tax/automatic_rules/find",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AutomaticRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Retrieves an AutomaticRule object by ID.
        """
        return cast(
            "AutomaticRule",
            self._request(
                "get",
                "/v2/tax/automatic_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AutomaticRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Retrieves an AutomaticRule object by ID.
        """
        return cast(
            "AutomaticRule",
            await self._request_async(
                "get",
                "/v2/tax/automatic_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "AutomaticRuleUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Updates the automatic Tax configuration for an AutomaticRule object.
        """
        return cast(
            "AutomaticRule",
            self._request(
                "post",
                "/v2/tax/automatic_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "AutomaticRuleUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Updates the automatic Tax configuration for an AutomaticRule object.
        """
        return cast(
            "AutomaticRule",
            await self._request_async(
                "post",
                "/v2/tax/automatic_rules/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def deactivate(
        self,
        id: str,
        params: Optional["AutomaticRuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Deactivates an AutomaticRule object. Deactivated AutomaticRule objects are ignored in future tax calculations.
        """
        return cast(
            "AutomaticRule",
            self._request(
                "post",
                "/v2/tax/automatic_rules/{id}/deactivate".format(
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
        params: Optional["AutomaticRuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AutomaticRule":
        """
        Deactivates an AutomaticRule object. Deactivated AutomaticRule objects are ignored in future tax calculations.
        """
        return cast(
            "AutomaticRule",
            await self._request_async(
                "post",
                "/v2/tax/automatic_rules/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
