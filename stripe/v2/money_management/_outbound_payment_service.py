# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._outbound_payment_cancel_params import (
        OutboundPaymentCancelParams,
    )
    from stripe.params.v2.money_management._outbound_payment_create_params import (
        OutboundPaymentCreateParams,
    )
    from stripe.params.v2.money_management._outbound_payment_list_params import (
        OutboundPaymentListParams,
    )
    from stripe.params.v2.money_management._outbound_payment_retrieve_params import (
        OutboundPaymentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._outbound_payment import OutboundPayment


class OutboundPaymentService(StripeService):
    def list(
        self,
        params: Optional["OutboundPaymentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundPayment]":
        """
        Returns a list of OutboundPayments that match the provided filters.
        """
        return cast(
            "ListObject[OutboundPayment]",
            self._request(
                "get",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OutboundPaymentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OutboundPayment]":
        """
        Returns a list of OutboundPayments that match the provided filters.
        """
        return cast(
            "ListObject[OutboundPayment]",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OutboundPaymentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Creates an OutboundPayment.
        """
        return cast(
            "OutboundPayment",
            self._request(
                "post",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OutboundPaymentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Creates an OutboundPayment.
        """
        return cast(
            "OutboundPayment",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OutboundPaymentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment create or list response.
        """
        return cast(
            "OutboundPayment",
            self._request(
                "get",
                "/v2/money_management/outbound_payments/{id}".format(
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
        params: Optional["OutboundPaymentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Retrieves the details of an existing OutboundPayment by passing the unique OutboundPayment ID from either the OutboundPayment create or list response.
        """
        return cast(
            "OutboundPayment",
            await self._request_async(
                "get",
                "/v2/money_management/outbound_payments/{id}".format(
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
        params: Optional["OutboundPaymentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Cancels an OutboundPayment. Only processing OutboundPayments can be canceled.
        """
        return cast(
            "OutboundPayment",
            self._request(
                "post",
                "/v2/money_management/outbound_payments/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["OutboundPaymentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OutboundPayment":
        """
        Cancels an OutboundPayment. Only processing OutboundPayments can be canceled.
        """
        return cast(
            "OutboundPayment",
            await self._request_async(
                "post",
                "/v2/money_management/outbound_payments/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
