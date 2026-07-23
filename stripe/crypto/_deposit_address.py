# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.crypto._deposit_address_create_params import (
        DepositAddressCreateParams,
    )
    from stripe.params.crypto._deposit_address_list_params import (
        DepositAddressListParams,
    )
    from stripe.params.crypto._deposit_address_retrieve_params import (
        DepositAddressRetrieveParams,
    )


class DepositAddress(
    CreateableAPIResource["DepositAddress"],
    ListableAPIResource["DepositAddress"],
):
    """
    A crypto deposit address is a blockchain address that can be used by a merchant for deposit mode crypto payments.
    """

    OBJECT_NAME: ClassVar[Literal["crypto.deposit_address"]] = (
        "crypto.deposit_address"
    )

    class SupportedToken(StripeObject):
        token_contract_address: str
        """
        The on-chain contract address for the supported token currency on this specific network.
        """
        token_currency: Literal["usdc"]
        """
        The supported token currency. Supported token currencies include: `usdc`.
        """

    address: str
    created: int
    customer: Optional[str]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    metadata: UntypedStripeObject[str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network: Literal["base", "solana", "tempo"]
    object: Literal["crypto.deposit_address"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    supported_tokens: List[SupportedToken]

    @classmethod
    def create(
        cls, **params: Unpack["DepositAddressCreateParams"]
    ) -> "DepositAddress":
        """
        Creates a new crypto deposit address for the authenticated merchant on the specified network.
        The returned address can be used across multiple PaymentIntents.
        """
        return cast(
            "DepositAddress",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["DepositAddressCreateParams"]
    ) -> "DepositAddress":
        """
        Creates a new crypto deposit address for the authenticated merchant on the specified network.
        The returned address can be used across multiple PaymentIntents.
        """
        return cast(
            "DepositAddress",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["DepositAddressListParams"]
    ) -> ListObject["DepositAddress"]:
        """
        Lists crypto deposit addresses for the authenticated merchant.
        Supports cursor-based pagination and optional filtering by customer, network, or on-chain address.
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
        cls, **params: Unpack["DepositAddressListParams"]
    ) -> ListObject["DepositAddress"]:
        """
        Lists crypto deposit addresses for the authenticated merchant.
        Supports cursor-based pagination and optional filtering by customer, network, or on-chain address.
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
    def retrieve(
        cls, id: str, **params: Unpack["DepositAddressRetrieveParams"]
    ) -> "DepositAddress":
        """
        Retrieves the details of an existing crypto deposit address by ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["DepositAddressRetrieveParams"]
    ) -> "DepositAddress":
        """
        Retrieves the details of an existing crypto deposit address by ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/crypto/deposit_addresses"

    _inner_class_types = {"supported_tokens": SupportedToken}
