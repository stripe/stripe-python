# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.contracts.terms._quantity_change_list_contract_term_quantity_changes_params import (
        QuantityChangeListContractTermQuantityChangesParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._contract_term_quantity_change import (
        ContractTermQuantityChange,
    )


class QuantityChangeService(StripeService):
    def list_contract_term_quantity_changes(
        self,
        contract_id: str,
        term: str,
        /,
        params: Optional[
            "QuantityChangeListContractTermQuantityChangesParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractTermQuantityChange]":
        """
        List quantity changes for a licensed recurring-price term.
        """
        return cast(
            "ListObject[ContractTermQuantityChange]",
            self._request(
                "get",
                "/v2/billing/contracts/{contract_id}/terms/{term}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    term=sanitize_id(term),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_contract_term_quantity_changes_async(
        self,
        contract_id: str,
        term: str,
        /,
        params: Optional[
            "QuantityChangeListContractTermQuantityChangesParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractTermQuantityChange]":
        """
        List quantity changes for a licensed recurring-price term.
        """
        return cast(
            "ListObject[ContractTermQuantityChange]",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{contract_id}/terms/{term}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    term=sanitize_id(term),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
