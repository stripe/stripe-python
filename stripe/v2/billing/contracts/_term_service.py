# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.contracts._term_list_contract_terms_params import (
        TermListContractTermsParams,
    )
    from stripe.params.v2.billing.contracts._term_retrieve_contract_term_params import (
        TermRetrieveContractTermParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._contract_term import ContractTerm
    from stripe.v2.billing.contracts.terms._quantity_change_service import (
        QuantityChangeService,
    )

_subservices = {
    "quantity_changes": [
        "stripe.v2.billing.contracts.terms._quantity_change_service",
        "QuantityChangeService",
    ],
}


class TermService(StripeService):
    quantity_changes: "QuantityChangeService"

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

    def list_contract_terms(
        self,
        contract_id: str,
        /,
        params: Optional["TermListContractTermsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractTerm]":
        """
        List the terms on a contract, optionally filtered by type.
        """
        return cast(
            "ListObject[ContractTerm]",
            self._request(
                "get",
                "/v2/billing/contracts/{contract_id}/terms".format(
                    contract_id=sanitize_id(contract_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_contract_terms_async(
        self,
        contract_id: str,
        /,
        params: Optional["TermListContractTermsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ContractTerm]":
        """
        List the terms on a contract, optionally filtered by type.
        """
        return cast(
            "ListObject[ContractTerm]",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{contract_id}/terms".format(
                    contract_id=sanitize_id(contract_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve_contract_term(
        self,
        contract_id: str,
        id: str,
        /,
        params: Optional["TermRetrieveContractTermParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ContractTerm":
        """
        Retrieve a term on a contract.
        """
        return cast(
            "ContractTerm",
            self._request(
                "get",
                "/v2/billing/contracts/{contract_id}/terms/{id}".format(
                    contract_id=sanitize_id(contract_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_contract_term_async(
        self,
        contract_id: str,
        id: str,
        /,
        params: Optional["TermRetrieveContractTermParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ContractTerm":
        """
        Retrieve a term on a contract.
        """
        return cast(
            "ContractTerm",
            await self._request_async(
                "get",
                "/v2/billing/contracts/{contract_id}/terms/{id}".format(
                    contract_id=sanitize_id(contract_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
