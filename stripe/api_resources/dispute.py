# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.file import File
    from stripe.api_resources.payment_intent import PaymentIntent


class Dispute(
    ListableAPIResource["Dispute"], UpdateableAPIResource["Dispute"]
):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you have the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate.

    Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)
    """

    OBJECT_NAME = "dispute"

    class Evidence(StripeObject):
        access_activity_log: Optional[str]
        billing_address: Optional[str]
        cancellation_policy: Optional[ExpandableField["File"]]
        cancellation_policy_disclosure: Optional[str]
        cancellation_rebuttal: Optional[str]
        customer_communication: Optional[ExpandableField["File"]]
        customer_email_address: Optional[str]
        customer_name: Optional[str]
        customer_purchase_ip: Optional[str]
        customer_signature: Optional[ExpandableField["File"]]
        duplicate_charge_documentation: Optional[ExpandableField["File"]]
        duplicate_charge_explanation: Optional[str]
        duplicate_charge_id: Optional[str]
        product_description: Optional[str]
        receipt: Optional[ExpandableField["File"]]
        refund_policy: Optional[ExpandableField["File"]]
        refund_policy_disclosure: Optional[str]
        refund_refusal_explanation: Optional[str]
        service_date: Optional[str]
        service_documentation: Optional[ExpandableField["File"]]
        shipping_address: Optional[str]
        shipping_carrier: Optional[str]
        shipping_date: Optional[str]
        shipping_documentation: Optional[ExpandableField["File"]]
        shipping_tracking_number: Optional[str]
        uncategorized_file: Optional[ExpandableField["File"]]
        uncategorized_text: Optional[str]

    class EvidenceDetails(StripeObject):
        due_by: Optional[int]
        has_evidence: bool
        past_due: bool
        submission_count: int

    class PaymentMethodDetails(StripeObject):
        class Card(StripeObject):
            brand: str
            network_reason_code: Optional[str]

        card: Optional[Card]
        type: Literal["card"]
        _inner_class_types = {"card": Card}

    amount: int
    balance_transactions: List["BalanceTransaction"]
    charge: ExpandableField["Charge"]
    created: int
    currency: str
    evidence: Evidence
    evidence_details: EvidenceDetails
    id: str
    is_charge_refundable: bool
    livemode: bool
    metadata: Dict[str, str]
    network_reason_code: Optional[str]
    object: Literal["dispute"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_method_details: Optional[PaymentMethodDetails]
    reason: str
    status: Literal[
        "lost",
        "needs_response",
        "under_review",
        "warning_closed",
        "warning_needs_response",
        "warning_under_review",
        "won",
    ]

    @classmethod
    def _cls_close(
        cls,
        dispute: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def close(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/disputes/{dispute}/close".format(
                dispute=util.sanitize_id(self.get("id"))
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
        **params: Any
    ) -> ListObject["Dispute"]:
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
    def modify(cls, id, **params: Any) -> "Dispute":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Dispute",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Dispute":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "evidence": Evidence,
        "evidence_details": EvidenceDetails,
        "payment_method_details": PaymentMethodDetails,
    }
