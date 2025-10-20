# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.issuing._credit_underwriting_record import (
        CreditUnderwritingRecord,
    )
    from stripe.params.issuing._credit_underwriting_record_correct_params import (
        CreditUnderwritingRecordCorrectParams,
    )
    from stripe.params.issuing._credit_underwriting_record_create_from_application_params import (
        CreditUnderwritingRecordCreateFromApplicationParams,
    )
    from stripe.params.issuing._credit_underwriting_record_create_from_proactive_review_params import (
        CreditUnderwritingRecordCreateFromProactiveReviewParams,
    )
    from stripe.params.issuing._credit_underwriting_record_list_params import (
        CreditUnderwritingRecordListParams,
    )
    from stripe.params.issuing._credit_underwriting_record_report_decision_params import (
        CreditUnderwritingRecordReportDecisionParams,
    )
    from stripe.params.issuing._credit_underwriting_record_retrieve_params import (
        CreditUnderwritingRecordRetrieveParams,
    )


class CreditUnderwritingRecordService(StripeService):
    def list(
        self,
        params: Optional["CreditUnderwritingRecordListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CreditUnderwritingRecord]":
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            "ListObject[CreditUnderwritingRecord]",
            self._request(
                "get",
                "/v1/issuing/credit_underwriting_records",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["CreditUnderwritingRecordListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[CreditUnderwritingRecord]":
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            "ListObject[CreditUnderwritingRecord]",
            await self._request_async(
                "get",
                "/v1/issuing/credit_underwriting_records",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        credit_underwriting_record: str,
        params: Optional["CreditUnderwritingRecordRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "get",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        credit_underwriting_record: str,
        params: Optional["CreditUnderwritingRecordRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "get",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def correct(
        self,
        credit_underwriting_record: str,
        params: Optional["CreditUnderwritingRecordCorrectParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def correct_async(
        self,
        credit_underwriting_record: str,
        params: Optional["CreditUnderwritingRecordCorrectParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_decision(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordReportDecisionParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_decision_async(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordReportDecisionParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_application(
        self,
        params: "CreditUnderwritingRecordCreateFromApplicationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_application_async(
        self,
        params: "CreditUnderwritingRecordCreateFromApplicationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_proactive_review(
        self,
        params: "CreditUnderwritingRecordCreateFromProactiveReviewParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_proactive_review_async(
        self,
        params: "CreditUnderwritingRecordCreateFromProactiveReviewParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                base_address="api",
                params=params,
                options=options,
            ),
        )
