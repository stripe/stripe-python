# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._reward_program_activate_params import (
        RewardProgramActivateParams,
    )
    from stripe.params.v2.money_management._reward_program_create_params import (
        RewardProgramCreateParams,
    )
    from stripe.params.v2.money_management._reward_program_deactivate_params import (
        RewardProgramDeactivateParams,
    )
    from stripe.params.v2.money_management._reward_program_list_params import (
        RewardProgramListParams,
    )
    from stripe.params.v2.money_management._reward_program_retrieve_params import (
        RewardProgramRetrieveParams,
    )
    from stripe.params.v2.money_management._reward_program_update_params import (
        RewardProgramUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._reward_program import RewardProgram
    from stripe.v2.money_management.reward_programs._rule_service import (
        RuleService,
    )

_subservices = {
    "rules": [
        "stripe.v2.money_management.reward_programs._rule_service",
        "RuleService",
    ],
}


class RewardProgramService(StripeService):
    rules: "RuleService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["RewardProgramListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgram]":
        """
        Returns a list of RewardPrograms.
        """
        return cast(
            "ListObject[RewardProgram]",
            self._request(
                "get",
                "/v2/money_management/reward_programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RewardProgramListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgram]":
        """
        Returns a list of RewardPrograms.
        """
        return cast(
            "ListObject[RewardProgram]",
            await self._request_async(
                "get",
                "/v2/money_management/reward_programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RewardProgramCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Creates a new RewardProgram. RewardPrograms are inactive by default on creation; use
        ActivateRewardProgram to make them eligible for reward evaluation.
        """
        return cast(
            "RewardProgram",
            self._request(
                "post",
                "/v2/money_management/reward_programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RewardProgramCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Creates a new RewardProgram. RewardPrograms are inactive by default on creation; use
        ActivateRewardProgram to make them eligible for reward evaluation.
        """
        return cast(
            "RewardProgram",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["RewardProgramRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Retrieves the details of an existing RewardProgram.
        """
        return cast(
            "RewardProgram",
            self._request(
                "get",
                "/v2/money_management/reward_programs/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["RewardProgramRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Retrieves the details of an existing RewardProgram.
        """
        return cast(
            "RewardProgram",
            await self._request_async(
                "get",
                "/v2/money_management/reward_programs/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["RewardProgramUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Updates the mutable fields of an existing RewardProgram. Use ActivateRewardProgram /
        DeactivateRewardProgram to change the RewardProgram's status.
        """
        return cast(
            "RewardProgram",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["RewardProgramUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Updates the mutable fields of an existing RewardProgram. Use ActivateRewardProgram /
        DeactivateRewardProgram to change the RewardProgram's status.
        """
        return cast(
            "RewardProgram",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def activate(
        self,
        id: str,
        /,
        params: Optional["RewardProgramActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Activates a RewardProgram, making it eligible for reward evaluation. Idempotent: calling this on a
        RewardProgram that is already active returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgram",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{id}/activate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def activate_async(
        self,
        id: str,
        /,
        params: Optional["RewardProgramActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Activates a RewardProgram, making it eligible for reward evaluation. Idempotent: calling this on a
        RewardProgram that is already active returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgram",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{id}/activate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def deactivate(
        self,
        id: str,
        /,
        params: Optional["RewardProgramDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Deactivates a RewardProgram. Idempotent: calling this on a RewardProgram that is already inactive
        returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgram",
            self._request(
                "post",
                "/v2/money_management/reward_programs/{id}/deactivate".format(
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
        /,
        params: Optional["RewardProgramDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgram":
        """
        Deactivates a RewardProgram. Idempotent: calling this on a RewardProgram that is already inactive
        returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgram",
            await self._request_async(
                "post",
                "/v2/money_management/reward_programs/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
