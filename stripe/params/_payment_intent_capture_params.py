# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentCaptureParams(RequestOptions):
    amount_details: NotRequired["PaymentIntentCaptureParamsAmountDetails"]
    """
    Provides industry-specific information about the amount.
    """
    amount_to_capture: NotRequired[int]
    """
    The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it's not provided.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    final_capture: NotRequired[bool]
    """
    Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they're captured in future requests. You can only use this setting when [multicapture](https://docs.stripe.com/payments/multicapture) is available for PaymentIntents.
    """
    hooks: NotRequired["PaymentIntentCaptureParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    metadata: NotRequired[
        "Literal['']|Dict[str, str]|UntypedStripeObject[str]"
    ]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: NotRequired[
        "Literal['']|PaymentIntentCaptureParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the charge.
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
    transfer_data: NotRequired["PaymentIntentCaptureParamsTransferData"]
    """
    The parameters that you can use to automatically create a transfer after the payment
    is captured. Learn more about the [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class PaymentIntentCaptureParamsAmountDetails(TypedDict):
    discount_amount: NotRequired["Literal['']|int"]
    """
    The total discount applied on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[line_items][#][discount_amount]` field.
    """
    enforce_arithmetic_validation: NotRequired[bool]
    """
    Set to `false` to return arithmetic validation errors in the response without failing the request. Use this when you want the operation to proceed regardless of arithmetic errors in the line item data.

    Omit or set to `true` to immediately return a 400 error when arithmetic validation fails. Use this for strict validation that prevents processing with line item data that has arithmetic inconsistencies.

    For card payments, Stripe doesn't send line item data to card networks if there's an arithmetic validation error.
    """
    line_items: NotRequired[
        "Literal['']|List[PaymentIntentCaptureParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 200 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentCaptureParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    tax: NotRequired["Literal['']|PaymentIntentCaptureParamsAmountDetailsTax"]
    """
    Contains information about the tax portion of the amount.
    """


class PaymentIntentCaptureParamsAmountDetailsLineItem(TypedDict):
    discount_amount: NotRequired[int]
    """
    The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]` field.
    """
    payment_method_options: NotRequired[
        "PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptions"
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

    For Cards, this field is truncated to 26 alphanumeric characters before being sent to the card networks. For PayPal, this field is truncated to 127 characters.
    """
    quantity: int
    """
    The quantity of items. Required for L3 rates. An integer greater than 0.
    """
    tax: NotRequired["PaymentIntentCaptureParamsAmountDetailsLineItemTax"]
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


class PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to the `card` payment method.
    """
    card_present: NotRequired[
        "PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to the `card_present` payment method.
    """
    klarna: NotRequired[
        "PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to the `klarna` payment method.
    """
    paypal: NotRequired[
        "PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to the `paypal` payment method.
    """


class PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """


class PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """


class PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
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


class PaymentIntentCaptureParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
    TypedDict,
):
    category: NotRequired[
        "Literal['digital_goods', 'donation', 'physical_goods']|str"
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


class PaymentIntentCaptureParamsAmountDetailsLineItemTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.
    """


class PaymentIntentCaptureParamsAmountDetailsShipping(TypedDict):
    amount: NotRequired["Literal['']|int"]
    """
    If a physical good is being shipped, the cost of shipping represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than or equal to 0.
    """
    from_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped from. At most 10 alphanumeric characters long, hyphens and spaces are allowed.
    """
    to_postal_code: NotRequired["Literal['']|str"]
    """
    If a physical good is being shipped, the postal code of where it is being shipped to. At most 10 alphanumeric characters long, hyphens and spaces are allowed.
    """


class PaymentIntentCaptureParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class PaymentIntentCaptureParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentCaptureParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentCaptureParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentCaptureParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentCaptureParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id
    """


class PaymentIntentCaptureParamsPaymentDetails(TypedDict):
    car_rental_data: NotRequired[
        "Literal['']|List[PaymentIntentCaptureParamsPaymentDetailsCarRentalDatum]"
    ]
    """
    Car rental data for this PaymentIntent.
    """
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    lodging_data: NotRequired[
        "Literal['']|List[PaymentIntentCaptureParamsPaymentDetailsLodgingDatum]"
    ]
    """
    Lodging data for this PaymentIntent.
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatum(TypedDict):
    affiliate: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumAffiliate"
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
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDistance"
    ]
    """
    Distance details for the rental.
    """
    drivers: NotRequired[
        List["PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDriver"]
    ]
    """
    List of drivers for the rental.
    """
    drop_off: "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDropOff"
    """
    Drop-off location details.
    """
    insurances: NotRequired[
        List["PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumInsurance"]
    ]
    """
    Insurance details for the rental.
    """
    no_show_indicator: NotRequired[bool]
    """
    Indicates if the customer was a no-show.
    """
    pickup: "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumPickup"
    """
    Pickup location details.
    """
    renter_name: NotRequired[str]
    """
    Name of the person renting the vehicle.
    """
    total: "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotal"
    """
    Total cost breakdown for the rental.
    """
    vehicle: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumVehicle"
    ]
    """
    Vehicle details for the rental.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumAffiliate(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDistance(
    TypedDict
):
    amount: int
    """
    Distance traveled.
    """
    unit: Union[Literal["kilometers", "miles"], str]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDriver(TypedDict):
    date_of_birth: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDriverDateOfBirth"
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDriverDateOfBirth(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDropOff(TypedDict):
    address: (
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDropOffAddress"
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumDropOffAddress(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumInsurance(
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
    insurance_type: Union[
        Literal[
            "liability_supplement",
            "loss_damage_waiver",
            "other",
            "partial_damage_waiver",
            "personal_accident",
            "personal_effects",
        ],
        str,
    ]
    """
    Type of insurance coverage.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumPickup(TypedDict):
    address: (
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumPickupAddress"
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumPickupAddress(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotal(TypedDict):
    amount: int
    """
    Total amount in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the amount.
    """
    discounts: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalDiscounts"
    ]
    """
    Discount details for the rental.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalExtraCharge"
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
        "Literal['days', 'kilometers', 'miles', 'months', 'weeks']|str"
    ]
    """
    Unit of measurement for the rate.
    """
    tax: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalTax"
    ]
    """
    Tax breakdown for the rental.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalDiscounts(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalExtraCharge(
    TypedDict,
):
    amount: int
    """
    Amount of the extra charge in cents.
    """
    type: Union[
        Literal[
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
        ],
        str,
    ]
    """
    Type of extra charge.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalTax(
    TypedDict
):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates if the transaction is tax exempt.
    """
    tax_items: NotRequired[
        List[
            "PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalTaxTaxItem"
        ]
    ]
    """
    Array of tax details.
    """


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumTotalTaxTaxItem(
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


class PaymentIntentCaptureParamsPaymentDetailsCarRentalDatumVehicle(TypedDict):
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
        "Literal['cargo_van', 'compact', 'economy', 'exotic', 'exotic_suv', 'fifteen_passenger_van', 'four_wheel_drive', 'full_size', 'intermediate', 'large_suv', 'large_truck', 'luxury', 'medium_suv', 'midsize', 'mini', 'minivan', 'miscellaneous', 'moped', 'moving_van', 'premium', 'regular', 'small_medium_truck', 'small_suv', 'special', 'standard', 'stretch', 'subcompact', 'taxi', 'twelve_foot_truck', 'twelve_passenger_van', 'twenty_foot_truck', 'twenty_four_foot_truck', 'twenty_six_foot_truck', 'unique']|str"
    ]
    """
    Type of the rental vehicle.
    """
    vehicle_class: NotRequired[
        "Literal['business', 'economy', 'first_class', 'premium_economy']|str"
    ]
    """
    Class of the rental vehicle.
    """
    vehicle_identification_number: NotRequired[str]
    """
    Vehicle identification number (VIN).
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatum(TypedDict):
    accommodation: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumAccommodation"
    ]
    """
    Accommodation details for the lodging.
    """
    affiliate: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumAffiliate"
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
        List["PaymentIntentCaptureParamsPaymentDetailsLodgingDatumGuest"]
    ]
    """
    List of guests for the lodging.
    """
    host: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumHost"
    ]
    """
    Host details for the lodging.
    """
    insurances: NotRequired[
        List["PaymentIntentCaptureParamsPaymentDetailsLodgingDatumInsurance"]
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
    total: "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotal"
    """
    Total details for the lodging.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumAccommodation(
    TypedDict,
):
    accommodation_type: NotRequired[
        "Literal['apartment', 'cabana', 'house', 'penthouse', 'room', 'standard', 'suite', 'villa']|str"
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


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Affiliate partner name.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumGuest(TypedDict):
    name: str
    """
    Guest's full name.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumHost(TypedDict):
    address: NotRequired[
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumHostAddress"
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
        "Literal['hostel', 'hotel', 'owner', 'rental_agency']|str"
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


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumHostAddress(
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


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumInsurance(TypedDict):
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
    insurance_type: Union[
        Literal["bankruptcy", "cancelation", "emergency", "medical"], str
    ]
    """
    Type of insurance coverage.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotal(TypedDict):
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
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalDiscounts"
    ]
    """
    Discount details for the lodging.
    """
    extra_charges: NotRequired[
        List[
            "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalExtraCharge"
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
        "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalTax"
    ]
    """
    Tax breakdown for the lodging reservation.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalDiscounts(
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


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalExtraCharge(
    TypedDict,
):
    amount: NotRequired[int]
    """
    Amount of the extra charge in cents.
    """
    type: NotRequired[
        "Literal['gift_shop', 'laundry', 'mini_bar', 'other', 'phone', 'restaurant']|str"
    ]
    """
    Type of extra charge.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates whether the transaction is tax exempt.
    """
    tax_items: NotRequired[
        List[
            "PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalTaxTaxItem"
        ]
    ]
    """
    Tax details.
    """


class PaymentIntentCaptureParamsPaymentDetailsLodgingDatumTotalTaxTaxItem(
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


class PaymentIntentCaptureParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    """
