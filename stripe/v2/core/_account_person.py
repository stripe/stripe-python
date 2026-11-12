# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class AccountPerson(StripeObject):
    """
    A Person represents an individual associated with an Account's identity (for example, an owner, director, executive, or representative). Use Persons to provide and update identity information for verification and compliance.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.account_person"]] = (
        "v2.core.account_person"
    )

    class AdditionalAddress(StripeObject):
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
        purpose: Literal["registered"]
        """
        Purpose of additional address.
        """
        state: Optional[str]
        """
        State, county, province, or region.
        """
        town: Optional[str]
        """
        Town or district.
        """

    class AdditionalName(StripeObject):
        full_name: Optional[str]
        """
        The individual's full name.
        """
        given_name: Optional[str]
        """
        The individual's first or given name.
        """
        purpose: Literal["alias", "maiden"]
        """
        The purpose or type of the additional name.
        """
        surname: Optional[str]
        """
        The individual's last or family name.
        """

    class AdditionalTermsOfService(StripeObject):
        class Account(StripeObject):
            date: Optional[str]
            """
            The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
            """
            ip: Optional[str]
            """
            The IP address from which the Account's representative accepted the terms of service.
            """
            user_agent: Optional[str]
            """
            The user agent of the browser from which the Account's representative accepted the terms of service.
            """

        account: Optional[Account]
        """
        Stripe terms of service agreement.
        """
        _inner_class_types = {"account": Account}

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
        town: Optional[str]
        """
        Town or district.
        """

    class DateOfBirth(StripeObject):
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

    class Documents(StripeObject):
        class CompanyAuthorization(StripeObject):
            files: List[str]
            """
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
            """
            type: Union[Literal["files"], str]
            """
            The format of the document. Currently supports `files` only.
            """

        class Passport(StripeObject):
            files: List[str]
            """
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
            """
            type: Union[Literal["files"], str]
            """
            The format of the document. Currently supports `files` only.
            """

        class PrimaryVerification(StripeObject):
            class FrontBack(StripeObject):
                back: Optional[str]
                """
                A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                """
                front: str
                """
                A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                """

            front_back: FrontBack
            """
            The [file upload](https://docs.stripe.com/api/files/create) tokens for the front and back of the verification document.
            """
            type: Union[Literal["front_back"], str]
            """
            The format of the verification document. Currently supports `front_back` only.
            """
            _inner_class_types = {"front_back": FrontBack}

        class SecondaryVerification(StripeObject):
            class FrontBack(StripeObject):
                back: Optional[str]
                """
                A [file upload](https://docs.stripe.com/api/files/create) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                """
                front: str
                """
                A [file upload](https://docs.stripe.com/api/files/create) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
                """

            front_back: FrontBack
            """
            The [file upload](https://docs.stripe.com/api/files/create) tokens for the front and back of the verification document.
            """
            type: Union[Literal["front_back"], str]
            """
            The format of the verification document. Currently supports `front_back` only.
            """
            _inner_class_types = {"front_back": FrontBack}

        class Visa(StripeObject):
            files: List[str]
            """
            One or more document IDs returned by a [file upload](https://docs.stripe.com/api/files/create) with a purpose value of `account_requirement`.
            """
            type: Union[Literal["files"], str]
            """
            The format of the document. Currently supports `files` only.
            """

        company_authorization: Optional[CompanyAuthorization]
        """
        One or more documents that demonstrate proof that this person is authorized to represent the company.
        """
        passport: Optional[Passport]
        """
        One or more documents showing the person's passport page with photo and personal data.
        """
        primary_verification: Optional[PrimaryVerification]
        """
        An identifying document showing the person's name, either a passport or local ID card.
        """
        secondary_verification: Optional[SecondaryVerification]
        """
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
        """
        visa: Optional[Visa]
        """
        One or more documents showing the person's visa required for living in the country where they are residing.
        """
        _inner_class_types = {
            "company_authorization": CompanyAuthorization,
            "passport": Passport,
            "primary_verification": PrimaryVerification,
            "secondary_verification": SecondaryVerification,
            "visa": Visa,
        }

    class IdNumber(StripeObject):
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

    class Relationship(StripeObject):
        authorizer: Optional[bool]
        """
        Whether the individual is an authorizer of the Account's identity.
        """
        director: Optional[bool]
        """
        Whether the individual is a director of the Account's identity. Directors are typically members of the governing board of the company or are responsible for making sure that the company meets its regulatory obligations.
        """
        executive: Optional[bool]
        """
        Whether the individual has significant responsibility to control, manage, or direct the organization.
        """
        legal_guardian: Optional[bool]
        """
        Whether the individual is the legal guardian of the Account's representative.
        """
        owner: Optional[bool]
        """
        Whether the individual is an owner of the Account's identity.
        """
        percent_ownership: Optional[Decimal]
        """
        The percentage of the Account's identity that the individual owns.
        """
        representative: Optional[bool]
        """
        Whether the individual is authorized as the primary representative of the Account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
        """
        title: Optional[str]
        """
        The individual's title (e.g., CEO, Support Engineer).
        """
        _field_encodings = {"percent_ownership": "decimal_string"}

    class ScriptAddresses(StripeObject):
        class Kana(StripeObject):
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
            town: Optional[str]
            """
            Town or district.
            """

        class Kanji(StripeObject):
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
            town: Optional[str]
            """
            Town or district.
            """

        kana: Optional[Kana]
        """
        Kana Address.
        """
        kanji: Optional[Kanji]
        """
        Kanji Address.
        """
        _inner_class_types = {"kana": Kana, "kanji": Kanji}

    class ScriptNames(StripeObject):
        class Kana(StripeObject):
            given_name: Optional[str]
            """
            The person's first or given name.
            """
            surname: Optional[str]
            """
            The person's last or family name.
            """

        class Kanji(StripeObject):
            given_name: Optional[str]
            """
            The person's first or given name.
            """
            surname: Optional[str]
            """
            The person's last or family name.
            """

        kana: Optional[Kana]
        """
        Persons name in kana script.
        """
        kanji: Optional[Kanji]
        """
        Persons name in kanji script.
        """
        _inner_class_types = {"kana": Kana, "kanji": Kanji}

    account: str
    """
    The account ID which the individual belongs to.
    """
    additional_addresses: Optional[List[AdditionalAddress]]
    """
    Additional addresses associated with the person.
    """
    additional_names: Optional[List[AdditionalName]]
    """
    Additional names (e.g. aliases) associated with the person.
    """
    additional_terms_of_service: Optional[AdditionalTermsOfService]
    """
    Attestations of accepted terms of service agreements.
    """
    address: Optional[Address]
    """
    The person's residential address.
    """
    created: str
    """
    Time at which the object was created. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    date_of_birth: Optional[DateOfBirth]
    """
    The person's date of birth.
    """
    documents: Optional[Documents]
    """
    Documents that may be submitted to satisfy various informational requests.
    """
    email: Optional[str]
    """
    The person's email address.
    """
    given_name: Optional[str]
    """
    The person's first name.
    """
    id: str
    """
    Unique identifier for the Person.
    """
    id_numbers: Optional[List[IdNumber]]
    """
    The identification numbers (e.g., SSN) associated with the person.
    """
    legal_gender: Optional[Union[Literal["female", "male"], str]]
    """
    The person's gender (International regulations require either "male" or "female").
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    nationalities: Optional[List[str]]
    """
    The countries where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    object: Literal["v2.core.account_person"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    phone: Optional[str]
    """
    The person's phone number.
    """
    political_exposure: Optional[Union[Literal["existing", "none"], str]]
    """
    The person's political exposure.
    """
    relationship: Optional[Relationship]
    """
    The relationship that this person has with the Account's business or legal entity.
    """
    script_addresses: Optional[ScriptAddresses]
    """
    The script addresses (e.g., non-Latin characters) associated with the person.
    """
    script_names: Optional[ScriptNames]
    """
    The script names (e.g. non-Latin characters) associated with the person.
    """
    surname: Optional[str]
    """
    The person's last name.
    """
    updated: str
    """
    Time at which the object was last updated. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    _inner_class_types = {
        "additional_addresses": AdditionalAddress,
        "additional_names": AdditionalName,
        "additional_terms_of_service": AdditionalTermsOfService,
        "address": Address,
        "date_of_birth": DateOfBirth,
        "documents": Documents,
        "id_numbers": IdNumber,
        "relationship": Relationship,
        "script_addresses": ScriptAddresses,
        "script_names": ScriptNames,
    }
