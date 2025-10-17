# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account_notice import AccountNotice
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._account_notice_list_params import (
        AccountNoticeListParams,
    )
    from stripe.params._account_notice_retrieve_params import (
        AccountNoticeRetrieveParams,
    )
    from stripe.params._account_notice_update_params import (
        AccountNoticeUpdateParams,
    )


class AccountNoticeService(StripeService):
    def list(
        self,
        params: Optional["AccountNoticeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountNotice]":
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            "ListObject[AccountNotice]",
            self._request(
                "get",
                "/v1/account_notices",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["AccountNoticeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountNotice]":
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            "ListObject[AccountNotice]",
            await self._request_async(
                "get",
                "/v1/account_notices",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        account_notice: str,
        params: Optional["AccountNoticeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountNotice":
        """
        Retrieves an AccountNotice object.
        """
        return cast(
            "AccountNotice",
            self._request(
                "get",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_notice: str,
        params: Optional["AccountNoticeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountNotice":
        """
        Retrieves an AccountNotice object.
        """
        return cast(
            "AccountNotice",
            await self._request_async(
                "get",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        account_notice: str,
        params: "AccountNoticeUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountNotice":
        """
        Updates an AccountNotice object.
        """
        return cast(
            "AccountNotice",
            self._request(
                "post",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        account_notice: str,
        params: "AccountNoticeUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountNotice":
        """
        Updates an AccountNotice object.
        """
        return cast(
            "AccountNotice",
            await self._request_async(
                "post",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
