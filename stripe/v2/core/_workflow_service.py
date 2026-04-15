# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._workflow_invoke_params import (
        WorkflowInvokeParams,
    )
    from stripe.params.v2.core._workflow_list_params import WorkflowListParams
    from stripe.params.v2.core._workflow_retrieve_params import (
        WorkflowRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core._workflow import Workflow
    from stripe.v2.core._workflow_run import WorkflowRun


class WorkflowService(StripeService):
    def list(
        self,
        params: "WorkflowListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Workflow]":
        """
        List all Workflows.
        """
        return cast(
            "ListObject[Workflow]",
            self._request(
                "get",
                "/v2/core/workflows",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "WorkflowListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Workflow]":
        """
        List all Workflows.
        """
        return cast(
            "ListObject[Workflow]",
            await self._request_async(
                "get",
                "/v2/core/workflows",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["WorkflowRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Workflow":
        """
        Retrieves the details of a Workflow by ID.
        """
        return cast(
            "Workflow",
            self._request(
                "get",
                "/v2/core/workflows/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["WorkflowRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Workflow":
        """
        Retrieves the details of a Workflow by ID.
        """
        return cast(
            "Workflow",
            await self._request_async(
                "get",
                "/v2/core/workflows/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def invoke(
        self,
        id: str,
        params: "WorkflowInvokeParams",
        options: Optional["RequestOptions"] = None,
    ) -> "WorkflowRun":
        """
        Invokes an on-demand Workflow with parameters, to launch a new Workflow Run.
        """
        return cast(
            "WorkflowRun",
            self._request(
                "post",
                "/v2/core/workflows/{id}/invoke".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def invoke_async(
        self,
        id: str,
        params: "WorkflowInvokeParams",
        options: Optional["RequestOptions"] = None,
    ) -> "WorkflowRun":
        """
        Invokes an on-demand Workflow with parameters, to launch a new Workflow Run.
        """
        return cast(
            "WorkflowRun",
            await self._request_async(
                "post",
                "/v2/core/workflows/{id}/invoke".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
