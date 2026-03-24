# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._rate_card_create_params import (
        RateCardCreateParams,
    )
    from stripe.params.v2.billing._rate_card_list_params import (
        RateCardListParams,
    )
    from stripe.params.v2.billing._rate_card_modify_rates_params import (
        RateCardModifyRatesParams,
    )
    from stripe.params.v2.billing._rate_card_retrieve_params import (
        RateCardRetrieveParams,
    )
    from stripe.params.v2.billing._rate_card_update_params import (
        RateCardUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._rate_card import RateCard
    from stripe.v2.billing._rate_card_version import RateCardVersion
    from stripe.v2.billing.rate_cards._custom_pricing_unit_overage_rate_service import (
        CustomPricingUnitOverageRateService,
    )
    from stripe.v2.billing.rate_cards._rate_service import RateService
    from stripe.v2.billing.rate_cards._version_service import VersionService

_subservices = {
    "custom_pricing_unit_overage_rates": [
        "stripe.v2.billing.rate_cards._custom_pricing_unit_overage_rate_service",
        "CustomPricingUnitOverageRateService",
    ],
    "rates": ["stripe.v2.billing.rate_cards._rate_service", "RateService"],
    "versions": [
        "stripe.v2.billing.rate_cards._version_service",
        "VersionService",
    ],
}


class RateCardService(StripeService):
    custom_pricing_unit_overage_rates: "CustomPricingUnitOverageRateService"
    rates: "RateService"
    versions: "VersionService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["RateCardListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCard]":
        """
        List all Rate Card objects.
        """
        return cast(
            "ListObject[RateCard]",
            self._request(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RateCardListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCard]":
        """
        List all Rate Card objects.
        """
        return cast(
            "ListObject[RateCard]",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RateCardCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Create a Rate Card object.
        """
        return cast(
            "RateCard",
            self._request(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RateCardCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Create a Rate Card object.
        """
        return cast(
            "RateCard",
            await self._request_async(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["RateCardRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            "RateCard",
            self._request(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["RateCardRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            "RateCard",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["RateCardUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Update a Rate Card object.
        """
        return cast(
            "RateCard",
            self._request(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["RateCardUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCard":
        """
        Update a Rate Card object.
        """
        return cast(
            "RateCard",
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def modify_rates(
        self,
        id: str,
        params: "RateCardModifyRatesParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardVersion":
        """
        Creates, updates, and/or deletes multiple Rates on a Rate Card atomically.
        """
        return cast(
            "RateCardVersion",
            self._request(
                "post",
                "/v2/billing/rate_cards/{id}/modify_rates".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "rates_to_create": {
                            "transform_quantity": {
                                "divide_by": "int64_string"
                            },
                        },
                    },
                ),
                options=options,
            ),
        )

    async def modify_rates_async(
        self,
        id: str,
        params: "RateCardModifyRatesParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardVersion":
        """
        Creates, updates, and/or deletes multiple Rates on a Rate Card atomically.
        """
        return cast(
            "RateCardVersion",
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{id}/modify_rates".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "rates_to_create": {
                            "transform_quantity": {
                                "divide_by": "int64_string"
                            },
                        },
                    },
                ),
                options=options,
            ),
        )
