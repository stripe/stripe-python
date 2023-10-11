# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, Type, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.token import Token
    from stripe.api_resources.issuing.transaction import Transaction


class Authorization(
    ListableAPIResource["Authorization"],
    UpdateableAPIResource["Authorization"],
):
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)
    """

    OBJECT_NAME = "issuing.authorization"

    class ApproveParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class DeclineParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ListParams(RequestOptions):
        card: NotRequired[Optional[str]]
        cardholder: NotRequired[Optional[str]]
        created: NotRequired[
            Optional[Union["Authorization.ListParamsCreated", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[Optional[Literal["closed", "pending", "reversed"]]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CaptureParams(RequestOptions):
        capture_amount: NotRequired[Optional[int]]
        close_authorization: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        purchase_details: NotRequired[
            Optional["Authorization.CaptureParamsPurchaseDetails"]
        ]

    class CaptureParamsPurchaseDetails(TypedDict):
        flight: NotRequired[
            Optional["Authorization.CaptureParamsPurchaseDetailsFlight"]
        ]
        fuel: NotRequired[
            Optional["Authorization.CaptureParamsPurchaseDetailsFuel"]
        ]
        lodging: NotRequired[
            Optional["Authorization.CaptureParamsPurchaseDetailsLodging"]
        ]
        receipt: NotRequired[
            Optional[List["Authorization.CaptureParamsPurchaseDetailsReceipt"]]
        ]
        reference: NotRequired[Optional[str]]

    class CaptureParamsPurchaseDetailsReceipt(TypedDict):
        description: NotRequired[Optional[str]]
        quantity: NotRequired[Optional[float]]
        total: NotRequired[Optional[int]]
        unit_cost: NotRequired[Optional[int]]

    class CaptureParamsPurchaseDetailsLodging(TypedDict):
        check_in_at: NotRequired[Optional[int]]
        nights: NotRequired[Optional[int]]

    class CaptureParamsPurchaseDetailsFuel(TypedDict):
        type: NotRequired[
            Optional[
                Literal[
                    "diesel",
                    "other",
                    "unleaded_plus",
                    "unleaded_regular",
                    "unleaded_super",
                ]
            ]
        ]
        unit: NotRequired[Optional[Literal["liter", "us_gallon"]]]
        unit_cost_decimal: NotRequired[Optional[float]]
        volume_decimal: NotRequired[Optional[float]]

    class CaptureParamsPurchaseDetailsFlight(TypedDict):
        departure_at: NotRequired[Optional[int]]
        passenger_name: NotRequired[Optional[str]]
        refundable: NotRequired[Optional[bool]]
        segments: NotRequired[
            Optional[
                List["Authorization.CaptureParamsPurchaseDetailsFlightSegment"]
            ]
        ]
        travel_agency: NotRequired[Optional[str]]

    class CaptureParamsPurchaseDetailsFlightSegment(TypedDict):
        arrival_airport_code: NotRequired[Optional[str]]
        carrier: NotRequired[Optional[str]]
        departure_airport_code: NotRequired[Optional[str]]
        flight_number: NotRequired[Optional[str]]
        service_class: NotRequired[Optional[str]]
        stopover_allowed: NotRequired[Optional[bool]]

    class CreateParams(RequestOptions):
        amount: int
        amount_details: NotRequired[
            Optional["Authorization.CreateParamsAmountDetails"]
        ]
        authorization_method: NotRequired[
            Optional[
                Literal["chip", "contactless", "keyed_in", "online", "swipe"]
            ]
        ]
        card: str
        currency: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        is_amount_controllable: NotRequired[Optional[bool]]
        merchant_data: NotRequired[
            Optional["Authorization.CreateParamsMerchantData"]
        ]
        network_data: NotRequired[
            Optional["Authorization.CreateParamsNetworkData"]
        ]
        verification_data: NotRequired[
            Optional["Authorization.CreateParamsVerificationData"]
        ]
        wallet: NotRequired[
            Optional[Literal["apple_pay", "google_pay", "samsung_pay"]]
        ]

    class CreateParamsVerificationData(TypedDict):
        address_line1_check: NotRequired[
            Optional[Literal["match", "mismatch", "not_provided"]]
        ]
        address_postal_code_check: NotRequired[
            Optional[Literal["match", "mismatch", "not_provided"]]
        ]
        cvc_check: NotRequired[
            Optional[Literal["match", "mismatch", "not_provided"]]
        ]
        expiry_check: NotRequired[
            Optional[Literal["match", "mismatch", "not_provided"]]
        ]

    class CreateParamsNetworkData(TypedDict):
        acquiring_institution_id: NotRequired[Optional[str]]

    class CreateParamsMerchantData(TypedDict):
        category: NotRequired[
            Optional[
                Literal[
                    "ac_refrigeration_repair",
                    "accounting_bookkeeping_services",
                    "advertising_services",
                    "agricultural_cooperative",
                    "airlines_air_carriers",
                    "airports_flying_fields",
                    "ambulance_services",
                    "amusement_parks_carnivals",
                    "antique_reproductions",
                    "antique_shops",
                    "aquariums",
                    "architectural_surveying_services",
                    "art_dealers_and_galleries",
                    "artists_supply_and_craft_shops",
                    "auto_and_home_supply_stores",
                    "auto_body_repair_shops",
                    "auto_paint_shops",
                    "auto_service_shops",
                    "automated_cash_disburse",
                    "automated_fuel_dispensers",
                    "automobile_associations",
                    "automotive_parts_and_accessories_stores",
                    "automotive_tire_stores",
                    "bail_and_bond_payments",
                    "bakeries",
                    "bands_orchestras",
                    "barber_and_beauty_shops",
                    "betting_casino_gambling",
                    "bicycle_shops",
                    "billiard_pool_establishments",
                    "boat_dealers",
                    "boat_rentals_and_leases",
                    "book_stores",
                    "books_periodicals_and_newspapers",
                    "bowling_alleys",
                    "bus_lines",
                    "business_secretarial_schools",
                    "buying_shopping_services",
                    "cable_satellite_and_other_pay_television_and_radio",
                    "camera_and_photographic_supply_stores",
                    "candy_nut_and_confectionery_stores",
                    "car_and_truck_dealers_new_used",
                    "car_and_truck_dealers_used_only",
                    "car_rental_agencies",
                    "car_washes",
                    "carpentry_services",
                    "carpet_upholstery_cleaning",
                    "caterers",
                    "charitable_and_social_service_organizations_fundraising",
                    "chemicals_and_allied_products",
                    "child_care_services",
                    "childrens_and_infants_wear_stores",
                    "chiropodists_podiatrists",
                    "chiropractors",
                    "cigar_stores_and_stands",
                    "civic_social_fraternal_associations",
                    "cleaning_and_maintenance",
                    "clothing_rental",
                    "colleges_universities",
                    "commercial_equipment",
                    "commercial_footwear",
                    "commercial_photography_art_and_graphics",
                    "commuter_transport_and_ferries",
                    "computer_network_services",
                    "computer_programming",
                    "computer_repair",
                    "computer_software_stores",
                    "computers_peripherals_and_software",
                    "concrete_work_services",
                    "construction_materials",
                    "consulting_public_relations",
                    "correspondence_schools",
                    "cosmetic_stores",
                    "counseling_services",
                    "country_clubs",
                    "courier_services",
                    "court_costs",
                    "credit_reporting_agencies",
                    "cruise_lines",
                    "dairy_products_stores",
                    "dance_hall_studios_schools",
                    "dating_escort_services",
                    "dentists_orthodontists",
                    "department_stores",
                    "detective_agencies",
                    "digital_goods_applications",
                    "digital_goods_games",
                    "digital_goods_large_volume",
                    "digital_goods_media",
                    "direct_marketing_catalog_merchant",
                    "direct_marketing_combination_catalog_and_retail_merchant",
                    "direct_marketing_inbound_telemarketing",
                    "direct_marketing_insurance_services",
                    "direct_marketing_other",
                    "direct_marketing_outbound_telemarketing",
                    "direct_marketing_subscription",
                    "direct_marketing_travel",
                    "discount_stores",
                    "doctors",
                    "door_to_door_sales",
                    "drapery_window_covering_and_upholstery_stores",
                    "drinking_places",
                    "drug_stores_and_pharmacies",
                    "drugs_drug_proprietaries_and_druggist_sundries",
                    "dry_cleaners",
                    "durable_goods",
                    "duty_free_stores",
                    "eating_places_restaurants",
                    "educational_services",
                    "electric_razor_stores",
                    "electric_vehicle_charging",
                    "electrical_parts_and_equipment",
                    "electrical_services",
                    "electronics_repair_shops",
                    "electronics_stores",
                    "elementary_secondary_schools",
                    "emergency_services_gcas_visa_use_only",
                    "employment_temp_agencies",
                    "equipment_rental",
                    "exterminating_services",
                    "family_clothing_stores",
                    "fast_food_restaurants",
                    "financial_institutions",
                    "fines_government_administrative_entities",
                    "fireplace_fireplace_screens_and_accessories_stores",
                    "floor_covering_stores",
                    "florists",
                    "florists_supplies_nursery_stock_and_flowers",
                    "freezer_and_locker_meat_provisioners",
                    "fuel_dealers_non_automotive",
                    "funeral_services_crematories",
                    "furniture_home_furnishings_and_equipment_stores_except_appliances",
                    "furniture_repair_refinishing",
                    "furriers_and_fur_shops",
                    "general_services",
                    "gift_card_novelty_and_souvenir_shops",
                    "glass_paint_and_wallpaper_stores",
                    "glassware_crystal_stores",
                    "golf_courses_public",
                    "government_licensed_horse_dog_racing_us_region_only",
                    "government_licensed_online_casions_online_gambling_us_region_only",
                    "government_owned_lotteries_non_us_region",
                    "government_owned_lotteries_us_region_only",
                    "government_services",
                    "grocery_stores_supermarkets",
                    "hardware_equipment_and_supplies",
                    "hardware_stores",
                    "health_and_beauty_spas",
                    "hearing_aids_sales_and_supplies",
                    "heating_plumbing_a_c",
                    "hobby_toy_and_game_shops",
                    "home_supply_warehouse_stores",
                    "hospitals",
                    "hotels_motels_and_resorts",
                    "household_appliance_stores",
                    "industrial_supplies",
                    "information_retrieval_services",
                    "insurance_default",
                    "insurance_underwriting_premiums",
                    "intra_company_purchases",
                    "jewelry_stores_watches_clocks_and_silverware_stores",
                    "landscaping_services",
                    "laundries",
                    "laundry_cleaning_services",
                    "legal_services_attorneys",
                    "luggage_and_leather_goods_stores",
                    "lumber_building_materials_stores",
                    "manual_cash_disburse",
                    "marinas_service_and_supplies",
                    "marketplaces",
                    "masonry_stonework_and_plaster",
                    "massage_parlors",
                    "medical_and_dental_labs",
                    "medical_dental_ophthalmic_and_hospital_equipment_and_supplies",
                    "medical_services",
                    "membership_organizations",
                    "mens_and_boys_clothing_and_accessories_stores",
                    "mens_womens_clothing_stores",
                    "metal_service_centers",
                    "miscellaneous_apparel_and_accessory_shops",
                    "miscellaneous_auto_dealers",
                    "miscellaneous_business_services",
                    "miscellaneous_food_stores",
                    "miscellaneous_general_merchandise",
                    "miscellaneous_general_services",
                    "miscellaneous_home_furnishing_specialty_stores",
                    "miscellaneous_publishing_and_printing",
                    "miscellaneous_recreation_services",
                    "miscellaneous_repair_shops",
                    "miscellaneous_specialty_retail",
                    "mobile_home_dealers",
                    "motion_picture_theaters",
                    "motor_freight_carriers_and_trucking",
                    "motor_homes_dealers",
                    "motor_vehicle_supplies_and_new_parts",
                    "motorcycle_shops_and_dealers",
                    "motorcycle_shops_dealers",
                    "music_stores_musical_instruments_pianos_and_sheet_music",
                    "news_dealers_and_newsstands",
                    "non_fi_money_orders",
                    "non_fi_stored_value_card_purchase_load",
                    "nondurable_goods",
                    "nurseries_lawn_and_garden_supply_stores",
                    "nursing_personal_care",
                    "office_and_commercial_furniture",
                    "opticians_eyeglasses",
                    "optometrists_ophthalmologist",
                    "orthopedic_goods_prosthetic_devices",
                    "osteopaths",
                    "package_stores_beer_wine_and_liquor",
                    "paints_varnishes_and_supplies",
                    "parking_lots_garages",
                    "passenger_railways",
                    "pawn_shops",
                    "pet_shops_pet_food_and_supplies",
                    "petroleum_and_petroleum_products",
                    "photo_developing",
                    "photographic_photocopy_microfilm_equipment_and_supplies",
                    "photographic_studios",
                    "picture_video_production",
                    "piece_goods_notions_and_other_dry_goods",
                    "plumbing_heating_equipment_and_supplies",
                    "political_organizations",
                    "postal_services_government_only",
                    "precious_stones_and_metals_watches_and_jewelry",
                    "professional_services",
                    "public_warehousing_and_storage",
                    "quick_copy_repro_and_blueprint",
                    "railroads",
                    "real_estate_agents_and_managers_rentals",
                    "record_stores",
                    "recreational_vehicle_rentals",
                    "religious_goods_stores",
                    "religious_organizations",
                    "roofing_siding_sheet_metal",
                    "secretarial_support_services",
                    "security_brokers_dealers",
                    "service_stations",
                    "sewing_needlework_fabric_and_piece_goods_stores",
                    "shoe_repair_hat_cleaning",
                    "shoe_stores",
                    "small_appliance_repair",
                    "snowmobile_dealers",
                    "special_trade_services",
                    "specialty_cleaning",
                    "sporting_goods_stores",
                    "sporting_recreation_camps",
                    "sports_and_riding_apparel_stores",
                    "sports_clubs_fields",
                    "stamp_and_coin_stores",
                    "stationary_office_supplies_printing_and_writing_paper",
                    "stationery_stores_office_and_school_supply_stores",
                    "swimming_pools_sales",
                    "t_ui_travel_germany",
                    "tailors_alterations",
                    "tax_payments_government_agencies",
                    "tax_preparation_services",
                    "taxicabs_limousines",
                    "telecommunication_equipment_and_telephone_sales",
                    "telecommunication_services",
                    "telegraph_services",
                    "tent_and_awning_shops",
                    "testing_laboratories",
                    "theatrical_ticket_agencies",
                    "timeshares",
                    "tire_retreading_and_repair",
                    "tolls_bridge_fees",
                    "tourist_attractions_and_exhibits",
                    "towing_services",
                    "trailer_parks_campgrounds",
                    "transportation_services",
                    "travel_agencies_tour_operators",
                    "truck_stop_iteration",
                    "truck_utility_trailer_rentals",
                    "typesetting_plate_making_and_related_services",
                    "typewriter_stores",
                    "u_s_federal_government_agencies_or_departments",
                    "uniforms_commercial_clothing",
                    "used_merchandise_and_secondhand_stores",
                    "utilities",
                    "variety_stores",
                    "veterinary_services",
                    "video_amusement_game_supplies",
                    "video_game_arcades",
                    "video_tape_rental_stores",
                    "vocational_trade_schools",
                    "watch_jewelry_repair",
                    "welding_repair",
                    "wholesale_clubs",
                    "wig_and_toupee_stores",
                    "wires_money_orders",
                    "womens_accessory_and_specialty_shops",
                    "womens_ready_to_wear_stores",
                    "wrecking_and_salvage_yards",
                ]
            ]
        ]
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        network_id: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        terminal_id: NotRequired[Optional[str]]

    class CreateParamsAmountDetails(TypedDict):
        atm_fee: NotRequired[Optional[int]]
        cashback_amount: NotRequired[Optional[int]]

    class ExpireParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class IncrementParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        increment_amount: int
        is_amount_controllable: NotRequired[Optional[bool]]

    class ReverseParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        reverse_amount: NotRequired[Optional[int]]

    amount: int
    amount_details: Optional[StripeObject]
    approved: bool
    authorization_method: Literal[
        "chip", "contactless", "keyed_in", "online", "swipe"
    ]
    balance_transactions: List["BalanceTransaction"]
    card: "Card"
    cardholder: Optional[ExpandableField["Cardholder"]]
    created: int
    currency: str
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: StripeObject
    metadata: Dict[str, str]
    network_data: Optional[StripeObject]
    object: Literal["issuing.authorization"]
    pending_request: Optional[StripeObject]
    request_history: List[StripeObject]
    status: Literal["closed", "pending", "reversed"]
    token: Optional[ExpandableField["Token"]]
    transactions: List["Transaction"]
    treasury: Optional[StripeObject]
    verification_data: StripeObject
    wallet: Optional[str]

    @classmethod
    def _cls_approve(
        cls,
        authorization: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Authorization.ApproveParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_approve")
    def approve(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Authorization.ApproveParams"]
    ):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_decline(
        cls,
        authorization: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Authorization.DeclineParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_decline")
    def decline(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Authorization.DeclineParams"]
    ):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Authorization.ListParams"]
    ) -> ListObject["Authorization"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
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
        cls, id, **params: Unpack["Authorization.ModifyParams"]
    ) -> "Authorization":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Authorization",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Authorization.RetrieveParams"]
    ) -> "Authorization":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["Authorization"]):
        _resource_cls: Type["Authorization"]

        @classmethod
        def _cls_capture(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Authorization.CaptureParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_capture")
        def capture(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Authorization.CaptureParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def create(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Authorization.CreateParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def _cls_expire(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Authorization.ExpireParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_expire")
        def expire(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Authorization.ExpireParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_increment(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Authorization.IncrementParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_increment")
        def increment(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Authorization.IncrementParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_reverse(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Authorization.ReverseParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_reverse")
        def reverse(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Authorization.ReverseParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Authorization.TestHelpers._resource_cls = Authorization
