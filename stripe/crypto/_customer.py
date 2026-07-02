# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._list_object import ListObject
from stripe._nested_resource_class_methods import nested_resource_class_methods
from stripe._stripe_object import StripeObject
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.crypto._customer_consumer_wallet import CustomerConsumerWallet
    from stripe.crypto._customer_payment_token import CustomerPaymentToken
    from stripe.params.crypto._customer_list_crypto_consumer_wallets_params import (
        CustomerListCryptoConsumerWalletsParams,
    )
    from stripe.params.crypto._customer_list_payment_tokens_params import (
        CustomerListPaymentTokensParams,
    )
    from stripe.params.crypto._customer_retrieve_params import (
        CustomerRetrieveParams,
    )


@nested_resource_class_methods("crypto_consumer_wallet")
@nested_resource_class_methods("payment_token")
class Customer(APIResource["Customer"]):
    """
    This object represents a crypto onramp customer. Use it to get their kyc status and payment methods.
    """

    OBJECT_NAME: ClassVar[Literal["crypto.customer"]] = "crypto.customer"

    class KycTier(StripeObject):
        tier: Literal["l0", "l1", "l2"]
        """
        The KYC tier level (e.g., l0, l1, l2).
        """
        verification_errors: List[
            Literal[
                "id_document_verification_failed",
                "phone_verification_failed",
                "user_has_reached_max_verification_attempts",
            ]
        ]
        """
        List of errors associated with this KYC tier verification.
        """
        verification_status: Literal[
            "not_available", "not_started", "pending", "rejected", "verified"
        ]
        """
        The verification status for this KYC tier.
        """

    class Verification(StripeObject):
        errors: List[
            Literal[
                "id_document_verification_failed",
                "phone_verification_failed",
                "user_has_reached_max_verification_attempts",
            ]
        ]
        """
        List of errors associated with the verification.
        """
        name: Literal["id_document_verified", "kyc_verified", "phone_verified"]
        """
        Type of verification.
        """
        status: Literal[
            "not_available", "not_started", "pending", "rejected", "verified"
        ]
        """
        Outcome of the verification.
        """

    id: str
    """
    Unique identifier for the object.
    """
    kyc_region: Optional[Literal["eu", "us"]]
    """
    The KYC region determined by the customer's address country.
    """
    kyc_tiers: List[KycTier]
    """
    List of KYC tiers and their verification status.
    """
    object: Literal["crypto.customer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    provided_fields: List[
        Literal[
            "address_city",
            "address_country",
            "address_line_1",
            "address_line_2",
            "address_postal_code",
            "address_state",
            "attestation",
            "birth_city",
            "birth_country",
            "dob",
            "first_name",
            "id_document",
            "id_number",
            "id_type",
            "identifiers",
            "last_name",
            "nationalities",
            "selfie",
        ]
    ]
    """
    The set of KYC Fields provided for this customers.
    """
    verifications: List[Verification]
    """
    List of verifications and their outcome.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["CustomerRetrieveParams"]
    ) -> "Customer":
        """
        Retrieves the details of a Crypto Customer.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["CustomerRetrieveParams"]
    ) -> "Customer":
        """
        Retrieves the details of a Crypto Customer.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def list_crypto_consumer_wallets(
        cls,
        id: str,
        **params: Unpack["CustomerListCryptoConsumerWalletsParams"],
    ) -> ListObject["CustomerConsumerWallet"]:
        """
        Lists the Consumer Wallets for a Crypto Customer.
        """
        return cast(
            ListObject["CustomerConsumerWallet"],
            cls._static_request(
                "get",
                "/v1/crypto/customers/{id}/crypto_consumer_wallets".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @classmethod
    async def list_crypto_consumer_wallets_async(
        cls,
        id: str,
        **params: Unpack["CustomerListCryptoConsumerWalletsParams"],
    ) -> ListObject["CustomerConsumerWallet"]:
        """
        Lists the Consumer Wallets for a Crypto Customer.
        """
        return cast(
            ListObject["CustomerConsumerWallet"],
            await cls._static_request_async(
                "get",
                "/v1/crypto/customers/{id}/crypto_consumer_wallets".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @classmethod
    def list_payment_tokens(
        cls, id: str, **params: Unpack["CustomerListPaymentTokensParams"]
    ) -> ListObject["CustomerPaymentToken"]:
        """
        Lists the Payment Tokens for a Crypto Customer.
        """
        return cast(
            ListObject["CustomerPaymentToken"],
            cls._static_request(
                "get",
                "/v1/crypto/customers/{id}/payment_tokens".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @classmethod
    async def list_payment_tokens_async(
        cls, id: str, **params: Unpack["CustomerListPaymentTokensParams"]
    ) -> ListObject["CustomerPaymentToken"]:
        """
        Lists the Payment Tokens for a Crypto Customer.
        """
        return cast(
            ListObject["CustomerPaymentToken"],
            await cls._static_request_async(
                "get",
                "/v1/crypto/customers/{id}/payment_tokens".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    _inner_class_types = {"kyc_tiers": KycTier, "verifications": Verification}
