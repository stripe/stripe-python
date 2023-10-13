# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
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
    from stripe.api_resources.financial_connections.account_ownership import (
        AccountOwnership,
    )


@nested_resource_class_methods("inferred_balance")
class Account(ListableAPIResource["Account"]):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    OBJECT_NAME = "financial_connections.account"

    class AccountHolder(StripeObject):
        account: Optional[ExpandableField["AccountResource"]]
        customer: Optional[ExpandableField["Customer"]]
        type: Literal["account", "customer"]

    class Balance(StripeObject):
        class Cash(StripeObject):
            available: Optional[Dict[str, int]]

        class Credit(StripeObject):
            used: Optional[Dict[str, int]]

        as_of: int
        cash: Optional[Cash]
        credit: Optional[Credit]
        current: Dict[str, int]
        type: Literal["cash", "credit"]
        _inner_class_types = {"cash": Cash, "credit": Credit}

    class BalanceRefresh(StripeObject):
        last_attempted_at: int
        next_refresh_available_at: Optional[int]
        status: Literal["failed", "pending", "succeeded"]

    class InferredBalancesRefresh(StripeObject):
        last_attempted_at: int
        next_refresh_available_at: Optional[int]
        status: Literal["failed", "pending", "succeeded"]

    class OwnershipRefresh(StripeObject):
        last_attempted_at: int
        next_refresh_available_at: Optional[int]
        status: Literal["failed", "pending", "succeeded"]

    class TransactionRefresh(StripeObject):
        id: str
        last_attempted_at: int
        next_refresh_available_at: Optional[int]
        status: Literal["failed", "pending", "succeeded"]

    if TYPE_CHECKING:

        class DisconnectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            account_holder: NotRequired["Account.ListParamsAccountHolder|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            session: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsAccountHolder(TypedDict):
            account: NotRequired["str|None"]
            customer: NotRequired["str|None"]

        class ListOwnersParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            ownership: str
            starting_after: NotRequired["str|None"]

        class RefreshAccountParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            features: List[
                Literal[
                    "balance", "inferred_balances", "ownership", "transactions"
                ]
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SubscribeParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            features: List[Literal["inferred_balances", "transactions"]]

        class UnsubscribeParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            features: List[Literal["inferred_balances", "transactions"]]

        class ListInferredBalancesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

    account_holder: Optional[AccountHolder]
    balance: Optional[Balance]
    balance_refresh: Optional[BalanceRefresh]
    category: Literal["cash", "credit", "investment", "other"]
    created: int
    display_name: Optional[str]
    id: str
    inferred_balances_refresh: Optional[InferredBalancesRefresh]
    institution_name: str
    last4: Optional[str]
    livemode: bool
    object: Literal["financial_connections.account"]
    ownership: Optional[ExpandableField["AccountOwnership"]]
    ownership_refresh: Optional[OwnershipRefresh]
    permissions: Optional[
        List[
            Literal["balances", "ownership", "payment_method", "transactions"]
        ]
    ]
    status: Literal["active", "disconnected", "inactive"]
    subcategory: Literal[
        "checking",
        "credit_card",
        "line_of_credit",
        "mortgage",
        "other",
        "savings",
    ]
    subscriptions: Optional[List[Literal["inferred_balances", "transactions"]]]
    supported_payment_method_types: List[Literal["link", "us_bank_account"]]
    transaction_refresh: Optional[TransactionRefresh]

    @classmethod
    def _cls_disconnect(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/disconnect".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_disconnect")
    def disconnect(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/disconnect".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListParams"]
    ) -> ListObject["Account"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_owners(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListOwnersParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/financial_connections/accounts/{account}/owners".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_owners")
    def list_owners(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.ListOwnersParams"]
    ):
        return self._request(
            "get",
            "/v1/financial_connections/accounts/{account}/owners".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_refresh_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/refresh".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_refresh_account")
    def refresh_account(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/refresh".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Account.RetrieveParams"]
    ) -> "Account":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_subscribe(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.SubscribeParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/subscribe".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_subscribe")
    def subscribe(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.SubscribeParams"]
    ):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/subscribe".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_unsubscribe(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.UnsubscribeParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/financial_connections/accounts/{account}/unsubscribe".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_unsubscribe")
    def unsubscribe(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.UnsubscribeParams"]
    ):
        return self._request(
            "post",
            "/v1/financial_connections/accounts/{account}/unsubscribe".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list_inferred_balances(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListInferredBalancesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/financial_connections/accounts/{account}/inferred_balances".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    _inner_class_types = {
        "account_holder": AccountHolder,
        "balance": Balance,
        "balance_refresh": BalanceRefresh,
        "inferred_balances_refresh": InferredBalancesRefresh,
        "ownership_refresh": OwnershipRefresh,
        "transaction_refresh": TransactionRefresh,
    }
