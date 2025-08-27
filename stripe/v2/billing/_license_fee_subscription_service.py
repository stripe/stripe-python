# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2.billing._license_fee_subscription import LicenseFeeSubscription
from typing import cast
from typing_extensions import TypedDict


class LicenseFeeSubscriptionService(StripeService):
    class RetrieveParams(TypedDict):
        pass

    def retrieve(
        self,
        id: str,
        params: "LicenseFeeSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFeeSubscription:
        """
        Retrieve a License Fee Subscription object.
        """
        return cast(
            LicenseFeeSubscription,
            self._request(
                "get",
                "/v2/billing/license_fee_subscriptions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "LicenseFeeSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFeeSubscription:
        """
        Retrieve a License Fee Subscription object.
        """
        return cast(
            LicenseFeeSubscription,
            await self._request_async(
                "get",
                "/v2/billing/license_fee_subscriptions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
