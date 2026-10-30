# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class FormUpdateParams(TypedDict):
    appeal: NotRequired["FormUpdateParamsAppeal"]
    """
    Provide this for appeal inquiries.
    """
    authorization_documents: NotRequired[
        "FormUpdateParamsAuthorizationDocuments"
    ]
    """
    Provide this for authorization_documents inquiries.
    """
    product_removal: NotRequired["FormUpdateParamsProductRemoval"]
    """
    Provide this for product_removal inquiries.
    """
    self_funding_context: NotRequired["FormUpdateParamsSelfFundingContext"]
    """
    Provide this for self_funding_context inquiries.
    """
    transaction_context: NotRequired["FormUpdateParamsTransactionContext"]
    """
    Provide this for transaction_context inquiries.
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


class FormUpdateParamsProductRemoval(TypedDict):
    items_removed_at: str
    """
    The timestamp when the prohibited items were removed.
    """


class FormUpdateParamsSelfFundingContext(TypedDict):
    source_of_wealth: NotRequired[
        "FormUpdateParamsSelfFundingContextSourceOfWealth"
    ]
    """
    The connected account's source of wealth.
    """


class FormUpdateParamsSelfFundingContextSourceOfWealth(TypedDict):
    description: str
    """
    A text explanation of the connected account's source of wealth.
    """
    files: List[str]
    """
    IDs of uploaded files evidencing the source of wealth.
    """


class FormUpdateParamsTransactionContext(TypedDict):
    purpose: str
    """
    The purpose of the transaction.
    """
    sender_relationship: NotRequired[str]
    """
    The connected account's relationship to the sender. Optional.
    """
    source_of_funds: NotRequired[
        "FormUpdateParamsTransactionContextSourceOfFunds"
    ]
    """
    Where the funds for the transaction came from.
    """
    use_of_funds: str
    """
    How the funds from the transaction will be used.
    """


class FormUpdateParamsTransactionContextSourceOfFunds(TypedDict):
    description: str
    """
    A text explanation of where the funds for the transaction came from.
    """
    files: List[str]
    """
    IDs of uploaded files evidencing the source of funds.
    """
