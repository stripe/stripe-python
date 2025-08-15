# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.reporting._report_run import ReportRun
from typing import Dict, List, cast
from typing_extensions import NotRequired, TypedDict


class ReportRunService(StripeService):
    class CreateParams(TypedDict):
        report: str
        """
        The unique identifier of the `Report` being requested.
        """
        report_parameters: Dict[
            str, "ReportRunService.CreateParamsReportParameters"
        ]
        """
        A map of parameter names to values, specifying how the report should be customized.
        The accepted parameters depend on the specific `Report` being run.
        """
        result_options: NotRequired[
            "ReportRunService.CreateParamsResultOptions"
        ]
        """
        Optional settings to customize the results of the `ReportRun`.
        """

    class CreateParamsReportParameters(TypedDict):
        array_value: NotRequired[
            "ReportRunService.CreateParamsReportParametersArrayValue"
        ]
        """
        Parameter with an array data type.
        """
        string_value: NotRequired[str]
        """
        Parameter with a string data type.
        """
        timestamp_value: NotRequired[str]
        """
        Parameter with a timestamp data type.
        """

    class CreateParamsReportParametersArrayValue(TypedDict):
        items: List[str]
        """
        The list of string values in the array.
        """

    class CreateParamsResultOptions(TypedDict):
        compress_file: NotRequired[bool]
        """
        If set, the generated report file will be compressed into a ZIP folder.
        This is useful for reducing file size and download time for large reports.
        """

    class RetrieveParams(TypedDict):
        pass

    def create(
        self,
        params: "ReportRunService.CreateParams",
        options: RequestOptions = {},
    ) -> ReportRun:
        """
        Initiates the generation of a `ReportRun` based on the specified report template
        and user-provided parameters. It's the starting point for obtaining report data,
        and returns a `ReportRun` object which can be used to track the progress and retrieve
        the results of the report.
        """
        return cast(
            ReportRun,
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
        params: "ReportRunService.CreateParams",
        options: RequestOptions = {},
    ) -> ReportRun:
        """
        Initiates the generation of a `ReportRun` based on the specified report template
        and user-provided parameters. It's the starting point for obtaining report data,
        and returns a `ReportRun` object which can be used to track the progress and retrieve
        the results of the report.
        """
        return cast(
            ReportRun,
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
        params: "ReportRunService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReportRun:
        """
        Fetches the current state and details of a previously created `ReportRun`. If the `ReportRun`
        has succeeded, the endpoint will provide details for how to retrieve the results.
        """
        return cast(
            ReportRun,
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
        params: "ReportRunService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReportRun:
        """
        Fetches the current state and details of a previously created `ReportRun`. If the `ReportRun`
        has succeeded, the endpoint will provide details for how to retrieve the results.
        """
        return cast(
            ReportRun,
            await self._request_async(
                "get",
                "/v2/reporting/report_runs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
