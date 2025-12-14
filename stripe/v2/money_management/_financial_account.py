# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class FinancialAccount(StripeObject):
    """
    A FinancialAccount represents a balance and can be used as the source or destination for the money management (`/v2/money_management`) APIs.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_account"]] = (
        "v2.money_management.financial_account"
    )

    class Balance(StripeObject):
        class Available(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class InboundPending(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        class OutboundPending(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        available: Dict[str, Available]
        """
        Balance that can be used for money movement.
        """
        inbound_pending: Dict[str, InboundPending]
        """
        Balance of inbound funds that will later transition to the `available` balance.
        """
        outbound_pending: Dict[str, OutboundPending]
        """
        Balance of funds that are being used for a pending outbound money movement.
        """
        _inner_class_types = {
            "available": Available,
            "inbound_pending": InboundPending,
            "outbound_pending": OutboundPending,
        }
        _inner_class_dicts = [
            "available",
            "inbound_pending",
            "outbound_pending",
        ]

    class ManagedBy(StripeObject):
        type: Literal["multiprocessor_settlement"]
        """
        Enum describing the Stripe product that is managing this FinancialAccount.
        """

    class Other(StripeObject):
        type: str
        """
        The type of the FinancialAccount, represented as a string. Upgrade your API version to see the type reflected in `financial_account.type`.
        """

    class Payments(StripeObject):
        default_currency: str
        """
        The currency that non-settlement currency payments will be converted to.
        """
        settlement_currencies: List[str]
        """
        Settlement currencies enabled for this FinancialAccount. Payments in other currencies will be automatically converted to `default_currency`.
        """

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
            reason: Literal["account_closed", "closed_by_platform", "other"]
            _inner_class_types = {"forwarding_settings": ForwardingSettings}

        closed: Optional[Closed]
        _inner_class_types = {"closed": Closed}

    class Storage(StripeObject):
        holds_currencies: List[str]
        """
        The currencies that this FinancialAccount can hold.
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
    metadata: Optional[Dict[str, str]]
    """
    Metadata associated with the FinancialAccount.
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
    storage: Optional[Storage]
    """
    If this is a `storage` FinancialAccount, this hash includes details specific to `storage` FinancialAccounts.
    """
    type: Literal["other", "payments", "storage"]
    """
    Type of the FinancialAccount. An additional hash is included on the FinancialAccount with a name matching this value.
    It contains additional information specific to the FinancialAccount type.
    """
    _inner_class_types = {
        "balance": Balance,
        "managed_by": ManagedBy,
        "other": Other,
        "payments": Payments,
        "status_details": StatusDetails,
        "storage": Storage,
    }
