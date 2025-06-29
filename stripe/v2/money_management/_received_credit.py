# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class ReceivedCredit(StripeObject):
    """
    Use ReceivedCredits API to retrieve information on when, where, and how funds are sent into your FinancialAccount.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.received_credit"]] = (
        "v2.money_management.received_credit"
    )

    class BalanceTransfer(StripeObject):
        from_account: Optional[str]
        """
        The ID of the account that owns the source object originated the ReceivedCredit.
        """
        outbound_payment: Optional[str]
        """
        The ID of the outbound payment object that originated the ReceivedCredit.
        """
        outbound_transfer: Optional[str]
        """
        The ID of the outbound transfer object that originated the ReceivedCredit.
        """
        payout_v1: Optional[str]
        """
        The ID of the payout object that originated the ReceivedCredit.
        """
        type: Literal["outbound_payment", "outbound_transfer", "payout_v1"]
        """
        Open Enum. The type of Stripe Money Movement that originated the ReceivedCredit.
        """

    class BankTransfer(StripeObject):
        class GbBankAccount(StripeObject):
            account_holder_name: Optional[str]
            """
            The bank name the transfer was received from.
            """
            bank_name: Optional[str]
            """
            The bank name the transfer was received from.
            """
            last4: Optional[str]
            """
            The last 4 digits of the account number that originated the transfer.
            """
            network: Literal["fps"]
            """
            Open Enum. The money transmission network used to send funds for this ReceivedCredit.
            """
            sort_code: Optional[str]
            """
            The sort code of the account that originated the transfer.
            """

        class UsBankAccount(StripeObject):
            bank_name: Optional[str]
            """
            The bank name the transfer was received from.
            """
            last4: Optional[str]
            """
            The last 4 digits of the account number that originated the transfer.
            """
            network: Literal["ach", "rtp", "us_domestic_wire"]
            """
            Open Enum. The money transmission network used to send funds for this ReceivedCredit.
            """
            routing_number: Optional[str]
            """
            The routing number of the account that originated the transfer.
            """

        financial_address: str
        """
        Financial Address on which funds for ReceivedCredit were received.
        """
        gb_bank_account: Optional[GbBankAccount]
        """
        Hash containing the transaction bank details. Present if `payment_method_type` field value is `gb_bank_account`.
        """
        payment_method_type: Literal["gb_bank_account", "us_bank_account"]
        """
        Open Enum. Indicates the type of source via from which external funds originated.
        """
        statement_descriptor: Optional[str]
        """
        Freeform string set by originator of the external ReceivedCredit.
        """
        us_bank_account: Optional[UsBankAccount]
        """
        Hash containing the transaction bank details. Present if `payment_method_type` field value is `us_bank_account`.
        """
        _inner_class_types = {
            "gb_bank_account": GbBankAccount,
            "us_bank_account": UsBankAccount,
        }

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Literal[
                "capability_inactive",
                "currency_unsupported_on_financial_address",
                "financial_address_inactive",
                "stripe_rejected",
            ]
            """
            Open Enum. The `failed` status reason.
            """

        class Returned(StripeObject):
            reason: Literal["originator_initiated_reversal"]
            """
            Open Enum. The `returned` status reason.
            """

        failed: Optional[Failed]
        """
        Hash that provides additional information regarding the reason behind a `failed` ReceivedCredit status. It is only present when the ReceivedCredit status is `failed`.
        """
        returned: Optional[Returned]
        """
        Hash that provides additional information regarding the reason behind a `returned` ReceivedCredit status. It is only present when the ReceivedCredit status is `returned`.
        """
        _inner_class_types = {"failed": Failed, "returned": Returned}

    class StatusTransitions(StripeObject):
        failed_at: Optional[str]
        """
        Timestamp describing when the ReceivedCredit was marked as `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        returned_at: Optional[str]
        """
        Timestamp describing when the ReceivedCredit changed status to `returned`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        succeeded_at: Optional[str]
        """
        Timestamp describing when the ReceivedCredit was marked as `succeeded`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """

    amount: Amount
    """
    The amount and currency of the ReceivedCredit.
    """
    balance_transfer: Optional[BalanceTransfer]
    """
    This object stores details about the originating Stripe transaction that resulted in the ReceivedCredit. Present if `type` field value is `balance_transfer`.
    """
    bank_transfer: Optional[BankTransfer]
    """
    This object stores details about the originating banking transaction that resulted in the ReceivedCredit. Present if `type` field value is `external_credit`.
    """
    created: str
    """
    Time at which the ReceivedCredit was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    description: Optional[str]
    """
    Freeform string set by originator of the ReceivedCredit.
    """
    financial_account: str
    """
    Financial Account ID on which funds for ReceivedCredit were received.
    """
    id: str
    """
    Unique identifier for the ReceivedCredit.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.received_credit"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A hosted transaction receipt URL that is provided when money movement is considered regulated under Stripe's money transmission licenses.
    """
    status: Literal["failed", "pending", "returned", "succeeded"]
    """
    Open Enum. The status of the ReceivedCredit.
    """
    status_details: Optional[StatusDetails]
    """
    This hash contains detailed information that elaborates on the specific status of the ReceivedCredit. e.g the reason behind a failure if the status is marked as `failed`.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when the object transitioned to a particular status.
    """
    type: Literal["balance_transfer", "bank_transfer", "external_credit"]
    """
    Open Enum. The type of flow that caused the ReceivedCredit.
    """
    _inner_class_types = {
        "balance_transfer": BalanceTransfer,
        "bank_transfer": BankTransfer,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
    }
