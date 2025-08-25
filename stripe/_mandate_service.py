# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._mandate import Mandate
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class MandateService(StripeService):
    class ListParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        on_behalf_of: NotRequired[str]
        """
        The Stripe account ID that the mandates are intended for. Learn more about the [use case for connected accounts payments](https://stripe.com/docs/payments/connected-accounts).
        """
        payment_method: str
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: Literal["active", "inactive", "pending"]
        """
        The status of the mandates to retrieve. Status indicates whether or not you can use it to initiate a payment, and can have a value of `active`, `pending`, or `inactive`.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self, params: "MandateService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Mandate]:
        """
        Retrieves a list of Mandates for a given PaymentMethod.
        """
        return cast(
            ListObject[Mandate],
            self._request(
                "get",
                "/v1/mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self, params: "MandateService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Mandate]:
        """
        Retrieves a list of Mandates for a given PaymentMethod.
        """
        return cast(
            ListObject[Mandate],
            await self._request_async(
                "get",
                "/v1/mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        mandate: str,
        params: "MandateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Mandate:
        """
        Retrieves a Mandate object.
        """
        return cast(
            Mandate,
            self._request(
                "get",
                "/v1/mandates/{mandate}".format(mandate=sanitize_id(mandate)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        mandate: str,
        params: "MandateService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Mandate:
        """
        Retrieves a Mandate object.
        """
        return cast(
            Mandate,
            await self._request_async(
                "get",
                "/v1/mandates/{mandate}".format(mandate=sanitize_id(mandate)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
