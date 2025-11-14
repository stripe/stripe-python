# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.payments._off_session_payment_cancel_params import (
        OffSessionPaymentCancelParams,
    )
    from stripe.params.v2.payments._off_session_payment_capture_params import (
        OffSessionPaymentCaptureParams,
    )
    from stripe.params.v2.payments._off_session_payment_create_params import (
        OffSessionPaymentCreateParams,
    )
    from stripe.params.v2.payments._off_session_payment_list_params import (
        OffSessionPaymentListParams,
    )
    from stripe.params.v2.payments._off_session_payment_retrieve_params import (
        OffSessionPaymentRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.payments._off_session_payment import OffSessionPayment


class OffSessionPaymentService(StripeService):
    def list(
        self,
        params: Optional["OffSessionPaymentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OffSessionPayment]":
        """
        Returns a list of OffSessionPayments matching a filter.
        """
        return cast(
            "ListObject[OffSessionPayment]",
            self._request(
                "get",
                "/v2/payments/off_session_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OffSessionPaymentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OffSessionPayment]":
        """
        Returns a list of OffSessionPayments matching a filter.
        """
        return cast(
            "ListObject[OffSessionPayment]",
            await self._request_async(
                "get",
                "/v2/payments/off_session_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OffSessionPaymentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Creates an OffSessionPayment object.
        """
        return cast(
            "OffSessionPayment",
            self._request(
                "post",
                "/v2/payments/off_session_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OffSessionPaymentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Creates an OffSessionPayment object.
        """
        return cast(
            "OffSessionPayment",
            await self._request_async(
                "post",
                "/v2/payments/off_session_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OffSessionPaymentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Retrieves the details of an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            self._request(
                "get",
                "/v2/payments/off_session_payments/{id}".format(
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
        params: Optional["OffSessionPaymentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Retrieves the details of an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            await self._request_async(
                "get",
                "/v2/payments/off_session_payments/{id}".format(
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
        params: Optional["OffSessionPaymentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Cancel an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            self._request(
                "post",
                "/v2/payments/off_session_payments/{id}/cancel".format(
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
        params: Optional["OffSessionPaymentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Cancel an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            await self._request_async(
                "post",
                "/v2/payments/off_session_payments/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def capture(
        self,
        id: str,
        params: "OffSessionPaymentCaptureParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Captures an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            self._request(
                "post",
                "/v2/payments/off_session_payments/{id}/capture".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def capture_async(
        self,
        id: str,
        params: "OffSessionPaymentCaptureParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OffSessionPayment":
        """
        Captures an OffSessionPayment that has previously been created.
        """
        return cast(
            "OffSessionPayment",
            await self._request_async(
                "post",
                "/v2/payments/off_session_payments/{id}/capture".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
