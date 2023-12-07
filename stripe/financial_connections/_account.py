# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._account import Account as AccountResource
    from stripe._customer import Customer
    from stripe.financial_connections._account_owner import AccountOwner
    from stripe.financial_connections._account_ownership import (
        AccountOwnership,
    )


class Account(ListableAPIResource["Account"]):
    """
    A Financial Connections Account represents an account that exists outside of Stripe, to which you have been granted some degree of access.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account"]
    ] = "financial_connections.account"

    class AccountHolder(StripeObject):
        account: Optional[ExpandableField["AccountResource"]]
        """
        The ID of the Stripe account this account belongs to. Should only be present if `account_holder.type` is `account`.
        """
        customer: Optional[ExpandableField["Customer"]]
        """
        ID of the Stripe customer this account belongs to. Present if and only if `account_holder.type` is `customer`.
        """
        type: Literal["account", "customer"]
        """
        Type of account holder that this account belongs to.
        """

    class Balance(StripeObject):
        class Cash(StripeObject):
            available: Optional[Dict[str, int]]
            """
            The funds available to the account holder. Typically this is the current balance less any holds.

            Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

            Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
            """

        class Credit(StripeObject):
            used: Optional[Dict[str, int]]
            """
            The credit that has been used by the account holder.

            Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

            Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
            """

        as_of: int
        """
        The time that the external institution calculated this balance. Measured in seconds since the Unix epoch.
        """
        cash: Optional[Cash]
        credit: Optional[Credit]
        current: Dict[str, int]
        """
        The balances owed to (or by) the account holder.

        Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

        Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
        """
        type: Literal["cash", "credit"]
        """
        The `type` of the balance. An additional hash is included on the balance with a name matching this value.
        """
        _inner_class_types = {"cash": Cash, "credit": Credit}

    class BalanceRefresh(StripeObject):
        last_attempted_at: int
        """
        The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.
        """
        status: Literal["failed", "pending", "succeeded"]
        """
        The status of the last refresh attempt.
        """

    class OwnershipRefresh(StripeObject):
        last_attempted_at: int
        """
        The time at which the last refresh attempt was initiated. Measured in seconds since the Unix epoch.
        """
        status: Literal["failed", "pending", "succeeded"]
        """
        The status of the last refresh attempt.
        """

    class DisconnectParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(RequestOptions):
        account_holder: NotRequired["Account.ListParamsAccountHolder"]
        """
        If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        session: NotRequired["str"]
        """
        If present, only return accounts that were collected as part of the given session.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParamsAccountHolder(TypedDict):
        account: NotRequired["str"]
        """
        The ID of the Stripe account whose accounts will be retrieved.
        """
        customer: NotRequired["str"]
        """
        The ID of the Stripe customer whose accounts will be retrieved.
        """

    class ListOwnersParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        ownership: str
        """
        The ID of the ownership object to fetch owners from.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RefreshAccountParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        features: List[Literal["balance", "ownership"]]
        """
        The list of account features that you would like to refresh.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    account_holder: Optional[AccountHolder]
    """
    The account holder that this account belongs to.
    """
    balance: Optional[Balance]
    """
    The most recent information about the account's balance.
    """
    balance_refresh: Optional[BalanceRefresh]
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
    ownership_refresh: Optional[OwnershipRefresh]
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
        **params: Unpack[
            "Account.DisconnectParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).
        """
        return cast(
            "Account",
            cls._static_request(
                "post",
                "/v1/financial_connections/accounts/{account}/disconnect".format(
                    account=_util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def disconnect(
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Account.DisconnectParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).
        """
        ...

    @overload
    def disconnect(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.DisconnectParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).
        """
        ...

    @class_method_variant("_cls_disconnect")
    def disconnect(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.DisconnectParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Disables your access to a Financial Connections Account. You will no longer be able to access data associated with the account (e.g. balances, transactions).
        """
        return cast(
            "Account",
            self._request(
                "post",
                "/v1/financial_connections/accounts/{account}/disconnect".format(
                    account=_util.sanitize_id(self.get("id"))
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
        **params: Unpack[
            "Account.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Account"]:
        """
        Returns a list of Financial Connections Account objects.
        """
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
        **params: Unpack[
            "Account.ListOwnersParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["AccountOwner"]:
        """
        Lists all owners for a given Account
        """
        return cast(
            ListObject["AccountOwner"],
            cls._static_request(
                "get",
                "/v1/financial_connections/accounts/{account}/owners".format(
                    account=_util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_owners(
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Account.ListOwnersParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["AccountOwner"]:
        """
        Lists all owners for a given Account
        """
        ...

    @overload
    def list_owners(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.ListOwnersParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["AccountOwner"]:
        """
        Lists all owners for a given Account
        """
        ...

    @class_method_variant("_cls_list_owners")
    def list_owners(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.ListOwnersParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["AccountOwner"]:
        """
        Lists all owners for a given Account
        """
        return cast(
            ListObject["AccountOwner"],
            self._request(
                "get",
                "/v1/financial_connections/accounts/{account}/owners".format(
                    account=_util.sanitize_id(self.get("id"))
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
        **params: Unpack[
            "Account.RefreshAccountParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Refreshes the data associated with a Financial Connections Account.
        """
        return cast(
            "Account",
            cls._static_request(
                "post",
                "/v1/financial_connections/accounts/{account}/refresh".format(
                    account=_util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def refresh_account(
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Account.RefreshAccountParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Refreshes the data associated with a Financial Connections Account.
        """
        ...

    @overload
    def refresh_account(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.RefreshAccountParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Refreshes the data associated with a Financial Connections Account.
        """
        ...

    @class_method_variant("_cls_refresh_account")
    def refresh_account(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Account.RefreshAccountParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Account":
        """
        Refreshes the data associated with a Financial Connections Account.
        """
        return cast(
            "Account",
            self._request(
                "post",
                "/v1/financial_connections/accounts/{account}/refresh".format(
                    account=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Account.RetrieveParams"]
    ) -> "Account":
        """
        Retrieves the details of an Financial Connections Account.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "account_holder": AccountHolder,
        "balance": Balance,
        "balance_refresh": BalanceRefresh,
        "ownership_refresh": OwnershipRefresh,
    }
