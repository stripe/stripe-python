# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

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
    When this happens, you have the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate.

    Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)
    """

    OBJECT_NAME = "dispute"

    class CloseParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListParams(RequestOptions):
        charge: NotRequired[Optional[str]]
        created: NotRequired[Optional[Union["Dispute.ListCreatedParams", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        payment_intent: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        evidence: NotRequired[Optional["Dispute.ModifyEvidenceParams"]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        submit: NotRequired[Optional[bool]]

    class ModifyEvidenceParams(TypedDict):
        access_activity_log: NotRequired[Optional[str]]
        billing_address: NotRequired[Optional[str]]
        cancellation_policy: NotRequired[Optional[str]]
        cancellation_policy_disclosure: NotRequired[Optional[str]]
        cancellation_rebuttal: NotRequired[Optional[str]]
        customer_communication: NotRequired[Optional[str]]
        customer_email_address: NotRequired[Optional[str]]
        customer_name: NotRequired[Optional[str]]
        customer_purchase_ip: NotRequired[Optional[str]]
        customer_signature: NotRequired[Optional[str]]
        duplicate_charge_documentation: NotRequired[Optional[str]]
        duplicate_charge_explanation: NotRequired[Optional[str]]
        duplicate_charge_id: NotRequired[Optional[str]]
        product_description: NotRequired[Optional[str]]
        receipt: NotRequired[Optional[str]]
        refund_policy: NotRequired[Optional[str]]
        refund_policy_disclosure: NotRequired[Optional[str]]
        refund_refusal_explanation: NotRequired[Optional[str]]
        service_date: NotRequired[Optional[str]]
        service_documentation: NotRequired[Optional[str]]
        shipping_address: NotRequired[Optional[str]]
        shipping_carrier: NotRequired[Optional[str]]
        shipping_date: NotRequired[Optional[str]]
        shipping_documentation: NotRequired[Optional[str]]
        shipping_tracking_number: NotRequired[Optional[str]]
        uncategorized_file: NotRequired[Optional[str]]
        uncategorized_text: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    amount: int
    balance_transactions: List["BalanceTransaction"]
    charge: ExpandableField["Charge"]
    created: int
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
    payment_method_details: Optional[StripeObject]
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
        **params: Unpack["Dispute.CloseParams"]
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
    def close(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Dispute.CloseParams"]
    ):
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
        **params: Unpack["Dispute.ListParams"]
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
    def modify(cls, id, **params: Unpack["Dispute.ModifyParams"]) -> "Dispute":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Dispute",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Dispute.RetrieveParams"]
    ) -> "Dispute":
        instance = cls(id, **params)
        instance.refresh()
        return instance
