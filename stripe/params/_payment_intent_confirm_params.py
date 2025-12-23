# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentConfirmParams(RequestOptions):
    allocated_funds: NotRequired["PaymentIntentConfirmParamsAllocatedFunds"]
    """
    Allocated Funds configuration for this PaymentIntent.
    """
    amount_details: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsAmountDetails"
    ]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired["Literal['']|int"]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    capture_method: NotRequired[
        Literal["automatic", "automatic_async", "manual"]
    ]
    """
    Controls when the funds will be captured from the customer's account.
    """
    confirmation_token: NotRequired[str]
    """
    ID of the ConfirmationToken used to confirm this PaymentIntent.

    If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    """
    error_on_requires_action: NotRequired[bool]
    """
    Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://docs.stripe.com/payments/save-card-without-authentication).
    """
    excluded_payment_method_types: NotRequired[
        "Literal['']|List[Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'alma', 'amazon_pay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'billie', 'blik', 'boleto', 'card', 'cashapp', 'crypto', 'customer_balance', 'eps', 'fpx', 'giropay', 'gopay', 'grabpay', 'id_bank_transfer', 'ideal', 'kakao_pay', 'klarna', 'konbini', 'kr_card', 'mb_way', 'mobilepay', 'multibanco', 'naver_pay', 'nz_bank_account', 'oxxo', 'p24', 'pay_by_bank', 'payco', 'paynow', 'paypal', 'paypay', 'payto', 'pix', 'promptpay', 'qris', 'rechnung', 'revolut_pay', 'samsung_pay', 'satispay', 'sepa_debit', 'shopeepay', 'sofort', 'stripe_balance', 'swish', 'twint', 'us_bank_account', 'wechat_pay', 'zip']]"
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
    hooks: NotRequired["PaymentIntentConfirmParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    mandate: NotRequired[str]
    """
    ID of the mandate that's used for this payment.
    """
    mandate_data: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsMandateData"
    ]
    off_session: NotRequired["bool|Literal['one_off', 'recurring']"]
    """
    Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://docs.stripe.com/payments/cards/charging-saved-cards).
    """
    payment_details: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the charge.
    """
    payment_method: NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://docs.stripe.com/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.
    If the payment method is attached to a Customer, it must match the [customer](https://api.stripe.com#create_payment_intent-customer) that is set on this PaymentIntent.
    """
    payment_method_data: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodData"
    ]
    """
    If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
    in the [payment_method](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-payment_method)
    property on the PaymentIntent.
    """
    payment_method_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptions"
    ]
    """
    Payment method-specific configuration for this PaymentIntent.
    """
    payment_method_types: NotRequired[List[str]]
    """
    The list of payment method types (for example, a card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
    """
    radar_options: NotRequired["PaymentIntentConfirmParamsRadarOptions"]
    """
    Options to configure Radar. Learn more about [Radar Sessions](https://docs.stripe.com/radar/radar-session).
    """
    receipt_email: NotRequired["Literal['']|str"]
    """
    Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    """
    return_url: NotRequired[str]
    """
    The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.
    If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
    This parameter is only used for cards and other redirect-based payment methods.
    """
    setup_future_usage: NotRequired[
        "Literal['']|Literal['off_session', 'on_session']"
    ]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """
    shipping: NotRequired["Literal['']|PaymentIntentConfirmParamsShipping"]
    """
    Shipping information for this PaymentIntent.
    """
    use_stripe_sdk: NotRequired[bool]
    """
    Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
    """
    shared_payment_granted_token: NotRequired[str]
    """
    ID of the SharedPaymentToken used to confirm this PaymentIntent.
    """


class PaymentIntentConfirmParamsAllocatedFunds(TypedDict):
    enabled: NotRequired[bool]
    """
    Whether Allocated Funds creation is enabled for this PaymentIntent.
    """


class PaymentIntentConfirmParamsAmountDetails(TypedDict):
    discount_amount: NotRequired["Literal['']|int"]
    """
    The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[line_items][#][discount_amount]` field.
    """
    line_items: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 100 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired["Literal['']|PaymentIntentConfirmParamsAmountDetailsTax"]
    """
    Contains information about the tax portion of the amount.
    """


class PaymentIntentConfirmParamsAmountDetailsLineItem(TypedDict):
    discount_amount: NotRequired[int]
    """
    The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]` field.
    """
    payment_method_options: NotRequired[
        "PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptions"
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
    tax: NotRequired["PaymentIntentConfirmParamsAmountDetailsLineItemTax"]
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


class PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to `card` payment method."
    """
    card_present: NotRequired[
        "PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to `card_present` payment method."
    """
    klarna: NotRequired[
        "PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to `klarna` payment method."
    """
    paypal: NotRequired[
        "PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to `paypal` payment method."
    """


class PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, etc.
    """


class PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
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


class PaymentIntentConfirmParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
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


class PaymentIntentConfirmParamsAmountDetailsLineItemTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.
    """


class PaymentIntentConfirmParamsAmountDetailsShipping(TypedDict):
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


class PaymentIntentConfirmParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class PaymentIntentConfirmParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentConfirmParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentConfirmParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentConfirmParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentConfirmParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id
    """


class PaymentIntentConfirmParamsMandateData(TypedDict):
    customer_acceptance: NotRequired[
        "PaymentIntentConfirmParamsMandateDataCustomerAcceptance"
    ]
    """
    This hash contains details about the customer acceptance of the Mandate.
    """


class PaymentIntentConfirmParamsMandateDataCustomerAcceptance(TypedDict):
    accepted_at: NotRequired[int]
    """
    The time at which the customer accepted the Mandate.
    """
    offline: NotRequired[
        "PaymentIntentConfirmParamsMandateDataCustomerAcceptanceOffline"
    ]
    """
    If this is a Mandate accepted offline, this hash contains details about the offline acceptance.
    """
    online: NotRequired[
        "PaymentIntentConfirmParamsMandateDataCustomerAcceptanceOnline"
    ]
    """
    If this is a Mandate accepted online, this hash contains details about the online acceptance.
    """
    type: Literal["offline", "online"]
    """
    The type of customer acceptance information included with the Mandate. One of `online` or `offline`.
    """


class PaymentIntentConfirmParamsMandateDataCustomerAcceptanceOffline(
    TypedDict
):
    pass


class PaymentIntentConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
    ip_address: NotRequired[str]
    """
    The IP address from which the Mandate was accepted by the customer.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Mandate was accepted by the customer.
    """


class PaymentIntentConfirmParamsPaymentDetails(TypedDict):
    benefit: NotRequired["PaymentIntentConfirmParamsPaymentDetailsBenefit"]
    """
    Benefit details for this PaymentIntent
    """
    car_rental: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRental"
    ]
    """
    Car rental details for this PaymentIntent.
    """
    car_rental_data: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentDetailsCarRentalDatum]"
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
        "PaymentIntentConfirmParamsPaymentDetailsEventDetails"
    ]
    """
    Event details for this PaymentIntent
    """
    flight: NotRequired["PaymentIntentConfirmParamsPaymentDetailsFlight"]
    """
    Flight reservation details for this PaymentIntent
    """
    flight_data: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentDetailsFlightDatum]"
    ]
    """
    Flight data for this PaymentIntent.
    """
    lodging: NotRequired["PaymentIntentConfirmParamsPaymentDetailsLodging"]
    """
    Lodging reservation details for this PaymentIntent
    """
    lodging_data: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentDetailsLodgingDatum]"
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
        "PaymentIntentConfirmParamsPaymentDetailsSubscription"
    ]
    """
    Subscription details for this PaymentIntent
    """


class PaymentIntentConfirmParamsPaymentDetailsBenefit(TypedDict):
    fr_meal_voucher: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentDetailsBenefitFrMealVoucher"
    ]
    """
    French meal voucher benefit details for this PaymentIntent.
    """


class PaymentIntentConfirmParamsPaymentDetailsBenefitFrMealVoucher(TypedDict):
    siret: str
    """
    The 14-digit SIRET of the meal voucher acceptor.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRental(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalAffiliate"
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
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    distance: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDistance"
    ]
    """
    The details of the distance traveled during the rental period.
    """
    drivers: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsCarRentalDriver"]
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
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalPickupAddress"
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
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalReturnAddress"
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDeliveryRecipient(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDistance(TypedDict):
    amount: NotRequired[int]
    """
    Distance traveled.
    """
    unit: NotRequired[Literal["kilometers", "miles"]]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDriver(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalPickupAddress(
    TypedDict
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalReturnAddress(
    TypedDict
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatum(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumAffiliate"
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
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDistance"
    ]
    """
    Distance details for the rental.
    """
    drivers: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDriver"]
    ]
    """
    List of drivers for the rental.
    """
    drop_off: "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDropOff"
    """
    Drop-off location details.
    """
    insurances: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumInsurance"]
    ]
    """
    Insurance details for the rental.
    """
    no_show_indicator: NotRequired[bool]
    """
    Indicates if the customer was a no-show.
    """
    pickup: "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumPickup"
    """
    Pickup location details.
    """
    renter_name: NotRequired[str]
    """
    Name of the person renting the vehicle.
    """
    total: "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotal"
    """
    Total cost breakdown for the rental.
    """
    vehicle: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumVehicle"
    ]
    """
    Vehicle details for the rental.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumAffiliate(
    TypedDict,
):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Name of affiliate partner.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDistance(
    TypedDict
):
    amount: int
    """
    Distance traveled.
    """
    unit: Literal["kilometers", "miles"]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDriver(TypedDict):
    date_of_birth: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDriverDateOfBirth"
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDriverDateOfBirth(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDropOff(TypedDict):
    address: (
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDropOffAddress"
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumDropOffAddress(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumInsurance(
    TypedDict,
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumPickup(TypedDict):
    address: (
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumPickupAddress"
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumPickupAddress(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotal(TypedDict):
    amount: int
    """
    Total amount in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the amount.
    """
    discounts: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalDiscounts"
    ]
    """
    Discount details for the rental.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalExtraCharge"
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
        "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalTax"
    ]
    """
    Tax breakdown for the rental.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalDiscounts(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalExtraCharge(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalTax(
    TypedDict
):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates if the transaction is tax exempt.
    """
    taxes: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalTaxTax"
        ]
    ]
    """
    Array of tax details.
    """


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumTotalTaxTax(
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


class PaymentIntentConfirmParamsPaymentDetailsCarRentalDatumVehicle(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsEventDetails(TypedDict):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsEventDetailsAddress"
    ]
    """
    The event location's address.
    """
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsEventDetailsAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    company: NotRequired[str]
    """
    The name of the company
    """
    delivery: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsEventDetailsDelivery"
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


class PaymentIntentConfirmParamsPaymentDetailsEventDetailsAddress(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentConfirmParamsPaymentDetailsEventDetailsDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsEventDetailsDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentConfirmParamsPaymentDetailsEventDetailsDeliveryRecipient(
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


class PaymentIntentConfirmParamsPaymentDetailsFlight(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsFlightAffiliate"
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
        "PaymentIntentConfirmParamsPaymentDetailsFlightDelivery"
    ]
    """
    Delivery details for this purchase.
    """
    passenger_name: NotRequired[str]
    """
    The name of the person or entity on the reservation.
    """
    passengers: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsFlightPassenger"]
    ]
    """
    The details of the passengers in the travel reservation.
    """
    segments: List["PaymentIntentConfirmParamsPaymentDetailsFlightSegment"]
    """
    The individual flight segments associated with the trip.
    """
    ticket_number: NotRequired[str]
    """
    The ticket number associated with the travel reservation.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsFlightDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDeliveryRecipient(
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


class PaymentIntentConfirmParamsPaymentDetailsFlightPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the flight reservation.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightSegment(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatum(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumAffiliate"
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
        List["PaymentIntentConfirmParamsPaymentDetailsFlightDatumInsurance"]
    ]
    """
    List of insurances.
    """
    passengers: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsFlightDatumPassenger"]
    ]
    """
    List of passengers.
    """
    segments: List[
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegment"
    ]
    """
    List of flight segments.
    """
    ticket_electronically_issued_indicator: NotRequired[bool]
    """
    Electronic ticket indicator.
    """
    total: "PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotal"
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumAffiliate(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumInsurance(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumPassenger(TypedDict):
    name: str
    """
    Passenger's full name.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegment(TypedDict):
    amount: NotRequired[int]
    """
    Segment fare amount.
    """
    arrival: (
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegmentArrival"
    )
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
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegmentDeparture"
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegmentArrival(
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumSegmentDeparture(
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotal(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalDiscounts"
    ]
    """
    Discount details.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalExtraCharge"
        ]
    ]
    """
    Additional charges.
    """
    tax: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalTax"
    ]
    """
    Tax breakdown.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalDiscounts(
    TypedDict,
):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalExtraCharge(
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


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalTax(TypedDict):
    taxes: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalTaxTax"]
    ]
    """
    Array of tax details.
    """


class PaymentIntentConfirmParamsPaymentDetailsFlightDatumTotalTaxTax(
    TypedDict
):
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


class PaymentIntentConfirmParamsPaymentDetailsLodging(TypedDict):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingAddress"
    ]
    """
    The lodging location's address.
    """
    adults: NotRequired[int]
    """
    The number of adults on the booking
    """
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingAffiliate"
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
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDelivery"
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
        List["PaymentIntentConfirmParamsPaymentDetailsLodgingPassenger"]
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingAddress(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDeliveryRecipient(
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the lodging reservation.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatum(TypedDict):
    accommodation: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumAccommodation"
    ]
    """
    Accommodation details for the lodging.
    """
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumAffiliate"
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
        List["PaymentIntentConfirmParamsPaymentDetailsLodgingDatumGuest"]
    ]
    """
    List of guests for the lodging.
    """
    host: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumHost"
    ]
    """
    Host details for the lodging.
    """
    insurances: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsLodgingDatumInsurance"]
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
    total: "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotal"
    """
    Total details for the lodging.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumAccommodation(
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Affiliate partner name.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumGuest(TypedDict):
    name: str
    """
    Guest's full name.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumHost(TypedDict):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumHostAddress"
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumHostAddress(
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumInsurance(TypedDict):
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotal(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalDiscounts"
    ]
    """
    Discount details for the lodging.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalExtraCharge"
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
        "PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalTax"
    ]
    """
    Tax breakdown for the lodging reservation.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalDiscounts(
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalExtraCharge(
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


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates whether the transaction is tax exempt.
    """
    taxes: NotRequired[
        List["PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalTaxTax"]
    ]
    """
    Tax details.
    """


class PaymentIntentConfirmParamsPaymentDetailsLodgingDatumTotalTaxTax(
    TypedDict,
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


class PaymentIntentConfirmParamsPaymentDetailsSubscription(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsSubscriptionAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    auto_renewal: NotRequired[bool]
    """
    Info whether the subscription will be auto renewed upon expiry.
    """
    billing_interval: NotRequired[
        "PaymentIntentConfirmParamsPaymentDetailsSubscriptionBillingInterval"
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


class PaymentIntentConfirmParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class PaymentIntentConfirmParamsPaymentDetailsSubscriptionBillingInterval(
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


class PaymentIntentConfirmParamsPaymentMethodData(TypedDict):
    acss_debit: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataAcssDebit"
    ]
    """
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
    """
    affirm: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataAffirm"]
    """
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
    """
    afterpay_clearpay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataAfterpayClearpay"
    ]
    """
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
    """
    alipay: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataAlipay"]
    """
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
    """
    allow_redisplay: NotRequired[Literal["always", "limited", "unspecified"]]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    """
    alma: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataAlma"]
    """
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.
    """
    amazon_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataAmazonPay"
    ]
    """
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.
    """
    au_becs_debit: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataAuBecsDebit"
    ]
    """
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    """
    bacs_debit: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataBacsDebit"
    ]
    """
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    """
    bancontact: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataBancontact"
    ]
    """
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
    """
    billie: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataBillie"]
    """
    If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.
    """
    billing_details: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataBillingDetails"
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """
    blik: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataBlik"]
    """
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
    """
    boleto: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataBoleto"]
    """
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    """
    cashapp: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataCashapp"]
    """
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
    """
    crypto: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataCrypto"]
    """
    If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.
    """
    customer_balance: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataCustomerBalance"
    ]
    """
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
    """
    eps: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataEps"]
    """
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
    """
    fpx: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataFpx"]
    """
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    """
    giropay: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataGiropay"]
    """
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
    """
    gopay: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataGopay"]
    """
    If this is a Gopay PaymentMethod, this hash contains details about the Gopay payment method.
    """
    grabpay: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataGrabpay"]
    """
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
    """
    id_bank_transfer: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataIdBankTransfer"
    ]
    """
    If this is an `IdBankTransfer` PaymentMethod, this hash contains details about the IdBankTransfer payment method.
    """
    ideal: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataIdeal"]
    """
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    """
    interac_present: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataInteracPresent"
    ]
    """
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
    """
    kakao_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataKakaoPay"
    ]
    """
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.
    """
    klarna: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataKlarna"]
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    """
    konbini: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataKonbini"]
    """
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
    """
    kr_card: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataKrCard"]
    """
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.
    """
    link: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataLink"]
    """
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    """
    mb_way: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataMbWay"]
    """
    If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    mobilepay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataMobilepay"
    ]
    """
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.
    """
    multibanco: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataMultibanco"
    ]
    """
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.
    """
    naver_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataNaverPay"
    ]
    """
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    """
    nz_bank_account: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataNzBankAccount"
    ]
    """
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    """
    oxxo: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataOxxo"]
    """
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
    """
    p24: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataP24"]
    """
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
    """
    pay_by_bank: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataPayByBank"
    ]
    """
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    """
    payco: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPayco"]
    """
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.
    """
    paynow: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPaynow"]
    """
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
    """
    paypal: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPaypal"]
    """
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
    """
    paypay: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPaypay"]
    """
    If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.
    """
    payto: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPayto"]
    """
    If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.
    """
    pix: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataPix"]
    """
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
    """
    promptpay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataPromptpay"
    ]
    """
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
    """
    qris: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataQris"]
    """
    If this is a `qris` PaymentMethod, this hash contains details about the QRIS payment method.
    """
    radar_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataRadarOptions"
    ]
    """
    Options to configure Radar. See [Radar Session](https://docs.stripe.com/radar/radar-session) for more information.
    """
    rechnung: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataRechnung"
    ]
    """
    If this is a `rechnung` PaymentMethod, this hash contains details about the Rechnung payment method.
    """
    revolut_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataRevolutPay"
    ]
    """
    If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
    """
    samsung_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataSamsungPay"
    ]
    """
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.
    """
    satispay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataSatispay"
    ]
    """
    If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.
    """
    sepa_debit: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataSepaDebit"
    ]
    """
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    """
    shopeepay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataShopeepay"
    ]
    """
    If this is a Shopeepay PaymentMethod, this hash contains details about the Shopeepay payment method.
    """
    sofort: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataSofort"]
    """
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    """
    stripe_balance: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataStripeBalance"
    ]
    """
    This hash contains details about the Stripe balance payment method.
    """
    swish: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataSwish"]
    """
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.
    """
    twint: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataTwint"]
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
        "PaymentIntentConfirmParamsPaymentMethodDataUsBankAccount"
    ]
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """
    wechat_pay: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodDataWechatPay"
    ]
    """
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
    """
    zip: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataZip"]
    """
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
    """


class PaymentIntentConfirmParamsPaymentMethodDataAcssDebit(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataAffirm(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataAfterpayClearpay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataAlipay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataAlma(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataAmazonPay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataAuBecsDebit(TypedDict):
    account_number: str
    """
    The account number for the bank account.
    """
    bsb_number: str
    """
    Bank-State-Branch number of the bank account.
    """


class PaymentIntentConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
    account_number: NotRequired[str]
    """
    Account number of the bank account that the funds will be debited from.
    """
    sort_code: NotRequired[str]
    """
    Sort code of the bank account. (e.g., `10-20-30`)
    """


class PaymentIntentConfirmParamsPaymentMethodDataBancontact(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataBillie(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodDataBillingDetailsAddress"
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


class PaymentIntentConfirmParamsPaymentMethodDataBillingDetailsAddress(
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


class PaymentIntentConfirmParamsPaymentMethodDataBlik(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataBoleto(TypedDict):
    tax_id: str
    """
    The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
    """


class PaymentIntentConfirmParamsPaymentMethodDataCashapp(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataCrypto(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataCustomerBalance(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataEps(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataFpx(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataGiropay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataGopay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataGrabpay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataIdBankTransfer(TypedDict):
    bank: NotRequired[Literal["bca", "bni", "bri", "cimb", "permata"]]
    """
    Bank where the account is held.
    """


class PaymentIntentConfirmParamsPaymentMethodDataIdeal(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataKakaoPay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataKlarna(TypedDict):
    dob: NotRequired["PaymentIntentConfirmParamsPaymentMethodDataKlarnaDob"]
    """
    Customer's date of birth
    """


class PaymentIntentConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataKonbini(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataKrCard(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataLink(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataMbWay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataMobilepay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataMultibanco(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataNaverPay(TypedDict):
    funding: NotRequired[Literal["card", "points"]]
    """
    Whether to use Naver Pay points or a card to fund this transaction. If not provided, this defaults to `card`.
    """


class PaymentIntentConfirmParamsPaymentMethodDataNzBankAccount(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataOxxo(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataP24(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataPayByBank(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPayco(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPaynow(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPaypal(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPaypay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPayto(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataPix(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataPromptpay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataQris(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
    session: NotRequired[str]
    """
    A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
    """


class PaymentIntentConfirmParamsPaymentMethodDataRechnung(TypedDict):
    dob: "PaymentIntentConfirmParamsPaymentMethodDataRechnungDob"
    """
    Customer's date of birth
    """


class PaymentIntentConfirmParamsPaymentMethodDataRechnungDob(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataRevolutPay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataSamsungPay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataSatispay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
    iban: str
    """
    IBAN of the bank account.
    """


class PaymentIntentConfirmParamsPaymentMethodDataShopeepay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataSofort(TypedDict):
    country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    """
    Two-letter ISO code representing the country the bank account is located in.
    """


class PaymentIntentConfirmParamsPaymentMethodDataStripeBalance(TypedDict):
    account: NotRequired[str]
    """
    The connected account ID whose Stripe balance to use as the source of payment
    """
    source_type: NotRequired[Literal["bank_account", "card", "fpx"]]
    """
    The [source_type](https://docs.stripe.com/api/balance/balance_object#balance_object-available-source_types) of the balance
    """


class PaymentIntentConfirmParamsPaymentMethodDataSwish(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataTwint(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodDataWechatPay(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodDataZip(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAcssDebit"
    ]
    """
    If this is a `acss_debit` PaymentMethod, this sub-hash contains details about the ACSS Debit payment method options.
    """
    affirm: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAffirm"
    ]
    """
    If this is an `affirm` PaymentMethod, this sub-hash contains details about the Affirm payment method options.
    """
    afterpay_clearpay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAfterpayClearpay"
    ]
    """
    If this is a `afterpay_clearpay` PaymentMethod, this sub-hash contains details about the Afterpay Clearpay payment method options.
    """
    alipay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAlipay"
    ]
    """
    If this is a `alipay` PaymentMethod, this sub-hash contains details about the Alipay payment method options.
    """
    alma: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAlma"
    ]
    """
    If this is a `alma` PaymentMethod, this sub-hash contains details about the Alma payment method options.
    """
    amazon_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAmazonPay"
    ]
    """
    If this is a `amazon_pay` PaymentMethod, this sub-hash contains details about the Amazon Pay payment method options.
    """
    au_becs_debit: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsAuBecsDebit"
    ]
    """
    If this is a `au_becs_debit` PaymentMethod, this sub-hash contains details about the AU BECS Direct Debit payment method options.
    """
    bacs_debit: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsBacsDebit"
    ]
    """
    If this is a `bacs_debit` PaymentMethod, this sub-hash contains details about the BACS Debit payment method options.
    """
    bancontact: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsBancontact"
    ]
    """
    If this is a `bancontact` PaymentMethod, this sub-hash contains details about the Bancontact payment method options.
    """
    billie: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsBillie"
    ]
    """
    If this is a `billie` PaymentMethod, this sub-hash contains details about the Billie payment method options.
    """
    blik: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsBlik"
    ]
    """
    If this is a `blik` PaymentMethod, this sub-hash contains details about the BLIK payment method options.
    """
    boleto: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsBoleto"
    ]
    """
    If this is a `boleto` PaymentMethod, this sub-hash contains details about the Boleto payment method options.
    """
    card: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCard"
    ]
    """
    Configuration for any card payments attempted on this PaymentIntent.
    """
    card_present: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCardPresent"
    ]
    """
    If this is a `card_present` PaymentMethod, this sub-hash contains details about the Card Present payment method options.
    """
    cashapp: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCashapp"
    ]
    """
    If this is a `cashapp` PaymentMethod, this sub-hash contains details about the Cash App Pay payment method options.
    """
    crypto: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCrypto"
    ]
    """
    If this is a `crypto` PaymentMethod, this sub-hash contains details about the Crypto payment method options.
    """
    customer_balance: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalance"
    ]
    """
    If this is a `customer balance` PaymentMethod, this sub-hash contains details about the customer balance payment method options.
    """
    eps: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsEps"
    ]
    """
    If this is a `eps` PaymentMethod, this sub-hash contains details about the EPS payment method options.
    """
    fpx: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsFpx"
    ]
    """
    If this is a `fpx` PaymentMethod, this sub-hash contains details about the FPX payment method options.
    """
    giropay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsGiropay"
    ]
    """
    If this is a `giropay` PaymentMethod, this sub-hash contains details about the Giropay payment method options.
    """
    gopay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsGopay"
    ]
    """
    If this is a `gopay` PaymentMethod, this sub-hash contains details about the Gopay payment method options.
    """
    grabpay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsGrabpay"
    ]
    """
    If this is a `grabpay` PaymentMethod, this sub-hash contains details about the Grabpay payment method options.
    """
    id_bank_transfer: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsIdBankTransfer"
    ]
    """
    If this is a `id_bank_transfer` PaymentMethod, this sub-hash contains details about the Indonesia Bank Transfer payment method options.
    """
    ideal: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsIdeal"
    ]
    """
    If this is a `ideal` PaymentMethod, this sub-hash contains details about the Ideal payment method options.
    """
    interac_present: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsInteracPresent"
    ]
    """
    If this is a `interac_present` PaymentMethod, this sub-hash contains details about the Card Present payment method options.
    """
    kakao_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsKakaoPay"
    ]
    """
    If this is a `kakao_pay` PaymentMethod, this sub-hash contains details about the Kakao Pay payment method options.
    """
    klarna: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsKlarna"
    ]
    """
    If this is a `klarna` PaymentMethod, this sub-hash contains details about the Klarna payment method options.
    """
    konbini: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsKonbini"
    ]
    """
    If this is a `konbini` PaymentMethod, this sub-hash contains details about the Konbini payment method options.
    """
    kr_card: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsKrCard"
    ]
    """
    If this is a `kr_card` PaymentMethod, this sub-hash contains details about the KR Card payment method options.
    """
    link: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsLink"
    ]
    """
    If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
    """
    mb_way: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsMbWay"
    ]
    """
    If this is a `mb_way` PaymentMethod, this sub-hash contains details about the MB WAY payment method options.
    """
    mobilepay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsMobilepay"
    ]
    """
    If this is a `MobilePay` PaymentMethod, this sub-hash contains details about the MobilePay payment method options.
    """
    multibanco: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsMultibanco"
    ]
    """
    If this is a `multibanco` PaymentMethod, this sub-hash contains details about the Multibanco payment method options.
    """
    naver_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsNaverPay"
    ]
    """
    If this is a `naver_pay` PaymentMethod, this sub-hash contains details about the Naver Pay payment method options.
    """
    nz_bank_account: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsNzBankAccount"
    ]
    """
    If this is a `nz_bank_account` PaymentMethod, this sub-hash contains details about the NZ BECS Direct Debit payment method options.
    """
    oxxo: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsOxxo"
    ]
    """
    If this is a `oxxo` PaymentMethod, this sub-hash contains details about the OXXO payment method options.
    """
    p24: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsP24"
    ]
    """
    If this is a `p24` PaymentMethod, this sub-hash contains details about the Przelewy24 payment method options.
    """
    pay_by_bank: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPayByBank"
    ]
    """
    If this is a `pay_by_bank` PaymentMethod, this sub-hash contains details about the PayByBank payment method options.
    """
    payco: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPayco"
    ]
    """
    If this is a `payco` PaymentMethod, this sub-hash contains details about the PAYCO payment method options.
    """
    paynow: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPaynow"
    ]
    """
    If this is a `paynow` PaymentMethod, this sub-hash contains details about the PayNow payment method options.
    """
    paypal: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPaypal"
    ]
    """
    If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
    """
    paypay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPaypay"
    ]
    """
    If this is a `paypay` PaymentMethod, this sub-hash contains details about the PayPay payment method options.
    """
    payto: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPayto"
    ]
    """
    If this is a `payto` PaymentMethod, this sub-hash contains details about the PayTo payment method options.
    """
    pix: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPix"
    ]
    """
    If this is a `pix` PaymentMethod, this sub-hash contains details about the Pix payment method options.
    """
    promptpay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsPromptpay"
    ]
    """
    If this is a `promptpay` PaymentMethod, this sub-hash contains details about the PromptPay payment method options.
    """
    qris: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsQris"
    ]
    """
    If this is a `qris` PaymentMethod, this sub-hash contains details about the QRIS payment method options.
    """
    rechnung: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsRechnung"
    ]
    """
    If this is a `rechnung` PaymentMethod, this sub-hash contains details about the Rechnung payment method options.
    """
    revolut_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsRevolutPay"
    ]
    """
    If this is a `revolut_pay` PaymentMethod, this sub-hash contains details about the Revolut Pay payment method options.
    """
    samsung_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsSamsungPay"
    ]
    """
    If this is a `samsung_pay` PaymentMethod, this sub-hash contains details about the Samsung Pay payment method options.
    """
    satispay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsSatispay"
    ]
    """
    If this is a `satispay` PaymentMethod, this sub-hash contains details about the Satispay payment method options.
    """
    sepa_debit: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsSepaDebit"
    ]
    """
    If this is a `sepa_debit` PaymentIntent, this sub-hash contains details about the SEPA Debit payment method options.
    """
    shopeepay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsShopeepay"
    ]
    """
    If this is a `shopeepay` PaymentMethod, this sub-hash contains details about the ShopeePay payment method options.
    """
    sofort: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsSofort"
    ]
    """
    If this is a `sofort` PaymentMethod, this sub-hash contains details about the SOFORT payment method options.
    """
    stripe_balance: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsStripeBalance"
    ]
    """
    If this is a `stripe_balance` PaymentMethod, this sub-hash contains details about the Stripe Balance payment method options.
    """
    swish: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsSwish"
    ]
    """
    If this is a `Swish` PaymentMethod, this sub-hash contains details about the Swish payment method options.
    """
    twint: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsTwint"
    ]
    """
    If this is a `twint` PaymentMethod, this sub-hash contains details about the TWINT payment method options.
    """
    us_bank_account: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccount"
    ]
    """
    If this is a `us_bank_account` PaymentMethod, this sub-hash contains details about the US bank account payment method options.
    """
    wechat_pay: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsWechatPay"
    ]
    """
    If this is a `wechat_pay` PaymentMethod, this sub-hash contains details about the WeChat Pay payment method options.
    """
    zip: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsZip"
    ]
    """
    If this is a `zip` PaymentMethod, this sub-hash contains details about the Zip payment method options.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAffirm(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAfterpayClearpay(
    TypedDict
):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAlipay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAlma(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsAmazonPay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsBacsDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsBacsDebitMandateOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsBacsDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'DDIC' or 'STRIPE'.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsBancontact(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsBillie(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsBlik(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsBoleto(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCard(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardInstallments"
    ]
    """
    Installment configuration for payments attempted on this PaymentIntent.

    For more information, see the [installments integration guide](https://docs.stripe.com/payments/installments).
    """
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardMandateOptions"
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
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCardStatementDetails"
    ]
    """
    Statement details for this payment intent. You can use this to override the merchant details shown on your customers' statements.
    """
    three_d_secure: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecure"
    ]
    """
    If 3D Secure authentication was performed with a third-party provider,
    the authentication details to use for this payment.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCardInstallments(
    TypedDict
):
    enabled: NotRequired[bool]
    """
    Setting to true enables installments for this PaymentIntent.
    This will cause the response to contain a list of available installment plans.
    Setting to false will prevent any selected plan from applying to a charge.
    """
    plan: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsCardInstallmentsPlan"
    ]
    """
    The selected installment plan to use for this payment attempt.
    This parameter can only be provided during confirmation.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCardInstallmentsPlan(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCardMandateOptions(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCardStatementDetails(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardStatementDetailsAddress"
    ]
    """
    Please pass in an address that is within your Stripe user account country
    """
    phone: NotRequired[str]
    """
    Phone number (e.g., a toll-free number that customers can call)
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCardStatementDetailsAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecure(
    TypedDict
):
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    TypedDict,
):
    cartes_bancaires: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires"
    ]
    """
    Cartes Bancaires-specific 3DS fields.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCardPresent(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsCardPresentRouting"
    ]
    """
    Network routing priority on co-branded EMV cards supporting domestic debit and international card schemes.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCardPresentRouting(
    TypedDict,
):
    requested_priority: NotRequired[Literal["domestic", "international"]]
    """
    Routing requested priority
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCashapp(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCrypto(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalance(TypedDict):
    bank_transfer: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
    TypedDict,
):
    eu_bank_transfer: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
    TypedDict,
):
    country: str
    """
    The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsEps(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsFpx(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsGiropay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsGopay(TypedDict):
    setup_future_usage: NotRequired[Literal["none", "off_session"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsGrabpay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsIdBankTransfer(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsIdeal(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsInteracPresent(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodOptionsKakaoPay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarna(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """
    on_demand: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaOnDemand"
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
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSubscription]"
    ]
    """
    Subscription details if setting up or charging a subscription.
    """
    supplementary_purchase_data: NotRequired[
        "Literal['']|PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseData"
    ]
    """
    Supplementary Purchase Data for the corresponding Klarna payment
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaOnDemand(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSubscription(
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling"
    ]
    """
    Describes the upcoming charge for this subscription.
    """
    reference: str
    """
    A non-customer-facing reference to correlate subscription charges in the Klarna app. Use a value that persists across subscription charges.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseData(
    TypedDict,
):
    bus_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetail]"
    ]
    """
    Supplementary bus reservation details.
    """
    event_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetail]"
    ]
    """
    Supplementary event reservation details.
    """
    ferry_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetail]"
    ]
    """
    Supplementary ferry reservation details.
    """
    insurances: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataInsurance]"
    ]
    """
    Supplementary insurance details.
    """
    marketplace_sellers: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSeller]"
    ]
    """
    Supplementary marketplace seller details.
    """
    round_trip_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetail]"
    ]
    """
    Supplementary round trip reservation details.
    """
    train_reservation_details: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetail]"
    ]
    """
    Supplementary train reservation details.
    """
    vouchers: NotRequired[
        "Literal['']|List[PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataVoucher]"
    ]
    """
    Voucher details, such as a gift card or discount code.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrival"
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailPassenger"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailArrivalAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDepartureAddress"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailDepartureAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataBusReservationDetailPassenger(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetail(
    TypedDict,
):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailAddress"
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
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailInsurance"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataEventReservationDetailInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrival"
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailPassenger"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailArrivalAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDepartureAddress"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailDepartureAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataFerryReservationDetailPassenger(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSeller(
    TypedDict,
):
    line_item_references: NotRequired[List[str]]
    """
    The references to line items for purchases with multiple associated sub-sellers.
    """
    marketplace_seller_address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSellerMarketplaceSellerAddress"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataMarketplaceSellerMarketplaceSellerAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrival"
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailPassenger"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailArrivalAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDepartureAddress"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailDepartureAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataRoundTripReservationDetailPassenger(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetail(
    TypedDict,
):
    affiliate_name: NotRequired[str]
    """
    Name of associated or partner company for the service.
    """
    arrival: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrival"
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDeparture"
    ]
    """
    Departure details.
    """
    insurances: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailInsurance"
        ]
    ]
    """
    List of insurances for this reservation.
    """
    passengers: NotRequired[
        List[
            "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailPassenger"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrival(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrivalAddress"
    ]
    """
    Address of the arrival location.
    """
    arrival_location: NotRequired[str]
    """
    Identifier name or reference for the arrival location.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailArrivalAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDeparture(
    TypedDict,
):
    address: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDepartureAddress"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailDepartureAddress(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailInsurance(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataTrainReservationDetailPassenger(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKlarnaSupplementaryPurchaseDataVoucher(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKonbini(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsKrCard(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsLink(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsMbWay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsMobilepay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsMultibanco(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsNaverPay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsNzBankAccount(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsOxxo(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsP24(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPayByBank(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodOptionsPayco(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsPaynow(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds will be captured from the customer's account.
    """
    line_items: NotRequired[
        List["PaymentIntentConfirmParamsPaymentMethodOptionsPaypalLineItem"]
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPaypalLineItem(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsPaypalLineItemTax"
    ]
    """
    The tax information for the line item.
    """
    unit_amount: int
    """
    Price for a single unit of the line item in minor units. Cannot be a negative number.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsPaypalLineItemTax(
    TypedDict,
):
    amount: int
    """
    The tax for a single unit of the line item in minor units. Cannot be a negative number.
    """
    behavior: Literal["exclusive", "inclusive"]
    """
    The tax behavior for the line item.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsPaypay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsPayto(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsPaytoMandateOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPaytoMandateOptions(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPix(TypedDict):
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
        "PaymentIntentConfirmParamsPaymentMethodOptionsPixMandateOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPixMandateOptions(
    TypedDict,
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


class PaymentIntentConfirmParamsPaymentMethodOptionsPromptpay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsQris(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsRechnung(TypedDict):
    pass


class PaymentIntentConfirmParamsPaymentMethodOptionsRevolutPay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsSamsungPay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsSatispay(TypedDict):
    capture_method: NotRequired["Literal['']|Literal['manual']"]
    """
    Controls when the funds are captured from the customer's account.

    If provided, this parameter overrides the behavior of the top-level [capture_method](https://docs.stripe.com/api/payment_intents/update#update_payment_intent-capture_method) for this payment method type when finalizing the payment with this payment method type.

    If `capture_method` is already set on the PaymentIntent, providing an empty value for this parameter unsets the stored value for this payment method type.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'STRIPE'.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsShopeepay(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsSofort(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsStripeBalance(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsSwish(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsTwint(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
    financial_connections: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
    ]
    """
    Additional fields for Financial Connections Session creation
    """
    mandate_options: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    networks: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountNetworks"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    manual_entry: NotRequired[
        "PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry"
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


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
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


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
    TypedDict,
):
    mode: Literal["automatic", "custom"]
    """
    Settings for configuring manual entry of account details.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountMandateOptions(
    TypedDict,
):
    collection_method: NotRequired["Literal['']|Literal['paper']"]
    """
    The method used to collect offline mandate customer acceptance.
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(
    TypedDict,
):
    requested: NotRequired[List[Literal["ach", "us_domestic_wire"]]]
    """
    Triggers validations to run across the selected networks
    """


class PaymentIntentConfirmParamsPaymentMethodOptionsWechatPay(TypedDict):
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


class PaymentIntentConfirmParamsPaymentMethodOptionsZip(TypedDict):
    setup_future_usage: NotRequired[Literal["none"]]
    """
    Indicates that you intend to make future payments with this PaymentIntent's payment method.

    If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](https://docs.stripe.com/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](https://docs.stripe.com/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

    If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

    When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](https://docs.stripe.com/strong-customer-authentication).

    If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    """


class PaymentIntentConfirmParamsRadarOptions(TypedDict):
    session: NotRequired[str]
    """
    A [Radar Session](https://docs.stripe.com/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
    """


class PaymentIntentConfirmParamsShipping(TypedDict):
    address: "PaymentIntentConfirmParamsShippingAddress"
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


class PaymentIntentConfirmParamsShippingAddress(TypedDict):
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
