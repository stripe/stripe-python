# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import Literal, Type, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe.issuing._card import Card
    from stripe.issuing._cardholder import Cardholder
    from stripe.issuing._token import Token
    from stripe.issuing._transaction import Transaction
    from stripe.params.issuing._authorization_approve_params import (
        AuthorizationApproveParams,
    )
    from stripe.params.issuing._authorization_capture_params import (
        AuthorizationCaptureParams,
    )
    from stripe.params.issuing._authorization_create_params import (
        AuthorizationCreateParams,
    )
    from stripe.params.issuing._authorization_decline_params import (
        AuthorizationDeclineParams,
    )
    from stripe.params.issuing._authorization_expire_params import (
        AuthorizationExpireParams,
    )
    from stripe.params.issuing._authorization_finalize_amount_params import (
        AuthorizationFinalizeAmountParams,
    )
    from stripe.params.issuing._authorization_increment_params import (
        AuthorizationIncrementParams,
    )
    from stripe.params.issuing._authorization_list_params import (
        AuthorizationListParams,
    )
    from stripe.params.issuing._authorization_modify_params import (
        AuthorizationModifyParams,
    )
    from stripe.params.issuing._authorization_respond_params import (
        AuthorizationRespondParams,
    )
    from stripe.params.issuing._authorization_retrieve_params import (
        AuthorizationRetrieveParams,
    )
    from stripe.params.issuing._authorization_reverse_params import (
        AuthorizationReverseParams,
    )


class Authorization(
    ListableAPIResource["Authorization"],
    UpdateableAPIResource["Authorization"],
):
    """
    When an [issued card](https://docs.stripe.com/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://docs.stripe.com/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://docs.stripe.com/issuing/purchases/authorizations)
    """

    OBJECT_NAME: ClassVar[Literal["issuing.authorization"]] = (
        "issuing.authorization"
    )

    class AmountDetails(StripeObject):
        atm_fee: Optional[int]
        """
        The fee charged by the ATM for the cash withdrawal.
        """
        cashback_amount: Optional[int]
        """
        The amount of cash requested by the cardholder.
        """

    class BalanceResponse(StripeObject):
        account_type: Literal[
            "checking", "credit", "default", "other", "savings", "universal"
        ]
        """
        The cardholder account type affected by this authorization.
        """
        available_balance: int
        """
        The available balance or credit limit in the cardholder's account after the authorization, in the smallest currency unit.
        """
        currency: str
        """
        The currency of the remaining balances in the cardholder's account after the authorization.
        """
        current_balance: int
        """
        The current ledger balance or remaining credit amount in the cardholder's account after the authorization, in the smallest currency unit.
        """

    class CryptoTransaction(StripeObject):
        class CryptoTransactionConfirmed(StripeObject):
            class Fee(StripeObject):
                amount: str
                """
                The fee amount.
                """
                currency: str
                """
                The fee currency.
                """
                type: str
                """
                The fee type.
                """

            amount: str
            """
            The crypto amount for the confirmed transaction.
            """
            amount_mcc_upcharged: Optional[str]
            """
            The upcharged MCC amount, if one was applied.
            """
            chain: str
            """
            The blockchain network for the confirmed transaction.
            """
            confirmed_at: int
            """
            When the transaction was confirmed onchain.
            """
            currency: str
            """
            The currency of the crypto transaction amount.
            """
            fees: List[Fee]
            """
            Fees associated with the transaction.
            """
            from_address: str
            """
            The source wallet address for the transaction.
            """
            memo: Optional[str]
            """
            Memo metadata attached to the transaction, if present.
            """
            to_address: str
            """
            The destination wallet address for the transaction.
            """
            transaction_hash: str
            """
            The blockchain transaction hash.
            """
            _inner_class_types = {"fees": Fee}

        class CryptoTransactionFailed(StripeObject):
            class Fee(StripeObject):
                amount: str
                """
                The fee amount.
                """
                currency: str
                """
                The fee currency.
                """
                type: str
                """
                The fee type.
                """

            amount: str
            """
            The crypto amount for the failed transaction.
            """
            amount_mcc_upcharged: Optional[str]
            """
            The upcharged MCC amount, if one was applied.
            """
            chain: str
            """
            The blockchain network for the failed transaction.
            """
            currency: str
            """
            The currency of the crypto transaction amount.
            """
            failed_at: int
            """
            When the transaction failed.
            """
            failure_reason: str
            """
            The reason the transaction failed.
            """
            fees: List[Fee]
            """
            Fees associated with the transaction.
            """
            from_address: str
            """
            The source wallet address for the attempted transaction.
            """
            memo: Optional[str]
            """
            Memo metadata attached to the transaction, if present.
            """
            to_address: Optional[str]
            """
            The destination wallet address for the attempted transaction when one exists.
            """
            transaction_hash: Optional[str]
            """
            The blockchain transaction hash when one exists.
            """
            _inner_class_types = {"fees": Fee}

        crypto_transaction_confirmed: Optional[CryptoTransactionConfirmed]
        """
        The confirmed crypto transaction details when `type` is `crypto_transaction_confirmed`; otherwise null.
        """
        crypto_transaction_failed: Optional[CryptoTransactionFailed]
        """
        The failed crypto transaction details when `type` is `crypto_transaction_failed`; otherwise null.
        """
        type: str
        """
        The crypto transaction variant for this array entry.
        """
        _inner_class_types = {
            "crypto_transaction_confirmed": CryptoTransactionConfirmed,
            "crypto_transaction_failed": CryptoTransactionFailed,
        }

    class EnrichedMerchantData(StripeObject):
        class Merchant(StripeObject):
            class Industry(StripeObject):
                id: Literal[
                    "accessories",
                    "accounting_and_bookkeeping",
                    "acupuncture",
                    "administrative_services",
                    "adult_entertainment",
                    "adult_retail",
                    "advertising_and_marketing",
                    "advertising_technology",
                    "agricultural_technology",
                    "agriculture_and_forestry",
                    "airlines_and_aviation",
                    "alternative_medicine",
                    "alternative_rentals",
                    "anesthesiologists",
                    "antiques",
                    "aquatic_transportation",
                    "arcades_and_amusement_parks",
                    "art_dealers_and_galleries",
                    "arts_and_hobbies",
                    "atms",
                    "auctions",
                    "auto_parts_and_supplies",
                    "auto_smog_checks",
                    "auto_tires",
                    "auto_transmission",
                    "automotive_dealerships",
                    "automotive_retail",
                    "automotive_services",
                    "bakeries",
                    "banking_and_finance",
                    "bars",
                    "beauty_spas_and_salons",
                    "beer_wine_and_spirits",
                    "benefits",
                    "bicycles",
                    "billiards_and_pool",
                    "biotechnology",
                    "blood_banks_and_centers",
                    "boat_dealers",
                    "bookstores",
                    "bowling",
                    "breweries_distilleries_and_wineries",
                    "business_brokers_and_franchises",
                    "business_services",
                    "butchers",
                    "buy_now_pay_later",
                    "cafes",
                    "candy_shops",
                    "cannabis_dispensary",
                    "car_appraisers",
                    "car_wash_and_detail",
                    "cardiologists",
                    "cards_and_stationery",
                    "casinos_and_gambling",
                    "catering",
                    "charity",
                    "childcare",
                    "children_s_clothing",
                    "children_s_retail",
                    "chiropractors",
                    "circuses_and_carnivals",
                    "cleaning",
                    "clothing_and_accessories",
                    "clothing_services",
                    "commercial_supplies",
                    "communication_software",
                    "computers_and_electronics",
                    "construction_and_home_improvement",
                    "construction_supplies",
                    "contractors",
                    "convenience_stores",
                    "cosmetics",
                    "costumes",
                    "counseling_and_therapy",
                    "couriers",
                    "coworking_spaces",
                    "creative",
                    "creative_software",
                    "credit_reporting",
                    "crm",
                    "crowdfunding",
                    "cryptocurrency",
                    "dance_halls_and_saloons",
                    "delivery_services",
                    "dentists",
                    "department_stores",
                    "dermatologists",
                    "design_technology",
                    "developer_tools",
                    "digital_money_movement",
                    "discount_stores",
                    "education",
                    "educational_technology",
                    "electric_vehicle_charging",
                    "emergency_services",
                    "employment_services",
                    "enterprise_software",
                    "entertainment",
                    "ents",
                    "environmental_technology",
                    "equipment_rentals",
                    "events_and_event_planning",
                    "eyewear",
                    "fairgrounds_and_rodeos",
                    "family_medicine",
                    "fast_food",
                    "fertility",
                    "financial_management_software",
                    "financial_planning_and_investments",
                    "financial_technology",
                    "fishmongers",
                    "flea_markets",
                    "fleet",
                    "florists",
                    "food_and_drink",
                    "food_delivery_services",
                    "food_trucks",
                    "fuel_dealers",
                    "funeral_services",
                    "furniture",
                    "gas_stations",
                    "gastroenterologists",
                    "general_goods",
                    "general_surgery",
                    "gift_and_novelty",
                    "government",
                    "grocery_delivery_services",
                    "gyms_health_and_fitness_centers",
                    "hair_removal",
                    "hair_salons_and_barbers",
                    "hardware",
                    "hardware_and_home_improvement",
                    "hospitals_clinics_and_medical_centers",
                    "household_services",
                    "hr_platform",
                    "immigration",
                    "import_and_export",
                    "industrial_and_energy",
                    "inflight_internet_and_entertainment",
                    "insurance",
                    "internal_medicine",
                    "internet",
                    "jewelry_and_watches",
                    "landmarks",
                    "laundry_and_garment_services",
                    "lawn_and_garden",
                    "legal_services",
                    "legal_technology",
                    "lending",
                    "lingerie",
                    "lodging",
                    "luggage",
                    "maintenance_and_repair",
                    "manicures_and_pedicures",
                    "manufacturing",
                    "marina",
                    "marine_supplies",
                    "marketing_software",
                    "massage_clinics_and_therapists",
                    "media",
                    "medical_and_healthcare_services",
                    "medical_supplies_and_labs",
                    "men_s_clothing",
                    "mental_health_professionals",
                    "mobile_applications",
                    "motorcycle_moped_and_scooter_repair",
                    "museums",
                    "musical_instruments",
                    "neurologists",
                    "news_and_magazines",
                    "newsstands",
                    "nutritionists",
                    "obstetricians_and_gynecologists",
                    "office_supplies",
                    "oil_and_gas",
                    "oncologists",
                    "online_marketplace",
                    "ophthalmologists",
                    "optometrists",
                    "organizations",
                    "orthopedic_surgeons",
                    "other",
                    "outlets",
                    "packaging",
                    "paper",
                    "parking",
                    "parks_and_outdoors",
                    "party_centers",
                    "pathologists",
                    "pawn_shops",
                    "pediatricians",
                    "pet_grooming",
                    "pet_services",
                    "pets",
                    "pharmacies",
                    "photography",
                    "physical_therapy",
                    "piercings",
                    "plastic_surgeons",
                    "podiatrists",
                    "pregnancy_and_sexual_health",
                    "professional_services",
                    "property_management",
                    "psychiatrists",
                    "psychics_and_astrologers",
                    "psychologists",
                    "public_services",
                    "public_transportation",
                    "publishing_software",
                    "radiologists",
                    "rails",
                    "real_estate",
                    "recreation",
                    "religious",
                    "renewable_energy",
                    "respiratory",
                    "restaurants",
                    "retail",
                    "ride_shares",
                    "sales_enablement_software",
                    "security_and_privacy",
                    "security_and_safety",
                    "services",
                    "shipping_and_freight",
                    "shoes",
                    "skin_care",
                    "social_clubs",
                    "software",
                    "software_engineering",
                    "spas",
                    "specialist_physicans",
                    "specialty_clothing_and_accessories",
                    "specialty_foods",
                    "specialty_groceries",
                    "specialty_retail",
                    "sporting_goods",
                    "storage",
                    "streaming_services",
                    "supermarkets_and_grocery_stores",
                    "swimwear",
                    "tailors",
                    "tanning_salons",
                    "tattoos",
                    "taxes",
                    "taxi_and_limousines",
                    "technology",
                    "telecommunications",
                    "television",
                    "textiles",
                    "theater_and_cinema",
                    "tickets_and_reservations",
                    "tobacco_smoke_and_vape_shops",
                    "tolls_and_fees",
                    "tourist_information_and_services",
                    "towing_and_roadside_assistance",
                    "toy_stores",
                    "transportation",
                    "travel",
                    "travel_services",
                    "travel_software",
                    "urologists",
                    "utilities",
                    "vehicle_rentals",
                    "vending_machine",
                    "venues",
                    "veterinarians",
                    "video_games",
                    "vintage_and_thrift",
                    "warehouses_and_wholesale_stores",
                    "water_and_waste_management_services",
                    "web_infrastructure",
                    "wedding_and_bridal",
                    "women_s_clothing",
                    "zoos_and_aquariums",
                ]
                """
                Most specific value of the seller's category.
                """
                names: List[str]
                """
                Increasingly specific textual representations of the seller's category.
                """

            class Location(StripeObject):
                class Address(StripeObject):
                    city: Optional[str]
                    """
                    City, district, suburb, town, or village.
                    """
                    country: str
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

                class Coordinates(StripeObject):
                    latitude: Optional[float]
                    """
                    Latitude of the seller's location.
                    """
                    longitude: Optional[float]
                    """
                    Longitude of the seller's location.
                    """

                address: Optional[Address]
                """
                Address details of the seller.
                """
                coordinates: Optional[Coordinates]
                """
                Coordinates of the seller.
                """
                _inner_class_types = {
                    "address": Address,
                    "coordinates": Coordinates,
                }

            class Spade(StripeObject):
                counterparty_id: Optional[str]
                """
                Unified identifier for the seller.
                """
                location_id: Optional[str]
                """
                Unified identifier for the seller's location.
                """

            data_sources: List[Literal["spade"]]
            industry: Industry
            location: Optional[Location]
            """
            Location data of the seller.
            """
            logo: Optional[str]
            """
            Image link to the seller's logo.
            """
            name: Optional[str]
            """
            The name of the seller.
            """
            phone: Optional[str]
            """
            Phone number of the seller.
            """
            spade: Optional[Spade]
            """
            If `spade` is a data source, this hash contains details provided by Spade.
            """
            url: Optional[str]
            """
            URL of the seller's website.
            """
            _inner_class_types = {
                "industry": Industry,
                "location": Location,
                "spade": Spade,
            }

        class ThirdParty(StripeObject):
            class Spade(StripeObject):
                third_party_id: Optional[str]
                """
                Unified identifier for the third party.
                """

            data_sources: List[Literal["spade"]]
            logo: Optional[str]
            """
            Image link to the third party's logo.
            """
            name: Optional[str]
            """
            Name of the third party.
            """
            spade: Optional[Spade]
            """
            If `spade` is a data source, this hash contains details provided by Spade.
            """
            type: Literal[
                "buy_now_pay_later",
                "delivery_service",
                "marketplace",
                "other",
                "payment_processor",
                "platform",
            ]
            """
            Category of the third party.
            """
            _inner_class_types = {"spade": Spade}

        merchant: Optional[Merchant]
        """
        Additional details about the seller (grocery store, e-commerce website, and so on) where the card authorization happened.
        """
        third_parties: Optional[List[ThirdParty]]
        """
        An array of third parties involved in the card authorization, when applicable.
        """
        _inner_class_types = {
            "merchant": Merchant,
            "third_parties": ThirdParty,
        }

    class Fleet(StripeObject):
        class CardholderPromptData(StripeObject):
            alphanumeric_id: Optional[str]
            """
            [Deprecated] An alphanumeric ID, though typical point of sales only support numeric entry. The card program can be configured to prompt for a vehicle ID, driver ID, or generic ID.
            """
            driver_id: Optional[str]
            """
            Driver ID.
            """
            odometer: Optional[int]
            """
            Odometer reading.
            """
            unspecified_id: Optional[str]
            """
            An alphanumeric ID. This field is used when a vehicle ID, driver ID, or generic ID is entered by the cardholder, but the merchant or card network did not specify the prompt type.
            """
            user_id: Optional[str]
            """
            User ID.
            """
            vehicle_number: Optional[str]
            """
            Vehicle number.
            """

        class ReportedBreakdown(StripeObject):
            class Fuel(StripeObject):
                gross_amount_decimal: Optional[Decimal]
                """
                Gross fuel amount that should equal Fuel Quantity multiplied by Fuel Unit Cost, inclusive of taxes.
                """
                _field_encodings = {"gross_amount_decimal": "decimal_string"}

            class NonFuel(StripeObject):
                gross_amount_decimal: Optional[Decimal]
                """
                Gross non-fuel amount that should equal the sum of the line items, inclusive of taxes.
                """
                _field_encodings = {"gross_amount_decimal": "decimal_string"}

            class Tax(StripeObject):
                local_amount_decimal: Optional[Decimal]
                """
                Amount of state or provincial Sales Tax included in the transaction amount. `null` if not reported by merchant or not subject to tax.
                """
                national_amount_decimal: Optional[Decimal]
                """
                Amount of national Sales Tax or VAT included in the transaction amount. `null` if not reported by merchant or not subject to tax.
                """
                _field_encodings = {
                    "local_amount_decimal": "decimal_string",
                    "national_amount_decimal": "decimal_string",
                }

            fuel: Optional[Fuel]
            """
            Breakdown of fuel portion of the purchase.
            """
            non_fuel: Optional[NonFuel]
            """
            Breakdown of non-fuel portion of the purchase.
            """
            tax: Optional[Tax]
            """
            Information about tax included in this transaction.
            """
            _inner_class_types = {
                "fuel": Fuel,
                "non_fuel": NonFuel,
                "tax": Tax,
            }

        cardholder_prompt_data: Optional[CardholderPromptData]
        """
        Answers to prompts presented to the cardholder at the point of sale. Prompted fields vary depending on the configuration of your physical fleet cards. Typical points of sale support only numeric entry.
        """
        purchase_type: Optional[
            Literal[
                "fuel_and_non_fuel_purchase",
                "fuel_purchase",
                "non_fuel_purchase",
            ]
        ]
        """
        The type of purchase.
        """
        reported_breakdown: Optional[ReportedBreakdown]
        """
        More information about the total amount. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed. This information is not guaranteed to be accurate as some merchants may provide unreliable data.
        """
        service_type: Optional[
            Literal["full_service", "non_fuel_transaction", "self_service"]
        ]
        """
        The type of fuel service.
        """
        _inner_class_types = {
            "cardholder_prompt_data": CardholderPromptData,
            "reported_breakdown": ReportedBreakdown,
        }

    class FraudChallenge(StripeObject):
        channel: Literal["sms"]
        """
        The method by which the fraud challenge was delivered to the cardholder.
        """
        status: Literal[
            "expired", "pending", "rejected", "undeliverable", "verified"
        ]
        """
        The status of the fraud challenge.
        """
        undeliverable_reason: Optional[
            Literal["no_phone_number", "unsupported_phone_number"]
        ]
        """
        If the challenge is not deliverable, the reason why.
        """

    class Fuel(StripeObject):
        industry_product_code: Optional[str]
        """
        [Conexxus Payment System Product Code](https://www.conexxus.org/conexxus-payment-system-product-codes) identifying the primary fuel product purchased.
        """
        quantity_decimal: Optional[Decimal]
        """
        The quantity of `unit`s of fuel that was dispensed, represented as a decimal string with at most 12 decimal places.
        """
        type: Optional[
            Literal[
                "diesel",
                "other",
                "unleaded_plus",
                "unleaded_regular",
                "unleaded_super",
            ]
        ]
        """
        The type of fuel that was purchased.
        """
        unit: Optional[
            Literal[
                "charging_minute",
                "imperial_gallon",
                "kilogram",
                "kilowatt_hour",
                "liter",
                "other",
                "pound",
                "us_gallon",
            ]
        ]
        """
        The units for `quantity_decimal`.
        """
        unit_cost_decimal: Optional[Decimal]
        """
        The cost in cents per each unit of fuel, represented as a decimal string with at most 12 decimal places.
        """
        _field_encodings = {
            "quantity_decimal": "decimal_string",
            "unit_cost_decimal": "decimal_string",
        }

    class MerchantData(StripeObject):
        category: str
        """
        A categorization of the seller's type of business. See our [merchant categories guide](https://docs.stripe.com/issuing/merchant-categories) for a list of possible values.
        """
        category_code: str
        """
        The merchant category code for the seller's business
        """
        city: Optional[str]
        """
        City where the seller is located
        """
        country: Optional[str]
        """
        Country where the seller is located
        """
        name: Optional[str]
        """
        Name of the seller
        """
        network_id: str
        """
        Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.
        """
        payment_facilitator_id: Optional[str]
        """
        The identifier of the payment facilitator (PayFac) that processed this authorization, as assigned by the card network. Null when the transaction was not processed through a PayFac.
        """
        postal_code: Optional[str]
        """
        Postal code where the seller is located
        """
        state: Optional[str]
        """
        State where the seller is located
        """
        sub_merchant_id: Optional[str]
        """
        The identifier of the sub-merchant involved in this authorization, as assigned by the payment facilitator. Null when the transaction was not processed through a PayFac or when no sub-merchant ID was provided.
        """
        tax_id: Optional[str]
        """
        The seller's tax identification number. Currently populated for French merchants only.
        """
        terminal_id: Optional[str]
        """
        An ID assigned by the seller to the location of the sale.
        """
        url: Optional[str]
        """
        URL provided by the merchant on a 3DS request
        """

    class NetworkData(StripeObject):
        acquiring_institution_id: Optional[str]
        """
        Identifier assigned to the acquirer by the card network. Sometimes this value is not provided by the network; in this case, the value will be `null`.
        """
        system_trace_audit_number: Optional[str]
        """
        The System Trace Audit Number (STAN) is a 6-digit identifier assigned by the acquirer. Prefer `network_data.transaction_id` if present, unless you have special requirements.
        """
        transaction_id: Optional[str]
        """
        Unique identifier for the authorization assigned by the card network used to match subsequent messages, disputes, and transactions.
        """

    class PendingRequest(StripeObject):
        class AmountDetails(StripeObject):
            atm_fee: Optional[int]
            """
            The fee charged by the ATM for the cash withdrawal.
            """
            cashback_amount: Optional[int]
            """
            The amount of cash requested by the cardholder.
            """

        amount: int
        """
        The additional amount Stripe will hold if the authorization is approved, in the card's [currency](https://docs.stripe.com/api#issuing_authorization_object-pending-request-currency) and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
        """
        amount_details: Optional[AmountDetails]
        """
        Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        is_amount_controllable: bool
        """
        If set `true`, you may provide [amount](https://docs.stripe.com/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
        """
        merchant_amount: int
        """
        The amount the merchant is requesting to be authorized in the `merchant_currency`. The amount is in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
        """
        merchant_currency: str
        """
        The local currency the merchant is requesting to authorize.
        """
        network_risk_score: Optional[int]
        """
        The card network's estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.
        """
        _inner_class_types = {"amount_details": AmountDetails}

    class Redaction(StripeObject):
        status: Literal["processing", "redacted", "validated"]
        """
        Indicates whether this object and its related objects have been redacted or not.
        """

    class RequestHistory(StripeObject):
        class AmountDetails(StripeObject):
            atm_fee: Optional[int]
            """
            The fee charged by the ATM for the cash withdrawal.
            """
            cashback_amount: Optional[int]
            """
            The amount of cash requested by the cardholder.
            """

        amount: int
        """
        The `pending_request.amount` at the time of the request, presented in your card's currency and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal). Stripe held this amount from your account to fund the authorization if the request was approved.
        """
        amount_details: Optional[AmountDetails]
        """
        Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
        """
        approved: bool
        """
        Whether this request was approved.
        """
        authorization_code: Optional[str]
        """
        A code created by Stripe which is shared with the merchant to validate the authorization. This field will be populated if the authorization message was approved. The code typically starts with the letter "S", followed by a six-digit number. For example, "S498162". Please note that the code is not guaranteed to be unique across authorizations.
        """
        created: int
        """
        Time at which the object was created. Measured in seconds since the Unix epoch.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        merchant_amount: int
        """
        The `pending_request.merchant_amount` at the time of the request, presented in the `merchant_currency` and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
        """
        merchant_currency: str
        """
        The currency that was collected by the merchant and presented to the cardholder for the authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        network_risk_score: Optional[int]
        """
        The card network's estimate of the likelihood that an authorization is fraudulent. Takes on values between 1 and 99.
        """
        reason: Literal[
            "account_disabled",
            "card_active",
            "card_canceled",
            "card_expired",
            "card_inactive",
            "cardholder_blocked",
            "cardholder_inactive",
            "cardholder_verification_required",
            "insecure_authorization_method",
            "insufficient_funds",
            "network_fallback",
            "not_allowed",
            "pin_blocked",
            "spending_controls",
            "suspected_fraud",
            "verification_failed",
            "webhook_approved",
            "webhook_declined",
            "webhook_error",
            "webhook_timeout",
        ]
        """
        When an authorization is approved or declined by you or by Stripe, this field provides additional detail on the reason for the outcome.
        """
        reason_message: Optional[str]
        """
        If the `request_history.reason` is `webhook_error` because the direct webhook response is invalid (for example, parsing errors or missing parameters), we surface a more detailed error message via this field.
        """
        requested_at: Optional[int]
        """
        Time when the card network received an authorization request from the acquirer in UTC. Referred to by networks as transmission time.
        """
        _inner_class_types = {"amount_details": AmountDetails}

    class TokenDetails(StripeObject):
        class NetworkData(StripeObject):
            class Device(StripeObject):
                device_id: Optional[str]
                """
                An identifier for the device used during wallet provisioning.
                """
                ip_address: Optional[str]
                """
                The IP address of the device at provisioning time.
                """
                language: Optional[
                    Literal[
                        "aa",
                        "ab",
                        "ae",
                        "af",
                        "ak",
                        "am",
                        "an",
                        "ar",
                        "as",
                        "av",
                        "ay",
                        "az",
                        "ba",
                        "be",
                        "bg",
                        "bi",
                        "bm",
                        "bn",
                        "bo",
                        "br",
                        "bs",
                        "ca",
                        "ce",
                        "ch",
                        "co",
                        "cr",
                        "cs",
                        "cu",
                        "cv",
                        "cy",
                        "da",
                        "de",
                        "dv",
                        "dz",
                        "ee",
                        "el",
                        "en",
                        "eo",
                        "es",
                        "et",
                        "eu",
                        "fa",
                        "ff",
                        "fi",
                        "fj",
                        "fo",
                        "fr",
                        "fy",
                        "ga",
                        "gd",
                        "gl",
                        "gn",
                        "gu",
                        "gv",
                        "ha",
                        "he",
                        "hi",
                        "ho",
                        "hr",
                        "ht",
                        "hu",
                        "hy",
                        "hz",
                        "ia",
                        "id",
                        "ie",
                        "ig",
                        "ii",
                        "ik",
                        "io",
                        "is",
                        "it",
                        "iu",
                        "ja",
                        "jv",
                        "ka",
                        "kg",
                        "ki",
                        "kj",
                        "kk",
                        "kl",
                        "km",
                        "kn",
                        "ko",
                        "kr",
                        "ks",
                        "ku",
                        "kv",
                        "kw",
                        "ky",
                        "la",
                        "lb",
                        "lg",
                        "li",
                        "ln",
                        "lo",
                        "lt",
                        "lu",
                        "lv",
                        "mg",
                        "mh",
                        "mi",
                        "mk",
                        "ml",
                        "mn",
                        "mr",
                        "ms",
                        "mt",
                        "my",
                        "na",
                        "nb",
                        "nd",
                        "ne",
                        "ng",
                        "nl",
                        "nn",
                        "no",
                        "nr",
                        "nv",
                        "ny",
                        "oc",
                        "oj",
                        "om",
                        "or",
                        "os",
                        "pa",
                        "pi",
                        "pl",
                        "ps",
                        "pt",
                        "qu",
                        "rm",
                        "rn",
                        "ro",
                        "ru",
                        "rw",
                        "sa",
                        "sc",
                        "sd",
                        "se",
                        "sg",
                        "si",
                        "sk",
                        "sl",
                        "sm",
                        "sn",
                        "so",
                        "sq",
                        "sr",
                        "ss",
                        "st",
                        "su",
                        "sv",
                        "sw",
                        "ta",
                        "te",
                        "tg",
                        "th",
                        "ti",
                        "tk",
                        "tl",
                        "tn",
                        "to",
                        "tr",
                        "ts",
                        "tt",
                        "tw",
                        "ty",
                        "ug",
                        "uk",
                        "ur",
                        "uz",
                        "ve",
                        "vi",
                        "vo",
                        "wa",
                        "wo",
                        "xh",
                        "yi",
                        "yo",
                        "za",
                        "zh",
                        "zu",
                    ]
                ]
                """
                The ISO 639-1 language code of the device associated with the tokenization request.
                """
                phone_number: Optional[str]
                """
                The phone number of the device used for tokenization.
                """

            class Mastercard(StripeObject):
                card_reference_id: Optional[str]
                """
                A unique reference ID from the network to represent the card account number.
                """
                token_reference_id: str
                """
                The network-unique identifier for the token.
                """
                token_requestor_id: str
                """
                The ID of the entity requesting tokenization.
                """

            class Visa(StripeObject):
                card_reference_id: Optional[str]
                """
                A unique reference ID from the network to represent the card account number.
                """
                token_decision_recommendation: Optional[
                    Literal["approve", "decline", "recommend_id_and_v"]
                ]
                """
                The network's recommendation to Stripe for this token activation request.
                """
                token_reference_id: str
                """
                The network-unique identifier for the token.
                """
                token_requestor_id: str
                """
                The ID of the entity requesting tokenization.
                """
                token_risk_score: Optional[str]
                """
                Degree of risk associated with the token between `01` and `99`, with higher number indicating higher risk. A `00` value indicates the token was not scored by Visa.
                """

            class WalletProvider(StripeObject):
                account_trust_score: Optional[int]
                """
                An evaluation on the trustworthiness of the wallet account between 1 and 5. A higher score indicates more trustworthy.
                """
                card_number_source: Optional[
                    Literal["app", "manual", "on_file", "other"]
                ]
                """
                The method used for tokenizing a card.
                """
                device_trust_score: Optional[int]
                """
                An evaluation on the trustworthiness of the device. A higher score indicates more trustworthy.
                """
                reason_codes: Optional[
                    List[
                        Literal[
                            "account_card_too_new",
                            "account_recently_changed",
                            "account_too_new",
                            "account_too_new_since_launch",
                            "additional_device",
                            "data_expired",
                            "defer_id_v_decision",
                            "device_recently_lost",
                            "good_activity_history",
                            "has_suspended_tokens",
                            "high_risk",
                            "inactive_account",
                            "long_account_tenure",
                            "low_account_score",
                            "low_device_score",
                            "low_phone_number_score",
                            "network_service_error",
                            "outside_home_territory",
                            "provisioning_cardholder_mismatch",
                            "provisioning_device_and_cardholder_mismatch",
                            "provisioning_device_mismatch",
                            "same_device_no_prior_authentication",
                            "same_device_successful_prior_authentication",
                            "software_update",
                            "suspicious_activity",
                            "too_many_different_cardholders",
                            "too_many_recent_attempts",
                            "too_many_recent_tokens",
                        ]
                    ]
                ]
                """
                The reasons for suggested tokenization given by the card network.
                """
                suggested_decision: Optional[
                    Literal["approve", "decline", "require_auth"]
                ]
                """
                The recommendation on responding to the tokenization request.
                """

            device: Optional[Device]
            mastercard: Optional[Mastercard]
            type: Literal["mastercard", "visa"]
            """
            The card network for this token.
            """
            visa: Optional[Visa]
            wallet_provider: Optional[WalletProvider]
            _inner_class_types = {
                "device": Device,
                "mastercard": Mastercard,
                "visa": Visa,
                "wallet_provider": WalletProvider,
            }

        card: str
        """
        The card associated with this token.
        """
        created: int
        """
        Time at which the object was created. Measured in seconds since the Unix epoch.
        """
        device_fingerprint: Optional[str]
        """
        The hashed ID derived from the device ID from the card network associated with the token.
        """
        network_data: Optional[NetworkData]
        provisioning_decision: Optional[
            Literal["approve", "approve_pending_id_and_v", "decline"]
        ]
        """
        The decision made during token provisioning.
        """
        token_type: Optional[
            Literal[
                "card_on_file",
                "cloud_based",
                "commerce_platform",
                "commercial_virtual_account",
                "secure_element",
                "static_credential",
            ]
        ]
        """
        The type of the token, indicating how it is used.
        """
        _inner_class_types = {"network_data": NetworkData}

    class Treasury(StripeObject):
        received_credits: List[str]
        """
        The array of [ReceivedCredits](https://docs.stripe.com/api/treasury/received_credits) associated with this authorization
        """
        received_debits: List[str]
        """
        The array of [ReceivedDebits](https://docs.stripe.com/api/treasury/received_debits) associated with this authorization
        """
        transaction: Optional[str]
        """
        The Treasury [Transaction](https://docs.stripe.com/api/treasury/transactions) associated with this authorization
        """

    class VerificationData(StripeObject):
        class AuthenticationExemption(StripeObject):
            claimed_by: Literal["acquirer", "issuer"]
            """
            The entity that requested the exemption, either the acquiring merchant or the Issuing user.
            """
            type: Literal[
                "low_value_transaction", "transaction_risk_analysis", "unknown"
            ]
            """
            The specific exemption claimed for this authorization.
            """

        class ThreeDSecure(StripeObject):
            result: Literal[
                "attempt_acknowledged", "authenticated", "failed", "required"
            ]
            """
            The outcome of the 3D Secure authentication request.
            """

        address_line1_check: Literal["match", "mismatch", "not_provided"]
        """
        Whether the cardholder provided an address first line and if it matched the cardholder's `billing.address.line1`.
        """
        address_postal_code_check: Literal["match", "mismatch", "not_provided"]
        """
        Whether the cardholder provided a postal code and if it matched the cardholder's `billing.address.postal_code`.
        """
        authentication_exemption: Optional[AuthenticationExemption]
        """
        The exemption applied to this authorization.
        """
        cvc_check: Literal["match", "mismatch", "not_provided"]
        """
        Whether the cardholder provided a CVC and if it matched Stripe's record.
        """
        expiry_check: Literal["match", "mismatch", "not_provided"]
        """
        Whether the cardholder provided an expiry date and if it matched Stripe's record.
        """
        postal_code: Optional[str]
        """
        The postal code submitted as part of the authorization used for postal code verification.
        """
        three_d_secure: Optional[ThreeDSecure]
        """
        3D Secure details.
        """
        _inner_class_types = {
            "authentication_exemption": AuthenticationExemption,
            "three_d_secure": ThreeDSecure,
        }

    amount: int
    """
    The total amount that was authorized or rejected. This amount is in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `amount` should be the same as `merchant_amount`, unless `currency` and `merchant_currency` are different.
    """
    amount_details: Optional[AmountDetails]
    """
    Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """
    approved: bool
    """
    Whether the authorization has been approved.
    """
    authorization_method: Literal[
        "chip", "contactless", "keyed_in", "online", "swipe"
    ]
    """
    How the card details were provided.
    """
    balance_response: Optional[BalanceResponse]
    balance_transactions: List["BalanceTransaction"]
    """
    List of balance transactions associated with this authorization.
    """
    card: "Card"
    """
    You can [create physical or virtual cards](https://docs.stripe.com/issuing) that are issued to cardholders.
    """
    card_presence: Optional[Literal["not_present", "present"]]
    """
    Whether the card was present at the point of sale for the authorization.
    """
    cardholder: Optional[ExpandableField["Cardholder"]]
    """
    The cardholder to whom this authorization belongs.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    crypto_transactions: Optional[List[CryptoTransaction]]
    """
    Array of onchain crypto transactions linked to this resource.
    """
    currency: str
    """
    The currency of the cardholder. This currency can be different from the currency presented at authorization and the `merchant_currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    enriched_merchant_data: Optional[EnrichedMerchantData]
    """
    Enriched merchant data for this authorization.
    """
    fleet: Optional[Fleet]
    """
    Fleet-specific information for authorizations using Fleet cards.
    """
    fraud_challenges: Optional[List[FraudChallenge]]
    """
    Fraud challenges sent to the cardholder, if this authorization was declined for fraud risk reasons.
    """
    fuel: Optional[Fuel]
    """
    Information about fuel that was purchased with this transaction. Typically this information is received from the merchant after the authorization has been approved and the fuel dispensed.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    merchant_amount: int
    """
    The total amount that was authorized or rejected. This amount is in the `merchant_currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). `merchant_amount` should be the same as `amount`, unless `merchant_currency` and `currency` are different.
    """
    merchant_amount_exchange_rate: Optional[float]
    """
    The exchange rate used by the network to convert the `merchant_amount` to `amount`. The `merchant_amount` multiplied with this rate will equal to the `amount`.
    """
    merchant_currency: str
    """
    The local currency that was presented to the cardholder for the authorization. This currency can be different from the cardholder currency and the `currency` field on this authorization. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    merchant_data: MerchantData
    metadata: UntypedStripeObject[str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network_data: Optional[NetworkData]
    """
    Details about the authorization, such as identifiers, set by the card network.
    """
    object: Literal["issuing.authorization"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    pending_request: Optional[PendingRequest]
    """
    The pending authorization request. This field will only be non-null during an `issuing_authorization.request` webhook.
    """
    redaction: Optional[Redaction]
    """
    Redaction status of this authorization. If the authorization is not redacted, this field will be null.
    """
    request_history: List[RequestHistory]
    """
    History of every time a `pending_request` authorization was approved/declined, either by you directly or by Stripe (e.g. based on your spending_controls). If the merchant changes the authorization by performing an incremental authorization, you can look at this field to see the previous requests for the authorization. This field can be helpful in determining why a given authorization was approved/declined.
    """
    status: Literal["closed", "expired", "pending", "reversed"]
    """
    The current status of the authorization in its lifecycle.
    """
    token: Optional[ExpandableField["Token"]]
    """
    [Token](https://docs.stripe.com/api/issuing/tokens/object) object used for this authorization. If a network token was not used for this authorization, this field will be null.
    """
    token_details: Optional[TokenDetails]
    transactions: List["Transaction"]
    """
    List of [transactions](https://docs.stripe.com/api/issuing/transactions) associated with this authorization.
    """
    treasury: Optional[Treasury]
    """
    [Treasury](https://docs.stripe.com/api/treasury) details related to this authorization if it was created on a [FinancialAccount](https://docs.stripe.com/api/treasury/financial_accounts).
    """
    verification_data: VerificationData
    verified_by_fraud_challenge: Optional[bool]
    """
    Whether the authorization bypassed fraud risk checks because the cardholder has previously completed a fraud challenge on a similar high-risk authorization from the same merchant.
    """
    wallet: Optional[str]
    """
    The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized.
    """

    @classmethod
    def _cls_approve(
        cls, authorization: str, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            cls._static_request(
                "post",
                "/v1/issuing/authorizations/{authorization}/approve".format(
                    authorization=sanitize_id(authorization)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def approve(
        authorization: str, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @overload
    def approve(
        self, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @class_method_variant("_cls_approve")
    def approve(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/issuing/authorizations/{authorization}/approve".format(
                    authorization=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_approve_async(
        cls, authorization: str, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            await cls._static_request_async(
                "post",
                "/v1/issuing/authorizations/{authorization}/approve".format(
                    authorization=sanitize_id(authorization)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def approve_async(
        authorization: str, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @overload
    async def approve_async(
        self, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @class_method_variant("_cls_approve_async")
    async def approve_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthorizationApproveParams"]
    ) -> "Authorization":
        """
        [Deprecated] Approves a pending Issuing Authorization object. This request should be made within the timeout window of the [real-time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to approve an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/issuing/authorizations/{authorization}/approve".format(
                    authorization=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_decline(
        cls, authorization: str, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            cls._static_request(
                "post",
                "/v1/issuing/authorizations/{authorization}/decline".format(
                    authorization=sanitize_id(authorization)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def decline(
        authorization: str, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @overload
    def decline(
        self, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @class_method_variant("_cls_decline")
    def decline(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/issuing/authorizations/{authorization}/decline".format(
                    authorization=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_decline_async(
        cls, authorization: str, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            await cls._static_request_async(
                "post",
                "/v1/issuing/authorizations/{authorization}/decline".format(
                    authorization=sanitize_id(authorization)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def decline_async(
        authorization: str, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @overload
    async def decline_async(
        self, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        ...

    @class_method_variant("_cls_decline_async")
    async def decline_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthorizationDeclineParams"]
    ) -> "Authorization":
        """
        [Deprecated] Declines a pending Issuing Authorization object. This request should be made within the timeout window of the [real time authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations) flow.
        This method is deprecated. Instead, [respond directly to the webhook request to decline an authorization](https://docs.stripe.com/docs/issuing/controls/real-time-authorizations#authorization-handling).
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/issuing/authorizations/{authorization}/decline".format(
                    authorization=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["AuthorizationListParams"]
    ) -> ListObject["Authorization"]:
        """
        Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
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
        cls, **params: Unpack["AuthorizationListParams"]
    ) -> ListObject["Authorization"]:
        """
        Returns a list of Issuing Authorization objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
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
    def modify(
        cls, id: str, **params: Unpack["AuthorizationModifyParams"]
    ) -> "Authorization":
        """
        Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Authorization",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["AuthorizationModifyParams"]
    ) -> "Authorization":
        """
        Updates the specified Issuing Authorization object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Authorization",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["AuthorizationRetrieveParams"]
    ) -> "Authorization":
        """
        Retrieves an Issuing Authorization object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["AuthorizationRetrieveParams"]
    ) -> "Authorization":
        """
        Retrieves an Issuing Authorization object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    class TestHelpers(APIResourceTestHelpers["Authorization"]):
        _resource_cls: Type["Authorization"]

        @classmethod
        def _cls_capture(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationCaptureParams"],
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def capture(
            authorization: str, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            ...

        @overload
        def capture(
            self, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            ...

        @class_method_variant("_cls_capture")
        def capture(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_capture_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationCaptureParams"],
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def capture_async(
            authorization: str, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            ...

        @overload
        async def capture_async(
            self, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            ...

        @class_method_variant("_cls_capture_async")
        async def capture_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationCaptureParams"]
        ) -> "Authorization":
            """
            Capture a test-mode authorization.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        def create(
            cls, **params: Unpack["AuthorizationCreateParams"]
        ) -> "Authorization":
            """
            Create a test-mode authorization.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations",
                    params=params,
                ),
            )

        @classmethod
        async def create_async(
            cls, **params: Unpack["AuthorizationCreateParams"]
        ) -> "Authorization":
            """
            Create a test-mode authorization.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations",
                    params=params,
                ),
            )

        @classmethod
        def _cls_expire(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationExpireParams"],
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def expire(
            authorization: str, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            ...

        @overload
        def expire(
            self, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_expire")
        def expire(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_expire_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationExpireParams"],
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def expire_async(
            authorization: str, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            ...

        @overload
        async def expire_async(
            self, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_expire_async")
        async def expire_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationExpireParams"]
        ) -> "Authorization":
            """
            Expire a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_finalize_amount(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationFinalizeAmountParams"],
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def finalize_amount(
            authorization: str,
            **params: Unpack["AuthorizationFinalizeAmountParams"],
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            ...

        @overload
        def finalize_amount(
            self, **params: Unpack["AuthorizationFinalizeAmountParams"]
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            ...

        @class_method_variant("_cls_finalize_amount")
        def finalize_amount(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationFinalizeAmountParams"]
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_finalize_amount_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationFinalizeAmountParams"],
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def finalize_amount_async(
            authorization: str,
            **params: Unpack["AuthorizationFinalizeAmountParams"],
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            ...

        @overload
        async def finalize_amount_async(
            self, **params: Unpack["AuthorizationFinalizeAmountParams"]
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            ...

        @class_method_variant("_cls_finalize_amount_async")
        async def finalize_amount_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationFinalizeAmountParams"]
        ) -> "Authorization":
            """
            Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_increment(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationIncrementParams"],
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def increment(
            authorization: str,
            **params: Unpack["AuthorizationIncrementParams"],
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            ...

        @overload
        def increment(
            self, **params: Unpack["AuthorizationIncrementParams"]
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_increment")
        def increment(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationIncrementParams"]
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_increment_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationIncrementParams"],
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def increment_async(
            authorization: str,
            **params: Unpack["AuthorizationIncrementParams"],
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            ...

        @overload
        async def increment_async(
            self, **params: Unpack["AuthorizationIncrementParams"]
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_increment_async")
        async def increment_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationIncrementParams"]
        ) -> "Authorization":
            """
            Increment a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_respond(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationRespondParams"],
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def respond(
            authorization: str, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            ...

        @overload
        def respond(
            self, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            ...

        @class_method_variant("_cls_respond")
        def respond(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_respond_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationRespondParams"],
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def respond_async(
            authorization: str, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            ...

        @overload
        async def respond_async(
            self, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            ...

        @class_method_variant("_cls_respond_async")
        async def respond_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationRespondParams"]
        ) -> "Authorization":
            """
            Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_reverse(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationReverseParams"],
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            return cast(
                "Authorization",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def reverse(
            authorization: str, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            ...

        @overload
        def reverse(
            self, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_reverse")
        def reverse(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            return cast(
                "Authorization",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_reverse_async(
            cls,
            authorization: str,
            **params: Unpack["AuthorizationReverseParams"],
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                        authorization=sanitize_id(authorization)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def reverse_async(
            authorization: str, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            ...

        @overload
        async def reverse_async(
            self, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            ...

        @class_method_variant("_cls_reverse_async")
        async def reverse_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["AuthorizationReverseParams"]
        ) -> "Authorization":
            """
            Reverse a test-mode Authorization.
            """
            return cast(
                "Authorization",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                        authorization=sanitize_id(
                            self.resource._data.get("id")
                        )
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "amount_details": AmountDetails,
        "balance_response": BalanceResponse,
        "crypto_transactions": CryptoTransaction,
        "enriched_merchant_data": EnrichedMerchantData,
        "fleet": Fleet,
        "fraud_challenges": FraudChallenge,
        "fuel": Fuel,
        "merchant_data": MerchantData,
        "network_data": NetworkData,
        "pending_request": PendingRequest,
        "redaction": Redaction,
        "request_history": RequestHistory,
        "token_details": TokenDetails,
        "treasury": Treasury,
        "verification_data": VerificationData,
    }


Authorization.TestHelpers._resource_cls = Authorization
