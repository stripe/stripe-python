# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.contracts.license_pricing._quantity_change_list_quantity_changes_params import (
        QuantityChangeListQuantityChangesParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._contract_license_pricing_quantity_change import (
        ContractLicensePricingQuantityChange,
    )


class QuantityChangeService(StripeService):
    def list_quantity_changes(
        self,
        contract_id: str,
        license_pricing_id: str,
        params: Optional["QuantityChangeListQuantityChangesParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractLicensePricingQuantityChange]":
        """
        List license quantity changes for a contract given a license pricing ID.
        """
        return cast(
            "ListObject[ContractLicensePricingQuantityChange]",
            self._request(
                "get",
                "/v2/billing/contracts/{contract_id}/license_pricing/{license_pricing_id}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    license_pricing_id=sanitize_id(license_pricing_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_quantity_changes_async(
        self,
        contract_id: str,
        license_pricing_id: str,
        params: Optional["QuantityChangeListQuantityChangesParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractLicensePricingQuantityChange]":
        """
        List license quantity changes for a contract given a license pricing ID.
        """
        return cast(
            "ListObject[ContractLicensePricingQuantityChange]",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{contract_id}/license_pricing/{license_pricing_id}/quantity_changes".format(
                    contract_id=sanitize_id(contract_id),
                    license_pricing_id=sanitize_id(license_pricing_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
