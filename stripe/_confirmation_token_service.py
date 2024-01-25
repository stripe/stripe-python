# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._confirmation_token import ConfirmationToken
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class ConfirmationTokenService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        confirmation_token: str,
        params: "ConfirmationTokenService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ConfirmationToken:
        """
        Retrieves an existing ConfirmationToken object
        """
        return cast(
            ConfirmationToken,
            self._requestor.request(
                "get",
                "/v1/confirmation_tokens/{confirmation_token}".format(
                    confirmation_token=_util.sanitize_id(confirmation_token),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
