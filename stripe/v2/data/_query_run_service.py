# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.data._query_run_create_params import (
        QueryRunCreateParams,
    )
    from stripe.params.v2.data._query_run_retrieve_params import (
        QueryRunRetrieveParams,
    )
    from stripe.v2.data._query_run import QueryRun


class QueryRunService(StripeService):
    def create(
        self,
        params: "QueryRunCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "QueryRun":
        """
        Submits a SQL query for execution against a dataset and returns a `QueryRun` object
        to track progress and retrieve results.
        """
        return cast(
            "QueryRun",
            self._request(
                "post",
                "/v2/data/query_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "QueryRunCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "QueryRun":
        """
        Submits a SQL query for execution against a dataset and returns a `QueryRun` object
        to track progress and retrieve results.
        """
        return cast(
            "QueryRun",
            await self._request_async(
                "post",
                "/v2/data/query_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["QueryRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "QueryRun":
        """
        Retrieves the status and results of a previously created `QueryRun`.
        """
        return cast(
            "QueryRun",
            self._request(
                "get",
                "/v2/data/query_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["QueryRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "QueryRun":
        """
        Retrieves the status and results of a previously created `QueryRun`.
        """
        return cast(
            "QueryRun",
            await self._request_async(
                "get",
                "/v2/data/query_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
