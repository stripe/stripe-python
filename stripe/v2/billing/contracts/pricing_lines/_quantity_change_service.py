# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.contracts.pricing_lines._quantity_change_list_contract_pricing_line_quantity_changes_params import (
        QuantityChangeListContractPricingLineQuantityChangesParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._contract_pricing_line_quantity_change import (
        ContractPricingLineQuantityChange,
    )


class QuantityChangeService(StripeService):
    def list_contract_pricing_line_quantity_changes(
        self,
        contract_id: str,
        pricing_line_id: str,
        params: Optional[
            "QuantityChangeListContractPricingLineQuantityChangesParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractPricingLineQuantityChange]":
        """
        List quantity changes for a pricing line on a contract.
        """
        return cast(
            "ListObject[ContractPricingLineQuantityChange]",
            self._request(
                "get",
                "/v2/billing/contracts/{contract_id}/pricing_lines/{pricing_line_id}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    pricing_line_id=sanitize_id(pricing_line_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_contract_pricing_line_quantity_changes_async(
        self,
        contract_id: str,
        pricing_line_id: str,
        params: Optional[
            "QuantityChangeListContractPricingLineQuantityChangesParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractPricingLineQuantityChange]":
        """
        List quantity changes for a pricing line on a contract.
        """
        return cast(
            "ListObject[ContractPricingLineQuantityChange]",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{contract_id}/pricing_lines/{pricing_line_id}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    pricing_line_id=sanitize_id(pricing_line_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
