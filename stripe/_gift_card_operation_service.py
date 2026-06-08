# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._gift_card_operation import GiftCardOperation
    from stripe._request_options import RequestOptions
    from stripe.params._gift_card_operation_retrieve_params import (
        GiftCardOperationRetrieveParams,
    )


class GiftCardOperationService(StripeService):
    def retrieve(
        self,
        id: str,
        params: Optional["GiftCardOperationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Retrieves a third-party gift card operation object.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "get",
                "/v1/gift_card_operations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["GiftCardOperationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Retrieves a third-party gift card operation object.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "get",
                "/v1/gift_card_operations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
