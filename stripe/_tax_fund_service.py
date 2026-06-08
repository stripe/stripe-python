# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe._tax_fund import TaxFund
    from stripe.params._tax_fund_list_params import TaxFundListParams
    from stripe.params._tax_fund_retrieve_params import TaxFundRetrieveParams


class TaxFundService(StripeService):
    def list(
        self,
        params: Optional["TaxFundListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TaxFund]":
        """
        Returns a list of tax funds in reverse chronological order.
        """
        return cast(
            "ListObject[TaxFund]",
            self._request(
                "get",
                "/v1/tax_funds",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["TaxFundListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TaxFund]":
        """
        Returns a list of tax funds in reverse chronological order.
        """
        return cast(
            "ListObject[TaxFund]",
            await self._request_async(
                "get",
                "/v1/tax_funds",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        tax_fund: str,
        params: Optional["TaxFundRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxFund":
        """
        Retrieves a tax fund object by its ID.
        """
        return cast(
            "TaxFund",
            self._request(
                "get",
                "/v1/tax_funds/{tax_fund}".format(
                    tax_fund=sanitize_id(tax_fund),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        tax_fund: str,
        params: Optional["TaxFundRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxFund":
        """
        Retrieves a tax fund object by its ID.
        """
        return cast(
            "TaxFund",
            await self._request_async(
                "get",
                "/v1/tax_funds/{tax_fund}".format(
                    tax_fund=sanitize_id(tax_fund),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
