# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._customer import Customer
    from stripe.params.financial_connections._consent_create_params import (
        ConsentCreateParams,
    )
    from stripe.params.financial_connections._consent_retrieve_params import (
        ConsentRetrieveParams,
    )


class Consent(CreateableAPIResource["Consent"]):
    """
    Stripe-issued localized Financial Connections consent text.
    """

    OBJECT_NAME: ClassVar[Literal["financial_connections.consent"]] = (
        "financial_connections.consent"
    )

    class AccountHolder(StripeObject):
        account: Optional[ExpandableField["Account"]]
        """
        The ID of the Stripe account that this account belongs to. Only available when `account_holder.type` is `account`.
        """
        customer: Optional[ExpandableField["Customer"]]
        """
        The ID for an Account representing a customer that this account belongs to. Only available when `account_holder.type` is `customer`.
        """
        customer_account: Optional[str]
        type: Union[Literal["account", "customer"], str]
        """
        Type of account holder that this account belongs to.
        """

    account_holder: AccountHolder
    consent_text: str
    """
    The exact localized text that must be displayed before collecting affirmative consent.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    expires_at: int
    """
    The exclusive time after which this Consent can no longer be used as launch evidence.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    locale: str
    """
    The BCP 47 locale used to render `consent_text`.
    """
    object: Literal["financial_connections.consent"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def create(cls, **params: Unpack["ConsentCreateParams"]) -> "Consent":
        """
        Creates a Financial Connections Consent object for an account holder.
        """
        return cast(
            "Consent",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["ConsentCreateParams"]
    ) -> "Consent":
        """
        Creates a Financial Connections Consent object for an account holder.
        """
        return cast(
            "Consent",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ConsentRetrieveParams"]
    ) -> "Consent":
        """
        Retrieves the details of a Financial Connections Consent.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["ConsentRetrieveParams"]
    ) -> "Consent":
        """
        Retrieves the details of a Financial Connections Consent.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"account_holder": AccountHolder}
