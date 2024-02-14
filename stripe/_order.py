# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._customer import Customer
    from stripe._discount import Discount as DiscountResource
    from stripe._line_item import LineItem
    from stripe._payment_intent import PaymentIntent
    from stripe._shipping_rate import ShippingRate
    from stripe._tax_rate import TaxRate


class Order(
    CreateableAPIResource["Order"],
    ListableAPIResource["Order"],
    UpdateableAPIResource["Order"],
):
    """
    An Order describes a purchase being made by a customer, including the
    products & quantities being purchased, the order status, the payment information,
    and the billing/shipping details.

    Related guide: [Orders overview](https://stripe.com/docs/orders)
    """

    OBJECT_NAME: ClassVar[Literal["order"]] = "order"

    class AutomaticTax(StripeObject):
        enabled: bool
        """
        Whether Stripe automatically computes tax on this Order.
        """
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        """
        The status of the most recent automated tax calculation for this Order.
        """

    class BillingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Optional[Address]
        """
        Billing address for the order.
        """
        email: Optional[str]
        """
        Email address for the order.
        """
        name: Optional[str]
        """
        Full name for the order.
        """
        phone: Optional[str]
        """
        Billing phone number for the order (including extension).
        """
        _inner_class_types = {"address": Address}

    class Credit(StripeObject):
        class GiftCard(StripeObject):
            card: str
            """
            The token of the gift card applied to the order
            """

        amount: int
        """
        The amount of this credit to apply to the order.
        """
        gift_card: Optional[GiftCard]
        """
        Details for a gift card.
        """
        ineligible_line_items: Optional[List[str]]
        """
        Line items on this order that are ineligible for this credit
        """
        type: Literal["gift_card"]
        """
        The type of credit to apply to the order, only `gift_card` currently supported.
        """
        _inner_class_types = {"gift_card": GiftCard}

    class Payment(StripeObject):
        class Settings(StripeObject):
            class AutomaticPaymentMethods(StripeObject):
                enabled: bool
                """
                Whether this Order has been opted into managing payment method types via the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
                """

            class PaymentMethodOptions(StripeObject):
                class AcssDebit(StripeObject):
                    class MandateOptions(StripeObject):
                        custom_mandate_url: Optional[str]
                        """
                        A URL for custom mandate text
                        """
                        interval_description: Optional[str]
                        """
                        Description of the interval. Only required if the 'payment_schedule' parameter is 'interval' or 'combined'.
                        """
                        payment_schedule: Optional[
                            Literal["combined", "interval", "sporadic"]
                        ]
                        """
                        Payment schedule for the mandate.
                        """
                        transaction_type: Optional[
                            Literal["business", "personal"]
                        ]
                        """
                        Transaction type of the mandate.
                        """

                    mandate_options: Optional[MandateOptions]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """
                    verification_method: Optional[
                        Literal["automatic", "instant", "microdeposits"]
                    ]
                    """
                    Bank account verification method.
                    """
                    _inner_class_types = {"mandate_options": MandateOptions}

                class AfterpayClearpay(StripeObject):
                    capture_method: Optional[
                        Literal["automatic", "automatic_async", "manual"]
                    ]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    reference: Optional[str]
                    """
                    Order identifier shown to the user in Afterpay's online portal. We recommend using a value that helps you answer any questions a customer might have about the payment. The identifier is limited to 128 characters and may contain only letters, digits, underscores, backslashes and dashes.
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with the payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

                    If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
                    """

                class Alipay(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Bancontact(StripeObject):
                    preferred_language: Literal["de", "en", "fr", "nl"]
                    """
                    Preferred language of the Bancontact authorization page that the customer is redirected to.
                    """
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Card(StripeObject):
                    capture_method: Literal[
                        "automatic", "automatic_async", "manual"
                    ]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with the payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

                    If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
                    """

                class CustomerBalance(StripeObject):
                    class BankTransfer(StripeObject):
                        class EuBankTransfer(StripeObject):
                            country: Literal[
                                "BE", "DE", "ES", "FR", "IE", "NL"
                            ]
                            """
                            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
                            """

                        eu_bank_transfer: Optional[EuBankTransfer]
                        requested_address_types: Optional[
                            List[
                                Literal[
                                    "aba",
                                    "iban",
                                    "sepa",
                                    "sort_code",
                                    "spei",
                                    "swift",
                                    "zengin",
                                ]
                            ]
                        ]
                        """
                        List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

                        Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
                        """
                        type: Optional[
                            Literal[
                                "eu_bank_transfer",
                                "gb_bank_transfer",
                                "jp_bank_transfer",
                                "mx_bank_transfer",
                                "us_bank_transfer",
                            ]
                        ]
                        """
                        The bank transfer type that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
                        """
                        _inner_class_types = {
                            "eu_bank_transfer": EuBankTransfer,
                        }

                    bank_transfer: Optional[BankTransfer]
                    funding_type: Optional[Literal["bank_transfer"]]
                    """
                    The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """
                    _inner_class_types = {"bank_transfer": BankTransfer}

                class Ideal(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Klarna(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    preferred_locale: Optional[str]
                    """
                    Preferred locale of the Klarna checkout page that the customer is redirected to.
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Link(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    persistent_token: Optional[str]
                    """
                    [Deprecated] This is a legacy parameter that no longer has any function.
                    """
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Oxxo(StripeObject):
                    expires_after_days: int
                    """
                    The number of calendar days before an OXXO invoice expires. For example, if you create an OXXO invoice on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class P24(StripeObject):
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class Paypal(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    preferred_locale: Optional[str]
                    """
                    Preferred locale of the PayPal checkout page that the customer is redirected to.
                    """
                    reference: Optional[str]
                    """
                    A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
                    """
                    reference_id: Optional[str]
                    """
                    A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
                    """
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """
                    subsellers: Optional[List[str]]
                    """
                    The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
                    """

                class SepaDebit(StripeObject):
                    class MandateOptions(StripeObject):
                        pass

                    mandate_options: Optional[MandateOptions]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """
                    _inner_class_types = {"mandate_options": MandateOptions}

                class Sofort(StripeObject):
                    preferred_language: Optional[
                        Literal["de", "en", "es", "fr", "it", "nl", "pl"]
                    ]
                    """
                    Preferred language of the SOFORT authorization page that the customer is redirected to.
                    """
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                class WechatPay(StripeObject):
                    app_id: Optional[str]
                    """
                    The app ID registered with WeChat Pay. Only required when client is ios or android.
                    """
                    client: Optional[Literal["android", "ios", "web"]]
                    """
                    The client type that the end customer will pay from
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).
                    """

                acss_debit: Optional[AcssDebit]
                afterpay_clearpay: Optional[AfterpayClearpay]
                alipay: Optional[Alipay]
                bancontact: Optional[Bancontact]
                card: Optional[Card]
                customer_balance: Optional[CustomerBalance]
                ideal: Optional[Ideal]
                klarna: Optional[Klarna]
                link: Optional[Link]
                oxxo: Optional[Oxxo]
                p24: Optional[P24]
                paypal: Optional[Paypal]
                sepa_debit: Optional[SepaDebit]
                sofort: Optional[Sofort]
                wechat_pay: Optional[WechatPay]
                _inner_class_types = {
                    "acss_debit": AcssDebit,
                    "afterpay_clearpay": AfterpayClearpay,
                    "alipay": Alipay,
                    "bancontact": Bancontact,
                    "card": Card,
                    "customer_balance": CustomerBalance,
                    "ideal": Ideal,
                    "klarna": Klarna,
                    "link": Link,
                    "oxxo": Oxxo,
                    "p24": P24,
                    "paypal": Paypal,
                    "sepa_debit": SepaDebit,
                    "sofort": Sofort,
                    "wechat_pay": WechatPay,
                }

            class TransferData(StripeObject):
                amount: Optional[int]
                """
                The amount that will be transferred automatically when the order is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
                """
                destination: ExpandableField["Account"]
                """
                ID of the Connected account receiving the transfer.
                """

            application_fee_amount: Optional[int]
            """
            The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
            """
            automatic_payment_methods: Optional[AutomaticPaymentMethods]
            """
            Indicates whether order has been opted into using [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods) to manage payment method types.
            """
            payment_method_options: Optional[PaymentMethodOptions]
            """
            PaymentMethod-specific configuration to provide to the order's PaymentIntent.
            """
            payment_method_types: Optional[
                List[
                    Literal[
                        "acss_debit",
                        "afterpay_clearpay",
                        "alipay",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "card",
                        "customer_balance",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "klarna",
                        "link",
                        "oxxo",
                        "p24",
                        "paypal",
                        "sepa_debit",
                        "sofort",
                        "wechat_pay",
                    ]
                ]
            ]
            """
            The list of [payment method types](https://stripe.com/docs/payments/payment-methods/overview) to provide to the order's PaymentIntent. Do not include this attribute if you prefer to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
            """
            return_url: Optional[str]
            """
            The URL to redirect the customer to after they authenticate their payment.
            """
            statement_descriptor: Optional[str]
            """
            For non-card charges, you can use this value as the complete description that appears on your customers' statements. Must contain at least one letter, maximum 22 characters.
            """
            statement_descriptor_suffix: Optional[str]
            """
            Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
            """
            transfer_data: Optional[TransferData]
            """
            Provides configuration for completing a transfer for the order after it is paid.
            """
            _inner_class_types = {
                "automatic_payment_methods": AutomaticPaymentMethods,
                "payment_method_options": PaymentMethodOptions,
                "transfer_data": TransferData,
            }

        payment_intent: Optional[ExpandableField["PaymentIntent"]]
        """
        ID of the payment intent associated with this order. Null when the order is `open`.
        """
        settings: Optional[Settings]
        """
        Settings describing how the order should configure generated PaymentIntents.
        """
        status: Optional[
            Literal[
                "canceled",
                "complete",
                "not_required",
                "processing",
                "requires_action",
                "requires_capture",
                "requires_confirmation",
                "requires_payment_method",
            ]
        ]
        """
        The status of the underlying payment associated with this order, if any. Null when the order is `open`.
        """
        _inner_class_types = {"settings": Settings}

    class ShippingCost(StripeObject):
        class Tax(StripeObject):
            amount: int
            """
            Amount of tax applied for this rate.
            """
            rate: "TaxRate"
            """
            Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

            Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
            """
            taxability_reason: Optional[
                Literal[
                    "customer_exempt",
                    "not_collecting",
                    "not_subject_to_tax",
                    "not_supported",
                    "portion_product_exempt",
                    "portion_reduced_rated",
                    "portion_standard_rated",
                    "product_exempt",
                    "product_exempt_holiday",
                    "proportionally_rated",
                    "reduced_rated",
                    "reverse_charge",
                    "standard_rated",
                    "taxable_basis_reduced",
                    "zero_rated",
                ]
            ]
            """
            The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
            """
            taxable_amount: Optional[int]
            """
            The amount on which tax is calculated, in cents (or local equivalent).
            """

        amount_subtotal: int
        """
        Total shipping cost before any discounts or taxes are applied.
        """
        amount_tax: int
        """
        Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0.
        """
        amount_total: int
        """
        Total shipping cost after discounts and taxes are applied.
        """
        shipping_rate: Optional[ExpandableField["ShippingRate"]]
        """
        The ID of the ShippingRate for this order.
        """
        taxes: Optional[List[Tax]]
        """
        The taxes applied to the shipping rate.
        """
        _inner_class_types = {"taxes": Tax}

    class ShippingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Optional[Address]
        """
        Recipient shipping address. Required if the order includes products that are shippable.
        """
        name: Optional[str]
        """
        Recipient name.
        """
        phone: Optional[str]
        """
        Recipient phone (including extension).
        """
        _inner_class_types = {"address": Address}

    class TaxDetails(StripeObject):
        class TaxId(StripeObject):
            type: Literal[
                "ad_nrt",
                "ae_trn",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "bg_uic",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "ch_vat",
                "cl_tin",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "hk_br",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kr_brn",
                "li_uid",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "no_vat",
                "no_voec",
                "nz_gst",
                "pe_ruc",
                "ph_tin",
                "ro_tin",
                "rs_pib",
                "ru_inn",
                "ru_kpp",
                "sa_vat",
                "sg_gst",
                "sg_uen",
                "si_tin",
                "sv_nit",
                "th_vat",
                "tr_tin",
                "tw_vat",
                "ua_vat",
                "unknown",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            """
            The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, or `unknown`
            """
            value: Optional[str]
            """
            The value of the tax ID.
            """

        tax_exempt: Literal["exempt", "none", "reverse"]
        """
        Describes the purchaser's tax exemption status. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: List[TaxId]
        """
        The purchaser's tax IDs to be used in calculation of tax for this Order.
        """
        _inner_class_types = {"tax_ids": TaxId}

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                """
                The amount discounted.
                """
                discount: "DiscountResource"
                """
                A discount represents the actual application of a [coupon](https://stripe.com/docs/api#coupons) or [promotion code](https://stripe.com/docs/api#promotion_codes).
                It contains information about when the discount began, when it will end, and what it is applied to.

                Related guide: [Applying discounts to subscriptions](https://stripe.com/docs/billing/subscriptions/discounts)
                """

            class Tax(StripeObject):
                amount: int
                """
                Amount of tax applied for this rate.
                """
                rate: "TaxRate"
                """
                Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

                Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
                """
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                """
                The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
                """
                taxable_amount: Optional[int]
                """
                The amount on which tax is calculated, in cents (or local equivalent).
                """

            discounts: List[Discount]
            """
            The aggregated discounts.
            """
            taxes: List[Tax]
            """
            The aggregated tax amounts by rate.
            """
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_credit: Optional[int]
        amount_discount: int
        """
        This is the sum of all the discounts.
        """
        amount_shipping: Optional[int]
        """
        This is the sum of all the shipping amounts.
        """
        amount_tax: int
        """
        This is the sum of all the tax amounts.
        """
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    class CancelParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        automatic_tax: NotRequired["Order.CreateParamsAutomaticTax"]
        """
        Settings for automatic tax calculation for this order.
        """
        billing_details: NotRequired[
            "Literal['']|Order.CreateParamsBillingDetails"
        ]
        """
        Billing details for the customer. If a customer is provided, this will be automatically populated with values from that customer if override values are not provided.
        """
        credits: NotRequired["Literal['']|List[Order.CreateParamsCredit]"]
        """
        The credits to apply to the order, only `gift_card` currently supported.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: NotRequired["str"]
        """
        The customer associated with this order.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        discounts: NotRequired["Literal['']|List[Order.CreateParamsDiscount]"]
        """
        The coupons, promotion codes, and/or discounts to apply to the order.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        ip_address: NotRequired["str"]
        """
        The IP address of the purchaser for this order.
        """
        line_items: List["Order.CreateParamsLineItem"]
        """
        A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment: NotRequired["Order.CreateParamsPayment"]
        """
        Payment information associated with the order, including payment settings.
        """
        shipping_cost: NotRequired[
            "Literal['']|Order.CreateParamsShippingCost"
        ]
        """
        Settings for the customer cost of shipping for this order.
        """
        shipping_details: NotRequired[
            "Literal['']|Order.CreateParamsShippingDetails"
        ]
        """
        Shipping details for the order.
        """
        tax_details: NotRequired["Order.CreateParamsTaxDetails"]
        """
        Additional tax details about the purchaser to be used for this order.
        """

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enable automatic tax calculation which will automatically compute tax rates on this order.
        """

    class CreateParamsBillingDetails(TypedDict):
        address: NotRequired["Order.CreateParamsBillingDetailsAddress"]
        """
        The billing address provided by the customer.
        """
        email: NotRequired["str"]
        """
        The billing email provided by the customer.
        """
        name: NotRequired["str"]
        """
        The billing name provided by the customer.
        """
        phone: NotRequired["str"]
        """
        The billing phone number provided by the customer.
        """

    class CreateParamsBillingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
        """

    class CreateParamsCredit(TypedDict):
        gift_card: NotRequired["str"]
        """
        The gift card to apply to the order.
        """
        type: Literal["gift_card"]
        """
        The type of credit to apply to the order, only `gift_card` currently supported.
        """

    class CreateParamsDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class CreateParamsLineItem(TypedDict):
        description: NotRequired["str"]
        """
        The description for the line item. Will default to the name of the associated product.
        """
        discounts: NotRequired[
            "Literal['']|List[Order.CreateParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired["str"]
        """
        The ID of a [Price](https://stripe.com/docs/api/prices) to add to the Order.

        The `price` parameter is an alternative to using the `product` parameter. If each of your products are sold at a single price, you can set `Product.default_price` and then pass the `product` parameter when creating a line item. If your products are sold at several possible prices, use the `price` parameter to explicitly specify which one to use.
        """
        price_data: NotRequired["Order.CreateParamsLineItemPriceData"]
        """
        Data used to generate a new Price object inline.

        The `price_data` parameter is an alternative to using the `product` or `price` parameters. If you create products upfront and configure a `Product.default_price`, pass the `product` parameter when creating a line item. If you prefer not to define products upfront, or if you charge variable prices, pass the `price_data` parameter to describe the price for this line item.

        Each time you pass `price_data` we create a Price for the product. This Price is hidden in both the Dashboard and API lists and cannot be reused.
        """
        product: NotRequired["str"]
        """
        The ID of a [Product](https://stripe.com/docs/api/products) to add to the Order.

        The product must have a `default_price` specified. Otherwise, specify the price by passing the `price` or `price_data` parameter.
        """
        product_data: NotRequired["Order.CreateParamsLineItemProductData"]
        """
        Defines a Product inline and adds it to the Order.

        `product_data` is an alternative to the `product` parameter. If you created a Product upfront, use the `product` parameter to refer to the existing Product. But if you prefer not to create Products upfront, pass the `product_data` parameter to define a Product inline as part of configuring the Order.

        `product_data` automatically creates a Product, just as if you had manually created the Product. If a Product with the same ID already exists, then `product_data` re-uses it to avoid duplicates.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates applied to this line item.
        """

    class CreateParamsLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """

    class CreateParamsLineItemPriceData(TypedDict):
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: NotRequired["str"]
        """
        ID of the product this price belongs to.

        Use this to implement a variable-pricing model in your integration. This is required if `product_data` is not specifed.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class CreateParamsLineItemProductData(TypedDict):
        description: NotRequired["Literal['']|str"]
        """
        The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
        """
        id: str
        """
        A unique identifier for this product.

        `product_data` automatically creates a Product with this ID. If a Product with the same ID already exists, then `product_data` re-uses it to avoid duplicates. If any of the fields in the existing Product are different from the values in `product_data`, `product_data` updates the existing Product with the new information. So set `product_data[id]` to the same string every time you sell the same product, but don't re-use the same string for different products.
        """
        images: NotRequired["Literal['']|List[str]"]
        """
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: str
        """
        The product's name, meant to be displayable to the customer.
        """
        package_dimensions: NotRequired[
            "Literal['']|Order.CreateParamsLineItemProductDataPackageDimensions"
        ]
        """
        The dimensions of this product for shipping purposes.
        """
        shippable: NotRequired["bool"]
        """
        Whether this product is shipped (i.e., physical goods).
        """
        tax_code: NotRequired["Literal['']|str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        url: NotRequired["Literal['']|str"]
        """
        A URL of a publicly-accessible webpage for this product.
        """

    class CreateParamsLineItemProductDataPackageDimensions(TypedDict):
        height: float
        """
        Height, in inches. Maximum precision is 2 decimal places.
        """
        length: float
        """
        Length, in inches. Maximum precision is 2 decimal places.
        """
        weight: float
        """
        Weight, in ounces. Maximum precision is 2 decimal places.
        """
        width: float
        """
        Width, in inches. Maximum precision is 2 decimal places.
        """

    class CreateParamsPayment(TypedDict):
        settings: "Order.CreateParamsPaymentSettings"
        """
        Settings describing how the order should configure generated PaymentIntents.
        """

    class CreateParamsPaymentSettings(TypedDict):
        application_fee_amount: NotRequired["int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
        """
        payment_method_options: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptions"
        ]
        """
        PaymentMethod-specific configuration to provide to the order's PaymentIntent.
        """
        payment_method_types: NotRequired[
            "List[Literal['acss_debit', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'card', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'link', 'oxxo', 'p24', 'paypal', 'sepa_debit', 'sofort', 'wechat_pay']]"
        ]
        """
        The list of [payment method types](https://stripe.com/docs/payments/payment-methods/overview) to provide to the order's PaymentIntent. Do not include this attribute if you prefer to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
        """
        return_url: NotRequired["str"]
        """
        The URL to redirect the customer to after they authenticate their payment.
        """
        statement_descriptor: NotRequired["str"]
        """
        For non-card charges, you can use this value as the complete description that appears on your customers' statements. Must contain at least one letter, maximum 22 characters.
        """
        statement_descriptor_suffix: NotRequired["str"]
        """
        Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """
        transfer_data: NotRequired[
            "Order.CreateParamsPaymentSettingsTransferData"
        ]
        """
        Provides configuration for completing a transfer for the order after it is paid.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit"
        ]
        """
        If paying by `acss_debit`, this sub-hash contains details about the ACSS Debit payment method options to pass to the order's PaymentIntent.
        """
        afterpay_clearpay: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay"
        ]
        """
        If paying by `afterpay_clearpay`, this sub-hash contains details about the AfterpayClearpay payment method options to pass to the order's PaymentIntent.
        """
        alipay: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAlipay"
        ]
        """
        If paying by `alipay`, this sub-hash contains details about the Alipay payment method options to pass to the order's PaymentIntent.
        """
        bancontact: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact"
        ]
        """
        If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the order's PaymentIntent.
        """
        card: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCard"
        ]
        """
        If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the order's PaymentIntent.
        """
        customer_balance: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance"
        ]
        """
        If paying by `customer_balance`, this sub-hash contains details about the Customer Balance payment method options to pass to the order's PaymentIntent.
        """
        ideal: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsIdeal"
        ]
        """
        If paying by `ideal`, this sub-hash contains details about the iDEAL payment method options to pass to the order's PaymentIntent.
        """
        klarna: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsKlarna"
        ]
        """
        If paying by `klarna`, this sub-hash contains details about the Klarna payment method options to pass to the order's PaymentIntent.
        """
        link: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsLink"
        ]
        """
        If paying by `link`, this sub-hash contains details about the Link payment method options to pass to the order's PaymentIntent.
        """
        oxxo: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsOxxo"
        ]
        """
        If paying by `oxxo`, this sub-hash contains details about the OXXO payment method options to pass to the order's PaymentIntent.
        """
        p24: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsP24"
        ]
        """
        If paying by `p24`, this sub-hash contains details about the P24 payment method options to pass to the order's PaymentIntent.
        """
        paypal: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsPaypal"
        ]
        """
        If paying by `paypal`, this sub-hash contains details about the PayPal payment method options to pass to the order's PaymentIntent.
        """
        sepa_debit: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit"
        ]
        """
        If paying by `sepa_debit`, this sub-hash contains details about the SEPA Debit payment method options to pass to the order's PaymentIntent.
        """
        sofort: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSofort"
        ]
        """
        If paying by `sofort`, this sub-hash contains details about the Sofort payment method options to pass to the order's PaymentIntent.
        """
        wechat_pay: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsWechatPay"
        ]
        """
        If paying by `wechat_pay`, this sub-hash contains details about the WeChat Pay payment method options to pass to the order's PaymentIntent.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        verification_method: NotRequired[
            "Literal['automatic', 'instant', 'microdeposits']"
        ]
        """
        Bank account verification method.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
        TypedDict,
    ):
        custom_mandate_url: NotRequired["Literal['']|str"]
        """
        A URL for custom mandate text to render during confirmation step.
        The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
        or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
        """
        interval_description: NotRequired["str"]
        """
        Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
        """
        payment_schedule: NotRequired[
            "Literal['combined', 'interval', 'sporadic']"
        ]
        """
        Payment schedule for the mandate.
        """
        transaction_type: NotRequired["Literal['business', 'personal']"]
        """
        Transaction type of the mandate.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay(
        TypedDict,
    ):
        capture_method: NotRequired[
            "Literal['automatic', 'automatic_async', 'manual']"
        ]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        reference: NotRequired["str"]
        """
        An internal identifier or reference this payment corresponds to. The identifier is limited to 128 characters and may contain only letters, digits, underscores, backslashes and dashes.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with the payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired["Literal['de', 'en', 'fr', 'nl']"]
        """
        Preferred language of the Bancontact authorization page that the customer is redirected to.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        capture_method: NotRequired[
            "Literal['automatic', 'automatic_async', 'manual']"
        ]
        """
        Controls when the funds will be captured from the customer's account.
        """
        setup_future_usage: NotRequired[
            "Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with the payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
        ]
        """
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
        """
        funding_type: NotRequired["Literal['bank_transfer']"]
        """
        The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
        ]
        """
        Configuration for the eu_bank_transfer funding type.
        """
        requested_address_types: NotRequired[
            "List[Literal['aba', 'iban', 'sepa', 'sort_code', 'spei', 'swift', 'zengin']]"
        ]
        """
        List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

        Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
        """
        type: Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]
        """
        The list of bank transfer types that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str
        """
        The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsKlarna(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        preferred_locale: NotRequired[
            "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']"
        ]
        """
        Preferred language of the Klarna authorization page that the customer is redirected to
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsLink(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        persistent_token: NotRequired["str"]
        """
        [Deprecated] This is a legacy parameter that no longer has any function.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsOxxo(TypedDict):
        expires_after_days: NotRequired["int"]
        """
        The number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsP24(TypedDict):
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        tos_shown_and_accepted: NotRequired["bool"]
        """
        Confirm that the payer has accepted the P24 terms and conditions.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsPaypal(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.
        """
        preferred_locale: NotRequired[
            "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']"
        ]
        """
        [Preferred locale](https://stripe.com/docs/payments/paypal/supported-locales) of the PayPal checkout page that the customer is redirected to.
        """
        reference: NotRequired["str"]
        """
        A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
        """
        reference_id: NotRequired["str"]
        """
        A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
        """
        risk_correlation_id: NotRequired["str"]
        """
        The risk correlation ID for an on-session payment using a saved PayPal payment method.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        subsellers: NotRequired["List[str]"]
        """
        The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions(
        TypedDict,
    ):
        pass

    class CreateParamsPaymentSettingsPaymentMethodOptionsSofort(TypedDict):
        preferred_language: NotRequired[
            "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']"
        ]
        """
        Language shown to the payer on redirect.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsWechatPay(TypedDict):
        app_id: NotRequired["str"]
        """
        The app ID registered with WeChat Pay. Only required when client is ios or android.
        """
        client: Literal["android", "ios", "web"]
        """
        The client type that the end customer will pay from
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class CreateParamsPaymentSettingsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when the order is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        destination: str
        """
        ID of the Connected account receiving the transfer.
        """

    class CreateParamsShippingCost(TypedDict):
        shipping_rate: NotRequired["str"]
        """
        The ID of the shipping rate to use for this order.
        """
        shipping_rate_data: NotRequired[
            "Order.CreateParamsShippingCostShippingRateData"
        ]
        """
        Parameters to create a new ad-hoc shipping rate for this order.
        """

    class CreateParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimate"
        ]
        """
        The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        display_name: str
        """
        The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        fixed_amount: NotRequired[
            "Order.CreateParamsShippingCostShippingRateDataFixedAmount"
        ]
        """
        Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
        """
        tax_code: NotRequired["str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
        """
        type: NotRequired["Literal['fixed_amount']"]
        """
        The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now.
        """

    class CreateParamsShippingCostShippingRateDataDeliveryEstimate(TypedDict):
        maximum: NotRequired[
            "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
        ]
        """
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
        """
        minimum: NotRequired[
            "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
        ]
        """
        The lower bound of the estimated range. If empty, represents no lower bound.
        """

    class CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        """
        A unit of time.
        """
        value: int
        """
        Must be greater than 0.
        """

    class CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        """
        A unit of time.
        """
        value: int
        """
        Must be greater than 0.
        """

    class CreateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        currency_options: NotRequired[
            "Dict[str, Order.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]"
        ]
        """
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """

    class CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
        TypedDict,
    ):
        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
        """

    class CreateParamsShippingDetails(TypedDict):
        address: "Order.CreateParamsShippingDetailsAddress"
        """
        The shipping address for the order.
        """
        name: str
        """
        The name of the recipient of the order.
        """
        phone: NotRequired["Literal['']|str"]
        """
        The phone number (including extension) for the recipient of the order.
        """

    class CreateParamsShippingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
        """

    class CreateParamsTaxDetails(TypedDict):
        tax_exempt: NotRequired[
            "Literal['']|Literal['exempt', 'none', 'reverse']"
        ]
        """
        The purchaser's tax exemption status. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: NotRequired["List[Order.CreateParamsTaxDetailsTaxId]"]
        """
        The purchaser's tax IDs to be used for this order.
        """

    class CreateParamsTaxDetailsTaxId(TypedDict):
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "no_voec",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        """
        Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
        """
        value: str
        """
        Value of the tax ID.
        """

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListParams(RequestOptions):
        customer: NotRequired["str"]
        """
        Only return orders for the given customer.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        automatic_tax: NotRequired["Order.ModifyParamsAutomaticTax"]
        """
        Settings for automatic tax calculation for this order.
        """
        billing_details: NotRequired[
            "Literal['']|Order.ModifyParamsBillingDetails"
        ]
        """
        Billing details for the customer. If a customer is provided, this will be automatically populated with values from that customer if override values are not provided.
        """
        credits: NotRequired["Literal['']|List[Order.ModifyParamsCredit]"]
        """
        The credits to apply to the order, only `gift_card` currently supported. Pass the empty string `""` to unset this field.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: NotRequired["str"]
        """
        The customer associated with this order.
        """
        description: NotRequired["Literal['']|str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        discounts: NotRequired["Literal['']|List[Order.ModifyParamsDiscount]"]
        """
        The coupons, promotion codes, and/or discounts to apply to the order. Pass the empty string `""` to unset this field.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        ip_address: NotRequired["str"]
        """
        The IP address of the purchaser for this order.
        """
        line_items: NotRequired["List[Order.ModifyParamsLineItem]"]
        """
        A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment: NotRequired["Order.ModifyParamsPayment"]
        """
        Payment information associated with the order, including payment settings.
        """
        shipping_cost: NotRequired[
            "Literal['']|Order.ModifyParamsShippingCost"
        ]
        """
        Settings for the customer cost of shipping for this order.
        """
        shipping_details: NotRequired[
            "Literal['']|Order.ModifyParamsShippingDetails"
        ]
        """
        Shipping details for the order.
        """
        tax_details: NotRequired["Order.ModifyParamsTaxDetails"]
        """
        Additional tax details about the purchaser to be used for this order.
        """

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enable automatic tax calculation which will automatically compute tax rates on this order.
        """

    class ModifyParamsBillingDetails(TypedDict):
        address: NotRequired["Order.ModifyParamsBillingDetailsAddress"]
        """
        The billing address provided by the customer.
        """
        email: NotRequired["str"]
        """
        The billing email provided by the customer.
        """
        name: NotRequired["str"]
        """
        The billing name provided by the customer.
        """
        phone: NotRequired["str"]
        """
        The billing phone number provided by the customer.
        """

    class ModifyParamsBillingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
        """

    class ModifyParamsCredit(TypedDict):
        gift_card: NotRequired["str"]
        """
        The gift card to apply to the order.
        """
        type: Literal["gift_card"]
        """
        The type of credit to apply to the order, only `gift_card` currently supported.
        """

    class ModifyParamsDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        promotion_code: NotRequired["str"]
        """
        ID of the promotion code to create a new discount for.
        """

    class ModifyParamsLineItem(TypedDict):
        description: NotRequired["str"]
        """
        The description for the line item. Will default to the name of the associated product.
        """
        discounts: NotRequired[
            "Literal['']|List[Order.ModifyParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        id: NotRequired["str"]
        """
        The ID of an existing line item on the order.
        """
        price: NotRequired["str"]
        """
        The ID of a [Price](https://stripe.com/docs/api/prices) to add to the Order.

        The `price` parameter is an alternative to using the `product` parameter. If each of your products are sold at a single price, you can set `Product.default_price` and then pass the `product` parameter when creating a line item. If your products are sold at several possible prices, use the `price` parameter to explicitly specify which one to use.
        """
        price_data: NotRequired["Order.ModifyParamsLineItemPriceData"]
        """
        Data used to generate a new Price object inline.

        The `price_data` parameter is an alternative to using the `product` or `price` parameters. If you create products upfront and configure a `Product.default_price`, pass the `product` parameter when creating a line item. If you prefer not to define products upfront, or if you charge variable prices, pass the `price_data` parameter to describe the price for this line item.

        Each time you pass `price_data` we create a Price for the product. This Price is hidden in both the Dashboard and API lists and cannot be reused.
        """
        product: NotRequired["str"]
        """
        The ID of a [Product](https://stripe.com/docs/api/products) to add to the Order.

        The product must have a `default_price` specified. Otherwise, specify the price by passing the `price` or `price_data` parameter.
        """
        product_data: NotRequired["Order.ModifyParamsLineItemProductData"]
        """
        Defines a Product inline and adds it to the Order.

        `product_data` is an alternative to the `product` parameter. If you created a Product upfront, use the `product` parameter to refer to the existing Product. But if you prefer not to create Products upfront, pass the `product_data` parameter to define a Product inline as part of configuring the Order.

        `product_data` automatically creates a Product, just as if you had manually created the Product. If a Product with the same ID already exists, then `product_data` re-uses it to avoid duplicates.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates applied to this line item.
        """

    class ModifyParamsLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """

    class ModifyParamsLineItemPriceData(TypedDict):
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: NotRequired["str"]
        """
        ID of the product this price belongs to.

        Use this to implement a variable-pricing model in your integration. This is required if `product_data` is not specifed.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired["int"]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired["str"]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ModifyParamsLineItemProductData(TypedDict):
        description: NotRequired["Literal['']|str"]
        """
        The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
        """
        id: str
        """
        A unique identifier for this product.

        `product_data` automatically creates a Product with this ID. If a Product with the same ID already exists, then `product_data` re-uses it to avoid duplicates. If any of the fields in the existing Product are different from the values in `product_data`, `product_data` updates the existing Product with the new information. So set `product_data[id]` to the same string every time you sell the same product, but don't re-use the same string for different products.
        """
        images: NotRequired["Literal['']|List[str]"]
        """
        A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: str
        """
        The product's name, meant to be displayable to the customer.
        """
        package_dimensions: NotRequired[
            "Literal['']|Order.ModifyParamsLineItemProductDataPackageDimensions"
        ]
        """
        The dimensions of this product for shipping purposes.
        """
        shippable: NotRequired["bool"]
        """
        Whether this product is shipped (i.e., physical goods).
        """
        tax_code: NotRequired["Literal['']|str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        url: NotRequired["Literal['']|str"]
        """
        A URL of a publicly-accessible webpage for this product.
        """

    class ModifyParamsLineItemProductDataPackageDimensions(TypedDict):
        height: float
        """
        Height, in inches. Maximum precision is 2 decimal places.
        """
        length: float
        """
        Length, in inches. Maximum precision is 2 decimal places.
        """
        weight: float
        """
        Weight, in ounces. Maximum precision is 2 decimal places.
        """
        width: float
        """
        Width, in inches. Maximum precision is 2 decimal places.
        """

    class ModifyParamsPayment(TypedDict):
        settings: "Order.ModifyParamsPaymentSettings"
        """
        Settings describing how the order should configure generated PaymentIntents.
        """

    class ModifyParamsPaymentSettings(TypedDict):
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
        """
        payment_method_options: NotRequired[
            "Order.ModifyParamsPaymentSettingsPaymentMethodOptions"
        ]
        """
        PaymentMethod-specific configuration to provide to the order's PaymentIntent.
        """
        payment_method_types: NotRequired[
            "List[Literal['acss_debit', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'card', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'link', 'oxxo', 'p24', 'paypal', 'sepa_debit', 'sofort', 'wechat_pay']]"
        ]
        """
        The list of [payment method types](https://stripe.com/docs/payments/payment-methods/overview) to provide to the order's PaymentIntent. Do not include this attribute if you prefer to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
        """
        return_url: NotRequired["Literal['']|str"]
        """
        The URL to redirect the customer to after they authenticate their payment.
        """
        statement_descriptor: NotRequired["str"]
        """
        For non-card charges, you can use this value as the complete description that appears on your customers' statements. Must contain at least one letter, maximum 22 characters.
        """
        statement_descriptor_suffix: NotRequired["str"]
        """
        Provides information about a card payment that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """
        transfer_data: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsTransferData"
        ]
        """
        Provides configuration for completing a transfer for the order after it is paid.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit"
        ]
        """
        If paying by `acss_debit`, this sub-hash contains details about the ACSS Debit payment method options to pass to the order's PaymentIntent.
        """
        afterpay_clearpay: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay"
        ]
        """
        If paying by `afterpay_clearpay`, this sub-hash contains details about the AfterpayClearpay payment method options to pass to the order's PaymentIntent.
        """
        alipay: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAlipay"
        ]
        """
        If paying by `alipay`, this sub-hash contains details about the Alipay payment method options to pass to the order's PaymentIntent.
        """
        bancontact: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact"
        ]
        """
        If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the order's PaymentIntent.
        """
        card: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCard"
        ]
        """
        If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the order's PaymentIntent.
        """
        customer_balance: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance"
        ]
        """
        If paying by `customer_balance`, this sub-hash contains details about the Customer Balance payment method options to pass to the order's PaymentIntent.
        """
        ideal: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsIdeal"
        ]
        """
        If paying by `ideal`, this sub-hash contains details about the iDEAL payment method options to pass to the order's PaymentIntent.
        """
        klarna: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna"
        ]
        """
        If paying by `klarna`, this sub-hash contains details about the Klarna payment method options to pass to the order's PaymentIntent.
        """
        link: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsLink"
        ]
        """
        If paying by `link`, this sub-hash contains details about the Link payment method options to pass to the order's PaymentIntent.
        """
        oxxo: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsOxxo"
        ]
        """
        If paying by `oxxo`, this sub-hash contains details about the OXXO payment method options to pass to the order's PaymentIntent.
        """
        p24: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsP24"
        ]
        """
        If paying by `p24`, this sub-hash contains details about the P24 payment method options to pass to the order's PaymentIntent.
        """
        paypal: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsPaypal"
        ]
        """
        If paying by `paypal`, this sub-hash contains details about the PayPal payment method options to pass to the order's PaymentIntent.
        """
        sepa_debit: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit"
        ]
        """
        If paying by `sepa_debit`, this sub-hash contains details about the SEPA Debit payment method options to pass to the order's PaymentIntent.
        """
        sofort: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSofort"
        ]
        """
        If paying by `sofort`, this sub-hash contains details about the Sofort payment method options to pass to the order's PaymentIntent.
        """
        wechat_pay: NotRequired[
            "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsWechatPay"
        ]
        """
        If paying by `wechat_pay`, this sub-hash contains details about the WeChat Pay payment method options to pass to the order's PaymentIntent.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        verification_method: NotRequired[
            "Literal['automatic', 'instant', 'microdeposits']"
        ]
        """
        Bank account verification method.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
        TypedDict,
    ):
        custom_mandate_url: NotRequired["Literal['']|str"]
        """
        A URL for custom mandate text to render during confirmation step.
        The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
        or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
        """
        interval_description: NotRequired["str"]
        """
        Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
        """
        payment_schedule: NotRequired[
            "Literal['combined', 'interval', 'sporadic']"
        ]
        """
        Payment schedule for the mandate.
        """
        transaction_type: NotRequired["Literal['business', 'personal']"]
        """
        Transaction type of the mandate.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay(
        TypedDict,
    ):
        capture_method: NotRequired[
            "Literal['automatic', 'automatic_async', 'manual']"
        ]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        reference: NotRequired["str"]
        """
        An internal identifier or reference this payment corresponds to. The identifier is limited to 128 characters and may contain only letters, digits, underscores, backslashes and dashes.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with the payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired["Literal['de', 'en', 'fr', 'nl']"]
        """
        Preferred language of the Bancontact authorization page that the customer is redirected to.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
        capture_method: NotRequired[
            "Literal['automatic', 'automatic_async', 'manual']"
        ]
        """
        Controls when the funds will be captured from the customer's account.
        """
        setup_future_usage: NotRequired[
            "Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with the payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
        ]
        """
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
        """
        funding_type: NotRequired["Literal['bank_transfer']"]
        """
        The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
        ]
        """
        Configuration for the eu_bank_transfer funding type.
        """
        requested_address_types: NotRequired[
            "List[Literal['aba', 'iban', 'sepa', 'sort_code', 'spei', 'swift', 'zengin']]"
        ]
        """
        List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

        Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
        """
        type: Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]
        """
        The list of bank transfer types that this PaymentIntent is allowed to use for funding Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str
        """
        The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        preferred_locale: NotRequired[
            "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']"
        ]
        """
        Preferred language of the Klarna authorization page that the customer is redirected to
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsLink(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.

        If provided, this parameter will override the top-level `capture_method` when finalizing the payment with this payment method type.

        If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter will unset the stored value for this payment method type.
        """
        persistent_token: NotRequired["str"]
        """
        [Deprecated] This is a legacy parameter that no longer has any function.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsOxxo(TypedDict):
        expires_after_days: NotRequired["int"]
        """
        The number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsP24(TypedDict):
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        tos_shown_and_accepted: NotRequired["bool"]
        """
        Confirm that the payer has accepted the P24 terms and conditions.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsPaypal(TypedDict):
        capture_method: NotRequired["Literal['']|Literal['manual']"]
        """
        Controls when the funds will be captured from the customer's account.
        """
        preferred_locale: NotRequired[
            "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']"
        ]
        """
        [Preferred locale](https://stripe.com/docs/payments/paypal/supported-locales) of the PayPal checkout page that the customer is redirected to.
        """
        reference: NotRequired["str"]
        """
        A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
        """
        reference_id: NotRequired["str"]
        """
        A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
        """
        risk_correlation_id: NotRequired["str"]
        """
        The risk correlation ID for an on-session payment using a saved PayPal payment method.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """
        subsellers: NotRequired["List[str]"]
        """
        The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session', 'on_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions(
        TypedDict,
    ):
        pass

    class ModifyParamsPaymentSettingsPaymentMethodOptionsSofort(TypedDict):
        preferred_language: NotRequired[
            "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']"
        ]
        """
        Language shown to the payer on redirect.
        """
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsPaymentMethodOptionsWechatPay(TypedDict):
        app_id: NotRequired["str"]
        """
        The app ID registered with WeChat Pay. Only required when client is ios or android.
        """
        client: Literal["android", "ios", "web"]
        """
        The client type that the end customer will pay from
        """
        setup_future_usage: NotRequired["Literal['none']"]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class ModifyParamsPaymentSettingsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when the order is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        destination: str
        """
        ID of the Connected account receiving the transfer.
        """

    class ModifyParamsShippingCost(TypedDict):
        shipping_rate: NotRequired["str"]
        """
        The ID of the shipping rate to use for this order.
        """
        shipping_rate_data: NotRequired[
            "Order.ModifyParamsShippingCostShippingRateData"
        ]
        """
        Parameters to create a new ad-hoc shipping rate for this order.
        """

    class ModifyParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimate"
        ]
        """
        The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        display_name: str
        """
        The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        fixed_amount: NotRequired[
            "Order.ModifyParamsShippingCostShippingRateDataFixedAmount"
        ]
        """
        Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
        """
        tax_code: NotRequired["str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
        """
        type: NotRequired["Literal['fixed_amount']"]
        """
        The type of calculation to use on the shipping rate. Can only be `fixed_amount` for now.
        """

    class ModifyParamsShippingCostShippingRateDataDeliveryEstimate(TypedDict):
        maximum: NotRequired[
            "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
        ]
        """
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
        """
        minimum: NotRequired[
            "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
        ]
        """
        The lower bound of the estimated range. If empty, represents no lower bound.
        """

    class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        """
        A unit of time.
        """
        value: int
        """
        Must be greater than 0.
        """

    class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        """
        A unit of time.
        """
        value: int
        """
        Must be greater than 0.
        """

    class ModifyParamsShippingCostShippingRateDataFixedAmount(TypedDict):
        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        currency_options: NotRequired[
            "Dict[str, Order.ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]"
        ]
        """
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """

    class ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
        TypedDict,
    ):
        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        tax_behavior: NotRequired[
            "Literal['exclusive', 'inclusive', 'unspecified']"
        ]
        """
        Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
        """

    class ModifyParamsShippingDetails(TypedDict):
        address: "Order.ModifyParamsShippingDetailsAddress"
        """
        The shipping address for the order.
        """
        name: str
        """
        The name of the recipient of the order.
        """
        phone: NotRequired["Literal['']|str"]
        """
        The phone number (including extension) for the recipient of the order.
        """

    class ModifyParamsShippingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State/province as an [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) subdivision code, without country prefix. Example: "NY" or "TX".
        """

    class ModifyParamsTaxDetails(TypedDict):
        tax_exempt: NotRequired[
            "Literal['']|Literal['exempt', 'none', 'reverse']"
        ]
        """
        The purchaser's tax exemption status. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: NotRequired["List[Order.ModifyParamsTaxDetailsTaxId]"]
        """
        The purchaser's tax IDs to be used for this order.
        """

    class ModifyParamsTaxDetailsTaxId(TypedDict):
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "no_voec",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        """
        Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
        """
        value: str
        """
        Value of the tax ID.
        """

    class ReopenParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SubmitParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        expected_total: int
        """
        `expected_total` should always be set to the order's `amount_total` field. If they don't match, submitting the order will fail. This helps detect race conditions where something else concurrently modifies the order.
        """

    amount_remaining: Optional[int]
    amount_subtotal: int
    """
    Order cost before any discounts or taxes are applied. A positive integer representing the subtotal of the order in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency).
    """
    amount_total: int
    """
    Total order cost after discounts and taxes are applied. A positive integer representing the cost of the order in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). To submit an order, the total must be either 0 or at least $0.50 USD or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts).
    """
    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect application that created the Order, if any.
    """
    automatic_tax: Optional[AutomaticTax]
    billing_details: Optional[BillingDetails]
    """
    Customer billing details associated with the order.
    """
    client_secret: Optional[str]
    """
    The client secret of this Order. Used for client-side retrieval using a publishable key.

    The client secret can be used to complete a payment for an Order from your frontend. It should not be stored, logged, embedded in URLs, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.

    Refer to our docs for [creating and processing an order](https://stripe.com/docs/orders-beta/create-and-process) to learn about how client_secret should be handled.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    credits: Optional[List[Credit]]
    """
    The credits applied to the Order. At most 10 credits can be applied to an Order.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The customer which this orders belongs to.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discounts: Optional[List[ExpandableField["DiscountResource"]]]
    """
    The discounts applied to the order. Use `expand[]=discounts` to expand each discount.
    """
    id: str
    """
    Unique identifier for the object.
    """
    ip_address: Optional[str]
    """
    A recent IP address of the purchaser used for tax reporting and tax location inference.
    """
    line_items: Optional[ListObject["LineItem"]]
    """
    A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost. There is a maximum of 100 line items.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["order"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment: Payment
    shipping_cost: Optional[ShippingCost]
    """
    The details of the customer cost of shipping, including the customer chosen ShippingRate.
    """
    shipping_details: Optional[ShippingDetails]
    """
    Customer shipping information associated with the order.
    """
    status: Literal["canceled", "complete", "open", "processing", "submitted"]
    """
    The overall status of the order.
    """
    tax_details: Optional[TaxDetails]
    total_details: TotalDetails

    @classmethod
    def _cls_cancel(
        cls, id: str, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            "Order",
            cls._static_request(
                "post",
                "/v1/orders/{id}/cancel".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(id: str, **params: Unpack["Order.CancelParams"]) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @overload
    def cancel(self, **params: Unpack["Order.CancelParams"]) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders/{id}/cancel".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_async(
        cls, id: str, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            "Order",
            await cls._static_request_async(
                "post",
                "/v1/orders/{id}/cancel".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cancel_async(
        id: str, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.CancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders/{id}/cancel".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(cls, **params: Unpack["Order.CreateParams"]) -> "Order":
        """
        Creates a new open order object.
        """
        return cast(
            "Order",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["Order.CreateParams"]
    ) -> "Order":
        """
        Creates a new open order object.
        """
        return cast(
            "Order",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(cls, **params: Unpack["Order.ListParams"]) -> ListObject["Order"]:
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["Order.ListParams"]
    ) -> ListObject["Order"]:
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_line_items(
        cls, id: str, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/orders/{id}/line_items".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_line_items(
        id: str, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/orders/{id}/line_items".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_list_line_items_async(
        cls, id: str, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await cls._static_request_async(
                "get",
                "/v1/orders/{id}/line_items".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_line_items_async(
        id: str, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    async def list_line_items_async(
        self, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items_async")
    async def list_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItem"],
            await self._request_async(
                "get",
                "/v1/orders/{id}/line_items".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Order.ModifyParams"]
    ) -> "Order":
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Order",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["Order.ModifyParams"]
    ) -> "Order":
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Order",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def _cls_reopen(
        cls, id: str, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        return cast(
            "Order",
            cls._static_request(
                "post",
                "/v1/orders/{id}/reopen".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def reopen(id: str, **params: Unpack["Order.ReopenParams"]) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @overload
    def reopen(self, **params: Unpack["Order.ReopenParams"]) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @class_method_variant("_cls_reopen")
    def reopen(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders/{id}/reopen".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_reopen_async(
        cls, id: str, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        return cast(
            "Order",
            await cls._static_request_async(
                "post",
                "/v1/orders/{id}/reopen".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def reopen_async(
        id: str, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @overload
    async def reopen_async(
        self, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @class_method_variant("_cls_reopen_async")
    async def reopen_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.ReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders/{id}/reopen".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Order.RetrieveParams"]
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Order.RetrieveParams"]
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_submit(
        cls, id: str, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            cls._static_request(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def submit(id: str, **params: Unpack["Order.SubmitParams"]) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        ...

    @overload
    def submit(self, **params: Unpack["Order.SubmitParams"]) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        ...

    @class_method_variant("_cls_submit")
    def submit(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders/{id}/submit".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_submit_async(
        cls, id: str, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            await cls._static_request_async(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def submit_async(
        id: str, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        ...

    @overload
    async def submit_async(
        self, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        ...

    @class_method_variant("_cls_submit_async")
    async def submit_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Order.SubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders/{id}/submit".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "billing_details": BillingDetails,
        "credits": Credit,
        "payment": Payment,
        "shipping_cost": ShippingCost,
        "shipping_details": ShippingDetails,
        "tax_details": TaxDetails,
        "total_details": TotalDetails,
    }
