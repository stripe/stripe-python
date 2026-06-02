# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class FeeEntry(StripeObject):
    """
    A FeeEntry is the atomic, append-only record of an assessed fee.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.fee_entry"]] = "v2.core.fee_entry"

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

    class ChargedBy(StripeObject):
        class Application(StripeObject):
            feature_name: Optional[str]
            """
            Human-readable product name, e.g. "Card payments - Stripe fee".
            """

        class Network(StripeObject):
            feature_name: Optional[str]
            """
            Human-readable product name, e.g. "Card payments - Stripe fee".
            """

        class Stripe(StripeObject):
            feature_name: Optional[str]
            """
            Human-readable product name, e.g. "Card payments - Stripe fee".
            """

        application: Optional[Application]
        """
        Details for a fee charged by a Connect application.
        """
        network: Optional[Network]
        """
        Details for a fee charged by the payment network.
        """
        stripe: Optional[Stripe]
        """
        Details for a fee charged by Stripe.
        """
        type: Literal["application", "network", "stripe"]
        """
        The type of entity that charged this fee.
        """
        _inner_class_types = {
            "application": Application,
            "network": Network,
            "stripe": Stripe,
        }

    class IncurredBy(StripeObject):
        account: Optional[str]
        """
        The account that incurred the usage (may differ from the billing account).
        """
        id: str
        """
        Public API object id, e.g. ch_xxx.
        """
        occurred_at: Optional[str]
        """
        Timestamp of when the usage event occurred.
        """
        type: str
        """
        Public API object type: "charge", "payment", "refund", "dispute", "payout", etc.
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
        The tax amount calculated for this fee.
        """
        _inner_class_types = {"amount": Amount}

    amount: Amount
    """
    The fee amount.
    """
    charged_by: ChargedBy
    """
    The entity that assessed this fee.
    """
    created: str
    """
    Timestamp of when this fee entry was created.
    """
    fee_batch: Optional[str]
    """
    The ID of the FeeBatch that collected this fee, if any.
    """
    id: str
    """
    Unique identifier for the FeeEntry.
    """
    incurred_by: IncurredBy
    """
    The usage event that caused this fee to be assessed.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode, or `false` if in test mode.
    """
    object: Literal["v2.core.fee_entry"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reason: Literal[
        "other",
        "processing_fee",
        "refund",
        "refund_failure",
        "reprice",
        "tier_true_up",
    ]
    """
    The reason this fee entry was created.
    """
    tax: Optional[Tax]
    """
    The tax portion of the fee, if applicable.
    """
    type: Literal["application_fee", "passthrough_fee", "stripe_fee"]
    """
    The category of this fee.
    """
    _inner_class_types = {
        "amount": Amount,
        "charged_by": ChargedBy,
        "incurred_by": IncurredBy,
        "tax": Tax,
    }
