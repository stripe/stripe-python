# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_create_params import (
        CustomPricingUnitOverageRateCreateParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_delete_params import (
        CustomPricingUnitOverageRateDeleteParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_list_params import (
        CustomPricingUnitOverageRateListParams,
    )
    from stripe.params.v2.billing.rate_cards._custom_pricing_unit_overage_rate_retrieve_params import (
        CustomPricingUnitOverageRateRetrieveParams,
    )
    from stripe.v2._deleted_object import DeletedObject
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._rate_card_custom_pricing_unit_overage_rate import (
        RateCardCustomPricingUnitOverageRate,
    )


class CustomPricingUnitOverageRateService(StripeService):
    def list(
        self,
        rate_card_id: str,
        params: Optional["CustomPricingUnitOverageRateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardCustomPricingUnitOverageRate]":
        """
        List all Rate Card Custom Pricing Unit Overage Rates on a Rate Card.
        """
        return cast(
            "ListObject[RateCardCustomPricingUnitOverageRate]",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates".format(
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
        params: Optional["CustomPricingUnitOverageRateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardCustomPricingUnitOverageRate]":
        """
        List all Rate Card Custom Pricing Unit Overage Rates on a Rate Card.
        """
        return cast(
            "ListObject[RateCardCustomPricingUnitOverageRate]",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates".format(
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
        params: "CustomPricingUnitOverageRateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardCustomPricingUnitOverageRate":
        """
        Create a Rate Card Custom Pricing Unit Overage Rate on a Rate Card.
        """
        return cast(
            "RateCardCustomPricingUnitOverageRate",
            self._request(
                "post",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates".format(
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
        params: "CustomPricingUnitOverageRateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardCustomPricingUnitOverageRate":
        """
        Create a Rate Card Custom Pricing Unit Overage Rate on a Rate Card.
        """
        return cast(
            "RateCardCustomPricingUnitOverageRate",
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates".format(
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
        params: Optional["CustomPricingUnitOverageRateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Delete a Rate Card Custom Pricing Unit Overage Rate from a Rate Card.
        """
        return cast(
            "DeletedObject",
            self._request(
                "delete",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates/{id}".format(
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
        params: Optional["CustomPricingUnitOverageRateDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Delete a Rate Card Custom Pricing Unit Overage Rate from a Rate Card.
        """
        return cast(
            "DeletedObject",
            await self._request_async(
                "delete",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates/{id}".format(
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
        params: Optional["CustomPricingUnitOverageRateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardCustomPricingUnitOverageRate":
        """
        Retrieve a Rate Card Custom Pricing Unit Overage Rate from a Rate Card.
        """
        return cast(
            "RateCardCustomPricingUnitOverageRate",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates/{id}".format(
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
        params: Optional["CustomPricingUnitOverageRateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardCustomPricingUnitOverageRate":
        """
        Retrieve a Rate Card Custom Pricing Unit Overage Rate from a Rate Card.
        """
        return cast(
            "RateCardCustomPricingUnitOverageRate",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/custom_pricing_unit_overage_rates/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
