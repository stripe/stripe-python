# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ChargeUpdateParams(TypedDict):
    customer: NotRequired[str]
    """
    The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
    """
    description: NotRequired[str]
    """
    An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    fraud_details: NotRequired["ChargeUpdateParamsFraudDetails"]
    """
    A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: NotRequired["ChargeUpdateParamsPaymentDetails"]
    """
    Provides industry-specific information about the charge.
    """
    receipt_email: NotRequired[str]
    """
    This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
    """
    shipping: NotRequired["ChargeUpdateParamsShipping"]
    """
    Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    """
    transfer_group: NotRequired[str]
    """
    A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://docs.stripe.com/connect/separate-charges-and-transfers#transfer-options) for details.
    """


class ChargeUpdateParamsFraudDetails(TypedDict):
    user_report: Union[Literal[""], Literal["fraudulent", "safe"]]
    """
    Either `safe` or `fraudulent`.
    """


class ChargeUpdateParamsPaymentDetails(TypedDict):
    car_rental: NotRequired["ChargeUpdateParamsPaymentDetailsCarRental"]
    """
    Car rental details for this PaymentIntent.
    """
    car_rental_data: NotRequired[
        "Literal['']|List[ChargeUpdateParamsPaymentDetailsCarRentalDatum]"
    ]
    """
    Car rental data for this PaymentIntent.
    """
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    event_details: NotRequired["ChargeUpdateParamsPaymentDetailsEventDetails"]
    """
    Event details for this PaymentIntent
    """
    flight: NotRequired["ChargeUpdateParamsPaymentDetailsFlight"]
    """
    Flight reservation details for this PaymentIntent
    """
    flight_data: NotRequired[
        "Literal['']|List[ChargeUpdateParamsPaymentDetailsFlightDatum]"
    ]
    """
    Flight data for this PaymentIntent.
    """
    lodging: NotRequired["ChargeUpdateParamsPaymentDetailsLodging"]
    """
    Lodging reservation details for this PaymentIntent
    """
    lodging_data: NotRequired[
        "Literal['']|List[ChargeUpdateParamsPaymentDetailsLodgingDatum]"
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
    subscription: NotRequired["ChargeUpdateParamsPaymentDetailsSubscription"]
    """
    Subscription details for this PaymentIntent
    """


class ChargeUpdateParamsPaymentDetailsCarRental(TypedDict):
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalAffiliate"
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
    delivery: NotRequired["ChargeUpdateParamsPaymentDetailsCarRentalDelivery"]
    """
    Delivery details for this purchase.
    """
    distance: NotRequired["ChargeUpdateParamsPaymentDetailsCarRentalDistance"]
    """
    The details of the distance traveled during the rental period.
    """
    drivers: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsCarRentalDriver"]
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
        "ChargeUpdateParamsPaymentDetailsCarRentalPickupAddress"
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
        "ChargeUpdateParamsPaymentDetailsCarRentalReturnAddress"
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


class ChargeUpdateParamsPaymentDetailsCarRentalAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDeliveryRecipient(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDistance(TypedDict):
    amount: NotRequired[int]
    """
    Distance traveled.
    """
    unit: NotRequired[Literal["kilometers", "miles"]]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDriver(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalPickupAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalReturnAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatum(TypedDict):
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalDatumAffiliate"
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
        "ChargeUpdateParamsPaymentDetailsCarRentalDatumDistance"
    ]
    """
    Distance details for the rental.
    """
    drivers: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsCarRentalDatumDriver"]
    ]
    """
    List of drivers for the rental.
    """
    drop_off: "ChargeUpdateParamsPaymentDetailsCarRentalDatumDropOff"
    """
    Drop-off location details.
    """
    insurances: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsCarRentalDatumInsurance"]
    ]
    """
    Insurance details for the rental.
    """
    no_show_indicator: NotRequired[bool]
    """
    Indicates if the customer was a no-show.
    """
    pickup: "ChargeUpdateParamsPaymentDetailsCarRentalDatumPickup"
    """
    Pickup location details.
    """
    renter_name: NotRequired[str]
    """
    Name of the person renting the vehicle.
    """
    total: "ChargeUpdateParamsPaymentDetailsCarRentalDatumTotal"
    """
    Total cost breakdown for the rental.
    """
    vehicle: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalDatumVehicle"
    ]
    """
    Vehicle details for the rental.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Name of affiliate partner.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDatumDistance(TypedDict):
    amount: int
    """
    Distance traveled.
    """
    unit: Literal["kilometers", "miles"]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDatumDriver(TypedDict):
    date_of_birth: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalDatumDriverDateOfBirth"
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumDriverDateOfBirth(
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumDropOff(TypedDict):
    address: "ChargeUpdateParamsPaymentDetailsCarRentalDatumDropOffAddress"
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumDropOffAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumInsurance(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumPickup(TypedDict):
    address: "ChargeUpdateParamsPaymentDetailsCarRentalDatumPickupAddress"
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumPickupAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumTotal(TypedDict):
    amount: int
    """
    Total amount in cents.
    """
    currency: NotRequired[str]
    """
    Currency of the amount.
    """
    discounts: NotRequired[
        "ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalDiscounts"
    ]
    """
    Discount details for the rental.
    """
    extra_charges: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalExtraCharge"]
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
    tax: NotRequired["ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalTax"]
    """
    Tax breakdown for the rental.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalDiscounts(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalExtraCharge(
    TypedDict
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates if the transaction is tax exempt.
    """
    taxes: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalTaxTax"]
    ]
    """
    Array of tax details.
    """


class ChargeUpdateParamsPaymentDetailsCarRentalDatumTotalTaxTax(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsCarRentalDatumVehicle(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsEventDetails(TypedDict):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired["ChargeUpdateParamsPaymentDetailsEventDetailsAddress"]
    """
    The event location's address.
    """
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsEventDetailsAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    company: NotRequired[str]
    """
    The name of the company
    """
    delivery: NotRequired[
        "ChargeUpdateParamsPaymentDetailsEventDetailsDelivery"
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


class ChargeUpdateParamsPaymentDetailsEventDetailsAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeUpdateParamsPaymentDetailsEventDetailsDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeUpdateParamsPaymentDetailsEventDetailsDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeUpdateParamsPaymentDetailsEventDetailsDeliveryRecipient(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlight(TypedDict):
    affiliate: NotRequired["ChargeUpdateParamsPaymentDetailsFlightAffiliate"]
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
    delivery: NotRequired["ChargeUpdateParamsPaymentDetailsFlightDelivery"]
    """
    Delivery details for this purchase.
    """
    passenger_name: NotRequired[str]
    """
    The name of the person or entity on the reservation.
    """
    passengers: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsFlightPassenger"]
    ]
    """
    The details of the passengers in the travel reservation.
    """
    segments: List["ChargeUpdateParamsPaymentDetailsFlightSegment"]
    """
    The individual flight segments associated with the trip.
    """
    ticket_number: NotRequired[str]
    """
    The ticket number associated with the travel reservation.
    """


class ChargeUpdateParamsPaymentDetailsFlightAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeUpdateParamsPaymentDetailsFlightDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeUpdateParamsPaymentDetailsFlightDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeUpdateParamsPaymentDetailsFlightDeliveryRecipient(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the flight reservation.
    """


class ChargeUpdateParamsPaymentDetailsFlightSegment(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatum(TypedDict):
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsFlightDatumAffiliate"
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
        List["ChargeUpdateParamsPaymentDetailsFlightDatumInsurance"]
    ]
    """
    List of insurances.
    """
    passengers: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsFlightDatumPassenger"]
    ]
    """
    List of passengers.
    """
    segments: List["ChargeUpdateParamsPaymentDetailsFlightDatumSegment"]
    """
    List of flight segments.
    """
    ticket_electronically_issued_indicator: NotRequired[bool]
    """
    Electronic ticket indicator.
    """
    total: "ChargeUpdateParamsPaymentDetailsFlightDatumTotal"
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


class ChargeUpdateParamsPaymentDetailsFlightDatumAffiliate(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatumInsurance(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatumPassenger(TypedDict):
    name: str
    """
    Passenger's full name.
    """


class ChargeUpdateParamsPaymentDetailsFlightDatumSegment(TypedDict):
    amount: NotRequired[int]
    """
    Segment fare amount.
    """
    arrival: "ChargeUpdateParamsPaymentDetailsFlightDatumSegmentArrival"
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
    departure: "ChargeUpdateParamsPaymentDetailsFlightDatumSegmentDeparture"
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


class ChargeUpdateParamsPaymentDetailsFlightDatumSegmentArrival(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatumSegmentDeparture(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatumTotal(TypedDict):
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
        "ChargeUpdateParamsPaymentDetailsFlightDatumTotalDiscounts"
    ]
    """
    Discount details.
    """
    extra_charges: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsFlightDatumTotalExtraCharge"]
    ]
    """
    Additional charges.
    """
    tax: NotRequired["ChargeUpdateParamsPaymentDetailsFlightDatumTotalTax"]
    """
    Tax breakdown.
    """


class ChargeUpdateParamsPaymentDetailsFlightDatumTotalDiscounts(TypedDict):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """


class ChargeUpdateParamsPaymentDetailsFlightDatumTotalExtraCharge(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsFlightDatumTotalTax(TypedDict):
    taxes: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsFlightDatumTotalTaxTax"]
    ]
    """
    Array of tax details.
    """


class ChargeUpdateParamsPaymentDetailsFlightDatumTotalTaxTax(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodging(TypedDict):
    address: NotRequired["ChargeUpdateParamsPaymentDetailsLodgingAddress"]
    """
    The lodging location's address.
    """
    adults: NotRequired[int]
    """
    The number of adults on the booking
    """
    affiliate: NotRequired["ChargeUpdateParamsPaymentDetailsLodgingAffiliate"]
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
    delivery: NotRequired["ChargeUpdateParamsPaymentDetailsLodgingDelivery"]
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
        List["ChargeUpdateParamsPaymentDetailsLodgingPassenger"]
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


class ChargeUpdateParamsPaymentDetailsLodgingAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeUpdateParamsPaymentDetailsLodgingDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDeliveryRecipient(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the lodging reservation.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatum(TypedDict):
    accommodation: NotRequired[
        "ChargeUpdateParamsPaymentDetailsLodgingDatumAccommodation"
    ]
    """
    Accommodation details for the lodging.
    """
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsLodgingDatumAffiliate"
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
        List["ChargeUpdateParamsPaymentDetailsLodgingDatumGuest"]
    ]
    """
    List of guests for the lodging.
    """
    host: NotRequired["ChargeUpdateParamsPaymentDetailsLodgingDatumHost"]
    """
    Host details for the lodging.
    """
    insurances: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsLodgingDatumInsurance"]
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
    total: "ChargeUpdateParamsPaymentDetailsLodgingDatumTotal"
    """
    Total details for the lodging.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumAccommodation(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingDatumAffiliate(TypedDict):
    code: NotRequired[str]
    """
    Affiliate partner code.
    """
    name: NotRequired[str]
    """
    Affiliate partner name.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumGuest(TypedDict):
    name: str
    """
    Guest's full name.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumHost(TypedDict):
    address: NotRequired[
        "ChargeUpdateParamsPaymentDetailsLodgingDatumHostAddress"
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


class ChargeUpdateParamsPaymentDetailsLodgingDatumHostAddress(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingDatumInsurance(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingDatumTotal(TypedDict):
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
        "ChargeUpdateParamsPaymentDetailsLodgingDatumTotalDiscounts"
    ]
    """
    Discount details for the lodging.
    """
    extra_charges: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsLodgingDatumTotalExtraCharge"]
    ]
    """
    Additional charges for the lodging.
    """
    prepaid_amount: NotRequired[int]
    """
    Prepaid amount in cents.
    """
    tax: NotRequired["ChargeUpdateParamsPaymentDetailsLodgingDatumTotalTax"]
    """
    Tax breakdown for the lodging reservation.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumTotalDiscounts(TypedDict):
    corporate_client_code: NotRequired[str]
    """
    Corporate client discount code.
    """
    coupon: NotRequired[str]
    """
    Coupon code.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumTotalExtraCharge(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsLodgingDatumTotalTax(TypedDict):
    tax_exempt_indicator: NotRequired[bool]
    """
    Indicates whether the transaction is tax exempt.
    """
    taxes: NotRequired[
        List["ChargeUpdateParamsPaymentDetailsLodgingDatumTotalTaxTax"]
    ]
    """
    Tax details.
    """


class ChargeUpdateParamsPaymentDetailsLodgingDatumTotalTaxTax(TypedDict):
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


class ChargeUpdateParamsPaymentDetailsSubscription(TypedDict):
    affiliate: NotRequired[
        "ChargeUpdateParamsPaymentDetailsSubscriptionAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    auto_renewal: NotRequired[bool]
    """
    Info whether the subscription will be auto renewed upon expiry.
    """
    billing_interval: NotRequired[
        "ChargeUpdateParamsPaymentDetailsSubscriptionBillingInterval"
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


class ChargeUpdateParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeUpdateParamsPaymentDetailsSubscriptionBillingInterval(TypedDict):
    count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """


class ChargeUpdateParamsShipping(TypedDict):
    address: "ChargeUpdateParamsShippingAddress"
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


class ChargeUpdateParamsShippingAddress(TypedDict):
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
