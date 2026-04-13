# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._workflow_run_list_params import (
        WorkflowRunListParams,
    )
    from stripe.params.v2.core._workflow_run_retrieve_params import (
        WorkflowRunRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core._workflow_run import WorkflowRun


class WorkflowRunService(StripeService):
    def list(
        self,
        params: "WorkflowRunListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[WorkflowRun]":
        """
        List all Workflow Runs.
        """
        return cast(
            "ListObject[WorkflowRun]",
            self._request(
                "get",
                "/v2/core/workflow_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "WorkflowRunListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[WorkflowRun]":
        """
        List all Workflow Runs.
        """
        return cast(
            "ListObject[WorkflowRun]",
            await self._request_async(
                "get",
                "/v2/core/workflow_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["WorkflowRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "WorkflowRun":
        """
        Retrieves the details of a Workflow Run by ID.
        """
        return cast(
            "WorkflowRun",
            self._request(
                "get",
                "/v2/core/workflow_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["WorkflowRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "WorkflowRun":
        """
        Retrieves the details of a Workflow Run by ID.
        """
        return cast(
            "WorkflowRun",
            await self._request_async(
                "get",
                "/v2/core/workflow_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
