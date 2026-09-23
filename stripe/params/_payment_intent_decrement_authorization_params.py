# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PaymentIntentDecrementAuthorizationParams(RequestOptions):
    amount: int
    """
    The updated total amount that you intend to collect from the cardholder. This amount must be smaller than the currently authorized amount and greater than the already captured amount.
    """
    amount_details: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetails"
    ]
    """
    Provides industry-specific information about the amount.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    hooks: NotRequired["PaymentIntentDecrementAuthorizationParamsHooks"]
    """
    Automations to be run during the PaymentIntent lifecycle
    """
    metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_details: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsPaymentDetails"
    ]
    """
    Provides industry-specific information about the charge.
    """
    transfer_data: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsTransferData"
    ]
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetails(TypedDict):
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
        "Literal['']|List[PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItem]"
    ]
    """
    A list of line items, each containing information about a product in the PaymentIntent. There is a maximum of 200 line items.
    """
    shipping: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsShipping"
    ]
    """
    Contains information about the shipping portion of the amount.
    """
    surcharge: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsSurcharge"
    ]
    """
    Contains information about the surcharge portion of the amount.
    """
    tax: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsTax"
    ]
    """
    Contains information about the tax portion of the amount.
    """
    tip: NotRequired[
        "Literal['']|PaymentIntentDecrementAuthorizationParamsAmountDetailsTip"
    ]
    """
    Contains information about the tip portion of the amount.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItem(
    TypedDict
):
    discount_amount: NotRequired[int]
    """
    The discount applied on this line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). An integer greater than 0.

    This field is mutually exclusive with the `amount_details[discount_amount]` field.
    """
    payment_method_options: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions"
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
    quantity_precision: NotRequired[int]
    """
    The number of decimal places implied in the quantity. For example, if quantity is 10000 and quantity_precision is 2, the actual quantity is 100.00. Defaults to 0 if not provided.
    """
    tax: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemTax"
    ]
    """
    Contains information about the tax on the item.
    """
    unit_cost: int
    """
    The unit cost of the line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.
    """
    unit_cost_precision: NotRequired[int]
    """
    The number of decimal places implied in the unit_cost. For example, if unit_cost is 10000 and unit_cost_precision is 1, the actual unit cost is 1000.0. Defaults to 0 if not provided.
    """
    unit_of_measure: NotRequired[str]
    """
    A unit of measure for the line item, such as gallons, feet, meters, etc.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptions(
    TypedDict,
):
    card: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard"
    ]
    """
    This sub-hash contains line item details that are specific to the `card` payment method.
    """
    card_present: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent"
    ]
    """
    This sub-hash contains line item details that are specific to the `card_present` payment method.
    """
    klarna: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna"
    ]
    """
    This sub-hash contains line item details that are specific to the `klarna` payment method.
    """
    paypal: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal"
    ]
    """
    This sub-hash contains line item details that are specific to the `paypal` payment method.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCard(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """
    ev_charging: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardEvCharging"
    ]
    """
    EV charging data for this line item.
    """
    fleet_data: NotRequired[
        "PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardFleetData"
    ]
    """
    Fleet data for this line item.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardEvCharging(
    TypedDict,
):
    carbon_footprint_avoided_grams_co2: NotRequired[int]
    """
    The carbon footprint avoided by the charging session, in grams of CO2.
    """
    charging_ended_at: int
    """
    The time the charging session ended, measured in seconds since the Unix epoch.
    """
    charging_power_output_capacity_kw: int
    """
    The power output capacity of the charging station, in kilowatts (kW).
    """
    charging_started_at: int
    """
    The time the charging session started, measured in seconds since the Unix epoch.
    """
    connector_type: Union[
        Literal[
            "ac_gb_t",
            "ac_j1772",
            "ac_mennekes",
            "dc_ccs1",
            "dc_ccs2",
            "dc_chademo",
            "dc_gb_t",
            "dc_mcs",
            "nacs",
        ],
        str,
    ]
    """
    The type of connector used for the charging session.
    """
    estimated_range_added: NotRequired[int]
    """
    The estimated distance in kilometers or miles added to the vehicle during the charging session.
    """
    estimated_range_left: NotRequired[int]
    """
    The estimated distance in kilometers or miles remaining in the vehicle after the charging session.
    """
    maximum_power_dispensed_kw: int
    """
    The maximum power dispensed during the charging session, in kilowatts (kW).
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardFleetData(
    TypedDict,
):
    product_type: Union[
        Literal[
            "additive_dosage",
            "additized_diesel_2",
            "additized_diesel_3",
            "air_conditioning_service",
            "air_filter",
            "alcohol",
            "antifreeze",
            "automotive_merchandise",
            "aviation_fuel_premium",
            "aviation_fuel_regular",
            "batteries",
            "biodiesel_b1",
            "biodiesel_b10",
            "biodiesel_b100",
            "biodiesel_b11",
            "biodiesel_b15",
            "biodiesel_b2",
            "biodiesel_b20",
            "biodiesel_b5",
            "biodiesel_b75",
            "biodiesel_b99",
            "blended_diesel_1_and_2",
            "body_work",
            "brake_fluid",
            "brake_service",
            "car_care_detailing",
            "car_wash",
            "compressed_natural_gas",
            "def_at_pump",
            "deli",
            "e85",
            "engine_service",
            "ethanol_e16_to_e84",
            "ev_battery_exchanges",
            "ev_charging_fee",
            "evc_level_1",
            "evc_level_2",
            "evc_level_3",
            "evc_level_4",
            "evc_level_5",
            "exhaust_service",
            "federal_tire_excise_tax",
            "food_service",
            "fuel_additive_treatment",
            "fuel_system",
            "green_gasoline_mid_plus",
            "green_gasoline_premium_super",
            "green_gasoline_regular",
            "grocery",
            "heating_oil",
            "hoses",
            "hydrogen_h35",
            "hydrogen_h70",
            "inspection",
            "kerosene_low_sulfur",
            "kerosene_low_sulfur_non_taxable",
            "kerosene_ultra_low_sulfur",
            "kerosene_ultra_low_sulfur_non_taxable",
            "labor",
            "lamps",
            "liquid_natural_gas",
            "liquid_propane_gas",
            "lodging",
            "low_octane_unleaded",
            "lube",
            "marine_diesel",
            "marine_fuel",
            "marine_fuel_1",
            "marine_fuel_2",
            "marine_fuel_3",
            "marine_fuel_4",
            "marine_fuel_5",
            "marine_other",
            "merchandise",
            "mid_plus",
            "mid_plus_2",
            "mid_plus_2_10",
            "mid_plus_2_e15",
            "mid_plus_2_reformulated",
            "mid_plus_e10",
            "mid_plus_e15",
            "mid_plus_ethanol",
            "mid_plus_reformulated",
            "miscellaneous_aviation_products_services",
            "miscellaneous_fuel",
            "miscellaneous_marine_products_services",
            "miscellaneous_vehicle_products_services",
            "motor_oil",
            "off_road_b1",
            "off_road_b10",
            "off_road_b100",
            "off_road_b11",
            "off_road_b15",
            "off_road_b2",
            "off_road_b20",
            "off_road_b5",
            "off_road_b75",
            "off_road_b99",
            "off_road_biodiesel",
            "off_road_diesel_1",
            "off_road_diesel_2",
            "off_road_mid_plus",
            "off_road_mid_plus_2",
            "off_road_premium_diesel_1",
            "off_road_premium_diesel_2",
            "off_road_premium_super",
            "off_road_premium_super_2",
            "off_road_regular",
            "off_road_renewable_diesel_b6_to_b20",
            "off_road_renewable_diesel_r95",
            "oil_change",
            "oil_filter",
            "other_lubricants",
            "packaged_beverage",
            "premium_diesel",
            "premium_diesel_2",
            "premium_diesel_b20_plus",
            "premium_diesel_under_b20",
            "premium_super",
            "premium_super_2",
            "premium_super_2_10",
            "premium_super_2_e15",
            "premium_super_2_reformulated",
            "premium_super_e10",
            "premium_super_e15",
            "premium_super_ethanol",
            "premium_super_reformulated",
            "preventative_maintenance",
            "racing_fuel",
            "recreational_fuel_90_octane",
            "regular",
            "regular_diesel",
            "regular_diesel_2",
            "regular_e10",
            "regular_e15",
            "regular_ethanol",
            "regular_reformulated",
            "renewable_diesel_b6_to_b20",
            "renewable_diesel_r95",
            "repairs",
            "road_service",
            "rv_dump_fee",
            "scales",
            "self_service_car_wash",
            "service_package",
            "shower",
            "store_service",
            "synthetic_oil",
            "tire_related",
            "tire_repair",
            "tire_rotation",
            "tires",
            "tobacco",
            "toll_payments",
            "towing",
            "trailer_wash",
            "transmission_service",
            "truck_tank_cleaning",
            "vehicle_accessories",
            "vehicle_glass",
            "vehicle_parking",
            "vehicle_parts",
            "vehicle_prep",
            "vehicle_rental",
            "vehicle_work_order",
            "wash_out",
            "washer_fluid",
            "white_gas",
            "wipers",
        ],
        str,
    ]
    """
    The type of product being purchased at this line item.
    """
    service_type: NotRequired[
        "Literal['full_service', 'high_speed_diesel', 'non_fuel_only', 'self_service']|str"
    ]
    """
    The type of service received at the acceptor location.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsCardPresent(
    TypedDict,
):
    commodity_code: NotRequired[str]
    """
    Identifier that categorizes the items being purchased using a standardized commodity scheme such as (but not limited to) UNSPSC, NAICS, NAPCS, and so on.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsKlarna(
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


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemPaymentMethodOptionsPaypal(
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


class PaymentIntentDecrementAuthorizationParamsAmountDetailsLineItemTax(
    TypedDict,
):
    total_tax_amount: int
    """
    The total amount of tax on a single line item represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L3 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[tax][total_tax_amount]` field.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsShipping(
    TypedDict
):
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


class PaymentIntentDecrementAuthorizationParamsAmountDetailsSurcharge(
    TypedDict,
):
    amount: NotRequired["Literal['']|int"]
    """
    Portion of the amount that corresponds to a surcharge.
    """
    enforce_validation: NotRequired[
        "Literal['']|Literal['automatic', 'disabled', 'enabled']|str"
    ]
    """
    Indicate whether to enforce validations on the surcharge amount.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsTax(TypedDict):
    total_tax_amount: int
    """
    The total amount of tax on the transaction represented in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Required for L2 rates. An integer greater than or equal to 0.

    This field is mutually exclusive with the `amount_details[line_items][#][tax][total_tax_amount]` field.
    """


class PaymentIntentDecrementAuthorizationParamsAmountDetailsTip(TypedDict):
    amount: NotRequired["Literal['']|int"]
    """
    Portion of the amount that corresponds to a tip.
    """


class PaymentIntentDecrementAuthorizationParamsHooks(TypedDict):
    inputs: NotRequired["PaymentIntentDecrementAuthorizationParamsHooksInputs"]
    """
    Arguments passed in automations
    """


class PaymentIntentDecrementAuthorizationParamsHooksInputs(TypedDict):
    tax: NotRequired["PaymentIntentDecrementAuthorizationParamsHooksInputsTax"]
    """
    Tax arguments for automations
    """


class PaymentIntentDecrementAuthorizationParamsHooksInputsTax(TypedDict):
    calculation: Union[Literal[""], str]
    """
    The [TaxCalculation](https://docs.stripe.com/api/tax/calculations) id
    """


class PaymentIntentDecrementAuthorizationParamsPaymentDetails(TypedDict):
    customer_reference: NotRequired["Literal['']|str"]
    """
    A unique value to identify the customer. This field is available only for card payments.

    This field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks.
    """
    order_reference: NotRequired["Literal['']|str"]
    """
    A unique value assigned by the business to identify the transaction. Required for L2 and L3 rates.

    For Cards, this field is truncated to 25 alphanumeric characters, excluding spaces, before being sent to card networks. For Klarna, this field is truncated to 255 characters and is visible to customers when they view the order in the Klarna app.
    """


class PaymentIntentDecrementAuthorizationParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    """
