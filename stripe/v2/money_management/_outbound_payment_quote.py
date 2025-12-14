# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal


class OutboundPaymentQuote(StripeObject):
    """
    OutboundPaymentQuote represents a quote that provides fee and amount estimates for OutboundPayment.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.outbound_payment_quote"]
    ] = "v2.money_management.outbound_payment_quote"

    class Amount(StripeObject):
        currency: Optional[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        value: Optional[int]
        """
        A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
        """

    class DeliveryOptions(StripeObject):
        bank_account: Optional[Literal["automatic", "local", "wire"]]
        """
        Open Enum. Method for bank account.
        """
        speed: Optional[Literal["instant", "next_business_day", "standard"]]
        """
        Open Enum. Speed of the payout.
        """

    class EstimatedFee(StripeObject):
        class Amount(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        amount: Amount
        """
        The fee amount for corresponding fee type.
        """
        type: Literal[
            "cross_border_payout_fee",
            "foreign_exchange_fee",
            "instant_payout_fee",
            "real_time_payout_fee",
            "standard_payout_fee",
            "wire_payout_fee",
        ]
        """
        The fee type.
        """
        _inner_class_types = {"amount": Amount}

    class From(StripeObject):
        class Debited(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        debited: Debited
        """
        The monetary amount debited from the sender, only set on responses.
        """
        financial_account: str
        """
        The FinancialAccount that funds were pulled from.
        """
        _inner_class_types = {"debited": Debited}

    class FxQuote(StripeObject):
        class Rates(StripeObject):
            exchange_rate: str
            """
            The exchange rate going from_currency -> to_currency.
            """

        lock_duration: Literal["five_minutes", "none"]
        """
        The duration the exchange rate lock remains valid from creation time. Allowed value is five_minutes or none.
        """
        lock_expires_at: Optional[str]
        """
        Time at which the rate lock will expire, measured in seconds since the Unix epoch. Null when rate locking is not supported.
        """
        lock_status: Literal["active", "expired", "none"]
        """
        Lock status of the quote. Transitions from active to expired once past the lock_expires_at timestamp. Value can be active, expired or none.
        """
        rates: Dict[str, Rates]
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
        class Credited(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        credited: Credited
        """
        The monetary amount being credited to the destination.
        """
        payout_method: str
        """
        The payout method which the OutboundPayment uses to send payout.
        """
        recipient: str
        """
        To which account the OutboundPayment is sent.
        """
        _inner_class_types = {"credited": Credited}

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
        "amount": Amount,
        "delivery_options": DeliveryOptions,
        "estimated_fees": EstimatedFee,
        "from": From,
        "fx_quote": FxQuote,
        "to": To,
    }
    _field_remappings = {"from_": "from"}
