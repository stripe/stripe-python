# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.financial_connections.account_ownership import (
        AccountOwnership,
    )


class Account(ListableAPIResource["Account"]):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    OBJECT_NAME = "financial_connections.account"
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
            features: List[Literal["balance", "ownership"]]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    account_holder: Optional[StripeObject]
    balance: Optional[StripeObject]
    balance_refresh: Optional[StripeObject]
    category: Literal["cash", "credit", "investment", "other"]
    created: int
    display_name: Optional[str]
    id: str
    institution_name: str
    last4: Optional[str]
    livemode: bool
    object: Literal["financial_connections.account"]
    ownership: Optional[ExpandableField["AccountOwnership"]]
    ownership_refresh: Optional[StripeObject]
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
    supported_payment_method_types: List[Literal["link", "us_bank_account"]]

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
