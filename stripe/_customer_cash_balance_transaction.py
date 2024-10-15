# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from typing import ClassVar, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe._customer import Customer
    from stripe._payment_intent import PaymentIntent
    from stripe._refund import Refund


class CustomerCashBalanceTransaction(StripeObject):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid
    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.
    """

    OBJECT_NAME: ClassVar[Literal["customer_cash_balance_transaction"]] = (
        "customer_cash_balance_transaction"
    )

    class AdjustedForOverdraft(StripeObject):
        balance_transaction: ExpandableField["BalanceTransaction"]
        """
        The [Balance Transaction](https://stripe.com/docs/api/balance_transactions/object) that corresponds to funds taken out of your Stripe balance.
        """
        linked_transaction: ExpandableField["CustomerCashBalanceTransaction"]
        """
        The [Cash Balance Transaction](https://stripe.com/docs/api/cash_balance_transactions/object) that brought the customer balance negative, triggering the clawback of funds.
        """

    class AppliedToPayment(StripeObject):
        payment_intent: ExpandableField["PaymentIntent"]
        """
        The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were applied to.
        """

    class Funded(StripeObject):
        class BankTransfer(StripeObject):
            class EuBankTransfer(StripeObject):
                bic: Optional[str]
                """
                The BIC of the bank of the sender of the funding.
                """
                iban_last4: Optional[str]
                """
                The last 4 digits of the IBAN of the sender of the funding.
                """
                sender_name: Optional[str]
                """
                The full name of the sender, as supplied by the sending bank.
                """

            class GbBankTransfer(StripeObject):
                account_number_last4: Optional[str]
                """
                The last 4 digits of the account number of the sender of the funding.
                """
                sender_name: Optional[str]
                """
                The full name of the sender, as supplied by the sending bank.
                """
                sort_code: Optional[str]
                """
                The sort code of the bank of the sender of the funding
                """

            class JpBankTransfer(StripeObject):
                sender_bank: Optional[str]
                """
                The name of the bank of the sender of the funding.
                """
                sender_branch: Optional[str]
                """
                The name of the bank branch of the sender of the funding.
                """
                sender_name: Optional[str]
                """
                The full name of the sender, as supplied by the sending bank.
                """

            class UsBankTransfer(StripeObject):
                network: Optional[Literal["ach", "domestic_wire_us", "swift"]]
                """
                The banking network used for this funding.
                """
                sender_name: Optional[str]
                """
                The full name of the sender, as supplied by the sending bank.
                """

            eu_bank_transfer: Optional[EuBankTransfer]
            gb_bank_transfer: Optional[GbBankTransfer]
            jp_bank_transfer: Optional[JpBankTransfer]
            reference: Optional[str]
            """
            The user-supplied reference field on the bank transfer.
            """
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
            """
            The funding method type used to fund the customer balance. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
            """
            us_bank_transfer: Optional[UsBankTransfer]
            _inner_class_types = {
                "eu_bank_transfer": EuBankTransfer,
                "gb_bank_transfer": GbBankTransfer,
                "jp_bank_transfer": JpBankTransfer,
                "us_bank_transfer": UsBankTransfer,
            }

        bank_transfer: BankTransfer
        _inner_class_types = {"bank_transfer": BankTransfer}

    class RefundedFromPayment(StripeObject):
        refund: ExpandableField["Refund"]
        """
        The [Refund](https://stripe.com/docs/api/refunds/object) that moved these funds into the customer's cash balance.
        """

    class TransferredToBalance(StripeObject):
        balance_transaction: ExpandableField["BalanceTransaction"]
        """
        The [Balance Transaction](https://stripe.com/docs/api/balance_transactions/object) that corresponds to funds transferred to your Stripe balance.
        """

    class UnappliedFromPayment(StripeObject):
        payment_intent: ExpandableField["PaymentIntent"]
        """
        The [Payment Intent](https://stripe.com/docs/api/payment_intents/object) that funds were unapplied from.
        """

    class CreateParams(RequestOptions):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: str
        """
        The ID of the customer.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        funded: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFunded"
        ]
        """
        If this is a `type=funded` transaction, contains information about the funding.
        """
        funding_reversed: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundingReversed"
        ]
        """
        If this is a `type=funding_reversed` transaction, contains information about the reversal of a funding.
        """
        net_amount: NotRequired[int]
        """
        The amount associated with the cash balance transaction. Only applicable to transactions of type `funded`.
        """
        type: Literal["funded", "funding_reversed"]
        """
        The type of cash balance transaction to generate.
        """

    class CreateParamsFunded(TypedDict):
        bank_transfer: (
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransfer"
        )

    class CreateParamsFundedBankTransfer(TypedDict):
        ca_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferCaBankTransfer"
        ]
        """
        CA-specific details of the bank transfer funding.
        """
        eu_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferEuBankTransfer"
        ]
        """
        EU-specific details of the bank transfer funding.
        """
        gb_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferGbBankTransfer"
        ]
        """
        GB-specific details of the bank transfer funding.
        """
        jp_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferJpBankTransfer"
        ]
        """
        JP-specific details of the bank transfer funding.
        """
        mx_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferMxBankTransfer"
        ]
        """
        MX-specific details of the bank transfer funding.
        """
        reference: NotRequired[str]
        type: NotRequired[
            Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
        ]
        us_bank_transfer: NotRequired[
            "CustomerCashBalanceTransaction.CreateParamsFundedBankTransferUsBankTransfer"
        ]
        """
        US-specific details of the bank transfer funding.
        """

    class CreateParamsFundedBankTransferCaBankTransfer(TypedDict):
        pass

    class CreateParamsFundedBankTransferEuBankTransfer(TypedDict):
        bic: NotRequired[str]
        iban_last4: NotRequired[str]
        network: NotRequired[Literal["sepa", "swift"]]
        sender_name: NotRequired[str]

    class CreateParamsFundedBankTransferGbBankTransfer(TypedDict):
        account_number_last4: NotRequired[str]
        sender_name: NotRequired[str]
        sort_code: NotRequired[str]

    class CreateParamsFundedBankTransferJpBankTransfer(TypedDict):
        sender_bank: NotRequired[str]
        sender_branch: NotRequired[str]
        sender_name: NotRequired[str]

    class CreateParamsFundedBankTransferMxBankTransfer(TypedDict):
        pass

    class CreateParamsFundedBankTransferUsBankTransfer(TypedDict):
        network: NotRequired[Literal["ach", "domestic_wire_us", "swift"]]
        sender_name: NotRequired[str]

    class CreateParamsFundingReversed(TypedDict):
        reversed_customer_cash_balance_transaction: str
        """
        The ID of the `funded` cash balance transaction to be reversed.
        """

    adjusted_for_overdraft: Optional[AdjustedForOverdraft]
    applied_to_payment: Optional[AppliedToPayment]
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: ExpandableField["Customer"]
    """
    The customer whose available cash balance changed as a result of this transaction.
    """
    ending_balance: int
    """
    The total available cash balance for the specified currency after this transaction was applied. Represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    funded: Optional[Funded]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    net_amount: int
    """
    The amount by which the cash balance changed, represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). A positive value represents funds being added to the cash balance, a negative value represents funds being removed from the cash balance.
    """
    object: Literal["customer_cash_balance_transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    refunded_from_payment: Optional[RefundedFromPayment]
    transferred_to_balance: Optional[TransferredToBalance]
    type: Literal[
        "adjusted_for_overdraft",
        "applied_to_payment",
        "funded",
        "funding_reversed",
        "refunded_from_payment",
        "return_canceled",
        "return_initiated",
        "transferred_to_balance",
        "unapplied_from_payment",
    ]
    """
    The type of the cash balance transaction. New types may be added in future. See [Customer Balance](https://stripe.com/docs/payments/customer-balance#types) to learn more about these types.
    """
    unapplied_from_payment: Optional[UnappliedFromPayment]

    class TestHelpers(
        APIResourceTestHelpers["CustomerCashBalanceTransaction"]
    ):
        _resource_cls: Type["CustomerCashBalanceTransaction"]

        @classmethod
        def create(
            cls,
            **params: Unpack["CustomerCashBalanceTransaction.CreateParams"],
        ) -> "CustomerCashBalanceTransaction":
            """
            Simulate various customer cash balance side-effects by creating synthetic cash balance transactions in testmode.
            """
            return cast(
                "CustomerCashBalanceTransaction",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/customer_cash_balance_transactions",
                    params=params,
                ),
            )

        @classmethod
        async def create_async(
            cls,
            **params: Unpack["CustomerCashBalanceTransaction.CreateParams"],
        ) -> "CustomerCashBalanceTransaction":
            """
            Simulate various customer cash balance side-effects by creating synthetic cash balance transactions in testmode.
            """
            return cast(
                "CustomerCashBalanceTransaction",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/customer_cash_balance_transactions",
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "adjusted_for_overdraft": AdjustedForOverdraft,
        "applied_to_payment": AppliedToPayment,
        "funded": Funded,
        "refunded_from_payment": RefundedFromPayment,
        "transferred_to_balance": TransferredToBalance,
        "unapplied_from_payment": UnappliedFromPayment,
    }


CustomerCashBalanceTransaction.TestHelpers._resource_cls = (
    CustomerCashBalanceTransaction
)
