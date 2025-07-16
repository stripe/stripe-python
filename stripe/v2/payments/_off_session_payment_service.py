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
        The “presentment amount” to be collected from the customer.
        """
        cadence: Literal["recurring", "unscheduled"]
        """
        The frequency of the underlying payment.
        """
        customer: str
        """
        ID of the Customer to which this OffSessionPayment belongs.
        """
        metadata: Dict[str, str]
        """
        Set of [key-value pairs](https://docs.corp.stripe.com/api/metadata) that you can
        attach to an object. This can be useful for storing additional information about
        the object in a structured format. Learn more about
        [storing information in metadata](https://docs.corp.stripe.com/payments/payment-intents#storing-information-in-metadata).
        """
        on_behalf_of: NotRequired[str]
        """
        The account (if any) for which the funds of the OffSessionPayment are intended.
        """
        payment_method: str
        """
        ID of the payment method used in this OffSessionPayment.
        """
        retry_details: NotRequired[
            "OffSessionPaymentService.CreateParamsRetryDetails"
        ]
        """
        Details about the OffSessionPayment retries.
        """
        statement_descriptor: NotRequired[str]
        """
        Text that appears on the customer's statement as the statement descriptor for a
        non-card charge. This value overrides the account's default statement descriptor.
        For information about requirements, including the 22-character limit, see the
        [Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
        """
        statement_descriptor_suffix: NotRequired[str]
        """
        Provides information about a card charge. Concatenated to the account's
        [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
        to form the complete statement descriptor that appears on the customer's statement.
        """
        test_clock: NotRequired[str]
        """
        Test clock that can be used to advance the retry attempts in a sandbox.
        """
        transfer_data: NotRequired[
            "OffSessionPaymentService.CreateParamsTransferData"
        ]
        """
        The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.corp.stripe.com/payments/connected-accounts).
        """

    class CreateParamsRetryDetails(TypedDict):
        retry_strategy: Literal["none", "smart"]
        """
        Indicates the strategy for how you want Stripe to retry the payment.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[int]
        """
        The amount transferred to the destination account. This transfer will occur
        automatically after the payment succeeds. If no amount is specified, by default
        the entire payment amount is transferred to the destination account. The amount
        must be less than or equal to the
        [amount_requested](https://docs.corp.stripe.com/api/v2/off-session-payments/object?api-version=2025-05-28.preview#v2_off_session_payment_object-amount_requested),
        and must be a positive integer representing how much to transfer in the smallest
        currency unit (e.g., 100 cents to charge $1.00).
        """
        destination: str
        """
        The account (if any) that the payment is attributed to for tax reporting, and
        where funds from the payment are transferred to after payment success.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The page size limit. If not provided, the default is 20.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "OffSessionPaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[OffSessionPayment]:
        """
        Returns a list of OffSessionPayments matching a filter.
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
        Returns a list of OffSessionPayments matching a filter.
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
        Creates an OffSessionPayment object.
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
        Creates an OffSessionPayment object.
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
        Retrieves the details of an OffSessionPayment that has previously been created.
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
        Retrieves the details of an OffSessionPayment that has previously been created.
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
        Cancel an OffSessionPayment that has previously been created.
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
        Cancel an OffSessionPayment that has previously been created.
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
