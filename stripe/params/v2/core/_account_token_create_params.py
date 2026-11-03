# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountTokenCreateParams(TypedDict):
    contact_email: NotRequired[str]
    """
    The primary contact email address for the Account.
    """
    contact_phone: NotRequired[str]
    """
    The default contact phone for the Account.
    """
    display_name: NotRequired[str]
    """
    A descriptive name for the Account. This name will be surfaced in the Stripe Dashboard and on any invoices sent to the Account.
    """
    identity: NotRequired["AccountTokenCreateParamsIdentity"]
    """
    Information about the company, individual, and business represented by the Account.
    """


class AccountTokenCreateParamsIdentity(TypedDict):
    attestations: NotRequired["AccountTokenCreateParamsIdentityAttestations"]
    """
    Attestations from the identity's key people, e.g. owners, executives, directors, representatives.
    """
    business_details: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetails"
    ]
    """
    Information about the company or business.
    """
    entity_type: NotRequired[
        "Literal['company', 'government_entity', 'individual', 'non_profit']|str"
    ]
    """
    The entity type.
    """
    individual: NotRequired["AccountTokenCreateParamsIdentityIndividual"]
    """
    Information about the person represented by the account.
    """


class AccountTokenCreateParamsIdentityAttestations(TypedDict):
    directorship_declaration: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsDirectorshipDeclaration"
    ]
    """
    This hash is used to attest that the directors information provided to Stripe is both current and correct; IP, date, and User Agent are expanded by Stripe.
    """
    ownership_declaration: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsOwnershipDeclaration"
    ]
    """
    This hash is used to attest that the beneficial owner information provided to Stripe is both current and correct; IP, date, and User Agent are expanded by Stripe.
    """
    persons_provided: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsPersonsProvided"
    ]
    """
    Attestation that all Persons with a specific Relationship value have been provided.
    """
    representative_declaration: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsRepresentativeDeclaration"
    ]
    """
    This hash is used to attest that the representative is authorized to act as the representative of their legal entity; IP, date, and User Agent are expanded by Stripe.
    """
    terms_of_service: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsTermsOfService"
    ]
    """
    Attestations of accepted terms of service agreements.
    """


class AccountTokenCreateParamsIdentityAttestationsDirectorshipDeclaration(
    TypedDict,
):
    attested: NotRequired[bool]
    """
    A boolean indicating if the directors information has been attested.
    """


class AccountTokenCreateParamsIdentityAttestationsOwnershipDeclaration(
    TypedDict,
):
    attested: NotRequired[bool]
    """
    A boolean indicating if the beneficial owner information has been attested.
    """


class AccountTokenCreateParamsIdentityAttestationsPersonsProvided(TypedDict):
    directors: NotRequired[bool]
    """
    Whether the company's directors have been provided. Set this Boolean to true after creating all the company's directors with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    executives: NotRequired[bool]
    """
    Whether the company's executives have been provided. Set this Boolean to true after creating all the company's executives with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    owners: NotRequired[bool]
    """
    Whether the company's owners have been provided. Set this Boolean to true after creating all the company's owners with the [Persons API](https://docs.stripe.com/api/v2/core/accounts/createperson).
    """
    ownership_exemption_reason: NotRequired[
        Literal[
            "qualified_entity_exceeds_ownership_threshold",
            "qualifies_as_financial_institution",
        ]
    ]
    """
    Reason for why the company is exempt from providing ownership information.
    """


class AccountTokenCreateParamsIdentityAttestationsRepresentativeDeclaration(
    TypedDict,
):
    attested: NotRequired[bool]
    """
    A boolean indicating if the representative is authorized to act as the representative of their legal entity.
    """


class AccountTokenCreateParamsIdentityAttestationsTermsOfService(TypedDict):
    account: NotRequired[
        "AccountTokenCreateParamsIdentityAttestationsTermsOfServiceAccount"
    ]
    """
    Details on the Account's acceptance of the [Stripe Services Agreement]; IP, date, and User Agent are expanded by Stripe.
    """


class AccountTokenCreateParamsIdentityAttestationsTermsOfServiceAccount(
    TypedDict,
):
    shown_and_accepted: NotRequired[bool]
    """
    The boolean value indicating if the terms of service have been accepted.
    """


class AccountTokenCreateParamsIdentityBusinessDetails(TypedDict):
    additional_addresses: NotRequired[
        List[
            "AccountTokenCreateParamsIdentityBusinessDetailsAdditionalAddress"
        ]
    ]
    """
    Additional addresses associated with the business.
    """
    address: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsAddress"
    ]
    """
    The business registration address of the business entity.
    """
    annual_revenue: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsAnnualRevenue"
    ]
    """
    The business gross annual revenue for its preceding fiscal year.
    """
    documents: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocuments"
    ]
    """
    A document verifying the business.
    """
    estimated_worker_count: NotRequired[int]
    """
    Estimated maximum number of workers currently engaged by the business (including employees, contractors, and vendors).
    """
    id_numbers: NotRequired[
        List["AccountTokenCreateParamsIdentityBusinessDetailsIdNumber"]
    ]
    """
    The ID numbers of a business entity.
    """
    monthly_estimated_revenue: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue"
    ]
    """
    An estimate of the monthly revenue of the business.
    """
    phone: NotRequired[str]
    """
    The phone number of the Business Entity.
    """
    registered_name: NotRequired[str]
    """
    The business legal name.
    """
    registration_date: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsRegistrationDate"
    ]
    """
    When the business was incorporated or registered.
    """
    script_addresses: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptAddresses"
    ]
    """
    The business registration address of the business entity in non latin script.
    """
    script_names: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptNames"
    ]
    """
    The business legal name in non latin script.
    """
    structure: NotRequired[
        "Literal['cooperative', 'free_zone_establishment', 'free_zone_llc', 'governmental_unit', 'government_instrumentality', 'incorporated_association', 'incorporated_non_profit', 'incorporated_partnership', 'limited_liability_partnership', 'llc', 'multi_member_llc', 'private_company', 'private_corporation', 'private_partnership', 'public_company', 'public_corporation', 'public_listed_corporation', 'public_partnership', 'registered_charity', 'single_member_llc', 'sole_establishment', 'sole_proprietorship', 'tax_exempt_government_instrumentality', 'trust', 'unincorporated_association', 'unincorporated_non_profit', 'unincorporated_partnership']|str"
    ]
    """
    The category identifying the legal structure of the business.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsAdditionalAddress(
    TypedDict,
):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    purpose: Literal["administrative", "principal_place_of_business"]
    """
    Purpose of additional address.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsAddress(TypedDict):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsAnnualRevenue(TypedDict):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """
    fiscal_year_end: NotRequired[str]
    """
    The close-out date of the preceding fiscal year in ISO 8601 format. E.g. 2023-12-31 for the 31st of December, 2023.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocuments(TypedDict):
    bank_account_ownership_verification: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification"
    ]
    """
    One or more documents that support the bank account ownership verification requirement. Must be a document associated with the account's primary active bank account that displays the last 4 digits of the account number, either a statement or a check.
    """
    company_license: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyLicense"
    ]
    """
    One or more documents that demonstrate proof of a company's license to operate.
    """
    company_memorandum_of_association: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation"
    ]
    """
    One or more documents showing the company's Memorandum of Association.
    """
    company_ministerial_decree: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree"
    ]
    """
    Certain countries only: One or more documents showing the ministerial decree legalizing the company's establishment.
    """
    company_registration_verification: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's registration with the appropriate local authorities.
    """
    company_tax_id_verification: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification"
    ]
    """
    One or more documents that demonstrate proof of a company's tax ID.
    """
    primary_verification: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification"
    ]
    """
    A document verifying the business.
    """
    proof_of_address: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfAddress"
    ]
    """
    One or more documents that demonstrate proof of address.
    """
    proof_of_registration: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration"
    ]
    """
    One or more documents that demonstrate proof of ultimate beneficial ownership.
    """
    proof_of_ultimate_beneficial_ownership: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership"
    ]
    """
    One or more documents that demonstrate proof of ultimate beneficial ownership.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsBankAccountOwnershipVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyLicense(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyMemorandumOfAssociation(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyMinisterialDecree(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyRegistrationVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsCompanyTaxIdVerification(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/files/create) tokens referring to each side of the document.
    """
    type: Union[Literal["front_back"], str]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfAddress(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistration(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    signer: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistrationSigner"
    ]
    """
    Person that is signing the document.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfRegistrationSigner(
    TypedDict,
):
    person: str
    """
    Person signing the document.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnership(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    signer: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnershipSigner"
    ]
    """
    Person that is signing the document.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsDocumentsProofOfUltimateBeneficialOwnershipSigner(
    TypedDict,
):
    person: str
    """
    Person signing the document.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsIdNumber(TypedDict):
    registrar: NotRequired[str]
    """
    The registrar of the ID number (Only valid for DE ID number types).
    """
    type: Union[
        Literal[
            "ae_crn",
            "ae_vat",
            "ag_tin",
            "ao_nif",
            "ar_cuit",
            "at_fn",
            "at_stn",
            "at_vat",
            "au_abn",
            "au_acn",
            "au_in",
            "au_wpn",
            "az_tin",
            "ba_pib",
            "bd_etin",
            "be_cbe",
            "be_vat",
            "bg_uic",
            "bg_vat",
            "bj_ifu",
            "br_cnpj",
            "ca_cn",
            "ca_crarr",
            "ca_gst_hst",
            "ca_neq",
            "ca_qst",
            "ca_rid",
            "ch_chid",
            "ch_uid",
            "cl_rut",
            "cr_cpj",
            "cr_nite",
            "cy_he",
            "cy_tic",
            "cy_vat",
            "cz_dic",
            "cz_ico",
            "cz_vat",
            "de_hrn",
            "de_stn",
            "de_vat",
            "dk_cvr",
            "dk_vat",
            "do_rcn",
            "dz_nif",
            "ee_rk",
            "ee_vat",
            "es_cif",
            "es_vat",
            "et_tin",
            "fi_vat",
            "fi_yt",
            "fr_rna",
            "fr_siren",
            "fr_siret",
            "fr_vat",
            "gb_crn",
            "gb_vat",
            "ge_tin",
            "gi_crn",
            "gi_vat",
            "gr_afm",
            "gr_gemi",
            "gr_vat",
            "gt_nit",
            "hk_br",
            "hk_cr",
            "hr_mbs",
            "hr_oib",
            "hr_vat",
            "hu_cjs",
            "hu_tin",
            "hu_vat",
            "id_npwp",
            "ie_crn",
            "ie_trn",
            "ie_vat",
            "il_tin",
            "il_vat",
            "in_gst",
            "in_pan",
            "is_kt",
            "it_rea",
            "it_vat",
            "jp_cn",
            "kh_tin",
            "kr_brn",
            "kz_bin",
            "la_tin",
            "lc_tin",
            "li_uid",
            "li_vat",
            "lt_ccrn",
            "lt_vat",
            "lu_nif",
            "lu_rcs",
            "lu_vat",
            "lv_urn",
            "lv_vat",
            "md_cf",
            "mg_nif",
            "mk_edb",
            "mt_crn",
            "mt_tin",
            "mt_vat",
            "mu_vat",
            "mx_rfc",
            "my_brn",
            "my_coid",
            "my_itn",
            "my_sst",
            "mz_nuit",
            "ne_tin",
            "nl_kvk",
            "nl_rsin",
            "nl_vat",
            "no_orgnr",
            "nz_bn",
            "nz_ird",
            "om_tin",
            "pe_ruc",
            "pk_ntn",
            "pl_nip",
            "pl_regon",
            "pl_vat",
            "pt_vat",
            "qa_tin",
            "ro_cui",
            "ro_orc",
            "ro_vat",
            "rw_tin",
            "sa_crn",
            "sa_tin",
            "se_orgnr",
            "se_vat",
            "sg_uen",
            "si_msp",
            "si_tin",
            "si_vat",
            "sk_dic",
            "sk_ico",
            "sk_vat",
            "sm_coe",
            "th_crn",
            "th_prn",
            "th_tin",
            "tr_tin",
            "tt_bir",
            "tt_vat",
            "us_ein",
            "vn_tin",
        ],
        str,
    ]
    """
    Open Enum. The ID number type of a business entity.
    """
    value: str
    """
    The value of the ID number.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsMonthlyEstimatedRevenue(
    TypedDict,
):
    amount: NotRequired[AmountParam]
    """
    A non-negative integer representing the amount in the smallest currency unit.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsRegistrationDate(
    TypedDict,
):
    day: int
    """
    The day of registration, between 1 and 31.
    """
    month: int
    """
    The month of registration, between 1 and 12.
    """
    year: int
    """
    The four-digit year of registration.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptAddresses(
    TypedDict
):
    kana: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptAddressesKana(
    TypedDict,
):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptAddressesKanji(
    TypedDict,
):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptNames(TypedDict):
    kana: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptNamesKana"
    ]
    """
    Kana name.
    """
    kanji: NotRequired[
        "AccountTokenCreateParamsIdentityBusinessDetailsScriptNamesKanji"
    ]
    """
    Kanji name.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptNamesKana(
    TypedDict
):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountTokenCreateParamsIdentityBusinessDetailsScriptNamesKanji(
    TypedDict,
):
    registered_name: NotRequired[str]
    """
    Registered name of the business.
    """


class AccountTokenCreateParamsIdentityIndividual(TypedDict):
    additional_addresses: NotRequired[
        List["AccountTokenCreateParamsIdentityIndividualAdditionalAddress"]
    ]
    """
    Additional addresses associated with the individual.
    """
    additional_names: NotRequired[
        List["AccountTokenCreateParamsIdentityIndividualAdditionalName"]
    ]
    """
    Additional names (e.g. aliases) associated with the individual.
    """
    address: NotRequired["AccountTokenCreateParamsIdentityIndividualAddress"]
    """
    The individual's residential address.
    """
    date_of_birth: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDateOfBirth"
    ]
    """
    The individual's date of birth.
    """
    documents: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocuments"
    ]
    """
    Documents that may be submitted to satisfy various informational requests.
    """
    email: NotRequired[str]
    """
    The individual's email address. You can only set this field when the Account is configured as a `merchant` or `recipient`. Use `contact_email` as the primary contact email for this Account.
    """
    given_name: NotRequired[str]
    """
    The individual's first name.
    """
    id_numbers: NotRequired[
        List["AccountTokenCreateParamsIdentityIndividualIdNumber"]
    ]
    """
    The identification numbers (e.g., SSN) associated with the individual.
    """
    legal_gender: NotRequired["Literal['female', 'male']|str"]
    """
    The individual's gender (International regulations require either "male" or "female").
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationalities: NotRequired[List[str]]
    """
    The countries where the individual is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    phone: NotRequired[str]
    """
    The individual's phone number.
    """
    political_exposure: NotRequired["Literal['existing', 'none']|str"]
    """
    The individual's political exposure.
    """
    relationship: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualRelationship"
    ]
    """
    The relationship that this individual has with the account's identity.
    """
    script_addresses: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptAddresses"
    ]
    """
    The script addresses (e.g., non-Latin characters) associated with the individual.
    """
    script_names: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptNames"
    ]
    """
    The individuals primary name in non latin script.
    """
    surname: NotRequired[str]
    """
    The individual's last name.
    """


class AccountTokenCreateParamsIdentityIndividualAdditionalAddress(TypedDict):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    purpose: Literal["registered"]
    """
    Purpose of additional address.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityIndividualAdditionalName(TypedDict):
    full_name: NotRequired[str]
    """
    The person's full name.
    """
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    purpose: Literal["alias", "maiden"]
    """
    The purpose or type of the additional name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class AccountTokenCreateParamsIdentityIndividualAddress(TypedDict):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityIndividualDateOfBirth(TypedDict):
    day: int
    """
    The day of the birth.
    """
    month: int
    """
    The month of birth.
    """
    year: int
    """
    The year of birth.
    """


class AccountTokenCreateParamsIdentityIndividualDocuments(TypedDict):
    company_authorization: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocumentsPassport"
    ]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    primary_verification: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocumentsPrimaryVerification"
    ]
    """
    An identifying document showing the person's name, either a passport or local ID card.
    """
    secondary_verification: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocumentsSecondaryVerification"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    visa: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualDocumentsVisa"
    ]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsCompanyAuthorization(
    TypedDict,
):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsPassport(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsPrimaryVerification(
    TypedDict,
):
    front_back: "AccountTokenCreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/files/create) tokens referring to each side of the document.
    """
    type: Union[Literal["front_back"], str]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsPrimaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsSecondaryVerification(
    TypedDict,
):
    front_back: "AccountTokenCreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/files/create) tokens referring to each side of the document.
    """
    type: Union[Literal["front_back"], str]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsSecondaryVerificationFrontBack(
    TypedDict,
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountTokenCreateParamsIdentityIndividualDocumentsVisa(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class AccountTokenCreateParamsIdentityIndividualIdNumber(TypedDict):
    type: Union[
        Literal[
            "ae_eid",
            "ae_pp",
            "al_pp",
            "am_pp",
            "ao_nif",
            "ar_cuil",
            "ar_dni",
            "ar_pp",
            "at_pp",
            "at_stn",
            "au_pp",
            "az_pin",
            "az_pp",
            "az_tin",
            "bd_brc",
            "bd_etin",
            "bd_nid",
            "bd_pp",
            "be_nrn",
            "be_pp",
            "bg_pp",
            "bg_ucn",
            "bh_pp",
            "bj_pp",
            "bn_nric",
            "bo_pp",
            "br_cpf",
            "br_pp",
            "br_rg",
            "bs_pp",
            "bs_tin",
            "by_pp",
            "ca_pp",
            "ca_sin",
            "ch_oasi",
            "ch_pp",
            "ci_pp",
            "cl_pp",
            "cl_rut",
            "cm_pp",
            "cn_pp",
            "co_nuip",
            "co_pp",
            "cr_ci",
            "cr_cpf",
            "cr_dimex",
            "cr_nite",
            "cr_pp",
            "cy_pp",
            "cy_tic",
            "cz_dic",
            "cz_pp",
            "cz_rc",
            "de_pp",
            "de_stn",
            "dk_cpr",
            "dk_pp",
            "do_cie",
            "do_pp",
            "do_rcn",
            "dz_pp",
            "ec_ci",
            "ec_pp",
            "ee_ik",
            "ee_pp",
            "eg_pp",
            "es_nif",
            "es_pp",
            "et_tin",
            "fi_hetu",
            "fi_pp",
            "fr_nir",
            "fr_pp",
            "fr_spi",
            "ga_nif",
            "gb_nino",
            "gb_pp",
            "ge_pp",
            "gh_pp",
            "gr_afm",
            "gr_pp",
            "gt_cui",
            "gt_nit",
            "gt_pp",
            "hk_id",
            "hk_pp",
            "hn_dni",
            "hn_pp",
            "hr_oib",
            "hr_pp",
            "ht_pp",
            "hu_ad",
            "hu_pp",
            "id_nik",
            "id_pp",
            "ie_pp",
            "ie_ppsn",
            "il_pp",
            "in_pan",
            "in_pp",
            "iq_pp",
            "is_kt",
            "is_pp",
            "it_cf",
            "it_pp",
            "je_pp",
            "jm_pp",
            "jo_pp",
            "jp_inc",
            "jp_pp",
            "ke_pin",
            "ke_pp",
            "kr_pp",
            "kw_pp",
            "kz_iin",
            "kz_pp",
            "lb_pp",
            "li_peid",
            "li_pp",
            "lk_pp",
            "lt_ak",
            "lt_pp",
            "lu_nif",
            "lu_pp",
            "lv_pk",
            "lv_pp",
            "ma_pp",
            "md_cf",
            "md_pp",
            "mg_nif",
            "mk_pin",
            "mk_pp",
            "mm_pp",
            "mn_pp",
            "mt_pp",
            "mu_pp",
            "mx_curp",
            "mx_pp",
            "mx_rfc",
            "my_nric",
            "my_pp",
            "mz_nuit",
            "ng_nin",
            "ng_pp",
            "nl_bsn",
            "nl_pp",
            "no_nin",
            "no_pp",
            "np_pp",
            "nz_ird",
            "nz_pp",
            "pa_pp",
            "pe_dni",
            "pe_pp",
            "ph_pp",
            "pk_cnic",
            "pk_pp",
            "pk_snic",
            "pl_pesel",
            "pl_pp",
            "pr_pp",
            "ps_pp",
            "pt_nif",
            "pt_pp",
            "py_ci",
            "py_pp",
            "ro_cnp",
            "ro_pp",
            "rs_pp",
            "ru_pp",
            "rw_tin",
            "sa_pp",
            "sa_ptin",
            "sa_tin",
            "se_pin",
            "se_pp",
            "sg_fin",
            "sg_nric",
            "sg_pp",
            "si_pp",
            "si_ptin",
            "sk_dic",
            "sk_pp",
            "sv_pp",
            "th_lc",
            "th_pin",
            "th_pp",
            "tn_pp",
            "tr_pp",
            "tr_tin",
            "tt_bir",
            "tw_pp",
            "ua_pp",
            "ug_pp",
            "us_itin",
            "us_itin_last_4",
            "us_pp",
            "us_ssn",
            "us_ssn_last_4",
            "uy_dni",
            "uy_pp",
            "uz_pp",
            "uz_tin",
            "ve_pp",
            "vn_pp",
            "za_id",
            "za_pp",
        ],
        str,
    ]
    """
    The ID number type of an individual.
    """
    value: str
    """
    The value of the ID number.
    """


class AccountTokenCreateParamsIdentityIndividualRelationship(TypedDict):
    director: NotRequired[bool]
    """
    Whether the person is a director of the account's identity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
    """
    executive: NotRequired[bool]
    """
    Whether the person has significant responsibility to control, manage, or direct the organization.
    """
    owner: NotRequired[bool]
    """
    Whether the person is an owner of the account's identity.
    """
    percent_ownership: NotRequired[Decimal]
    """
    The percent owned by the person of the account's legal entity.
    """
    title: NotRequired[str]
    """
    The person's title (e.g., CEO, Support Engineer).
    """


class AccountTokenCreateParamsIdentityIndividualScriptAddresses(TypedDict):
    kana: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptAddressesKana"
    ]
    """
    Kana Address.
    """
    kanji: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptAddressesKanji"
    ]
    """
    Kanji Address.
    """


class AccountTokenCreateParamsIdentityIndividualScriptAddressesKana(TypedDict):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityIndividualScriptAddressesKanji(
    TypedDict
):
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
    Address line 1 (e.g., street, PO Box, or company name).
    """
    line2: NotRequired[str]
    """
    Address line 2 (e.g., apartment, suite, unit, or building).
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """
    town: NotRequired[str]
    """
    Town or district.
    """


class AccountTokenCreateParamsIdentityIndividualScriptNames(TypedDict):
    kana: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptNamesKana"
    ]
    """
    Persons name in kana script.
    """
    kanji: NotRequired[
        "AccountTokenCreateParamsIdentityIndividualScriptNamesKanji"
    ]
    """
    Persons name in kanji script.
    """


class AccountTokenCreateParamsIdentityIndividualScriptNamesKana(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class AccountTokenCreateParamsIdentityIndividualScriptNamesKanji(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """
