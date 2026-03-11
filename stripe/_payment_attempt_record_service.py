# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._payment_attempt_record import PaymentAttemptRecord
    from stripe._request_options import RequestOptions
    from stripe.params._payment_attempt_record_list_params import (
        PaymentAttemptRecordListParams,
    )
    from stripe.params._payment_attempt_record_report_authenticated_params import (
        PaymentAttemptRecordReportAuthenticatedParams,
    )
    from stripe.params._payment_attempt_record_report_canceled_params import (
        PaymentAttemptRecordReportCanceledParams,
    )
    from stripe.params._payment_attempt_record_report_failed_params import (
        PaymentAttemptRecordReportFailedParams,
    )
    from stripe.params._payment_attempt_record_report_guaranteed_params import (
        PaymentAttemptRecordReportGuaranteedParams,
    )
    from stripe.params._payment_attempt_record_report_informational_params import (
        PaymentAttemptRecordReportInformationalParams,
    )
    from stripe.params._payment_attempt_record_report_refund_params import (
        PaymentAttemptRecordReportRefundParams,
    )
    from stripe.params._payment_attempt_record_retrieve_params import (
        PaymentAttemptRecordRetrieveParams,
    )


class PaymentAttemptRecordService(StripeService):
    def list(
        self,
        params: "PaymentAttemptRecordListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentAttemptRecord]":
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        return cast(
            "ListObject[PaymentAttemptRecord]",
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
        params: "PaymentAttemptRecordListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentAttemptRecord]":
        """
        List all the Payment Attempt Records attached to the specified Payment Record.
        """
        return cast(
            "ListObject[PaymentAttemptRecord]",
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
        params: Optional["PaymentAttemptRecordRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        return cast(
            "PaymentAttemptRecord",
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
        params: Optional["PaymentAttemptRecordRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Retrieves a Payment Attempt Record with the given ID
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "get",
                "/v1/payment_attempt_records/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_authenticated(
        self,
        payment_attempt_record: str,
        params: Optional[
            "PaymentAttemptRecordReportAuthenticatedParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was authenticated.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_authenticated".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_authenticated_async(
        self,
        payment_attempt_record: str,
        params: Optional[
            "PaymentAttemptRecordReportAuthenticatedParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was authenticated.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_authenticated".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_canceled(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportCanceledParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was canceled.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_canceled".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_canceled_async(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportCanceledParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was canceled.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_canceled".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_failed(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportFailedParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record failed.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_failed".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_failed_async(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportFailedParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record failed.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_failed".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_guaranteed(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportGuaranteedParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was guaranteed.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_guaranteed".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_guaranteed_async(
        self,
        payment_attempt_record: str,
        params: Optional["PaymentAttemptRecordReportGuaranteedParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was guaranteed.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_guaranteed".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_informational(
        self,
        payment_attempt_record: str,
        params: Optional[
            "PaymentAttemptRecordReportInformationalParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report informational updates on the specified Payment Attempt Record.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_informational".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_informational_async(
        self,
        payment_attempt_record: str,
        params: Optional[
            "PaymentAttemptRecordReportInformationalParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report informational updates on the specified Payment Attempt Record.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_informational".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_refund(
        self,
        payment_attempt_record: str,
        params: "PaymentAttemptRecordReportRefundParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was refunded.
        """
        return cast(
            "PaymentAttemptRecord",
            self._request(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_refund".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_refund_async(
        self,
        payment_attempt_record: str,
        params: "PaymentAttemptRecordReportRefundParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentAttemptRecord":
        """
        Report that the specified Payment Attempt Record was refunded.
        """
        return cast(
            "PaymentAttemptRecord",
            await self._request_async(
                "post",
                "/v1/payment_attempt_records/{payment_attempt_record}/report_refund".format(
                    payment_attempt_record=sanitize_id(payment_attempt_record),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
