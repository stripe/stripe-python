# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class FormUpdateParams(TypedDict):
    appeal: NotRequired["FormUpdateParamsAppeal"]
    """
    Provide this for Forms of type `appeal`.
    """
    authorization_documents: NotRequired[
        "FormUpdateParamsAuthorizationDocuments"
    ]
    """
    Provide this for Forms of type `authorization_documents`.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_processing: NotRequired["FormUpdateParamsPaymentProcessing"]
    """
    Provide this for Forms of type `payment_processing`.
    """
    product_removal: NotRequired["FormUpdateParamsProductRemoval"]
    """
    Provide this for Forms of type `product_removal`.
    """
    reviewed_fields: NotRequired["FormUpdateParamsReviewedFields"]
    """
    Provide this for Forms of type `reviewed_fields`.
    """
    self_funding_context: NotRequired["FormUpdateParamsSelfFundingContext"]
    """
    Provide this for Forms of type `self_funding_context`.
    """
    transaction_context: NotRequired["FormUpdateParamsTransactionContext"]
    """
    Provide this for Forms of type `transaction_context`.
    """


class FormUpdateParamsAppeal(TypedDict):
    explanation: str
    """
    A text explanation for the appeal.
    """


class FormUpdateParamsAuthorizationDocuments(TypedDict):
    files: List[str]
    """
    IDs of uploaded files to attach as authorization documents.
    """


class FormUpdateParamsPaymentProcessing(TypedDict):
    multi_processor: NotRequired[
        "FormUpdateParamsPaymentProcessingMultiProcessor"
    ]
    """
    Payments the connected account accepts outside Stripe.
    """
    purpose: NotRequired[str]
    """
    How the connected account uses Stripe.
    """
    stripe_selection_rationale: NotRequired[str]
    """
    Why the connected account chose Stripe.
    """


class FormUpdateParamsPaymentProcessingMultiProcessor(TypedDict):
    files: NotRequired[
        List["FormUpdateParamsPaymentProcessingMultiProcessorFile"]
    ]
    """
    Files evidencing payments accepted outside Stripe. Each entry carries a tag naming the document type so a reviewer can distinguish statement types without opening the file.
    """
    value: NotRequired[str]
    """
    Whether the connected account accepts payments outside Stripe.
    """


class FormUpdateParamsPaymentProcessingMultiProcessorFile(TypedDict):
    file: str
    """
    ID of the uploaded file. Upload using /v1/files before referencing it here.
    """
    tag: NotRequired[str]
    """
    What kind of document this is. One of alt_financial_statements, recent_bank_statements, or payment_receipt.
    """


class FormUpdateParamsProductRemoval(TypedDict):
    items_removed_at: int
    """
    The Unix timestamp when the prohibited items were removed.
    """


class FormUpdateParamsReviewedFields(TypedDict):
    attestation: "FormUpdateParamsReviewedFieldsAttestation"
    """
    The connected account's attestation that the named account field values are accurate. Update inaccurate values through the Accounts API before attesting.
    """


class FormUpdateParamsReviewedFieldsAttestation(TypedDict):
    attested_at: NotRequired[int]
    """
    The Unix timestamp when the connected account attested to these fields.
    """
    fields: NotRequired[List[str]]
    """
    Account field paths in the currently accepted v2 Accounts API format, for example `defaults.profile.product_description`.
    """


class FormUpdateParamsSelfFundingContext(TypedDict):
    source_of_wealth: NotRequired[
        "FormUpdateParamsSelfFundingContextSourceOfWealth"
    ]
    """
    The connected account's source of wealth.
    """


class FormUpdateParamsSelfFundingContextSourceOfWealth(TypedDict):
    description: NotRequired[str]
    """
    A text explanation of the connected account's source of wealth.
    """
    files: NotRequired[List[str]]
    """
    IDs of uploaded files evidencing the source of wealth.
    """


class FormUpdateParamsTransactionContext(TypedDict):
    frequency: NotRequired[str]
    """
    How often the connected account expects transactions like this one. One of one_time_payment, recurring_subscription, repeat_customer, split_payment, or something_else.
    """
    purpose: NotRequired[str]
    """
    The purpose of the transaction.
    """
    purpose_files: NotRequired[List[str]]
    """
    IDs of uploaded files evidencing the purpose of the transaction.
    """
    sender_relationship: NotRequired[str]
    """
    The connected account's relationship to the sender.
    """
    source_of_funds: NotRequired[
        "FormUpdateParamsTransactionContextSourceOfFunds"
    ]
    """
    Where the funds for the transaction came from.
    """
    use_of_funds: NotRequired[str]
    """
    How the funds from the transaction will be used.
    """


class FormUpdateParamsTransactionContextSourceOfFunds(TypedDict):
    description: NotRequired[str]
    """
    A text explanation of where the funds for the transaction came from.
    """
    files: NotRequired[List[str]]
    """
    IDs of uploaded files evidencing the source of funds.
    """
