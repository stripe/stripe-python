# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Optional, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PersonTokenCreateParams(TypedDict):
    additional_addresses: NotRequired[
        List["PersonTokenCreateParamsAdditionalAddress"]
    ]
    """
    Additional addresses associated with the person.
    """
    additional_names: NotRequired[
        List["PersonTokenCreateParamsAdditionalName"]
    ]
    """
    Additional names (e.g. aliases) associated with the person.
    """
    additional_terms_of_service: NotRequired[
        "PersonTokenCreateParamsAdditionalTermsOfService"
    ]
    """
    Attestations of accepted terms of service agreements.
    """
    address: NotRequired["PersonTokenCreateParamsAddress"]
    """
    The person's residential address.
    """
    date_of_birth: NotRequired["PersonTokenCreateParamsDateOfBirth"]
    """
    The person's date of birth.
    """
    documents: NotRequired["PersonTokenCreateParamsDocuments"]
    """
    Documents that may be submitted to satisfy various informational requests.
    """
    email: NotRequired[str]
    """
    Email.
    """
    given_name: NotRequired[str]
    """
    The person's first name.
    """
    id_numbers: NotRequired[List["PersonTokenCreateParamsIdNumber"]]
    """
    The identification numbers (e.g., SSN) associated with the person.
    """
    legal_gender: NotRequired["Literal['female', 'male']|str"]
    """
    The person's gender (International regulations require either "male" or "female").
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationalities: NotRequired[List[str]]
    """
    The nationalities (countries) this person is associated with.
    """
    phone: NotRequired[str]
    """
    The phone number for this person.
    """
    political_exposure: NotRequired["Literal['existing', 'none']|str"]
    """
    The person's political exposure.
    """
    relationship: NotRequired["PersonTokenCreateParamsRelationship"]
    """
    The relationship that this person has with the Account's business or legal entity.
    """
    script_addresses: NotRequired["PersonTokenCreateParamsScriptAddresses"]
    """
    The script addresses (e.g., non-Latin characters) associated with the person.
    """
    script_names: NotRequired["PersonTokenCreateParamsScriptNames"]
    """
    The script names (e.g. non-Latin characters) associated with the person.
    """
    surname: NotRequired[str]
    """
    The person's last name.
    """


class PersonTokenCreateParamsAdditionalAddress(TypedDict):
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


class PersonTokenCreateParamsAdditionalName(TypedDict):
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


class PersonTokenCreateParamsAdditionalTermsOfService(TypedDict):
    account: NotRequired[
        "PersonTokenCreateParamsAdditionalTermsOfServiceAccount"
    ]
    """
    Details on the Person's acceptance of the [Stripe Services Agreement]; IP, date, and User Agent are expanded by Stripe.
    """


class PersonTokenCreateParamsAdditionalTermsOfServiceAccount(TypedDict):
    shown_and_accepted: NotRequired[bool]
    """
    The boolean value indicating if the terms of service have been accepted.
    """


class PersonTokenCreateParamsAddress(TypedDict):
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


class PersonTokenCreateParamsDateOfBirth(TypedDict):
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


class PersonTokenCreateParamsDocuments(TypedDict):
    company_authorization: NotRequired[
        "PersonTokenCreateParamsDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired["PersonTokenCreateParamsDocumentsPassport"]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    primary_verification: NotRequired[
        "PersonTokenCreateParamsDocumentsPrimaryVerification"
    ]
    """
    An identifying document showing the person's name, either a passport or local ID card.
    """
    secondary_verification: NotRequired[
        "PersonTokenCreateParamsDocumentsSecondaryVerification"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    visa: NotRequired["PersonTokenCreateParamsDocumentsVisa"]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class PersonTokenCreateParamsDocumentsCompanyAuthorization(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonTokenCreateParamsDocumentsPassport(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonTokenCreateParamsDocumentsPrimaryVerification(TypedDict):
    front_back: "PersonTokenCreateParamsDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/files/create) tokens referring to each side of the document.
    """
    type: Union[Literal["front_back"], str]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class PersonTokenCreateParamsDocumentsPrimaryVerificationFrontBack(TypedDict):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class PersonTokenCreateParamsDocumentsSecondaryVerification(TypedDict):
    front_back: (
        "PersonTokenCreateParamsDocumentsSecondaryVerificationFrontBack"
    )
    """
    The [file upload](https://docs.stripe.com/api/files/create) tokens referring to each side of the document.
    """
    type: Union[Literal["front_back"], str]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class PersonTokenCreateParamsDocumentsSecondaryVerificationFrontBack(
    TypedDict
):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class PersonTokenCreateParamsDocumentsVisa(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
    """
    type: Union[Literal["files"], str]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonTokenCreateParamsIdNumber(TypedDict):
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


class PersonTokenCreateParamsRelationship(TypedDict):
    authorizer: NotRequired[bool]
    """
    Whether the individual is an authorizer of the Account's identity.
    """
    director: NotRequired[bool]
    """
    Indicates whether the person is a director of the associated legal entity.
    """
    executive: NotRequired[bool]
    """
    Indicates whether the person is an executive of the associated legal entity.
    """
    legal_guardian: NotRequired[bool]
    """
    Indicates whether the person is a legal guardian of the associated legal entity.
    """
    owner: NotRequired[bool]
    """
    Indicates whether the person is an owner of the associated legal entity.
    """
    percent_ownership: NotRequired[Decimal]
    """
    The percentage of ownership the person has in the associated legal entity.
    """
    representative: NotRequired[bool]
    """
    Indicates whether the person is a representative of the associated legal entity.
    """
    title: NotRequired[str]
    """
    The title or position the person holds in the associated legal entity.
    """


class PersonTokenCreateParamsScriptAddresses(TypedDict):
    kana: NotRequired["PersonTokenCreateParamsScriptAddressesKana"]
    """
    Kana Address.
    """
    kanji: NotRequired["PersonTokenCreateParamsScriptAddressesKanji"]
    """
    Kanji Address.
    """


class PersonTokenCreateParamsScriptAddressesKana(TypedDict):
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


class PersonTokenCreateParamsScriptAddressesKanji(TypedDict):
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


class PersonTokenCreateParamsScriptNames(TypedDict):
    kana: NotRequired["PersonTokenCreateParamsScriptNamesKana"]
    """
    Persons name in kana script.
    """
    kanji: NotRequired["PersonTokenCreateParamsScriptNamesKanji"]
    """
    Persons name in kanji script.
    """


class PersonTokenCreateParamsScriptNamesKana(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class PersonTokenCreateParamsScriptNamesKanji(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """
