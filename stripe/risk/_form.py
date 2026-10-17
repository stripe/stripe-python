# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.risk._form_modify_params import FormModifyParams
    from stripe.params.risk._form_retrieve_params import FormRetrieveParams


class Form(UpdateableAPIResource["Form"]):
    """
    A risk Form represents a request from Stripe for information about a connected account.
    """

    OBJECT_NAME: ClassVar[Literal["risk.form"]] = "risk.form"

    class Appeal(StripeObject):
        explanation: Optional[str]
        """
        A text explanation for the appeal.
        """

    class AuthorizationDocuments(StripeObject):
        files: Optional[List[str]]
        """
        IDs of uploaded files attached as authorization documents.
        """

    class PaymentProcessing(StripeObject):
        class MultiProcessor(StripeObject):
            class File(StripeObject):
                file: Optional[str]
                """
                ID of the uploaded file.
                """
                tag: Optional[str]
                """
                The document type: `alt_financial_statements`, `recent_bank_statements`, or `payment_receipt`.
                """

            files: Optional[List[File]]
            """
            Files evidencing payments accepted outside Stripe. Each entry includes a file ID and, when supplied, a document type tag.
            """
            value: Optional[str]
            """
            Whether the connected account accepts payments outside Stripe.
            """
            _inner_class_types = {"files": File}

        multi_processor: Optional[MultiProcessor]
        purpose: Optional[str]
        """
        How the connected account uses Stripe.
        """
        stripe_selection_rationale: Optional[str]
        """
        Why the connected account chose Stripe.
        """
        _inner_class_types = {"multi_processor": MultiProcessor}

    class ProductRemoval(StripeObject):
        items_removed_at: Optional[int]
        """
        Time when the prohibited items were removed, measured in seconds since the Unix epoch.
        """

    class ReviewedFields(StripeObject):
        class Attestation(StripeObject):
            attested_at: Optional[int]
            """
            Time when the connected account attested to these fields, measured in seconds since the Unix epoch.
            """
            fields: Optional[List[str]]
            """
            Account field paths covered by this attestation. These are currently returned in v2 Accounts API format, such as `defaults.profile.product_description`.
            """

        attestation: Optional[Attestation]
        _inner_class_types = {"attestation": Attestation}

    class SelfFundingContext(StripeObject):
        class SourceOfWealth(StripeObject):
            description: Optional[str]
            """
            A text explanation of the connected account's source of wealth.
            """
            files: Optional[List[str]]
            """
            IDs of uploaded files evidencing the source of wealth.
            """

        source_of_wealth: Optional[SourceOfWealth]
        _inner_class_types = {"source_of_wealth": SourceOfWealth}

    class Subject(StripeObject):
        fields_to_review: Optional[List[str]]
        """
        Account field paths the connected account must review. These are currently returned in v2 Accounts API format, such as `defaults.profile.product_description`. Present for reviewed fields Forms.
        """
        transactions: Optional[List[str]]
        """
        IDs of the transactions this Form is about. Present for transaction context Forms.
        """

    class TransactionContext(StripeObject):
        class SourceOfFunds(StripeObject):
            description: Optional[str]
            """
            A text explanation of where the funds for the transaction came from.
            """
            files: Optional[List[str]]
            """
            IDs of uploaded files evidencing the source of funds.
            """

        frequency: Optional[str]
        """
        How often the connected account expects transactions like this one. Can be `one_time_payment`, `recurring_subscription`, `repeat_customer`, `split_payment`, or `something_else`. A custom explanation can follow `something_else: `.
        """
        purpose: Optional[str]
        """
        The purpose of the transaction.
        """
        purpose_files: Optional[List[str]]
        """
        IDs of uploaded files evidencing the purpose of the transaction.
        """
        sender_relationship: Optional[str]
        """
        The connected account's relationship to the sender.
        """
        source_of_funds: Optional[SourceOfFunds]
        use_of_funds: Optional[str]
        """
        How the funds from the transaction will be used.
        """
        _inner_class_types = {"source_of_funds": SourceOfFunds}

    appeal: Optional[Appeal]
    authorization_documents: Optional[AuthorizationDocuments]
    closed_at: Optional[int]
    """
    Time at which the Form closed, measured in seconds since the Unix epoch.
    """
    created: Optional[int]
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If it exists in a sandbox, the value is `false`.
    """
    object: Literal["risk.form"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    opened_at: Optional[int]
    """
    Time at which the Form opened, measured in seconds since the Unix epoch.
    """
    payment_processing: Optional[PaymentProcessing]
    product_removal: Optional[ProductRemoval]
    reviewed_fields: Optional[ReviewedFields]
    self_funding_context: Optional[SelfFundingContext]
    status: Literal["closed", "open"]
    """
    The current status of the Form.
    """
    subject: Optional[Subject]
    transaction_context: Optional[TransactionContext]
    type: Union[
        Literal[
            "appeal",
            "authorization_documents",
            "payment_processing",
            "product_removal",
            "reviewed_fields",
            "self_funding_context",
            "transaction_context",
        ],
        str,
    ]
    """
    The type of information requested by Stripe.
    """

    @classmethod
    def modify(
        cls, id: str, /, **params: Unpack["FormModifyParams"]
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | A submitted field is not supported by this Form type. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Form",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, /, **params: Unpack["FormModifyParams"]
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | A submitted field is not supported by this Form type. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Form",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FormRetrieveParams"]
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FormRetrieveParams"]
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "appeal": Appeal,
        "authorization_documents": AuthorizationDocuments,
        "payment_processing": PaymentProcessing,
        "product_removal": ProductRemoval,
        "reviewed_fields": ReviewedFields,
        "self_funding_context": SelfFundingContext,
        "subject": Subject,
        "transaction_context": TransactionContext,
    }
