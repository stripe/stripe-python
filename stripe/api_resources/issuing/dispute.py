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
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
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
    from stripe.api_resources.file import File
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

    OBJECT_NAME: ClassVar[Literal["issuing.dispute"]] = "issuing.dispute"

    class Evidence(StripeObject):
        class Canceled(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            canceled_at: Optional[int]
            """
            Date when order was canceled.
            """
            cancellation_policy_provided: Optional[bool]
            """
            Whether the cardholder was provided with a cancellation policy.
            """
            cancellation_reason: Optional[str]
            """
            Reason for canceling the order.
            """
            expected_at: Optional[int]
            """
            Date when the cardholder expected to receive the product.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            product_description: Optional[str]
            """
            Description of the merchandise or service that was purchased.
            """
            product_type: Optional[Literal["merchandise", "service"]]
            """
            Whether the product was a merchandise or service.
            """
            return_status: Optional[Literal["merchant_rejected", "successful"]]
            """
            Result of cardholder's attempt to return the product.
            """
            returned_at: Optional[int]
            """
            Date when the product was returned or attempted to be returned.
            """

        class Duplicate(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            card_statement: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.
            """
            cash_receipt: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.
            """
            check_image: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            original_transaction: Optional[str]
            """
            Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.
            """

        class Fraudulent(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """

        class MerchandiseNotAsDescribed(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            received_at: Optional[int]
            """
            Date when the product was received.
            """
            return_description: Optional[str]
            """
            Description of the cardholder's attempt to return the product.
            """
            return_status: Optional[Literal["merchant_rejected", "successful"]]
            """
            Result of cardholder's attempt to return the product.
            """
            returned_at: Optional[int]
            """
            Date when the product was returned or attempted to be returned.
            """

        class NotReceived(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            expected_at: Optional[int]
            """
            Date when the cardholder expected to receive the product.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            product_description: Optional[str]
            """
            Description of the merchandise or service that was purchased.
            """
            product_type: Optional[Literal["merchandise", "service"]]
            """
            Whether the product was a merchandise or service.
            """

        class Other(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            product_description: Optional[str]
            """
            Description of the merchandise or service that was purchased.
            """
            product_type: Optional[Literal["merchandise", "service"]]
            """
            Whether the product was a merchandise or service.
            """

        class ServiceNotAsDescribed(StripeObject):
            additional_documentation: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
            """
            canceled_at: Optional[int]
            """
            Date when order was canceled.
            """
            cancellation_reason: Optional[str]
            """
            Reason for canceling the order.
            """
            explanation: Optional[str]
            """
            Explanation of why the cardholder is disputing this transaction.
            """
            received_at: Optional[int]
            """
            Date when the product was received.
            """

        canceled: Optional[Canceled]
        duplicate: Optional[Duplicate]
        fraudulent: Optional[Fraudulent]
        merchandise_not_as_described: Optional[MerchandiseNotAsDescribed]
        not_received: Optional[NotReceived]
        other: Optional[Other]
        reason: Literal[
            "canceled",
            "duplicate",
            "fraudulent",
            "merchandise_not_as_described",
            "not_received",
            "other",
            "service_not_as_described",
        ]
        """
        The reason for filing the dispute. Its value will match the field containing the evidence.
        """
        service_not_as_described: Optional[ServiceNotAsDescribed]
        _inner_class_types = {
            "canceled": Canceled,
            "duplicate": Duplicate,
            "fraudulent": Fraudulent,
            "merchandise_not_as_described": MerchandiseNotAsDescribed,
            "not_received": NotReceived,
            "other": Other,
            "service_not_as_described": ServiceNotAsDescribed,
        }

    class Treasury(StripeObject):
        debit_reversal: Optional[str]
        """
        The Treasury [DebitReversal](https://stripe.com/docs/api/treasury/debit_reversals) representing this Issuing dispute
        """
        received_debit: str
        """
        The Treasury [ReceivedDebit](https://stripe.com/docs/api/treasury/received_debits) that is being disputed.
        """

    class CreateParams(RequestOptions):
        amount: NotRequired["int"]
        """
        The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If not set, defaults to the full transaction amount.
        """
        evidence: NotRequired["Dispute.CreateParamsEvidence"]
        """
        Evidence provided for the dispute.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        transaction: NotRequired["str"]
        """
        The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`.
        """
        treasury: NotRequired["Dispute.CreateParamsTreasury"]
        """
        Params for disputes related to Treasury FinancialAccounts
        """

    class CreateParamsTreasury(TypedDict):
        received_debit: str
        """
        The ID of the ReceivedDebit to initiate an Issuings dispute for.
        """

    class CreateParamsEvidence(TypedDict):
        canceled: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceCanceled"
        ]
        """
        Evidence provided when `reason` is 'canceled'.
        """
        duplicate: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceDuplicate"
        ]
        """
        Evidence provided when `reason` is 'duplicate'.
        """
        fraudulent: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceFraudulent"
        ]
        """
        Evidence provided when `reason` is 'fraudulent'.
        """
        merchandise_not_as_described: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceMerchandiseNotAsDescribed"
        ]
        """
        Evidence provided when `reason` is 'merchandise_not_as_described'.
        """
        not_received: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceNotReceived"
        ]
        """
        Evidence provided when `reason` is 'not_received'.
        """
        other: NotRequired["Literal['']|Dispute.CreateParamsEvidenceOther"]
        """
        Evidence provided when `reason` is 'other'.
        """
        reason: NotRequired[
            "Literal['canceled', 'duplicate', 'fraudulent', 'merchandise_not_as_described', 'not_received', 'other', 'service_not_as_described']"
        ]
        """
        The reason for filing the dispute. The evidence should be submitted in the field of the same name.
        """
        service_not_as_described: NotRequired[
            "Literal['']|Dispute.CreateParamsEvidenceServiceNotAsDescribed"
        ]
        """
        Evidence provided when `reason` is 'service_not_as_described'.
        """

    class CreateParamsEvidenceServiceNotAsDescribed(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        canceled_at: NotRequired["Literal['']|int"]
        """
        Date when order was canceled.
        """
        cancellation_reason: NotRequired["Literal['']|str"]
        """
        Reason for canceling the order.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        received_at: NotRequired["Literal['']|int"]
        """
        Date when the product was received.
        """

    class CreateParamsEvidenceOther(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """

    class CreateParamsEvidenceNotReceived(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        expected_at: NotRequired["Literal['']|int"]
        """
        Date when the cardholder expected to receive the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """

    class CreateParamsEvidenceMerchandiseNotAsDescribed(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        received_at: NotRequired["Literal['']|int"]
        """
        Date when the product was received.
        """
        return_description: NotRequired["Literal['']|str"]
        """
        Description of the cardholder's attempt to return the product.
        """
        return_status: NotRequired[
            "Literal['']|Literal['merchant_rejected', 'successful']"
        ]
        """
        Result of cardholder's attempt to return the product.
        """
        returned_at: NotRequired["Literal['']|int"]
        """
        Date when the product was returned or attempted to be returned.
        """

    class CreateParamsEvidenceFraudulent(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """

    class CreateParamsEvidenceDuplicate(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        card_statement: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.
        """
        cash_receipt: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.
        """
        check_image: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        original_transaction: NotRequired["str"]
        """
        Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.
        """

    class CreateParamsEvidenceCanceled(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        canceled_at: NotRequired["Literal['']|int"]
        """
        Date when order was canceled.
        """
        cancellation_policy_provided: NotRequired["Literal['']|bool"]
        """
        Whether the cardholder was provided with a cancellation policy.
        """
        cancellation_reason: NotRequired["Literal['']|str"]
        """
        Reason for canceling the order.
        """
        expected_at: NotRequired["Literal['']|int"]
        """
        Date when the cardholder expected to receive the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """
        return_status: NotRequired[
            "Literal['']|Literal['merchant_rejected', 'successful']"
        ]
        """
        Result of cardholder's attempt to return the product.
        """
        returned_at: NotRequired["Literal['']|int"]
        """
        Date when the product was returned or attempted to be returned.
        """

    class ListParams(RequestOptions):
        created: NotRequired["Dispute.ListParamsCreated|int"]
        """
        Select Issuing disputes that were created during the given date interval.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            "Literal['expired', 'lost', 'submitted', 'unsubmitted', 'won']"
        ]
        """
        Select Issuing disputes with the given status.
        """
        transaction: NotRequired["str"]
        """
        Select the Issuing dispute for the given transaction.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class ModifyParams(RequestOptions):
        amount: NotRequired["int"]
        """
        The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        evidence: NotRequired["Dispute.ModifyParamsEvidence"]
        """
        Evidence provided for the dispute.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class ModifyParamsEvidence(TypedDict):
        canceled: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceCanceled"
        ]
        """
        Evidence provided when `reason` is 'canceled'.
        """
        duplicate: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceDuplicate"
        ]
        """
        Evidence provided when `reason` is 'duplicate'.
        """
        fraudulent: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceFraudulent"
        ]
        """
        Evidence provided when `reason` is 'fraudulent'.
        """
        merchandise_not_as_described: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceMerchandiseNotAsDescribed"
        ]
        """
        Evidence provided when `reason` is 'merchandise_not_as_described'.
        """
        not_received: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceNotReceived"
        ]
        """
        Evidence provided when `reason` is 'not_received'.
        """
        other: NotRequired["Literal['']|Dispute.ModifyParamsEvidenceOther"]
        """
        Evidence provided when `reason` is 'other'.
        """
        reason: NotRequired[
            "Literal['canceled', 'duplicate', 'fraudulent', 'merchandise_not_as_described', 'not_received', 'other', 'service_not_as_described']"
        ]
        """
        The reason for filing the dispute. The evidence should be submitted in the field of the same name.
        """
        service_not_as_described: NotRequired[
            "Literal['']|Dispute.ModifyParamsEvidenceServiceNotAsDescribed"
        ]
        """
        Evidence provided when `reason` is 'service_not_as_described'.
        """

    class ModifyParamsEvidenceServiceNotAsDescribed(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        canceled_at: NotRequired["Literal['']|int"]
        """
        Date when order was canceled.
        """
        cancellation_reason: NotRequired["Literal['']|str"]
        """
        Reason for canceling the order.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        received_at: NotRequired["Literal['']|int"]
        """
        Date when the product was received.
        """

    class ModifyParamsEvidenceOther(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """

    class ModifyParamsEvidenceNotReceived(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        expected_at: NotRequired["Literal['']|int"]
        """
        Date when the cardholder expected to receive the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """

    class ModifyParamsEvidenceMerchandiseNotAsDescribed(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        received_at: NotRequired["Literal['']|int"]
        """
        Date when the product was received.
        """
        return_description: NotRequired["Literal['']|str"]
        """
        Description of the cardholder's attempt to return the product.
        """
        return_status: NotRequired[
            "Literal['']|Literal['merchant_rejected', 'successful']"
        ]
        """
        Result of cardholder's attempt to return the product.
        """
        returned_at: NotRequired["Literal['']|int"]
        """
        Date when the product was returned or attempted to be returned.
        """

    class ModifyParamsEvidenceFraudulent(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """

    class ModifyParamsEvidenceDuplicate(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        card_statement: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the card statement showing that the product had already been paid for.
        """
        cash_receipt: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Copy of the receipt showing that the product had been paid for in cash.
        """
        check_image: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Image of the front and back of the check that was used to pay for the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        original_transaction: NotRequired["str"]
        """
        Transaction (e.g., ipi_...) that the disputed transaction is a duplicate of. Of the two or more transactions that are copies of each other, this is original undisputed one.
        """

    class ModifyParamsEvidenceCanceled(TypedDict):
        additional_documentation: NotRequired["Literal['']|str"]
        """
        (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Additional documentation supporting the dispute.
        """
        canceled_at: NotRequired["Literal['']|int"]
        """
        Date when order was canceled.
        """
        cancellation_policy_provided: NotRequired["Literal['']|bool"]
        """
        Whether the cardholder was provided with a cancellation policy.
        """
        cancellation_reason: NotRequired["Literal['']|str"]
        """
        Reason for canceling the order.
        """
        expected_at: NotRequired["Literal['']|int"]
        """
        Date when the cardholder expected to receive the product.
        """
        explanation: NotRequired["Literal['']|str"]
        """
        Explanation of why the cardholder is disputing this transaction.
        """
        product_description: NotRequired["Literal['']|str"]
        """
        Description of the merchandise or service that was purchased.
        """
        product_type: NotRequired[
            "Literal['']|Literal['merchandise', 'service']"
        ]
        """
        Whether the product was a merchandise or service.
        """
        return_status: NotRequired[
            "Literal['']|Literal['merchant_rejected', 'successful']"
        ]
        """
        Result of cardholder's attempt to return the product.
        """
        returned_at: NotRequired["Literal['']|int"]
        """
        Date when the product was returned or attempted to be returned.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SubmitParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    amount: int
    """
    Disputed amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). Usually the amount of the `transaction`, but can differ (usually because of currency fluctuation).
    """
    balance_transactions: Optional[List["BalanceTransaction"]]
    """
    List of balance transactions associated with the dispute.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    The currency the `transaction` was made in.
    """
    evidence: Evidence
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["issuing.dispute"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["expired", "lost", "submitted", "unsubmitted", "won"]
    """
    Current status of the dispute.
    """
    transaction: ExpandableField["Transaction"]
    """
    The transaction being disputed.
    """
    treasury: Optional[Treasury]
    """
    [Treasury](https://stripe.com/docs/api/treasury) details related to this dispute if it was created on a [FinancialAccount](/docs/api/treasury/financial_accounts
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Dispute.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Dispute":
        """
        Creates an Issuing Dispute object. Individual pieces of evidence within the evidence object are optional at this point. Stripe only validates that required evidence is present during submission. Refer to [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence) for more details about evidence requirements.
        """
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
        **params: Unpack[
            "Dispute.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Dispute"]:
        """
        Returns a list of Issuing Dispute objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
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
    def modify(
        cls, id: str, **params: Unpack["Dispute.ModifyParams"]
    ) -> "Dispute":
        """
        Updates the specified Issuing Dispute object by setting the values of the parameters passed. Any parameters not provided will be left unchanged. Properties on the evidence object can be unset by passing in an empty string.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Dispute",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Dispute.RetrieveParams"]
    ) -> "Dispute":
        """
        Retrieves an Issuing Dispute object.
        """
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
        **params: Unpack[
            "Dispute.SubmitParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Dispute":
        """
        Submits an Issuing Dispute to the card network. Stripe validates that all evidence fields required for the dispute's reason are present. For more details, see [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence).
        """
        return cast(
            "Dispute",
            cls._static_request(
                "post",
                "/v1/issuing/disputes/{dispute}/submit".format(
                    dispute=util.sanitize_id(dispute)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def submit(
        dispute: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Dispute.SubmitParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Dispute":
        """
        Submits an Issuing Dispute to the card network. Stripe validates that all evidence fields required for the dispute's reason are present. For more details, see [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence).
        """
        ...

    @overload
    def submit(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Dispute.SubmitParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Dispute":
        """
        Submits an Issuing Dispute to the card network. Stripe validates that all evidence fields required for the dispute's reason are present. For more details, see [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence).
        """
        ...

    @class_method_variant("_cls_submit")
    def submit(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Dispute.SubmitParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Dispute":
        """
        Submits an Issuing Dispute to the card network. Stripe validates that all evidence fields required for the dispute's reason are present. For more details, see [Dispute reasons and evidence](https://stripe.com/docs/issuing/purchases/disputes#dispute-reasons-and-evidence).
        """
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/issuing/disputes/{dispute}/submit".format(
                    dispute=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    _inner_class_types = {"evidence": Evidence, "treasury": Treasury}
