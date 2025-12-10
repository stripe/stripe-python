# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._customer import Customer
    from stripe._discount import Discount as DiscountResource
    from stripe._line_item import LineItem as LineItemResource
    from stripe._payment_intent import PaymentIntent
    from stripe._shipping_rate import ShippingRate
    from stripe._tax_rate import TaxRate
    from stripe.params._order_cancel_params import OrderCancelParams
    from stripe.params._order_create_params import OrderCreateParams
    from stripe.params._order_list_line_items_params import (
        OrderListLineItemsParams,
    )
    from stripe.params._order_list_params import OrderListParams
    from stripe.params._order_modify_params import OrderModifyParams
    from stripe.params._order_reopen_params import OrderReopenParams
    from stripe.params._order_retrieve_params import OrderRetrieveParams
    from stripe.params._order_submit_params import OrderSubmitParams


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
            Address line 1, such as the street, PO Box, or company name.
            """
            line2: Optional[str]
            """
            Address line 2, such as the apartment, suite, unit, or building.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """
                    target_date: Optional[str]
                    """
                    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
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

                    Providing this parameter will [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://docs.stripe.com/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

                    If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
                    """

                class Alipay(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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

                    Providing this parameter will [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the order's Customer, if present, after the order's PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://docs.stripe.com/api/payment_methods/attach) to a Customer after the transaction completes.

                    When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """
                    _inner_class_types = {"bank_transfer": BankTransfer}

                class Ideal(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """

                class Oxxo(StripeObject):
                    expires_after_days: int
                    """
                    The number of calendar days before an OXXO invoice expires. For example, if you create an OXXO invoice on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.
                    """
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """

                class P24(StripeObject):
                    setup_future_usage: Optional[Literal["none"]]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """

                class Paypal(StripeObject):
                    class LineItem(StripeObject):
                        class Tax(StripeObject):
                            amount: int
                            """
                            The tax for a single unit of the line item in minor units. Cannot be a negative number.
                            """
                            behavior: Literal["exclusive", "inclusive"]
                            """
                            The tax behavior for the line item.
                            """

                        category: Optional[
                            Literal[
                                "digital_goods", "donation", "physical_goods"
                            ]
                        ]
                        """
                        Type of the line item.
                        """
                        description: Optional[str]
                        """
                        Description of the line item.
                        """
                        name: str
                        """
                        Descriptive name of the line item.
                        """
                        quantity: int
                        """
                        Quantity of the line item. Cannot be a negative number.
                        """
                        sku: Optional[str]
                        """
                        Client facing stock keeping unit, article number or similar.
                        """
                        sold_by: Optional[str]
                        """
                        The Stripe account ID of the connected account that sells the item. This is only needed when using [Separate Charges and Transfers](https://docs.stripe.com/connect/separate-charges-and-transfers).
                        """
                        tax: Optional[Tax]
                        unit_amount: int
                        """
                        Price for a single unit of the line item in minor units. Cannot be a negative number.
                        """
                        _inner_class_types = {"tax": Tax}

                    capture_method: Optional[Literal["manual"]]
                    """
                    Controls when the funds will be captured from the customer's account.
                    """
                    line_items: Optional[List[LineItem]]
                    """
                    The line items purchased by the customer.
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """
                    subsellers: Optional[List[str]]
                    """
                    The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
                    """
                    _inner_class_types = {"line_items": LineItem}

                class SepaDebit(StripeObject):
                    class MandateOptions(StripeObject):
                        reference_prefix: Optional[str]
                        """
                        Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'STRIPE'.
                        """

                    mandate_options: Optional[MandateOptions]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    """
                    Indicates that you intend to make future payments with this PaymentIntent's payment method.

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
                    """
                    target_date: Optional[str]
                    """
                    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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

                    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

                    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

                    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
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
            The list of [payment method types](https://docs.stripe.com/payments/payment-methods/overview) to provide to the order's PaymentIntent. Do not include this attribute if you prefer to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
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
            Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

            Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
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
            Address line 1, such as the street, PO Box, or company name.
            """
            line2: Optional[str]
            """
            Address line 2, such as the apartment, suite, unit, or building.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
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
                "al_tin",
                "am_tin",
                "ao_tin",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "aw_tin",
                "az_tin",
                "ba_tin",
                "bb_tin",
                "bd_bin",
                "bf_ifu",
                "bg_uic",
                "bh_vat",
                "bj_ifu",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "bs_tin",
                "by_tin",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "cd_nif",
                "ch_uid",
                "ch_vat",
                "cl_tin",
                "cm_niu",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "cv_nif",
                "de_stn",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "et_tin",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "gn_nif",
                "hk_br",
                "hr_oib",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kg_tin",
                "kh_tin",
                "kr_brn",
                "kz_bin",
                "la_tin",
                "li_uid",
                "li_vat",
                "ma_vat",
                "md_vat",
                "me_pib",
                "mk_vat",
                "mr_nif",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "ng_tin",
                "no_vat",
                "no_voec",
                "np_pan",
                "nz_gst",
                "om_vat",
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
                "sn_ninea",
                "sr_fin",
                "sv_nit",
                "th_vat",
                "tj_tin",
                "tr_tin",
                "tw_vat",
                "tz_vat",
                "ua_vat",
                "ug_tin",
                "unknown",
                "us_ein",
                "uy_ruc",
                "uz_tin",
                "uz_vat",
                "ve_rif",
                "vn_tin",
                "za_vat",
                "zm_tin",
                "zw_tin",
            ]
            """
            The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `hr_oib`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `li_vat`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, `al_tin`, `bh_vat`, `kz_bin`, `ng_tin`, `om_vat`, `de_stn`, `ch_uid`, `tz_vat`, `uz_vat`, `uz_tin`, `md_vat`, `ma_vat`, `by_tin`, `ao_tin`, `bs_tin`, `bb_tin`, `cd_nif`, `mr_nif`, `me_pib`, `zw_tin`, `ba_tin`, `gn_nif`, `mk_vat`, `sr_fin`, `sn_ninea`, `am_tin`, `np_pan`, `tj_tin`, `ug_tin`, `zm_tin`, `kh_tin`, `aw_tin`, `az_tin`, `bd_bin`, `bj_ifu`, `et_tin`, `kg_tin`, `la_tin`, `cm_niu`, `cv_nif`, `bf_ifu`, or `unknown`
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
                A discount represents the actual application of a [coupon](https://api.stripe.com#coupons) or [promotion code](https://api.stripe.com#promotion_codes).
                It contains information about when the discount began, when it will end, and what it is applied to.

                Related guide: [Applying discounts to subscriptions](https://docs.stripe.com/billing/subscriptions/discounts)
                """

            class Tax(StripeObject):
                amount: int
                """
                Amount of tax applied for this rate.
                """
                rate: "TaxRate"
                """
                Tax rates can be applied to [invoices](https://docs.stripe.com/invoicing/taxes/tax-rates), [subscriptions](https://docs.stripe.com/billing/taxes/tax-rates) and [Checkout Sessions](https://docs.stripe.com/payments/checkout/use-manual-tax-rates) to collect tax.

                Related guide: [Tax rates](https://docs.stripe.com/billing/taxes/tax-rates)
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

    amount_subtotal: int
    """
    Order cost before any discounts or taxes are applied. A positive integer representing the subtotal of the order in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency).
    """
    amount_total: int
    """
    Total order cost after discounts and taxes are applied. A positive integer representing the cost of the order in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). To submit an order, the total must be either 0 or at least $0.50 USD or [equivalent in charge currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts).
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

    Refer to our docs for [creating and processing an order](https://docs.stripe.com/orders-beta/create-and-process) to learn about how client_secret should be handled.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
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
    line_items: Optional[ListObject["LineItemResource"]]
    """
    A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost. There is a maximum of 100 line items.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
        cls, id: str, **params: Unpack["OrderCancelParams"]
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
    def cancel(id: str, **params: Unpack["OrderCancelParams"]) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @overload
    def cancel(self, **params: Unpack["OrderCancelParams"]) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderCancelParams"]
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
        cls, id: str, **params: Unpack["OrderCancelParams"]
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
        id: str, **params: Unpack["OrderCancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["OrderCancelParams"]
    ) -> "Order":
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderCancelParams"]
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
    def create(cls, **params: Unpack["OrderCreateParams"]) -> "Order":
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
        cls, **params: Unpack["OrderCreateParams"]
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
    def list(cls, **params: Unpack["OrderListParams"]) -> ListObject["Order"]:
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
        cls, **params: Unpack["OrderListParams"]
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
        cls, id: str, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItemResource"],
            cls._static_request(
                "get",
                "/v1/orders/{id}/line_items".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_line_items(
        id: str, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItemResource"],
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
        cls, id: str, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItemResource"],
            await cls._static_request_async(
                "get",
                "/v1/orders/{id}/line_items".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def list_line_items_async(
        id: str, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    async def list_line_items_async(
        self, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items_async")
    async def list_line_items_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderListLineItemsParams"]
    ) -> ListObject["LineItemResource"]:
        """
        When retrieving an order, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject["LineItemResource"],
            await self._request_async(
                "get",
                "/v1/orders/{id}/line_items".format(
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def modify(cls, id: str, **params: Unpack["OrderModifyParams"]) -> "Order":
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
        cls, id: str, **params: Unpack["OrderModifyParams"]
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
        cls, id: str, **params: Unpack["OrderReopenParams"]
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
    def reopen(id: str, **params: Unpack["OrderReopenParams"]) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @overload
    def reopen(self, **params: Unpack["OrderReopenParams"]) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @class_method_variant("_cls_reopen")
    def reopen(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderReopenParams"]
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
        cls, id: str, **params: Unpack["OrderReopenParams"]
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
        id: str, **params: Unpack["OrderReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @overload
    async def reopen_async(
        self, **params: Unpack["OrderReopenParams"]
    ) -> "Order":
        """
        Reopens a submitted order.
        """
        ...

    @class_method_variant("_cls_reopen_async")
    async def reopen_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderReopenParams"]
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
        cls, id: str, **params: Unpack["OrderRetrieveParams"]
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["OrderRetrieveParams"]
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_submit(
        cls, id: str, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
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
    def submit(id: str, **params: Unpack["OrderSubmitParams"]) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        ...

    @overload
    def submit(self, **params: Unpack["OrderSubmitParams"]) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        ...

    @class_method_variant("_cls_submit")
    def submit(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
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
        cls, id: str, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
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
        id: str, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        ...

    @overload
    async def submit_async(
        self, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        ...

    @class_method_variant("_cls_submit_async")
    async def submit_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["OrderSubmitParams"]
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
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
        "payment": Payment,
        "shipping_cost": ShippingCost,
        "shipping_details": ShippingDetails,
        "tax_details": TaxDetails,
        "total_details": TotalDetails,
    }
