# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class FeeBatch(StripeObject):
    """
    A FeeBatch represents a settlement grouping of fees.
    It bridges the fee domain with actual money movement, tracking what was settled and how.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.fee_batch"]] = "v2.core.fee_batch"

    class Adjustments(StripeObject):
        class TaxAdjustment(StripeObject):
            currency: str
            """
            A lowercase alpha3 currency code like "usd"
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """
            value: str
            """
            In major units like "1.23" for 1.23 USD
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """

        tax_adjustment: Optional[TaxAdjustment]
        """
        The amount of tax adjusted for this batch.
        """
        _inner_class_types = {"tax_adjustment": TaxAdjustment}

    class Amount(StripeObject):
        currency: str
        """
        A lowercase alpha3 currency code like "usd"
        For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
        """
        value: str
        """
        In major units like "1.23" for 1.23 USD
        For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
        """

    class CollectedBy(StripeObject):
        type: Literal["application", "network", "stripe"]
        """
        The type of entity that collected this batch.
        """

    class CollectionRecord(StripeObject):
        class Amount(StripeObject):
            currency: str
            """
            A lowercase alpha3 currency code like "usd"
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """
            value: str
            """
            In major units like "1.23" for 1.23 USD
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """

        class Tax(StripeObject):
            class Amount(StripeObject):
                currency: str
                """
                A lowercase alpha3 currency code like "usd"
                For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
                """
                value: str
                """
                In major units like "1.23" for 1.23 USD
                For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
                """

            amount: Amount
            """
            The tax amount collected via this record.
            """
            _inner_class_types = {"amount": Amount}

        amount: Amount
        """
        The fee amount collected via this record.
        """
        balance_transaction: Optional[str]
        """
        The ID of the associated v1 balance transaction.
        """
        credit_transaction: Optional[str]
        """
        The ID of the associated credit transaction.
        """
        money_management_transaction: Optional[str]
        """
        The ID of the associated v2 money management transaction.
        """
        payable_invoice: Optional[str]
        """
        The ID of the associated accounts-receivable invoice.
        """
        tax: Optional[Tax]
        """
        The tax amount collected via this record.
        """
        type: Literal[
            "balance_transaction",
            "credit_transaction",
            "money_management_transaction",
            "payable_invoice",
        ]
        """
        The type of money movement object.
        """
        _inner_class_types = {"amount": Amount, "tax": Tax}

    class StatusTransitions(StripeObject):
        billed_at: Optional[str]
        """
        Timestamp of when the batch transitioned to BILLED, if applicable.
        """

    class Tax(StripeObject):
        class Amount(StripeObject):
            currency: str
            """
            A lowercase alpha3 currency code like "usd"
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """
            value: str
            """
            In major units like "1.23" for 1.23 USD
            For the taxonomy label choice, see SECURE_FRAMEWORKS-2849.
            """

        amount: Amount
        """
        The tax amount included in this batch.
        """
        _inner_class_types = {"amount": Amount}

    adjustments: Optional[Adjustments]
    """
    Adjustments applied to this batch.
    """
    amount: Amount
    """
    The total fee amount billed in this batch.
    """
    collected_by: CollectedBy
    """
    The entity that collected this batch.
    """
    collection_records: List[CollectionRecord]
    """
    The money movement records associated with collecting this batch.
    """
    created: str
    """
    Timestamp of when this batch was created.
    """
    id: str
    """
    Unique identifier for the FeeBatch.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode, or `false` if in test mode.
    """
    object: Literal["v2.core.fee_batch"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["billed", "pending"]
    """
    The current state of this batch.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for each status transition.
    """
    tax: Optional[Tax]
    """
    The tax amount included in this batch.
    """
    _inner_class_types = {
        "adjustments": Adjustments,
        "amount": Amount,
        "collected_by": CollectedBy,
        "collection_records": CollectionRecord,
        "status_transitions": StatusTransitions,
        "tax": Tax,
    }
