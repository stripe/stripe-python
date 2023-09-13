# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from typing import Any
from typing import Dict
from typing import Optional
from typing_extensions import Literal

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
    as well as list all payouts. Payouts are made on [varying
    schedules](https://stripe.com/docs/connect/manage-payout-schedule), depending on your country and
    industry.

    Related guide: [Receiving payouts](https://stripe.com/docs/payouts)
    """

    OBJECT_NAME = "payout"
    amount: int
    arrival_date: str
    automatic: bool
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    created: str
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
    reconciliation_status: str
    reversed_by: Optional[ExpandableField["Payout"]]
    source_type: str
    statement_descriptor: Optional[str]
    status: str
    type: str

    @classmethod
    def _cls_cancel(
        cls,
        payout,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payouts/{payout}/cancel".format(
                payout=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_reverse(
        cls,
        payout,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def reverse(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/payouts/{payout}/reverse".format(
                payout=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
