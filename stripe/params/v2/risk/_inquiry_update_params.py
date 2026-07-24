# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class InquiryUpdateParams(TypedDict):
    appeal: NotRequired["InquiryUpdateParamsAppeal"]
    """
    Provide this for appeal inquiries.
    """
    authorization_documents: NotRequired[
        "InquiryUpdateParamsAuthorizationDocuments"
    ]
    """
    Provide this for authorization_documents inquiries.
    """
    product_removal: NotRequired["InquiryUpdateParamsProductRemoval"]
    """
    Provide this for product_removal inquiries.
    """


class InquiryUpdateParamsAppeal(TypedDict):
    explanation: str
    """
    A text explanation for the appeal.
    """


class InquiryUpdateParamsAuthorizationDocuments(TypedDict):
    files: List[str]
    """
    IDs of uploaded files to attach as authorization documents.
    """


class InquiryUpdateParamsProductRemoval(TypedDict):
    items_removed_at: str
    """
    The timestamp when the prohibited items were removed.
    """
