# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class GbBankAccount(StripeObject):
    """
    Use the GBBankAccounts API to create and manage GB bank account objects
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.vault.gb_bank_account"]] = (
        "v2.core.vault.gb_bank_account"
    )

    class ConfirmationOfPayee(StripeObject):
        class Result(StripeObject):
            class Matched(StripeObject):
                business_type: Optional[Literal["business", "personal"]]
                """
                The business type given by the bank for this account, in case of a MATCH or PARTIAL_MATCH.
                Closed enum.
                """
                name: Optional[str]
                """
                The name given by the bank for this account, in case of a MATCH or PARTIAL_MATCH.
                """

            class Provided(StripeObject):
                business_type: Literal["business", "personal"]
                """
                The provided or Legal Entity business type to match against the CoP service. Closed enum.
                """
                name: str
                """
                The provided or Legal Entity name to match against the CoP service.
                """

            created: str
            """
            When the CoP result was created.
            """
            match_result: Literal[
                "match", "mismatch", "partial_match", "unavailable"
            ]
            """
            Whether or not the information of the bank account matches what you have provided. Closed enum.
            """
            matched: Matched
            """
            The fields that CoP service matched against. Only has value if MATCH or PARTIAL_MATCH, empty otherwise.
            """
            message: str
            """
            Human-readable message describing the match result.
            """
            provided: Provided
            """
            The fields that are matched against what the network has on file.
            """
            _inner_class_types = {"matched": Matched, "provided": Provided}

        result: Result
        """
        The result of the Confirmation of Payee check, once the check has been initiated. Closed enum.
        """
        status: Literal["awaiting_acknowledgement", "confirmed", "uninitiated"]
        """
        The current state of Confirmation of Payee on this bank account. Closed enum.
        """
        _inner_class_types = {"result": Result}

    archived: bool
    """
    Whether this bank account object was archived. Bank account objects can be archived through
    the /archive API, and they will not be automatically archived by Stripe. Archived bank account objects
    cannot be used as outbound destinations and will not appear in the outbound destination list.
    """
    bank_account_type: Literal["checking", "savings"]
    """
    Closed Enum. The type of the bank account (checking or savings).
    """
    bank_name: str
    """
    The name of the bank.
    """
    confirmation_of_payee: ConfirmationOfPayee
    """
    Information around the status of Confirmation of Payee matching done on this bank account.
    Confirmation of Payee is a name matching service that must be done before making OutboundPayments in the UK.
    """
    created: str
    """
    Creation time.
    """
    id: str
    """
    The ID of the GBBankAccount object.
    """
    last4: str
    """
    The last 4 digits of the account number or IBAN.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.vault.gb_bank_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    sort_code: str
    """
    The Sort Code of the bank account.
    """
    _inner_class_types = {"confirmation_of_payee": ConfirmationOfPayee}
