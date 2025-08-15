# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.reporting._report import Report
from typing import cast
from typing_extensions import TypedDict


class ReportService(StripeService):
    class RetrieveParams(TypedDict):
        pass

    def retrieve(
        self,
        id: str,
        params: "ReportService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Report:
        """
        Retrieves metadata about a specific `Report` template, including its name, description,
        and the parameters it accepts. It's useful for understanding the capabilities and
        requirements of a particular `Report` before requesting a `ReportRun`.
        """
        return cast(
            Report,
            self._request(
                "get",
                "/v2/reporting/reports/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "ReportService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Report:
        """
        Retrieves metadata about a specific `Report` template, including its name, description,
        and the parameters it accepts. It's useful for understanding the capabilities and
        requirements of a particular `Report` before requesting a `ReportRun`.
        """
        return cast(
            Report,
            await self._request_async(
                "get",
                "/v2/reporting/reports/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
