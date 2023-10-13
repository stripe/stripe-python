# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.account import Account as AccountResource
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.financial_connections.account import (
        Account as FinancialConnectionsAccountResource,
    )


class Session(CreateableAPIResource["Session"]):
    """
    A Financial Connections Session is the secure way to programmatically launch the client-side Stripe.js modal that lets your users link their accounts.
    """

    OBJECT_NAME = "financial_connections.session"

    class AccountHolder(StripeObject):
        account: Optional[ExpandableField["AccountResource"]]
        customer: Optional[ExpandableField["Customer"]]
        type: Literal["account", "customer"]

    class Filters(StripeObject):
        countries: Optional[List[str]]

    class Limits(StripeObject):
        accounts: int

    class ManualEntry(StripeObject):
        pass

    class StatusDetails(StripeObject):
        class Cancelled(StripeObject):
            reason: Literal["custom_manual_entry", "other"]

        cancelled: Optional[Cancelled]
        _inner_class_types = {"cancelled": Cancelled}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_holder: "Session.CreateParamsAccountHolder"
            expand: NotRequired["List[str]|None"]
            filters: NotRequired["Session.CreateParamsFilters|None"]
            limits: NotRequired["Session.CreateParamsLimits|None"]
            manual_entry: NotRequired["Session.CreateParamsManualEntry|None"]
            permissions: List[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ]
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            return_url: NotRequired["str|None"]

        class CreateParamsManualEntry(TypedDict):
            mode: NotRequired["Literal['automatic', 'custom']|None"]

        class CreateParamsLimits(TypedDict):
            accounts: int

        class CreateParamsFilters(TypedDict):
            countries: List[str]

        class CreateParamsAccountHolder(TypedDict):
            account: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            type: Literal["account", "customer"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    account_holder: Optional[AccountHolder]
    accounts: ListObject["FinancialConnectionsAccountResource"]
    client_secret: str
    filters: Optional[Filters]
    id: str
    limits: Optional[Limits]
    livemode: bool
    manual_entry: Optional[ManualEntry]
    object: Literal["financial_connections.session"]
    permissions: List[
        Literal["balances", "ownership", "payment_method", "transactions"]
    ]
    prefetch: Optional[
        List[
            Literal[
                "balances", "inferred_balances", "ownership", "transactions"
            ]
        ]
    ]
    return_url: Optional[str]
    status: Optional[Literal["cancelled", "failed", "pending", "succeeded"]]
    status_details: Optional[StatusDetails]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.CreateParams"]
    ) -> "Session":
        return cast(
            "Session",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Session.RetrieveParams"]
    ) -> "Session":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "account_holder": AccountHolder,
        "filters": Filters,
        "limits": Limits,
        "manual_entry": ManualEntry,
        "status_details": StatusDetails,
    }
