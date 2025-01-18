# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._payment_attempt_record import PaymentAttemptRecord
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class PaymentAttemptRecordService(StripeService):
    class ListParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_record: str
        """
        The ID of the Payment Record.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "PaymentAttemptRecordService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[PaymentAttemptRecord]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        return cast(
            ListObject[PaymentAttemptRecord],
            self._request(
                "get",
                "/v1/payment_attempt_records",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "PaymentAttemptRecordService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[PaymentAttemptRecord]:
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        return cast(
            ListObject[PaymentAttemptRecord],
            await self._request_async(
                "get",
                "/v1/payment_attempt_records",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "PaymentAttemptRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PaymentAttemptRecord:
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        return cast(
            PaymentAttemptRecord,
            self._request(
                "get",
                "/v1/payment_attempt_records/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "PaymentAttemptRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> PaymentAttemptRecord:
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        return cast(
            PaymentAttemptRecord,
            await self._request_async(
                "get",
                "/v1/payment_attempt_records/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
