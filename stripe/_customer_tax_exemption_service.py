# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer_tax_exemption import CustomerTaxExemption
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._customer_tax_exemption_create_params import (
        CustomerTaxExemptionCreateParams,
    )
    from stripe.params._customer_tax_exemption_delete_params import (
        CustomerTaxExemptionDeleteParams,
    )
    from stripe.params._customer_tax_exemption_list_params import (
        CustomerTaxExemptionListParams,
    )
    from stripe.params._customer_tax_exemption_retrieve_params import (
        CustomerTaxExemptionRetrieveParams,
    )


class CustomerTaxExemptionService(StripeService):
    def delete(
        self,
        customer: str,
        id: str,
        params: Optional["CustomerTaxExemptionDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Delete a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            self._request(
                "delete",
                "/v1/customers/{customer}/tax_exemptions/{id}".format(
                    customer=sanitize_id(customer),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        customer: str,
        id: str,
        params: Optional["CustomerTaxExemptionDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Delete a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            await self._request_async(
                "delete",
                "/v1/customers/{customer}/tax_exemptions/{id}".format(
                    customer=sanitize_id(customer),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        customer: str,
        id: str,
        params: Optional["CustomerTaxExemptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Retrieve a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            self._request(
                "get",
                "/v1/customers/{customer}/tax_exemptions/{id}".format(
                    customer=sanitize_id(customer),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        customer: str,
        id: str,
        params: Optional["CustomerTaxExemptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Retrieve a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            await self._request_async(
                "get",
                "/v1/customers/{customer}/tax_exemptions/{id}".format(
                    customer=sanitize_id(customer),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        customer: str,
        params: Optional["CustomerTaxExemptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerTaxExemption]":
        """
        List all location specific tax exemptions for a customer.
        """
        return cast(
            "ListObject[CustomerTaxExemption]",
            self._request(
                "get",
                "/v1/customers/{customer}/tax_exemptions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        customer: str,
        params: Optional["CustomerTaxExemptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CustomerTaxExemption]":
        """
        List all location specific tax exemptions for a customer.
        """
        return cast(
            "ListObject[CustomerTaxExemption]",
            await self._request_async(
                "get",
                "/v1/customers/{customer}/tax_exemptions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        customer: str,
        params: "CustomerTaxExemptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Create a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            self._request(
                "post",
                "/v1/customers/{customer}/tax_exemptions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        customer: str,
        params: "CustomerTaxExemptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerTaxExemption":
        """
        Create a location specific tax exemption for a customer.
        """
        return cast(
            "CustomerTaxExemption",
            await self._request_async(
                "post",
                "/v1/customers/{customer}/tax_exemptions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
