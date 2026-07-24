# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._received_debit_mandate_cancel_params import (
        ReceivedDebitMandateCancelParams,
    )
    from stripe.params.v2.money_management._received_debit_mandate_list_params import (
        ReceivedDebitMandateListParams,
    )
    from stripe.params.v2.money_management._received_debit_mandate_retrieve_params import (
        ReceivedDebitMandateRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._received_debit_mandate import (
        ReceivedDebitMandate,
    )


class ReceivedDebitMandateService(StripeService):
    def list(
        self,
        params: Optional["ReceivedDebitMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ReceivedDebitMandate]":
        """
        Returns a list of ReceivedDebitMandates.
        """
        return cast(
            "ListObject[ReceivedDebitMandate]",
            self._request(
                "get",
                "/v2/money_management/received_debit_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ReceivedDebitMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ReceivedDebitMandate]":
        """
        Returns a list of ReceivedDebitMandates.
        """
        return cast(
            "ListObject[ReceivedDebitMandate]",
            await self._request_async(
                "get",
                "/v2/money_management/received_debit_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ReceivedDebitMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedDebitMandate":
        """
        Retrieves the details of an existing ReceivedDebitMandate.
        """
        return cast(
            "ReceivedDebitMandate",
            self._request(
                "get",
                "/v2/money_management/received_debit_mandates/{id}".format(
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
        params: Optional["ReceivedDebitMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedDebitMandate":
        """
        Retrieves the details of an existing ReceivedDebitMandate.
        """
        return cast(
            "ReceivedDebitMandate",
            await self._request_async(
                "get",
                "/v2/money_management/received_debit_mandates/{id}".format(
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
        params: Optional["ReceivedDebitMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedDebitMandate":
        """
        Cancels an active ReceivedDebitMandate.
        """
        return cast(
            "ReceivedDebitMandate",
            self._request(
                "post",
                "/v2/money_management/received_debit_mandates/{id}/cancel".format(
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
        params: Optional["ReceivedDebitMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedDebitMandate":
        """
        Cancels an active ReceivedDebitMandate.
        """
        return cast(
            "ReceivedDebitMandate",
            await self._request_async(
                "post",
                "/v2/money_management/received_debit_mandates/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
