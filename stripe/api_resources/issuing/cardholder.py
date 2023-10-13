# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Cardholder(
    CreateableAPIResource["Cardholder"],
    ListableAPIResource["Cardholder"],
    UpdateableAPIResource["Cardholder"],
):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

    Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards#create-cardholder)
    """

    OBJECT_NAME = "issuing.cardholder"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            billing: "Cardholder.CreateParamsBilling"
            company: NotRequired["Cardholder.CreateParamsCompany|None"]
            email: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            individual: NotRequired["Cardholder.CreateParamsIndividual|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str
            phone_number: NotRequired["str|None"]
            preferred_locales: NotRequired[
                "List[Literal['de', 'en', 'es', 'fr', 'it']]|None"
            ]
            spending_controls: NotRequired[
                "Cardholder.CreateParamsSpendingControls|None"
            ]
            status: NotRequired["Literal['active', 'inactive']|None"]
            type: NotRequired["Literal['company', 'individual']|None"]

        class CreateParamsSpendingControls(TypedDict):
            allowed_categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            blocked_categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            spending_limits: NotRequired[
                "List[Cardholder.CreateParamsSpendingControlsSpendingLimit]|None"
            ]
            spending_limits_currency: NotRequired["str|None"]

        class CreateParamsSpendingControlsSpendingLimit(TypedDict):
            amount: int
            categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            interval: Literal[
                "all_time",
                "daily",
                "monthly",
                "per_authorization",
                "weekly",
                "yearly",
            ]

        class CreateParamsIndividual(TypedDict):
            card_issuing: NotRequired[
                "Cardholder.CreateParamsIndividualCardIssuing|None"
            ]
            dob: NotRequired["Cardholder.CreateParamsIndividualDob|None"]
            first_name: NotRequired["str|None"]
            last_name: NotRequired["str|None"]
            verification: NotRequired[
                "Cardholder.CreateParamsIndividualVerification|None"
            ]

        class CreateParamsIndividualVerification(TypedDict):
            document: NotRequired[
                "Cardholder.CreateParamsIndividualVerificationDocument|None"
            ]

        class CreateParamsIndividualVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsIndividualDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsIndividualCardIssuing(TypedDict):
            user_terms_acceptance: NotRequired[
                "Cardholder.CreateParamsIndividualCardIssuingUserTermsAcceptance|None"
            ]

        class CreateParamsIndividualCardIssuingUserTermsAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["Literal['']|str|None"]

        class CreateParamsCompany(TypedDict):
            tax_id: NotRequired["str|None"]

        class CreateParamsBilling(TypedDict):
            address: "Cardholder.CreateParamsBillingAddress"

        class CreateParamsBillingAddress(TypedDict):
            city: str
            country: str
            line1: str
            line2: NotRequired["str|None"]
            postal_code: str
            state: NotRequired["str|None"]

        class ListParams(RequestOptions):
            created: NotRequired["Cardholder.ListParamsCreated|int|None"]
            email: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            phone_number: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['active', 'blocked', 'inactive']|None"
            ]
            type: NotRequired["Literal['company', 'individual']|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            billing: NotRequired["Cardholder.ModifyParamsBilling|None"]
            company: NotRequired["Cardholder.ModifyParamsCompany|None"]
            email: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            individual: NotRequired["Cardholder.ModifyParamsIndividual|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            phone_number: NotRequired["str|None"]
            preferred_locales: NotRequired[
                "List[Literal['de', 'en', 'es', 'fr', 'it']]|None"
            ]
            spending_controls: NotRequired[
                "Cardholder.ModifyParamsSpendingControls|None"
            ]
            status: NotRequired["Literal['active', 'inactive']|None"]

        class ModifyParamsSpendingControls(TypedDict):
            allowed_categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            blocked_categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            spending_limits: NotRequired[
                "List[Cardholder.ModifyParamsSpendingControlsSpendingLimit]|None"
            ]
            spending_limits_currency: NotRequired["str|None"]

        class ModifyParamsSpendingControlsSpendingLimit(TypedDict):
            amount: int
            categories: NotRequired[
                "List[Literal['ac_refrigeration_repair', 'accounting_bookkeeping_services', 'advertising_services', 'agricultural_cooperative', 'airlines_air_carriers', 'airports_flying_fields', 'ambulance_services', 'amusement_parks_carnivals', 'antique_reproductions', 'antique_shops', 'aquariums', 'architectural_surveying_services', 'art_dealers_and_galleries', 'artists_supply_and_craft_shops', 'auto_and_home_supply_stores', 'auto_body_repair_shops', 'auto_paint_shops', 'auto_service_shops', 'automated_cash_disburse', 'automated_fuel_dispensers', 'automobile_associations', 'automotive_parts_and_accessories_stores', 'automotive_tire_stores', 'bail_and_bond_payments', 'bakeries', 'bands_orchestras', 'barber_and_beauty_shops', 'betting_casino_gambling', 'bicycle_shops', 'billiard_pool_establishments', 'boat_dealers', 'boat_rentals_and_leases', 'book_stores', 'books_periodicals_and_newspapers', 'bowling_alleys', 'bus_lines', 'business_secretarial_schools', 'buying_shopping_services', 'cable_satellite_and_other_pay_television_and_radio', 'camera_and_photographic_supply_stores', 'candy_nut_and_confectionery_stores', 'car_and_truck_dealers_new_used', 'car_and_truck_dealers_used_only', 'car_rental_agencies', 'car_washes', 'carpentry_services', 'carpet_upholstery_cleaning', 'caterers', 'charitable_and_social_service_organizations_fundraising', 'chemicals_and_allied_products', 'child_care_services', 'childrens_and_infants_wear_stores', 'chiropodists_podiatrists', 'chiropractors', 'cigar_stores_and_stands', 'civic_social_fraternal_associations', 'cleaning_and_maintenance', 'clothing_rental', 'colleges_universities', 'commercial_equipment', 'commercial_footwear', 'commercial_photography_art_and_graphics', 'commuter_transport_and_ferries', 'computer_network_services', 'computer_programming', 'computer_repair', 'computer_software_stores', 'computers_peripherals_and_software', 'concrete_work_services', 'construction_materials', 'consulting_public_relations', 'correspondence_schools', 'cosmetic_stores', 'counseling_services', 'country_clubs', 'courier_services', 'court_costs', 'credit_reporting_agencies', 'cruise_lines', 'dairy_products_stores', 'dance_hall_studios_schools', 'dating_escort_services', 'dentists_orthodontists', 'department_stores', 'detective_agencies', 'digital_goods_applications', 'digital_goods_games', 'digital_goods_large_volume', 'digital_goods_media', 'direct_marketing_catalog_merchant', 'direct_marketing_combination_catalog_and_retail_merchant', 'direct_marketing_inbound_telemarketing', 'direct_marketing_insurance_services', 'direct_marketing_other', 'direct_marketing_outbound_telemarketing', 'direct_marketing_subscription', 'direct_marketing_travel', 'discount_stores', 'doctors', 'door_to_door_sales', 'drapery_window_covering_and_upholstery_stores', 'drinking_places', 'drug_stores_and_pharmacies', 'drugs_drug_proprietaries_and_druggist_sundries', 'dry_cleaners', 'durable_goods', 'duty_free_stores', 'eating_places_restaurants', 'educational_services', 'electric_razor_stores', 'electric_vehicle_charging', 'electrical_parts_and_equipment', 'electrical_services', 'electronics_repair_shops', 'electronics_stores', 'elementary_secondary_schools', 'emergency_services_gcas_visa_use_only', 'employment_temp_agencies', 'equipment_rental', 'exterminating_services', 'family_clothing_stores', 'fast_food_restaurants', 'financial_institutions', 'fines_government_administrative_entities', 'fireplace_fireplace_screens_and_accessories_stores', 'floor_covering_stores', 'florists', 'florists_supplies_nursery_stock_and_flowers', 'freezer_and_locker_meat_provisioners', 'fuel_dealers_non_automotive', 'funeral_services_crematories', 'furniture_home_furnishings_and_equipment_stores_except_appliances', 'furniture_repair_refinishing', 'furriers_and_fur_shops', 'general_services', 'gift_card_novelty_and_souvenir_shops', 'glass_paint_and_wallpaper_stores', 'glassware_crystal_stores', 'golf_courses_public', 'government_licensed_horse_dog_racing_us_region_only', 'government_licensed_online_casions_online_gambling_us_region_only', 'government_owned_lotteries_non_us_region', 'government_owned_lotteries_us_region_only', 'government_services', 'grocery_stores_supermarkets', 'hardware_equipment_and_supplies', 'hardware_stores', 'health_and_beauty_spas', 'hearing_aids_sales_and_supplies', 'heating_plumbing_a_c', 'hobby_toy_and_game_shops', 'home_supply_warehouse_stores', 'hospitals', 'hotels_motels_and_resorts', 'household_appliance_stores', 'industrial_supplies', 'information_retrieval_services', 'insurance_default', 'insurance_underwriting_premiums', 'intra_company_purchases', 'jewelry_stores_watches_clocks_and_silverware_stores', 'landscaping_services', 'laundries', 'laundry_cleaning_services', 'legal_services_attorneys', 'luggage_and_leather_goods_stores', 'lumber_building_materials_stores', 'manual_cash_disburse', 'marinas_service_and_supplies', 'marketplaces', 'masonry_stonework_and_plaster', 'massage_parlors', 'medical_and_dental_labs', 'medical_dental_ophthalmic_and_hospital_equipment_and_supplies', 'medical_services', 'membership_organizations', 'mens_and_boys_clothing_and_accessories_stores', 'mens_womens_clothing_stores', 'metal_service_centers', 'miscellaneous', 'miscellaneous_apparel_and_accessory_shops', 'miscellaneous_auto_dealers', 'miscellaneous_business_services', 'miscellaneous_food_stores', 'miscellaneous_general_merchandise', 'miscellaneous_general_services', 'miscellaneous_home_furnishing_specialty_stores', 'miscellaneous_publishing_and_printing', 'miscellaneous_recreation_services', 'miscellaneous_repair_shops', 'miscellaneous_specialty_retail', 'mobile_home_dealers', 'motion_picture_theaters', 'motor_freight_carriers_and_trucking', 'motor_homes_dealers', 'motor_vehicle_supplies_and_new_parts', 'motorcycle_shops_and_dealers', 'motorcycle_shops_dealers', 'music_stores_musical_instruments_pianos_and_sheet_music', 'news_dealers_and_newsstands', 'non_fi_money_orders', 'non_fi_stored_value_card_purchase_load', 'nondurable_goods', 'nurseries_lawn_and_garden_supply_stores', 'nursing_personal_care', 'office_and_commercial_furniture', 'opticians_eyeglasses', 'optometrists_ophthalmologist', 'orthopedic_goods_prosthetic_devices', 'osteopaths', 'package_stores_beer_wine_and_liquor', 'paints_varnishes_and_supplies', 'parking_lots_garages', 'passenger_railways', 'pawn_shops', 'pet_shops_pet_food_and_supplies', 'petroleum_and_petroleum_products', 'photo_developing', 'photographic_photocopy_microfilm_equipment_and_supplies', 'photographic_studios', 'picture_video_production', 'piece_goods_notions_and_other_dry_goods', 'plumbing_heating_equipment_and_supplies', 'political_organizations', 'postal_services_government_only', 'precious_stones_and_metals_watches_and_jewelry', 'professional_services', 'public_warehousing_and_storage', 'quick_copy_repro_and_blueprint', 'railroads', 'real_estate_agents_and_managers_rentals', 'record_stores', 'recreational_vehicle_rentals', 'religious_goods_stores', 'religious_organizations', 'roofing_siding_sheet_metal', 'secretarial_support_services', 'security_brokers_dealers', 'service_stations', 'sewing_needlework_fabric_and_piece_goods_stores', 'shoe_repair_hat_cleaning', 'shoe_stores', 'small_appliance_repair', 'snowmobile_dealers', 'special_trade_services', 'specialty_cleaning', 'sporting_goods_stores', 'sporting_recreation_camps', 'sports_and_riding_apparel_stores', 'sports_clubs_fields', 'stamp_and_coin_stores', 'stationary_office_supplies_printing_and_writing_paper', 'stationery_stores_office_and_school_supply_stores', 'swimming_pools_sales', 't_ui_travel_germany', 'tailors_alterations', 'tax_payments_government_agencies', 'tax_preparation_services', 'taxicabs_limousines', 'telecommunication_equipment_and_telephone_sales', 'telecommunication_services', 'telegraph_services', 'tent_and_awning_shops', 'testing_laboratories', 'theatrical_ticket_agencies', 'timeshares', 'tire_retreading_and_repair', 'tolls_bridge_fees', 'tourist_attractions_and_exhibits', 'towing_services', 'trailer_parks_campgrounds', 'transportation_services', 'travel_agencies_tour_operators', 'truck_stop_iteration', 'truck_utility_trailer_rentals', 'typesetting_plate_making_and_related_services', 'typewriter_stores', 'u_s_federal_government_agencies_or_departments', 'uniforms_commercial_clothing', 'used_merchandise_and_secondhand_stores', 'utilities', 'variety_stores', 'veterinary_services', 'video_amusement_game_supplies', 'video_game_arcades', 'video_tape_rental_stores', 'vocational_trade_schools', 'watch_jewelry_repair', 'welding_repair', 'wholesale_clubs', 'wig_and_toupee_stores', 'wires_money_orders', 'womens_accessory_and_specialty_shops', 'womens_ready_to_wear_stores', 'wrecking_and_salvage_yards']]|None"
            ]
            interval: Literal[
                "all_time",
                "daily",
                "monthly",
                "per_authorization",
                "weekly",
                "yearly",
            ]

        class ModifyParamsIndividual(TypedDict):
            card_issuing: NotRequired[
                "Cardholder.ModifyParamsIndividualCardIssuing|None"
            ]
            dob: NotRequired["Cardholder.ModifyParamsIndividualDob|None"]
            first_name: NotRequired["str|None"]
            last_name: NotRequired["str|None"]
            verification: NotRequired[
                "Cardholder.ModifyParamsIndividualVerification|None"
            ]

        class ModifyParamsIndividualVerification(TypedDict):
            document: NotRequired[
                "Cardholder.ModifyParamsIndividualVerificationDocument|None"
            ]

        class ModifyParamsIndividualVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class ModifyParamsIndividualDob(TypedDict):
            day: int
            month: int
            year: int

        class ModifyParamsIndividualCardIssuing(TypedDict):
            user_terms_acceptance: NotRequired[
                "Cardholder.ModifyParamsIndividualCardIssuingUserTermsAcceptance|None"
            ]

        class ModifyParamsIndividualCardIssuingUserTermsAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["Literal['']|str|None"]

        class ModifyParamsCompany(TypedDict):
            tax_id: NotRequired["str|None"]

        class ModifyParamsBilling(TypedDict):
            address: "Cardholder.ModifyParamsBillingAddress"

        class ModifyParamsBillingAddress(TypedDict):
            city: str
            country: str
            line1: str
            line2: NotRequired["str|None"]
            postal_code: str
            state: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    billing: StripeObject
    company: Optional[StripeObject]
    created: int
    email: Optional[str]
    id: str
    individual: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["issuing.cardholder"]
    phone_number: Optional[str]
    preferred_locales: Optional[List[Literal["de", "en", "es", "fr", "it"]]]
    requirements: StripeObject
    spending_controls: Optional[StripeObject]
    status: Literal["active", "blocked", "inactive"]
    type: Literal["company", "individual"]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Cardholder.CreateParams"]
    ) -> "Cardholder":
        return cast(
            "Cardholder",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Cardholder.ListParams"]
    ) -> ListObject["Cardholder"]:
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
        cls, id, **params: Unpack["Cardholder.ModifyParams"]
    ) -> "Cardholder":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Cardholder",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Cardholder.RetrieveParams"]
    ) -> "Cardholder":
        instance = cls(id, **params)
        instance.refresh()
        return instance
