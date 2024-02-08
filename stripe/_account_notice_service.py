# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_notice import AccountNotice
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import NotRequired, TypedDict


class AccountNoticeService(StripeService):
    class ListParams(TypedDict):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        sent: NotRequired["bool"]
        """
        Set to false to only return unsent AccountNotices.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        email: "AccountNoticeService.UpdateParamsEmail"
        """
        Information about the email you sent.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        sent_at: int
        """
        Date when you sent the notice.
        """

    class UpdateParamsEmail(TypedDict):
        plain_text: str
        """
        Content of the email in plain text. The copy must match exactly the language that Stripe Compliance has approved for use.
        """
        recipient: str
        """
        Email address of the recipient.
        """
        subject: str
        """
        Subject of the email.
        """

    def list(
        self,
        params: "AccountNoticeService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[AccountNotice]:
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            ListObject[AccountNotice],
            self._request(
                "get",
                "/v1/account_notices",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "AccountNoticeService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[AccountNotice]:
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            ListObject[AccountNotice],
            await self._request_async(
                "get",
                "/v1/account_notices",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        account_notice: str,
        params: "AccountNoticeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> AccountNotice:
        """
        Retrieves an AccountNotice object.
        """
        return cast(
            AccountNotice,
            self._request(
                "get",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_notice: str,
        params: "AccountNoticeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> AccountNotice:
        """
        Retrieves an AccountNotice object.
        """
        return cast(
            AccountNotice,
            await self._request_async(
                "get",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        account_notice: str,
        params: "AccountNoticeService.UpdateParams",
        options: RequestOptions = {},
    ) -> AccountNotice:
        """
        Updates an AccountNotice object.
        """
        return cast(
            AccountNotice,
            self._request(
                "post",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        account_notice: str,
        params: "AccountNoticeService.UpdateParams",
        options: RequestOptions = {},
    ) -> AccountNotice:
        """
        Updates an AccountNotice object.
        """
        return cast(
            AccountNotice,
            await self._request_async(
                "post",
                "/v1/account_notices/{account_notice}".format(
                    account_notice=sanitize_id(account_notice),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
