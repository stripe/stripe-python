# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._login_link import LoginLink
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class AccountLoginLinkService(StripeService):
    class CreateParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def create(
        self,
        account: str,
        params: "AccountLoginLinkService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> LoginLink:
        """
        Creates a single-use login link for an Express account to access their Stripe dashboard.

        You may only create login links for [Express accounts](https://stripe.com/docs/connect/express-accounts) connected to your platform.
        """
        return cast(
            LoginLink,
            self._requestor.request(
                "post",
                "/v1/accounts/{account}/login_links".format(
                    account=_util.sanitize_id(account),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
