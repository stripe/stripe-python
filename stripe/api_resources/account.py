# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import api_resources, oauth, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card
    from stripe.api_resources.file import File
    from stripe.api_resources.person import Person


@nested_resource_class_methods("capability")
@nested_resource_class_methods("external_account")
@nested_resource_class_methods("login_link")
@nested_resource_class_methods("person")
class Account(
    CreateableAPIResource["Account"],
    DeletableAPIResource["Account"],
    ListableAPIResource["Account"],
    UpdateableAPIResource["Account"],
):
    """
    This is an object representing a Stripe account. You can retrieve it to see
    properties on the account like its current requirements or if the account is
    enabled to make live charges or receive payouts.

    For Custom accounts, the properties below are always returned. For other accounts, some properties are returned until that
    account has started to go through Connect Onboarding. Once you create an [Account Link](https://stripe.com/docs/api/account_links)
    for a Standard or Express account, some parameters are no longer returned. These are marked as **Custom Only** or **Custom and Express**
    below. Learn about the differences [between accounts](https://stripe.com/docs/connect/accounts).
    """

    OBJECT_NAME = "account"

    class BusinessProfile(StripeObject):
        class MonthlyEstimatedRevenue(StripeObject):
            amount: int
            currency: str

        class SupportAddress(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        mcc: Optional[str]
        monthly_estimated_revenue: Optional[MonthlyEstimatedRevenue]
        name: Optional[str]
        product_description: Optional[str]
        support_address: Optional[SupportAddress]
        support_email: Optional[str]
        support_phone: Optional[str]
        support_url: Optional[str]
        url: Optional[str]
        _inner_class_types = {
            "monthly_estimated_revenue": MonthlyEstimatedRevenue,
            "support_address": SupportAddress,
        }

    class Capabilities(StripeObject):
        acss_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        affirm_payments: Optional[Literal["active", "inactive", "pending"]]
        afterpay_clearpay_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        au_becs_debit_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        bacs_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        bancontact_payments: Optional[Literal["active", "inactive", "pending"]]
        bank_transfer_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        blik_payments: Optional[Literal["active", "inactive", "pending"]]
        boleto_payments: Optional[Literal["active", "inactive", "pending"]]
        card_issuing: Optional[Literal["active", "inactive", "pending"]]
        card_payments: Optional[Literal["active", "inactive", "pending"]]
        cartes_bancaires_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        cashapp_payments: Optional[Literal["active", "inactive", "pending"]]
        eps_payments: Optional[Literal["active", "inactive", "pending"]]
        fpx_payments: Optional[Literal["active", "inactive", "pending"]]
        giropay_payments: Optional[Literal["active", "inactive", "pending"]]
        grabpay_payments: Optional[Literal["active", "inactive", "pending"]]
        ideal_payments: Optional[Literal["active", "inactive", "pending"]]
        india_international_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        jcb_payments: Optional[Literal["active", "inactive", "pending"]]
        klarna_payments: Optional[Literal["active", "inactive", "pending"]]
        konbini_payments: Optional[Literal["active", "inactive", "pending"]]
        legacy_payments: Optional[Literal["active", "inactive", "pending"]]
        link_payments: Optional[Literal["active", "inactive", "pending"]]
        oxxo_payments: Optional[Literal["active", "inactive", "pending"]]
        p24_payments: Optional[Literal["active", "inactive", "pending"]]
        paynow_payments: Optional[Literal["active", "inactive", "pending"]]
        paypal_payments: Optional[Literal["active", "inactive", "pending"]]
        promptpay_payments: Optional[Literal["active", "inactive", "pending"]]
        sepa_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        sofort_payments: Optional[Literal["active", "inactive", "pending"]]
        tax_reporting_us_1099_k: Optional[
            Literal["active", "inactive", "pending"]
        ]
        tax_reporting_us_1099_misc: Optional[
            Literal["active", "inactive", "pending"]
        ]
        transfers: Optional[Literal["active", "inactive", "pending"]]
        treasury: Optional[Literal["active", "inactive", "pending"]]
        us_bank_account_ach_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        zip_payments: Optional[Literal["active", "inactive", "pending"]]

    class Company(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        class AddressKana(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]
            town: Optional[str]

        class AddressKanji(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]
            town: Optional[str]

        class OwnershipDeclaration(StripeObject):
            date: Optional[int]
            ip: Optional[str]
            user_agent: Optional[str]

        class Verification(StripeObject):
            class Document(StripeObject):
                back: Optional[ExpandableField["File"]]
                details: Optional[str]
                details_code: Optional[str]
                front: Optional[ExpandableField["File"]]

            document: Document
            _inner_class_types = {"document": Document}

        address: Optional[Address]
        address_kana: Optional[AddressKana]
        address_kanji: Optional[AddressKanji]
        directors_provided: Optional[bool]
        executives_provided: Optional[bool]
        export_license_id: Optional[str]
        export_purpose_code: Optional[str]
        name: Optional[str]
        name_kana: Optional[str]
        name_kanji: Optional[str]
        owners_provided: Optional[bool]
        ownership_declaration: Optional[OwnershipDeclaration]
        phone: Optional[str]
        structure: Optional[
            Literal[
                "free_zone_establishment",
                "free_zone_llc",
                "government_instrumentality",
                "governmental_unit",
                "incorporated_non_profit",
                "incorporated_partnership",
                "limited_liability_partnership",
                "llc",
                "multi_member_llc",
                "private_company",
                "private_corporation",
                "private_partnership",
                "public_company",
                "public_corporation",
                "public_partnership",
                "single_member_llc",
                "sole_establishment",
                "sole_proprietorship",
                "tax_exempt_government_instrumentality",
                "unincorporated_association",
                "unincorporated_non_profit",
                "unincorporated_partnership",
            ]
        ]
        tax_id_provided: Optional[bool]
        tax_id_registrar: Optional[str]
        vat_id_provided: Optional[bool]
        verification: Optional[Verification]
        _inner_class_types = {
            "address": Address,
            "address_kana": AddressKana,
            "address_kanji": AddressKanji,
            "ownership_declaration": OwnershipDeclaration,
            "verification": Verification,
        }

    class Controller(StripeObject):
        class Application(StripeObject):
            loss_liable: bool
            onboarding_owner: bool
            pricing_controls: bool

        class Dashboard(StripeObject):
            type: Literal["express", "full", "none"]

        application: Optional[Application]
        dashboard: Optional[Dashboard]
        is_controller: Optional[bool]
        type: Literal["account", "application"]
        _inner_class_types = {
            "application": Application,
            "dashboard": Dashboard,
        }

    class FutureRequirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_dob_age_under_18",
                "invalid_representative_country",
                "invalid_street_address",
                "invalid_tos_acceptance",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
            ]
            reason: str
            requirement: str

        alternatives: Optional[List[Alternative]]
        current_deadline: Optional[int]
        currently_due: Optional[List[str]]
        disabled_reason: Optional[str]
        errors: Optional[List[Error]]
        eventually_due: Optional[List[str]]
        past_due: Optional[List[str]]
        pending_verification: Optional[List[str]]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Requirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_dob_age_under_18",
                "invalid_representative_country",
                "invalid_street_address",
                "invalid_tos_acceptance",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
            ]
            reason: str
            requirement: str

        alternatives: Optional[List[Alternative]]
        current_deadline: Optional[int]
        currently_due: Optional[List[str]]
        disabled_reason: Optional[str]
        errors: Optional[List[Error]]
        eventually_due: Optional[List[str]]
        past_due: Optional[List[str]]
        pending_verification: Optional[List[str]]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Settings(StripeObject):
        class BacsDebitPayments(StripeObject):
            display_name: Optional[str]

        class Branding(StripeObject):
            icon: Optional[ExpandableField["File"]]
            logo: Optional[ExpandableField["File"]]
            primary_color: Optional[str]
            secondary_color: Optional[str]

        class CardIssuing(StripeObject):
            class TosAcceptance(StripeObject):
                date: Optional[int]
                ip: Optional[str]
                user_agent: Optional[str]

            tos_acceptance: Optional[TosAcceptance]
            _inner_class_types = {"tos_acceptance": TosAcceptance}

        class CardPayments(StripeObject):
            class DeclineOn(StripeObject):
                avs_failure: bool
                cvc_failure: bool

            decline_on: Optional[DeclineOn]
            statement_descriptor_prefix: Optional[str]
            statement_descriptor_prefix_kana: Optional[str]
            statement_descriptor_prefix_kanji: Optional[str]
            _inner_class_types = {"decline_on": DeclineOn}

        class Dashboard(StripeObject):
            display_name: Optional[str]
            timezone: Optional[str]

        class Payments(StripeObject):
            statement_descriptor: Optional[str]
            statement_descriptor_kana: Optional[str]
            statement_descriptor_kanji: Optional[str]
            statement_descriptor_prefix_kana: Optional[str]
            statement_descriptor_prefix_kanji: Optional[str]

        class Payouts(StripeObject):
            class Schedule(StripeObject):
                delay_days: int
                interval: str
                monthly_anchor: Optional[int]
                weekly_anchor: Optional[str]

            debit_negative_balances: bool
            schedule: Schedule
            statement_descriptor: Optional[str]
            _inner_class_types = {"schedule": Schedule}

        class SepaDebitPayments(StripeObject):
            creditor_id: Optional[str]

        class TaxForms(StripeObject):
            consented_to_paperless_delivery: bool

        class Treasury(StripeObject):
            class TosAcceptance(StripeObject):
                date: Optional[int]
                ip: Optional[str]
                user_agent: Optional[str]

            tos_acceptance: Optional[TosAcceptance]
            _inner_class_types = {"tos_acceptance": TosAcceptance}

        bacs_debit_payments: Optional[BacsDebitPayments]
        branding: Branding
        card_issuing: Optional[CardIssuing]
        card_payments: CardPayments
        dashboard: Dashboard
        payments: Payments
        payouts: Optional[Payouts]
        sepa_debit_payments: Optional[SepaDebitPayments]
        tax_forms: Optional[TaxForms]
        treasury: Optional[Treasury]
        _inner_class_types = {
            "bacs_debit_payments": BacsDebitPayments,
            "branding": Branding,
            "card_issuing": CardIssuing,
            "card_payments": CardPayments,
            "dashboard": Dashboard,
            "payments": Payments,
            "payouts": Payouts,
            "sepa_debit_payments": SepaDebitPayments,
            "tax_forms": TaxForms,
            "treasury": Treasury,
        }

    class TosAcceptance(StripeObject):
        date: Optional[int]
        ip: Optional[str]
        service_agreement: Optional[str]
        user_agent: Optional[str]

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_token: NotRequired["str|None"]
            business_profile: NotRequired[
                "Account.CreateParamsBusinessProfile|None"
            ]
            business_type: NotRequired[
                "Literal['company', 'government_entity', 'individual', 'non_profit']|None"
            ]
            capabilities: NotRequired["Account.CreateParamsCapabilities|None"]
            company: NotRequired["Account.CreateParamsCompany|None"]
            controller: NotRequired["Account.CreateParamsController|None"]
            country: NotRequired["str|None"]
            default_currency: NotRequired["str|None"]
            documents: NotRequired["Account.CreateParamsDocuments|None"]
            email: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            external_account: NotRequired["str|None"]
            individual: NotRequired["Account.CreateParamsIndividual|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            settings: NotRequired["Account.CreateParamsSettings|None"]
            tos_acceptance: NotRequired[
                "Account.CreateParamsTosAcceptance|None"
            ]
            type: NotRequired["Literal['custom', 'express', 'standard']|None"]

        class CreateParamsTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            service_agreement: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class CreateParamsSettings(TypedDict):
            branding: NotRequired["Account.CreateParamsSettingsBranding|None"]
            card_issuing: NotRequired[
                "Account.CreateParamsSettingsCardIssuing|None"
            ]
            card_payments: NotRequired[
                "Account.CreateParamsSettingsCardPayments|None"
            ]
            payments: NotRequired["Account.CreateParamsSettingsPayments|None"]
            payouts: NotRequired["Account.CreateParamsSettingsPayouts|None"]
            tax_forms: NotRequired["Account.CreateParamsSettingsTaxForms|None"]
            treasury: NotRequired["Account.CreateParamsSettingsTreasury|None"]

        class CreateParamsSettingsTreasury(TypedDict):
            tos_acceptance: NotRequired[
                "Account.CreateParamsSettingsTreasuryTosAcceptance|None"
            ]

        class CreateParamsSettingsTreasuryTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["Literal['']|str|None"]

        class CreateParamsSettingsTaxForms(TypedDict):
            consented_to_paperless_delivery: NotRequired["bool|None"]

        class CreateParamsSettingsPayouts(TypedDict):
            debit_negative_balances: NotRequired["bool|None"]
            schedule: NotRequired[
                "Account.CreateParamsSettingsPayoutsSchedule|None"
            ]
            statement_descriptor: NotRequired["str|None"]

        class CreateParamsSettingsPayoutsSchedule(TypedDict):
            delay_days: NotRequired["Literal['minimum']|int|None"]
            interval: NotRequired[
                "Literal['daily', 'manual', 'monthly', 'weekly']|None"
            ]
            monthly_anchor: NotRequired["int|None"]
            weekly_anchor: NotRequired[
                "Literal['friday', 'monday', 'saturday', 'sunday', 'thursday', 'tuesday', 'wednesday']|None"
            ]

        class CreateParamsSettingsPayments(TypedDict):
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_kana: NotRequired["str|None"]
            statement_descriptor_kanji: NotRequired["str|None"]

        class CreateParamsSettingsCardPayments(TypedDict):
            decline_on: NotRequired[
                "Account.CreateParamsSettingsCardPaymentsDeclineOn|None"
            ]
            statement_descriptor_prefix: NotRequired["str|None"]
            statement_descriptor_prefix_kana: NotRequired[
                "Literal['']|str|None"
            ]
            statement_descriptor_prefix_kanji: NotRequired[
                "Literal['']|str|None"
            ]

        class CreateParamsSettingsCardPaymentsDeclineOn(TypedDict):
            avs_failure: NotRequired["bool|None"]
            cvc_failure: NotRequired["bool|None"]

        class CreateParamsSettingsCardIssuing(TypedDict):
            tos_acceptance: NotRequired[
                "Account.CreateParamsSettingsCardIssuingTosAcceptance|None"
            ]

        class CreateParamsSettingsCardIssuingTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["Literal['']|str|None"]

        class CreateParamsSettingsBranding(TypedDict):
            icon: NotRequired["str|None"]
            logo: NotRequired["str|None"]
            primary_color: NotRequired["str|None"]
            secondary_color: NotRequired["str|None"]

        class CreateParamsIndividual(TypedDict):
            address: NotRequired["Account.CreateParamsIndividualAddress|None"]
            address_kana: NotRequired[
                "Account.CreateParamsIndividualAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Account.CreateParamsIndividualAddressKanji|None"
            ]
            dob: NotRequired[
                "Literal['']|Account.CreateParamsIndividualDob|None"
            ]
            email: NotRequired["str|None"]
            first_name: NotRequired["str|None"]
            first_name_kana: NotRequired["str|None"]
            first_name_kanji: NotRequired["str|None"]
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            gender: NotRequired["str|None"]
            id_number: NotRequired["str|None"]
            id_number_secondary: NotRequired["str|None"]
            last_name: NotRequired["str|None"]
            last_name_kana: NotRequired["str|None"]
            last_name_kanji: NotRequired["str|None"]
            maiden_name: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            phone: NotRequired["str|None"]
            political_exposure: NotRequired["Literal['existing', 'none']|None"]
            registered_address: NotRequired[
                "Account.CreateParamsIndividualRegisteredAddress|None"
            ]
            ssn_last_4: NotRequired["str|None"]
            verification: NotRequired[
                "Account.CreateParamsIndividualVerification|None"
            ]

        class CreateParamsIndividualVerification(TypedDict):
            additional_document: NotRequired[
                "Account.CreateParamsIndividualVerificationAdditionalDocument|None"
            ]
            document: NotRequired[
                "Account.CreateParamsIndividualVerificationDocument|None"
            ]

        class CreateParamsIndividualVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsIndividualVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsIndividualRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsIndividualDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsIndividualAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsIndividualAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsIndividualAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsDocuments(TypedDict):
            bank_account_ownership_verification: NotRequired[
                "Account.CreateParamsDocumentsBankAccountOwnershipVerification|None"
            ]
            company_license: NotRequired[
                "Account.CreateParamsDocumentsCompanyLicense|None"
            ]
            company_memorandum_of_association: NotRequired[
                "Account.CreateParamsDocumentsCompanyMemorandumOfAssociation|None"
            ]
            company_ministerial_decree: NotRequired[
                "Account.CreateParamsDocumentsCompanyMinisterialDecree|None"
            ]
            company_registration_verification: NotRequired[
                "Account.CreateParamsDocumentsCompanyRegistrationVerification|None"
            ]
            company_tax_id_verification: NotRequired[
                "Account.CreateParamsDocumentsCompanyTaxIdVerification|None"
            ]
            proof_of_registration: NotRequired[
                "Account.CreateParamsDocumentsProofOfRegistration|None"
            ]

        class CreateParamsDocumentsProofOfRegistration(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsCompanyTaxIdVerification(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsCompanyRegistrationVerification(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsCompanyMinisterialDecree(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsCompanyMemorandumOfAssociation(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsCompanyLicense(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsDocumentsBankAccountOwnershipVerification(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsController(TypedDict):
            application: NotRequired[
                "Account.CreateParamsControllerApplication|None"
            ]
            dashboard: NotRequired[
                "Account.CreateParamsControllerDashboard|None"
            ]

        class CreateParamsControllerDashboard(TypedDict):
            type: NotRequired["Literal['express', 'full', 'none']|None"]

        class CreateParamsControllerApplication(TypedDict):
            loss_liable: bool
            onboarding_owner: NotRequired["bool|None"]
            pricing_controls: NotRequired["bool|None"]

        class CreateParamsCompany(TypedDict):
            address: NotRequired["Account.CreateParamsCompanyAddress|None"]
            address_kana: NotRequired[
                "Account.CreateParamsCompanyAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Account.CreateParamsCompanyAddressKanji|None"
            ]
            directors_provided: NotRequired["bool|None"]
            executives_provided: NotRequired["bool|None"]
            export_license_id: NotRequired["str|None"]
            export_purpose_code: NotRequired["str|None"]
            name: NotRequired["str|None"]
            name_kana: NotRequired["str|None"]
            name_kanji: NotRequired["str|None"]
            owners_provided: NotRequired["bool|None"]
            ownership_declaration: NotRequired[
                "Account.CreateParamsCompanyOwnershipDeclaration|None"
            ]
            phone: NotRequired["str|None"]
            registration_number: NotRequired["str|None"]
            structure: NotRequired[
                "Literal['']|Literal['free_zone_establishment', 'free_zone_llc', 'government_instrumentality', 'governmental_unit', 'incorporated_non_profit', 'incorporated_partnership', 'limited_liability_partnership', 'llc', 'multi_member_llc', 'private_company', 'private_corporation', 'private_partnership', 'public_company', 'public_corporation', 'public_partnership', 'single_member_llc', 'sole_establishment', 'sole_proprietorship', 'tax_exempt_government_instrumentality', 'unincorporated_association', 'unincorporated_non_profit', 'unincorporated_partnership']|None"
            ]
            tax_id: NotRequired["str|None"]
            tax_id_registrar: NotRequired["str|None"]
            vat_id: NotRequired["str|None"]
            verification: NotRequired[
                "Account.CreateParamsCompanyVerification|None"
            ]

        class CreateParamsCompanyVerification(TypedDict):
            document: NotRequired[
                "Account.CreateParamsCompanyVerificationDocument|None"
            ]

        class CreateParamsCompanyVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsCompanyOwnershipDeclaration(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class CreateParamsCompanyAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsCompanyAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsCompanyAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsCapabilities(TypedDict):
            acss_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAcssDebitPayments|None"
            ]
            affirm_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAffirmPayments|None"
            ]
            afterpay_clearpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAfterpayClearpayPayments|None"
            ]
            au_becs_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAuBecsDebitPayments|None"
            ]
            bacs_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBacsDebitPayments|None"
            ]
            bancontact_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBancontactPayments|None"
            ]
            bank_transfer_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBankTransferPayments|None"
            ]
            blik_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBlikPayments|None"
            ]
            boleto_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBoletoPayments|None"
            ]
            card_issuing: NotRequired[
                "Account.CreateParamsCapabilitiesCardIssuing|None"
            ]
            card_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCardPayments|None"
            ]
            cartes_bancaires_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCartesBancairesPayments|None"
            ]
            cashapp_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCashappPayments|None"
            ]
            eps_payments: NotRequired[
                "Account.CreateParamsCapabilitiesEpsPayments|None"
            ]
            fpx_payments: NotRequired[
                "Account.CreateParamsCapabilitiesFpxPayments|None"
            ]
            giropay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesGiropayPayments|None"
            ]
            grabpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesGrabpayPayments|None"
            ]
            ideal_payments: NotRequired[
                "Account.CreateParamsCapabilitiesIdealPayments|None"
            ]
            india_international_payments: NotRequired[
                "Account.CreateParamsCapabilitiesIndiaInternationalPayments|None"
            ]
            jcb_payments: NotRequired[
                "Account.CreateParamsCapabilitiesJcbPayments|None"
            ]
            klarna_payments: NotRequired[
                "Account.CreateParamsCapabilitiesKlarnaPayments|None"
            ]
            konbini_payments: NotRequired[
                "Account.CreateParamsCapabilitiesKonbiniPayments|None"
            ]
            legacy_payments: NotRequired[
                "Account.CreateParamsCapabilitiesLegacyPayments|None"
            ]
            link_payments: NotRequired[
                "Account.CreateParamsCapabilitiesLinkPayments|None"
            ]
            oxxo_payments: NotRequired[
                "Account.CreateParamsCapabilitiesOxxoPayments|None"
            ]
            p24_payments: NotRequired[
                "Account.CreateParamsCapabilitiesP24Payments|None"
            ]
            paynow_payments: NotRequired[
                "Account.CreateParamsCapabilitiesPaynowPayments|None"
            ]
            paypal_payments: NotRequired[
                "Account.CreateParamsCapabilitiesPaypalPayments|None"
            ]
            promptpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesPromptpayPayments|None"
            ]
            sepa_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesSepaDebitPayments|None"
            ]
            sofort_payments: NotRequired[
                "Account.CreateParamsCapabilitiesSofortPayments|None"
            ]
            tax_reporting_us_1099_k: NotRequired[
                "Account.CreateParamsCapabilitiesTaxReportingUs1099K|None"
            ]
            tax_reporting_us_1099_misc: NotRequired[
                "Account.CreateParamsCapabilitiesTaxReportingUs1099Misc|None"
            ]
            transfers: NotRequired[
                "Account.CreateParamsCapabilitiesTransfers|None"
            ]
            treasury: NotRequired[
                "Account.CreateParamsCapabilitiesTreasury|None"
            ]
            us_bank_account_ach_payments: NotRequired[
                "Account.CreateParamsCapabilitiesUsBankAccountAchPayments|None"
            ]
            zip_payments: NotRequired[
                "Account.CreateParamsCapabilitiesZipPayments|None"
            ]

        class CreateParamsCapabilitiesZipPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesUsBankAccountAchPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesTreasury(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesTransfers(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesTaxReportingUs1099Misc(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesTaxReportingUs1099K(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesSofortPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesSepaDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesPromptpayPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesPaypalPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesPaynowPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesP24Payments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesOxxoPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesLinkPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesLegacyPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesKonbiniPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesKlarnaPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesJcbPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesIndiaInternationalPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesIdealPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesGrabpayPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesGiropayPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesFpxPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesEpsPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesCashappPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesCartesBancairesPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesCardPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesCardIssuing(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesBoletoPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesBlikPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesBankTransferPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesBancontactPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesBacsDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesAuBecsDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesAfterpayClearpayPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesAffirmPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsCapabilitiesAcssDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]

        class CreateParamsBusinessProfile(TypedDict):
            mcc: NotRequired["str|None"]
            monthly_estimated_revenue: NotRequired[
                "Account.CreateParamsBusinessProfileMonthlyEstimatedRevenue|None"
            ]
            name: NotRequired["str|None"]
            product_description: NotRequired["str|None"]
            support_address: NotRequired[
                "Account.CreateParamsBusinessProfileSupportAddress|None"
            ]
            support_email: NotRequired["str|None"]
            support_phone: NotRequired["str|None"]
            support_url: NotRequired["Literal['']|str|None"]
            url: NotRequired["str|None"]

        class CreateParamsBusinessProfileSupportAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsBusinessProfileMonthlyEstimatedRevenue(TypedDict):
            amount: int
            currency: str

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["Account.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class PersonsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            relationship: NotRequired["Account.PersonsParamsRelationship|None"]
            starting_after: NotRequired["str|None"]

        class PersonsParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            executive: NotRequired["bool|None"]
            owner: NotRequired["bool|None"]
            representative: NotRequired["bool|None"]

        class RejectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            reason: str

        class RetrieveCapabilityParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyCapabilityParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            requested: NotRequired["bool|None"]

        class ListCapabilitiesParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateExternalAccountParams(RequestOptions):
            default_for_currency: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            external_account: str
            metadata: NotRequired["Dict[str, str]|None"]

        class RetrieveExternalAccountParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyExternalAccountParams(RequestOptions):
            account_holder_name: NotRequired["str|None"]
            account_holder_type: NotRequired[
                "Literal['']|Literal['company', 'individual']|None"
            ]
            account_type: NotRequired[
                "Literal['checking', 'futsu', 'savings', 'toza']|None"
            ]
            address_city: NotRequired["str|None"]
            address_country: NotRequired["str|None"]
            address_line1: NotRequired["str|None"]
            address_line2: NotRequired["str|None"]
            address_state: NotRequired["str|None"]
            address_zip: NotRequired["str|None"]
            default_for_currency: NotRequired["bool|None"]
            documents: NotRequired[
                "Account.ModifyExternalAccountParamsDocuments|None"
            ]
            exp_month: NotRequired["str|None"]
            exp_year: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: NotRequired["str|None"]

        class ModifyExternalAccountParamsDocuments(TypedDict):
            bank_account_ownership_verification: NotRequired[
                "Account.ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification|None"
            ]

        class ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification(
            TypedDict,
        ):
            files: NotRequired["List[str]|None"]

        class DeleteExternalAccountParams(RequestOptions):
            pass

        class ListExternalAccountsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            object: NotRequired["Literal['bank_account', 'card']|None"]
            starting_after: NotRequired["str|None"]

        class CreateLoginLinkParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreatePersonParams(RequestOptions):
            address: NotRequired["Account.CreatePersonParamsAddress|None"]
            address_kana: NotRequired[
                "Account.CreatePersonParamsAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Account.CreatePersonParamsAddressKanji|None"
            ]
            dob: NotRequired["Literal['']|Account.CreatePersonParamsDob|None"]
            documents: NotRequired["Account.CreatePersonParamsDocuments|None"]
            email: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            first_name: NotRequired["str|None"]
            first_name_kana: NotRequired["str|None"]
            first_name_kanji: NotRequired["str|None"]
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            gender: NotRequired["str|None"]
            id_number: NotRequired["str|None"]
            id_number_secondary: NotRequired["str|None"]
            last_name: NotRequired["str|None"]
            last_name_kana: NotRequired["str|None"]
            last_name_kanji: NotRequired["str|None"]
            maiden_name: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            nationality: NotRequired["str|None"]
            person_token: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            political_exposure: NotRequired["str|None"]
            registered_address: NotRequired[
                "Account.CreatePersonParamsRegisteredAddress|None"
            ]
            relationship: NotRequired[
                "Account.CreatePersonParamsRelationship|None"
            ]
            ssn_last_4: NotRequired["str|None"]
            verification: NotRequired[
                "Account.CreatePersonParamsVerification|None"
            ]

        class CreatePersonParamsVerification(TypedDict):
            additional_document: NotRequired[
                "Account.CreatePersonParamsVerificationAdditionalDocument|None"
            ]
            document: NotRequired[
                "Account.CreatePersonParamsVerificationDocument|None"
            ]

        class CreatePersonParamsVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreatePersonParamsVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreatePersonParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            executive: NotRequired["bool|None"]
            owner: NotRequired["bool|None"]
            percent_ownership: NotRequired["Literal['']|float|None"]
            representative: NotRequired["bool|None"]
            title: NotRequired["str|None"]

        class CreatePersonParamsRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreatePersonParamsDocuments(TypedDict):
            company_authorization: NotRequired[
                "Account.CreatePersonParamsDocumentsCompanyAuthorization|None"
            ]
            passport: NotRequired[
                "Account.CreatePersonParamsDocumentsPassport|None"
            ]
            visa: NotRequired["Account.CreatePersonParamsDocumentsVisa|None"]

        class CreatePersonParamsDocumentsVisa(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreatePersonParamsDocumentsPassport(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreatePersonParamsDocumentsCompanyAuthorization(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreatePersonParamsDob(TypedDict):
            day: int
            month: int
            year: int

        class CreatePersonParamsAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreatePersonParamsAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreatePersonParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class RetrievePersonParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyPersonParams(RequestOptions):
            address: NotRequired["Account.ModifyPersonParamsAddress|None"]
            address_kana: NotRequired[
                "Account.ModifyPersonParamsAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Account.ModifyPersonParamsAddressKanji|None"
            ]
            dob: NotRequired["Literal['']|Account.ModifyPersonParamsDob|None"]
            documents: NotRequired["Account.ModifyPersonParamsDocuments|None"]
            email: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            first_name: NotRequired["str|None"]
            first_name_kana: NotRequired["str|None"]
            first_name_kanji: NotRequired["str|None"]
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            gender: NotRequired["str|None"]
            id_number: NotRequired["str|None"]
            id_number_secondary: NotRequired["str|None"]
            last_name: NotRequired["str|None"]
            last_name_kana: NotRequired["str|None"]
            last_name_kanji: NotRequired["str|None"]
            maiden_name: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            nationality: NotRequired["str|None"]
            person_token: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            political_exposure: NotRequired["str|None"]
            registered_address: NotRequired[
                "Account.ModifyPersonParamsRegisteredAddress|None"
            ]
            relationship: NotRequired[
                "Account.ModifyPersonParamsRelationship|None"
            ]
            ssn_last_4: NotRequired["str|None"]
            verification: NotRequired[
                "Account.ModifyPersonParamsVerification|None"
            ]

        class ModifyPersonParamsVerification(TypedDict):
            additional_document: NotRequired[
                "Account.ModifyPersonParamsVerificationAdditionalDocument|None"
            ]
            document: NotRequired[
                "Account.ModifyPersonParamsVerificationDocument|None"
            ]

        class ModifyPersonParamsVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class ModifyPersonParamsVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class ModifyPersonParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            executive: NotRequired["bool|None"]
            owner: NotRequired["bool|None"]
            percent_ownership: NotRequired["Literal['']|float|None"]
            representative: NotRequired["bool|None"]
            title: NotRequired["str|None"]

        class ModifyPersonParamsRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyPersonParamsDocuments(TypedDict):
            company_authorization: NotRequired[
                "Account.ModifyPersonParamsDocumentsCompanyAuthorization|None"
            ]
            passport: NotRequired[
                "Account.ModifyPersonParamsDocumentsPassport|None"
            ]
            visa: NotRequired["Account.ModifyPersonParamsDocumentsVisa|None"]

        class ModifyPersonParamsDocumentsVisa(TypedDict):
            files: NotRequired["List[str]|None"]

        class ModifyPersonParamsDocumentsPassport(TypedDict):
            files: NotRequired["List[str]|None"]

        class ModifyPersonParamsDocumentsCompanyAuthorization(TypedDict):
            files: NotRequired["List[str]|None"]

        class ModifyPersonParamsDob(TypedDict):
            day: int
            month: int
            year: int

        class ModifyPersonParamsAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class ModifyPersonParamsAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class ModifyPersonParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class DeletePersonParams(RequestOptions):
            pass

        class ListPersonsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            relationship: NotRequired[
                "Account.ListPersonsParamsRelationship|None"
            ]
            starting_after: NotRequired["str|None"]

        class ListPersonsParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            executive: NotRequired["bool|None"]
            owner: NotRequired["bool|None"]
            representative: NotRequired["bool|None"]

    business_profile: Optional[BusinessProfile]
    business_type: Optional[
        Literal["company", "government_entity", "individual", "non_profit"]
    ]
    capabilities: Optional[Capabilities]
    charges_enabled: Optional[bool]
    company: Optional[Company]
    controller: Optional[Controller]
    country: Optional[str]
    created: Optional[int]
    default_currency: Optional[str]
    details_submitted: Optional[bool]
    email: Optional[str]
    external_accounts: Optional[ListObject[Union["BankAccount", "Card"]]]
    future_requirements: Optional[FutureRequirements]
    id: str
    individual: Optional["Person"]
    metadata: Optional[Dict[str, str]]
    object: Literal["account"]
    payouts_enabled: Optional[bool]
    requirements: Optional[Requirements]
    settings: Optional[Settings]
    tos_acceptance: Optional[TosAcceptance]
    type: Optional[Literal["custom", "express", "standard"]]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateParams"]
    ) -> "Account":
        return cast(
            "Account",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Account.DeleteParams"]
    ) -> "Account":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Account",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Account.DeleteParams"]) -> "Account":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListParams"]
    ) -> ListObject["Account"]:
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
    def _cls_persons(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.PersonsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_persons")
    def persons(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.PersonsParams"]
    ):
        return self._request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_reject(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/reject".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reject")
    def reject(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ):
        return self._request(
            "post",
            "/v1/accounts/{account}/reject".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    # We are not adding a helper for capabilities here as the Account object already has a
    # capabilities property which is a hash and not the sub-list of capabilities.

    @classmethod
    def retrieve(cls, id=None, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def modify(cls, id=None, **params):
        url = cls._build_instance_url(id)
        return cls._static_request("post", url, params=params)

    @classmethod
    def _build_instance_url(cls, sid):
        if not sid:
            return "/v1/account"
        base = cls.class_url()
        extn = quote_plus(sid)
        return "%s/%s" % (base, extn)

    def instance_url(self):
        return self._build_instance_url(self.get("id"))

    def deauthorize(self, **params):
        params["stripe_user_id"] = self.id
        return oauth.OAuth.deauthorize(**params)

    def serialize(self, previous):
        params = super(Account, self).serialize(previous)
        previous = previous or self._previous or {}

        for k, v in iter(self.items()):
            if (
                k == "individual"
                and isinstance(v, api_resources.Person)
                and k not in params
            ):
                params[k] = v.serialize(previous.get(k, None))

        return params

    @classmethod
    def retrieve_capability(
        cls,
        account: str,
        capability: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RetrieveCapabilityParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/capabilities/{capability}".format(
                account=util.sanitize_id(account),
                capability=util.sanitize_id(capability),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_capability(
        cls,
        account: str,
        capability: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ModifyCapabilityParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/capabilities/{capability}".format(
                account=util.sanitize_id(account),
                capability=util.sanitize_id(capability),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_capabilities(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListCapabilitiesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/capabilities".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_external_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateExternalAccountParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/external_accounts".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RetrieveExternalAccountParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ModifyExternalAccountParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.DeleteExternalAccountParams"]
    ):
        return cls._static_request(
            "delete",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_external_accounts(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListExternalAccountsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/external_accounts".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_login_link(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateLoginLinkParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/login_links".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_person(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreatePersonParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RetrievePersonParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ModifyPersonParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.DeletePersonParams"]
    ):
        return cls._static_request(
            "delete",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_persons(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListPersonsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    _inner_class_types = {
        "business_profile": BusinessProfile,
        "capabilities": Capabilities,
        "company": Company,
        "controller": Controller,
        "future_requirements": FutureRequirements,
        "requirements": Requirements,
        "settings": Settings,
        "tos_acceptance": TosAcceptance,
    }
