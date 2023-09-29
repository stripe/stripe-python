# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction


class Payout(
    CreateableAPIResource["Payout"],
    ListableAPIResource["Payout"],
    UpdateableAPIResource["Payout"],
):
    """
    A `Payout` object is created when you receive funds from Stripe, or when you
    initiate a payout to either a bank account or debit card of a [connected
    Stripe account](https://stripe.com/docs/connect/bank-debit-card-payouts). You can retrieve individual payouts,
    and list all payouts. Payouts are made on [varying
    schedules](https://stripe.com/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving payouts](https://stripe.com/docs/payouts)
    """

    OBJECT_NAME = "payout"
    amount: int
    arrival_date: int
    automatic: bool
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    created: int
    currency: str
    description: Optional[str]
    destination: Optional[ExpandableField[Any]]
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_code: Optional[str]
    failure_message: Optional[str]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    method: str
    object: Literal["payout"]
    original_payout: Optional[ExpandableField["Payout"]]
    reconciliation_status: Literal[
        "completed", "in_progress", "not_applicable"
    ]
    reversed_by: Optional[ExpandableField["Payout"]]
    source_type: str
    statement_descriptor: Optional[str]
    status: str
    type: Literal["bank_account", "card"]

    @classmethod
    def _cls_cancel(
        cls,
        payout: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payouts/{payout}/cancel".format(
                payout=util.sanitize_id(payout)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payouts/{payout}/cancel".format(
                payout=util.sanitize_id(self.get("id"))
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
    ) -> "Payout":
        return cast(
            "Payout",
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
    ) -> ListObject["Payout"]:
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
    def modify(cls, id, **params: Any) -> "Payout":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Payout",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Payout":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_reverse(
        cls,
        payout: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payouts/{payout}/reverse".format(
                payout=util.sanitize_id(payout)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reverse")
    def reverse(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payouts/{payout}/reverse".format(
                payout=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
