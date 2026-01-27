# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._customer import Customer
    from stripe.financial_connections._institution import Institution
    from stripe.params.financial_connections._authorization_retrieve_params import (
        AuthorizationRetrieveParams,
    )


class Authorization(APIResource["Authorization"]):
    """
    An Authorization represents the set of credentials used to connect a group of Financial Connections Accounts.
    """

    OBJECT_NAME: ClassVar[Literal["financial_connections.authorization"]] = (
        "financial_connections.authorization"
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
        type: Literal["account", "customer"]
        """
        Type of account holder that this account belongs to.
        """

    class StatusDetails(StripeObject):
        class Inactive(StripeObject):
            action: Literal["none", "relink_required"]
            """
            The action (if any) to relink the inactive Authorization.
            """

        inactive: Optional[Inactive]
        _inner_class_types = {"inactive": Inactive}

    account_holder: Optional[AccountHolder]
    """
    The account holder that this authorization belongs to.
    """
    id: str
    """
    Unique identifier for the object.
    """
    institution: Optional[ExpandableField["Institution"]]
    """
    The ID of the Financial Connections Institution this account belongs to. Note that this relationship may sometimes change in rare circumstances (e.g. institution mergers).
    """
    institution_name: str
    """
    The name of the institution that this authorization belongs to.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["financial_connections.authorization"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "disconnected", "inactive"]
    """
    The status of the connection to the Authorization.
    """
    status_details: StatusDetails

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["AuthorizationRetrieveParams"]
    ) -> "Authorization":
        """
        Retrieves the details of an Financial Connections Authorization.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["AuthorizationRetrieveParams"]
    ) -> "Authorization":
        """
        Retrieves the details of an Financial Connections Authorization.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "account_holder": AccountHolder,
        "status_details": StatusDetails,
    }
