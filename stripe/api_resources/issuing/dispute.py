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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        evidence: NotRequired[Optional["Dispute.CreateEvidenceParams"]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        transaction: NotRequired[Optional[str]]
        treasury: NotRequired[Optional["Dispute.CreateTreasuryParams"]]

    class CreateTreasuryParams(TypedDict):
        received_debit: str

    class CreateEvidenceParams(TypedDict):
        canceled: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.CreateEvidenceCanceledParams"]
            ]
        ]
        duplicate: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.CreateEvidenceDuplicateParams"]
            ]
        ]
        fraudulent: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.CreateEvidenceFraudulentParams"]
            ]
        ]
        merchandise_not_as_described: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Dispute.CreateEvidenceMerchandiseNotAsDescribedParams",
                ]
            ]
        ]
        not_received: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.CreateEvidenceNotReceivedParams"]
            ]
        ]
        other: NotRequired[
            Optional[Union[Literal[""], "Dispute.CreateEvidenceOtherParams"]]
        ]
        reason: NotRequired[
            Optional[
                Literal[
                    "canceled",
                    "duplicate",
                    "fraudulent",
                    "merchandise_not_as_described",
                    "not_received",
                    "other",
                    "service_not_as_described",
                ]
            ]
        ]
        service_not_as_described: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Dispute.CreateEvidenceServiceNotAsDescribedParams",
                ]
            ]
        ]

    class CreateEvidenceServiceNotAsDescribedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        canceled_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancellation_reason: NotRequired[Optional[Union[Literal[""], str]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        received_at: NotRequired[Optional[Union[Literal[""], int]]]

    class CreateEvidenceOtherParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]

    class CreateEvidenceNotReceivedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        expected_at: NotRequired[Optional[Union[Literal[""], int]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]

    class CreateEvidenceMerchandiseNotAsDescribedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        received_at: NotRequired[Optional[Union[Literal[""], int]]]
        return_description: NotRequired[Optional[Union[Literal[""], str]]]
        return_status: NotRequired[
            Optional[
                Union[Literal[""], Literal["merchant_rejected", "successful"]]
            ]
        ]
        returned_at: NotRequired[Optional[Union[Literal[""], int]]]

    class CreateEvidenceFraudulentParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateEvidenceDuplicateParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        card_statement: NotRequired[Optional[Union[Literal[""], str]]]
        cash_receipt: NotRequired[Optional[Union[Literal[""], str]]]
        check_image: NotRequired[Optional[Union[Literal[""], str]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        original_transaction: NotRequired[Optional[str]]

    class CreateEvidenceCanceledParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        canceled_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancellation_policy_provided: NotRequired[
            Optional[Union[Literal[""], bool]]
        ]
        cancellation_reason: NotRequired[Optional[Union[Literal[""], str]]]
        expected_at: NotRequired[Optional[Union[Literal[""], int]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]
        return_status: NotRequired[
            Optional[
                Union[Literal[""], Literal["merchant_rejected", "successful"]]
            ]
        ]
        returned_at: NotRequired[Optional[Union[Literal[""], int]]]

    class ListParams(RequestOptions):
        created: NotRequired[Optional[Union["Dispute.ListCreatedParams", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[
            Optional[
                Literal["expired", "lost", "submitted", "unsubmitted", "won"]
            ]
        ]
        transaction: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        evidence: NotRequired[Optional["Dispute.ModifyEvidenceParams"]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ModifyEvidenceParams(TypedDict):
        canceled: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.ModifyEvidenceCanceledParams"]
            ]
        ]
        duplicate: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.ModifyEvidenceDuplicateParams"]
            ]
        ]
        fraudulent: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.ModifyEvidenceFraudulentParams"]
            ]
        ]
        merchandise_not_as_described: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Dispute.ModifyEvidenceMerchandiseNotAsDescribedParams",
                ]
            ]
        ]
        not_received: NotRequired[
            Optional[
                Union[Literal[""], "Dispute.ModifyEvidenceNotReceivedParams"]
            ]
        ]
        other: NotRequired[
            Optional[Union[Literal[""], "Dispute.ModifyEvidenceOtherParams"]]
        ]
        reason: NotRequired[
            Optional[
                Literal[
                    "canceled",
                    "duplicate",
                    "fraudulent",
                    "merchandise_not_as_described",
                    "not_received",
                    "other",
                    "service_not_as_described",
                ]
            ]
        ]
        service_not_as_described: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Dispute.ModifyEvidenceServiceNotAsDescribedParams",
                ]
            ]
        ]

    class ModifyEvidenceServiceNotAsDescribedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        canceled_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancellation_reason: NotRequired[Optional[Union[Literal[""], str]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        received_at: NotRequired[Optional[Union[Literal[""], int]]]

    class ModifyEvidenceOtherParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]

    class ModifyEvidenceNotReceivedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        expected_at: NotRequired[Optional[Union[Literal[""], int]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]

    class ModifyEvidenceMerchandiseNotAsDescribedParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        received_at: NotRequired[Optional[Union[Literal[""], int]]]
        return_description: NotRequired[Optional[Union[Literal[""], str]]]
        return_status: NotRequired[
            Optional[
                Union[Literal[""], Literal["merchant_rejected", "successful"]]
            ]
        ]
        returned_at: NotRequired[Optional[Union[Literal[""], int]]]

    class ModifyEvidenceFraudulentParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyEvidenceDuplicateParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        card_statement: NotRequired[Optional[Union[Literal[""], str]]]
        cash_receipt: NotRequired[Optional[Union[Literal[""], str]]]
        check_image: NotRequired[Optional[Union[Literal[""], str]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        original_transaction: NotRequired[Optional[str]]

    class ModifyEvidenceCanceledParams(TypedDict):
        additional_documentation: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        canceled_at: NotRequired[Optional[Union[Literal[""], int]]]
        cancellation_policy_provided: NotRequired[
            Optional[Union[Literal[""], bool]]
        ]
        cancellation_reason: NotRequired[Optional[Union[Literal[""], str]]]
        expected_at: NotRequired[Optional[Union[Literal[""], int]]]
        explanation: NotRequired[Optional[Union[Literal[""], str]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        product_type: NotRequired[
            Optional[Union[Literal[""], Literal["merchandise", "service"]]]
        ]
        return_status: NotRequired[
            Optional[
                Union[Literal[""], Literal["merchant_rejected", "successful"]]
            ]
        ]
        returned_at: NotRequired[Optional[Union[Literal[""], int]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SubmitParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

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
