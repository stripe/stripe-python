# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
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
    from stripe.api_resources.issuing.transaction import Transaction


class Dispute(
    CreateableAPIResource["Dispute"],
    ListableAPIResource["Dispute"],
    UpdateableAPIResource["Dispute"],
):
    """
    As a [card issuer](https://stripe.com/docs/issuing), you can dispute transactions that the cardholder does not recognize, suspects to be fraudulent, or has other issues with.

    Related guide: [Issuing disputes](https://stripe.com/docs/issuing/purchases/disputes)
    """

    OBJECT_NAME = "issuing.dispute"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            evidence: NotRequired["Dispute.CreateParamsEvidence|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            transaction: NotRequired["str|None"]
            treasury: NotRequired["Dispute.CreateParamsTreasury|None"]

        class CreateParamsTreasury(TypedDict):
            received_debit: str

        class CreateParamsEvidence(TypedDict):
            canceled: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceCanceled|None"
            ]
            duplicate: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceDuplicate|None"
            ]
            fraudulent: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceFraudulent|None"
            ]
            merchandise_not_as_described: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceMerchandiseNotAsDescribed|None"
            ]
            not_received: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceNotReceived|None"
            ]
            other: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceOther|None"
            ]
            reason: NotRequired[
                "Literal['canceled', 'duplicate', 'fraudulent', 'merchandise_not_as_described', 'not_received', 'other', 'service_not_as_described']|None"
            ]
            service_not_as_described: NotRequired[
                "Literal['']|Dispute.CreateParamsEvidenceServiceNotAsDescribed|None"
            ]

        class CreateParamsEvidenceServiceNotAsDescribed(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            canceled_at: NotRequired["Literal['']|int|None"]
            cancellation_reason: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            received_at: NotRequired["Literal['']|int|None"]

        class CreateParamsEvidenceOther(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]

        class CreateParamsEvidenceNotReceived(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            expected_at: NotRequired["Literal['']|int|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]

        class CreateParamsEvidenceMerchandiseNotAsDescribed(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            received_at: NotRequired["Literal['']|int|None"]
            return_description: NotRequired["Literal['']|str|None"]
            return_status: NotRequired[
                "Literal['']|Literal['merchant_rejected', 'successful']|None"
            ]
            returned_at: NotRequired["Literal['']|int|None"]

        class CreateParamsEvidenceFraudulent(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]

        class CreateParamsEvidenceDuplicate(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            card_statement: NotRequired["Literal['']|str|None"]
            cash_receipt: NotRequired["Literal['']|str|None"]
            check_image: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            original_transaction: NotRequired["str|None"]

        class CreateParamsEvidenceCanceled(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            canceled_at: NotRequired["Literal['']|int|None"]
            cancellation_policy_provided: NotRequired["Literal['']|bool|None"]
            cancellation_reason: NotRequired["Literal['']|str|None"]
            expected_at: NotRequired["Literal['']|int|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]
            return_status: NotRequired[
                "Literal['']|Literal['merchant_rejected', 'successful']|None"
            ]
            returned_at: NotRequired["Literal['']|int|None"]

        class ListParams(RequestOptions):
            created: NotRequired["Dispute.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['expired', 'lost', 'submitted', 'unsubmitted', 'won']|None"
            ]
            transaction: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            evidence: NotRequired["Dispute.ModifyParamsEvidence|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ModifyParamsEvidence(TypedDict):
            canceled: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceCanceled|None"
            ]
            duplicate: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceDuplicate|None"
            ]
            fraudulent: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceFraudulent|None"
            ]
            merchandise_not_as_described: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceMerchandiseNotAsDescribed|None"
            ]
            not_received: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceNotReceived|None"
            ]
            other: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceOther|None"
            ]
            reason: NotRequired[
                "Literal['canceled', 'duplicate', 'fraudulent', 'merchandise_not_as_described', 'not_received', 'other', 'service_not_as_described']|None"
            ]
            service_not_as_described: NotRequired[
                "Literal['']|Dispute.ModifyParamsEvidenceServiceNotAsDescribed|None"
            ]

        class ModifyParamsEvidenceServiceNotAsDescribed(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            canceled_at: NotRequired["Literal['']|int|None"]
            cancellation_reason: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            received_at: NotRequired["Literal['']|int|None"]

        class ModifyParamsEvidenceOther(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]

        class ModifyParamsEvidenceNotReceived(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            expected_at: NotRequired["Literal['']|int|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]

        class ModifyParamsEvidenceMerchandiseNotAsDescribed(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            received_at: NotRequired["Literal['']|int|None"]
            return_description: NotRequired["Literal['']|str|None"]
            return_status: NotRequired[
                "Literal['']|Literal['merchant_rejected', 'successful']|None"
            ]
            returned_at: NotRequired["Literal['']|int|None"]

        class ModifyParamsEvidenceFraudulent(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]

        class ModifyParamsEvidenceDuplicate(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            card_statement: NotRequired["Literal['']|str|None"]
            cash_receipt: NotRequired["Literal['']|str|None"]
            check_image: NotRequired["Literal['']|str|None"]
            explanation: NotRequired["Literal['']|str|None"]
            original_transaction: NotRequired["str|None"]

        class ModifyParamsEvidenceCanceled(TypedDict):
            additional_documentation: NotRequired["Literal['']|str|None"]
            canceled_at: NotRequired["Literal['']|int|None"]
            cancellation_policy_provided: NotRequired["Literal['']|bool|None"]
            cancellation_reason: NotRequired["Literal['']|str|None"]
            expected_at: NotRequired["Literal['']|int|None"]
            explanation: NotRequired["Literal['']|str|None"]
            product_description: NotRequired["Literal['']|str|None"]
            product_type: NotRequired[
                "Literal['']|Literal['merchandise', 'service']|None"
            ]
            return_status: NotRequired[
                "Literal['']|Literal['merchant_rejected', 'successful']|None"
            ]
            returned_at: NotRequired["Literal['']|int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SubmitParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

    amount: int
    balance_transactions: Optional[List["BalanceTransaction"]]
    created: int
    currency: str
    evidence: StripeObject
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["issuing.dispute"]
    status: Literal["expired", "lost", "submitted", "unsubmitted", "won"]
    transaction: ExpandableField["Transaction"]
    treasury: Optional[StripeObject]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Dispute.CreateParams"]
    ) -> "Dispute":
        return cast(
            "Dispute",
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

    @classmethod
    def _cls_submit(
        cls,
        dispute: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Dispute.SubmitParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/disputes/{dispute}/submit".format(
                dispute=util.sanitize_id(dispute)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_submit")
    def submit(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Dispute.SubmitParams"]
    ):
        return self._request(
            "post",
            "/v1/issuing/disputes/{dispute}/submit".format(
                dispute=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
