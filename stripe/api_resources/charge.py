# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.application_fee import ApplicationFee
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.review import Review
    from stripe.api_resources.transfer import Transfer


class Charge(
    CreateableAPIResource["Charge"],
    ListableAPIResource["Charge"],
    SearchableAPIResource["Charge"],
    UpdateableAPIResource["Charge"],
):
    """
    The `Charge` object represents a single attempt to move money into your Stripe account.
    PaymentIntent confirmation is the most common way to create Charges, but transferring
    money to a different Stripe account through Connect also creates Charges.
    Some legacy payment flows create Charges directly, which is not recommended for new integrations.
    """

    OBJECT_NAME = "charge"
    amount: int
    amount_captured: int
    amount_refunded: int
    application: Optional[ExpandableField["Application"]]
    application_fee: Optional[ExpandableField["ApplicationFee"]]
    application_fee_amount: Optional[int]
    authorization_code: Optional[str]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    billing_details: StripeObject
    calculated_statement_descriptor: Optional[str]
    captured: bool
    created: int
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    disputed: bool
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_code: Optional[str]
    failure_message: Optional[str]
    fraud_details: Optional[StripeObject]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    level3: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["charge"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    outcome: Optional[StripeObject]
    paid: bool
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_method: Optional[str]
    payment_method_details: Optional[StripeObject]
    radar_options: Optional[StripeObject]
    receipt_email: Optional[str]
    receipt_number: Optional[str]
    receipt_url: Optional[str]
    refunded: bool
    refunds: Optional[ListObject["Refund"]]
    review: Optional[ExpandableField["Review"]]
    shipping: Optional[StripeObject]
    source: Optional[Any]
    source_transfer: Optional[ExpandableField["Transfer"]]
    statement_descriptor: Optional[str]
    statement_descriptor_suffix: Optional[str]
    status: Literal["failed", "pending", "succeeded"]
    transfer: Optional[ExpandableField["Transfer"]]
    transfer_data: Optional[StripeObject]
    transfer_group: Optional[str]

    @classmethod
    def _cls_capture(
        cls,
        charge: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(charge)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_capture")
    def capture(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Charge":
        return cast(
            "Charge",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Charge"]:
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
    def modify(cls, id, **params: Any) -> "Charge":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Charge",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Charge":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(cls, *args, **kwargs) -> Any:
        return cls._search(search_url="/v1/charges/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs) -> Any:
        return cls.search(*args, **kwargs).auto_paging_iter()

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "fraudulent"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "safe"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
