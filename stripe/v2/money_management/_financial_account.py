# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class FinancialAccount(StripeObject):
    """
    A FinancialAccount represents a balance and can be used as the source or destination for the money management (`/v2/money_management`) APIs.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_account"]] = (
        "v2.money_management.financial_account"
    )

    class AccruedFees(StripeObject):
        currencies: List[str]
        """
        The currencies enabled for fee accrual on this FinancialAccount.
        """
        direction: Literal["payable", "receivable"]
        """
        Direction of fee accrual for this FinancialAccount.
        """

    class Balance(StripeObject):
        available: UntypedStripeObject[Amount]
        """
        Balance that can be used for money movement.
        """
        inbound_pending: UntypedStripeObject[Amount]
        """
        Balance of inbound funds that will later transition to the `available` balance.
        """
        outbound_pending: UntypedStripeObject[Amount]
        """
        Balance of funds that are being used for a pending outbound money movement.
        """

    class ManagedBy(StripeObject):
        type: Literal["multiprocessor_settlement"]
        """
        Enum describing the Stripe product that is managing this FinancialAccount.
        """

    class MultiprocessorSettlement(StripeObject):
        settlement_currencies: List[str]
        """
        Settlement currencies enabled for this FinancialAccount.
        """

    class Other(StripeObject):
        type: str
        """
        The type of the FinancialAccount, represented as a string. Upgrade your API version to see the type reflected in `financial_account.type`.
        """

    class Payments(StripeObject):
        class BalanceByFundsType(StripeObject):
            class PaymentProcessing(StripeObject):
                available: UntypedStripeObject[Amount]
                """
                Balance that can be used for money movement.
                """
                inbound_pending: UntypedStripeObject[Amount]
                """
                Balance of inbound funds that will later transition to the `available` balance.
                """
                outbound_pending: UntypedStripeObject[Amount]
                """
                Balance of funds that are being used for a pending outbound money movement.
                """

            class StoredValue(StripeObject):
                available: UntypedStripeObject[Amount]
                """
                Balance that can be used for money movement.
                """
                inbound_pending: UntypedStripeObject[Amount]
                """
                Balance of inbound funds that will later transition to the `available` balance.
                """
                outbound_pending: UntypedStripeObject[Amount]
                """
                Balance of funds that are being used for a pending outbound money movement.
                """

            payment_processing: PaymentProcessing
            """
            Payment processing funds are those that are received for goods or services and may only be used for payouts to self. These funds may be converted to stored value funds.
            """
            stored_value: StoredValue
            """
            Stored value funds may be used for either payouts to self or payments to others.
            """
            _inner_class_types = {
                "payment_processing": PaymentProcessing,
                "stored_value": StoredValue,
            }

        class StartingBalance(StripeObject):
            at: str
            """
            When the balance was projected.
            """
            available: UntypedStripeObject[Amount]
            """
            The available balance at the time when the balance was projected.
            """

        balance_by_funds_type: Optional[BalanceByFundsType]
        """
        The balance of the `payments` FinancialAccount is a mix of payment processing and stored value funds, and this field
        describes the breakdown between the two. The sum will match the balance of the FinancialAccount.
        """
        default_currency: str
        """
        The currency that non-settlement currency payments will be converted to.
        """
        settlement_currencies: List[str]
        """
        Settlement currencies enabled for this FinancialAccount. Payments in other currencies will be automatically converted to `default_currency`.
        """
        starting_balance: Optional[StartingBalance]
        """
        Describes the available balance when it was projected.
        """
        _inner_class_types = {
            "balance_by_funds_type": BalanceByFundsType,
            "starting_balance": StartingBalance,
        }

    class StatusDetails(StripeObject):
        class Closed(StripeObject):
            class ForwardingSettings(StripeObject):
                payment_method: Optional[str]
                """
                The address to send forwarded payments to.
                """
                payout_method: Optional[str]
                """
                The address to send forwarded payouts to.
                """

            forwarding_settings: Optional[ForwardingSettings]
            """
            The forwarding settings for the closed FinancialAccount.
            """
            reason: Literal["account_closed", "closed_by_platform", "other"]
            """
            The reason the FinancialAccount was closed.
            """
            _inner_class_types = {"forwarding_settings": ForwardingSettings}

        closed: Optional[Closed]
        """
        Details related to the closed state of the FinancialAccount.
        """
        _inner_class_types = {"closed": Closed}

    class Storage(StripeObject):
        funds_usage_type: Optional[Literal["business", "consumer"]]
        """
        The usage type for funds in this FinancialAccount. Can be used to specify that the funds are for Consumer activity.
        """
        holds_currencies: List[str]
        """
        The currencies that this FinancialAccount can hold.
        """

    accrued_fees: Optional[AccruedFees]
    """
    If this is a `accrued_fees` FinancialAccount, this hash include details specific to `accrued_fees` FinancialAccount.
    """
    balance: Balance
    """
    Multi-currency balance of this FinancialAccount, split by availability state. Each balance is represented as a hash where the key is the three-letter ISO currency code, in lowercase, and the value is the amount for that currency.
    """
    country: str
    """
    Open Enum. Two-letter country code that represents the country where the LegalEntity associated with the FinancialAccount is based in.
    """
    created: str
    """
    Time at which the object was created.
    """
    display_name: Optional[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name will be used in the Stripe Dashboard and embedded components.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    managed_by: Optional[ManagedBy]
    """
    If this is a managed FinancialAccount, `managed_by` indicates the product that created and manages this FinancialAccount. For managed FinancialAccounts,
    creation of money management resources can only be orchestrated by the managing product.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Metadata associated with the FinancialAccount.
    """
    multiprocessor_settlement: Optional[MultiprocessorSettlement]
    """
    If this is a `multiprocessor_settlement` FinancialAccount, this hash includes details specific to `multiprocessor_settlement` FinancialAccounts.
    """
    object: Literal["v2.money_management.financial_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    other: Optional[Other]
    """
    If this is a `other` FinancialAccount, this hash indicates what the actual type is. Upgrade your API version to see it reflected in `type`.
    """
    payments: Optional[Payments]
    """
    If this is a `payments` FinancialAccount, this hash include details specific to `payments` FinancialAccount.
    """
    status: Literal["closed", "open", "pending"]
    """
    Closed Enum. An enum representing the status of the FinancialAccount. This indicates whether or not the FinancialAccount can be used for any money movement flows.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details related to the status of the FinancialAccount.
    """
    storage: Optional[Storage]
    """
    If this is a `storage` FinancialAccount, this hash includes details specific to `storage` FinancialAccounts.
    """
    type: Literal[
        "accrued_fees",
        "multiprocessor_settlement",
        "other",
        "payments",
        "storage",
    ]
    """
    Type of the FinancialAccount. An additional hash is included on the FinancialAccount with a name matching this value.
    It contains additional information specific to the FinancialAccount type.
    """
    _inner_class_types = {
        "accrued_fees": AccruedFees,
        "balance": Balance,
        "managed_by": ManagedBy,
        "multiprocessor_settlement": MultiprocessorSettlement,
        "other": Other,
        "payments": Payments,
        "status_details": StatusDetails,
        "storage": Storage,
    }
