# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._payment_method import PaymentMethod
    from stripe._request_options import RequestOptions
    from stripe.params._customer_payment_method_list_params import (
        CustomerPaymentMethodListParams,
    )
    from stripe.params._customer_payment_method_retrieve_params import (
        CustomerPaymentMethodRetrieveParams,
    )


class CustomerPaymentMethodService(StripeService):
    def list(
        self,
        id: str,
        /,
        params: Optional["CustomerPaymentMethodListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentMethod]":
        """
        Returns a list of PaymentMethods for a given Customer
        """
        return cast(
            "ListObject[PaymentMethod]",
            self._request(
                "get",
                "/v1/customers/{id}/payment_methods".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        /,
        params: Optional["CustomerPaymentMethodListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentMethod]":
        """
        Returns a list of PaymentMethods for a given Customer
        """
        return cast(
            "ListObject[PaymentMethod]",
            await self._request_async(
                "get",
                "/v1/customers/{id}/payment_methods".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        customer_id: str,
        id: str,
        /,
        params: Optional["CustomerPaymentMethodRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "get",
                "/v1/customers/{customer_id}/payment_methods/{id}".format(
                    customer_id=sanitize_id(customer_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        customer_id: str,
        id: str,
        /,
        params: Optional["CustomerPaymentMethodRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        return cast(
            "PaymentMethod",
            await self._request_async(
                "get",
                "/v1/customers/{customer_id}/payment_methods/{id}".format(
                    customer_id=sanitize_id(customer_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
