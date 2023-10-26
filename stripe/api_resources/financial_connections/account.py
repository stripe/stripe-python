# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.financial_connections.account_owner import (
        AccountOwner,
    )
    from stripe.api_resources.financial_connections.account_ownership import (
        AccountOwnership,
    )


class Account(ListableAPIResource["Account"]):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account"]
    ] = "financial_connections.account"
    if TYPE_CHECKING:

        class DisconnectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListParams(RequestOptions):
            account_holder: NotRequired["Account.ListParamsAccountHolder|None"]
            """
            If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            session: NotRequired["str|None"]
            """
            If present, only return accounts that were collected as part of the given session.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListParamsAccountHolder(TypedDict):
            account: NotRequired["str|None"]
            """
            The ID of the Stripe account whose accounts will be retrieved.
            """
            customer: NotRequired["str|None"]
            """
            The ID of the Stripe customer whose accounts will be retrieved.
            """

        class ListOwnersParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            ownership: str
            """
            The ID of the ownership object to fetch owners from.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class RefreshAccountParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            features: List[Literal["balance", "ownership"]]
            """
            The list of account features that you would like to refresh.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    account_holder: Optional[StripeObject]
    """
    The account holder that this account belongs to.
    """
    balance: Optional[StripeObject]
    """
    The most recent information about the account's balance.
    """
    balance_refresh: Optional[StripeObject]
    """
    The state of the most recent attempt to refresh the account balance.
    """
    category: Literal["cash", "credit", "investment", "other"]
    """
    The type of the account. Account category is further divided in `subcategory`.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    display_name: Optional[str]
    """
    A human-readable name that has been assigned to this account, either by the account holder or by the institution.
    """
    id: str
    """
    Unique identifier for the object.
    """
    institution_name: str
    """
    The name of the institution that holds this account.
    """
    last4: Optional[str]
    """
    The last 4 digits of the account number. If present, this will be 4 numeric characters.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["financial_connections.account"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    ownership: Optional[ExpandableField["AccountOwnership"]]
    """
    The most recent information about the account's owners.
    """
    ownership_refresh: Optional[StripeObject]
    """
    The state of the most recent attempt to refresh the account owners.
    """
    permissions: Optional[
        List[
            Literal["balances", "ownership", "payment_method", "transactions"]
        ]
    ]
    """
    The list of permissions granted by this account.
    """
    status: Literal["active", "disconnected", "inactive"]
    """
    The status of the link to the account.
    """
    subcategory: Literal[
        "checking",
        "credit_card",
        "line_of_credit",
        "mortgage",
        "other",
        "savings",
    ]
    """
    If `category` is `cash`, one of:

     - `checking`
     - `savings`
     - `other`

    If `category` is `credit`, one of:

     - `mortgage`
     - `line_of_credit`
     - `credit_card`
     - `other`

    If `category` is `investment` or `other`, this will be `other`.
    """
    supported_payment_method_types: List[Literal["link", "us_bank_account"]]
    """
    The [PaymentMethod type](https://stripe.com/docs/api/payment_methods/object#payment_method_object-type)(s) that can be created from this account.
    """

    @classmethod
    def _cls_disconnect(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ) -> "Account":
        return cast(
            "Account",
            cls._static_request(
                "post",
                "/v1/financial_connections/accounts/{account}/disconnect".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def disconnect(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ) -> "Account":
        ...

    @overload
    def disconnect(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ) -> "Account":
        ...

    @class_method_variant("_cls_disconnect")
    def disconnect(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.DisconnectParams"]
    ) -> "Account":
        return cast(
            "Account",
            self._request(
                "post",
                "/v1/financial_connections/accounts/{account}/disconnect".format(
                    account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
    ) -> ListObject["AccountOwner"]:
        return cast(
            ListObject["AccountOwner"],
            cls._static_request(
                "get",
                "/v1/financial_connections/accounts/{account}/owners".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def list_owners(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListOwnersParams"]
    ) -> ListObject["AccountOwner"]:
        ...

    @overload
    def list_owners(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.ListOwnersParams"]
    ) -> ListObject["AccountOwner"]:
        ...

    @class_method_variant("_cls_list_owners")
    def list_owners(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.ListOwnersParams"]
    ) -> ListObject["AccountOwner"]:
        return cast(
            ListObject["AccountOwner"],
            self._request(
                "get",
                "/v1/financial_connections/accounts/{account}/owners".format(
                    account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_refresh_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ) -> "Account":
        return cast(
            "Account",
            cls._static_request(
                "post",
                "/v1/financial_connections/accounts/{account}/refresh".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def refresh_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ) -> "Account":
        ...

    @overload
    def refresh_account(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ) -> "Account":
        ...

    @class_method_variant("_cls_refresh_account")
    def refresh_account(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RefreshAccountParams"]
    ) -> "Account":
        return cast(
            "Account",
            self._request(
                "post",
                "/v1/financial_connections/accounts/{account}/refresh".format(
                    account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Account.RetrieveParams"]
    ) -> "Account":
        instance = cls(id, **params)
        instance.refresh()
        return instance
