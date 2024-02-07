# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.gift_cards._transaction import Transaction
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class TransactionService(StripeService):
    class CancelParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ConfirmParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(TypedDict):
        amount: int
        """
        The amount of the transaction. A negative amount deducts funds, and a positive amount adds funds.
        """
        confirm: NotRequired["bool"]
        """
        Whether this is a confirmed transaction. A confirmed transaction immediately deducts from/adds to the `amount_available` on the gift card. Otherwise, it creates a held transaction that increments the `amount_held` on the gift card.
        """
        created_by: NotRequired["TransactionService.CreateParamsCreatedBy"]
        """
        Related objects which created this transaction.
        """
        currency: str
        """
        The currency of the transaction. This must match the currency of the gift card.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        gift_card: str
        """
        The gift card to create a new transaction on.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        transfer_group: NotRequired["str"]
        """
        A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
        """

    class CreateParamsCreatedBy(TypedDict):
        payment: "TransactionService.CreateParamsCreatedByPayment"
        """
        The details for the payment that created this object.
        """
        type: Literal["payment"]
        """
        The type of event that created this object.
        """

    class CreateParamsCreatedByPayment(TypedDict):
        payment_intent: str
        """
        The PaymentIntent used to collect payment for this object.
        """

    class ListParams(TypedDict):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        gift_card: NotRequired["str"]
        """
        The gift card to list transactions for.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        transfer_group: NotRequired["str"]
        """
        A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    def list(
        self,
        params: "TransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Transaction]:
        """
        List gift card transactions for a gift card
        """
        return cast(
            ListObject[Transaction],
            self._request(
                "get",
                "/v1/gift_cards/transactions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "TransactionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Transaction]:
        """
        List gift card transactions for a gift card
        """
        return cast(
            ListObject[Transaction],
            await self._request_async(
                "get",
                "/v1/gift_cards/transactions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "TransactionService.CreateParams",
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Create a gift card transaction
        """
        return cast(
            Transaction,
            self._request(
                "post",
                "/v1/gift_cards/transactions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "TransactionService.CreateParams",
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Create a gift card transaction
        """
        return cast(
            Transaction,
            await self._request_async(
                "post",
                "/v1/gift_cards/transactions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "TransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Retrieves the gift card transaction.
        """
        return cast(
            Transaction,
            self._request(
                "get",
                "/v1/gift_cards/transactions/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "TransactionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Retrieves the gift card transaction.
        """
        return cast(
            Transaction,
            await self._request_async(
                "get",
                "/v1/gift_cards/transactions/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "TransactionService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Update a gift card transaction
        """
        return cast(
            Transaction,
            self._request(
                "post",
                "/v1/gift_cards/transactions/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "TransactionService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Update a gift card transaction
        """
        return cast(
            Transaction,
            await self._request_async(
                "post",
                "/v1/gift_cards/transactions/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "TransactionService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Cancel a gift card transaction
        """
        return cast(
            Transaction,
            self._request(
                "post",
                "/v1/gift_cards/transactions/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "TransactionService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Cancel a gift card transaction
        """
        return cast(
            Transaction,
            await self._request_async(
                "post",
                "/v1/gift_cards/transactions/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def confirm(
        self,
        id: str,
        params: "TransactionService.ConfirmParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Confirm a gift card transaction
        """
        return cast(
            Transaction,
            self._request(
                "post",
                "/v1/gift_cards/transactions/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_async(
        self,
        id: str,
        params: "TransactionService.ConfirmParams" = {},
        options: RequestOptions = {},
    ) -> Transaction:
        """
        Confirm a gift card transaction
        """
        return cast(
            Transaction,
            await self._request_async(
                "post",
                "/v1/gift_cards/transactions/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
