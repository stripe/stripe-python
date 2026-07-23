# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.billing._alert_notification import AlertNotification
    from stripe.params.billing._alert_notification_list_params import (
        AlertNotificationListParams,
    )


class AlertNotificationService(StripeService):
    def list(
        self,
        id: str,
        params: "AlertNotificationListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AlertNotification]":
        """
        Lists sent billing alert triggered and recovered notifications for a billing alert.
        """
        return cast(
            "ListObject[AlertNotification]",
            self._request(
                "get",
                "/v1/billing/alerts/{id}/notifications".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        params: "AlertNotificationListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AlertNotification]":
        """
        Lists sent billing alert triggered and recovered notifications for a billing alert.
        """
        return cast(
            "ListObject[AlertNotification]",
            await self._request_async(
                "get",
                "/v1/billing/alerts/{id}/notifications".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
