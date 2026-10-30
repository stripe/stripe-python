# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Form(StripeObject):
    """
    A risk Form represents a request from Stripe for information about a connected account.
    """

    OBJECT_NAME: ClassVar[Literal["v2.risk.form"]] = "v2.risk.form"

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

    class SelfFundingContext(StripeObject):
        class SourceOfWealth(StripeObject):
            description: str
            """
            A text explanation of the connected account's source of wealth.
            """
            files: List[str]
            """
            IDs of uploaded files evidencing the source of wealth.
            """

        source_of_wealth: Optional[SourceOfWealth]
        """
        The connected account's source of wealth.
        """
        _inner_class_types = {"source_of_wealth": SourceOfWealth}

    class Subject(StripeObject):
        transaction: Optional[str]
        """
        ID of the transaction this Form is about. Present only for transaction_context
        Forms. Absent for other Form types.
        """
        transactions: Optional[List[str]]
        """
        IDs of the transactions this inquiry is about.
        """

    class TransactionContext(StripeObject):
        class SourceOfFunds(StripeObject):
            description: str
            """
            A text explanation of where the funds for the transaction came from.
            """
            files: List[str]
            """
            IDs of uploaded files evidencing the source of funds.
            """

        purpose: str
        """
        The purpose of the transaction.
        """
        sender_relationship: Optional[str]
        """
        The connected account's relationship to the sender. Optional.
        """
        source_of_funds: Optional[SourceOfFunds]
        """
        Where the funds for the transaction came from.
        """
        use_of_funds: str
        """
        How the funds from the transaction will be used.
        """
        _inner_class_types = {"source_of_funds": SourceOfFunds}

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
    Time at which the Form was closed.
    """
    created: str
    """
    Time at which the Form was created.
    """
    id: str
    """
    Unique identifier for the Form.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.risk.form"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    opened_at: str
    """
    Time at which the Form was opened.
    """
    product_removal: Optional[ProductRemoval]
    """
    Data for product_removal inquiries. Only present when type is product_removal.
    """
    self_funding_context: Optional[SelfFundingContext]
    """
    Data for self_funding_context inquiries. Only present when type is self_funding_context.
    """
    status: Literal["closed", "open"]
    """
    The current status of the Form.
    """
    subject: Optional[Subject]
    """
    What this Form was raised about, as a typed object. Only present when the Form
    is scoped to a specific object. Absent when the Form covers the account as a whole.
    """
    transaction_context: Optional[TransactionContext]
    """
    Data for transaction_context inquiries. Only present when type is transaction_context.
    """
    type: Union[
        Literal[
            "appeal",
            "authorization_documents",
            "product_removal",
            "self_funding_context",
            "transaction_context",
        ],
        str,
    ]
    """
    The type of Form.
    """
    _inner_class_types = {
        "appeal": Appeal,
        "authorization_documents": AuthorizationDocuments,
        "product_removal": ProductRemoval,
        "self_funding_context": SelfFundingContext,
        "subject": Subject,
        "transaction_context": TransactionContext,
    }
