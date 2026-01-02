# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentCreateParams(RequestOptions):
    allocated_funds: NotRequired["PaymentIntentCreateParamsAllocatedFunds"]
    """
    Allocated Funds configuration for this PaymentIntent.
    """
    amount: int
    """
    Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://docs.stripe.com/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """
    amount_details: NotRequired["PaymentIntentCreateParamsAmountDetails"]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    automatic_payment_methods: NotRequired[
        "PaymentIntentCreateParamsAutomaticPaymentMethods"
    ]
    """
    When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
    """
    capture_method: NotRequired[
        Literal["automatic", "automatic_async", "manual"]
    ]
    """
    Controls when the funds will be captured from the customer's account.
    """
    confirm: NotRequired[bool]
    """
    Set to `true` to attempt to [confirm this PaymentIntent](https://docs.stripe.com/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://docs.stripe.com/api/payment_intents/confirm).
    """
    confirmation_method: NotRequired[Literal["automatic", "manual"]]
    """
    Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
    """
    confirmation_token: NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this PaymentIntent.

    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: NotRequired[str]
    """
    ID of the Customer this PaymentIntent belongs to, if one exists.

    Payment methods attached to other Customers cannot be used with this PaymentIntent.

    If [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
    """
    customer_account: NotRequired[str]
    """
    ID of the Account representing the customer that this PaymentIntent belongs to, if one exists.

    Payment methods attached to other Accounts cannot be used with this PaymentIntent.

    If [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Account after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Account instead.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    error_on_requires_action: NotRequired[bool]
    """
    Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://docs.stripe.com/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm).
    """
    excluded_payment_method_types: NotRequired[
        List[
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
                "blik",
                "boleto",
                "card",
                "cashapp",
                "crypto",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "gopay",
                "grabpay",
                "id_bank_transfer",
                "ideal",
                "kakao_pay",
                "klarna",
                "konbini",
                "kr_card",
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
                "rechnung",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "sepa_debit",
                "shopeepay",
                "sofort",
                "stripe_balance",
                "swish",
                "twint",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
        ]
    ]
    """
    The list of payment method types to exclude from use with this payment.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fx_quote: NotRequired[str]
    """
    The FX rate in the quote is validated and used to convert the presentment amount to the settlement amount.
    """
    hooks: NotRequired["PaymentIntentCreateParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    mandate: NotRequired[str]
    """
    ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm).
    """
    mandate_data: NotRequired[
        "Literal['']|PaymentIntentCreateParamsMandateData"
    ]
    """
    This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm).
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    off_session: NotRequired["bool|Literal['one_off', 'recurring']"]
    """
    Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://docs.stripe.com/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm).
    """
    on_behalf_of: NotRequired[str]
    """
    The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    payment_details: NotRequired["PaymentIntentCreateParamsPaymentDetails"]
    """
    Provides industry-specific information about the charge.
    """
    payment_method: NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://docs.stripe.com/payments/payment-methods#compatibility) object) to attach to this PaymentIntent.

    If you don't provide the `payment_method` parameter or the `source` parameter with `confirm=true`, `source` automatically populates with `customer.default_source` to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.
    If the payment method is attached to a Customer, you must also provide the ID of that Customer as the [customer](https://api.stripe.com#create_payment_intent-customer) parameter of this PaymentIntent.
    end
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the [payment method configuration](https://docs.stripe.com/api/payment_method_configurations) to use with this PaymentIntent.
    """
    payment_method_data: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodData"
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """
    payment_method_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptions"
    ]
    """
    Payment method-specific configuration for this PaymentIntent.
    """
    payment_method_types: NotRequired[List[str]]
    """
    The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
    """
    payments_orchestration: NotRequired[
        "PaymentIntentCreateParamsPaymentsOrchestration"
    ]
    """
    When you enable this parameter, this PaymentIntent will route your payment to processors that you configure in the dashboard.
    """
    radar_options: NotRequired["PaymentIntentCreateParamsRadarOptions"]
    """
    Options to configure Radar. Learn more about [Radar Sessions](https://docs.stripe.com/radar/radar-session).
    """
    receipt_email: NotRequired[str]
    """
    Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    """
    return_url: NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-confirm).
    """
    secret_key_confirmation: NotRequired[Literal["optional", "required"]]
    """
    Indicates whether confirmation for this PaymentIntent using a secret key is `required` or `optional`.
    """
    setup_future_usage: NotRequired[Literal["off_session", "on_session"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """
    shipping: NotRequired["PaymentIntentCreateParamsShipping"]
    """
    Shipping information for this PaymentIntent.
    """
    statement_descriptor: NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

    Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    """
    statement_descriptor_suffix: NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    """
    transfer_data: NotRequired["PaymentIntentCreateParamsTransferData"]
    """
    The parameters that you can use to automatically create a Transfer.
    Learn more about the [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    transfer_group: NotRequired[str]
    """
    A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://docs.stripe.com/connect/separate-charges-and-transfers).
    """
    use_stripe_sdk: NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """
    shared_payment_granted_token: NotRequired[str]
    """
    ID of the SharedPaymentToken used to confirm this PaymentIntent.
    """


class PaymentIntentCreateParamsAllocatedFunds(TypedDict):
    enabled: NotRequired[bool]
    """
    Whether Allocated Funds creation is enabled for this PaymentIntent.
    """


class PaymentIntentCreateParamsAmountDetails(TypedDict):
    discount_amount: NotRequired["Literal['']|int"]
    """
    The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[line_items][#][discount_amount]` field.
    """
    line_items: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 100 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentCreateParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired["Literal['']|PaymentIntentCreateParamsAmountDetailsTax"]
    """
    Contains information about the tax portion of the amount.
    """


class PaymentIntentCreateParamsAmountDetailsLineItem(TypedDict):
    discount_amount: NotRequired[int]
    """
    The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]` field.
    """
    payment_method_options: NotRequired[
        "PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptions"
    ]
    """
    Payment method-specific information for line items.
    """
    product_code: NotRequired[str]
    """
    The product code of the line item, such as an SKU. Required for L3 rates. At most 12 characters long.
    """
    product_name: str
    """
    The product name of the line item. Required for L3 rates. At most 1024 characters long.

    For Cards, this field is truncated to 26 alphanumeric characters before being sent to the card networks. For Paypal, this field is truncated to 127 characters.
    """
    quantity: int
    """
    The quantity of items. Required for L3 rates. An integer greater than 0.
    """
    tax: NotRequired["PaymentIntentCreateParamsAmountDetailsLineItemTax"]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    The unit cost of the line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.
    """
    unit_of_measure: NotRequired[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    """


class PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to `card` payment method."
    """
    card_present: NotRequired[
        "PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to `card_present` payment method."
    """
    klarna: NotRequired[
        "PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to `klarna` payment method."
    """
    paypal: NotRequired[
        "PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to `paypal` payment method."
    """


class PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
    TypedDict,
):
    image_url: NotRequired[str]
    """
    URL to an image for the product. Max length, 4096 characters.
    """
    product_url: NotRequired[str]
    """
    URL to the product page. Max length, 4096 characters.
    """
    reference: NotRequired[str]
    """
    Unique reference for this line item to correlate it with your system's internal records. The field is displayed in the Klarna Consumer App if passed.
    """
    subscription_reference: NotRequired[str]
    """
    Reference for the subscription this line item is for.
    """


class PaymentIntentCreateParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
    TypedDict,
):
    category: NotRequired[
        Literal["digital_goods", "donation", "physical_goods"]
    ]
    """
    Type of the line item.
    """
    description: NotRequired[str]
    """
    Description of the line item.
    """
    sold_by: NotRequired[str]
    """
    The Stripe account ID of the connected account that sells the item.
    """


class PaymentIntentCreateParamsAmountDetailsLineItemTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.
    """


class PaymentIntentCreateParamsAmountDetailsShipping(TypedDict):
    amount: NotRequired["Literal['']|int"]
    """
    If a physical good is being shipped, the cost of shipping represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than or equal to 0.
    """
    from_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped from. At most 10 alphanumeric characters long, hyphens are allowed.
    """
    to_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped to. At most 10 alphanumeric characters long, hyphens are allowed.
    """


class PaymentIntentCreateParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class PaymentIntentCreateParamsAutomaticPaymentMethods(TypedDict):
    allow_redirects: NotRequired[Literal["always", "never"]]
    """
    Controls whether this PaymentIntent will accept redirect-based payment methods.

    Redirect-based payment methods may require your customer to be redirected to a payment method's app or site for authentication or additional steps. To [confirm](https://docs.stripe.com/api/payment_intents/confirm) this PaymentIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the payment.
    """
    enabled: bool
    """
    Whether this feature is enabled.
    """


class PaymentIntentCreateParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentCreateParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentCreateParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentCreateParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentCreateParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id
    """


class PaymentIntentCreateParamsMandateData(TypedDict):
    customer_acceptance: (
        "PaymentIntentCreateParamsMandateDataCustomerAcceptance"
    )
    """
    This hash contains details about the customer acceptance of the Mandate.
    """


class PaymentIntentCreateParamsMandateDataCustomerAcceptance(TypedDict):
    accepted_at: NotRequired[int]
    """
    The time at which the customer accepted the Mandate.
    """
    offline: NotRequired[
        "PaymentIntentCreateParamsMandateDataCustomerAcceptanceOffline"
    ]
    """
    If this is a Mandate accepted offline, this hash contains details about the offline acceptance.
    """
    online: NotRequired[
        "PaymentIntentCreateParamsMandateDataCustomerAcceptanceOnline"
    ]
    """
    If this is a Mandate accepted online, this hash contains details about the online acceptance.
    """
    type: Literal["offline", "online"]
    """
    The type of customer acceptance information included with the Mandate. One of `online` or `offline`.
    """


class PaymentIntentCreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
    pass


class PaymentIntentCreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
    ip_address: str
    """
    The IP address from which the Mandate was accepted by the customer.
    """
    user_agent: str
    """
    The user agent of the browser from which the Mandate was accepted by the customer.
    """


class PaymentIntentCreateParamsPaymentDetails(TypedDict):
    benefit: NotRequired["PaymentIntentCreateParamsPaymentDetailsBenefit"]
    """
    Benefit details for this PaymentIntent
    """
    car_rental: NotRequired["PaymentIntentCreateParamsPaymentDetailsCarRental"]
    """
    Car rental details for this PaymentIntent.
    """
    car_rental_data: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentDetailsCarRentalDatum]"
    ]
    """
    Car rental data for this PaymentIntent.
    """
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    event_details: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsEventDetails"
    ]
    """
    Event details for this PaymentIntent
    """
    flight: NotRequired["PaymentIntentCreateParamsPaymentDetailsFlight"]
    """
    Flight reservation details for this PaymentIntent
    """
    flight_data: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentDetailsFlightDatum]"
    ]
    """
    Flight data for this PaymentIntent.
    """
    lodging: NotRequired["PaymentIntentCreateParamsPaymentDetailsLodging"]
    """
    Lodging reservation details for this PaymentIntent
    """
    lodging_data: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentDetailsLodgingDatum]"
    ]
    """
    Lodging data for this PaymentIntent.
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    Required when the Payment Method Types array contains `card`, including when [automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled) is set to `true`.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.
    """
    subscription: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsSubscription"
    ]
    """
    Subscription details for this PaymentIntent
    """


class PaymentIntentCreateParamsPaymentDetailsBenefit(TypedDict):
    fr_meal_voucher: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentDetailsBenefitFrMealVoucher"
    ]
    """
    French meal voucher benefit details for this PaymentIntent.
    """


class PaymentIntentCreateParamsPaymentDetailsBenefitFrMealVoucher(TypedDict):
    siret: str
    """
    The 14-digit SIRET of the meal voucher acceptor.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRental(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    booking_number: str
    """
    The booking number associated with the car rental.
    """
    car_class_code: NotRequired[str]
    """
    Class code of the car.
    """
    car_make: NotRequired[str]
    """
    Make of the car.
    """
    car_model: NotRequired[str]
    """
    Model of the car.
    """
    company: NotRequired[str]
    """
    The name of the rental car company.
    """
    customer_service_phone_number: NotRequired[str]
    """
    The customer service phone number of the car rental company.
    """
    days_rented: int
    """
    Number of days the car is being rented.
    """
    delivery: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    distance: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDistance"
    ]
    """
    The details of the distance traveled during the rental period.
    """
    drivers: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsCarRentalDriver"]
    ]
    """
    The details of the passengers in the travel reservation
    """
    extra_charges: NotRequired[
        List[
            Literal[
                "extra_mileage",
                "gas",
                "late_return",
                "one_way_service",
                "parking_violation",
            ]
        ]
    ]
    """
    List of additional charges being billed.
    """
    no_show: NotRequired[bool]
    """
    Indicates if the customer did not keep nor cancel their booking.
    """
    pickup_address: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalPickupAddress"
    ]
    """
    Car pick-up address.
    """
    pickup_at: int
    """
    Car pick-up time. Measured in seconds since the Unix epoch.
    """
    pickup_location_name: NotRequired[str]
    """
    Name of the pickup location.
    """
    rate_amount: NotRequired[int]
    """
    Rental rate.
    """
    rate_interval: NotRequired[Literal["day", "month", "week"]]
    """
    The frequency at which the rate amount is applied. One of `day`, `week` or `month`
    """
    renter_name: NotRequired[str]
    """
    The name of the person or entity renting the car.
    """
    return_address: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalReturnAddress"
    ]
    """
    Car return address.
    """
    return_at: int
    """
    Car return time. Measured in seconds since the Unix epoch.
    """
    return_location_name: NotRequired[str]
    """
    Name of the return location.
    """
    tax_exempt: NotRequired[bool]
    """
    Indicates whether the goods or services are tax-exempt or tax is not collected.
    """
    vehicle_identification_number: NotRequired[str]
    """
    The vehicle identification number.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDeliveryRecipient(
    TypedDict,
):
    email: NotRequired[str]
    """
    The email of the recipient the ticket is delivered to.
    """
    name: NotRequired[str]
    """
    The name of the recipient the ticket is delivered to.
    """
    phone: NotRequired[str]
    """
    The phone number of the recipient the ticket is delivered to.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDistance(TypedDict):
    amount: NotRequired[int]
    """
    Distance traveled.
    """
    unit: NotRequired[Literal["kilometers", "miles"]]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDriver(TypedDict):
    driver_identification_number: NotRequired[str]
    """
    Driver's identification number.
    """
    driver_tax_number: NotRequired[str]
    """
    Driver's tax number.
    """
    name: str
    """
    Full name of the person or entity on the car reservation.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalPickupAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalReturnAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatum(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumAffiliate"
    ]
    """
    Affiliate (such as travel agency) details for the rental.
    """
    booking_number: NotRequired[str]
    """
    Booking confirmation number for the car rental.
    """
    carrier_name: NotRequired[str]
    """
    Name of the car rental company.
    """
    customer_service_phone_number: NotRequired[str]
    """
    Customer service phone number for the car rental company.
    """
    days_rented: NotRequired[int]
    """
    Number of days the car is being rented.
    """
    distance: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDistance"
    ]
    """
    Distance details for the rental.
    """
    drivers: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDriver"]
    ]
    """
    List of drivers for the rental.
    """
    drop_off: "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDropOff"
    """
    Drop-off location details.
    """
    insurances: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsCarRentalDatumInsurance"]
    ]
    """
    Insurance details for the rental.
    """
    no_show_indicator: NotRequired[bool]
    """
    Indicates if the customer was a no-show.
    """
    pickup: "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumPickup"
    """
    Pickup location details.
    """
    renter_name: NotRequired[str]
    """
    Name of the person renting the vehicle.
    """
    total: "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotal"
    """
    Total cost breakdown for the rental.
    """
    vehicle: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumVehicle"
    ]
    """
    Vehicle details for the rental.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumAffiliate(
    TypedDict
):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Name of affiliate partner.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDistance(TypedDict):
    amount: int
    """
    Distance traveled.
    """
    unit: Literal["kilometers", "miles"]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDriver(TypedDict):
    date_of_birth: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDriverDateOfBirth"
    ]
    """
    Driver's date of birth.
    """
    driver_identification_number: NotRequired[str]
    """
    Driver's identification number.
    """
    driver_tax_number: NotRequired[str]
    """
    Driver's tax number.
    """
    name: str
    """
    Driver's full name.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDriverDateOfBirth(
    TypedDict,
):
    day: int
    """
    Day of birth (1-31).
    """
    month: int
    """
    Month of birth (1-12).
    """
    year: int
    """
    Year of birth (must be greater than 1900).
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDropOff(TypedDict):
    address: (
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDropOffAddress"
    )
    """
    Address of the rental location.
    """
    location_name: NotRequired[str]
    """
    Location name.
    """
    time: int
    """
    Timestamp for the location.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumDropOffAddress(
    TypedDict,
):
    city: str
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: str
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: str
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumInsurance(
    TypedDict
):
    amount: int
    """
    Amount of the insurance coverage in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the insurance amount.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the insurance company.
    """
    insurance_type: Literal[
        "liability_supplement",
        "loss_damage_waiver",
        "other",
        "partial_damage_waiver",
        "personal_accident",
        "personal_effects",
    ]
    """
    Type of insurance coverage.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumPickup(TypedDict):
    address: (
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumPickupAddress"
    )
    """
    Address of the rental location.
    """
    location_name: NotRequired[str]
    """
    Location name.
    """
    time: int
    """
    Timestamp for the location.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumPickupAddress(
    TypedDict,
):
    city: str
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: str
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: str
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotal(TypedDict):
    amount: int
    """
    Total amount in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the amount.
    """
    discounts: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalDiscounts"
    ]
    """
    Discount details for the rental.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalExtraCharge"
        ]
    ]
    """
    Additional charges for the rental.
    """
    rate_per_unit: NotRequired[int]
    """
    Rate per unit for the rental.
    """
    rate_unit: NotRequired[
        Literal["days", "kilometers", "miles", "months", "weeks"]
    ]
    """
    Unit of measurement for the rate.
    """
    tax: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalTax"
    ]
    """
    Tax breakdown for the rental.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalDiscounts(
    TypedDict,
):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """
    coupon: NotRequired[str]
    """
    Coupon code applied to the rental.
    """
    maximum_free_miles_or_kilometers: NotRequired[int]
    """
    Maximum number of free miles or kilometers included.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalExtraCharge(
    TypedDict,
):
    amount: int
    """
    Amount of the extra charge in cents.
    """
    type: Literal[
        "extra_mileage",
        "gas",
        "gps",
        "late_charge",
        "one_way_drop_off",
        "other",
        "parking",
        "phone",
        "regular_mileage",
        "towing",
    ]
    """
    Type of extra charge.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates if the transaction is tax exempt.
    """
    taxes: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalTaxTax"
        ]
    ]
    """
    Array of tax details.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumTotalTaxTax(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Tax amount.
    """
    rate: NotRequired[int]
    """
    Tax rate applied.
    """
    type: NotRequired[str]
    """
    Type of tax applied.
    """


class PaymentIntentCreateParamsPaymentDetailsCarRentalDatumVehicle(TypedDict):
    make: NotRequired[str]
    """
    Make of the rental vehicle.
    """
    model: NotRequired[str]
    """
    Model of the rental vehicle.
    """
    odometer: NotRequired[int]
    """
    Odometer reading at the time of rental.
    """
    type: NotRequired[
        Literal[
            "cargo_van",
            "compact",
            "economy",
            "exotic",
            "exotic_suv",
            "fifteen_passenger_van",
            "four_wheel_drive",
            "full_size",
            "intermediate",
            "large_suv",
            "large_truck",
            "luxury",
            "medium_suv",
            "midsize",
            "mini",
            "minivan",
            "miscellaneous",
            "moped",
            "moving_van",
            "premium",
            "regular",
            "small_medium_truck",
            "small_suv",
            "special",
            "standard",
            "stretch",
            "subcompact",
            "taxi",
            "twelve_foot_truck",
            "twelve_passenger_van",
            "twenty_foot_truck",
            "twenty_four_foot_truck",
            "twenty_six_foot_truck",
            "unique",
        ]
    ]
    """
    Type of the rental vehicle.
    """
    vehicle_class: NotRequired[
        Literal["business", "economy", "first_class", "premium_economy"]
    ]
    """
    Class of the rental vehicle.
    """
    vehicle_identification_number: NotRequired[str]
    """
    Vehicle identification number (VIN).
    """


class PaymentIntentCreateParamsPaymentDetailsEventDetails(TypedDict):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsEventDetailsAddress"
    ]
    """
    The event location's address.
    """
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsEventDetailsAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    company: NotRequired[str]
    """
    The name of the company
    """
    delivery: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsEventDetailsDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    ends_at: NotRequired[int]
    """
    Event end time. Measured in seconds since the Unix epoch.
    """
    genre: NotRequired[str]
    """
    Type of the event entertainment (concert, sports event etc)
    """
    name: str
    """
    The name of the event.
    """
    starts_at: NotRequired[int]
    """
    Event start time. Measured in seconds since the Unix epoch.
    """


class PaymentIntentCreateParamsPaymentDetailsEventDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentCreateParamsPaymentDetailsEventDetailsDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsEventDetailsDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentCreateParamsPaymentDetailsEventDetailsDeliveryRecipient(
    TypedDict,
):
    email: NotRequired[str]
    """
    The email of the recipient the ticket is delivered to.
    """
    name: NotRequired[str]
    """
    The name of the recipient the ticket is delivered to.
    """
    phone: NotRequired[str]
    """
    The phone number of the recipient the ticket is delivered to.
    """


class PaymentIntentCreateParamsPaymentDetailsFlight(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    agency_number: NotRequired[str]
    """
    The agency number (i.e. International Air Transport Association (IATA) agency number) of the travel agency that made the booking.
    """
    carrier: NotRequired[str]
    """
    The International Air Transport Association (IATA) carrier code of the carrier that issued the ticket.
    """
    delivery: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    passenger_name: NotRequired[str]
    """
    The name of the person or entity on the reservation.
    """
    passengers: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsFlightPassenger"]
    ]
    """
    The details of the passengers in the travel reservation.
    """
    segments: List["PaymentIntentCreateParamsPaymentDetailsFlightSegment"]
    """
    The individual flight segments associated with the trip.
    """
    ticket_number: NotRequired[str]
    """
    The ticket number associated with the travel reservation.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDeliveryRecipient(
    TypedDict
):
    email: NotRequired[str]
    """
    The email of the recipient the ticket is delivered to.
    """
    name: NotRequired[str]
    """
    The name of the recipient the ticket is delivered to.
    """
    phone: NotRequired[str]
    """
    The phone number of the recipient the ticket is delivered to.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the flight reservation.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightSegment(TypedDict):
    amount: NotRequired[int]
    """
    The flight segment amount.
    """
    arrival_airport: NotRequired[str]
    """
    The International Air Transport Association (IATA) airport code for the arrival airport.
    """
    arrives_at: NotRequired[int]
    """
    The arrival time for the flight segment. Measured in seconds since the Unix epoch.
    """
    carrier: NotRequired[str]
    """
    The International Air Transport Association (IATA) carrier code of the carrier operating the flight segment.
    """
    departs_at: int
    """
    The departure time for the flight segment. Measured in seconds since the Unix epoch.
    """
    departure_airport: NotRequired[str]
    """
    The International Air Transport Association (IATA) airport code for the departure airport.
    """
    flight_number: NotRequired[str]
    """
    The flight number associated with the segment
    """
    service_class: NotRequired[
        Literal["business", "economy", "first", "premium_economy"]
    ]
    """
    The fare class for the segment.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatum(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightDatumAffiliate"
    ]
    """
    Affiliate details if applicable.
    """
    booking_number: NotRequired[str]
    """
    Reservation reference.
    """
    computerized_reservation_system: NotRequired[str]
    """
    Computerized reservation system used to make the reservation and purchase the ticket.
    """
    endorsements_and_restrictions: NotRequired[str]
    """
    Ticket restrictions.
    """
    insurances: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsFlightDatumInsurance"]
    ]
    """
    List of insurances.
    """
    passengers: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsFlightDatumPassenger"]
    ]
    """
    List of passengers.
    """
    segments: List["PaymentIntentCreateParamsPaymentDetailsFlightDatumSegment"]
    """
    List of flight segments.
    """
    ticket_electronically_issued_indicator: NotRequired[bool]
    """
    Electronic ticket indicator.
    """
    total: "PaymentIntentCreateParamsPaymentDetailsFlightDatumTotal"
    """
    Total cost breakdown.
    """
    transaction_type: NotRequired[
        Literal[
            "exchange_ticket", "miscellaneous", "refund", "ticket_purchase"
        ]
    ]
    """
    Type of flight transaction.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Name of affiliate partner.
    """
    travel_authorization_code: NotRequired[str]
    """
    Code provided by the company to a travel agent authorizing ticket issuance.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumInsurance(TypedDict):
    amount: int
    """
    Insurance cost.
    """
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Insurance company name.
    """
    insurance_type: Literal[
        "baggage", "bankruptcy", "cancelation", "emergency", "medical"
    ]
    """
    Type of insurance.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumPassenger(TypedDict):
    name: str
    """
    Passenger's full name.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumSegment(TypedDict):
    amount: NotRequired[int]
    """
    Segment fare amount.
    """
    arrival: "PaymentIntentCreateParamsPaymentDetailsFlightDatumSegmentArrival"
    """
    Arrival details.
    """
    carrier_code: str
    """
    Airline carrier code.
    """
    carrier_name: NotRequired[str]
    """
    Carrier name.
    """
    currency: NotRequired[str]
    """
    Segment currency.
    """
    departure: (
        "PaymentIntentCreateParamsPaymentDetailsFlightDatumSegmentDeparture"
    )
    """
    Departure details.
    """
    exchange_ticket_number: NotRequired[str]
    """
    Exchange ticket number.
    """
    fare_basis_code: NotRequired[str]
    """
    Fare basis code.
    """
    fees: NotRequired[int]
    """
    Additional fees.
    """
    flight_number: NotRequired[str]
    """
    Flight number.
    """
    is_stop_over_indicator: NotRequired[bool]
    """
    Stopover indicator.
    """
    refundable: NotRequired[bool]
    """
    Refundable ticket indicator.
    """
    service_class: Literal[
        "business", "economy", "first_class", "premium_economy"
    ]
    """
    Class of service.
    """
    tax_amount: NotRequired[int]
    """
    Tax amount for segment.
    """
    ticket_number: NotRequired[str]
    """
    Ticket number.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumSegmentArrival(
    TypedDict,
):
    airport: str
    """
    Arrival airport IATA code.
    """
    arrives_at: NotRequired[int]
    """
    Arrival date/time.
    """
    city: NotRequired[str]
    """
    Arrival city.
    """
    country: NotRequired[str]
    """
    Arrival country.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumSegmentDeparture(
    TypedDict,
):
    airport: str
    """
    Departure airport IATA code.
    """
    city: NotRequired[str]
    """
    Departure city.
    """
    country: NotRequired[str]
    """
    Departure country.
    """
    departs_at: int
    """
    Departure date/time.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumTotal(TypedDict):
    amount: int
    """
    Total flight amount.
    """
    credit_reason: NotRequired[
        Literal[
            "other",
            "partial_ticket_refund",
            "passenger_transport_ancillary_cancellation",
            "ticket_and_ancillary_cancellation",
            "ticket_cancellation",
        ]
    ]
    """
    Reason for credit.
    """
    currency: NotRequired[str]
    """
    Total currency.
    """
    discounts: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalDiscounts"
    ]
    """
    Discount details.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalExtraCharge"
        ]
    ]
    """
    Additional charges.
    """
    tax: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalTax"
    ]
    """
    Tax breakdown.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalDiscounts(
    TypedDict,
):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalExtraCharge(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount of additional charges.
    """
    type: NotRequired[
        Literal["additional_fees", "ancillary_service_charges", "exchange_fee"]
    ]
    """
    Type of additional charges.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalTax(TypedDict):
    taxes: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalTaxTax"]
    ]
    """
    Array of tax details.
    """


class PaymentIntentCreateParamsPaymentDetailsFlightDatumTotalTaxTax(TypedDict):
    amount: NotRequired[int]
    """
    Tax amount.
    """
    rate: NotRequired[int]
    """
    Tax rate.
    """
    type: NotRequired[str]
    """
    Type of tax.
    """


class PaymentIntentCreateParamsPaymentDetailsLodging(TypedDict):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingAddress"
    ]
    """
    The lodging location's address.
    """
    adults: NotRequired[int]
    """
    The number of adults on the booking
    """
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    booking_number: NotRequired[str]
    """
    The booking number associated with the lodging reservation.
    """
    category: NotRequired[Literal["hotel", "vacation_rental"]]
    """
    The lodging category
    """
    checkin_at: int
    """
    Lodging check-in time. Measured in seconds since the Unix epoch.
    """
    checkout_at: int
    """
    Lodging check-out time. Measured in seconds since the Unix epoch.
    """
    customer_service_phone_number: NotRequired[str]
    """
    The customer service phone number of the lodging company.
    """
    daily_room_rate_amount: NotRequired[int]
    """
    The daily lodging room rate.
    """
    delivery: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    extra_charges: NotRequired[
        List[
            Literal[
                "gift_shop",
                "laundry",
                "mini_bar",
                "other",
                "restaurant",
                "telephone",
            ]
        ]
    ]
    """
    List of additional charges being billed.
    """
    fire_safety_act_compliance: NotRequired[bool]
    """
    Indicates whether the lodging location is compliant with the Fire Safety Act.
    """
    name: NotRequired[str]
    """
    The name of the lodging location.
    """
    no_show: NotRequired[bool]
    """
    Indicates if the customer did not keep their booking while failing to cancel the reservation.
    """
    number_of_rooms: NotRequired[int]
    """
    The number of rooms on the booking
    """
    passengers: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsLodgingPassenger"]
    ]
    """
    The details of the passengers in the travel reservation
    """
    property_phone_number: NotRequired[str]
    """
    The phone number of the lodging location.
    """
    room_class: NotRequired[str]
    """
    The room class for this purchase.
    """
    room_nights: NotRequired[int]
    """
    The number of room nights
    """
    total_room_tax_amount: NotRequired[int]
    """
    The total tax amount associating with the room reservation.
    """
    total_tax_amount: NotRequired[int]
    """
    The total tax amount
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDeliveryRecipient(
    TypedDict,
):
    email: NotRequired[str]
    """
    The email of the recipient the ticket is delivered to.
    """
    name: NotRequired[str]
    """
    The name of the recipient the ticket is delivered to.
    """
    phone: NotRequired[str]
    """
    The phone number of the recipient the ticket is delivered to.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the lodging reservation.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatum(TypedDict):
    accommodation: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumAccommodation"
    ]
    """
    Accommodation details for the lodging.
    """
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumAffiliate"
    ]
    """
    Affiliate details if applicable.
    """
    booking_number: NotRequired[str]
    """
    Booking confirmation number for the lodging.
    """
    checkin_at: int
    """
    Check-in date.
    """
    checkout_at: int
    """
    Check-out date.
    """
    customer_service_phone_number: NotRequired[str]
    """
    Customer service phone number for the lodging company.
    """
    fire_safety_act_compliance_indicator: NotRequired[bool]
    """
    Whether the lodging is compliant with any hotel fire safety regulations.
    """
    guests: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsLodgingDatumGuest"]
    ]
    """
    List of guests for the lodging.
    """
    host: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumHost"
    ]
    """
    Host details for the lodging.
    """
    insurances: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsLodgingDatumInsurance"]
    ]
    """
    List of insurances for the lodging.
    """
    no_show_indicator: NotRequired[bool]
    """
    Whether the renter is a no-show.
    """
    renter_id_number: NotRequired[str]
    """
    Renter ID number for the lodging.
    """
    renter_name: NotRequired[str]
    """
    Renter name for the lodging.
    """
    total: "PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotal"
    """
    Total details for the lodging.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumAccommodation(
    TypedDict,
):
    accommodation_type: NotRequired[
        Literal[
            "apartment",
            "cabana",
            "house",
            "penthouse",
            "room",
            "standard",
            "suite",
            "villa",
        ]
    ]
    """
    Type of accommodation.
    """
    bed_type: NotRequired[str]
    """
    Bed type.
    """
    daily_rate_amount: NotRequired[int]
    """
    Daily accommodation rate in cents.
    """
    nights: NotRequired[int]
    """
    Number of nights.
    """
    number_of_rooms: NotRequired[int]
    """
    Number of rooms, cabanas, apartments, and so on.
    """
    rate_type: NotRequired[str]
    """
    Rate type.
    """
    smoking_indicator: NotRequired[bool]
    """
    Whether smoking is allowed.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Affiliate partner name.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumGuest(TypedDict):
    name: str
    """
    Guest's full name.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumHost(TypedDict):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumHostAddress"
    ]
    """
    Address of the host.
    """
    country_of_domicile: NotRequired[str]
    """
    Host's country of domicile.
    """
    host_reference: NotRequired[str]
    """
    Reference number for the host.
    """
    host_type: NotRequired[
        Literal["hostel", "hotel", "owner", "rental_agency"]
    ]
    """
    Type of host.
    """
    name: NotRequired[str]
    """
    Name of the lodging property or host.
    """
    number_of_reservations: NotRequired[int]
    """
    Total number of reservations for the host.
    """
    property_phone_number: NotRequired[str]
    """
    Property phone number.
    """
    registered_at: NotRequired[int]
    """
    Host's registration date.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumHostAddress(
    TypedDict
):
    city: str
    """
    City, district, suburb, town, or village.
    """
    country: str
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: str
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: str
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumInsurance(TypedDict):
    amount: int
    """
    Price of the insurance coverage in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the insurance amount.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the insurance company.
    """
    insurance_type: Literal[
        "bankruptcy", "cancelation", "emergency", "medical"
    ]
    """
    Type of insurance coverage.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotal(TypedDict):
    amount: int
    """
    Total price of the lodging reservation in cents.
    """
    cash_advances: NotRequired[int]
    """
    Cash advances in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the total amount.
    """
    discounts: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalDiscounts"
    ]
    """
    Discount details for the lodging.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalExtraCharge"
        ]
    ]
    """
    Additional charges for the lodging.
    """
    prepaid_amount: NotRequired[int]
    """
    Prepaid amount in cents.
    """
    tax: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalTax"
    ]
    """
    Tax breakdown for the lodging reservation.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalDiscounts(
    TypedDict,
):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """
    coupon: NotRequired[str]
    """
    Coupon code.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalExtraCharge(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount of the extra charge in cents.
    """
    type: NotRequired[
        Literal[
            "gift_shop", "laundry", "mini_bar", "other", "phone", "restaurant"
        ]
    ]
    """
    Type of extra charge.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates whether the transaction is tax exempt.
    """
    taxes: NotRequired[
        List["PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalTaxTax"]
    ]
    """
    Tax details.
    """


class PaymentIntentCreateParamsPaymentDetailsLodgingDatumTotalTaxTax(
    TypedDict
):
    amount: NotRequired[int]
    """
    Tax amount in cents.
    """
    rate: NotRequired[int]
    """
    Tax rate.
    """
    type: NotRequired[str]
    """
    Type of tax applied.
    """


class PaymentIntentCreateParamsPaymentDetailsSubscription(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsSubscriptionAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    auto_renewal: NotRequired[bool]
    """
    Info whether the subscription will be auto renewed upon expiry.
    """
    billing_interval: NotRequired[
        "PaymentIntentCreateParamsPaymentDetailsSubscriptionBillingInterval"
    ]
    """
    Subscription billing details for this purchase.
    """
    ends_at: NotRequired[int]
    """
    Subscription end time. Measured in seconds since the Unix epoch.
    """
    name: str
    """
    Name of the product on subscription. e.g. Apple Music Subscription
    """
    starts_at: NotRequired[int]
    """
    Subscription start time. Measured in seconds since the Unix epoch.
    """


class PaymentIntentCreateParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentCreateParamsPaymentDetailsSubscriptionBillingInterval(
    TypedDict,
):
    count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """


class PaymentIntentCreateParamsPaymentMethodData(TypedDict):
    acss_debit: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataAcssDebit"
    ]
    """
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
    """
    affirm: NotRequired["PaymentIntentCreateParamsPaymentMethodDataAffirm"]
    """
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
    """
    afterpay_clearpay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataAfterpayClearpay"
    ]
    """
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
    """
    alipay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataAlipay"]
    """
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
    """
    allow_redisplay: NotRequired[Literal["always", "limited", "unspecified"]]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    """
    alma: NotRequired["PaymentIntentCreateParamsPaymentMethodDataAlma"]
    """
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.
    """
    amazon_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataAmazonPay"
    ]
    """
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.
    """
    au_becs_debit: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataAuBecsDebit"
    ]
    """
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    """
    bacs_debit: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataBacsDebit"
    ]
    """
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    """
    bancontact: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataBancontact"
    ]
    """
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
    """
    billie: NotRequired["PaymentIntentCreateParamsPaymentMethodDataBillie"]
    """
    If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.
    """
    billing_details: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataBillingDetails"
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """
    blik: NotRequired["PaymentIntentCreateParamsPaymentMethodDataBlik"]
    """
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
    """
    boleto: NotRequired["PaymentIntentCreateParamsPaymentMethodDataBoleto"]
    """
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    """
    cashapp: NotRequired["PaymentIntentCreateParamsPaymentMethodDataCashapp"]
    """
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
    """
    crypto: NotRequired["PaymentIntentCreateParamsPaymentMethodDataCrypto"]
    """
    If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.
    """
    customer_balance: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataCustomerBalance"
    ]
    """
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
    """
    eps: NotRequired["PaymentIntentCreateParamsPaymentMethodDataEps"]
    """
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
    """
    fpx: NotRequired["PaymentIntentCreateParamsPaymentMethodDataFpx"]
    """
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    """
    giropay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataGiropay"]
    """
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
    """
    gopay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataGopay"]
    """
    If this is a Gopay PaymentMethod, this hash contains details about the Gopay payment method.
    """
    grabpay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataGrabpay"]
    """
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
    """
    id_bank_transfer: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataIdBankTransfer"
    ]
    """
    If this is an `IdBankTransfer` PaymentMethod, this hash contains details about the IdBankTransfer payment method.
    """
    ideal: NotRequired["PaymentIntentCreateParamsPaymentMethodDataIdeal"]
    """
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    """
    interac_present: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataInteracPresent"
    ]
    """
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
    """
    kakao_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataKakaoPay"
    ]
    """
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.
    """
    klarna: NotRequired["PaymentIntentCreateParamsPaymentMethodDataKlarna"]
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    """
    konbini: NotRequired["PaymentIntentCreateParamsPaymentMethodDataKonbini"]
    """
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
    """
    kr_card: NotRequired["PaymentIntentCreateParamsPaymentMethodDataKrCard"]
    """
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.
    """
    link: NotRequired["PaymentIntentCreateParamsPaymentMethodDataLink"]
    """
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    """
    mb_way: NotRequired["PaymentIntentCreateParamsPaymentMethodDataMbWay"]
    """
    If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    mobilepay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataMobilepay"
    ]
    """
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.
    """
    multibanco: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataMultibanco"
    ]
    """
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.
    """
    naver_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataNaverPay"
    ]
    """
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    """
    nz_bank_account: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataNzBankAccount"
    ]
    """
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    """
    oxxo: NotRequired["PaymentIntentCreateParamsPaymentMethodDataOxxo"]
    """
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
    """
    p24: NotRequired["PaymentIntentCreateParamsPaymentMethodDataP24"]
    """
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
    """
    pay_by_bank: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataPayByBank"
    ]
    """
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    """
    payco: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPayco"]
    """
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.
    """
    paynow: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPaynow"]
    """
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
    """
    paypal: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPaypal"]
    """
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
    """
    paypay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPaypay"]
    """
    If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.
    """
    payto: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPayto"]
    """
    If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.
    """
    pix: NotRequired["PaymentIntentCreateParamsPaymentMethodDataPix"]
    """
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
    """
    promptpay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataPromptpay"
    ]
    """
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
    """
    qris: NotRequired["PaymentIntentCreateParamsPaymentMethodDataQris"]
    """
    If this is a `qris` PaymentMethod, this hash contains details about the QRIS payment method.
    """
    radar_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataRadarOptions"
    ]
    """
    Options to configure Radar. See [Radar Session](https://docs.stripe.com/radar/radar-session) for more information.
    """
    rechnung: NotRequired["PaymentIntentCreateParamsPaymentMethodDataRechnung"]
    """
    If this is a `rechnung` PaymentMethod, this hash contains details about the Rechnung payment method.
    """
    revolut_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataRevolutPay"
    ]
    """
    If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
    """
    samsung_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataSamsungPay"
    ]
    """
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.
    """
    satispay: NotRequired["PaymentIntentCreateParamsPaymentMethodDataSatispay"]
    """
    If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.
    """
    sepa_debit: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataSepaDebit"
    ]
    """
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    """
    shopeepay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataShopeepay"
    ]
    """
    If this is a Shopeepay PaymentMethod, this hash contains details about the Shopeepay payment method.
    """
    sofort: NotRequired["PaymentIntentCreateParamsPaymentMethodDataSofort"]
    """
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    """
    stripe_balance: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataStripeBalance"
    ]
    """
    This hash contains details about the Stripe balance payment method.
    """
    swish: NotRequired["PaymentIntentCreateParamsPaymentMethodDataSwish"]
    """
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.
    """
    twint: NotRequired["PaymentIntentCreateParamsPaymentMethodDataTwint"]
    """
    If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.
    """
    type: Literal[
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
        "blik",
        "boleto",
        "cashapp",
        "crypto",
        "customer_balance",
        "eps",
        "fpx",
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
        "rechnung",
        "revolut_pay",
        "samsung_pay",
        "satispay",
        "sepa_debit",
        "shopeepay",
        "sofort",
        "stripe_balance",
        "swish",
        "twint",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataUsBankAccount"
    ]
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """
    wechat_pay: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodDataWechatPay"
    ]
    """
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
    """
    zip: NotRequired["PaymentIntentCreateParamsPaymentMethodDataZip"]
    """
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
    """


class PaymentIntentCreateParamsPaymentMethodDataAcssDebit(TypedDict):
    account_number: str
    """
    Customer's bank account number.
    """
    institution_number: str
    """
    Institution number of the customer's bank.
    """
    transit_number: str
    """
    Transit number of the customer's bank.
    """


class PaymentIntentCreateParamsPaymentMethodDataAffirm(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataAfterpayClearpay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataAlipay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataAlma(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataAmazonPay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataAuBecsDebit(TypedDict):
    account_number: str
    """
    The account number for the bank account.
    """
    bsb_number: str
    """
    Bank-State-Branch number of the bank account.
    """


class PaymentIntentCreateParamsPaymentMethodDataBacsDebit(TypedDict):
    account_number: NotRequired[str]
    """
    Account number of the bank account that the funds will be debited from.
    """
    sort_code: NotRequired[str]
    """
    Sort code of the bank account. (e.g., `10-20-30`)
    """


class PaymentIntentCreateParamsPaymentMethodDataBancontact(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataBillie(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodDataBillingDetailsAddress"
    ]
    """
    Billing address.
    """
    email: NotRequired["Literal['']|str"]
    """
    Email address.
    """
    name: NotRequired["Literal['']|str"]
    """
    Full name.
    """
    phone: NotRequired["Literal['']|str"]
    """
    Billing phone number (including extension).
    """
    tax_id: NotRequired[str]
    """
    Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.
    """


class PaymentIntentCreateParamsPaymentMethodDataBillingDetailsAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentMethodDataBlik(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataBoleto(TypedDict):
    tax_id: str
    """
    The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
    """


class PaymentIntentCreateParamsPaymentMethodDataCashapp(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataCrypto(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataCustomerBalance(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataEps(TypedDict):
    bank: NotRequired[
        Literal[
            "arzte_und_apotheker_bank",
            "austrian_anadi_bank_ag",
            "bank_austria",
            "bankhaus_carl_spangler",
            "bankhaus_schelhammer_und_schattera_ag",
            "bawag_psk_ag",
            "bks_bank_ag",
            "brull_kallmus_bank_ag",
            "btv_vier_lander_bank",
            "capital_bank_grawe_gruppe_ag",
            "deutsche_bank_ag",
            "dolomitenbank",
            "easybank_ag",
            "erste_bank_und_sparkassen",
            "hypo_alpeadriabank_international_ag",
            "hypo_bank_burgenland_aktiengesellschaft",
            "hypo_noe_lb_fur_niederosterreich_u_wien",
            "hypo_oberosterreich_salzburg_steiermark",
            "hypo_tirol_bank_ag",
            "hypo_vorarlberg_bank_ag",
            "marchfelder_bank",
            "oberbank_ag",
            "raiffeisen_bankengruppe_osterreich",
            "schoellerbank_ag",
            "sparda_bank_wien",
            "volksbank_gruppe",
            "volkskreditbank_ag",
            "vr_bank_braunau",
        ]
    ]
    """
    The customer's bank.
    """


class PaymentIntentCreateParamsPaymentMethodDataFpx(TypedDict):
    account_holder_type: NotRequired[Literal["company", "individual"]]
    """
    Account holder type for FPX transaction
    """
    bank: Literal[
        "affin_bank",
        "agrobank",
        "alliance_bank",
        "ambank",
        "bank_islam",
        "bank_muamalat",
        "bank_of_china",
        "bank_rakyat",
        "bsn",
        "cimb",
        "deutsche_bank",
        "hong_leong_bank",
        "hsbc",
        "kfh",
        "maybank2e",
        "maybank2u",
        "ocbc",
        "pb_enterprise",
        "public_bank",
        "rhb",
        "standard_chartered",
        "uob",
    ]
    """
    The customer's bank.
    """


class PaymentIntentCreateParamsPaymentMethodDataGiropay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataGopay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataGrabpay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataIdBankTransfer(TypedDict):
    bank: NotRequired[Literal["bca", "bni", "bri", "cimb", "permata"]]
    """
    Bank where the account is held.
    """


class PaymentIntentCreateParamsPaymentMethodDataIdeal(TypedDict):
    bank: NotRequired[
        Literal[
            "abn_amro",
            "asn_bank",
            "bunq",
            "buut",
            "finom",
            "handelsbanken",
            "ing",
            "knab",
            "mollie",
            "moneyou",
            "n26",
            "nn",
            "rabobank",
            "regiobank",
            "revolut",
            "sns_bank",
            "triodos_bank",
            "van_lanschot",
            "yoursafe",
        ]
    ]
    """
    The customer's bank. Only use this parameter for existing customers. Don't use it for new customers.
    """


class PaymentIntentCreateParamsPaymentMethodDataInteracPresent(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataKakaoPay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataKlarna(TypedDict):
    dob: NotRequired["PaymentIntentCreateParamsPaymentMethodDataKlarnaDob"]
    """
    Customer's date of birth
    """


class PaymentIntentCreateParamsPaymentMethodDataKlarnaDob(TypedDict):
    day: int
    """
    The day of birth, between 1 and 31.
    """
    month: int
    """
    The month of birth, between 1 and 12.
    """
    year: int
    """
    The four-digit year of birth.
    """


class PaymentIntentCreateParamsPaymentMethodDataKonbini(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataKrCard(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataLink(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataMbWay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataMobilepay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataMultibanco(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataNaverPay(TypedDict):
    funding: NotRequired[Literal["card", "points"]]
    """
    Whether to use Naver Pay points or a card to fund this transaction. If not provided, this defaults to `card`.
    """


class PaymentIntentCreateParamsPaymentMethodDataNzBankAccount(TypedDict):
    account_holder_name: NotRequired[str]
    """
    The name on the bank account. Only required if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod's billing details.
    """
    account_number: str
    """
    The account number for the bank account.
    """
    bank_code: str
    """
    The numeric code for the bank account's bank.
    """
    branch_code: str
    """
    The numeric code for the bank account's bank branch.
    """
    reference: NotRequired[str]
    suffix: str
    """
    The suffix of the bank account number.
    """


class PaymentIntentCreateParamsPaymentMethodDataOxxo(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataP24(TypedDict):
    bank: NotRequired[
        Literal[
            "alior_bank",
            "bank_millennium",
            "bank_nowy_bfg_sa",
            "bank_pekao_sa",
            "banki_spbdzielcze",
            "blik",
            "bnp_paribas",
            "boz",
            "citi_handlowy",
            "credit_agricole",
            "envelobank",
            "etransfer_pocztowy24",
            "getin_bank",
            "ideabank",
            "ing",
            "inteligo",
            "mbank_mtransfer",
            "nest_przelew",
            "noble_pay",
            "pbac_z_ipko",
            "plus_bank",
            "santander_przelew24",
            "tmobile_usbugi_bankowe",
            "toyota_bank",
            "velobank",
            "volkswagen_bank",
        ]
    ]
    """
    The customer's bank.
    """


class PaymentIntentCreateParamsPaymentMethodDataPayByBank(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPayco(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPaynow(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPaypal(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPaypay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPayto(TypedDict):
    account_number: NotRequired[str]
    """
    The account number for the bank account.
    """
    bsb_number: NotRequired[str]
    """
    Bank-State-Branch number of the bank account.
    """
    pay_id: NotRequired[str]
    """
    The PayID alias for the bank account.
    """


class PaymentIntentCreateParamsPaymentMethodDataPix(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataPromptpay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataQris(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataRadarOptions(TypedDict):
    session: NotRequired[str]
    """
    A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
    """


class PaymentIntentCreateParamsPaymentMethodDataRechnung(TypedDict):
    dob: "PaymentIntentCreateParamsPaymentMethodDataRechnungDob"
    """
    Customer's date of birth
    """


class PaymentIntentCreateParamsPaymentMethodDataRechnungDob(TypedDict):
    day: int
    """
    The day of birth, between 1 and 31.
    """
    month: int
    """
    The month of birth, between 1 and 12.
    """
    year: int
    """
    The four-digit year of birth.
    """


class PaymentIntentCreateParamsPaymentMethodDataRevolutPay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataSamsungPay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataSatispay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataSepaDebit(TypedDict):
    iban: str
    """
    IBAN of the bank account.
    """


class PaymentIntentCreateParamsPaymentMethodDataShopeepay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataSofort(TypedDict):
    country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    """
    Two-letter ISO code representing the country the bank account is located in.
    """


class PaymentIntentCreateParamsPaymentMethodDataStripeBalance(TypedDict):
    account: NotRequired[str]
    """
    The connected account ID whose Stripe balance to use as the source of payment
    """
    source_type: NotRequired[Literal["bank_account", "card", "fpx"]]
    """
    The [source_type](https://docs.stripe.com/api/balance/balance_object#balance_object-available-source_types) of the balance
    """


class PaymentIntentCreateParamsPaymentMethodDataSwish(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataTwint(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataUsBankAccount(TypedDict):
    account_holder_type: NotRequired[Literal["company", "individual"]]
    """
    Account holder type: individual or company.
    """
    account_number: NotRequired[str]
    """
    Account number of the bank account.
    """
    account_type: NotRequired[Literal["checking", "savings"]]
    """
    Account type: checkings or savings. Defaults to checking if omitted.
    """
    financial_connections_account: NotRequired[str]
    """
    The ID of a Financial Connections Account to use as a payment method.
    """
    routing_number: NotRequired[str]
    """
    Routing number of the bank account.
    """


class PaymentIntentCreateParamsPaymentMethodDataWechatPay(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodDataZip(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAcssDebit"
    ]
    """
    If this is a `acss_debit` PaymentMethod, this sub-hash contains details about the ACSS Debit payment method options.
    """
    affirm: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAffirm"
    ]
    """
    If this is an `affirm` PaymentMethod, this sub-hash contains details about the Affirm payment method options.
    """
    afterpay_clearpay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAfterpayClearpay"
    ]
    """
    If this is a `afterpay_clearpay` PaymentMethod, this sub-hash contains details about the Afterpay Clearpay payment method options.
    """
    alipay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAlipay"
    ]
    """
    If this is a `alipay` PaymentMethod, this sub-hash contains details about the Alipay payment method options.
    """
    alma: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAlma"
    ]
    """
    If this is a `alma` PaymentMethod, this sub-hash contains details about the Alma payment method options.
    """
    amazon_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAmazonPay"
    ]
    """
    If this is a `amazon_pay` PaymentMethod, this sub-hash contains details about the Amazon Pay payment method options.
    """
    au_becs_debit: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsAuBecsDebit"
    ]
    """
    If this is a `au_becs_debit` PaymentMethod, this sub-hash contains details about the AU BECS Direct Debit payment method options.
    """
    bacs_debit: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsBacsDebit"
    ]
    """
    If this is a `bacs_debit` PaymentMethod, this sub-hash contains details about the BACS Debit payment method options.
    """
    bancontact: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsBancontact"
    ]
    """
    If this is a `bancontact` PaymentMethod, this sub-hash contains details about the Bancontact payment method options.
    """
    billie: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsBillie"
    ]
    """
    If this is a `billie` PaymentMethod, this sub-hash contains details about the Billie payment method options.
    """
    blik: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsBlik"
    ]
    """
    If this is a `blik` PaymentMethod, this sub-hash contains details about the BLIK payment method options.
    """
    boleto: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsBoleto"
    ]
    """
    If this is a `boleto` PaymentMethod, this sub-hash contains details about the Boleto payment method options.
    """
    card: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCard"
    ]
    """
    Configuration for any card payments attempted on this PaymentIntent.
    """
    card_present: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCardPresent"
    ]
    """
    If this is a `card_present` PaymentMethod, this sub-hash contains details about the Card Present payment method options.
    """
    cashapp: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCashapp"
    ]
    """
    If this is a `cashapp` PaymentMethod, this sub-hash contains details about the Cash App Pay payment method options.
    """
    crypto: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCrypto"
    ]
    """
    If this is a `crypto` PaymentMethod, this sub-hash contains details about the Crypto payment method options.
    """
    customer_balance: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalance"
    ]
    """
    If this is a `customer balance` PaymentMethod, this sub-hash contains details about the customer balance payment method options.
    """
    eps: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsEps"
    ]
    """
    If this is a `eps` PaymentMethod, this sub-hash contains details about the EPS payment method options.
    """
    fpx: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsFpx"
    ]
    """
    If this is a `fpx` PaymentMethod, this sub-hash contains details about the FPX payment method options.
    """
    giropay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsGiropay"
    ]
    """
    If this is a `giropay` PaymentMethod, this sub-hash contains details about the Giropay payment method options.
    """
    gopay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsGopay"
    ]
    """
    If this is a `gopay` PaymentMethod, this sub-hash contains details about the Gopay payment method options.
    """
    grabpay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsGrabpay"
    ]
    """
    If this is a `grabpay` PaymentMethod, this sub-hash contains details about the Grabpay payment method options.
    """
    id_bank_transfer: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsIdBankTransfer"
    ]
    """
    If this is a `id_bank_transfer` PaymentMethod, this sub-hash contains details about the Indonesia Bank Transfer payment method options.
    """
    ideal: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsIdeal"
    ]
    """
    If this is a `ideal` PaymentMethod, this sub-hash contains details about the Ideal payment method options.
    """
    interac_present: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsInteracPresent"
    ]
    """
    If this is a `interac_present` PaymentMethod, this sub-hash contains details about the Card Present payment method options.
    """
    kakao_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsKakaoPay"
    ]
    """
    If this is a `kakao_pay` PaymentMethod, this sub-hash contains details about the Kakao Pay payment method options.
    """
    klarna: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsKlarna"
    ]
    """
    If this is a `klarna` PaymentMethod, this sub-hash contains details about the Klarna payment method options.
    """
    konbini: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsKonbini"
    ]
    """
    If this is a `konbini` PaymentMethod, this sub-hash contains details about the Konbini payment method options.
    """
    kr_card: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsKrCard"
    ]
    """
    If this is a `kr_card` PaymentMethod, this sub-hash contains details about the KR Card payment method options.
    """
    link: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsLink"
    ]
    """
    If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
    """
    mb_way: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsMbWay"
    ]
    """
    If this is a `mb_way` PaymentMethod, this sub-hash contains details about the MB WAY payment method options.
    """
    mobilepay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsMobilepay"
    ]
    """
    If this is a `MobilePay` PaymentMethod, this sub-hash contains details about the MobilePay payment method options.
    """
    multibanco: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsMultibanco"
    ]
    """
    If this is a `multibanco` PaymentMethod, this sub-hash contains details about the Multibanco payment method options.
    """
    naver_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsNaverPay"
    ]
    """
    If this is a `naver_pay` PaymentMethod, this sub-hash contains details about the Naver Pay payment method options.
    """
    nz_bank_account: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsNzBankAccount"
    ]
    """
    If this is a `nz_bank_account` PaymentMethod, this sub-hash contains details about the NZ BECS Direct Debit payment method options.
    """
    oxxo: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsOxxo"
    ]
    """
    If this is a `oxxo` PaymentMethod, this sub-hash contains details about the OXXO payment method options.
    """
    p24: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsP24"
    ]
    """
    If this is a `p24` PaymentMethod, this sub-hash contains details about the Przelewy24 payment method options.
    """
    pay_by_bank: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPayByBank"
    ]
    """
    If this is a `pay_by_bank` PaymentMethod, this sub-hash contains details about the PayByBank payment method options.
    """
    payco: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPayco"
    ]
    """
    If this is a `payco` PaymentMethod, this sub-hash contains details about the PAYCO payment method options.
    """
    paynow: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPaynow"
    ]
    """
    If this is a `paynow` PaymentMethod, this sub-hash contains details about the PayNow payment method options.
    """
    paypal: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPaypal"
    ]
    """
    If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
    """
    paypay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPaypay"
    ]
    """
    If this is a `paypay` PaymentMethod, this sub-hash contains details about the PayPay payment method options.
    """
    payto: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPayto"
    ]
    """
    If this is a `payto` PaymentMethod, this sub-hash contains details about the PayTo payment method options.
    """
    pix: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPix"
    ]
    """
    If this is a `pix` PaymentMethod, this sub-hash contains details about the Pix payment method options.
    """
    promptpay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsPromptpay"
    ]
    """
    If this is a `promptpay` PaymentMethod, this sub-hash contains details about the PromptPay payment method options.
    """
    qris: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsQris"
    ]
    """
    If this is a `qris` PaymentMethod, this sub-hash contains details about the QRIS payment method options.
    """
    rechnung: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsRechnung"
    ]
    """
    If this is a `rechnung` PaymentMethod, this sub-hash contains details about the Rechnung payment method options.
    """
    revolut_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsRevolutPay"
    ]
    """
    If this is a `revolut_pay` PaymentMethod, this sub-hash contains details about the Revolut Pay payment method options.
    """
    samsung_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsSamsungPay"
    ]
    """
    If this is a `samsung_pay` PaymentMethod, this sub-hash contains details about the Samsung Pay payment method options.
    """
    satispay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsSatispay"
    ]
    """
    If this is a `satispay` PaymentMethod, this sub-hash contains details about the Satispay payment method options.
    """
    sepa_debit: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsSepaDebit"
    ]
    """
    If this is a `sepa_debit` PaymentIntent, this sub-hash contains details about the SEPA Debit payment method options.
    """
    shopeepay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsShopeepay"
    ]
    """
    If this is a `shopeepay` PaymentMethod, this sub-hash contains details about the ShopeePay payment method options.
    """
    sofort: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsSofort"
    ]
    """
    If this is a `sofort` PaymentMethod, this sub-hash contains details about the SOFORT payment method options.
    """
    stripe_balance: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsStripeBalance"
    ]
    """
    If this is a `stripe_balance` PaymentMethod, this sub-hash contains details about the Stripe Balance payment method options.
    """
    swish: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsSwish"
    ]
    """
    If this is a `Swish` PaymentMethod, this sub-hash contains details about the Swish payment method options.
    """
    twint: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsTwint"
    ]
    """
    If this is a `twint` PaymentMethod, this sub-hash contains details about the TWINT payment method options.
    """
    us_bank_account: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccount"
    ]
    """
    If this is a `us_bank_account` PaymentMethod, this sub-hash contains details about the US bank account payment method options.
    """
    wechat_pay: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsWechatPay"
    ]
    """
    If this is a `wechat_pay` PaymentMethod, this sub-hash contains details about the WeChat Pay payment method options.
    """
    zip: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsZip"
    ]
    """
    If this is a `zip` PaymentMethod, this sub-hash contains details about the Zip payment method options.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsAcssDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """
    verification_method: NotRequired[
        Literal["automatic", "instant", "microdeposits"]
    ]
    """
    Bank account verification method.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    custom_mandate_url: NotRequired["Literal['']|str"]
    """
    A URL for custom mandate text to render during confirmation step.
    The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
    or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
    """
    interval_description: NotRequired[str]
    """
    Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
    """
    payment_schedule: NotRequired[Literal["combined", "interval", "sporadic"]]
    """
    Payment schedule for the mandate.
    """
    transaction_type: NotRequired[Literal["business", "personal"]]
    """
    Transaction type of the mandate.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAffirm(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    preferred_locale: NotRequired[str]
    """
    Preferred language of the Affirm authorization page that the customer is redirected to.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    reference: NotRequired[str]
    """
    An internal identifier or reference that this payment corresponds to. You must limit the identifier to 128 characters, and it can only contain letters, numbers, underscores, backslashes, and dashes.
    This field differs from the statement descriptor and item name.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAlipay(TypedDict):
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAlma(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAmazonPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBacsDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsBacsDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBacsDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'DDIC' or 'STRIPE'.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBancontact(TypedDict):
    preferred_language: NotRequired[Literal["de", "en", "fr", "nl"]]
    """
    Preferred language of the Bancontact authorization page that the customer is redirected to.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBillie(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBlik(TypedDict):
    code: NotRequired[str]
    """
    The 6-digit BLIK code that a customer has generated using their banking application. Can only be set on confirmation.
    """
    setup_future_usage: NotRequired["Literal['']|Literal['none']"]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsBoleto(TypedDict):
    expires_after_days: NotRequired[int]
    """
    The number of calendar days before a Boleto voucher expires. For example, if you create a Boleto voucher on Monday and you set expires_after_days to 2, the Boleto invoice will expire on Wednesday at 23:59 America/Sao_Paulo time.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCard(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    cvc_token: NotRequired[str]
    """
    A single-use `cvc_update` Token that represents a card CVC value. When provided, the CVC value will be verified during the card payment attempt. This parameter can only be provided during confirmation.
    """
    installments: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardInstallments"
    ]
    """
    Installment configuration for payments attempted on this PaymentIntent.

    For more information, see the [installments integration guide](https://docs.stripe.com/payments/installments).
    """
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardMandateOptions"
    ]
    """
    Configuration options for setting up an eMandate for cards issued in India.
    """
    moto: NotRequired[bool]
    """
    When specified, this parameter indicates that a transaction will be marked
    as MOTO (Mail Order Telephone Order) and thus out of scope for SCA. This
    parameter can only be provided during confirmation.
    """
    network: NotRequired[
        Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ]
    """
    Selected network to process this PaymentIntent on. Depends on the available networks of the card attached to the PaymentIntent. Can be only set confirm-time.
    """
    request_decremental_authorization: NotRequired[
        Literal["if_available", "never"]
    ]
    """
    Request ability to [decrement the authorization](https://docs.stripe.com/payments/decremental-authorization) for this PaymentIntent.
    """
    request_extended_authorization: NotRequired[
        Literal["if_available", "never"]
    ]
    """
    Request ability to [capture beyond the standard authorization validity window](https://docs.stripe.com/payments/extended-authorization) for this PaymentIntent.
    """
    request_incremental_authorization: NotRequired[
        Literal["if_available", "never"]
    ]
    """
    Request ability to [increment the authorization](https://docs.stripe.com/payments/incremental-authorization) for this PaymentIntent.
    """
    request_multicapture: NotRequired[Literal["if_available", "never"]]
    """
    Request ability to make [multiple captures](https://docs.stripe.com/payments/multicapture) for this PaymentIntent.
    """
    request_overcapture: NotRequired[Literal["if_available", "never"]]
    """
    Request ability to [overcapture](https://docs.stripe.com/payments/overcapture) for this PaymentIntent.
    """
    request_partial_authorization: NotRequired[
        Literal["if_available", "never"]
    ]
    """
    Request partial authorization on this PaymentIntent.
    """
    request_three_d_secure: NotRequired[
        Literal["any", "automatic", "challenge"]
    ]
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://docs.stripe.com/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://docs.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """
    require_cvc_recollection: NotRequired[bool]
    """
    When enabled, using a card that is attached to a customer will require the CVC to be provided again (i.e. using the cvc_token parameter).
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    statement_descriptor_suffix_kana: NotRequired["Literal['']|str"]
    """
    Provides information about a card payment that customers see on their statements. Concatenated with the Kana prefix (shortened Kana descriptor) or Kana statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 22 characters.
    """
    statement_descriptor_suffix_kanji: NotRequired["Literal['']|str"]
    """
    Provides information about a card payment that customers see on their statements. Concatenated with the Kanji prefix (shortened Kanji descriptor) or Kanji statement descriptor that's set on the account to form the complete statement descriptor. Maximum 17 characters. On card statements, the *concatenation* of both prefix and suffix (including separators) will appear truncated to 17 characters.
    """
    statement_details: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCardStatementDetails"
    ]
    """
    Statement details for this payment intent. You can use this to override the merchant details shown on your customers' statements.
    """
    three_d_secure: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecure"
    ]
    """
    If 3D Secure authentication was performed with a third-party provider,
    the authentication details to use for this payment.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardInstallments(TypedDict):
    enabled: NotRequired[bool]
    """
    Setting to true enables installments for this PaymentIntent.
    This will cause the response to contain a list of available installment plans.
    Setting to false will prevent any selected plan from applying to a charge.
    """
    plan: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsCardInstallmentsPlan"
    ]
    """
    The selected installment plan to use for this payment attempt.
    This parameter can only be provided during confirmation.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardInstallmentsPlan(
    TypedDict,
):
    count: NotRequired[int]
    """
    For `fixed_count` installment plans, this is required. It represents the number of installment payments your customer will make to their credit card.
    """
    interval: NotRequired[Literal["month"]]
    """
    For `fixed_count` installment plans, this is required. It represents the interval between installment payments your customer will make to their credit card.
    One of `month`.
    """
    type: Literal["bonus", "fixed_count", "revolving"]
    """
    Type of installment plan, one of `fixed_count`, `bonus`, or `revolving`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardMandateOptions(
    TypedDict,
):
    amount: int
    """
    Amount to be charged for future payments.
    """
    amount_type: Literal["fixed", "maximum"]
    """
    One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
    """
    description: NotRequired[str]
    """
    A description of the mandate or subscription that is meant to be displayed to the customer.
    """
    end_date: NotRequired[int]
    """
    End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
    """
    interval: Literal["day", "month", "sporadic", "week", "year"]
    """
    Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
    """
    reference: str
    """
    Unique identifier for the mandate or subscription.
    """
    start_date: int
    """
    Start date of the mandate or subscription. Start date should not be lesser than yesterday.
    """
    supported_types: NotRequired[List[Literal["india"]]]
    """
    Specifies the type of mandates supported. Possible values are `india`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardStatementDetails(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardStatementDetailsAddress"
    ]
    """
    Please pass in an address that is within your Stripe user account country
    """
    phone: NotRequired[str]
    """
    Phone number (e.g., a toll-free number that customers can call)
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardStatementDetailsAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecure(TypedDict):
    ares_trans_status: NotRequired[Literal["A", "C", "I", "N", "R", "U", "Y"]]
    """
    The `transStatus` returned from the card Issuer's ACS in the ARes.
    """
    cryptogram: str
    """
    The cryptogram, also known as the "authentication value" (AAV, CAVV or
    AEVV). This value is 20 bytes, base64-encoded into a 28-character string.
    (Most 3D Secure providers will return the base64-encoded version, which
    is what you should specify here.)
    """
    electronic_commerce_indicator: NotRequired[
        Literal["01", "02", "05", "06", "07"]
    ]
    """
    The Electronic Commerce Indicator (ECI) is returned by your 3D Secure
    provider and indicates what degree of authentication was performed.
    """
    exemption_indicator: NotRequired[Literal["low_risk", "none"]]
    """
    The exemption requested via 3DS and accepted by the issuer at authentication time.
    """
    network_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions"
    ]
    """
    Network specific 3DS fields. Network specific arguments require an
    explicit card brand choice. The parameter `payment_method_options.card.network``
    must be populated accordingly
    """
    requestor_challenge_indicator: NotRequired[str]
    """
    The challenge indicator (`threeDSRequestorChallengeInd`) which was requested in the
    AReq sent to the card Issuer's ACS. A string containing 2 digits from 01-99.
    """
    transaction_id: str
    """
    For 3D Secure 1, the XID. For 3D Secure 2, the Directory Server
    Transaction ID (dsTransID).
    """
    version: Literal["1.0.2", "2.1.0", "2.2.0"]
    """
    The version of 3D Secure that was performed.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    TypedDict,
):
    cartes_bancaires: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires"
    ]
    """
    Cartes Bancaires-specific 3DS fields.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires(
    TypedDict,
):
    cb_avalgo: Literal["0", "1", "2", "3", "4", "A"]
    """
    The cryptogram calculation algorithm used by the card Issuer's ACS
    to calculate the Authentication cryptogram. Also known as `cavvAlgorithm`.
    messageExtension: CB-AVALGO
    """
    cb_exemption: NotRequired[str]
    """
    The exemption indicator returned from Cartes Bancaires in the ARes.
    message extension: CB-EXEMPTION; string (4 characters)
    This is a 3 byte bitmap (low significant byte first and most significant
    bit first) that has been Base64 encoded
    """
    cb_score: NotRequired[int]
    """
    The risk score returned from Cartes Bancaires in the ARes.
    message extension: CB-SCORE; numeric value 0-99
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardPresent(TypedDict):
    capture_method: NotRequired[Literal["manual", "manual_preferred"]]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    request_extended_authorization: NotRequired[bool]
    """
    Request ability to capture this payment beyond the standard [authorization validity window](https://docs.stripe.com/terminal/features/extended-authorizations#authorization-validity)
    """
    request_incremental_authorization_support: NotRequired[bool]
    """
    Request ability to [increment](https://docs.stripe.com/terminal/features/incremental-authorizations) this PaymentIntent if the combination of MCC and card brand is eligible. Check [incremental_authorization_supported](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-incremental_authorization_supported) in the [Confirm](https://docs.stripe.com/api/payment_intents/confirm) response to verify support.
    """
    routing: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCardPresentRouting"
    ]
    """
    Network routing priority on co-branded EMV cards supporting domestic debit and international card schemes.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCardPresentRouting(
    TypedDict,
):
    requested_priority: NotRequired[Literal["domestic", "international"]]
    """
    Routing requested priority
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCashapp(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCrypto(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalance(TypedDict):
    bank_transfer: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
    ]
    """
    Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
    """
    funding_type: NotRequired[Literal["bank_transfer"]]
    """
    The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
    ]
    """
    Configuration for the eu_bank_transfer funding type.
    """
    requested_address_types: NotRequired[
        List[
            Literal[
                "aba", "iban", "sepa", "sort_code", "spei", "swift", "zengin"
            ]
        ]
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


class PaymentIntentCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: str
    """
    The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsEps(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsFpx(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsGiropay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsGopay(TypedDict):
    setup_future_usage: NotRequired[Literal["none", "off_session"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsGrabpay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsIdBankTransfer(TypedDict):
    expires_after: NotRequired[int]
    """
    The UNIX timestamp until which the virtual bank account is valid. Permitted range is from 5 minutes from now until 31 days from now. If unset, it defaults to 3 days from now.
    """
    expires_at: NotRequired[int]
    """
    The UNIX timestamp until which the virtual bank account is valid. Permitted range is from now until 30 days from now. If unset, it defaults to 1 days from now.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsIdeal(TypedDict):
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsInteracPresent(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodOptionsKakaoPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarna(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    on_demand: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaOnDemand"
    ]
    """
    On-demand details if setting up or charging an on-demand payment.
    """
    preferred_locale: NotRequired[
        Literal[
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-CH",
            "de-DE",
            "el-GR",
            "en-AT",
            "en-AU",
            "en-BE",
            "en-CA",
            "en-CH",
            "en-CZ",
            "en-DE",
            "en-DK",
            "en-ES",
            "en-FI",
            "en-FR",
            "en-GB",
            "en-GR",
            "en-IE",
            "en-IT",
            "en-NL",
            "en-NO",
            "en-NZ",
            "en-PL",
            "en-PT",
            "en-RO",
            "en-SE",
            "en-US",
            "es-ES",
            "es-US",
            "fi-FI",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "it-CH",
            "it-IT",
            "nb-NO",
            "nl-BE",
            "nl-NL",
            "pl-PL",
            "pt-PT",
            "ro-RO",
            "sv-FI",
            "sv-SE",
        ]
    ]
    """
    Preferred language of the Klarna authorization page that the customer is redirected to
    """
    setup_future_usage: NotRequired[
        Literal["none", "off_session", "on_session"]
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    subscriptions: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSubscription]"
    ]
    """
    Subscription details if setting up or charging a subscription.
    """
    supplementary_purchase_data: NotRequired[
        "Literal['']|PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseData"
    ]
    """
    Supplementary Purchase Data for the corresponding Klarna payment
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaOnDemand(TypedDict):
    average_amount: NotRequired[int]
    """
    Your average amount value. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    maximum_amount: NotRequired[int]
    """
    The maximum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    minimum_amount: NotRequired[int]
    """
    The lowest or minimum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    purchase_interval: NotRequired[Literal["day", "month", "week", "year"]]
    """
    Interval at which the customer is making purchases
    """
    purchase_interval_count: NotRequired[int]
    """
    The number of `purchase_interval` between charges
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSubscription(
    TypedDict,
):
    interval: Literal["day", "month", "week", "year"]
    """
    Unit of time between subscription charges.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals (specified in the `interval` attribute) between subscription charges. For example, `interval=month` and `interval_count=3` charges every 3 months.
    """
    name: NotRequired[str]
    """
    Name for subscription.
    """
    next_billing: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling"
    ]
    """
    Describes the upcoming charge for this subscription.
    """
    reference: str
    """
    A non-customer-facing reference to correlate subscription charges in the Klarna app. Use a value that persists across subscription charges.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling(
    TypedDict,
):
    amount: int
    """
    The amount of the next charge for the subscription.
    """
    date: str
    """
    The date of the next charge for the subscription in YYYY-MM-DD format.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseData(
    TypedDict,
):
    bus_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetail]"
    ]
    """
    Supplementary bus reservation details.
    """
    event_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetail]"
    ]
    """
    Supplementary event reservation details.
    """
    ferry_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetail]"
    ]
    """
    Supplementary ferry reservation details.
    """
    insurances: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataInsurance]"
    ]
    """
    Supplementary insurance details.
    """
    marketplace_sellers: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSeller]"
    ]
    """
    Supplementary marketplace seller details.
    """
    round_trip_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetail]"
    ]
    """
    Supplementary round trip reservation details.
    """
    train_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetail]"
    ]
    """
    Supplementary train reservation details.
    """
    vouchers: NotRequired[
        "Literal['']|List[PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataVoucher]"
    ]
    """
    Voucher details, such as a gift card or discount code.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrival"
    ]
    """
    Arrival details.
    """
    carrier_name: NotRequired[str]
    """
    Name of transportation company.
    """
    currency: NotRequired[str]
    """
    Currency.
    """
    departure: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailPassenger"
        ]
    ]
    """
    List of passengers that this reservation applies to.
    """
    price: NotRequired[int]
    """
    Price in cents.
    """
    ticket_class: NotRequired[
        Literal["business", "economy", "first_class", "premium_economy"]
    ]
    """
    Ticket class.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrivalAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDepartureAddress"
    ]
    """
    Address of the departure location.
    """
    departs_at: NotRequired[int]
    """
    Timestamp of departure.
    """
    departure_location: NotRequired[str]
    """
    Identifier name or reference for the origin location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDepartureAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["baggage", "bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance.
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailPassenger(
    TypedDict,
):
    family_name: NotRequired[str]
    """
    The family name of the person.
    """
    given_name: NotRequired[str]
    """
    The given name of the person.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetail(
    TypedDict,
):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailAddress"
    ]
    """
    Address of the event.
    """
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    ends_at: NotRequired[int]
    """
    End timestamp of the event.
    """
    event_company_name: NotRequired[str]
    """
    Company selling the ticket.
    """
    event_name: NotRequired[str]
    """
    Name of the event.
    """
    event_type: NotRequired[
        Literal[
            "concert",
            "conference",
            "digital_education",
            "expo",
            "festival",
            "in_person_education",
            "sport",
            "tour",
        ]
    ]
    """
    Type of the event.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this event.
    """
    starts_at: NotRequired[int]
    """
    Start timestamp of the event.
    """
    venue_name: NotRequired[str]
    """
    Name of the venue where the event takes place.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance.
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrival"
    ]
    """
    Arrival details.
    """
    carrier_name: NotRequired[str]
    """
    Name of transportation company.
    """
    currency: NotRequired[str]
    """
    Currency.
    """
    departure: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailPassenger"
        ]
    ]
    """
    List of passengers that this reservation applies to.
    """
    price: NotRequired[int]
    """
    Price in cents.
    """
    ticket_class: NotRequired[
        Literal["business", "economy", "first_class", "premium_economy"]
    ]
    """
    Ticket class.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrivalAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDepartureAddress"
    ]
    """
    Address of the departure location.
    """
    departs_at: NotRequired[int]
    """
    Timestamp of departure.
    """
    departure_location: NotRequired[str]
    """
    Identifier name or reference for the origin location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDepartureAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["baggage", "bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance.
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailPassenger(
    TypedDict,
):
    family_name: NotRequired[str]
    """
    The family name of the person.
    """
    given_name: NotRequired[str]
    """
    The given name of the person.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSeller(
    TypedDict,
):
    line_item_references: NotRequired[List[str]]
    """
    The references to line items for purchases with multiple associated sub-sellers.
    """
    marketplace_seller_address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSellerMarketplaceSellerAddress"
    ]
    """
    The address of the selling or delivering merchant.
    """
    marketplace_seller_name: NotRequired[str]
    """
    The name of the marketplace seller.
    """
    marketplace_seller_reference: NotRequired[str]
    """
    The unique identifier for the marketplace seller.
    """
    number_of_transactions: NotRequired[int]
    """
    The number of transactions the sub-seller completed in the last 12 months.
    """
    product_category: NotRequired[
        Literal[
            "accessories",
            "appliances",
            "apps_and_games",
            "arts_crafts_and_sewing",
            "automotive",
            "baby",
            "baby_clothing",
            "bags_and_purses",
            "beauty",
            "books",
            "cds_and_vinyl",
            "cell_phones_and_accessories",
            "collectibles_and_fine_arts",
            "digital_music",
            "electronics",
            "grocery_and_gourmet_food",
            "handmade",
            "health_and_personal_care",
            "home_and_kitchen",
            "industrial_and_scientific",
            "luggage_and_travel_gear",
            "magazine_subscriptions",
            "men_clothing",
            "musical_instruments",
            "office_products",
            "patio_lawn_and_garden",
            "pet_supplies",
            "shoes",
            "software",
            "sports_and_outdoors",
            "tools_and_home_improvement",
            "toys_and_games",
            "video_games",
            "women_clothing",
        ]
    ]
    """
    The category of the product.
    """
    seller_last_login_at: NotRequired[int]
    """
    The date when the seller's account with the marketplace was last logged in.
    """
    seller_rating: NotRequired[
        Literal["high", "low", "medium", "very_high", "very_low"]
    ]
    """
    The current rating of the marketplace seller. If the marketplace uses numeric ranking, map these to the enum values.
    """
    seller_registered_at: NotRequired[int]
    """
    The date when the seller's account with the marketplace was created.
    """
    seller_updated_at: NotRequired[int]
    """
    The date when the seller's account with the marketplace was last updated.
    """
    shipping_references: NotRequired[List[str]]
    """
    The references to shipping addresses for purchases with multiple associated sub-sellers.
    """
    volume_of_transactions: NotRequired[int]
    """
    The accumulated amount of sales transactions made by the sub-merchant or sub-seller within the past 12 months in the payment currency. These transactions are in minor currency units.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSellerMarketplaceSellerAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrival"
    ]
    """
    Arrival details.
    """
    carrier_name: NotRequired[str]
    """
    Name of transportation company.
    """
    currency: NotRequired[str]
    """
    Currency.
    """
    departure: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailPassenger"
        ]
    ]
    """
    List of passengers that this reservation applies to.
    """
    price: NotRequired[int]
    """
    Price in cents.
    """
    ticket_class: NotRequired[
        Literal["business", "economy", "first_class", "premium_economy"]
    ]
    """
    Ticket class.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrivalAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDepartureAddress"
    ]
    """
    Address of the departure location.
    """
    departs_at: NotRequired[int]
    """
    Timestamp of departure.
    """
    departure_location: NotRequired[str]
    """
    Identifier name or reference for the origin location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDepartureAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["baggage", "bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance.
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailPassenger(
    TypedDict,
):
    family_name: NotRequired[str]
    """
    The family name of the person.
    """
    given_name: NotRequired[str]
    """
    The given name of the person.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrival"
    ]
    """
    Arrival details.
    """
    carrier_name: NotRequired[str]
    """
    Name of transportation company.
    """
    currency: NotRequired[str]
    """
    Currency.
    """
    departure: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailPassenger"
        ]
    ]
    """
    List of passengers that this reservation applies to.
    """
    price: NotRequired[int]
    """
    Price in cents.
    """
    ticket_class: NotRequired[
        Literal["business", "economy", "first_class", "premium_economy"]
    ]
    """
    Ticket class.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrivalAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDepartureAddress"
    ]
    """
    Address of the departure location.
    """
    departs_at: NotRequired[int]
    """
    Timestamp of departure.
    """
    departure_location: NotRequired[str]
    """
    Identifier name or reference for the origin location.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDepartureAddress(
    TypedDict,
):
    city: NotRequired[str]
    """
    The city or town.
    """
    country: NotRequired[str]
    """
    The country in ISO 3166-1 alpha-2 format.
    """
    postal_code: NotRequired[str]
    """
    The postal code formatted according to country.
    """
    region: NotRequired[str]
    """
    The state, county, province, or region formatted according to country.
    """
    street_address: NotRequired[str]
    """
    Line 1 of the street address.
    """
    street_address2: NotRequired[str]
    """
    Line 2 of the street address.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailInsurance(
    TypedDict,
):
    currency: NotRequired[str]
    """
    Insurance currency.
    """
    insurance_company_name: NotRequired[str]
    """
    Name of the company providing the insurance.
    """
    insurance_type: NotRequired[
        Literal["baggage", "bankruptcy", "cancelation", "emergency", "medical"]
    ]
    """
    Type of insurance.
    """
    price: NotRequired[int]
    """
    Price of insurance in cents.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailPassenger(
    TypedDict,
):
    family_name: NotRequired[str]
    """
    The family name of the person.
    """
    given_name: NotRequired[str]
    """
    The given name of the person.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataVoucher(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for this voucher.
    """
    ends_at: NotRequired[int]
    """
    The voucher validity end time.
    """
    starts_at: NotRequired[int]
    """
    The voucher validity start time.
    """
    voucher_company: NotRequired[str]
    """
    The issuer or provider of this voucher.
    """
    voucher_name: NotRequired[str]
    """
    The name or reference to identify the voucher.
    """
    voucher_type: NotRequired[
        Literal[
            "digital_product",
            "discount",
            "gift_card",
            "physical_product",
            "services",
        ]
    ]
    """
    The type of this voucher.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKonbini(TypedDict):
    confirmation_number: NotRequired["Literal['']|str"]
    """
    An optional 10 to 11 digit numeric-only string determining the confirmation code at applicable convenience stores. Must not consist of only zeroes and could be rejected in case of insufficient uniqueness. We recommend to use the customer's phone number.
    """
    expires_after_days: NotRequired["Literal['']|int"]
    """
    The number of calendar days (between 1 and 60) after which Konbini payment instructions will expire. For example, if a PaymentIntent is confirmed with Konbini and `expires_after_days` set to 2 on Monday JST, the instructions will expire on Wednesday 23:59:59 JST. Defaults to 3 days.
    """
    expires_at: NotRequired["Literal['']|int"]
    """
    The timestamp at which the Konbini payment instructions will expire. Only one of `expires_after_days` or `expires_at` may be set.
    """
    product_description: NotRequired["Literal['']|str"]
    """
    A product descriptor of up to 22 characters, which will appear to customers at the convenience store.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsKrCard(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsLink(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    persistent_token: NotRequired[str]
    """
    [Deprecated] This is a legacy parameter that no longer has any function.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsMbWay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsMobilepay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsMultibanco(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsNaverPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsNzBankAccount(TypedDict):
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsOxxo(TypedDict):
    expires_after_days: NotRequired[int]
    """
    The number of calendar days before an OXXO voucher expires. For example, if you create an OXXO voucher on Monday and you set expires_after_days to 2, the OXXO invoice will expire on Wednesday at 23:59 America/Mexico_City time.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsP24(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    tos_shown_and_accepted: NotRequired[bool]
    """
    Confirm that the payer has accepted the P24 terms and conditions.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPayByBank(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodOptionsPayco(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaynow(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaypal(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds will be captured from the customer's account.
    """
    line_items: NotRequired[
        List["PaymentIntentCreateParamsPaymentMethodOptionsPaypalLineItem"]
    ]
    """
    The line items purchased by the customer.
    """
    preferred_locale: NotRequired[
        Literal[
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-DE",
            "de-LU",
            "el-GR",
            "en-GB",
            "en-US",
            "es-ES",
            "fi-FI",
            "fr-BE",
            "fr-FR",
            "fr-LU",
            "hu-HU",
            "it-IT",
            "nl-BE",
            "nl-NL",
            "pl-PL",
            "pt-PT",
            "sk-SK",
            "sv-SE",
        ]
    ]
    """
    [Preferred locale](https://docs.stripe.com/payments/paypal/supported-locales) of the PayPal checkout page that the customer is redirected to.
    """
    reference: NotRequired[str]
    """
    A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
    """
    reference_id: NotRequired[str]
    """
    A reference of the PayPal transaction visible to customer which is mapped to PayPal's invoice ID. This must be a globally unique ID if you have configured in your PayPal settings to block multiple payments per invoice ID.
    """
    risk_correlation_id: NotRequired[str]
    """
    The risk correlation ID for an on-session payment using a saved PayPal payment method.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    subsellers: NotRequired[List[str]]
    """
    The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaypalLineItem(TypedDict):
    category: NotRequired[
        Literal["digital_goods", "donation", "physical_goods"]
    ]
    """
    Type of the line item.
    """
    description: NotRequired[str]
    """
    Description of the line item.
    """
    name: str
    """
    Descriptive name of the line item.
    """
    quantity: int
    """
    Quantity of the line item. Must be a positive number.
    """
    sku: NotRequired[str]
    """
    Client facing stock keeping unit, article number or similar.
    """
    sold_by: NotRequired[str]
    """
    The Stripe account ID of the connected account that sells the item.
    """
    tax: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsPaypalLineItemTax"
    ]
    """
    The tax information for the line item.
    """
    unit_amount: int
    """
    Price for a single unit of the line item in minor units. Cannot be a negative number.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaypalLineItemTax(
    TypedDict
):
    amount: int
    """
    The tax for a single unit of the line item in minor units. Cannot be a negative number.
    """
    behavior: Literal["exclusive", "inclusive"]
    """
    The tax behavior for the line item.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaypay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPayto(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsPaytoMandateOptions"
    ]
    """
    Additional fields for Mandate creation. Only `purpose` field is configurable for PayTo PaymentIntent with `setup_future_usage=none`. Other fields are only applicable to PayTo PaymentIntent with `setup_future_usage=off_session`
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPaytoMandateOptions(
    TypedDict,
):
    amount: NotRequired["Literal['']|int"]
    """
    Amount that will be collected. It is required when `amount_type` is `fixed`.
    """
    amount_type: NotRequired["Literal['']|Literal['fixed', 'maximum']"]
    """
    The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively. Defaults to `maximum`.
    """
    end_date: NotRequired["Literal['']|str"]
    """
    Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.
    """
    payment_schedule: NotRequired[
        "Literal['']|Literal['adhoc', 'annual', 'daily', 'fortnightly', 'monthly', 'quarterly', 'semi_annual', 'weekly']"
    ]
    """
    The periodicity at which payments will be collected. Defaults to `adhoc`.
    """
    payments_per_period: NotRequired["Literal['']|int"]
    """
    The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.
    """
    purpose: NotRequired[
        "Literal['']|Literal['dependant_support', 'government', 'loan', 'mortgage', 'other', 'pension', 'personal', 'retail', 'salary', 'tax', 'utility']"
    ]
    """
    The purpose for which payments are made. Has a default value based on your merchant category code.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPix(TypedDict):
    amount_includes_iof: NotRequired[Literal["always", "never"]]
    """
    Determines if the amount includes the IOF tax. Defaults to `never`.
    """
    expires_after_seconds: NotRequired[int]
    """
    The number of seconds (between 10 and 1209600) after which Pix payment will expire. Defaults to 86400 seconds.
    """
    expires_at: NotRequired[int]
    """
    The timestamp at which the Pix expires (between 10 and 1209600 seconds in the future). Defaults to 1 day in the future.
    """
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsPixMandateOptions"
    ]
    """
    Additional fields for mandate creation. Only applicable when `setup_future_usage=off_session`.
    """
    setup_future_usage: NotRequired[Literal["none", "off_session"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPixMandateOptions(
    TypedDict
):
    amount: NotRequired[int]
    """
    Amount to be charged for future payments. Required when `amount_type=fixed`. If not provided for `amount_type=maximum`, defaults to 40000.
    """
    amount_includes_iof: NotRequired[Literal["always", "never"]]
    """
    Determines if the amount includes the IOF tax. Defaults to `never`.
    """
    amount_type: NotRequired[Literal["fixed", "maximum"]]
    """
    Type of amount. Defaults to `maximum`.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Only `brl` is supported currently.
    """
    end_date: NotRequired[str]
    """
    Date when the mandate expires and no further payments will be charged, in `YYYY-MM-DD`. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
    """
    payment_schedule: NotRequired[
        Literal["halfyearly", "monthly", "quarterly", "weekly", "yearly"]
    ]
    """
    Schedule at which the future payments will be charged. Defaults to `weekly`.
    """
    reference: NotRequired[str]
    """
    Subscription name displayed to buyers in their bank app. Defaults to the displayable business name.
    """
    start_date: NotRequired[str]
    """
    Start date of the mandate, in `YYYY-MM-DD`. Start date should be at least 3 days in the future. Defaults to 3 days after the current date.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsPromptpay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsQris(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsRechnung(TypedDict):
    pass


class PaymentIntentCreateParamsPaymentMethodOptionsRevolutPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSamsungPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSatispay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsSepaDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSepaDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'STRIPE'.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsShopeepay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSofort(TypedDict):
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

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsStripeBalance(TypedDict):
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsSwish(TypedDict):
    reference: NotRequired["Literal['']|str"]
    """
    A reference for this payment to be displayed in the Swish app.
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsTwint(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
    financial_connections: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
    ]
    """
    Additional fields for Financial Connections Session creation
    """
    mandate_options: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    networks: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountNetworks"
    ]
    """
    Additional fields for network related functions
    """
    preferred_settlement_speed: NotRequired[
        "Literal['']|Literal['fastest', 'standard']"
    ]
    """
    Preferred transaction settlement speed
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['none', 'off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    target_date: NotRequired[str]
    """
    Controls when Stripe will attempt to debit the funds from the customer's account. The date must be a string in YYYY-MM-DD format. The date must be in the future and between 3 and 15 calendar days from now.
    """
    verification_method: NotRequired[
        Literal["automatic", "instant", "microdeposits"]
    ]
    """
    Bank account verification method.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    manual_entry: NotRequired[
        "PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry"
    ]
    """
    Customize manual entry behavior
    """
    permissions: NotRequired[
        List[
            Literal["balances", "ownership", "payment_method", "transactions"]
        ]
    ]
    """
    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
    """
    prefetch: NotRequired[
        List[
            Literal[
                "balances", "inferred_balances", "ownership", "transactions"
            ]
        ]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """
    return_url: NotRequired[str]
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[List[Literal["checking", "savings"]]]
    """
    The account subcategories to use to filter for selectable accounts. Valid subcategories are `checking` and `savings`.
    """
    institution: NotRequired[str]
    """
    ID of the institution to use to filter for selectable accounts.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
    TypedDict,
):
    mode: Literal["automatic", "custom"]
    """
    Settings for configuring manual entry of account details.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountMandateOptions(
    TypedDict,
):
    collection_method: NotRequired["Literal['']|Literal['paper']"]
    """
    The method used to collect offline mandate customer acceptance.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsUsBankAccountNetworks(
    TypedDict,
):
    requested: NotRequired[List[Literal["ach", "us_domestic_wire"]]]
    """
    Triggers validations to run across the selected networks
    """


class PaymentIntentCreateParamsPaymentMethodOptionsWechatPay(TypedDict):
    app_id: NotRequired[str]
    """
    The app ID registered with WeChat Pay. Only required when client is ios or android.
    """
    client: NotRequired[Literal["android", "ios", "web"]]
    """
    The client type that the end customer will pay from
    """
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentMethodOptionsZip(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentCreateParamsPaymentsOrchestration(TypedDict):
    enabled: bool
    """
    Whether this feature is enabled.
    """


class PaymentIntentCreateParamsRadarOptions(TypedDict):
    session: NotRequired[str]
    """
    A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
    """


class PaymentIntentCreateParamsShipping(TypedDict):
    address: "PaymentIntentCreateParamsShippingAddress"
    """
    Shipping address.
    """
    carrier: NotRequired[str]
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
    """
    name: str
    """
    Recipient name.
    """
    phone: NotRequired[str]
    """
    Recipient phone (including extension).
    """
    tracking_number: NotRequired[str]
    """
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
    """


class PaymentIntentCreateParamsShippingAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
    """


class PaymentIntentCreateParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    The amount is capped at the total transaction amount and if no amount is set,
    the full amount is transferred.

    If you intend to collect a fee and you need a more robust reporting experience, using
    [application_fee_amount](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-application_fee_amount)
    might be a better fit for your integration.
    """
    destination: str
    """
    If specified, successful charges will be attributed to the destination
    account for tax reporting, and the funds from charges will be transferred
    to the destination account. The ID of the resulting transfer will be
    returned on the successful charge's `transfer` field.
    """
