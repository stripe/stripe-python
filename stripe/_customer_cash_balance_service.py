# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._cash_balance import CashBalance
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerCashBalanceService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        settings: NotRequired[
            "CustomerCashBalanceService.UpdateParamsSettings"
        ]
        """
        A hash of settings for this cash balance.
        """

    class UpdateParamsSettings(TypedDict):
        reconciliation_mode: NotRequired[
            "Literal['automatic', 'manual', 'merchant_default']"
        ]
        """
        Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://stripe.com/docs/payments/customer-balance/reconciliation).
        """

    def retrieve(
        self,
        customer: str,
        params: "CustomerCashBalanceService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CashBalance:
        """
        Retrieves a customer's cash balance.
        """
        return cast(
            CashBalance,
            self._requestor.request(
                "get",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=_util.sanitize_id(customer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        customer: str,
        params: "CustomerCashBalanceService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CashBalance:
        """
        Changes the settings on a customer's cash balance.
        """
        return cast(
            CashBalance,
            self._requestor.request(
                "post",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=_util.sanitize_id(customer),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
