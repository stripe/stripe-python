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
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, Union, cast, overload
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
    from stripe.api_resources.capability import Capability
    from stripe.api_resources.card import Card
    from stripe.api_resources.file import File
    from stripe.api_resources.login_link import LoginLink
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

    OBJECT_NAME: ClassVar[Literal["account"]] = "account"

    class BusinessProfile(StripeObject):
        class MonthlyEstimatedRevenue(StripeObject):
            amount: int
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """

        class SupportAddress(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        mcc: Optional[str]
        """
        [The merchant category code for the account](https://stripe.com/docs/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide.
        """
        monthly_estimated_revenue: Optional[MonthlyEstimatedRevenue]
        name: Optional[str]
        """
        The customer-facing business name.
        """
        product_description: Optional[str]
        """
        Internal-only description of the product sold or service provided by the business. It's used by Stripe for risk and underwriting purposes.
        """
        support_address: Optional[SupportAddress]
        """
        A publicly available mailing address for sending support issues to.
        """
        support_email: Optional[str]
        """
        A publicly available email address for sending support issues to.
        """
        support_phone: Optional[str]
        """
        A publicly available phone number to call with support issues.
        """
        support_url: Optional[str]
        """
        A publicly available website for handling support issues.
        """
        url: Optional[str]
        """
        The business's publicly available website.
        """
        _inner_class_types = {
            "monthly_estimated_revenue": MonthlyEstimatedRevenue,
            "support_address": SupportAddress,
        }

    class Capabilities(StripeObject):
        acss_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Canadian pre-authorized debits payments capability of the account, or whether the account can directly process Canadian pre-authorized debits charges.
        """
        affirm_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Affirm capability of the account, or whether the account can directly process Affirm charges.
        """
        afterpay_clearpay_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the Afterpay Clearpay capability of the account, or whether the account can directly process Afterpay Clearpay charges.
        """
        au_becs_debit_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the BECS Direct Debit (AU) payments capability of the account, or whether the account can directly process BECS Direct Debit (AU) charges.
        """
        bacs_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Bacs Direct Debits payments capability of the account, or whether the account can directly process Bacs Direct Debits charges.
        """
        bancontact_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Bancontact payments capability of the account, or whether the account can directly process Bancontact charges.
        """
        bank_transfer_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the customer_balance payments capability of the account, or whether the account can directly process customer_balance charges.
        """
        blik_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the blik payments capability of the account, or whether the account can directly process blik charges.
        """
        boleto_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the boleto payments capability of the account, or whether the account can directly process boleto charges.
        """
        card_issuing: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the card issuing capability of the account, or whether you can use Issuing to distribute funds on cards
        """
        card_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the card payments capability of the account, or whether the account can directly process credit and debit card charges.
        """
        cartes_bancaires_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the Cartes Bancaires payments capability of the account, or whether the account can directly process Cartes Bancaires card charges in EUR currency.
        """
        cashapp_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Cash App Pay capability of the account, or whether the account can directly process Cash App Pay payments.
        """
        eps_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the EPS payments capability of the account, or whether the account can directly process EPS charges.
        """
        fpx_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the FPX payments capability of the account, or whether the account can directly process FPX charges.
        """
        giropay_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the giropay payments capability of the account, or whether the account can directly process giropay charges.
        """
        grabpay_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the GrabPay payments capability of the account, or whether the account can directly process GrabPay charges.
        """
        ideal_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the iDEAL payments capability of the account, or whether the account can directly process iDEAL charges.
        """
        india_international_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the india_international_payments capability of the account, or whether the account can process international charges (non INR) in India.
        """
        jcb_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the JCB payments capability of the account, or whether the account (Japan only) can directly process JCB credit card charges in JPY currency.
        """
        klarna_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Klarna payments capability of the account, or whether the account can directly process Klarna charges.
        """
        konbini_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the konbini payments capability of the account, or whether the account can directly process konbini charges.
        """
        legacy_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the legacy payments capability of the account.
        """
        link_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the link_payments capability of the account, or whether the account can directly process Link charges.
        """
        oxxo_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the OXXO payments capability of the account, or whether the account can directly process OXXO charges.
        """
        p24_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the P24 payments capability of the account, or whether the account can directly process P24 charges.
        """
        paynow_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the paynow payments capability of the account, or whether the account can directly process paynow charges.
        """
        promptpay_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the promptpay payments capability of the account, or whether the account can directly process promptpay charges.
        """
        sepa_debit_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the SEPA Direct Debits payments capability of the account, or whether the account can directly process SEPA Direct Debits charges.
        """
        sofort_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Sofort payments capability of the account, or whether the account can directly process Sofort charges.
        """
        tax_reporting_us_1099_k: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the tax reporting 1099-K (US) capability of the account.
        """
        tax_reporting_us_1099_misc: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the tax reporting 1099-MISC (US) capability of the account.
        """
        transfers: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the transfers capability of the account, or whether your platform can transfer funds to the account.
        """
        treasury: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the banking capability, or whether the account can have bank accounts.
        """
        us_bank_account_ach_payments: Optional[
            Literal["active", "inactive", "pending"]
        ]
        """
        The status of the US bank account ACH payments capability of the account, or whether the account can directly process US bank account charges.
        """
        zip_payments: Optional[Literal["active", "inactive", "pending"]]
        """
        The status of the Zip capability of the account, or whether the account can directly process Zip charges.
        """

    class Company(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        class AddressKana(StripeObject):
            city: Optional[str]
            """
            City/Ward.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Block/Building number.
            """
            line2: Optional[str]
            """
            Building details.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            Prefecture.
            """
            town: Optional[str]
            """
            Town/cho-me.
            """

        class AddressKanji(StripeObject):
            city: Optional[str]
            """
            City/Ward.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Block/Building number.
            """
            line2: Optional[str]
            """
            Building details.
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            Prefecture.
            """
            town: Optional[str]
            """
            Town/cho-me.
            """

        class OwnershipDeclaration(StripeObject):
            date: Optional[int]
            """
            The Unix timestamp marking when the beneficial owner attestation was made.
            """
            ip: Optional[str]
            """
            The IP address from which the beneficial owner attestation was made.
            """
            user_agent: Optional[str]
            """
            The user-agent string from the browser where the beneficial owner attestation was made.
            """

        class Verification(StripeObject):
            class Document(StripeObject):
                back: Optional[ExpandableField["File"]]
                """
                The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`.
                """
                details: Optional[str]
                """
                A user-displayable string describing the verification state of this document.
                """
                details_code: Optional[str]
                """
                One of `document_corrupt`, `document_expired`, `document_failed_copy`, `document_failed_greyscale`, `document_failed_other`, `document_failed_test_mode`, `document_fraudulent`, `document_incomplete`, `document_invalid`, `document_manipulated`, `document_not_readable`, `document_not_uploaded`, `document_type_not_supported`, or `document_too_large`. A machine-readable code specifying the verification state for this document.
                """
                front: Optional[ExpandableField["File"]]
                """
                The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`.
                """

            document: Document
            _inner_class_types = {"document": Document}

        address: Optional[Address]
        address_kana: Optional[AddressKana]
        """
        The Kana variation of the company's primary address (Japan only).
        """
        address_kanji: Optional[AddressKanji]
        """
        The Kanji variation of the company's primary address (Japan only).
        """
        directors_provided: Optional[bool]
        """
        Whether the company's directors have been provided. This Boolean will be `true` if you've manually indicated that all directors are provided via [the `directors_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-directors_provided).
        """
        executives_provided: Optional[bool]
        """
        Whether the company's executives have been provided. This Boolean will be `true` if you've manually indicated that all executives are provided via [the `executives_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-executives_provided), or if Stripe determined that sufficient executives were provided.
        """
        export_license_id: Optional[str]
        """
        The export license ID number of the company, also referred as Import Export Code (India only).
        """
        export_purpose_code: Optional[str]
        """
        The purpose code to use for export transactions (India only).
        """
        name: Optional[str]
        """
        The company's legal name.
        """
        name_kana: Optional[str]
        """
        The Kana variation of the company's legal name (Japan only).
        """
        name_kanji: Optional[str]
        """
        The Kanji variation of the company's legal name (Japan only).
        """
        owners_provided: Optional[bool]
        """
        Whether the company's owners have been provided. This Boolean will be `true` if you've manually indicated that all owners are provided via [the `owners_provided` parameter](https://stripe.com/docs/api/accounts/update#update_account-company-owners_provided), or if Stripe determined that sufficient owners were provided. Stripe determines ownership requirements using both the number of owners provided and their total percent ownership (calculated by adding the `percent_ownership` of each owner together).
        """
        ownership_declaration: Optional[OwnershipDeclaration]
        """
        This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
        """
        phone: Optional[str]
        """
        The company's phone number (used for verification).
        """
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
        """
        The category identifying the legal structure of the company or legal entity. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details.
        """
        tax_id_provided: Optional[bool]
        """
        Whether the company's business ID number was provided.
        """
        tax_id_registrar: Optional[str]
        """
        The jurisdiction in which the `tax_id` is registered (Germany-based companies only).
        """
        vat_id_provided: Optional[bool]
        """
        Whether the company's business VAT number was provided.
        """
        verification: Optional[Verification]
        """
        Information on the verification state of the company.
        """
        _inner_class_types = {
            "address": Address,
            "address_kana": AddressKana,
            "address_kanji": AddressKanji,
            "ownership_declaration": OwnershipDeclaration,
            "verification": Verification,
        }

    class Controller(StripeObject):
        is_controller: Optional[bool]
        """
        `true` if the Connect application retrieving the resource controls the account and can therefore exercise [platform controls](https://stripe.com/docs/connect/platform-controls-for-standard-accounts). Otherwise, this field is null.
        """
        type: Literal["account", "application"]
        """
        The controller type. Can be `application`, if a Connect application controls the account, or `account`, if the account controls itself.
        """

    class FutureRequirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            """
            Fields that can be provided to satisfy all fields in `original_fields_due`.
            """
            original_fields_due: List[str]
            """
            Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`.
            """

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_dob_age_under_minimum",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
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
            """
            The code for the type of error.
            """
            reason: str
            """
            An informative message that indicates the error type and provides additional details about the error.
            """
            requirement: str
            """
            The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.
            """

        alternatives: Optional[List[Alternative]]
        """
        Fields that are due and can be satisfied by providing the corresponding alternative fields instead.
        """
        current_deadline: Optional[int]
        """
        Date on which `future_requirements` merges with the main `requirements` hash and `future_requirements` becomes empty. After the transition, `currently_due` requirements may immediately become `past_due`, but the account may also be given a grace period depending on its enablement state prior to transitioning.
        """
        currently_due: Optional[List[str]]
        """
        Fields that need to be collected to keep the account enabled. If not collected by `future_requirements[current_deadline]`, these fields will transition to the main `requirements` hash.
        """
        disabled_reason: Optional[str]
        """
        This is typed as a string for consistency with `requirements.disabled_reason`.
        """
        errors: Optional[List[Error]]
        """
        Fields that are `currently_due` and need to be collected again because validation or verification failed.
        """
        eventually_due: Optional[List[str]]
        """
        Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well.
        """
        past_due: Optional[List[str]]
        """
        Fields that weren't collected by `requirements.current_deadline`. These fields need to be collected to enable the capability on the account. New fields will never appear here; `future_requirements.past_due` will always be a subset of `requirements.past_due`.
        """
        pending_verification: Optional[List[str]]
        """
        Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due` or `currently_due`.
        """
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Requirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            """
            Fields that can be provided to satisfy all fields in `original_fields_due`.
            """
            original_fields_due: List[str]
            """
            Fields that are due and can be satisfied by providing all fields in `alternative_fields_due`.
            """

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_dob_age_under_minimum",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
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
            """
            The code for the type of error.
            """
            reason: str
            """
            An informative message that indicates the error type and provides additional details about the error.
            """
            requirement: str
            """
            The specific user onboarding requirement field (in the requirements hash) that needs to be resolved.
            """

        alternatives: Optional[List[Alternative]]
        """
        Fields that are due and can be satisfied by providing the corresponding alternative fields instead.
        """
        current_deadline: Optional[int]
        """
        Date by which the fields in `currently_due` must be collected to keep the account enabled. These fields may disable the account sooner if the next threshold is reached before they are collected.
        """
        currently_due: Optional[List[str]]
        """
        Fields that need to be collected to keep the account enabled. If not collected by `current_deadline`, these fields appear in `past_due` as well, and the account is disabled.
        """
        disabled_reason: Optional[str]
        """
        If the account is disabled, this string describes why. [Learn more about handling verification issues](https://stripe.com/docs/connect/handling-api-verification). Can be `action_required.requested_capabilities`, `requirements.past_due`, `requirements.pending_verification`, `listed`, `platform_paused`, `rejected.fraud`, `rejected.incomplete_verification`, `rejected.listed`, `rejected.other`, `rejected.terms_of_service`, `under_review`, or `other`.
        """
        errors: Optional[List[Error]]
        """
        Fields that are `currently_due` and need to be collected again because validation or verification failed.
        """
        eventually_due: Optional[List[str]]
        """
        Fields that need to be collected assuming all volume thresholds are reached. As they become required, they appear in `currently_due` as well, and `current_deadline` becomes set.
        """
        past_due: Optional[List[str]]
        """
        Fields that weren't collected by `current_deadline`. These fields need to be collected to enable the account.
        """
        pending_verification: Optional[List[str]]
        """
        Fields that may become required depending on the results of verification or review. Will be an empty array unless an asynchronous verification is pending. If verification fails, these fields move to `eventually_due`, `currently_due`, or `past_due`.
        """
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Settings(StripeObject):
        class BacsDebitPayments(StripeObject):
            display_name: Optional[str]
            """
            The Bacs Direct Debit Display Name for this account. For payments made with Bacs Direct Debit, this will appear on the mandate, and as the statement descriptor.
            """

        class Branding(StripeObject):
            icon: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px.
            """
            logo: Optional[ExpandableField["File"]]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px.
            """
            primary_color: Optional[str]
            """
            A CSS hex color value representing the primary branding color for this account
            """
            secondary_color: Optional[str]
            """
            A CSS hex color value representing the secondary branding color for this account
            """

        class CardIssuing(StripeObject):
            class TosAcceptance(StripeObject):
                date: Optional[int]
                """
                The Unix timestamp marking when the account representative accepted the service agreement.
                """
                ip: Optional[str]
                """
                The IP address from which the account representative accepted the service agreement.
                """
                user_agent: Optional[str]
                """
                The user agent of the browser from which the account representative accepted the service agreement.
                """

            tos_acceptance: Optional[TosAcceptance]
            _inner_class_types = {"tos_acceptance": TosAcceptance}

        class CardPayments(StripeObject):
            class DeclineOn(StripeObject):
                avs_failure: bool
                """
                Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
                """
                cvc_failure: bool
                """
                Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
                """

            decline_on: Optional[DeclineOn]
            statement_descriptor_prefix: Optional[str]
            """
            The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion.
            """
            statement_descriptor_prefix_kana: Optional[str]
            """
            The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion.
            """
            statement_descriptor_prefix_kanji: Optional[str]
            """
            The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion.
            """
            _inner_class_types = {"decline_on": DeclineOn}

        class Dashboard(StripeObject):
            display_name: Optional[str]
            """
            The display name for this account. This is used on the Stripe Dashboard to differentiate between accounts.
            """
            timezone: Optional[str]
            """
            The timezone used in the Stripe Dashboard for this account. A list of possible time zone values is maintained at the [IANA Time Zone Database](http://www.iana.org/time-zones).
            """

        class Payments(StripeObject):
            statement_descriptor: Optional[str]
            """
            The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge.
            """
            statement_descriptor_kana: Optional[str]
            """
            The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only)
            """
            statement_descriptor_kanji: Optional[str]
            """
            The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only)
            """
            statement_descriptor_prefix_kana: Optional[str]
            """
            The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion.
            """
            statement_descriptor_prefix_kanji: Optional[str]
            """
            The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion.
            """

        class Payouts(StripeObject):
            class Schedule(StripeObject):
                delay_days: int
                """
                The number of days charges for the account will be held before being paid out.
                """
                interval: str
                """
                How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`.
                """
                monthly_anchor: Optional[int]
                """
                The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.
                """
                weekly_anchor: Optional[str]
                """
                The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly.
                """

            debit_negative_balances: bool
            """
            A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See our [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances) documentation for details. Default value is `false` for Custom accounts, otherwise `true`.
            """
            schedule: Schedule
            statement_descriptor: Optional[str]
            """
            The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
            """
            _inner_class_types = {"schedule": Schedule}

        class SepaDebitPayments(StripeObject):
            creditor_id: Optional[str]
            """
            SEPA creditor identifier that identifies the company making the payment.
            """

        class Treasury(StripeObject):
            class TosAcceptance(StripeObject):
                date: Optional[int]
                """
                The Unix timestamp marking when the account representative accepted the service agreement.
                """
                ip: Optional[str]
                """
                The IP address from which the account representative accepted the service agreement.
                """
                user_agent: Optional[str]
                """
                The user agent of the browser from which the account representative accepted the service agreement.
                """

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
            "treasury": Treasury,
        }

    class TosAcceptance(StripeObject):
        date: Optional[int]
        """
        The Unix timestamp marking when the account representative accepted their service agreement
        """
        ip: Optional[str]
        """
        The IP address from which the account representative accepted their service agreement
        """
        service_agreement: Optional[str]
        """
        The user's service agreement type
        """
        user_agent: Optional[str]
        """
        The user agent of the browser from which the account representative accepted their service agreement
        """

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_token: NotRequired["str|None"]
            """
            An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.
            """
            business_profile: NotRequired[
                "Account.CreateParamsBusinessProfile|None"
            ]
            """
            Business information about the account.
            """
            business_type: NotRequired[
                "Literal['company', 'government_entity', 'individual', 'non_profit']|None"
            ]
            """
            The business type.
            """
            capabilities: NotRequired["Account.CreateParamsCapabilities|None"]
            """
            Each key of the dictionary represents a capability, and each capability maps to its settings (e.g. whether it has been requested or not). Each capability will be inactive until you have provided its specific requirements and Stripe has verified them. An account may have some of its requested capabilities be active and some be inactive.
            """
            company: NotRequired["Account.CreateParamsCompany|None"]
            """
            Information about the company or business. This field is available for any `business_type`.
            """
            country: NotRequired["str|None"]
            """
            The country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you're creating an account is legally represented in Canada, you would use `CA` as the country for the account being created. Available countries include [Stripe's global markets](https://stripe.com/global) as well as countries where [cross-border payouts](https://stripe.com/docs/connect/cross-border-payouts) are supported.
            """
            default_currency: NotRequired["str|None"]
            """
            Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts).
            """
            documents: NotRequired["Account.CreateParamsDocuments|None"]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            email: NotRequired["str|None"]
            """
            The email address of the account holder. This is only to make the account easier to identify to you. Stripe only emails Custom accounts with your consent.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            external_account: NotRequired["str|None"]
            """
            A card or bank account to attach to the account for receiving [payouts](https://stripe.com/docs/connect/bank-debit-card-payouts) (you won't be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary, as documented in the `external_account` parameter for [bank account](https://stripe.com/docs/api#account_create_bank_account) creation.

            By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](https://stripe.com/docs/api#account_create_bank_account) or [card creation](https://stripe.com/docs/api#account_create_card) APIs.
            """
            individual: NotRequired["Account.CreateParamsIndividual|None"]
            """
            Information about the person represented by the account. This field is null unless `business_type` is set to `individual`.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            settings: NotRequired["Account.CreateParamsSettings|None"]
            """
            Options for customizing how the account functions within Stripe.
            """
            tos_acceptance: NotRequired[
                "Account.CreateParamsTosAcceptance|None"
            ]
            """
            Details on the account's acceptance of the [Stripe Services Agreement](https://stripe.com/docs/connect/updating-accounts#tos-acceptance).
            """
            type: NotRequired["Literal['custom', 'express', 'standard']|None"]
            """
            The type of Stripe account to create. May be one of `custom`, `express` or `standard`.
            """

        class CreateParamsTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the account representative accepted their service agreement.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the account representative accepted their service agreement.
            """
            service_agreement: NotRequired["str|None"]
            """
            The user's service agreement type.
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the account representative accepted their service agreement.
            """

        class CreateParamsSettings(TypedDict):
            branding: NotRequired["Account.CreateParamsSettingsBranding|None"]
            """
            Settings used to apply the account's branding to email receipts, invoices, Checkout, and other products.
            """
            card_issuing: NotRequired[
                "Account.CreateParamsSettingsCardIssuing|None"
            ]
            """
            Settings specific to the account's use of the Card Issuing product.
            """
            card_payments: NotRequired[
                "Account.CreateParamsSettingsCardPayments|None"
            ]
            """
            Settings specific to card charging on the account.
            """
            payments: NotRequired["Account.CreateParamsSettingsPayments|None"]
            """
            Settings that apply across payment methods for charging on the account.
            """
            payouts: NotRequired["Account.CreateParamsSettingsPayouts|None"]
            """
            Settings specific to the account's payouts.
            """
            treasury: NotRequired["Account.CreateParamsSettingsTreasury|None"]
            """
            Settings specific to the account's Treasury FinancialAccounts.
            """

        class CreateParamsSettingsTreasury(TypedDict):
            tos_acceptance: NotRequired[
                "Account.CreateParamsSettingsTreasuryTosAcceptance|None"
            ]
            """
            Details on the account's acceptance of the Stripe Treasury Services Agreement.
            """

        class CreateParamsSettingsTreasuryTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the account representative accepted the service agreement.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the account representative accepted the service agreement.
            """
            user_agent: NotRequired["Literal['']|str|None"]
            """
            The user agent of the browser from which the account representative accepted the service agreement.
            """

        class CreateParamsSettingsPayouts(TypedDict):
            debit_negative_balances: NotRequired["bool|None"]
            """
            A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://stripe.com/docs/connect/account-balances).
            """
            schedule: NotRequired[
                "Account.CreateParamsSettingsPayoutsSchedule|None"
            ]
            """
            Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://stripe.com/docs/connect/bank-transfers#payout-information) documentation.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
            """

        class CreateParamsSettingsPayoutsSchedule(TypedDict):
            delay_days: NotRequired["Literal['minimum']|int|None"]
            """
            The number of days charge funds are held before being paid out. May also be set to `minimum`, representing the lowest available value for the account country. Default is `minimum`. The `delay_days` parameter remains at the last configured value if `interval` is `manual`. [Learn more about controlling payout delay days](https://stripe.com/docs/connect/manage-payout-schedule).
            """
            interval: NotRequired[
                "Literal['daily', 'manual', 'monthly', 'weekly']|None"
            ]
            """
            How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.
            """
            monthly_anchor: NotRequired["int|None"]
            """
            The day of the month when available funds are paid out, specified as a number between 1--31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.
            """
            weekly_anchor: NotRequired[
                "Literal['friday', 'monday', 'saturday', 'sunday', 'thursday', 'tuesday', 'wednesday']|None"
            ]
            """
            The day of the week when available funds are paid out, specified as `monday`, `tuesday`, etc. (required and applicable only if `interval` is `weekly`.)
            """

        class CreateParamsSettingsPayments(TypedDict):
            statement_descriptor: NotRequired["str|None"]
            """
            The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge.
            """
            statement_descriptor_kana: NotRequired["str|None"]
            """
            The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only).
            """
            statement_descriptor_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only).
            """

        class CreateParamsSettingsCardPayments(TypedDict):
            decline_on: NotRequired[
                "Account.CreateParamsSettingsCardPaymentsDeclineOn|None"
            ]
            """
            Automatically declines certain charge types regardless of whether the card issuer accepted or declined the charge.
            """
            statement_descriptor_prefix: NotRequired["str|None"]
            """
            The default text that appears on credit card statements when a charge is made. This field prefixes any dynamic `statement_descriptor` specified on the charge. `statement_descriptor_prefix` is useful for maximizing descriptor space for the dynamic portion.
            """
            statement_descriptor_prefix_kana: NotRequired[
                "Literal['']|str|None"
            ]
            """
            The Kana variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kana` specified on the charge. `statement_descriptor_prefix_kana` is useful for maximizing descriptor space for the dynamic portion.
            """
            statement_descriptor_prefix_kanji: NotRequired[
                "Literal['']|str|None"
            ]
            """
            The Kanji variation of the default text that appears on credit card statements when a charge is made (Japan only). This field prefixes any dynamic `statement_descriptor_suffix_kanji` specified on the charge. `statement_descriptor_prefix_kanji` is useful for maximizing descriptor space for the dynamic portion.
            """

        class CreateParamsSettingsCardPaymentsDeclineOn(TypedDict):
            avs_failure: NotRequired["bool|None"]
            """
            Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
            """
            cvc_failure: NotRequired["bool|None"]
            """
            Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
            """

        class CreateParamsSettingsCardIssuing(TypedDict):
            tos_acceptance: NotRequired[
                "Account.CreateParamsSettingsCardIssuingTosAcceptance|None"
            ]
            """
            Details on the account's acceptance of the [Stripe Issuing Terms and Disclosures](https://stripe.com/docs/issuing/connect/tos_acceptance).
            """

        class CreateParamsSettingsCardIssuingTosAcceptance(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the account representative accepted the service agreement.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the account representative accepted the service agreement.
            """
            user_agent: NotRequired["Literal['']|str|None"]
            """
            The user agent of the browser from which the account representative accepted the service agreement.
            """

        class CreateParamsSettingsBranding(TypedDict):
            icon: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) An icon for the account. Must be square and at least 128px x 128px.
            """
            logo: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A logo for the account that will be used in Checkout instead of the icon and without the account's name next to it if provided. Must be at least 128px x 128px.
            """
            primary_color: NotRequired["str|None"]
            """
            A CSS hex color value representing the primary branding color for this account.
            """
            secondary_color: NotRequired["str|None"]
            """
            A CSS hex color value representing the secondary branding color for this account.
            """

        class CreateParamsIndividual(TypedDict):
            address: NotRequired["Account.CreateParamsIndividualAddress|None"]
            """
            The individual's primary address.
            """
            address_kana: NotRequired[
                "Account.CreateParamsIndividualAddressKana|None"
            ]
            """
            The Kana variation of the the individual's primary address (Japan only).
            """
            address_kanji: NotRequired[
                "Account.CreateParamsIndividualAddressKanji|None"
            ]
            """
            The Kanji variation of the the individual's primary address (Japan only).
            """
            dob: NotRequired[
                "Literal['']|Account.CreateParamsIndividualDob|None"
            ]
            """
            The individual's date of birth.
            """
            email: NotRequired["str|None"]
            """
            The individual's email address.
            """
            first_name: NotRequired["str|None"]
            """
            The individual's first name.
            """
            first_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the the individual's first name (Japan only).
            """
            first_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the individual's first name (Japan only).
            """
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            """
            A list of alternate names or aliases that the individual is known by.
            """
            gender: NotRequired["str|None"]
            """
            The individual's gender (International regulations require either "male" or "female").
            """
            id_number: NotRequired["str|None"]
            """
            The government-issued ID number of the individual, as appropriate for the representative's country. (Examples are a Social Security Number in the U.S., or a Social Insurance Number in Canada). Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            id_number_secondary: NotRequired["str|None"]
            """
            The government-issued secondary ID number of the individual, as appropriate for the representative's country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token created with Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            last_name: NotRequired["str|None"]
            """
            The individual's last name.
            """
            last_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the individual's last name (Japan only).
            """
            last_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the individual's last name (Japan only).
            """
            maiden_name: NotRequired["str|None"]
            """
            The individual's maiden name.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            phone: NotRequired["str|None"]
            """
            The individual's phone number.
            """
            political_exposure: NotRequired["Literal['existing', 'none']|None"]
            """
            Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
            """
            registered_address: NotRequired[
                "Account.CreateParamsIndividualRegisteredAddress|None"
            ]
            """
            The individual's registered address.
            """
            ssn_last_4: NotRequired["str|None"]
            """
            The last four digits of the individual's Social Security Number (U.S. only).
            """
            verification: NotRequired[
                "Account.CreateParamsIndividualVerification|None"
            ]
            """
            The individual's verification document information.
            """

        class CreateParamsIndividualVerification(TypedDict):
            additional_document: NotRequired[
                "Account.CreateParamsIndividualVerificationAdditionalDocument|None"
            ]
            """
            A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
            """
            document: NotRequired[
                "Account.CreateParamsIndividualVerificationDocument|None"
            ]
            """
            An identifying document, either a passport or local ID card.
            """

        class CreateParamsIndividualVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class CreateParamsIndividualVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class CreateParamsIndividualRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsIndividualDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class CreateParamsIndividualAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreateParamsIndividualAddressKana(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreateParamsIndividualAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsDocuments(TypedDict):
            bank_account_ownership_verification: NotRequired[
                "Account.CreateParamsDocumentsBankAccountOwnershipVerification|None"
            ]
            """
            One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a voided check.
            """
            company_license: NotRequired[
                "Account.CreateParamsDocumentsCompanyLicense|None"
            ]
            """
            One or more documents that demonstrate proof of a company's license to operate.
            """
            company_memorandum_of_association: NotRequired[
                "Account.CreateParamsDocumentsCompanyMemorandumOfAssociation|None"
            ]
            """
            One or more documents showing the company's Memorandum of Association.
            """
            company_ministerial_decree: NotRequired[
                "Account.CreateParamsDocumentsCompanyMinisterialDecree|None"
            ]
            """
            (Certain countries only) One or more documents showing the ministerial decree legalizing the company's establishment.
            """
            company_registration_verification: NotRequired[
                "Account.CreateParamsDocumentsCompanyRegistrationVerification|None"
            ]
            """
            One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
            """
            company_tax_id_verification: NotRequired[
                "Account.CreateParamsDocumentsCompanyTaxIdVerification|None"
            ]
            """
            One or more documents that demonstrate proof of a company's tax ID.
            """
            proof_of_registration: NotRequired[
                "Account.CreateParamsDocumentsProofOfRegistration|None"
            ]
            """
            One or more documents showing the company's proof of registration with the national business registry.
            """

        class CreateParamsDocumentsProofOfRegistration(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsCompanyTaxIdVerification(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsCompanyRegistrationVerification(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsCompanyMinisterialDecree(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsCompanyMemorandumOfAssociation(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsCompanyLicense(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsDocumentsBankAccountOwnershipVerification(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreateParamsCompany(TypedDict):
            address: NotRequired["Account.CreateParamsCompanyAddress|None"]
            """
            The company's primary address.
            """
            address_kana: NotRequired[
                "Account.CreateParamsCompanyAddressKana|None"
            ]
            """
            The Kana variation of the company's primary address (Japan only).
            """
            address_kanji: NotRequired[
                "Account.CreateParamsCompanyAddressKanji|None"
            ]
            """
            The Kanji variation of the company's primary address (Japan only).
            """
            directors_provided: NotRequired["bool|None"]
            """
            Whether the company's directors have been provided. Set this Boolean to `true` after creating all the company's directors with [the Persons API](https://stripe.com/docs/api/persons) for accounts with a `relationship.director` requirement. This value is not automatically set to `true` after creating directors, so it needs to be updated to indicate all directors have been provided.
            """
            executives_provided: NotRequired["bool|None"]
            """
            Whether the company's executives have been provided. Set this Boolean to `true` after creating all the company's executives with [the Persons API](https://stripe.com/docs/api/persons) for accounts with a `relationship.executive` requirement.
            """
            export_license_id: NotRequired["str|None"]
            """
            The export license ID number of the company, also referred as Import Export Code (India only).
            """
            export_purpose_code: NotRequired["str|None"]
            """
            The purpose code to use for export transactions (India only).
            """
            name: NotRequired["str|None"]
            """
            The company's legal name.
            """
            name_kana: NotRequired["str|None"]
            """
            The Kana variation of the company's legal name (Japan only).
            """
            name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the company's legal name (Japan only).
            """
            owners_provided: NotRequired["bool|None"]
            """
            Whether the company's owners have been provided. Set this Boolean to `true` after creating all the company's owners with [the Persons API](https://stripe.com/docs/api/persons) for accounts with a `relationship.owner` requirement.
            """
            ownership_declaration: NotRequired[
                "Account.CreateParamsCompanyOwnershipDeclaration|None"
            ]
            """
            This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct.
            """
            phone: NotRequired["str|None"]
            """
            The company's phone number (used for verification).
            """
            registration_number: NotRequired["str|None"]
            """
            The identification number given to a company when it is registered or incorporated, if distinct from the identification number used for filing taxes. (Examples are the CIN for companies and LLP IN for partnerships in India, and the Company Registration Number in Hong Kong).
            """
            structure: NotRequired[
                "Literal['']|Literal['free_zone_establishment', 'free_zone_llc', 'government_instrumentality', 'governmental_unit', 'incorporated_non_profit', 'incorporated_partnership', 'limited_liability_partnership', 'llc', 'multi_member_llc', 'private_company', 'private_corporation', 'private_partnership', 'public_company', 'public_corporation', 'public_partnership', 'single_member_llc', 'sole_establishment', 'sole_proprietorship', 'tax_exempt_government_instrumentality', 'unincorporated_association', 'unincorporated_non_profit', 'unincorporated_partnership']|None"
            ]
            """
            The category identifying the legal structure of the company or legal entity. See [Business structure](https://stripe.com/docs/connect/identity-verification#business-structure) for more details.
            """
            tax_id: NotRequired["str|None"]
            """
            The business ID number of the company, as appropriate for the company's country. (Examples are an Employer ID Number in the U.S., a Business Number in Canada, or a Company Number in the UK.)
            """
            tax_id_registrar: NotRequired["str|None"]
            """
            The jurisdiction in which the `tax_id` is registered (Germany-based companies only).
            """
            vat_id: NotRequired["str|None"]
            """
            The VAT number of the company.
            """
            verification: NotRequired[
                "Account.CreateParamsCompanyVerification|None"
            ]
            """
            Information on the verification state of the company.
            """

        class CreateParamsCompanyVerification(TypedDict):
            document: NotRequired[
                "Account.CreateParamsCompanyVerificationDocument|None"
            ]
            """
            A document verifying the business.
            """

        class CreateParamsCompanyVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `additional_verification`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class CreateParamsCompanyOwnershipDeclaration(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the beneficial owner attestation was made.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the beneficial owner attestation was made.
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the beneficial owner attestation was made.
            """

        class CreateParamsCompanyAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreateParamsCompanyAddressKana(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreateParamsCompanyAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsCapabilities(TypedDict):
            acss_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAcssDebitPayments|None"
            ]
            """
            The acss_debit_payments capability.
            """
            affirm_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAffirmPayments|None"
            ]
            """
            The affirm_payments capability.
            """
            afterpay_clearpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAfterpayClearpayPayments|None"
            ]
            """
            The afterpay_clearpay_payments capability.
            """
            au_becs_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesAuBecsDebitPayments|None"
            ]
            """
            The au_becs_debit_payments capability.
            """
            bacs_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBacsDebitPayments|None"
            ]
            """
            The bacs_debit_payments capability.
            """
            bancontact_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBancontactPayments|None"
            ]
            """
            The bancontact_payments capability.
            """
            bank_transfer_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBankTransferPayments|None"
            ]
            """
            The bank_transfer_payments capability.
            """
            blik_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBlikPayments|None"
            ]
            """
            The blik_payments capability.
            """
            boleto_payments: NotRequired[
                "Account.CreateParamsCapabilitiesBoletoPayments|None"
            ]
            """
            The boleto_payments capability.
            """
            card_issuing: NotRequired[
                "Account.CreateParamsCapabilitiesCardIssuing|None"
            ]
            """
            The card_issuing capability.
            """
            card_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCardPayments|None"
            ]
            """
            The card_payments capability.
            """
            cartes_bancaires_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCartesBancairesPayments|None"
            ]
            """
            The cartes_bancaires_payments capability.
            """
            cashapp_payments: NotRequired[
                "Account.CreateParamsCapabilitiesCashappPayments|None"
            ]
            """
            The cashapp_payments capability.
            """
            eps_payments: NotRequired[
                "Account.CreateParamsCapabilitiesEpsPayments|None"
            ]
            """
            The eps_payments capability.
            """
            fpx_payments: NotRequired[
                "Account.CreateParamsCapabilitiesFpxPayments|None"
            ]
            """
            The fpx_payments capability.
            """
            giropay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesGiropayPayments|None"
            ]
            """
            The giropay_payments capability.
            """
            grabpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesGrabpayPayments|None"
            ]
            """
            The grabpay_payments capability.
            """
            ideal_payments: NotRequired[
                "Account.CreateParamsCapabilitiesIdealPayments|None"
            ]
            """
            The ideal_payments capability.
            """
            india_international_payments: NotRequired[
                "Account.CreateParamsCapabilitiesIndiaInternationalPayments|None"
            ]
            """
            The india_international_payments capability.
            """
            jcb_payments: NotRequired[
                "Account.CreateParamsCapabilitiesJcbPayments|None"
            ]
            """
            The jcb_payments capability.
            """
            klarna_payments: NotRequired[
                "Account.CreateParamsCapabilitiesKlarnaPayments|None"
            ]
            """
            The klarna_payments capability.
            """
            konbini_payments: NotRequired[
                "Account.CreateParamsCapabilitiesKonbiniPayments|None"
            ]
            """
            The konbini_payments capability.
            """
            legacy_payments: NotRequired[
                "Account.CreateParamsCapabilitiesLegacyPayments|None"
            ]
            """
            The legacy_payments capability.
            """
            link_payments: NotRequired[
                "Account.CreateParamsCapabilitiesLinkPayments|None"
            ]
            """
            The link_payments capability.
            """
            oxxo_payments: NotRequired[
                "Account.CreateParamsCapabilitiesOxxoPayments|None"
            ]
            """
            The oxxo_payments capability.
            """
            p24_payments: NotRequired[
                "Account.CreateParamsCapabilitiesP24Payments|None"
            ]
            """
            The p24_payments capability.
            """
            paynow_payments: NotRequired[
                "Account.CreateParamsCapabilitiesPaynowPayments|None"
            ]
            """
            The paynow_payments capability.
            """
            promptpay_payments: NotRequired[
                "Account.CreateParamsCapabilitiesPromptpayPayments|None"
            ]
            """
            The promptpay_payments capability.
            """
            sepa_debit_payments: NotRequired[
                "Account.CreateParamsCapabilitiesSepaDebitPayments|None"
            ]
            """
            The sepa_debit_payments capability.
            """
            sofort_payments: NotRequired[
                "Account.CreateParamsCapabilitiesSofortPayments|None"
            ]
            """
            The sofort_payments capability.
            """
            tax_reporting_us_1099_k: NotRequired[
                "Account.CreateParamsCapabilitiesTaxReportingUs1099K|None"
            ]
            """
            The tax_reporting_us_1099_k capability.
            """
            tax_reporting_us_1099_misc: NotRequired[
                "Account.CreateParamsCapabilitiesTaxReportingUs1099Misc|None"
            ]
            """
            The tax_reporting_us_1099_misc capability.
            """
            transfers: NotRequired[
                "Account.CreateParamsCapabilitiesTransfers|None"
            ]
            """
            The transfers capability.
            """
            treasury: NotRequired[
                "Account.CreateParamsCapabilitiesTreasury|None"
            ]
            """
            The treasury capability.
            """
            us_bank_account_ach_payments: NotRequired[
                "Account.CreateParamsCapabilitiesUsBankAccountAchPayments|None"
            ]
            """
            The us_bank_account_ach_payments capability.
            """
            zip_payments: NotRequired[
                "Account.CreateParamsCapabilitiesZipPayments|None"
            ]
            """
            The zip_payments capability.
            """

        class CreateParamsCapabilitiesZipPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesUsBankAccountAchPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesTreasury(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesTransfers(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesTaxReportingUs1099Misc(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesTaxReportingUs1099K(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesSofortPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesSepaDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesPromptpayPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesPaynowPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesP24Payments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesOxxoPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesLinkPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesLegacyPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesKonbiniPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesKlarnaPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesJcbPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesIndiaInternationalPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesIdealPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesGrabpayPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesGiropayPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesFpxPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesEpsPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesCashappPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesCartesBancairesPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesCardPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesCardIssuing(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesBoletoPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesBlikPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesBankTransferPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesBancontactPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesBacsDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesAuBecsDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesAfterpayClearpayPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesAffirmPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsCapabilitiesAcssDebitPayments(TypedDict):
            requested: NotRequired["bool|None"]
            """
            Passing true requests the capability for the account, if it is not already requested. A requested capability may not immediately become active. Any requirements to activate the capability are returned in the `requirements` arrays.
            """

        class CreateParamsBusinessProfile(TypedDict):
            mcc: NotRequired["str|None"]
            """
            [The merchant category code for the account](https://stripe.com/docs/connect/setting-mcc). MCCs are used to classify businesses based on the goods or services they provide.
            """
            monthly_estimated_revenue: NotRequired[
                "Account.CreateParamsBusinessProfileMonthlyEstimatedRevenue|None"
            ]
            """
            An estimate of the monthly revenue of the business. Only accepted for accounts in Brazil and India.
            """
            name: NotRequired["str|None"]
            """
            The customer-facing business name.
            """
            product_description: NotRequired["str|None"]
            """
            Internal-only description of the product sold by, or service provided by, the business. Used by Stripe for risk and underwriting purposes.
            """
            support_address: NotRequired[
                "Account.CreateParamsBusinessProfileSupportAddress|None"
            ]
            """
            A publicly available mailing address for sending support issues to.
            """
            support_email: NotRequired["str|None"]
            """
            A publicly available email address for sending support issues to.
            """
            support_phone: NotRequired["str|None"]
            """
            A publicly available phone number to call with support issues.
            """
            support_url: NotRequired["Literal['']|str|None"]
            """
            A publicly available website for handling support issues.
            """
            url: NotRequired["str|None"]
            """
            The business's publicly available website.
            """

        class CreateParamsBusinessProfileSupportAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsBusinessProfileMonthlyEstimatedRevenue(TypedDict):
            amount: int
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["Account.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class PersonsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            relationship: NotRequired["Account.PersonsParamsRelationship|None"]
            """
            Filters on the list of people returned based on the person's relationship to the account's company.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class PersonsParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are directors of the account's company.
            """
            executive: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are executives of the account's company.
            """
            legal_guardian: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are legal guardians of the account's representative.
            """
            owner: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are owners of the account's company.
            """
            representative: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are the representative of the account's company.
            """

        class RejectParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            reason: str
            """
            The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`.
            """

        class RetrieveCapabilityParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifyCapabilityParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            requested: NotRequired["bool|None"]
            """
            To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.

            If a capability isn't permanent, you can remove it from the account by passing false. Most capabilities are permanent after they've been requested. Attempting to remove a permanent capability returns an error.
            """

        class ListCapabilitiesParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreateExternalAccountParams(RequestOptions):
            default_for_currency: NotRequired["bool|None"]
            """
            When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            external_account: str
            """
            Please refer to full [documentation](https://stripe.com/docs/api) instead.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """

        class RetrieveExternalAccountParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifyExternalAccountParams(RequestOptions):
            account_holder_name: NotRequired["str|None"]
            """
            The name of the person or business that owns the bank account.
            """
            account_holder_type: NotRequired[
                "Literal['']|Literal['company', 'individual']|None"
            ]
            """
            The type of entity that holds the account. This can be either `individual` or `company`.
            """
            account_type: NotRequired[
                "Literal['checking', 'futsu', 'savings', 'toza']|None"
            ]
            """
            The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
            """
            address_city: NotRequired["str|None"]
            """
            City/District/Suburb/Town/Village.
            """
            address_country: NotRequired["str|None"]
            """
            Billing address country, if provided when creating card.
            """
            address_line1: NotRequired["str|None"]
            """
            Address line 1 (Street address/PO Box/Company name).
            """
            address_line2: NotRequired["str|None"]
            """
            Address line 2 (Apartment/Suite/Unit/Building).
            """
            address_state: NotRequired["str|None"]
            """
            State/County/Province/Region.
            """
            address_zip: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            default_for_currency: NotRequired["bool|None"]
            """
            When set to true, this becomes the default external account for its currency.
            """
            documents: NotRequired[
                "Account.ModifyExternalAccountParamsDocuments|None"
            ]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            exp_month: NotRequired["str|None"]
            """
            Two digit number representing the card's expiration month.
            """
            exp_year: NotRequired["str|None"]
            """
            Four digit number representing the card's expiration year.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["str|None"]
            """
            Cardholder name.
            """

        class ModifyExternalAccountParamsDocuments(TypedDict):
            bank_account_ownership_verification: NotRequired[
                "Account.ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification|None"
            ]
            """
            One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the bank account that displays the last 4 digits of the account number, either a statement or a voided check.
            """

        class ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification(
            TypedDict,
        ):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class DeleteExternalAccountParams(RequestOptions):
            pass

        class ListExternalAccountsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            object: NotRequired["Literal['bank_account', 'card']|None"]
            """
            Filter external accounts according to a particular object type.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class CreateLoginLinkParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreatePersonParams(RequestOptions):
            additional_tos_acceptances: NotRequired[
                "Account.CreatePersonParamsAdditionalTosAcceptances|None"
            ]
            """
            Details on the legal guardian's acceptance of the required Stripe agreements.
            """
            address: NotRequired["Account.CreatePersonParamsAddress|None"]
            """
            The person's address.
            """
            address_kana: NotRequired[
                "Account.CreatePersonParamsAddressKana|None"
            ]
            """
            The Kana variation of the person's address (Japan only).
            """
            address_kanji: NotRequired[
                "Account.CreatePersonParamsAddressKanji|None"
            ]
            """
            The Kanji variation of the person's address (Japan only).
            """
            dob: NotRequired["Literal['']|Account.CreatePersonParamsDob|None"]
            """
            The person's date of birth.
            """
            documents: NotRequired["Account.CreatePersonParamsDocuments|None"]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            email: NotRequired["str|None"]
            """
            The person's email address.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            first_name: NotRequired["str|None"]
            """
            The person's first name.
            """
            first_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the person's first name (Japan only).
            """
            first_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the person's first name (Japan only).
            """
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            """
            A list of alternate names or aliases that the person is known by.
            """
            gender: NotRequired["str|None"]
            """
            The person's gender (International regulations require either "male" or "female").
            """
            id_number: NotRequired["str|None"]
            """
            The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            id_number_secondary: NotRequired["str|None"]
            """
            The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            last_name: NotRequired["str|None"]
            """
            The person's last name.
            """
            last_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the person's last name (Japan only).
            """
            last_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the person's last name (Japan only).
            """
            maiden_name: NotRequired["str|None"]
            """
            The person's maiden name.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            nationality: NotRequired["str|None"]
            """
            The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
            """
            person_token: NotRequired["str|None"]
            """
            A [person token](https://stripe.com/docs/connect/account-tokens), used to securely provide details to the person.
            """
            phone: NotRequired["str|None"]
            """
            The person's phone number.
            """
            political_exposure: NotRequired["str|None"]
            """
            Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
            """
            registered_address: NotRequired[
                "Account.CreatePersonParamsRegisteredAddress|None"
            ]
            """
            The person's registered address.
            """
            relationship: NotRequired[
                "Account.CreatePersonParamsRelationship|None"
            ]
            """
            The relationship that this person has with the account's legal entity.
            """
            ssn_last_4: NotRequired["str|None"]
            """
            The last four digits of the person's Social Security number (U.S. only).
            """
            verification: NotRequired[
                "Account.CreatePersonParamsVerification|None"
            ]
            """
            The person's verification status.
            """

        class CreatePersonParamsVerification(TypedDict):
            additional_document: NotRequired[
                "Account.CreatePersonParamsVerificationAdditionalDocument|None"
            ]
            """
            A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
            """
            document: NotRequired[
                "Account.CreatePersonParamsVerificationDocument|None"
            ]
            """
            An identifying document, either a passport or local ID card.
            """

        class CreatePersonParamsVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class CreatePersonParamsVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class CreatePersonParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            """
            Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
            """
            executive: NotRequired["bool|None"]
            """
            Whether the person has significant responsibility to control, manage, or direct the organization.
            """
            legal_guardian: NotRequired["bool|None"]
            """
            Whether the person is the legal guardian of the account's representative.
            """
            owner: NotRequired["bool|None"]
            """
            Whether the person is an owner of the account's legal entity.
            """
            percent_ownership: NotRequired["Literal['']|float|None"]
            """
            The percent owned by the person of the account's legal entity.
            """
            representative: NotRequired["bool|None"]
            """
            Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
            """
            title: NotRequired["str|None"]
            """
            The person's title (e.g., CEO, Support Engineer).
            """

        class CreatePersonParamsRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreatePersonParamsDocuments(TypedDict):
            company_authorization: NotRequired[
                "Account.CreatePersonParamsDocumentsCompanyAuthorization|None"
            ]
            """
            One or more documents that demonstrate proof that this person is authorized to represent the company.
            """
            passport: NotRequired[
                "Account.CreatePersonParamsDocumentsPassport|None"
            ]
            """
            One or more documents showing the person's passport page with photo and personal data.
            """
            visa: NotRequired["Account.CreatePersonParamsDocumentsVisa|None"]
            """
            One or more documents showing the person's visa required for living in the country where they are residing.
            """

        class CreatePersonParamsDocumentsVisa(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreatePersonParamsDocumentsPassport(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreatePersonParamsDocumentsCompanyAuthorization(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class CreatePersonParamsDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class CreatePersonParamsAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreatePersonParamsAddressKana(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class CreatePersonParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreatePersonParamsAdditionalTosAcceptances(TypedDict):
            account: NotRequired[
                "Account.CreatePersonParamsAdditionalTosAcceptancesAccount|None"
            ]
            """
            Details on the legal guardian's acceptance of the main Stripe service agreement.
            """

        class CreatePersonParamsAdditionalTosAcceptancesAccount(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the account representative accepted the service agreement.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the account representative accepted the service agreement.
            """
            user_agent: NotRequired["Literal['']|str|None"]
            """
            The user agent of the browser from which the account representative accepted the service agreement.
            """

        class RetrievePersonParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifyPersonParams(RequestOptions):
            additional_tos_acceptances: NotRequired[
                "Account.ModifyPersonParamsAdditionalTosAcceptances|None"
            ]
            """
            Details on the legal guardian's acceptance of the required Stripe agreements.
            """
            address: NotRequired["Account.ModifyPersonParamsAddress|None"]
            """
            The person's address.
            """
            address_kana: NotRequired[
                "Account.ModifyPersonParamsAddressKana|None"
            ]
            """
            The Kana variation of the person's address (Japan only).
            """
            address_kanji: NotRequired[
                "Account.ModifyPersonParamsAddressKanji|None"
            ]
            """
            The Kanji variation of the person's address (Japan only).
            """
            dob: NotRequired["Literal['']|Account.ModifyPersonParamsDob|None"]
            """
            The person's date of birth.
            """
            documents: NotRequired["Account.ModifyPersonParamsDocuments|None"]
            """
            Documents that may be submitted to satisfy various informational requests.
            """
            email: NotRequired["str|None"]
            """
            The person's email address.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            first_name: NotRequired["str|None"]
            """
            The person's first name.
            """
            first_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the person's first name (Japan only).
            """
            first_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the person's first name (Japan only).
            """
            full_name_aliases: NotRequired["Literal['']|List[str]|None"]
            """
            A list of alternate names or aliases that the person is known by.
            """
            gender: NotRequired["str|None"]
            """
            The person's gender (International regulations require either "male" or "female").
            """
            id_number: NotRequired["str|None"]
            """
            The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            id_number_secondary: NotRequired["str|None"]
            """
            The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://stripe.com/docs/js/tokens/create_token?type=pii).
            """
            last_name: NotRequired["str|None"]
            """
            The person's last name.
            """
            last_name_kana: NotRequired["str|None"]
            """
            The Kana variation of the person's last name (Japan only).
            """
            last_name_kanji: NotRequired["str|None"]
            """
            The Kanji variation of the person's last name (Japan only).
            """
            maiden_name: NotRequired["str|None"]
            """
            The person's maiden name.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            nationality: NotRequired["str|None"]
            """
            The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
            """
            person_token: NotRequired["str|None"]
            """
            A [person token](https://stripe.com/docs/connect/account-tokens), used to securely provide details to the person.
            """
            phone: NotRequired["str|None"]
            """
            The person's phone number.
            """
            political_exposure: NotRequired["str|None"]
            """
            Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
            """
            registered_address: NotRequired[
                "Account.ModifyPersonParamsRegisteredAddress|None"
            ]
            """
            The person's registered address.
            """
            relationship: NotRequired[
                "Account.ModifyPersonParamsRelationship|None"
            ]
            """
            The relationship that this person has with the account's legal entity.
            """
            ssn_last_4: NotRequired["str|None"]
            """
            The last four digits of the person's Social Security number (U.S. only).
            """
            verification: NotRequired[
                "Account.ModifyPersonParamsVerification|None"
            ]
            """
            The person's verification status.
            """

        class ModifyPersonParamsVerification(TypedDict):
            additional_document: NotRequired[
                "Account.ModifyPersonParamsVerificationAdditionalDocument|None"
            ]
            """
            A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
            """
            document: NotRequired[
                "Account.ModifyPersonParamsVerificationDocument|None"
            ]
            """
            An identifying document, either a passport or local ID card.
            """

        class ModifyPersonParamsVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class ModifyPersonParamsVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            """
            The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """
            front: NotRequired["str|None"]
            """
            The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
            """

        class ModifyPersonParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            """
            Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
            """
            executive: NotRequired["bool|None"]
            """
            Whether the person has significant responsibility to control, manage, or direct the organization.
            """
            legal_guardian: NotRequired["bool|None"]
            """
            Whether the person is the legal guardian of the account's representative.
            """
            owner: NotRequired["bool|None"]
            """
            Whether the person is an owner of the account's legal entity.
            """
            percent_ownership: NotRequired["Literal['']|float|None"]
            """
            The percent owned by the person of the account's legal entity.
            """
            representative: NotRequired["bool|None"]
            """
            Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
            """
            title: NotRequired["str|None"]
            """
            The person's title (e.g., CEO, Support Engineer).
            """

        class ModifyPersonParamsRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyPersonParamsDocuments(TypedDict):
            company_authorization: NotRequired[
                "Account.ModifyPersonParamsDocumentsCompanyAuthorization|None"
            ]
            """
            One or more documents that demonstrate proof that this person is authorized to represent the company.
            """
            passport: NotRequired[
                "Account.ModifyPersonParamsDocumentsPassport|None"
            ]
            """
            One or more documents showing the person's passport page with photo and personal data.
            """
            visa: NotRequired["Account.ModifyPersonParamsDocumentsVisa|None"]
            """
            One or more documents showing the person's visa required for living in the country where they are residing.
            """

        class ModifyPersonParamsDocumentsVisa(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class ModifyPersonParamsDocumentsPassport(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class ModifyPersonParamsDocumentsCompanyAuthorization(TypedDict):
            files: NotRequired["List[str]|None"]
            """
            One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
            """

        class ModifyPersonParamsDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class ModifyPersonParamsAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class ModifyPersonParamsAddressKana(TypedDict):
            city: NotRequired["str|None"]
            """
            City or ward.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Block or building number.
            """
            line2: NotRequired["str|None"]
            """
            Building details.
            """
            postal_code: NotRequired["str|None"]
            """
            Postal code.
            """
            state: NotRequired["str|None"]
            """
            Prefecture.
            """
            town: NotRequired["str|None"]
            """
            Town or cho-me.
            """

        class ModifyPersonParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyPersonParamsAdditionalTosAcceptances(TypedDict):
            account: NotRequired[
                "Account.ModifyPersonParamsAdditionalTosAcceptancesAccount|None"
            ]
            """
            Details on the legal guardian's acceptance of the main Stripe service agreement.
            """

        class ModifyPersonParamsAdditionalTosAcceptancesAccount(TypedDict):
            date: NotRequired["int|None"]
            """
            The Unix timestamp marking when the account representative accepted the service agreement.
            """
            ip: NotRequired["str|None"]
            """
            The IP address from which the account representative accepted the service agreement.
            """
            user_agent: NotRequired["Literal['']|str|None"]
            """
            The user agent of the browser from which the account representative accepted the service agreement.
            """

        class DeletePersonParams(RequestOptions):
            pass

        class ListPersonsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            relationship: NotRequired[
                "Account.ListPersonsParamsRelationship|None"
            ]
            """
            Filters on the list of people returned based on the person's relationship to the account's company.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListPersonsParamsRelationship(TypedDict):
            director: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are directors of the account's company.
            """
            executive: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are executives of the account's company.
            """
            legal_guardian: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are legal guardians of the account's representative.
            """
            owner: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are owners of the account's company.
            """
            representative: NotRequired["bool|None"]
            """
            A filter on the list of people returned based on whether these people are the representative of the account's company.
            """

    business_profile: Optional[BusinessProfile]
    """
    Business information about the account.
    """
    business_type: Optional[
        Literal["company", "government_entity", "individual", "non_profit"]
    ]
    """
    The business type.
    """
    capabilities: Optional[Capabilities]
    charges_enabled: Optional[bool]
    """
    Whether the account can create live charges.
    """
    company: Optional[Company]
    controller: Optional[Controller]
    country: Optional[str]
    """
    The account's country.
    """
    created: Optional[int]
    """
    Time at which the account was connected. Measured in seconds since the Unix epoch.
    """
    default_currency: Optional[str]
    """
    Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://stripe.com/docs/payouts).
    """
    details_submitted: Optional[bool]
    """
    Whether account details have been submitted. Standard accounts cannot receive payouts before this is true.
    """
    email: Optional[str]
    """
    An email address associated with the account. It's not used for authentication and Stripe doesn't market to this field without explicit approval from the platform.
    """
    external_accounts: Optional[ListObject[Union["BankAccount", "Card"]]]
    """
    External accounts (bank accounts and debit cards) currently attached to this account
    """
    future_requirements: Optional[FutureRequirements]
    id: str
    """
    Unique identifier for the object.
    """
    individual: Optional["Person"]
    """
    This is an object representing a person associated with a Stripe account.

    A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
    See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform prefilling and account onboarding steps.

    Related guide: [Handling identity verification with the API](https://stripe.com/docs/connect/handling-api-verification#person-information)
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["account"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payouts_enabled: Optional[bool]
    """
    Whether Stripe can send payouts to this account.
    """
    requirements: Optional[Requirements]
    settings: Optional[Settings]
    """
    Options for customizing how the account functions within Stripe.
    """
    tos_acceptance: Optional[TosAcceptance]
    type: Optional[Literal["custom", "express", "standard"]]
    """
    The Stripe account type. Can be `standard`, `express`, or `custom`.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you can create Stripe accounts for your users.
        To do this, you'll first need to [register your platform](https://dashboard.stripe.com/account/applications/settings).

        If you've already collected information for your connected accounts, you [can prefill that information](https://stripe.com/docs/connect/best-practices#onboarding) when
        creating the account. Connect Onboarding won't ask for the prefilled information during account onboarding.
        You can prefill any information on the account.
        """
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
        """
        With [Connect](https://stripe.com/docs/connect), you can delete accounts you manage.

        Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

        If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Account",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["Account.DeleteParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you can delete accounts you manage.

        Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

        If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Account.DeleteParams"]) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you can delete accounts you manage.

        Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

        If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Account.DeleteParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you can delete accounts you manage.

        Accounts created using test-mode keys can be deleted at any time. Standard accounts created using live-mode keys cannot be deleted. Custom or Express accounts created using live-mode keys can only be deleted once all balances are zero.

        If you want to delete your own account, use the [account information tab in your account settings](https://dashboard.stripe.com/settings/account) instead.
        """
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
        """
        Returns a list of accounts connected to your platform via [Connect](https://stripe.com/docs/connect). If you're not a platform, the list is empty.
        """
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
    ) -> ListObject["Person"]:
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        return cast(
            ListObject["Person"],
            cls._static_request(
                "get",
                "/v1/accounts/{account}/persons".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def persons(
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.PersonsParams"]
    ) -> ListObject["Person"]:
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        ...

    @overload
    def persons(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.PersonsParams"]
    ) -> ListObject["Person"]:
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        ...

    @class_method_variant("_cls_persons")
    def persons(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.PersonsParams"]
    ) -> ListObject["Person"]:
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        return cast(
            ListObject["Person"],
            self._request(
                "get",
                "/v1/accounts/{account}/persons".format(
                    account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_reject(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you may flag accounts as suspicious.

        Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.
        """
        return cast(
            "Account",
            cls._static_request(
                "post",
                "/v1/accounts/{account}/reject".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def reject(
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you may flag accounts as suspicious.

        Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.
        """
        ...

    @overload
    def reject(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you may flag accounts as suspicious.

        Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.
        """
        ...

    @class_method_variant("_cls_reject")
    def reject(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Account.RejectParams"]
    ) -> "Account":
        """
        With [Connect](https://stripe.com/docs/connect), you may flag accounts as suspicious.

        Test-mode Custom and Express accounts can be rejected at any time. Accounts created using live-mode keys may only be rejected once all balances are zero.
        """
        return cast(
            "Account",
            self._request(
                "post",
                "/v1/accounts/{account}/reject".format(
                    account=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
    ) -> "Capability":
        """
        Retrieves information about the specified Account Capability.
        """
        return cast(
            "Capability",
            cls._static_request(
                "get",
                "/v1/accounts/{account}/capabilities/{capability}".format(
                    account=util.sanitize_id(account),
                    capability=util.sanitize_id(capability),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> "Capability":
        """
        Updates an existing Account Capability. Request or remove a capability by updating its requested parameter.
        """
        return cast(
            "Capability",
            cls._static_request(
                "post",
                "/v1/accounts/{account}/capabilities/{capability}".format(
                    account=util.sanitize_id(account),
                    capability=util.sanitize_id(capability),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_capabilities(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListCapabilitiesParams"]
    ) -> ListObject["Capability"]:
        """
        Returns a list of capabilities associated with the account. The capabilities are returned sorted by creation date, with the most recent capability appearing first.
        """
        return cast(
            ListObject["Capability"],
            cls._static_request(
                "get",
                "/v1/accounts/{account}/capabilities".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_external_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateExternalAccountParams"]
    ) -> Union["BankAccount", "Card"]:
        """
        Create an external account for a given account.
        """
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request(
                "post",
                "/v1/accounts/{account}/external_accounts".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> Union["BankAccount", "Card"]:
        """
        Retrieve a specified external account for a given account.
        """
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request(
                "get",
                "/v1/accounts/{account}/external_accounts/{id}".format(
                    account=util.sanitize_id(account), id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> Union["BankAccount", "Card"]:
        """
        Updates the metadata, account holder name, account holder type of a bank account belonging to a [Custom account](https://stripe.com/docs/connect/custom-accounts), and optionally sets it as the default for its currency. Other bank account details are not editable by design.

        You can re-enable a disabled bank account by performing an update call without providing any arguments or changes.
        """
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request(
                "post",
                "/v1/accounts/{account}/external_accounts/{id}".format(
                    account=util.sanitize_id(account), id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> Union["BankAccount", "Card"]:
        """
        Delete a specified external account for a given account.
        """
        return cast(
            Union["BankAccount", "Card"],
            cls._static_request(
                "delete",
                "/v1/accounts/{account}/external_accounts/{id}".format(
                    account=util.sanitize_id(account), id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_external_accounts(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListExternalAccountsParams"]
    ) -> ListObject[Union["BankAccount", "Card"]]:
        """
        List external accounts for an account.
        """
        return cast(
            ListObject[Union["BankAccount", "Card"]],
            cls._static_request(
                "get",
                "/v1/accounts/{account}/external_accounts".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_login_link(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreateLoginLinkParams"]
    ) -> "LoginLink":
        """
        Creates a single-use login link for an Express account to access their Stripe dashboard.

        You may only create login links for [Express accounts](https://stripe.com/docs/connect/express-accounts) connected to your platform.
        """
        return cast(
            "LoginLink",
            cls._static_request(
                "post",
                "/v1/accounts/{account}/login_links".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_person(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.CreatePersonParams"]
    ) -> "Person":
        """
        Creates a new person.
        """
        return cast(
            "Person",
            cls._static_request(
                "post",
                "/v1/accounts/{account}/persons".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> "Person":
        """
        Retrieves an existing person.
        """
        return cast(
            "Person",
            cls._static_request(
                "get",
                "/v1/accounts/{account}/persons/{person}".format(
                    account=util.sanitize_id(account),
                    person=util.sanitize_id(person),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> "Person":
        """
        Updates an existing person.
        """
        return cast(
            "Person",
            cls._static_request(
                "post",
                "/v1/accounts/{account}/persons/{person}".format(
                    account=util.sanitize_id(account),
                    person=util.sanitize_id(person),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
    ) -> "Person":
        """
        Deletes an existing person's relationship to the account's legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the account_opener. If your integration is using the executive parameter, you cannot delete the only verified executive on file.
        """
        return cast(
            "Person",
            cls._static_request(
                "delete",
                "/v1/accounts/{account}/persons/{person}".format(
                    account=util.sanitize_id(account),
                    person=util.sanitize_id(person),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_persons(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Account.ListPersonsParams"]
    ) -> ListObject["Person"]:
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        return cast(
            ListObject["Person"],
            cls._static_request(
                "get",
                "/v1/accounts/{account}/persons".format(
                    account=util.sanitize_id(account)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
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
