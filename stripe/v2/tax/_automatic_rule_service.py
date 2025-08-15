# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.tax._automatic_rule import AutomaticRule
from typing import cast
from typing_extensions import TypedDict


class AutomaticRuleService(StripeService):
    class CreateParams(TypedDict):
        billable_item: str
        """
        The BillableItem ID to set automatic Tax configuration for.
        """
        tax_code: str
        """
        The TaxCode object to be used for automatic tax calculations.
        """

    class DeactivateParams(TypedDict):
        pass

    class FindParams(TypedDict):
        billable_item: str
        """
        The BillableItem ID to search by.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        tax_code: str
        """
        The TaxCode object to be used for automatic tax calculations.
        """

    def create(
        self,
        params: "AutomaticRuleService.CreateParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Creates an AutomaticRule object.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.CreateParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Creates an AutomaticRule object.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.FindParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Finds an AutomaticRule object by BillableItem ID.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.FindParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Finds an AutomaticRule object by BillableItem ID.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Retrieves an AutomaticRule object by ID.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Retrieves an AutomaticRule object by ID.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.UpdateParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Updates the automatic Tax configuration for an AutomaticRule object.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.UpdateParams",
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Updates the automatic Tax configuration for an AutomaticRule object.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.DeactivateParams" = {},
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Deactivates an AutomaticRule object. Deactivated AutomaticRule objects are ignored in future tax calculations.
        """
        return cast(
            AutomaticRule,
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
        params: "AutomaticRuleService.DeactivateParams" = {},
        options: RequestOptions = {},
    ) -> AutomaticRule:
        """
        Deactivates an AutomaticRule object. Deactivated AutomaticRule objects are ignored in future tax calculations.
        """
        return cast(
            AutomaticRule,
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
