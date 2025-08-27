# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._rate_card_rate import RateCardRate
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class RateService(StripeService):
    class CreateParams(TypedDict):
        custom_pricing_unit_amount: NotRequired[
            "RateService.CreateParamsCustomPricingUnitAmount"
        ]
        """
        The custom pricing unit that this rate binds to.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        metered_item: NotRequired[str]
        """
        The Metered Item that this rate binds to.
        """
        price: NotRequired[str]
        """
        The ID of the price object to take price information from. The price must have the same interval as the rate card.
        Updates to the Price will not be reflected in the Rate Card or its rates.
        """
        tiering_mode: NotRequired[Literal["graduated", "volume"]]
        """
        Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
        quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
        grows into new tiers. Can only be set if `tiers` is set.
        """
        tiers: NotRequired[List["RateService.CreateParamsTier"]]
        """
        Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
        """
        transform_quantity: NotRequired[
            "RateService.CreateParamsTransformQuantity"
        ]
        """
        Apply a transformation to the reported usage or set quantity before computing the amount billed.
        """
        unit_amount: NotRequired[str]
        """
        The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
        places. Cannot be set if `tiers` is provided.
        """

    class CreateParamsCustomPricingUnitAmount(TypedDict):
        id: str
        """
        The id of the custom pricing unit.
        """
        value: str
        """
        The unit value for the custom pricing unit, as a string.
        """

    class CreateParamsTier(TypedDict):
        flat_amount: NotRequired[str]
        """
        Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
        """
        unit_amount: NotRequired[str]
        """
        Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
        most 12 decimal places.
        """
        up_to_decimal: NotRequired[str]
        """
        Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
        be set.
        """
        up_to_inf: NotRequired[Literal["inf"]]
        """
        No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
        """

    class CreateParamsTransformQuantity(TypedDict):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, round the result up or down.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        metered_item: NotRequired[str]
        """
        Optionally filter by a Metered Item.
        """
        rate_card_version: NotRequired[str]
        """
        Optionally filter by a RateCard version. If not specified, defaults to the latest version.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        rate_card_id: str,
        params: "RateService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardRate]:
        """
        List all Rates associated with a Rate Card for a specific version (defaults to latest). Rates remain active for all subsequent versions until a new rate is created for the same Metered Item.
        """
        return cast(
            ListObject[RateCardRate],
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
        params: "RateService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardRate]:
        """
        List all Rates associated with a Rate Card for a specific version (defaults to latest). Rates remain active for all subsequent versions until a new rate is created for the same Metered Item.
        """
        return cast(
            ListObject[RateCardRate],
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
        params: "RateService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Set the Rate for a Metered Item on the latest version of a Rate Card object. This will create a new Rate Card version
        if the Metered Item already has a rate on the Rate Card.
        """
        return cast(
            RateCardRate,
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
        params: "RateService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Set the Rate for a Metered Item on the latest version of a Rate Card object. This will create a new Rate Card version
        if the Metered Item already has a rate on the Rate Card.
        """
        return cast(
            RateCardRate,
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
        params: "RateService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Remove an existing Rate from a Rate Card. This will create a new Rate Card Version without that Rate.
        """
        return cast(
            RateCardRate,
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
        params: "RateService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Remove an existing Rate from a Rate Card. This will create a new Rate Card Version without that Rate.
        """
        return cast(
            RateCardRate,
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
        params: "RateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Retrieve a Rate object.
        """
        return cast(
            RateCardRate,
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
        params: "RateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardRate:
        """
        Retrieve a Rate object.
        """
        return cast(
            RateCardRate,
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
