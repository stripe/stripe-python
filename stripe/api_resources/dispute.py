# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CloseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            charge: NotRequired["str|None"]
            created: NotRequired["Dispute.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payment_intent: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            evidence: NotRequired["Dispute.ModifyParamsEvidence|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            submit: NotRequired["bool|None"]

        class ModifyParamsEvidence(TypedDict):
            access_activity_log: NotRequired["str|None"]
            billing_address: NotRequired["str|None"]
            cancellation_policy: NotRequired["str|None"]
            cancellation_policy_disclosure: NotRequired["str|None"]
            cancellation_rebuttal: NotRequired["str|None"]
            customer_communication: NotRequired["str|None"]
            customer_email_address: NotRequired["str|None"]
            customer_name: NotRequired["str|None"]
            customer_purchase_ip: NotRequired["str|None"]
            customer_signature: NotRequired["str|None"]
            duplicate_charge_documentation: NotRequired["str|None"]
            duplicate_charge_explanation: NotRequired["str|None"]
            duplicate_charge_id: NotRequired["str|None"]
            product_description: NotRequired["str|None"]
            receipt: NotRequired["str|None"]
            refund_policy: NotRequired["str|None"]
            refund_policy_disclosure: NotRequired["str|None"]
            refund_refusal_explanation: NotRequired["str|None"]
            service_date: NotRequired["str|None"]
            service_documentation: NotRequired["str|None"]
            shipping_address: NotRequired["str|None"]
            shipping_carrier: NotRequired["str|None"]
            shipping_date: NotRequired["str|None"]
            shipping_documentation: NotRequired["str|None"]
            shipping_tracking_number: NotRequired["str|None"]
            uncategorized_file: NotRequired["str|None"]
            uncategorized_text: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
