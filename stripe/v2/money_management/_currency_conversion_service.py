# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._currency_conversion_create_params import (
        CurrencyConversionCreateParams,
    )
    from stripe.params.v2.money_management._currency_conversion_list_params import (
        CurrencyConversionListParams,
    )
    from stripe.params.v2.money_management._currency_conversion_retrieve_params import (
        CurrencyConversionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._currency_conversion import (
        CurrencyConversion,
    )


class CurrencyConversionService(StripeService):
    def list(
        self,
        params: Optional["CurrencyConversionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CurrencyConversion]":
        """
        Lists all Currency Conversions that match the provided filters.
        """
        return cast(
            "ListObject[CurrencyConversion]",
            self._request(
                "get",
                "/v2/money_management/currency_conversions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["CurrencyConversionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CurrencyConversion]":
        """
        Lists all Currency Conversions that match the provided filters.
        """
        return cast(
            "ListObject[CurrencyConversion]",
            await self._request_async(
                "get",
                "/v2/money_management/currency_conversions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CurrencyConversionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CurrencyConversion":
        """
        Create a new Currency Conversion in a Financial Account or the payments balance.
        """
        return cast(
            "CurrencyConversion",
            self._request(
                "post",
                "/v2/money_management/currency_conversions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CurrencyConversionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CurrencyConversion":
        """
        Create a new Currency Conversion in a Financial Account or the payments balance.
        """
        return cast(
            "CurrencyConversion",
            await self._request_async(
                "post",
                "/v2/money_management/currency_conversions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["CurrencyConversionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CurrencyConversion":
        """
        Retrieves the details of a Currency Conversion by its ID.
        """
        return cast(
            "CurrencyConversion",
            self._request(
                "get",
                "/v2/money_management/currency_conversions/{id}".format(
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
        /,
        params: Optional["CurrencyConversionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CurrencyConversion":
        """
        Retrieves the details of a Currency Conversion by its ID.
        """
        return cast(
            "CurrencyConversion",
            await self._request_async(
                "get",
                "/v2/money_management/currency_conversions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
