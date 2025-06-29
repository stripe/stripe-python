# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._list_object import ListObject
from stripe.v2.payments._off_session_payment import OffSessionPayment
from typing import Dict, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OffSessionPaymentService(StripeService):
    class CancelParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        amount: AmountParam
        """
        Amount you want to collect.
        """
        cadence: Literal["recurring", "unscheduled"]
        """
        The frequency of the OSP.
        """
        customer: str
        """
        Customer that owns the provided payment method.
        """
        metadata: Dict[str, str]
        """
        Any of your internal data you want to track here.
        """
        on_behalf_of: NotRequired[str]
        """
        The OBO merchant you want to use.
        """
        payment_method: str
        """
        Payment method you want to debit. Must be attached to a customer and set up for off-session usage.
        """
        retry_details: NotRequired[
            "OffSessionPaymentService.CreateParamsRetryDetails"
        ]
        """
        How you want stripe to retry the OSP.
        """
        statement_descriptor: NotRequired[str]
        """
        String you want to appear on your customer's statement.
        """
        statement_descriptor_suffix: NotRequired[str]
        """
        Suffix appended to your account level descriptor.
        """
        test_clock: NotRequired[str]
        """
        Test clock to be used for testing your retry handling. Only usable in a sandbox.
        """
        transfer_data: NotRequired[
            "OffSessionPaymentService.CreateParamsTransferData"
        ]
        """
        How you want to transfer the funds to your connected accounts.
        """

    class CreateParamsRetryDetails(TypedDict):
        retry_strategy: Literal["none", "smart"]
        """
        How you want Stripe to retry the payment.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[int]
        """
        Amount in minor units that you want to transfer.
        """
        destination: str
        """
        ID of the connected account where you want money to go.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page size limit, if not provided the default is 20.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "OffSessionPaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OffSessionPayment]:
        """
        List OSPs matching filter.
        """
        return cast(
            ListObject[OffSessionPayment],
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
        params: "OffSessionPaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OffSessionPayment]:
        """
        List OSPs matching filter.
        """
        return cast(
            ListObject[OffSessionPayment],
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
        params: "OffSessionPaymentService.CreateParams",
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Create OSP.
        """
        return cast(
            OffSessionPayment,
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
        params: "OffSessionPaymentService.CreateParams",
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Create OSP.
        """
        return cast(
            OffSessionPayment,
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
        params: "OffSessionPaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Retrieve OSP by ID.
        """
        return cast(
            OffSessionPayment,
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
        params: "OffSessionPaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Retrieve OSP by ID.
        """
        return cast(
            OffSessionPayment,
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
        params: "OffSessionPaymentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Cancel OSP.
        """
        return cast(
            OffSessionPayment,
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
        params: "OffSessionPaymentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> OffSessionPayment:
        """
        Cancel OSP.
        """
        return cast(
            OffSessionPayment,
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
