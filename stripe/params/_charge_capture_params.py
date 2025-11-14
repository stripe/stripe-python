# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ChargeCaptureParams(RequestOptions):
    amount: NotRequired[int]
    """
    The amount to capture, which must be less than or equal to the original amount.
    """
    application_fee: NotRequired[int]
    """
    An application fee to add on to this charge.
    """
    application_fee_amount: NotRequired[int]
    """
    An application fee amount to add on to this charge, which must be less than or equal to the original amount.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_details: NotRequired["ChargeCaptureParamsPaymentDetails"]
    """
    Provides industry-specific information about the charge.
    """
    receipt_email: NotRequired[str]
    """
    The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.
    """
    statement_descriptor: NotRequired[str]
    """
    For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

    For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    """
    statement_descriptor_suffix: NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    """
    transfer_data: NotRequired["ChargeCaptureParamsTransferData"]
    """
    An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """
    transfer_group: NotRequired[str]
    """
    A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """


class ChargeCaptureParamsPaymentDetails(TypedDict):
    car_rental: NotRequired["ChargeCaptureParamsPaymentDetailsCarRental"]
    """
    Car rental details for this PaymentIntent.
    """
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    event_details: NotRequired["ChargeCaptureParamsPaymentDetailsEventDetails"]
    """
    Event details for this PaymentIntent
    """
    flight: NotRequired["ChargeCaptureParamsPaymentDetailsFlight"]
    """
    Flight reservation details for this PaymentIntent
    """
    lodging: NotRequired["ChargeCaptureParamsPaymentDetailsLodging"]
    """
    Lodging reservation details for this PaymentIntent
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    Required when the Payment Method Types array contains `card`, including when [automatic_payment_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled) is set to `true`.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.
    """
    subscription: NotRequired["ChargeCaptureParamsPaymentDetailsSubscription"]
    """
    Subscription details for this PaymentIntent
    """


class ChargeCaptureParamsPaymentDetailsCarRental(TypedDict):
    affiliate: NotRequired[
        "ChargeCaptureParamsPaymentDetailsCarRentalAffiliate"
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
    delivery: NotRequired["ChargeCaptureParamsPaymentDetailsCarRentalDelivery"]
    """
    Delivery details for this purchase.
    """
    distance: NotRequired["ChargeCaptureParamsPaymentDetailsCarRentalDistance"]
    """
    The details of the distance traveled during the rental period.
    """
    drivers: NotRequired[
        List["ChargeCaptureParamsPaymentDetailsCarRentalDriver"]
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
        "ChargeCaptureParamsPaymentDetailsCarRentalPickupAddress"
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
        "ChargeCaptureParamsPaymentDetailsCarRentalReturnAddress"
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


class ChargeCaptureParamsPaymentDetailsCarRentalAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeCaptureParamsPaymentDetailsCarRentalDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeCaptureParamsPaymentDetailsCarRentalDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeCaptureParamsPaymentDetailsCarRentalDeliveryRecipient(TypedDict):
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


class ChargeCaptureParamsPaymentDetailsCarRentalDistance(TypedDict):
    amount: NotRequired[int]
    """
    Distance traveled.
    """
    unit: NotRequired[Literal["kilometers", "miles"]]
    """
    Unit of measurement for the distance traveled. One of `miles` or `kilometers`.
    """


class ChargeCaptureParamsPaymentDetailsCarRentalDriver(TypedDict):
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


class ChargeCaptureParamsPaymentDetailsCarRentalPickupAddress(TypedDict):
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
    State, county, province, or region.
    """


class ChargeCaptureParamsPaymentDetailsCarRentalReturnAddress(TypedDict):
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
    State, county, province, or region.
    """


class ChargeCaptureParamsPaymentDetailsEventDetails(TypedDict):
    access_controlled_venue: NotRequired[bool]
    """
    Indicates if the tickets are digitally checked when entering the venue.
    """
    address: NotRequired[
        "ChargeCaptureParamsPaymentDetailsEventDetailsAddress"
    ]
    """
    The event location's address.
    """
    affiliate: NotRequired[
        "ChargeCaptureParamsPaymentDetailsEventDetailsAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    company: NotRequired[str]
    """
    The name of the company
    """
    delivery: NotRequired[
        "ChargeCaptureParamsPaymentDetailsEventDetailsDelivery"
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


class ChargeCaptureParamsPaymentDetailsEventDetailsAddress(TypedDict):
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
    State, county, province, or region.
    """


class ChargeCaptureParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeCaptureParamsPaymentDetailsEventDetailsDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeCaptureParamsPaymentDetailsEventDetailsDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeCaptureParamsPaymentDetailsEventDetailsDeliveryRecipient(
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


class ChargeCaptureParamsPaymentDetailsFlight(TypedDict):
    affiliate: NotRequired["ChargeCaptureParamsPaymentDetailsFlightAffiliate"]
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
    delivery: NotRequired["ChargeCaptureParamsPaymentDetailsFlightDelivery"]
    """
    Delivery details for this purchase.
    """
    passenger_name: NotRequired[str]
    """
    The name of the person or entity on the reservation.
    """
    passengers: NotRequired[
        List["ChargeCaptureParamsPaymentDetailsFlightPassenger"]
    ]
    """
    The details of the passengers in the travel reservation.
    """
    segments: List["ChargeCaptureParamsPaymentDetailsFlightSegment"]
    """
    The individual flight segments associated with the trip.
    """
    ticket_number: NotRequired[str]
    """
    The ticket number associated with the travel reservation.
    """


class ChargeCaptureParamsPaymentDetailsFlightAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeCaptureParamsPaymentDetailsFlightDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeCaptureParamsPaymentDetailsFlightDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeCaptureParamsPaymentDetailsFlightDeliveryRecipient(TypedDict):
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


class ChargeCaptureParamsPaymentDetailsFlightPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the flight reservation.
    """


class ChargeCaptureParamsPaymentDetailsFlightSegment(TypedDict):
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


class ChargeCaptureParamsPaymentDetailsLodging(TypedDict):
    address: NotRequired["ChargeCaptureParamsPaymentDetailsLodgingAddress"]
    """
    The lodging location's address.
    """
    adults: NotRequired[int]
    """
    The number of adults on the booking
    """
    affiliate: NotRequired["ChargeCaptureParamsPaymentDetailsLodgingAffiliate"]
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
    delivery: NotRequired["ChargeCaptureParamsPaymentDetailsLodgingDelivery"]
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
        List["ChargeCaptureParamsPaymentDetailsLodgingPassenger"]
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


class ChargeCaptureParamsPaymentDetailsLodgingAddress(TypedDict):
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
    State, county, province, or region.
    """


class ChargeCaptureParamsPaymentDetailsLodgingAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeCaptureParamsPaymentDetailsLodgingDelivery(TypedDict):
    mode: NotRequired[Literal["email", "phone", "pickup", "post"]]
    """
    The delivery method for the payment
    """
    recipient: NotRequired[
        "ChargeCaptureParamsPaymentDetailsLodgingDeliveryRecipient"
    ]
    """
    Details of the recipient.
    """


class ChargeCaptureParamsPaymentDetailsLodgingDeliveryRecipient(TypedDict):
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


class ChargeCaptureParamsPaymentDetailsLodgingPassenger(TypedDict):
    name: str
    """
    Full name of the person or entity on the lodging reservation.
    """


class ChargeCaptureParamsPaymentDetailsSubscription(TypedDict):
    affiliate: NotRequired[
        "ChargeCaptureParamsPaymentDetailsSubscriptionAffiliate"
    ]
    """
    Affiliate details for this purchase.
    """
    auto_renewal: NotRequired[bool]
    """
    Info whether the subscription will be auto renewed upon expiry.
    """
    billing_interval: NotRequired[
        "ChargeCaptureParamsPaymentDetailsSubscriptionBillingInterval"
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


class ChargeCaptureParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
    name: str
    """
    The name of the affiliate that originated the purchase.
    """


class ChargeCaptureParamsPaymentDetailsSubscriptionBillingInterval(TypedDict):
    count: int
    """
    The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
    """
    interval: Literal["day", "month", "week", "year"]
    """
    Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
    """


class ChargeCaptureParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
    """
