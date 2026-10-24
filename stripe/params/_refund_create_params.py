# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class RefundCreateParams(RequestOptions):
    amount: NotRequired[int]
    charge: NotRequired[str]
    """
    The identifier of the charge to refund.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: NotRequired[str]
    """
    Customer whose customer balance to refund from.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    instructions_email: NotRequired[str]
    """
    For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    origin: NotRequired[Literal["customer_balance"]]
    """
    Origin of the refund
    """
    payment_attempt_record: NotRequired[str]
    """
    The identifier of the PaymentAttemptRecord to refund.
    """
    payment_intent: NotRequired[str]
    """
    The identifier of the PaymentIntent to refund.
    """
    payment_method_data: NotRequired["RefundCreateParamsPaymentMethodData"]
    """
    Used to create the PaymentMethod that will receive the refund.
    """
    payment_method_options: NotRequired[
        "RefundCreateParamsPaymentMethodOptions"
    ]
    """
    Payment method-specific options for the refund.
    """
    payment_record: NotRequired[str]
    """
    The identifier of the PaymentRecord to refund.
    """
    reason: NotRequired[
        "Literal['duplicate', 'fraudulent', 'requested_by_customer']|str"
    ]
    """
    String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://docs.stripe.com/radar/lists), and will also help us improve our fraud detection algorithms.
    """
    refund_application_fee: NotRequired[bool]
    """
    Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    """
    reverse_transfer: NotRequired[bool]
    """
    Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).

    A transfer can be reversed only by the application that created the charge.
    """


class RefundCreateParamsPaymentMethodData(TypedDict):
    gift_card: NotRequired["RefundCreateParamsPaymentMethodDataGiftCard"]
    """
    The gift card to receive the refund.
    """
    type: Union[
        Literal[
            "acss_debit",
            "affirm",
            "afterpay_clearpay",
            "alipay",
            "alma",
            "amazon_pay",
            "au_becs_debit",
            "bacs_debit",
            "bancontact",
            "billie",
            "bizum",
            "blik",
            "boleto",
            "card",
            "carecredit",
            "cashapp",
            "crypto",
            "custom",
            "customer_balance",
            "eps",
            "fpx",
            "getflex",
            "gift_card",
            "giropay",
            "gopay",
            "grabpay",
            "id_bank_transfer",
            "ideal",
            "kakao_pay",
            "klarna",
            "konbini",
            "kr_card",
            "link",
            "mb_way",
            "mobilepay",
            "multibanco",
            "naver_pay",
            "nz_bank_account",
            "oxxo",
            "p24",
            "pay_by_bank",
            "payco",
            "paynow",
            "paypal",
            "paypay",
            "payto",
            "pix",
            "promptpay",
            "qris",
            "rakuten_pay",
            "rechnung",
            "revolut_pay",
            "samsung_pay",
            "satispay",
            "scalapay",
            "sepa_debit",
            "sequra",
            "sezzle",
            "shopeepay",
            "sofort",
            "stripe_balance",
            "sunbit",
            "swish",
            "tamara",
            "toss_pay",
            "twint",
            "upi",
            "us_bank_account",
            "vipps",
            "wechat_pay",
            "wero",
            "zip",
        ],
        str,
    ]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """


class RefundCreateParamsPaymentMethodDataGiftCard(TypedDict):
    gift_card: str
    """
    The ID of the gift card to receive the refund.
    """


class RefundCreateParamsPaymentMethodOptions(TypedDict):
    gift_card: NotRequired[
        "Literal['']|RefundCreateParamsPaymentMethodOptionsGiftCard"
    ]
    """
    Gift card refund options.
    """


class RefundCreateParamsPaymentMethodOptionsGiftCard(TypedDict):
    operation_type: NotRequired[Literal["activation", "reload"]]
    """
    The type of gift card operation to perform for the refund.
    """
