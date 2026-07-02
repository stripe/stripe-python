# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._singleton_api_resource import SingletonAPIResource
from stripe._stripe_object import UntypedStripeObject
from typing import Any, ClassVar
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.crypto._onramp_transaction_limits_retrieve_params import (
        OnrampTransactionLimitsRetrieveParams,
    )


class OnrampTransactionLimits(SingletonAPIResource["OnrampTransactionLimits"]):
    """
    This object represents the limit for the remaining amount that the crypto customer can onramp.
    """

    OBJECT_NAME: ClassVar[Literal["crypto.onramp_transaction_limits"]] = (
        "crypto.onramp_transaction_limits"
    )
    crypto_customer_id: str
    """
    The ID of the crypto customer.
    """
    limits: UntypedStripeObject[Any]
    """
    The remaining onramp limit for the crypto customer, separated by currency, payment method, and settlement speed.

    Limits are shown for currencies that correspond to the regions where the customer previously transacted. If the customer has no prior transactions, we return limits for all supported currencies.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["crypto.onramp_transaction_limits"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def retrieve(
        cls, **params: Unpack["OnrampTransactionLimitsRetrieveParams"]
    ) -> "OnrampTransactionLimits":
        """
        Retrieves the remaining onramp limit for a crypto customer.
        """
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, **params: Unpack["OnrampTransactionLimitsRetrieveParams"]
    ) -> "OnrampTransactionLimits":
        """
        Retrieves the remaining onramp limit for a crypto customer.
        """
        instance = cls(None, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/crypto/onramp_transaction_limits"
