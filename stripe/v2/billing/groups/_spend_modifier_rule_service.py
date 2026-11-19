# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.groups._spend_modifier_rule_list_params import (
        SpendModifierRuleListParams,
    )
    from stripe.params.v2.billing.groups._spend_modifier_rule_retrieve_params import (
        SpendModifierRuleRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._group_spend_modifier import GroupSpendModifier


class SpendModifierRuleService(StripeService):
    def list(
        self,
        group_id: str,
        /,
        params: Optional["SpendModifierRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[GroupSpendModifier]":
        """
        List spend modifiers associated with a billing group.
        """
        return cast(
            "ListObject[GroupSpendModifier]",
            self._request(
                "get",
                "/v2/billing/groups/{group_id}/spend_modifier_rules".format(
                    group_id=sanitize_id(group_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        group_id: str,
        /,
        params: Optional["SpendModifierRuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[GroupSpendModifier]":
        """
        List spend modifiers associated with a billing group.
        """
        return cast(
            "ListObject[GroupSpendModifier]",
            await self._request_async(
                "get",
                "/v2/billing/groups/{group_id}/spend_modifier_rules".format(
                    group_id=sanitize_id(group_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        group_id: str,
        id: str,
        /,
        params: Optional["SpendModifierRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GroupSpendModifier":
        """
        Retrieve a spend modifier associated with a billing group.
        """
        return cast(
            "GroupSpendModifier",
            self._request(
                "get",
                "/v2/billing/groups/{group_id}/spend_modifier_rules/{id}".format(
                    group_id=sanitize_id(group_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        group_id: str,
        id: str,
        /,
        params: Optional["SpendModifierRuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GroupSpendModifier":
        """
        Retrieve a spend modifier associated with a billing group.
        """
        return cast(
            "GroupSpendModifier",
            await self._request_async(
                "get",
                "/v2/billing/groups/{group_id}/spend_modifier_rules/{id}".format(
                    group_id=sanitize_id(group_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
