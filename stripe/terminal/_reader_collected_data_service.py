# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.terminal._reader_collected_data import ReaderCollectedData
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class ReaderCollectedDataService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        reader_collected_data: str,
        params: "ReaderCollectedDataService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReaderCollectedData:
        """
        Retrieve data collected using Reader hardware.
        """
        return cast(
            ReaderCollectedData,
            self._request(
                "get",
                "/v1/terminal/reader_collected_data/{reader_collected_data}".format(
                    reader_collected_data=sanitize_id(reader_collected_data),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        reader_collected_data: str,
        params: "ReaderCollectedDataService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ReaderCollectedData:
        """
        Retrieve data collected using Reader hardware.
        """
        return cast(
            ReaderCollectedData,
            await self._request_async(
                "get",
                "/v1/terminal/reader_collected_data/{reader_collected_data}".format(
                    reader_collected_data=sanitize_id(reader_collected_data),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
