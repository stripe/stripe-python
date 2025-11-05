# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.reporting._report_run_create_params import (
        ReportRunCreateParams,
    )
    from stripe.params.v2.reporting._report_run_retrieve_params import (
        ReportRunRetrieveParams,
    )
    from stripe.v2.reporting._report_run import ReportRun


class ReportRunService(StripeService):
    def create(
        self,
        params: "ReportRunCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ReportRun":
        """
        Initiates the generation of a `ReportRun` based on the specified report template
        and user-provided parameters. It's the starting point for obtaining report data,
        and returns a `ReportRun` object which can be used to track the progress and retrieve
        the results of the report.
        """
        return cast(
            "ReportRun",
            self._request(
                "post",
                "/v2/reporting/report_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ReportRunCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ReportRun":
        """
        Initiates the generation of a `ReportRun` based on the specified report template
        and user-provided parameters. It's the starting point for obtaining report data,
        and returns a `ReportRun` object which can be used to track the progress and retrieve
        the results of the report.
        """
        return cast(
            "ReportRun",
            await self._request_async(
                "post",
                "/v2/reporting/report_runs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ReportRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReportRun":
        """
        Fetches the current state and details of a previously created `ReportRun`. If the `ReportRun`
        has succeeded, the endpoint will provide details for how to retrieve the results.
        """
        return cast(
            "ReportRun",
            self._request(
                "get",
                "/v2/reporting/report_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ReportRunRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReportRun":
        """
        Fetches the current state and details of a previously created `ReportRun`. If the `ReportRun`
        has succeeded, the endpoint will provide details for how to retrieve the results.
        """
        return cast(
            "ReportRun",
            await self._request_async(
                "get",
                "/v2/reporting/report_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
