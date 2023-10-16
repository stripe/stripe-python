# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.authorization import Authorization
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.dispute import Dispute
    from stripe.api_resources.issuing.token import Token


class Transaction(
    ListableAPIResource["Transaction"],
    UpdateableAPIResource["Transaction"],
):
    """
    Any use of an [issued card](https://stripe.com/docs/issuing) that results in funds entering or leaving
    your Stripe account, such as a completed purchase or refund, is represented by an Issuing
    `Transaction` object.

    Related guide: [Issued card transactions](https://stripe.com/docs/issuing/purchases/transactions)
    """

    OBJECT_NAME = "issuing.transaction"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            card: NotRequired["str|None"]
            cardholder: NotRequired["str|None"]
            created: NotRequired["Transaction.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired["Literal['capture', 'refund']|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateForceCaptureParams(RequestOptions):
            amount: int
            card: str
            currency: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            merchant_data: NotRequired[
                "Transaction.CreateForceCaptureParamsMerchantData|None"
            ]
            purchase_details: NotRequired[
                "Transaction.CreateForceCaptureParamsPurchaseDetails|None"
            ]

        class CreateForceCaptureParamsPurchaseDetails(TypedDict):
            flight: NotRequired[
                "Transaction.CreateForceCaptureParamsPurchaseDetailsFlight|None"
            ]
            fuel: NotRequired[
                "Transaction.CreateForceCaptureParamsPurchaseDetailsFuel|None"
            ]
            lodging: NotRequired[
                "Transaction.CreateForceCaptureParamsPurchaseDetailsLodging|None"
            ]
            receipt: NotRequired[
                "List[Transaction.CreateForceCaptureParamsPurchaseDetailsReceipt]|None"
            ]
            reference: NotRequired["str|None"]

        class CreateForceCaptureParamsPurchaseDetailsReceipt(TypedDict):
            description: NotRequired["str|None"]
            quantity: NotRequired["float|None"]
            total: NotRequired["int|None"]
            unit_cost: NotRequired["int|None"]

        class CreateForceCaptureParamsPurchaseDetailsLodging(TypedDict):
            check_in_at: NotRequired["int|None"]
            nights: NotRequired["int|None"]

        class CreateForceCaptureParamsPurchaseDetailsFuel(TypedDict):
            type: NotRequired[
                "Literal['diesel', 'other', 'unleaded_plus', 'unleaded_regular', 'unleaded_super']|None"
            ]
            unit: NotRequired["Literal['liter', 'us_gallon']|None"]
            unit_cost_decimal: NotRequired["float|None"]
            volume_decimal: NotRequired["float|None"]

        class CreateForceCaptureParamsPurchaseDetailsFlight(TypedDict):
            departure_at: NotRequired["int|None"]
            passenger_name: NotRequired["str|None"]
            refundable: NotRequired["bool|None"]
            segments: NotRequired[
                "List[Transaction.CreateForceCaptureParamsPurchaseDetailsFlightSegment]|None"
            ]
            travel_agency: NotRequired["str|None"]

        class CreateForceCaptureParamsPurchaseDetailsFlightSegment(TypedDict):
            arrival_airport_code: NotRequired["str|None"]
            carrier: NotRequired["str|None"]
            departure_airport_code: NotRequired["str|None"]
            flight_number: NotRequired["str|None"]
            service_class: NotRequired["str|None"]
            stopover_allowed: NotRequired["bool|None"]

        class CreateForceCaptureParamsMerchantData(TypedDict):
            category: NotRequired[
                "Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']|None"
            ]
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            name: NotRequired["str|None"]
            network_id: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            terminal_id: NotRequired["str|None"]

        class CreateUnlinkedRefundParams(RequestOptions):
            amount: int
            card: str
            currency: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            merchant_data: NotRequired[
                "Transaction.CreateUnlinkedRefundParamsMerchantData|None"
            ]
            purchase_details: NotRequired[
                "Transaction.CreateUnlinkedRefundParamsPurchaseDetails|None"
            ]

        class CreateUnlinkedRefundParamsPurchaseDetails(TypedDict):
            flight: NotRequired[
                "Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFlight|None"
            ]
            fuel: NotRequired[
                "Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFuel|None"
            ]
            lodging: NotRequired[
                "Transaction.CreateUnlinkedRefundParamsPurchaseDetailsLodging|None"
            ]
            receipt: NotRequired[
                "List[Transaction.CreateUnlinkedRefundParamsPurchaseDetailsReceipt]|None"
            ]
            reference: NotRequired["str|None"]

        class CreateUnlinkedRefundParamsPurchaseDetailsReceipt(TypedDict):
            description: NotRequired["str|None"]
            quantity: NotRequired["float|None"]
            total: NotRequired["int|None"]
            unit_cost: NotRequired["int|None"]

        class CreateUnlinkedRefundParamsPurchaseDetailsLodging(TypedDict):
            check_in_at: NotRequired["int|None"]
            nights: NotRequired["int|None"]

        class CreateUnlinkedRefundParamsPurchaseDetailsFuel(TypedDict):
            type: NotRequired[
                "Literal['diesel', 'other', 'unleaded_plus', 'unleaded_regular', 'unleaded_super']|None"
            ]
            unit: NotRequired["Literal['liter', 'us_gallon']|None"]
            unit_cost_decimal: NotRequired["float|None"]
            volume_decimal: NotRequired["float|None"]

        class CreateUnlinkedRefundParamsPurchaseDetailsFlight(TypedDict):
            departure_at: NotRequired["int|None"]
            passenger_name: NotRequired["str|None"]
            refundable: NotRequired["bool|None"]
            segments: NotRequired[
                "List[Transaction.CreateUnlinkedRefundParamsPurchaseDetailsFlightSegment]|None"
            ]
            travel_agency: NotRequired["str|None"]

        class CreateUnlinkedRefundParamsPurchaseDetailsFlightSegment(
            TypedDict
        ):
            arrival_airport_code: NotRequired["str|None"]
            carrier: NotRequired["str|None"]
            departure_airport_code: NotRequired["str|None"]
            flight_number: NotRequired["str|None"]
            service_class: NotRequired["str|None"]
            stopover_allowed: NotRequired["bool|None"]

        class CreateUnlinkedRefundParamsMerchantData(TypedDict):
            category: NotRequired[
                "Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']|None"
            ]
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            name: NotRequired["str|None"]
            network_id: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            terminal_id: NotRequired["str|None"]

        class RefundParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            refund_amount: NotRequired["int|None"]

    amount: int
    amount_details: Optional[StripeObject]
    authorization: Optional[ExpandableField["Authorization"]]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    card: ExpandableField["Card"]
    cardholder: Optional[ExpandableField["Cardholder"]]
    created: int
    currency: str
    dispute: Optional[ExpandableField["Dispute"]]
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: StripeObject
    metadata: Dict[str, str]
    object: Literal["issuing.transaction"]
    purchase_details: Optional[StripeObject]
    token: Optional[ExpandableField["Token"]]
    treasury: Optional[StripeObject]
    type: Literal["capture", "refund"]
    wallet: Optional[Literal["apple_pay", "google_pay", "samsung_pay"]]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Transaction.ListParams"]
    ) -> ListObject["Transaction"]:
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
        cls, id, **params: Unpack["Transaction.ModifyParams"]
    ) -> "Transaction":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Transaction",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Transaction.RetrieveParams"]
    ) -> "Transaction":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["Transaction"]):
        _resource_cls: Type["Transaction"]

        @classmethod
        def create_force_capture(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Transaction.CreateForceCaptureParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/create_force_capture",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def create_unlinked_refund(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Transaction.CreateUnlinkedRefundParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/create_unlinked_refund",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def _cls_refund(
            cls,
            transaction: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Transaction.RefundParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/transactions/{transaction}/refund".format(
                    transaction=util.sanitize_id(transaction)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_refund")
        def refund(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Transaction.RefundParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/transactions/{transaction}/refund".format(
                    transaction=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Transaction.TestHelpers._resource_cls = Transaction
