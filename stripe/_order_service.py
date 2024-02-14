# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._order import Order
from stripe._order_line_item_service import OrderLineItemService
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class OrderService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.line_items = OrderLineItemService(self._requestor)

    class CancelParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(TypedDict):
        automatic_tax: NotRequired["OrderService.CreateParamsAutomaticTax"]
        """
        Settings for automatic tax calculation for this order.
        """
        billing_details: NotRequired[
            "Literal['']|OrderService.CreateParamsBillingDetails"
        ]
        """
        Billing details for the customer. If a customer is provided, this will be automatically populated with values from that customer if override values are not provided.
        """
        credits: NotRequired[
            "Literal['']|List[OrderService.CreateParamsCredit]"
        ]
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
        discounts: NotRequired[
            "Literal['']|List[OrderService.CreateParamsDiscount]"
        ]
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
        line_items: List["OrderService.CreateParamsLineItem"]
        """
        A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment: NotRequired["OrderService.CreateParamsPayment"]
        """
        Payment information associated with the order, including payment settings.
        """
        shipping_cost: NotRequired[
            "Literal['']|OrderService.CreateParamsShippingCost"
        ]
        """
        Settings for the customer cost of shipping for this order.
        """
        shipping_details: NotRequired[
            "Literal['']|OrderService.CreateParamsShippingDetails"
        ]
        """
        Shipping details for the order.
        """
        tax_details: NotRequired["OrderService.CreateParamsTaxDetails"]
        """
        Additional tax details about the purchaser to be used for this order.
        """

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enable automatic tax calculation which will automatically compute tax rates on this order.
        """

    class CreateParamsBillingDetails(TypedDict):
        address: NotRequired["OrderService.CreateParamsBillingDetailsAddress"]
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
            "Literal['']|List[OrderService.CreateParamsLineItemDiscount]"
        ]
        """
        The discounts applied to this line item.
        """
        price: NotRequired["str"]
        """
        The ID of a [Price](https://stripe.com/docs/api/prices) to add to the Order.

        The `price` parameter is an alternative to using the `product` parameter. If each of your products are sold at a single price, you can set `Product.default_price` and then pass the `product` parameter when creating a line item. If your products are sold at several possible prices, use the `price` parameter to explicitly specify which one to use.
        """
        price_data: NotRequired["OrderService.CreateParamsLineItemPriceData"]
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
        product_data: NotRequired[
            "OrderService.CreateParamsLineItemProductData"
        ]
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
            "Literal['']|OrderService.CreateParamsLineItemProductDataPackageDimensions"
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
        settings: "OrderService.CreateParamsPaymentSettings"
        """
        Settings describing how the order should configure generated PaymentIntents.
        """

    class CreateParamsPaymentSettings(TypedDict):
        application_fee_amount: NotRequired["int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
        """
        payment_method_options: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptions"
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
            "OrderService.CreateParamsPaymentSettingsTransferData"
        ]
        """
        Provides configuration for completing a transfer for the order after it is paid.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit"
        ]
        """
        If paying by `acss_debit`, this sub-hash contains details about the ACSS Debit payment method options to pass to the order's PaymentIntent.
        """
        afterpay_clearpay: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay"
        ]
        """
        If paying by `afterpay_clearpay`, this sub-hash contains details about the AfterpayClearpay payment method options to pass to the order's PaymentIntent.
        """
        alipay: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsAlipay"
        ]
        """
        If paying by `alipay`, this sub-hash contains details about the Alipay payment method options to pass to the order's PaymentIntent.
        """
        bancontact: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact"
        ]
        """
        If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the order's PaymentIntent.
        """
        card: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsCard"
        ]
        """
        If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the order's PaymentIntent.
        """
        customer_balance: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance"
        ]
        """
        If paying by `customer_balance`, this sub-hash contains details about the Customer Balance payment method options to pass to the order's PaymentIntent.
        """
        ideal: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsIdeal"
        ]
        """
        If paying by `ideal`, this sub-hash contains details about the iDEAL payment method options to pass to the order's PaymentIntent.
        """
        klarna: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsKlarna"
        ]
        """
        If paying by `klarna`, this sub-hash contains details about the Klarna payment method options to pass to the order's PaymentIntent.
        """
        link: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsLink"
        ]
        """
        If paying by `link`, this sub-hash contains details about the Link payment method options to pass to the order's PaymentIntent.
        """
        oxxo: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsOxxo"
        ]
        """
        If paying by `oxxo`, this sub-hash contains details about the OXXO payment method options to pass to the order's PaymentIntent.
        """
        p24: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsP24"
        ]
        """
        If paying by `p24`, this sub-hash contains details about the P24 payment method options to pass to the order's PaymentIntent.
        """
        paypal: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsPaypal"
        ]
        """
        If paying by `paypal`, this sub-hash contains details about the PayPal payment method options to pass to the order's PaymentIntent.
        """
        sepa_debit: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit"
        ]
        """
        If paying by `sepa_debit`, this sub-hash contains details about the SEPA Debit payment method options to pass to the order's PaymentIntent.
        """
        sofort: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsSofort"
        ]
        """
        If paying by `sofort`, this sub-hash contains details about the Sofort payment method options to pass to the order's PaymentIntent.
        """
        wechat_pay: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsWechatPay"
        ]
        """
        If paying by `wechat_pay`, this sub-hash contains details about the WeChat Pay payment method options to pass to the order's PaymentIntent.
        """

    class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
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
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
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
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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
            "OrderService.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions"
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
            "OrderService.CreateParamsShippingCostShippingRateData"
        ]
        """
        Parameters to create a new ad-hoc shipping rate for this order.
        """

    class CreateParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            "OrderService.CreateParamsShippingCostShippingRateDataDeliveryEstimate"
        ]
        """
        The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        display_name: str
        """
        The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        fixed_amount: NotRequired[
            "OrderService.CreateParamsShippingCostShippingRateDataFixedAmount"
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
            "OrderService.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
        ]
        """
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
        """
        minimum: NotRequired[
            "OrderService.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
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
            "Dict[str, OrderService.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]"
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
        address: "OrderService.CreateParamsShippingDetailsAddress"
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
        tax_ids: NotRequired["List[OrderService.CreateParamsTaxDetailsTaxId]"]
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

    class ListParams(TypedDict):
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

    class ReopenParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SubmitParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        expected_total: int
        """
        `expected_total` should always be set to the order's `amount_total` field. If they don't match, submitting the order will fail. This helps detect race conditions where something else concurrently modifies the order.
        """

    class UpdateParams(TypedDict):
        automatic_tax: NotRequired["OrderService.UpdateParamsAutomaticTax"]
        """
        Settings for automatic tax calculation for this order.
        """
        billing_details: NotRequired[
            "Literal['']|OrderService.UpdateParamsBillingDetails"
        ]
        """
        Billing details for the customer. If a customer is provided, this will be automatically populated with values from that customer if override values are not provided.
        """
        credits: NotRequired[
            "Literal['']|List[OrderService.UpdateParamsCredit]"
        ]
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
        discounts: NotRequired[
            "Literal['']|List[OrderService.UpdateParamsDiscount]"
        ]
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
        line_items: NotRequired["List[OrderService.UpdateParamsLineItem]"]
        """
        A list of line items the customer is ordering. Each line item includes information about the product, the quantity, and the resulting cost.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment: NotRequired["OrderService.UpdateParamsPayment"]
        """
        Payment information associated with the order, including payment settings.
        """
        shipping_cost: NotRequired[
            "Literal['']|OrderService.UpdateParamsShippingCost"
        ]
        """
        Settings for the customer cost of shipping for this order.
        """
        shipping_details: NotRequired[
            "Literal['']|OrderService.UpdateParamsShippingDetails"
        ]
        """
        Shipping details for the order.
        """
        tax_details: NotRequired["OrderService.UpdateParamsTaxDetails"]
        """
        Additional tax details about the purchaser to be used for this order.
        """

    class UpdateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Enable automatic tax calculation which will automatically compute tax rates on this order.
        """

    class UpdateParamsBillingDetails(TypedDict):
        address: NotRequired["OrderService.UpdateParamsBillingDetailsAddress"]
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

    class UpdateParamsBillingDetailsAddress(TypedDict):
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

    class UpdateParamsCredit(TypedDict):
        gift_card: NotRequired["str"]
        """
        The gift card to apply to the order.
        """
        type: Literal["gift_card"]
        """
        The type of credit to apply to the order, only `gift_card` currently supported.
        """

    class UpdateParamsDiscount(TypedDict):
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

    class UpdateParamsLineItem(TypedDict):
        description: NotRequired["str"]
        """
        The description for the line item. Will default to the name of the associated product.
        """
        discounts: NotRequired[
            "Literal['']|List[OrderService.UpdateParamsLineItemDiscount]"
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
        price_data: NotRequired["OrderService.UpdateParamsLineItemPriceData"]
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
        product_data: NotRequired[
            "OrderService.UpdateParamsLineItemProductData"
        ]
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

    class UpdateParamsLineItemDiscount(TypedDict):
        coupon: NotRequired["str"]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired["str"]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """

    class UpdateParamsLineItemPriceData(TypedDict):
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

    class UpdateParamsLineItemProductData(TypedDict):
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
            "Literal['']|OrderService.UpdateParamsLineItemProductDataPackageDimensions"
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

    class UpdateParamsLineItemProductDataPackageDimensions(TypedDict):
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

    class UpdateParamsPayment(TypedDict):
        settings: "OrderService.UpdateParamsPaymentSettings"
        """
        Settings describing how the order should configure generated PaymentIntents.
        """

    class UpdateParamsPaymentSettings(TypedDict):
        application_fee_amount: NotRequired["Literal['']|int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
        """
        payment_method_options: NotRequired[
            "OrderService.UpdateParamsPaymentSettingsPaymentMethodOptions"
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
            "Literal['']|OrderService.UpdateParamsPaymentSettingsTransferData"
        ]
        """
        Provides configuration for completing a transfer for the order after it is paid.
        """

    class UpdateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsAcssDebit"
        ]
        """
        If paying by `acss_debit`, this sub-hash contains details about the ACSS Debit payment method options to pass to the order's PaymentIntent.
        """
        afterpay_clearpay: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay"
        ]
        """
        If paying by `afterpay_clearpay`, this sub-hash contains details about the AfterpayClearpay payment method options to pass to the order's PaymentIntent.
        """
        alipay: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsAlipay"
        ]
        """
        If paying by `alipay`, this sub-hash contains details about the Alipay payment method options to pass to the order's PaymentIntent.
        """
        bancontact: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsBancontact"
        ]
        """
        If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the order's PaymentIntent.
        """
        card: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsCard"
        ]
        """
        If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the order's PaymentIntent.
        """
        customer_balance: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance"
        ]
        """
        If paying by `customer_balance`, this sub-hash contains details about the Customer Balance payment method options to pass to the order's PaymentIntent.
        """
        ideal: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsIdeal"
        ]
        """
        If paying by `ideal`, this sub-hash contains details about the iDEAL payment method options to pass to the order's PaymentIntent.
        """
        klarna: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsKlarna"
        ]
        """
        If paying by `klarna`, this sub-hash contains details about the Klarna payment method options to pass to the order's PaymentIntent.
        """
        link: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsLink"
        ]
        """
        If paying by `link`, this sub-hash contains details about the Link payment method options to pass to the order's PaymentIntent.
        """
        oxxo: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsOxxo"
        ]
        """
        If paying by `oxxo`, this sub-hash contains details about the OXXO payment method options to pass to the order's PaymentIntent.
        """
        p24: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsP24"
        ]
        """
        If paying by `p24`, this sub-hash contains details about the P24 payment method options to pass to the order's PaymentIntent.
        """
        paypal: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsPaypal"
        ]
        """
        If paying by `paypal`, this sub-hash contains details about the PayPal payment method options to pass to the order's PaymentIntent.
        """
        sepa_debit: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsSepaDebit"
        ]
        """
        If paying by `sepa_debit`, this sub-hash contains details about the SEPA Debit payment method options to pass to the order's PaymentIntent.
        """
        sofort: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsSofort"
        ]
        """
        If paying by `sofort`, this sub-hash contains details about the Sofort payment method options to pass to the order's PaymentIntent.
        """
        wechat_pay: NotRequired[
            "Literal['']|OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsWechatPay"
        ]
        """
        If paying by `wechat_pay`, this sub-hash contains details about the WeChat Pay payment method options to pass to the order's PaymentIntent.
        """

    class UpdateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions"
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay(
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class UpdateParamsPaymentSettingsPaymentMethodOptionsBancontact(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
        TypedDict,
    ):
        bank_transfer: NotRequired[
            "OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer"
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            "OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str
        """
        The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
        """

    class UpdateParamsPaymentSettingsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            "Literal['']|Literal['none', 'off_session']"
        ]
        """
        Indicates that you intend to make future payments with this PaymentIntent's payment method.

        Providing this parameter will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete. If no Customer was provided, the payment method can still be [attached](https://stripe.com/docs/api/payment_methods/attach) to a Customer after the transaction completes.

        When processing card payments, Stripe also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as [SCA](https://stripe.com/docs/strong-customer-authentication).

        If `setup_future_usage` is already set and you are performing a request using a publishable key, you may only update the value from `on_session` to `off_session`.
        """

    class UpdateParamsPaymentSettingsPaymentMethodOptionsKlarna(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsLink(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsOxxo(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsP24(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsPaypal(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            "OrderService.UpdateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions"
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions(
        TypedDict,
    ):
        pass

    class UpdateParamsPaymentSettingsPaymentMethodOptionsSofort(TypedDict):
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

    class UpdateParamsPaymentSettingsPaymentMethodOptionsWechatPay(TypedDict):
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

    class UpdateParamsPaymentSettingsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when the order is paid. If no amount is set, the full amount is transferred. There cannot be any line items with recurring prices when using this field.
        """
        destination: str
        """
        ID of the Connected account receiving the transfer.
        """

    class UpdateParamsShippingCost(TypedDict):
        shipping_rate: NotRequired["str"]
        """
        The ID of the shipping rate to use for this order.
        """
        shipping_rate_data: NotRequired[
            "OrderService.UpdateParamsShippingCostShippingRateData"
        ]
        """
        Parameters to create a new ad-hoc shipping rate for this order.
        """

    class UpdateParamsShippingCostShippingRateData(TypedDict):
        delivery_estimate: NotRequired[
            "OrderService.UpdateParamsShippingCostShippingRateDataDeliveryEstimate"
        ]
        """
        The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        display_name: str
        """
        The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
        """
        fixed_amount: NotRequired[
            "OrderService.UpdateParamsShippingCostShippingRateDataFixedAmount"
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

    class UpdateParamsShippingCostShippingRateDataDeliveryEstimate(TypedDict):
        maximum: NotRequired[
            "OrderService.UpdateParamsShippingCostShippingRateDataDeliveryEstimateMaximum"
        ]
        """
        The upper bound of the estimated range. If empty, represents no upper bound i.e., infinite.
        """
        minimum: NotRequired[
            "OrderService.UpdateParamsShippingCostShippingRateDataDeliveryEstimateMinimum"
        ]
        """
        The lower bound of the estimated range. If empty, represents no lower bound.
        """

    class UpdateParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
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

    class UpdateParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
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

    class UpdateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
        amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        currency_options: NotRequired[
            "Dict[str, OrderService.UpdateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]"
        ]
        """
        Shipping rates defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
        """

    class UpdateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
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

    class UpdateParamsShippingDetails(TypedDict):
        address: "OrderService.UpdateParamsShippingDetailsAddress"
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

    class UpdateParamsShippingDetailsAddress(TypedDict):
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

    class UpdateParamsTaxDetails(TypedDict):
        tax_exempt: NotRequired[
            "Literal['']|Literal['exempt', 'none', 'reverse']"
        ]
        """
        The purchaser's tax exemption status. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: NotRequired["List[OrderService.UpdateParamsTaxDetailsTaxId]"]
        """
        The purchaser's tax IDs to be used for this order.
        """

    class UpdateParamsTaxDetailsTaxId(TypedDict):
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

    def list(
        self,
        params: "OrderService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Order]:
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        return cast(
            ListObject[Order],
            self._request(
                "get",
                "/v1/orders",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "OrderService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Order]:
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        return cast(
            ListObject[Order],
            await self._request_async(
                "get",
                "/v1/orders",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self, params: "OrderService.CreateParams", options: RequestOptions = {}
    ) -> Order:
        """
        Creates a new open order object.
        """
        return cast(
            Order,
            self._request(
                "post",
                "/v1/orders",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self, params: "OrderService.CreateParams", options: RequestOptions = {}
    ) -> Order:
        """
        Creates a new open order object.
        """
        return cast(
            Order,
            await self._request_async(
                "post",
                "/v1/orders",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "OrderService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        return cast(
            Order,
            self._request(
                "get",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "OrderService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        return cast(
            Order,
            await self._request_async(
                "get",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "OrderService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Order,
            self._request(
                "post",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "OrderService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Order,
            await self._request_async(
                "post",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "OrderService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            Order,
            self._request(
                "post",
                "/v1/orders/{id}/cancel".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "OrderService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Cancels the order as well as the payment intent if one is attached.
        """
        return cast(
            Order,
            await self._request_async(
                "post",
                "/v1/orders/{id}/cancel".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reopen(
        self,
        id: str,
        params: "OrderService.ReopenParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Reopens a submitted order.
        """
        return cast(
            Order,
            self._request(
                "post",
                "/v1/orders/{id}/reopen".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reopen_async(
        self,
        id: str,
        params: "OrderService.ReopenParams" = {},
        options: RequestOptions = {},
    ) -> Order:
        """
        Reopens a submitted order.
        """
        return cast(
            Order,
            await self._request_async(
                "post",
                "/v1/orders/{id}/reopen".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit(
        self,
        id: str,
        params: "OrderService.SubmitParams",
        options: RequestOptions = {},
    ) -> Order:
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            Order,
            self._request(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_async(
        self,
        id: str,
        params: "OrderService.SubmitParams",
        options: RequestOptions = {},
    ) -> Order:
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://stripe.com/docs/api#reopen_order) method is called.
        """
        return cast(
            Order,
            await self._request_async(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
