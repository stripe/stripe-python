# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class OutboundPaymentQuote(StripeObject):
    """
    OutboundPaymentQuote represents a quote that provides fee and amount estimates for OutboundPayment.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.outbound_payment_quote"]
    ] = "v2.money_management.outbound_payment_quote"

    class DeliveryOptions(StripeObject):
        bank_account: Optional[
            Union[Literal["automatic", "local", "wire"], str]
        ]
        """
        Open Enum. Method for bank account.
        """
        speed: Optional[
            Union[Literal["instant", "next_business_day", "standard"], str]
        ]
        """
        Open Enum. Speed of the payout.
        """

    class EstimatedFee(StripeObject):
        class TaxAmount(StripeObject):
            currency: str
            """
            Currency code.
            """
            value_decimal: str
            """
            Tax amount value represented as a decimal string in major units.
            """

        amount: Amount
        """
        The fee amount for corresponding fee type.
        """
        tax_amount: Optional[TaxAmount]
        """
        Tax charged for this fee, if applicable. Value expressed as a decimal string in major units.
        """
        type: Union[
            Literal[
                "cross_border_payout_fee",
                "foreign_exchange_fee",
                "instant_payout_fee",
                "next_day_payout_fee",
                "real_time_payout_fee",
                "standard_payout_fee",
                "wire_payout_fee",
            ],
            str,
        ]
        """
        The fee type.
        """
        _inner_class_types = {"tax_amount": TaxAmount}

    class From(StripeObject):
        debited: Amount
        """
        The monetary amount debited from the sender, only set on responses.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """

    class FxQuote(StripeObject):
        class Rates(StripeObject):
            exchange_rate: str
            """
            The exchange rate going from_currency -> to_currency.
            """

        lock_duration: Union[Literal["five_minutes", "none"], str]
        """
        The duration the exchange rate lock remains valid from creation time. Allowed value is five_minutes or none.
        """
        lock_expires_at: Optional[str]
        """
        Time at which the rate lock will expire, measured in seconds since the Unix epoch. Null when rate locking is not supported.
        """
        lock_status: Union[Literal["active", "expired", "none"], str]
        """
        Lock status of the quote. Transitions from active to expired once past the lock_expires_at timestamp. Value can be active, expired or none.
        """
        rates: UntypedStripeObject[Rates]
        """
        Key pair: from currency Value: exchange rate going from_currency -> to_currency.
        """
        to_currency: str
        """
        The currency that the transaction is exchanging to.
        """
        _inner_class_types = {"rates": Rates}
        _inner_class_dicts = ["rates"]

    class To(StripeObject):
        class PayoutMethodOptions(StripeObject):
            class BankAccount(StripeObject):
                class PreferredNetworkOptions(StripeObject):
                    class Ach(StripeObject):
                        submission: Optional[
                            Union[Literal["next_day", "same_day"], str]
                        ]
                        """
                        Open Enum. ACH submission timing.
                        """
                        transaction_purpose: Optional[Literal["payroll"]]
                        """
                        The transaction purpose for this ACH payment.
                        """

                    ach: Optional[Ach]
                    """
                    ACH-specific network options.
                    """
                    _inner_class_types = {"ach": Ach}

                preferred_network_options: Optional[PreferredNetworkOptions]
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
                _inner_class_types = {
                    "preferred_network_options": PreferredNetworkOptions,
                }

            bank_account: Optional[BankAccount]
            """
            Options for bank account payout methods.
            """
            _inner_class_types = {"bank_account": BankAccount}

        credited: Amount
        """
        The monetary amount being credited to the destination.
        """
        payout_method: str
        """
        The payout method which the OutboundPayment uses to send payout.
        """
        payout_method_options: Optional[PayoutMethodOptions]
        """
        Payout method options for the OutboundPaymentQuote.
        """
        recipient: str
        """
        To which account the OutboundPayment is sent.
        """
        _inner_class_types = {"payout_method_options": PayoutMethodOptions}

    amount: Amount
    """
    The "presentment amount" for the OutboundPaymentQuote.
    """
    created: str
    """
    Time at which the OutboundPaymentQuote was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    delivery_options: Optional[DeliveryOptions]
    """
    Delivery options to be used to send the OutboundPayment.
    """
    estimated_fees: List[EstimatedFee]
    """
    The estimated fees for the OutboundPaymentQuote.
    """
    from_: From
    """
    Details about the sender of an OutboundPaymentQuote.
    """
    fx_quote: FxQuote
    """
    The underlying FXQuote details for the OutboundPaymentQuote.
    """
    id: str
    """
    Unique identifier for the OutboundPaymentQuote.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.outbound_payment_quote"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    to: To
    """
    Details about the recipient of an OutboundPaymentQuote.
    """
    _inner_class_types = {
        "delivery_options": DeliveryOptions,
        "estimated_fees": EstimatedFee,
        "from": From,
        "fx_quote": FxQuote,
        "to": To,
    }
    _field_remappings = {"from_": "from"}
