# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.crypto._onramp_session import OnrampSession
    from stripe.params.crypto._onramp_session_checkout_params import (
        OnrampSessionCheckoutParams,
    )
    from stripe.params.crypto._onramp_session_create_params import (
        OnrampSessionCreateParams,
    )
    from stripe.params.crypto._onramp_session_list_params import (
        OnrampSessionListParams,
    )
    from stripe.params.crypto._onramp_session_quote_params import (
        OnrampSessionQuoteParams,
    )
    from stripe.params.crypto._onramp_session_retrieve_params import (
        OnrampSessionRetrieveParams,
    )


class OnrampSessionService(StripeService):
    def list(
        self,
        params: Optional["OnrampSessionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OnrampSession]":
        """
        Returns a list of onramp sessions that match the filter criteria. The onramp sessions are returned in sorted order, with the most recent onramp sessions appearing first.
        """
        return cast(
            "ListObject[OnrampSession]",
            self._request(
                "get",
                "/v1/crypto/onramp_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OnrampSessionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[OnrampSession]":
        """
        Returns a list of onramp sessions that match the filter criteria. The onramp sessions are returned in sorted order, with the most recent onramp sessions appearing first.
        """
        return cast(
            "ListObject[OnrampSession]",
            await self._request_async(
                "get",
                "/v1/crypto/onramp_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: Optional["OnrampSessionCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Creates a CryptoOnrampSession object.

        After the CryptoOnrampSession is created, display the onramp session modal using the client_secret.

        Related guide: [Set up an onramp integration](https://docs.stripe.com/docs/crypto/integrate-the-onramp)
        """
        return cast(
            "OnrampSession",
            self._request(
                "post",
                "/v1/crypto/onramp_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["OnrampSessionCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Creates a CryptoOnrampSession object.

        After the CryptoOnrampSession is created, display the onramp session modal using the client_secret.

        Related guide: [Set up an onramp integration](https://docs.stripe.com/docs/crypto/integrate-the-onramp)
        """
        return cast(
            "OnrampSession",
            await self._request_async(
                "post",
                "/v1/crypto/onramp_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OnrampSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Retrieves the details of a CryptoOnrampSession that was previously created.
        """
        return cast(
            "OnrampSession",
            self._request(
                "get",
                "/v1/crypto/onramp_sessions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["OnrampSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Retrieves the details of a CryptoOnrampSession that was previously created.
        """
        return cast(
            "OnrampSession",
            await self._request_async(
                "get",
                "/v1/crypto/onramp_sessions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def checkout(
        self,
        id: str,
        params: Optional["OnrampSessionCheckoutParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        return cast(
            "OnrampSession",
            self._request(
                "post",
                "/v1/crypto/onramp_sessions/{id}/checkout".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def checkout_async(
        self,
        id: str,
        params: Optional["OnrampSessionCheckoutParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        return cast(
            "OnrampSession",
            await self._request_async(
                "post",
                "/v1/crypto/onramp_sessions/{id}/checkout".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def quote(
        self,
        id: str,
        params: Optional["OnrampSessionQuoteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            self._request(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def quote_async(
        self,
        id: str,
        params: Optional["OnrampSessionQuoteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            await self._request_async(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
