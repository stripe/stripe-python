# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class UsBankAccount(StripeObject):
    """
    Use the USBankAccounts API to create and manage US bank accounts objects that you can use to receive funds. Note that these are not interchangeable with v1 Tokens.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.vault.us_bank_account"]] = (
        "v2.core.vault.us_bank_account"
    )

    class AlternativeReference(StripeObject):
        id: str
        """
        The ID of the alternative resource being referenced.
        """
        type: Literal["external_account", "payment_method"]
        """
        The type of the alternative reference (e.g., external_account for V1 external accounts).
        """

    class Verification(StripeObject):
        class MicrodepositVerificationDetails(StripeObject):
            expires: str
            """
            Time when microdeposits will expire and have to be re-sent.
            """
            microdeposit_type: Literal["amounts", "descriptor_code"]
            """
            Microdeposit type can be amounts or descriptor_type.
            """
            sent: str
            """
            Time when microdeposits were sent.
            """

        microdeposit_verification_details: Optional[
            MicrodepositVerificationDetails
        ]
        """
        The microdeposit verification details if the status is awaiting verification.
        """
        status: Literal[
            "awaiting_verification",
            "unverified",
            "verification_failed",
            "verified",
        ]
        """
        The bank account verification status.
        """
        _inner_class_types = {
            "microdeposit_verification_details": MicrodepositVerificationDetails,
        }

    alternative_reference: Optional[AlternativeReference]
    """
    The alternative reference for this payout method, if it's a projected payout method.
    """
    archived: bool
    """
    Whether this USBankAccount object was archived.
    """
    bank_account_type: Literal["checking", "savings"]
    """
    Closed Enum. The type of bank account (checking or savings).
    """
    bank_name: str
    """
    The name of the bank this bank account belongs to. This field is populated automatically by Stripe based on the routing number.
    """
    created: str
    """
    Creation time of the object.
    """
    fedwire_routing_number: Optional[str]
    """
    The fedwire routing number of the bank account.
    """
    financial_connections_account: Optional[str]
    """
    The ID of the Financial Connections Account used to create the bank account.
    """
    id: str
    """
    The ID of the USBankAccount object.
    """
    last4: str
    """
    The last 4 digits of the account number.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.vault.us_bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    routing_number: Optional[str]
    """
    The ACH routing number of the bank account.
    """
    verification: Verification
    """
    The bank account verification details.
    """
    _inner_class_types = {
        "alternative_reference": AlternativeReference,
        "verification": Verification,
    }
