# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.cadences._spend_modifier_rule_list_params import (
        SpendModifierRuleListParams,
    )
    from stripe.params.v2.billing.cadences._spend_modifier_rule_retrieve_params import (
        SpendModifierRuleRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._cadence_spend_modifier import CadenceSpendModifier


class SpendModifierRuleService(StripeService):
    def list(
        self,
        cadence_id: str,
        params: Optional["SpendModifierRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CadenceSpendModifier]":
        """
        List all Spend Modifiers associated with a Billing Cadence.
        """
        return cast(
            "ListObject[CadenceSpendModifier]",
            self._request(
                "get",
                "/v2/billing/cadences/{cadence_id}/spend_modifier_rules".format(
                    cadence_id=sanitize_id(cadence_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        cadence_id: str,
        params: Optional["SpendModifierRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CadenceSpendModifier]":
        """
        List all Spend Modifiers associated with a Billing Cadence.
        """
        return cast(
            "ListObject[CadenceSpendModifier]",
            await self._request_async(
                "get",
                "/v2/billing/cadences/{cadence_id}/spend_modifier_rules".format(
                    cadence_id=sanitize_id(cadence_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        cadence_id: str,
        id: str,
        params: Optional["SpendModifierRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CadenceSpendModifier":
        """
        Retrieve a Spend Modifier associated with a Billing Cadence.
        """
        return cast(
            "CadenceSpendModifier",
            self._request(
                "get",
                "/v2/billing/cadences/{cadence_id}/spend_modifier_rules/{id}".format(
                    cadence_id=sanitize_id(cadence_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        cadence_id: str,
        id: str,
        params: Optional["SpendModifierRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CadenceSpendModifier":
        """
        Retrieve a Spend Modifier associated with a Billing Cadence.
        """
        return cast(
            "CadenceSpendModifier",
            await self._request_async(
                "get",
                "/v2/billing/cadences/{cadence_id}/spend_modifier_rules/{id}".format(
                    cadence_id=sanitize_id(cadence_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
