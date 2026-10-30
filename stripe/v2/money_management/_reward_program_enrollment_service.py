# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._reward_program_enrollment_activate_params import (
        RewardProgramEnrollmentActivateParams,
    )
    from stripe.params.v2.money_management._reward_program_enrollment_create_params import (
        RewardProgramEnrollmentCreateParams,
    )
    from stripe.params.v2.money_management._reward_program_enrollment_deactivate_params import (
        RewardProgramEnrollmentDeactivateParams,
    )
    from stripe.params.v2.money_management._reward_program_enrollment_list_params import (
        RewardProgramEnrollmentListParams,
    )
    from stripe.params.v2.money_management._reward_program_enrollment_retrieve_params import (
        RewardProgramEnrollmentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._reward_program_enrollment import (
        RewardProgramEnrollment,
    )


class RewardProgramEnrollmentService(StripeService):
    def list(
        self,
        params: Optional["RewardProgramEnrollmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgramEnrollment]":
        """
        Returns a list of RewardProgramEnrollments. Omitting `reward_program` returns platform-wide
        enrollments across all RewardPrograms.
        """
        return cast(
            "ListObject[RewardProgramEnrollment]",
            self._request(
                "get",
                "/v2/money_management/reward_program_enrollments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RewardProgramEnrollmentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RewardProgramEnrollment]":
        """
        Returns a list of RewardProgramEnrollments. Omitting `reward_program` returns platform-wide
        enrollments across all RewardPrograms.
        """
        return cast(
            "ListObject[RewardProgramEnrollment]",
            await self._request_async(
                "get",
                "/v2/money_management/reward_program_enrollments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RewardProgramEnrollmentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Creates a new RewardProgramEnrollment, binding a connected account / Issuer Program to a
        RewardProgram. RewardProgramEnrollments are active by default on creation.
        """
        return cast(
            "RewardProgramEnrollment",
            self._request(
                "post",
                "/v2/money_management/reward_program_enrollments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RewardProgramEnrollmentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Creates a new RewardProgramEnrollment, binding a connected account / Issuer Program to a
        RewardProgram. RewardProgramEnrollments are active by default on creation.
        """
        return cast(
            "RewardProgramEnrollment",
            await self._request_async(
                "post",
                "/v2/money_management/reward_program_enrollments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["RewardProgramEnrollmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Retrieves the details of an existing RewardProgramEnrollment.
        """
        return cast(
            "RewardProgramEnrollment",
            self._request(
                "get",
                "/v2/money_management/reward_program_enrollments/{id}".format(
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
        params: Optional["RewardProgramEnrollmentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Retrieves the details of an existing RewardProgramEnrollment.
        """
        return cast(
            "RewardProgramEnrollment",
            await self._request_async(
                "get",
                "/v2/money_management/reward_program_enrollments/{id}".format(
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
        params: Optional["RewardProgramEnrollmentActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Activates a RewardProgramEnrollment. At most one RewardProgramEnrollment may be active per Issuer
        Program globally, across all RewardPrograms. Idempotent: calling this on a RewardProgramEnrollment
        that is already active returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramEnrollment",
            self._request(
                "post",
                "/v2/money_management/reward_program_enrollments/{id}/activate".format(
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
        params: Optional["RewardProgramEnrollmentActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Activates a RewardProgramEnrollment. At most one RewardProgramEnrollment may be active per Issuer
        Program globally, across all RewardPrograms. Idempotent: calling this on a RewardProgramEnrollment
        that is already active returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramEnrollment",
            await self._request_async(
                "post",
                "/v2/money_management/reward_program_enrollments/{id}/activate".format(
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
        params: Optional["RewardProgramEnrollmentDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Deactivates a RewardProgramEnrollment. Idempotent: calling this on a RewardProgramEnrollment that is
        already inactive returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramEnrollment",
            self._request(
                "post",
                "/v2/money_management/reward_program_enrollments/{id}/deactivate".format(
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
        params: Optional["RewardProgramEnrollmentDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RewardProgramEnrollment":
        """
        Deactivates a RewardProgramEnrollment. Idempotent: calling this on a RewardProgramEnrollment that is
        already inactive returns 200 with the current object unchanged.
        """
        return cast(
            "RewardProgramEnrollment",
            await self._request_async(
                "post",
                "/v2/money_management/reward_program_enrollments/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
