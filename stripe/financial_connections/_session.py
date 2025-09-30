# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account as AccountResource
    from stripe._customer import Customer
    from stripe.financial_connections._account import (
        Account as FinancialConnectionsAccountResource,
    )
    from stripe.params.financial_connections._session_create_params import (
        SessionCreateParams,
    )
    from stripe.params.financial_connections._session_retrieve_params import (
        SessionRetrieveParams,
    )


class Session(CreateableAPIResource["Session"]):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    OBJECT_NAME: ClassVar[Literal["financial_connections.session"]] = (
        "financial_connections.session"
    )

    class AccountHolder(StripeObject):
        account: Optional[ExpandableField["AccountResource"]]
        """
        The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`.
        """
        customer: Optional[ExpandableField["Customer"]]
        """
        ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`.
        """
        customer_account: Optional[str]
        type: Literal["account", "customer"]
        """
        Type of account holder that this account belongs to.
        """

    class Filters(StripeObject):
        account_subcategories: Optional[
            List[
                Literal[
                    "checking",
                    "credit_card",
                    "line_of_credit",
                    "mortgage",
                    "savings",
                ]
            ]
        ]
        """
        Restricts the Session to subcategories of accounts that can be linked. Valid subcategories are: `checking`, `savings`, `mortgage`, `line_of_credit`, `credit_card`.
        """
        countries: Optional[List[str]]
        """
        List of countries from which to filter accounts.
        """
        institution: Optional[str]
        """
        Stripe ID of the institution with which the customer should be directed to log in.
        """

    class Limits(StripeObject):
        accounts: int
        """
        The number of accounts that can be linked in this Session.
        """

    class ManualEntry(StripeObject):
        pass

    class StatusDetails(StripeObject):
        class Cancelled(StripeObject):
            reason: Literal["custom_manual_entry", "other"]
            """
            The reason for the Session being cancelled.
            """

        cancelled: Optional[Cancelled]
        _inner_class_types = {"cancelled": Cancelled}

    account_holder: Optional[AccountHolder]
    """
    The account holder for whom accounts are collected in this session.
    """
    accounts: ListObject["FinancialConnectionsAccountResource"]
    """
    The accounts that were collected as part of this Session.
    """
    client_secret: str
    """
    A value that will be passed to the client to launch the authentication flow.
    """
    filters: Optional[Filters]
    id: str
    """
    Unique identifier for the object.
    """
    limits: Optional[Limits]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    manual_entry: Optional[ManualEntry]
    object: Literal["financial_connections.session"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    permissions: List[
        Literal["balances", "ownership", "payment_method", "transactions"]
    ]
    """
    Permissions requested for accounts collected during this session.
    """
    prefetch: Optional[
        List[
            Literal[
                "balances", "inferred_balances", "ownership", "transactions"
            ]
        ]
    ]
    """
    Data features requested to be retrieved upon account creation.
    """
    return_url: Optional[str]
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """
    status: Optional[Literal["cancelled", "failed", "pending", "succeeded"]]
    """
    The current state of the session.
    """
    status_details: Optional[StatusDetails]

    @classmethod
    def create(cls, **params: Unpack["SessionCreateParams"]) -> "Session":
        """
        To launch the Financial Connections authorization flow, create a Session. The session's client_secret can be used to launch the flow using Stripe.js.
        """
        return cast(
            "Session",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["SessionCreateParams"]
    ) -> "Session":
        """
        To launch the Financial Connections authorization flow, create a Session. The session's client_secret can be used to launch the flow using Stripe.js.
        """
        return cast(
            "Session",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SessionRetrieveParams"]
    ) -> "Session":
        """
        Retrieves the details of a Financial Connections Session
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["SessionRetrieveParams"]
    ) -> "Session":
        """
        Retrieves the details of a Financial Connections Session
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "account_holder": AccountHolder,
        "filters": Filters,
        "limits": Limits,
        "manual_entry": ManualEntry,
        "status_details": StatusDetails,
    }
