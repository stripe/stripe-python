# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._approval_request_cancel_params import (
        ApprovalRequestCancelParams,
    )
    from stripe.params.v2.core._approval_request_execute_params import (
        ApprovalRequestExecuteParams,
    )
    from stripe.params.v2.core._approval_request_list_params import (
        ApprovalRequestListParams,
    )
    from stripe.params.v2.core._approval_request_retrieve_params import (
        ApprovalRequestRetrieveParams,
    )
    from stripe.params.v2.core._approval_request_submit_params import (
        ApprovalRequestSubmitParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core._approval_request import ApprovalRequest


class ApprovalRequestService(StripeService):
    def list(
        self,
        params: Optional["ApprovalRequestListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ApprovalRequest]":
        """
        GET /v2/core/approval_requests
        Lists approval requests with optional filtering.
        """
        return cast(
            "ListObject[ApprovalRequest]",
            self._request(
                "get",
                "/v2/core/approval_requests",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ApprovalRequestListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ApprovalRequest]":
        """
        GET /v2/core/approval_requests
        Lists approval requests with optional filtering.
        """
        return cast(
            "ListObject[ApprovalRequest]",
            await self._request_async(
                "get",
                "/v2/core/approval_requests",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ApprovalRequestRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        GET /v2/core/approval_requests/:id
        Retrieves an approval request by ID.
        """
        return cast(
            "ApprovalRequest",
            self._request(
                "get",
                "/v2/core/approval_requests/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ApprovalRequestRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        GET /v2/core/approval_requests/:id
        Retrieves an approval request by ID.
        """
        return cast(
            "ApprovalRequest",
            await self._request_async(
                "get",
                "/v2/core/approval_requests/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["ApprovalRequestCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/cancel
        Cancels a pending approval request.
        """
        return cast(
            "ApprovalRequest",
            self._request(
                "post",
                "/v2/core/approval_requests/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["ApprovalRequestCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/cancel
        Cancels a pending approval request.
        """
        return cast(
            "ApprovalRequest",
            await self._request_async(
                "post",
                "/v2/core/approval_requests/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def execute(
        self,
        id: str,
        params: Optional["ApprovalRequestExecuteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/execute
        Executes an approved approval request.
        """
        return cast(
            "ApprovalRequest",
            self._request(
                "post",
                "/v2/core/approval_requests/{id}/execute".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def execute_async(
        self,
        id: str,
        params: Optional["ApprovalRequestExecuteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/execute
        Executes an approved approval request.
        """
        return cast(
            "ApprovalRequest",
            await self._request_async(
                "post",
                "/v2/core/approval_requests/{id}/execute".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit(
        self,
        id: str,
        params: Optional["ApprovalRequestSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/submit
        Moves a pending approval request into the reviewer queue for auto-execution upon approval.
        """
        return cast(
            "ApprovalRequest",
            self._request(
                "post",
                "/v2/core/approval_requests/{id}/submit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_async(
        self,
        id: str,
        params: Optional["ApprovalRequestSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApprovalRequest":
        """
        POST /v2/core/approval_requests/:id/submit
        Moves a pending approval request into the reviewer queue for auto-execution upon approval.
        """
        return cast(
            "ApprovalRequest",
            await self._request_async(
                "post",
                "/v2/core/approval_requests/{id}/submit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
