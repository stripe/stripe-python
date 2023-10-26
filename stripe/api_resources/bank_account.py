# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error
from stripe.api_resources.abstract import (
    DeletableAPIResource,
    UpdateableAPIResource,
    VerifyMixin,
)
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.card import Card


class BankAccount(
    DeletableAPIResource["BankAccount"],
    UpdateableAPIResource["BankAccount"],
    VerifyMixin,
):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
    destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](https://stripe.com/docs/payments/bank-debits-transfers)
    """

    OBJECT_NAME: ClassVar[Literal["bank_account"]] = "bank_account"
    if TYPE_CHECKING:

        class DeleteParams(RequestOptions):
            pass

    account: Optional[ExpandableField["Account"]]
    """
    The ID of the account that the bank account is associated with.
    """
    account_holder_name: Optional[str]
    """
    The name of the person or business that owns the bank account.
    """
    account_holder_type: Optional[str]
    """
    The type of entity that holds the account. This can be either `individual` or `company`.
    """
    account_type: Optional[str]
    """
    The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    """
    available_payout_methods: Optional[List[Literal["instant", "standard"]]]
    """
    A set of available payout methods for this bank account. Only values from this set should be passed as the `method` when creating a payout.
    """
    bank_name: Optional[str]
    """
    Name of the bank associated with the routing number (e.g., `WELLS FARGO`).
    """
    country: str
    """
    Two-letter ISO code representing the country the bank account is located in.
    """
    currency: str
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/payouts) paid out to the bank account.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The ID of the customer that the bank account is associated with.
    """
    default_for_currency: Optional[bool]
    """
    Whether this bank account is the default external account for its currency.
    """
    fingerprint: Optional[str]
    """
    Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
    """
    future_requirements: Optional[StripeObject]
    """
    Information about the [upcoming new requirements for the bank account](https://stripe.com/docs/connect/custom-accounts/future-requirements), including what information needs to be collected, and by when.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last4: str
    """
    The last four digits of the bank account number.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    requirements: Optional[StripeObject]
    """
    Information about the requirements for the bank account, including what information needs to be collected.
    """
    routing_number: Optional[str]
    """
    The routing transit number for the bank account.
    """
    status: str
    """
    For bank accounts, possible values are `new`, `validated`, `verified`, `verification_failed`, or `errored`. A bank account that hasn't had any activity or validation performed is `new`. If Stripe can determine that the bank account exists, its status will be `validated`. Note that there often isn't enough information to know (e.g., for smaller credit unions), and the validation is not always run. If customer bank account verification has succeeded, the bank account status will be `verified`. If the verification failed for any reason, such as microdeposit failure, the status will be `verification_failed`. If a transfer sent to this bank account fails, we'll set the status to `errored` and will not continue to send transfers until the bank details are updated.

    For external accounts, possible values are `new`, `errored` and `verification_failed`. If a transfer fails, the status is set to `errored` and transfers are stopped until account details are updated. In India, if we can't [verify the owner of the bank account](https://support.stripe.com/questions/bank-account-ownership-verification), we'll set the status to `verification_failed`. Other validations aren't run against external accounts because they're only used for payouts. This means the other statuses don't apply.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request("delete", url, params=params),
        )

    @overload
    @classmethod
    def delete(
        cls, sid: str, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        ...

    @overload
    def delete(
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["BankAccount.DeleteParams"]
    ) -> Union["BankAccount", "Card"]:
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    def instance_url(self):
        token = self.id
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = self.customer

            base = Customer.class_url()
            assert customer is not None
            if isinstance(customer, Customer):
                customer = customer.id
            owner_extn = quote_plus(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = self.account

            base = Account.class_url()
            assert account is not None
            if isinstance(account, Account):
                account = account.id
            owner_extn = quote_plus(account)
            class_base = "external_accounts"

        else:
            raise error.InvalidRequestError(
                "Could not determine whether bank_account_id %s is "
                "attached to a customer or an account." % token,
                "id",
            )

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a bank account without a customer or account ID. "
            "Use stripe.Customer.modify_source('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/customer_bank_accounts/update) or "
            "stripe.Account.modify_external_account('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/update)."
        )

    @classmethod
    def retrieve(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        raise NotImplementedError(
            "Can't retrieve a bank account without a customer or account ID. "
            "Use stripe.customer.retrieve_source('customer_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/customer_bank_accounts/retrieve) or "
            "stripe.Account.retrieve_external_account('account_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/retrieve)."
        )
