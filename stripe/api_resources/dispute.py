# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class Dispute(
    ListableAPIResource["Dispute"], UpdateableAPIResource["Dispute"]
):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you're given the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate. You can find more
    information about the dispute process in our [Disputes and
    Fraud](https://stripe.com/docs/disputes) documentation.

    Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)
    """

    OBJECT_NAME = "dispute"
    amount: int
    balance_transactions: List["BalanceTransaction"]
    charge: ExpandableField["Charge"]
    created: str
    currency: str
    evidence: StripeObject
    evidence_details: StripeObject
    id: str
    is_charge_refundable: bool
    livemode: bool
    metadata: Dict[str, str]
    network_reason_code: Optional[str]
    object: Literal["dispute"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_method_details: StripeObject
    reason: str
    status: str

    @classmethod
    def _cls_close(
        cls,
        dispute,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/disputes/{dispute}/close".format(
                dispute=util.sanitize_id(dispute)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_close")
    def close(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/disputes/{dispute}/close".format(
                dispute=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
