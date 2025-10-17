# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._recipient_verification_acknowledge_params import (
        RecipientVerificationAcknowledgeParams,
    )
    from stripe.params.v2.money_management._recipient_verification_create_params import (
        RecipientVerificationCreateParams,
    )
    from stripe.params.v2.money_management._recipient_verification_retrieve_params import (
        RecipientVerificationRetrieveParams,
    )
    from stripe.v2.money_management._recipient_verification import (
        RecipientVerification,
    )


class RecipientVerificationService(StripeService):
    def create(
        self,
        params: "RecipientVerificationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Creates a RecipientVerification to verify the recipient you intend to send funds to.
        """
        return cast(
            "RecipientVerification",
            self._request(
                "post",
                "/v2/money_management/recipient_verifications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RecipientVerificationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Creates a RecipientVerification to verify the recipient you intend to send funds to.
        """
        return cast(
            "RecipientVerification",
            await self._request_async(
                "post",
                "/v2/money_management/recipient_verifications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["RecipientVerificationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Retrieves the details of an existing RecipientVerification by passing the unique RecipientVerification ID.
        """
        return cast(
            "RecipientVerification",
            self._request(
                "get",
                "/v2/money_management/recipient_verifications/{id}".format(
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
        params: Optional["RecipientVerificationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Retrieves the details of an existing RecipientVerification by passing the unique RecipientVerification ID.
        """
        return cast(
            "RecipientVerification",
            await self._request_async(
                "get",
                "/v2/money_management/recipient_verifications/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def acknowledge(
        self,
        id: str,
        params: Optional["RecipientVerificationAcknowledgeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Acknowledges an existing RecipientVerification. Only RecipientVerification awaiting acknowledgement can be acknowledged.
        """
        return cast(
            "RecipientVerification",
            self._request(
                "post",
                "/v2/money_management/recipient_verifications/{id}/acknowledge".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def acknowledge_async(
        self,
        id: str,
        params: Optional["RecipientVerificationAcknowledgeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RecipientVerification":
        """
        Acknowledges an existing RecipientVerification. Only RecipientVerification awaiting acknowledgement can be acknowledged.
        """
        return cast(
            "RecipientVerification",
            await self._request_async(
                "post",
                "/v2/money_management/recipient_verifications/{id}/acknowledge".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
