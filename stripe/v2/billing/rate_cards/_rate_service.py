# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.rate_cards._rate_create_params import (
        RateCreateParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_delete_params import (
        RateDeleteParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_list_params import (
        RateListParams,
    )
    from stripe.params.v2.billing.rate_cards._rate_retrieve_params import (
        RateRetrieveParams,
    )
    from stripe.v2._deleted_object import DeletedObject
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._rate_card_rate import RateCardRate


class RateService(StripeService):
    def list(
        self,
        rate_card_id: str,
        params: Optional["RateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardRate]":
        """
        List all Rates associated with a Rate Card for a specific version (defaults to latest). Rates remain active for all subsequent versions until a new rate is created for the same Metered Item.
        """
        return cast(
            "ListObject[RateCardRate]",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/rates".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        rate_card_id: str,
        params: Optional["RateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardRate]":
        """
        List all Rates associated with a Rate Card for a specific version (defaults to latest). Rates remain active for all subsequent versions until a new rate is created for the same Metered Item.
        """
        return cast(
            "ListObject[RateCardRate]",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/rates".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        rate_card_id: str,
        params: Optional["RateCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardRate":
        """
        Set the Rate for a Metered Item on the latest version of a Rate Card object. This will create a new Rate Card version
        if the Metered Item already has a rate on the Rate Card.
        """
        return cast(
            "RateCardRate",
            self._request(
                "post",
                "/v2/billing/rate_cards/{rate_card_id}/rates".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        rate_card_id: str,
        params: Optional["RateCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardRate":
        """
        Set the Rate for a Metered Item on the latest version of a Rate Card object. This will create a new Rate Card version
        if the Metered Item already has a rate on the Rate Card.
        """
        return cast(
            "RateCardRate",
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{rate_card_id}/rates".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def delete(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["RateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Remove an existing Rate from a Rate Card. This will create a new Rate Card Version without that Rate.
        """
        return cast(
            "DeletedObject",
            self._request(
                "delete",
                "/v2/billing/rate_cards/{rate_card_id}/rates/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["RateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Remove an existing Rate from a Rate Card. This will create a new Rate Card Version without that Rate.
        """
        return cast(
            "DeletedObject",
            await self._request_async(
                "delete",
                "/v2/billing/rate_cards/{rate_card_id}/rates/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["RateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardRate":
        """
        Retrieve a Rate object.
        """
        return cast(
            "RateCardRate",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/rates/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["RateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardRate":
        """
        Retrieve a Rate object.
        """
        return cast(
            "RateCardRate",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/rates/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
