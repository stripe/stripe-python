# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._charge import Charge
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._search_result_object import SearchResultObject
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ChargeService(StripeService):
    class CaptureParams(TypedDict):
        amount: NotRequired["int"]
        """
        The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.
        """
        application_fee: NotRequired["int"]
        """
        An application fee to add on to this charge.
        """
        application_fee_amount: NotRequired["int"]
        """
        An application fee amount to add on to this charge, which must be less than or equal to the original amount.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_details: NotRequired[
            "ChargeService.CaptureParamsPaymentDetails"
        ]
        """
        Provides industry-specific information about the charge.
        """
        receipt_email: NotRequired["str"]
        """
        The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.
        """
        statement_descriptor: NotRequired["str"]
        """
        For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
        """
        statement_descriptor_suffix: NotRequired["str"]
        """
        Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """
        transfer_data: NotRequired["ChargeService.CaptureParamsTransferData"]
        """
        An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
        """
        transfer_group: NotRequired["str"]
        """
        A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
        """

    class CaptureParamsPaymentDetails(TypedDict):
        car_rental: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRental"
        ]
        """
        Car rental details for this PaymentIntent.
        """
        event_details: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsEventDetails"
        ]
        """
        Event details for this PaymentIntent
        """
        flight: NotRequired["ChargeService.CaptureParamsPaymentDetailsFlight"]
        """
        Flight reservation details for this PaymentIntent
        """
        lodging: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsLodging"
        ]
        """
        Lodging reservation details for this PaymentIntent
        """
        subscription: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsSubscription"
        ]
        """
        Subscription details for this PaymentIntent
        """

    class CaptureParamsPaymentDetailsCarRental(TypedDict):
        affiliate: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRentalAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        booking_number: str
        """
        The booking number associated with the car rental.
        """
        car_class_code: NotRequired["str"]
        """
        Class code of the car.
        """
        car_make: NotRequired["str"]
        """
        Make of the car.
        """
        car_model: NotRequired["str"]
        """
        Model of the car.
        """
        company: NotRequired["str"]
        """
        The name of the rental car company.
        """
        customer_service_phone_number: NotRequired["str"]
        """
        The customer service phone number of the car rental company.
        """
        days_rented: int
        """
        Number of days the car is being rented.
        """
        delivery: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRentalDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        drivers: NotRequired[
            "List[ChargeService.CaptureParamsPaymentDetailsCarRentalDriver]"
        ]
        """
        The details of the passengers in the travel reservation
        """
        extra_charges: NotRequired[
            "List[Literal['extra_mileage', 'gas', 'late_return', 'one_way_service', 'parking_violation']]"
        ]
        """
        List of additional charges being billed.
        """
        no_show: NotRequired["bool"]
        """
        Indicates if the customer did not keep nor cancel their booking.
        """
        pickup_address: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRentalPickupAddress"
        ]
        """
        Car pick-up address.
        """
        pickup_at: int
        """
        Car pick-up time. Measured in seconds since the Unix epoch.
        """
        rate_amount: NotRequired["int"]
        """
        Rental rate.
        """
        rate_interval: NotRequired["Literal['day', 'month', 'week']"]
        """
        The frequency at which the rate amount is applied. One of `day`, `week` or `month`
        """
        renter_name: NotRequired["str"]
        """
        The name of the person or entity renting the car.
        """
        return_address: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRentalReturnAddress"
        ]
        """
        Car return address.
        """
        return_at: int
        """
        Car return time. Measured in seconds since the Unix epoch.
        """
        tax_exempt: NotRequired["bool"]
        """
        Indicates whether the goods or services are tax-exempt or tax is not collected.
        """

    class CaptureParamsPaymentDetailsCarRentalAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class CaptureParamsPaymentDetailsCarRentalDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsCarRentalDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class CaptureParamsPaymentDetailsCarRentalDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class CaptureParamsPaymentDetailsCarRentalDriver(TypedDict):
        name: str
        """
        Full name of the person or entity on the car reservation.
        """

    class CaptureParamsPaymentDetailsCarRentalPickupAddress(TypedDict):
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
        State, county, province, or region.
        """

    class CaptureParamsPaymentDetailsCarRentalReturnAddress(TypedDict):
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
        State, county, province, or region.
        """

    class CaptureParamsPaymentDetailsEventDetails(TypedDict):
        access_controlled_venue: NotRequired["bool"]
        """
        Indicates if the tickets are digitally checked when entering the venue.
        """
        address: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsEventDetailsAddress"
        ]
        """
        The event location's address.
        """
        affiliate: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsEventDetailsAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        company: NotRequired["str"]
        """
        The name of the company
        """
        delivery: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsEventDetailsDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        ends_at: NotRequired["int"]
        """
        Event end time. Measured in seconds since the Unix epoch.
        """
        genre: NotRequired["str"]
        """
        Type of the event entertainment (concert, sports event etc)
        """
        name: str
        """
        The name of the event.
        """
        starts_at: NotRequired["int"]
        """
        Event start time. Measured in seconds since the Unix epoch.
        """

    class CaptureParamsPaymentDetailsEventDetailsAddress(TypedDict):
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
        State, county, province, or region.
        """

    class CaptureParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class CaptureParamsPaymentDetailsEventDetailsDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsEventDetailsDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class CaptureParamsPaymentDetailsEventDetailsDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class CaptureParamsPaymentDetailsFlight(TypedDict):
        affiliate: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsFlightAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        agency_number: NotRequired["str"]
        """
        The agency number (i.e. International Air Transport Association (IATA) agency number) of the travel agency that made the booking.
        """
        carrier: NotRequired["str"]
        """
        The International Air Transport Association (IATA) carrier code of the carrier that issued the ticket.
        """
        delivery: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsFlightDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        passenger_name: NotRequired["str"]
        """
        The name of the person or entity on the reservation.
        """
        passengers: NotRequired[
            "List[ChargeService.CaptureParamsPaymentDetailsFlightPassenger]"
        ]
        """
        The details of the passengers in the travel reservation.
        """
        segments: List[
            "ChargeService.CaptureParamsPaymentDetailsFlightSegment"
        ]
        """
        The individual flight segments associated with the trip.
        """
        ticket_number: NotRequired["str"]
        """
        The ticket number associated with the travel reservation.
        """

    class CaptureParamsPaymentDetailsFlightAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class CaptureParamsPaymentDetailsFlightDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsFlightDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class CaptureParamsPaymentDetailsFlightDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class CaptureParamsPaymentDetailsFlightPassenger(TypedDict):
        name: str
        """
        Full name of the person or entity on the flight reservation.
        """

    class CaptureParamsPaymentDetailsFlightSegment(TypedDict):
        amount: NotRequired["int"]
        """
        The flight segment amount.
        """
        arrival_airport: NotRequired["str"]
        """
        The International Air Transport Association (IATA) airport code for the arrival airport.
        """
        arrives_at: NotRequired["int"]
        """
        The arrival time for the flight segment. Measured in seconds since the Unix epoch.
        """
        carrier: NotRequired["str"]
        """
        The International Air Transport Association (IATA) carrier code of the carrier operating the flight segment.
        """
        departs_at: int
        """
        The departure time for the flight segment. Measured in seconds since the Unix epoch.
        """
        departure_airport: NotRequired["str"]
        """
        The International Air Transport Association (IATA) airport code for the departure airport.
        """
        flight_number: NotRequired["str"]
        """
        The flight number associated with the segment
        """
        service_class: NotRequired[
            "Literal['business', 'economy', 'first', 'premium_economy']"
        ]
        """
        The fare class for the segment.
        """

    class CaptureParamsPaymentDetailsLodging(TypedDict):
        address: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsLodgingAddress"
        ]
        """
        The lodging location's address.
        """
        adults: NotRequired["int"]
        """
        The number of adults on the booking
        """
        affiliate: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsLodgingAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        booking_number: NotRequired["str"]
        """
        The booking number associated with the lodging reservation.
        """
        category: NotRequired["Literal['hotel', 'vacation_rental']"]
        """
        The lodging category
        """
        checkin_at: int
        """
        Loding check-in time. Measured in seconds since the Unix epoch.
        """
        checkout_at: int
        """
        Lodging check-out time. Measured in seconds since the Unix epoch.
        """
        customer_service_phone_number: NotRequired["str"]
        """
        The customer service phone number of the lodging company.
        """
        daily_room_rate_amount: NotRequired["int"]
        """
        The daily lodging room rate.
        """
        delivery: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsLodgingDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        extra_charges: NotRequired[
            "List[Literal['gift_shop', 'laundry', 'mini_bar', 'other', 'restaurant', 'telephone']]"
        ]
        """
        List of additional charges being billed.
        """
        fire_safety_act_compliance: NotRequired["bool"]
        """
        Indicates whether the lodging location is compliant with the Fire Safety Act.
        """
        name: NotRequired["str"]
        """
        The name of the lodging location.
        """
        no_show: NotRequired["bool"]
        """
        Indicates if the customer did not keep their booking while failing to cancel the reservation.
        """
        number_of_rooms: NotRequired["int"]
        """
        The number of rooms on the booking
        """
        passengers: NotRequired[
            "List[ChargeService.CaptureParamsPaymentDetailsLodgingPassenger]"
        ]
        """
        The details of the passengers in the travel reservation
        """
        property_phone_number: NotRequired["str"]
        """
        The phone number of the lodging location.
        """
        room_class: NotRequired["str"]
        """
        The room class for this purchase.
        """
        room_nights: NotRequired["int"]
        """
        The number of room nights
        """
        total_room_tax_amount: NotRequired["int"]
        """
        The total tax amount associating with the room reservation.
        """
        total_tax_amount: NotRequired["int"]
        """
        The total tax amount
        """

    class CaptureParamsPaymentDetailsLodgingAddress(TypedDict):
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
        State, county, province, or region.
        """

    class CaptureParamsPaymentDetailsLodgingAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class CaptureParamsPaymentDetailsLodgingDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsLodgingDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class CaptureParamsPaymentDetailsLodgingDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class CaptureParamsPaymentDetailsLodgingPassenger(TypedDict):
        name: str
        """
        Full name of the person or entity on the lodging reservation.
        """

    class CaptureParamsPaymentDetailsSubscription(TypedDict):
        affiliate: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsSubscriptionAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        auto_renewal: NotRequired["bool"]
        """
        Info whether the subscription will be auto renewed upon expiry.
        """
        billing_interval: NotRequired[
            "ChargeService.CaptureParamsPaymentDetailsSubscriptionBillingInterval"
        ]
        """
        Subscription billing details for this purchase.
        """
        ends_at: NotRequired["int"]
        """
        Subscription end time. Measured in seconds since the Unix epoch.
        """
        name: str
        """
        Name of the product on subscription. e.g. Apple Music Subscription
        """
        starts_at: NotRequired["int"]
        """
        Subscription start time. Measured in seconds since the Unix epoch.
        """

    class CaptureParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class CaptureParamsPaymentDetailsSubscriptionBillingInterval(TypedDict):
        count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """

    class CaptureParamsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
        """

    class CreateParams(TypedDict):
        amount: NotRequired["int"]
        """
        Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
        """
        application_fee: NotRequired["int"]
        application_fee_amount: NotRequired["int"]
        """
        A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees).
        """
        capture: NotRequired["bool"]
        """
        Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: NotRequired["str"]
        """
        The ID of an existing customer that will be charged in this request.
        """
        description: NotRequired["str"]
        """
        An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
        """
        destination: NotRequired["ChargeService.CreateParamsDestination"]
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        on_behalf_of: NotRequired["str"]
        """
        The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#on-behalf-of).
        """
        radar_options: NotRequired["ChargeService.CreateParamsRadarOptions"]
        """
        Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
        """
        receipt_email: NotRequired["str"]
        """
        The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
        """
        shipping: NotRequired["ChargeService.CreateParamsShipping"]
        """
        Shipping information for the charge. Helps prevent fraud on charges for physical goods.
        """
        source: NotRequired["str"]
        """
        A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer.
        """
        statement_descriptor: NotRequired["str"]
        """
        For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
        """
        statement_descriptor_suffix: NotRequired["str"]
        """
        Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """
        transfer_data: NotRequired["ChargeService.CreateParamsTransferData"]
        """
        An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
        """
        transfer_group: NotRequired["str"]
        """
        A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options).
        """

    class CreateParamsDestination(TypedDict):
        account: str
        """
        ID of an existing, connected Stripe account.
        """
        amount: NotRequired["int"]
        """
        The amount to transfer to the destination account without creating an `Application Fee` object. Cannot be combined with the `application_fee` parameter. Must be less than or equal to the charge amount.
        """

    class CreateParamsRadarOptions(TypedDict):
        session: NotRequired["str"]
        """
        A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
        """

    class CreateParamsShipping(TypedDict):
        address: "ChargeService.CreateParamsShippingAddress"
        """
        Shipping address.
        """
        carrier: NotRequired["str"]
        """
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
        """
        name: str
        """
        Recipient name.
        """
        phone: NotRequired["str"]
        """
        Recipient phone (including extension).
        """
        tracking_number: NotRequired["str"]
        """
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
        """

    class CreateParamsShippingAddress(TypedDict):
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
        State, county, province, or region.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
        """
        destination: str
        """
        ID of an existing, connected Stripe account.
        """

    class ListParams(TypedDict):
        created: NotRequired["ChargeService.ListParamsCreated|int"]
        customer: NotRequired["str"]
        """
        Only return charges for the customer specified by this customer ID.
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
        payment_intent: NotRequired["str"]
        """
        Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        transfer_group: NotRequired["str"]
        """
        Only return charges for this transfer group.
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired["int"]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired["int"]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired["int"]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired["int"]
        """
        Maximum value to filter by (inclusive)
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class SearchParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        page: NotRequired["str"]
        """
        A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
        """
        query: str
        """
        The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges).
        """

    class UpdateParams(TypedDict):
        customer: NotRequired["str"]
        """
        The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
        """
        description: NotRequired["str"]
        """
        An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        fraud_details: NotRequired["ChargeService.UpdateParamsFraudDetails"]
        """
        A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment_details: NotRequired[
            "ChargeService.UpdateParamsPaymentDetails"
        ]
        """
        Provides industry-specific information about the charge.
        """
        receipt_email: NotRequired["str"]
        """
        This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
        """
        shipping: NotRequired["ChargeService.UpdateParamsShipping"]
        """
        Shipping information for the charge. Helps prevent fraud on charges for physical goods.
        """
        transfer_group: NotRequired["str"]
        """
        A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
        """

    class UpdateParamsFraudDetails(TypedDict):
        user_report: Union[Literal[""], Literal["fraudulent", "safe"]]
        """
        Either `safe` or `fraudulent`.
        """

    class UpdateParamsPaymentDetails(TypedDict):
        car_rental: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRental"
        ]
        """
        Car rental details for this PaymentIntent.
        """
        event_details: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsEventDetails"
        ]
        """
        Event details for this PaymentIntent
        """
        flight: NotRequired["ChargeService.UpdateParamsPaymentDetailsFlight"]
        """
        Flight reservation details for this PaymentIntent
        """
        lodging: NotRequired["ChargeService.UpdateParamsPaymentDetailsLodging"]
        """
        Lodging reservation details for this PaymentIntent
        """
        subscription: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsSubscription"
        ]
        """
        Subscription details for this PaymentIntent
        """

    class UpdateParamsPaymentDetailsCarRental(TypedDict):
        affiliate: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRentalAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        booking_number: str
        """
        The booking number associated with the car rental.
        """
        car_class_code: NotRequired["str"]
        """
        Class code of the car.
        """
        car_make: NotRequired["str"]
        """
        Make of the car.
        """
        car_model: NotRequired["str"]
        """
        Model of the car.
        """
        company: NotRequired["str"]
        """
        The name of the rental car company.
        """
        customer_service_phone_number: NotRequired["str"]
        """
        The customer service phone number of the car rental company.
        """
        days_rented: int
        """
        Number of days the car is being rented.
        """
        delivery: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRentalDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        drivers: NotRequired[
            "List[ChargeService.UpdateParamsPaymentDetailsCarRentalDriver]"
        ]
        """
        The details of the passengers in the travel reservation
        """
        extra_charges: NotRequired[
            "List[Literal['extra_mileage', 'gas', 'late_return', 'one_way_service', 'parking_violation']]"
        ]
        """
        List of additional charges being billed.
        """
        no_show: NotRequired["bool"]
        """
        Indicates if the customer did not keep nor cancel their booking.
        """
        pickup_address: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRentalPickupAddress"
        ]
        """
        Car pick-up address.
        """
        pickup_at: int
        """
        Car pick-up time. Measured in seconds since the Unix epoch.
        """
        rate_amount: NotRequired["int"]
        """
        Rental rate.
        """
        rate_interval: NotRequired["Literal['day', 'month', 'week']"]
        """
        The frequency at which the rate amount is applied. One of `day`, `week` or `month`
        """
        renter_name: NotRequired["str"]
        """
        The name of the person or entity renting the car.
        """
        return_address: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRentalReturnAddress"
        ]
        """
        Car return address.
        """
        return_at: int
        """
        Car return time. Measured in seconds since the Unix epoch.
        """
        tax_exempt: NotRequired["bool"]
        """
        Indicates whether the goods or services are tax-exempt or tax is not collected.
        """

    class UpdateParamsPaymentDetailsCarRentalAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class UpdateParamsPaymentDetailsCarRentalDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsCarRentalDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class UpdateParamsPaymentDetailsCarRentalDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class UpdateParamsPaymentDetailsCarRentalDriver(TypedDict):
        name: str
        """
        Full name of the person or entity on the car reservation.
        """

    class UpdateParamsPaymentDetailsCarRentalPickupAddress(TypedDict):
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
        State, county, province, or region.
        """

    class UpdateParamsPaymentDetailsCarRentalReturnAddress(TypedDict):
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
        State, county, province, or region.
        """

    class UpdateParamsPaymentDetailsEventDetails(TypedDict):
        access_controlled_venue: NotRequired["bool"]
        """
        Indicates if the tickets are digitally checked when entering the venue.
        """
        address: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsEventDetailsAddress"
        ]
        """
        The event location's address.
        """
        affiliate: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsEventDetailsAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        company: NotRequired["str"]
        """
        The name of the company
        """
        delivery: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsEventDetailsDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        ends_at: NotRequired["int"]
        """
        Event end time. Measured in seconds since the Unix epoch.
        """
        genre: NotRequired["str"]
        """
        Type of the event entertainment (concert, sports event etc)
        """
        name: str
        """
        The name of the event.
        """
        starts_at: NotRequired["int"]
        """
        Event start time. Measured in seconds since the Unix epoch.
        """

    class UpdateParamsPaymentDetailsEventDetailsAddress(TypedDict):
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
        State, county, province, or region.
        """

    class UpdateParamsPaymentDetailsEventDetailsAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class UpdateParamsPaymentDetailsEventDetailsDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsEventDetailsDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class UpdateParamsPaymentDetailsEventDetailsDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class UpdateParamsPaymentDetailsFlight(TypedDict):
        affiliate: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsFlightAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        agency_number: NotRequired["str"]
        """
        The agency number (i.e. International Air Transport Association (IATA) agency number) of the travel agency that made the booking.
        """
        carrier: NotRequired["str"]
        """
        The International Air Transport Association (IATA) carrier code of the carrier that issued the ticket.
        """
        delivery: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsFlightDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        passenger_name: NotRequired["str"]
        """
        The name of the person or entity on the reservation.
        """
        passengers: NotRequired[
            "List[ChargeService.UpdateParamsPaymentDetailsFlightPassenger]"
        ]
        """
        The details of the passengers in the travel reservation.
        """
        segments: List["ChargeService.UpdateParamsPaymentDetailsFlightSegment"]
        """
        The individual flight segments associated with the trip.
        """
        ticket_number: NotRequired["str"]
        """
        The ticket number associated with the travel reservation.
        """

    class UpdateParamsPaymentDetailsFlightAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class UpdateParamsPaymentDetailsFlightDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsFlightDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class UpdateParamsPaymentDetailsFlightDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class UpdateParamsPaymentDetailsFlightPassenger(TypedDict):
        name: str
        """
        Full name of the person or entity on the flight reservation.
        """

    class UpdateParamsPaymentDetailsFlightSegment(TypedDict):
        amount: NotRequired["int"]
        """
        The flight segment amount.
        """
        arrival_airport: NotRequired["str"]
        """
        The International Air Transport Association (IATA) airport code for the arrival airport.
        """
        arrives_at: NotRequired["int"]
        """
        The arrival time for the flight segment. Measured in seconds since the Unix epoch.
        """
        carrier: NotRequired["str"]
        """
        The International Air Transport Association (IATA) carrier code of the carrier operating the flight segment.
        """
        departs_at: int
        """
        The departure time for the flight segment. Measured in seconds since the Unix epoch.
        """
        departure_airport: NotRequired["str"]
        """
        The International Air Transport Association (IATA) airport code for the departure airport.
        """
        flight_number: NotRequired["str"]
        """
        The flight number associated with the segment
        """
        service_class: NotRequired[
            "Literal['business', 'economy', 'first', 'premium_economy']"
        ]
        """
        The fare class for the segment.
        """

    class UpdateParamsPaymentDetailsLodging(TypedDict):
        address: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsLodgingAddress"
        ]
        """
        The lodging location's address.
        """
        adults: NotRequired["int"]
        """
        The number of adults on the booking
        """
        affiliate: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsLodgingAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        booking_number: NotRequired["str"]
        """
        The booking number associated with the lodging reservation.
        """
        category: NotRequired["Literal['hotel', 'vacation_rental']"]
        """
        The lodging category
        """
        checkin_at: int
        """
        Loding check-in time. Measured in seconds since the Unix epoch.
        """
        checkout_at: int
        """
        Lodging check-out time. Measured in seconds since the Unix epoch.
        """
        customer_service_phone_number: NotRequired["str"]
        """
        The customer service phone number of the lodging company.
        """
        daily_room_rate_amount: NotRequired["int"]
        """
        The daily lodging room rate.
        """
        delivery: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsLodgingDelivery"
        ]
        """
        Delivery details for this purchase.
        """
        extra_charges: NotRequired[
            "List[Literal['gift_shop', 'laundry', 'mini_bar', 'other', 'restaurant', 'telephone']]"
        ]
        """
        List of additional charges being billed.
        """
        fire_safety_act_compliance: NotRequired["bool"]
        """
        Indicates whether the lodging location is compliant with the Fire Safety Act.
        """
        name: NotRequired["str"]
        """
        The name of the lodging location.
        """
        no_show: NotRequired["bool"]
        """
        Indicates if the customer did not keep their booking while failing to cancel the reservation.
        """
        number_of_rooms: NotRequired["int"]
        """
        The number of rooms on the booking
        """
        passengers: NotRequired[
            "List[ChargeService.UpdateParamsPaymentDetailsLodgingPassenger]"
        ]
        """
        The details of the passengers in the travel reservation
        """
        property_phone_number: NotRequired["str"]
        """
        The phone number of the lodging location.
        """
        room_class: NotRequired["str"]
        """
        The room class for this purchase.
        """
        room_nights: NotRequired["int"]
        """
        The number of room nights
        """
        total_room_tax_amount: NotRequired["int"]
        """
        The total tax amount associating with the room reservation.
        """
        total_tax_amount: NotRequired["int"]
        """
        The total tax amount
        """

    class UpdateParamsPaymentDetailsLodgingAddress(TypedDict):
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
        State, county, province, or region.
        """

    class UpdateParamsPaymentDetailsLodgingAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class UpdateParamsPaymentDetailsLodgingDelivery(TypedDict):
        mode: NotRequired["Literal['email', 'phone', 'pickup', 'post']"]
        """
        The delivery method for the payment
        """
        recipient: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsLodgingDeliveryRecipient"
        ]
        """
        Details of the recipient.
        """

    class UpdateParamsPaymentDetailsLodgingDeliveryRecipient(TypedDict):
        email: NotRequired["str"]
        """
        The email of the recipient the ticket is delivered to.
        """
        name: NotRequired["str"]
        """
        The name of the recipient the ticket is delivered to.
        """
        phone: NotRequired["str"]
        """
        The phone number of the recipient the ticket is delivered to.
        """

    class UpdateParamsPaymentDetailsLodgingPassenger(TypedDict):
        name: str
        """
        Full name of the person or entity on the lodging reservation.
        """

    class UpdateParamsPaymentDetailsSubscription(TypedDict):
        affiliate: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsSubscriptionAffiliate"
        ]
        """
        Affiliate details for this purchase.
        """
        auto_renewal: NotRequired["bool"]
        """
        Info whether the subscription will be auto renewed upon expiry.
        """
        billing_interval: NotRequired[
            "ChargeService.UpdateParamsPaymentDetailsSubscriptionBillingInterval"
        ]
        """
        Subscription billing details for this purchase.
        """
        ends_at: NotRequired["int"]
        """
        Subscription end time. Measured in seconds since the Unix epoch.
        """
        name: str
        """
        Name of the product on subscription. e.g. Apple Music Subscription
        """
        starts_at: NotRequired["int"]
        """
        Subscription start time. Measured in seconds since the Unix epoch.
        """

    class UpdateParamsPaymentDetailsSubscriptionAffiliate(TypedDict):
        name: str
        """
        The name of the affiliate that originated the purchase.
        """

    class UpdateParamsPaymentDetailsSubscriptionBillingInterval(TypedDict):
        count: int
        """
        The number of intervals, as an whole number greater than 0. Stripe multiplies this by the interval type to get the overall duration.
        """
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies a type of interval unit. Either `day`, `week`, `month` or `year`.
        """

    class UpdateParamsShipping(TypedDict):
        address: "ChargeService.UpdateParamsShippingAddress"
        """
        Shipping address.
        """
        carrier: NotRequired["str"]
        """
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
        """
        name: str
        """
        Recipient name.
        """
        phone: NotRequired["str"]
        """
        Recipient phone (including extension).
        """
        tracking_number: NotRequired["str"]
        """
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
        """

    class UpdateParamsShippingAddress(TypedDict):
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
        State, county, province, or region.
        """

    def list(
        self,
        params: "ChargeService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Charge]:
        """
        Returns a list of charges you've previously created. The charges are returned in sorted order, with the most recent charges appearing first.
        """
        return cast(
            ListObject[Charge],
            self._request(
                "get",
                "/v1/charges",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ChargeService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Charge]:
        """
        Returns a list of charges you've previously created. The charges are returned in sorted order, with the most recent charges appearing first.
        """
        return cast(
            ListObject[Charge],
            await self._request_async(
                "get",
                "/v1/charges",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ChargeService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        This method is no longer recommended—use the [Payment Intents API](https://stripe.com/docs/api/payment_intents)
        to initiate a new payment instead. Confirmation of the PaymentIntent creates the Charge
        object used to request payment.
        """
        return cast(
            Charge,
            self._request(
                "post",
                "/v1/charges",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ChargeService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        This method is no longer recommended—use the [Payment Intents API](https://stripe.com/docs/api/payment_intents)
        to initiate a new payment instead. Confirmation of the PaymentIntent creates the Charge
        object used to request payment.
        """
        return cast(
            Charge,
            await self._request_async(
                "post",
                "/v1/charges",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        charge: str,
        params: "ChargeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.
        """
        return cast(
            Charge,
            self._request(
                "get",
                "/v1/charges/{charge}".format(charge=sanitize_id(charge)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        charge: str,
        params: "ChargeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Retrieves the details of a charge that has previously been created. Supply the unique charge ID that was returned from your previous request, and Stripe will return the corresponding charge information. The same information is returned when creating or refunding the charge.
        """
        return cast(
            Charge,
            await self._request_async(
                "get",
                "/v1/charges/{charge}".format(charge=sanitize_id(charge)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        charge: str,
        params: "ChargeService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Charge,
            self._request(
                "post",
                "/v1/charges/{charge}".format(charge=sanitize_id(charge)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        charge: str,
        params: "ChargeService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Updates the specified charge by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Charge,
            await self._request_async(
                "post",
                "/v1/charges/{charge}".format(charge=sanitize_id(charge)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def search(
        self,
        params: "ChargeService.SearchParams",
        options: RequestOptions = {},
    ) -> SearchResultObject[Charge]:
        """
        Search for charges you've previously created using Stripe's [Search Query Language](https://stripe.com/docs/search#search-query-language).
        Don't use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.
        """
        return cast(
            SearchResultObject[Charge],
            self._request(
                "get",
                "/v1/charges/search",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def search_async(
        self,
        params: "ChargeService.SearchParams",
        options: RequestOptions = {},
    ) -> SearchResultObject[Charge]:
        """
        Search for charges you've previously created using Stripe's [Search Query Language](https://stripe.com/docs/search#search-query-language).
        Don't use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.
        """
        return cast(
            SearchResultObject[Charge],
            await self._request_async(
                "get",
                "/v1/charges/search",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def capture(
        self,
        charge: str,
        params: "ChargeService.CaptureParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Capture the payment of an existing, uncaptured charge that was created with the capture option set to false.

        Uncaptured payments expire a set number of days after they are created ([7 by default](https://stripe.com/docs/charges/placing-a-hold)), after which they are marked as refunded and capture attempts will fail.

        Don't use this method to capture a PaymentIntent-initiated charge. Use [Capture a PaymentIntent](https://stripe.com/docs/api/payment_intents/capture).
        """
        return cast(
            Charge,
            self._request(
                "post",
                "/v1/charges/{charge}/capture".format(
                    charge=sanitize_id(charge),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def capture_async(
        self,
        charge: str,
        params: "ChargeService.CaptureParams" = {},
        options: RequestOptions = {},
    ) -> Charge:
        """
        Capture the payment of an existing, uncaptured charge that was created with the capture option set to false.

        Uncaptured payments expire a set number of days after they are created ([7 by default](https://stripe.com/docs/charges/placing-a-hold)), after which they are marked as refunded and capture attempts will fail.

        Don't use this method to capture a PaymentIntent-initiated charge. Use [Capture a PaymentIntent](https://stripe.com/docs/api/payment_intents/capture).
        """
        return cast(
            Charge,
            await self._request_async(
                "post",
                "/v1/charges/{charge}/capture".format(
                    charge=sanitize_id(charge),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
