# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management.reward_programs._rule_activate_params import (
        RuleActivateParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_create_params import (
        RuleCreateParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_deactivate_params import (
        RuleDeactivateParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_list_params import (
        RuleListParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_retrieve_params import (
        RuleRetrieveParams,
    )
    from stripe.params.v2.money_management.reward_programs._rule_update_params import (
        RuleUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._reward_program_rule import (
        RewardProgramRule,
    )


class RuleService(StripeService):
    def list(
        self,
        reward_program_id: str,
        /,
        params: Optional["RuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgramRule]":
        """
        Returns a list of RewardProgramRules for a RewardProgram.
        """
        return cast(
            "ListObject[RewardProgramRule]",
            self._request(
                "get",
                "/v2/money_management/reward_programs/{reward_program_id}/rules".format(
                    reward_program_id=sanitize_id(reward_program_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        reward_program_id: str,
        /,
        params: Optional["RuleListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgramRule]":
        """
        Returns a list of RewardProgramRules for a RewardProgram.
        """
        return cast(
            "ListObject[RewardProgramRule]",
            await self._request_async(
                "get",
                "/v2/money_management/reward_programs/{reward_program_id}/rules".format(
                    reward_program_id=sanitize_id(reward_program_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        reward_program_id: str,
        /,
        params: "RuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Creates a new RewardProgramRule under the given RewardProgram. RewardProgramRules are inactive by
        default on creation; use ActivateRewardProgramRule to make them eligible for reward evaluation.
        """
        return cast(
            "RewardProgramRule",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules".format(
                    reward_program_id=sanitize_id(reward_program_id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"reward": {"cashback": {"rate": "decimal_string"}}},
                ),
                options=options,
            ),
        )

    async def create_async(
        self,
        reward_program_id: str,
        /,
        params: "RuleCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Creates a new RewardProgramRule under the given RewardProgram. RewardProgramRules are inactive by
        default on creation; use ActivateRewardProgramRule to make them eligible for reward evaluation.
        """
        return cast(
            "RewardProgramRule",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules".format(
                    reward_program_id=sanitize_id(reward_program_id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"reward": {"cashback": {"rate": "decimal_string"}}},
                ),
                options=options,
            ),
        )

    def retrieve(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Retrieves the details of an existing RewardProgramRule.
        """
        return cast(
            "RewardProgramRule",
            self._request(
                "get",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Retrieves the details of an existing RewardProgramRule.
        """
        return cast(
            "RewardProgramRule",
            await self._request_async(
                "get",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Updates the mutable fields of an existing RewardProgramRule. Use ActivateRewardProgramRule /
        DeactivateRewardProgramRule to change the RewardProgramRule's status.
        """
        return cast(
            "RewardProgramRule",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"reward": {"cashback": {"rate": "decimal_string"}}},
                ),
                options=options,
            ),
        )

    async def update_async(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Updates the mutable fields of an existing RewardProgramRule. Use ActivateRewardProgramRule /
        DeactivateRewardProgramRule to change the RewardProgramRule's status.
        """
        return cast(
            "RewardProgramRule",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"reward": {"cashback": {"rate": "decimal_string"}}},
                ),
                options=options,
            ),
        )

    def activate(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Activates a RewardProgramRule. At most one RewardProgramRule may be active per RewardProgram at a
        time. Idempotent: calling this on a RewardProgramRule that is already active returns 200 with the
        current object unchanged.
        """
        return cast(
            "RewardProgramRule",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}/activate".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def activate_async(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Activates a RewardProgramRule. At most one RewardProgramRule may be active per RewardProgram at a
        time. Idempotent: calling this on a RewardProgramRule that is already active returns 200 with the
        current object unchanged.
        """
        return cast(
            "RewardProgramRule",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}/activate".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def deactivate(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Deactivates a RewardProgramRule. Idempotent: calling this on a RewardProgramRule that is already
        inactive returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramRule",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}/deactivate".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def deactivate_async(
        self,
        reward_program_id: str,
        id: str,
        /,
        params: Optional["RuleDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramRule":
        """
        Deactivates a RewardProgramRule. Idempotent: calling this on a RewardProgramRule that is already
        inactive returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramRule",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{reward_program_id}/rules/{id}/deactivate".format(
                    reward_program_id=sanitize_id(reward_program_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
