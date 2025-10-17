# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.terminal._reader_collected_data_retrieve_params import (
        ReaderCollectedDataRetrieveParams,
    )
    from stripe.terminal._reader_collected_data import ReaderCollectedData


class ReaderCollectedDataService(StripeService):
    def retrieve(
        self,
        reader_collected_data: str,
        params: Optional["ReaderCollectedDataRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReaderCollectedData":
        """
        Retrieve data collected using Reader hardware.
        """
        return cast(
            "ReaderCollectedData",
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
        params: Optional["ReaderCollectedDataRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReaderCollectedData":
        """
        Retrieve data collected using Reader hardware.
        """
        return cast(
            "ReaderCollectedData",
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
