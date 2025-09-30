# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.tax._calculation import Calculation
from stripe.tax._calculation_line_item_service import (
    CalculationLineItemService,
)
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.tax._calculation_create_params import (
        CalculationCreateParams,
    )
    from stripe.params.tax._calculation_retrieve_params import (
        CalculationRetrieveParams,
    )


class CalculationService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.line_items = CalculationLineItemService(self._requestor)

    def retrieve(
        self,
        calculation: str,
        params: Optional["CalculationRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> Calculation:
        """
        Retrieves a Tax Calculation object, if the calculation hasn't expired.
        """
        return cast(
            Calculation,
            self._request(
                "get",
                "/v1/tax/calculations/{calculation}".format(
                    calculation=sanitize_id(calculation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        calculation: str,
        params: Optional["CalculationRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> Calculation:
        """
        Retrieves a Tax Calculation object, if the calculation hasn't expired.
        """
        return cast(
            Calculation,
            await self._request_async(
                "get",
                "/v1/tax/calculations/{calculation}".format(
                    calculation=sanitize_id(calculation),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CalculationCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> Calculation:
        """
        Calculates tax based on the input and returns a Tax Calculation object.
        """
        return cast(
            Calculation,
            self._request(
                "post",
                "/v1/tax/calculations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CalculationCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> Calculation:
        """
        Calculates tax based on the input and returns a Tax Calculation object.
        """
        return cast(
            Calculation,
            await self._request_async(
                "post",
                "/v1/tax/calculations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
