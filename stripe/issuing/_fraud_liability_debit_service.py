# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.issuing._fraud_liability_debit import FraudLiabilityDebit
    from stripe.params.issuing._fraud_liability_debit_list_params import (
        FraudLiabilityDebitListParams,
    )
    from stripe.params.issuing._fraud_liability_debit_retrieve_params import (
        FraudLiabilityDebitRetrieveParams,
    )


class FraudLiabilityDebitService(StripeService):
    def list(
        self,
        params: Optional["FraudLiabilityDebitListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FraudLiabilityDebit]":
        """
        Returns a list of Issuing FraudLiabilityDebit objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            "ListObject[FraudLiabilityDebit]",
            self._request(
                "get",
                "/v1/issuing/fraud_liability_debits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FraudLiabilityDebitListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FraudLiabilityDebit]":
        """
        Returns a list of Issuing FraudLiabilityDebit objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            "ListObject[FraudLiabilityDebit]",
            await self._request_async(
                "get",
                "/v1/issuing/fraud_liability_debits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        fraud_liability_debit: str,
        params: Optional["FraudLiabilityDebitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FraudLiabilityDebit":
        """
        Retrieves an Issuing FraudLiabilityDebit object.
        """
        return cast(
            "FraudLiabilityDebit",
            self._request(
                "get",
                "/v1/issuing/fraud_liability_debits/{fraud_liability_debit}".format(
                    fraud_liability_debit=sanitize_id(fraud_liability_debit),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        fraud_liability_debit: str,
        params: Optional["FraudLiabilityDebitRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FraudLiabilityDebit":
        """
        Retrieves an Issuing FraudLiabilityDebit object.
        """
        return cast(
            "FraudLiabilityDebit",
            await self._request_async(
                "get",
                "/v1/issuing/fraud_liability_debits/{fraud_liability_debit}".format(
                    fraud_liability_debit=sanitize_id(fraud_liability_debit),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
