# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.billing._feedback_option import FeedbackOption
    from stripe.params.billing._feedback_option_create_params import (
        FeedbackOptionCreateParams,
    )
    from stripe.params.billing._feedback_option_deactivate_params import (
        FeedbackOptionDeactivateParams,
    )
    from stripe.params.billing._feedback_option_list_params import (
        FeedbackOptionListParams,
    )
    from stripe.params.billing._feedback_option_retrieve_params import (
        FeedbackOptionRetrieveParams,
    )
    from stripe.params.billing._feedback_option_update_params import (
        FeedbackOptionUpdateParams,
    )


class FeedbackOptionService(StripeService):
    def list(
        self,
        params: Optional["FeedbackOptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeedbackOption]":
        """
        Returns a list of your feedback options.
        """
        return cast(
            "ListObject[FeedbackOption]",
            self._request(
                "get",
                "/v1/billing/feedback_options",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FeedbackOptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeedbackOption]":
        """
        Returns a list of your feedback options.
        """
        return cast(
            "ListObject[FeedbackOption]",
            await self._request_async(
                "get",
                "/v1/billing/feedback_options",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FeedbackOptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Creates a new feedback option.
        """
        return cast(
            "FeedbackOption",
            self._request(
                "post",
                "/v1/billing/feedback_options",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FeedbackOptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Creates a new feedback option.
        """
        return cast(
            "FeedbackOption",
            await self._request_async(
                "post",
                "/v1/billing/feedback_options",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FeedbackOptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Retrieves a feedback option object given an ID.
        """
        return cast(
            "FeedbackOption",
            self._request(
                "get",
                "/v1/billing/feedback_options/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["FeedbackOptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Retrieves a feedback option object given an ID.
        """
        return cast(
            "FeedbackOption",
            await self._request_async(
                "get",
                "/v1/billing/feedback_options/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["FeedbackOptionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Updates the description of an existing feedback option.
        """
        return cast(
            "FeedbackOption",
            self._request(
                "post",
                "/v1/billing/feedback_options/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["FeedbackOptionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Updates the description of an existing feedback option.
        """
        return cast(
            "FeedbackOption",
            await self._request_async(
                "post",
                "/v1/billing/feedback_options/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def deactivate(
        self,
        id: str,
        params: Optional["FeedbackOptionDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            self._request(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def deactivate_async(
        self,
        id: str,
        params: Optional["FeedbackOptionDeactivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            await self._request_async(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
