# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._gift_card import GiftCard
    from stripe._gift_card_operation import GiftCardOperation
    from stripe._request_options import RequestOptions
    from stripe.params._gift_card_activate_params import GiftCardActivateParams
    from stripe.params._gift_card_cashout_params import GiftCardCashoutParams
    from stripe.params._gift_card_check_balance_params import (
        GiftCardCheckBalanceParams,
    )
    from stripe.params._gift_card_create_params import GiftCardCreateParams
    from stripe.params._gift_card_reload_params import GiftCardReloadParams
    from stripe.params._gift_card_retrieve_params import GiftCardRetrieveParams
    from stripe.params._gift_card_void_operation_params import (
        GiftCardVoidOperationParams,
    )


class GiftCardService(StripeService):
    def retrieve(
        self,
        gift_card: str,
        params: Optional["GiftCardRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCard":
        """
        Retrieves a third-party gift card object.
        """
        return cast(
            "GiftCard",
            self._request(
                "get",
                "/v1/gift_cards/{gift_card}".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        gift_card: str,
        params: Optional["GiftCardRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCard":
        """
        Retrieves a third-party gift card object.
        """
        return cast(
            "GiftCard",
            await self._request_async(
                "get",
                "/v1/gift_cards/{gift_card}".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "GiftCardCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCard":
        """
        Creates a gift card object.
        """
        return cast(
            "GiftCard",
            self._request(
                "post",
                "/v1/gift_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "GiftCardCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCard":
        """
        Creates a gift card object.
        """
        return cast(
            "GiftCard",
            await self._request_async(
                "post",
                "/v1/gift_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def activate(
        self,
        gift_card: str,
        params: Optional["GiftCardActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{gift_card}/activate".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def activate_async(
        self,
        gift_card: str,
        params: Optional["GiftCardActivateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{gift_card}/activate".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cashout(
        self,
        gift_card: str,
        params: Optional["GiftCardCashoutParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{gift_card}/cashout".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cashout_async(
        self,
        gift_card: str,
        params: Optional["GiftCardCashoutParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{gift_card}/cashout".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def check_balance(
        self,
        gift_card: str,
        params: Optional["GiftCardCheckBalanceParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{gift_card}/check_balance".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def check_balance_async(
        self,
        gift_card: str,
        params: Optional["GiftCardCheckBalanceParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{gift_card}/check_balance".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reload(
        self,
        gift_card: str,
        params: "GiftCardReloadParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{gift_card}/reload".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reload_async(
        self,
        gift_card: str,
        params: "GiftCardReloadParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{gift_card}/reload".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def void_operation(
        self,
        gift_card: str,
        params: "GiftCardVoidOperationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{gift_card}/void_operation".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def void_operation_async(
        self,
        gift_card: str,
        params: "GiftCardVoidOperationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{gift_card}/void_operation".format(
                    gift_card=sanitize_id(gift_card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
