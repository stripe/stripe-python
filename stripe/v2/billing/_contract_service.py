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
    from stripe.params.v2.billing._contract_activate_params import (
        ContractActivateParams,
    )
    from stripe.params.v2.billing._contract_cancel_params import (
        ContractCancelParams,
    )
    from stripe.params.v2.billing._contract_create_params import (
        ContractCreateParams,
    )
    from stripe.params.v2.billing._contract_list_params import (
        ContractListParams,
    )
    from stripe.params.v2.billing._contract_retrieve_params import (
        ContractRetrieveParams,
    )
    from stripe.params.v2.billing._contract_update_params import (
        ContractUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._contract import Contract
    from stripe.v2.billing.contracts._license_pricing_service import (
        LicensePricingService,
    )

_subservices = {
    "license_pricing": [
        "stripe.v2.billing.contracts._license_pricing_service",
        "LicensePricingService",
    ],
}


class ContractService(StripeService):
    license_pricing: "LicensePricingService"

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
        params: Optional["ContractListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Contract]":
        """
        List Contract objects with pagination.
        """
        return cast(
            "ListObject[Contract]",
            self._request(
                "get",
                "/v2/billing/contracts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ContractListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Contract]":
        """
        List Contract objects with pagination.
        """
        return cast(
            "ListObject[Contract]",
            await self._request_async(
                "get",
                "/v2/billing/contracts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ContractCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Create a Contract object.
        """
        return cast(
            "Contract",
            self._request(
                "post",
                "/v2/billing/contracts",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "one_time_fees": {
                            "bill_schedule": {"value": "int64_string"},
                        },
                    },
                ),
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ContractCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Create a Contract object.
        """
        return cast(
            "Contract",
            await self._request_async(
                "post",
                "/v2/billing/contracts",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "one_time_fees": {
                            "bill_schedule": {"value": "int64_string"},
                        },
                    },
                ),
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ContractRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Retrieve a Contract object by ID.
        """
        return cast(
            "Contract",
            self._request(
                "get",
                "/v2/billing/contracts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ContractRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Retrieve a Contract object by ID.
        """
        return cast(
            "Contract",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["ContractUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Update a Contract object by ID.
        """
        return cast(
            "Contract",
            self._request(
                "post",
                "/v2/billing/contracts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["ContractUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Update a Contract object by ID.
        """
        return cast(
            "Contract",
            await self._request_async(
                "post",
                "/v2/billing/contracts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def activate(
        self,
        id: str,
        params: Optional["ContractActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Activate a Draft Contract object by ID.
        """
        return cast(
            "Contract",
            self._request(
                "post",
                "/v2/billing/contracts/{id}/activate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def activate_async(
        self,
        id: str,
        params: Optional["ContractActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Activate a Draft Contract object by ID.
        """
        return cast(
            "Contract",
            await self._request_async(
                "post",
                "/v2/billing/contracts/{id}/activate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["ContractCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Cancel a Contract object by ID.
        """
        return cast(
            "Contract",
            self._request(
                "post",
                "/v2/billing/contracts/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["ContractCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Contract":
        """
        Cancel a Contract object by ID.
        """
        return cast(
            "Contract",
            await self._request_async(
                "post",
                "/v2/billing/contracts/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
