# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Inquiry(StripeObject):
    """
    A risk inquiry represents a request from Stripe for information about a connected account.
    """

    OBJECT_NAME: ClassVar[Literal["v2.risk.inquiry"]] = "v2.risk.inquiry"

    class Appeal(StripeObject):
        explanation: str
        """
        A text explanation for the appeal.
        """

    class AuthorizationDocuments(StripeObject):
        files: List[str]
        """
        IDs of uploaded files to attach as authorization documents.
        """

    class ProductRemoval(StripeObject):
        items_removed_at: str
        """
        The timestamp when the prohibited items were removed.
        """

    appeal: Optional[Appeal]
    """
    Data for appeal inquiries. Only present when type is appeal.
    """
    authorization_documents: Optional[AuthorizationDocuments]
    """
    Data for authorization_documents inquiries. Only present when type is authorization_documents.
    """
    closed_at: str
    """
    Time at which the inquiry was closed.
    """
    created: str
    """
    Time at which the inquiry was created.
    """
    id: str
    """
    Unique identifier for the inquiry.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.risk.inquiry"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    opened_at: str
    """
    Time at which the inquiry was opened.
    """
    product_removal: Optional[ProductRemoval]
    """
    Data for product_removal inquiries. Only present when type is product_removal.
    """
    status: Literal["closed", "open"]
    """
    The current status of the inquiry.
    """
    type: Union[
        Literal["appeal", "authorization_documents", "product_removal"], str
    ]
    """
    The type of inquiry.
    """
    _inner_class_types = {
        "appeal": Appeal,
        "authorization_documents": AuthorizationDocuments,
        "product_removal": ProductRemoval,
    }
