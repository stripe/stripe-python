# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.refund import Refund


class CustomerCashBalanceTransaction(
    ListableAPIResource["CustomerCashBalanceTransaction"],
):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid
    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.
    """

    OBJECT_NAME = "customer_cash_balance_transaction"

    class AdjustedForOverdraft(StripeObject):
        balance_transaction: ExpandableField["BalanceTransaction"]
        linked_transaction: ExpandableField["CustomerCashBalanceTransaction"]

    class AppliedToPayment(StripeObject):
        payment_intent: ExpandableField["PaymentIntent"]

    class Funded(StripeObject):
        class BankTransfer(StripeObject):
            class EuBankTransfer(StripeObject):
                bic: Optional[str]
                iban_last4: Optional[str]
                sender_name: Optional[str]

            class GbBankTransfer(StripeObject):
                account_number_last4: Optional[str]
                sender_name: Optional[str]
                sort_code: Optional[str]

            class JpBankTransfer(StripeObject):
                sender_bank: Optional[str]
                sender_branch: Optional[str]
                sender_name: Optional[str]

            class UsBankTransfer(StripeObject):
                network: Optional[Literal["ach", "domestic_wire_us", "swift"]]
                sender_name: Optional[str]

            eu_bank_transfer: Optional[EuBankTransfer]
            gb_bank_transfer: Optional[GbBankTransfer]
            jp_bank_transfer: Optional[JpBankTransfer]
            reference: Optional[str]
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
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

    class UnappliedFromPayment(StripeObject):
        payment_intent: ExpandableField["PaymentIntent"]

    adjusted_for_overdraft: Optional[AdjustedForOverdraft]
    applied_to_payment: Optional[AppliedToPayment]
    created: int
    currency: str
    customer: ExpandableField["Customer"]
    ending_balance: int
    funded: Optional[Funded]
    id: str
    livemode: bool
    net_amount: int
    object: Literal["customer_cash_balance_transaction"]
    refunded_from_payment: Optional[RefundedFromPayment]
    type: Literal[
        "adjusted_for_overdraft",
        "applied_to_payment",
        "funded",
        "funding_reversed",
        "refunded_from_payment",
        "return_canceled",
        "return_initiated",
        "unapplied_from_payment",
    ]
    unapplied_from_payment: Optional[UnappliedFromPayment]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["CustomerCashBalanceTransaction"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "CustomerCashBalanceTransaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "adjusted_for_overdraft": AdjustedForOverdraft,
        "applied_to_payment": AppliedToPayment,
        "funded": Funded,
        "refunded_from_payment": RefundedFromPayment,
        "unapplied_from_payment": UnappliedFromPayment,
    }
