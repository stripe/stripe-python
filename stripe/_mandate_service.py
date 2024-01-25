# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._mandate import Mandate
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class MandateService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        mandate: str,
        params: "MandateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Mandate:
        """
        Retrieves a Mandate object.
        """
        return cast(
            Mandate,
            self._requestor.request(
                "get",
                "/v1/mandates/{mandate}".format(
                    mandate=_util.sanitize_id(mandate),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
