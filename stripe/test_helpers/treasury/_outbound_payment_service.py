# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.treasury._outbound_payment import OutboundPayment
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundPaymentService(StripeService):
    class FailParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class PostParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReturnOutboundPaymentParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        returned_details: NotRequired[
            "OutboundPaymentService.ReturnOutboundPaymentParamsReturnedDetails"
        ]
        """
        Optional hash to set the the return code.
        """

    class ReturnOutboundPaymentParamsReturnedDetails(TypedDict):
        code: NotRequired[
            "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'declined', 'incorrect_account_holder_name', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']"
        ]
        """
        The return code to be set on the OutboundPayment object.
        """

    def fail(
        self,
        id: str,
        params: "OutboundPaymentService.FailParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Transitions a test mode created OutboundPayment to the failed status. The OutboundPayment must already be in the processing state.
        """
        return cast(
            OutboundPayment,
            self._requestor.request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def post(
        self,
        id: str,
        params: "OutboundPaymentService.PostParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Transitions a test mode created OutboundPayment to the posted status. The OutboundPayment must already be in the processing state.
        """
        return cast(
            OutboundPayment,
            self._requestor.request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def return_outbound_payment(
        self,
        id: str,
        params: "OutboundPaymentService.ReturnOutboundPaymentParams" = {},
        options: RequestOptions = {},
    ) -> OutboundPayment:
        """
        Transitions a test mode created OutboundPayment to the returned status. The OutboundPayment must already be in the processing state.
        """
        return cast(
            OutboundPayment,
            self._requestor.request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
