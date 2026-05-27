# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.iam._activity_log_list_params import (
        ActivityLogListParams,
    )
    from stripe.params.v2.iam._activity_log_retrieve_params import (
        ActivityLogRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.iam._activity_log import ActivityLog


class ActivityLogService(StripeService):
    def list(
        self,
        params: Optional["ActivityLogListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ActivityLog]":
        """
        List activity logs of an account.
        """
        return cast(
            "ListObject[ActivityLog]",
            self._request(
                "get",
                "/v2/iam/activity_logs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ActivityLogListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ActivityLog]":
        """
        List activity logs of an account.
        """
        return cast(
            "ListObject[ActivityLog]",
            await self._request_async(
                "get",
                "/v2/iam/activity_logs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ActivityLogRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ActivityLog":
        """
        Retrieve an activity log.
        """
        return cast(
            "ActivityLog",
            self._request(
                "get",
                "/v2/iam/activity_logs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ActivityLogRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ActivityLog":
        """
        Retrieve an activity log.
        """
        return cast(
            "ActivityLog",
            await self._request_async(
                "get",
                "/v2/iam/activity_logs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
