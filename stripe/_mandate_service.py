# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._mandate import Mandate
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, Optional, cast
from typing_extensions import NotRequired, TypedDict


class MandateService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        mandate: str,
        params: "MandateService.RetrieveParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Mandate:
        """
        Retrieves a Mandate object.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Mandate,
            self._request(
                "get",
                "/v1/mandates/{mandate}".format(mandate=sanitize_id(mandate)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        mandate: str,
        params: "MandateService.RetrieveParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Mandate:
        """
        Retrieves a Mandate object.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Mandate,
            await self._request_async(
                "get",
                "/v1/mandates/{mandate}".format(mandate=sanitize_id(mandate)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
