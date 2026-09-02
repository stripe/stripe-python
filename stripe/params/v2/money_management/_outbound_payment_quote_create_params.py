# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict

_OutboundPaymentQuoteCreateParamsBase = TypedDict(
    "OutboundPaymentQuoteCreateParams",
    {"from": "OutboundPaymentQuoteCreateParamsFrom"},
)


class OutboundPaymentQuoteCreateParams(_OutboundPaymentQuoteCreateParamsBase):
    amount: AmountParam
    """
    The "presentment amount" to be sent to the recipient.
    """
    delivery_options: NotRequired[
        "OutboundPaymentQuoteCreateParamsDeliveryOptions"
    ]
    """
    Method to be used to send the OutboundPayment.
    """
    to: "OutboundPaymentQuoteCreateParamsTo"
    """
    Request details about the recipient of an OutboundPaymentQuote.
    """


class OutboundPaymentQuoteCreateParamsDeliveryOptions(TypedDict):
    bank_account: NotRequired["Literal['automatic', 'local', 'wire']|str"]
    """
    Open Enum. Method for bank account.
    """
    speed: NotRequired[
        "Literal['instant', 'next_business_day', 'standard']|str"
    ]
    """
    Open Enum. Speed of the payout.
    """


class OutboundPaymentQuoteCreateParamsFrom(TypedDict):
    currency: str
    """
    Describes the FinancialAccount's currency drawn from.
    """
    financial_account: str
    """
    The FinancialAccount that funds were pulled from.
    """


class OutboundPaymentQuoteCreateParamsTo(TypedDict):
    currency: NotRequired[str]
    """
    Describes the currency to send to the recipient.
    If included, this currency must match a currency supported by the destination.
    Can be omitted in the following cases:
    - destination only supports one currency
    - destination supports multiple currencies and one of the currencies matches the FA currency
    - destination supports multiple currencies and one of the currencies matches the presentment currency
    Note - when both FA currency and presentment currency are supported, we pick the FA currency to minimize FX.
    """
    payout_method: NotRequired[str]
    """
    The payout method which the OutboundPayment uses to send payout.
    """
    payout_method_options: NotRequired[
        "OutboundPaymentQuoteCreateParamsToPayoutMethodOptions"
    ]
    """
    Payout method options for the OutboundPaymentQuote.
    """
    recipient: str
    """
    To which account the OutboundPayment is sent.
    """


class OutboundPaymentQuoteCreateParamsToPayoutMethodOptions(TypedDict):
    bank_account: NotRequired[
        "OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccount"
    ]
    """
    Options for bank account payout methods.
    """


class OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccount(
    TypedDict,
):
    preferred_network_options: NotRequired[
        "OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions"
    ]
    """
    Per-network configuration options.
    """
    preferred_networks: List[
        Union[
            Literal[
                "ach",
                "becs",
                "eft",
                "fedwire",
                "fps",
                "npp",
                "rtp",
                "sepa_credit",
                "sepa_instant",
                "swift",
            ],
            str,
        ]
    ]
    """
    The preferred networks to use for this OutboundPayment.
    """


class OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptions(
    TypedDict,
):
    ach: NotRequired[
        "OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch"
    ]
    """
    ACH-specific network options.
    """


class OutboundPaymentQuoteCreateParamsToPayoutMethodOptionsBankAccountPreferredNetworkOptionsAch(
    TypedDict,
):
    submission: NotRequired["Literal['next_day', 'same_day']|str"]
    """
    Open Enum. ACH submission timing.
    """
    transaction_purpose: NotRequired["Literal['payroll']|str"]
    """
    The transaction purpose for this ACH payment.
    """
