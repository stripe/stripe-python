# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
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


class OnrampSession(
    CreateableAPIResource["OnrampSession"],
    ListableAPIResource["OnrampSession"],
):
    """
    A Crypto Onramp Session represents your customer's session as they purchase cryptocurrency through Stripe. Once payment is successful, Stripe will fulfill the delivery of cryptocurrency to your user's wallet and contain a reference to the crypto transaction ID.

    You can create an onramp session on your server and embed the widget on your frontend. Alternatively, you can redirect your users to the standalone hosted onramp.

    Related guide: [Integrate the onramp](https://docs.stripe.com/crypto/integrate-the-onramp)
    """

    OBJECT_NAME: ClassVar[Literal["crypto.onramp_session"]] = (
        "crypto.onramp_session"
    )

    class TransactionDetails(StripeObject):
        class Fees(StripeObject):
            network_fee_amount: Optional[str]
            """
            The cost associated with moving crypto from Stripe to the end consumer's wallet. e.g: for ETH, this is called 'gas fee', for BTC this is a 'miner's fee'.
            """
            transaction_fee_amount: Optional[str]
            """
            Fee for processing the transaction.
            """

        class WalletAddresses(StripeObject):
            class DestinationTags(StripeObject):
                stellar: Optional[str]
                """
                A stellar destination tag
                """

            avalanche: Optional[str]
            """
            An avalanche address
            """
            base_network: Optional[str]
            """
            A base address
            """
            bitcoin: Optional[str]
            """
            A bitcoin address
            """
            destination_tags: Optional[DestinationTags]
            """
            The end customer's crypto wallet destination tag (for each network) to use for this transaction.
            """
            ethereum: Optional[str]
            """
            An ethereum address
            """
            optimism: Optional[str]
            """
            An optimism address
            """
            polygon: Optional[str]
            """
            A polygon address
            """
            solana: Optional[str]
            """
            A solana address
            """
            stellar: Optional[str]
            """
            A stellar address
            """
            sui: Optional[str]
            """
            A Sui address
            """
            worldchain: Optional[str]
            """
            A worldchain address
            """
            _inner_class_types = {"destination_tags": DestinationTags}

        destination_amount: Optional[str]
        """
        The amount of crypto the customer will get deposited into their wallet
        """
        destination_currencies: Optional[
            List[
                Union[
                    Literal[
                        "avax",
                        "btc",
                        "eth",
                        "matic",
                        "sol",
                        "usdc",
                        "wld",
                        "xlm",
                    ],
                    str,
                ]
            ]
        ]
        """
        If a platform wants to lock the currencies an session will support, they can add supported currencies to this array. If left null, the experience will allow selection of all supported destination currencies.
        """
        destination_currency: Optional[
            Union[
                Literal[
                    "avax", "btc", "eth", "matic", "sol", "usdc", "wld", "xlm"
                ],
                str,
            ]
        ]
        """
        The selected `destination_currency` to convert the `source` to. This should be a crypto currency code. If `destination_currencies` is set, it must be a value in that array.
        """
        destination_network: Optional[
            Union[
                Literal[
                    "avalanche",
                    "base",
                    "bitcoin",
                    "ethereum",
                    "optimism",
                    "polygon",
                    "solana",
                    "stellar",
                    "sui",
                    "worldchain",
                ],
                str,
            ]
        ]
        """
        The specific crypto network the `destination_currency` is settled on. If `destination_networks` is set, it must be a value in that array.
        """
        destination_networks: Optional[
            List[
                Union[
                    Literal[
                        "avalanche",
                        "base",
                        "bitcoin",
                        "ethereum",
                        "optimism",
                        "polygon",
                        "solana",
                        "stellar",
                        "sui",
                        "worldchain",
                    ],
                    str,
                ]
            ]
        ]
        """
        If a platform wants to lock the supported networks, they can do so through this array. If left null, the experience will allow selection of all supported networks.
        """
        fees: Optional[Fees]
        """
        Details about the fees associated with this transaction
        """
        lock_wallet_address: Optional[bool]
        """
        Whether or not to lock the suggested wallet address.
        """
        settlement_speed: Optional[Union[Literal["instant", "standard"], str]]
        """
        Speed at which the cryptocurrency is delivered to the wallet
        One of:
         `instant` (default): crypto is delivered when payment is confirmed
         `standard`: crypto is delivered when payment settles
        """
        source_amount: Optional[str]
        """
        The amount of fiat we intend to onramp - excluding fees
        """
        source_currency: Optional[Union[Literal["eur", "gbp", "usd"], str]]
        """
        A fiat currency code
        """
        transaction_id: Optional[str]
        """
        The on-chain transaction hash (also referred to as transaction ID or tx_hash) of the transaction that was sent to the customer's wallet. The format varies by chain (e.g. `0xc257...1a95` on Ethereum, `5UB1...v3xZ` on Solana, or `a1b2...bf00` on Bitcoin). This will only be set if the session reaches `status=fulfillment_complete` and we've transferred the crypto successfully to the external wallet.
        """
        wallet_address: Optional[str]
        """
        The consumer's wallet address (where crypto will be sent to)
        """
        wallet_addresses: Optional[WalletAddresses]
        """
        The end customer's crypto wallet address (for each network) to use for this transaction.
        """
        _inner_class_types = {
            "fees": Fees,
            "wallet_addresses": WalletAddresses,
        }

    client_secret: str
    """
    A client secret that can be used to drive a single session using our embedded widget.

    Related guide: [Set up an onramp integration](https://docs.stripe.com/crypto/integrate-the-onramp)
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    kyc_details_provided: bool
    """
    Has the value `true` if any user kyc details were provided during the creation of the onramp session. Otherwise, has the value `false`.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["crypto.onramp_session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    redirect_url: Optional[str]
    """
    Redirect your users to the URL for a prebuilt frontend integration of the crypto onramp on the standalone hosted onramp.

    Related guide: [Mint a session with a redirect url](https://docs.stripe.com/crypto/standalone-hosted-onramp#mint-a-session-with-a-redirect-url)
    """
    status: str
    """
    The status of the Onramp Session. One of = `{initialized, rejected, requires_payment, fulfillment_processing, fulfillment_complete}`
    """
    transaction_details: TransactionDetails

    @classmethod
    def _cls_checkout(
        cls, id: str, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        return cast(
            "OnrampSession",
            cls._static_request(
                "post",
                "/v1/crypto/onramp_sessions/{id}/checkout".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def checkout(
        id: str, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        ...

    @overload
    def checkout(
        self, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        ...

    @class_method_variant("_cls_checkout")
    def checkout(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OnrampSessionCheckoutParams"]
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
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_checkout_async(
        cls, id: str, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        return cast(
            "OnrampSession",
            await cls._static_request_async(
                "post",
                "/v1/crypto/onramp_sessions/{id}/checkout".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def checkout_async(
        id: str, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        ...

    @overload
    async def checkout_async(
        self, **params: Unpack["OnrampSessionCheckoutParams"]
    ) -> "OnrampSession":
        """
        Completes a headless CryptoOnrampSession.

        This method will attempt to confirm the payment and execute the quote to deliver the crypto to the customer.
        """
        ...

    @class_method_variant("_cls_checkout_async")
    async def checkout_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OnrampSessionCheckoutParams"]
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
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(
        cls, **params: Unpack["OnrampSessionCreateParams"]
    ) -> "OnrampSession":
        """
        Creates a CryptoOnrampSession object.

        After the CryptoOnrampSession is created, display the onramp session modal using the client_secret.

        Related guide: [Set up an onramp integration](https://docs.stripe.com/docs/crypto/integrate-the-onramp)
        """
        return cast(
            "OnrampSession",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["OnrampSessionCreateParams"]
    ) -> "OnrampSession":
        """
        Creates a CryptoOnrampSession object.

        After the CryptoOnrampSession is created, display the onramp session modal using the client_secret.

        Related guide: [Set up an onramp integration](https://docs.stripe.com/docs/crypto/integrate-the-onramp)
        """
        return cast(
            "OnrampSession",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["OnrampSessionListParams"]
    ) -> ListObject["OnrampSession"]:
        """
        Returns a list of onramp sessions that match the filter criteria. The onramp sessions are returned in sorted order, with the most recent onramp sessions appearing first.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["OnrampSessionListParams"]
    ) -> ListObject["OnrampSession"]:
        """
        Returns a list of onramp sessions that match the filter criteria. The onramp sessions are returned in sorted order, with the most recent onramp sessions appearing first.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_quote(
        cls, id: str, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            cls._static_request(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def quote(
        id: str, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        ...

    @overload
    def quote(
        self, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        ...

    @class_method_variant("_cls_quote")
    def quote(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            self._request(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_quote_async(
        cls, id: str, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            await cls._static_request_async(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def quote_async(
        id: str, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        ...

    @overload
    async def quote_async(
        self, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        ...

    @class_method_variant("_cls_quote_async")
    async def quote_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OnrampSessionQuoteParams"]
    ) -> "OnrampSession":
        """
        Refreshes an executable quote for a CryptoOnrampSession.
        """
        return cast(
            "OnrampSession",
            await self._request_async(
                "post",
                "/v1/crypto/onramp_sessions/{id}/quote".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["OnrampSessionRetrieveParams"]
    ) -> "OnrampSession":
        """
        Retrieves the details of a CryptoOnrampSession that was previously created.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["OnrampSessionRetrieveParams"]
    ) -> "OnrampSession":
        """
        Retrieves the details of a CryptoOnrampSession that was previously created.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"transaction_details": TransactionDetails}
