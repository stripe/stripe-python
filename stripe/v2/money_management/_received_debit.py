# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class ReceivedDebit(StripeObject):
    """
    ReceivedDebit resource
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.received_debit"]] = (
        "v2.money_management.received_debit"
    )

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    class BalanceTransfer(StripeObject):
        topup: Optional[str]
        """
        The ID of the topup object that originated the ReceivedDebit.
        """
        type: Literal["topup"]
        """
        Open Enum. The type of balance transfer that originated the ReceivedDebit.
        """

    class BankTransfer(StripeObject):
        class UsBankAccount(StripeObject):
            bank_name: Optional[str]
            """
            The name of the bank the debit originated from.
            """
            network: Literal["ach"]
            """
            Open Enum. The bank network the debit was originated on.
            """
            routing_number: Optional[str]
            """
            The routing number of the bank that originated the debit.
            """

        financial_address: str
        """
        The Financial Address that was debited.
        """
        origin_type: Literal["us_bank_account"]
        """
        Open Enum. Indicates the origin type through which this debit was initiated.
        """
        payment_method_type: Literal["us_bank_account"]
        """
        Open Enum. The type of the payment method used to originate the debit.
        """
        statement_descriptor: Optional[str]
        """
        The statement descriptor set by the originator of the debit.
        """
        us_bank_account: UsBankAccount
        """
        The payment method used to originate the debit.
        """
        _inner_class_types = {"us_bank_account": UsBankAccount}

    class ExternalAmount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    class StatusDetails(StripeObject):
        class Failed(StripeObject):
            reason: Literal[
                "financial_address_inactive",
                "insufficient_funds",
                "stripe_rejected",
            ]
            """
            Open Enum. The reason for the failure of the ReceivedDebit.
            """

        failed: Failed
        """
        Information that elaborates on the `failed` status of a ReceivedDebit.
        It is only present when the ReceivedDebit status is `failed`.
        """
        _inner_class_types = {"failed": Failed}

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `canceled`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """
        failed_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `failed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """
        succeeded_at: Optional[str]
        """
        The time when the ReceivedDebit was marked as `succeeded`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
        """

    class StripeBalancePayment(StripeObject):
        debit_agreement: Optional[str]
        """
        ID of the debit agreement associated with this payment.
        """
        statement_descriptor: Optional[str]
        """
        Statement descriptor for the Stripe Balance Payment.
        """

    amount: Amount
    """
    Amount and currency of the ReceivedDebit.
    """
    balance_transfer: Optional[BalanceTransfer]
    """
    This object stores details about the balance transfer object that resulted in the ReceivedDebit.
    """
    bank_transfer: Optional[BankTransfer]
    """
    This object stores details about the originating banking transaction that resulted in the ReceivedDebit. Present if `type` field value is `bank_transfer`.
    """
    created: str
    """
    The time at which the ReceivedDebit was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: `2022-09-18T13:22:18.123Z`.
    """
    description: Optional[str]
    """
    Freeform string sent by the originator of the ReceivedDebit.
    """
    external_amount: Optional[ExternalAmount]
    """
    The amount and currency of the original/external debit request.
    """
    financial_account: str
    """
    Financial Account on which funds for ReceivedDebit were debited.
    """
    id: str
    """
    Unique identifier for the ReceivedDebit.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.received_debit"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    receipt_url: Optional[str]
    """
    A link to the Stripe-hosted receipt for this ReceivedDebit.
    """
    status: Literal["canceled", "failed", "pending", "returned", "succeeded"]
    """
    Open Enum. The status of the ReceivedDebit.
    """
    status_details: Optional[StatusDetails]
    """
    Detailed information about the status of the ReceivedDebit.
    """
    status_transitions: Optional[StatusTransitions]
    """
    The time at which the ReceivedDebit transitioned to a particular status.
    """
    stripe_balance_payment: Optional[StripeBalancePayment]
    """
    This object stores details about the Stripe Balance Payment that resulted in the ReceivedDebit.
    """
    type: Literal[
        "balance_transfer",
        "bank_transfer",
        "external_debit",
        "stripe_balance_payment",
    ]
    """
    Open enum, the type of the received debit.
    """
    _inner_class_types = {
        "amount": Amount,
        "balance_transfer": BalanceTransfer,
        "bank_transfer": BankTransfer,
        "external_amount": ExternalAmount,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "stripe_balance_payment": StripeBalancePayment,
    }
