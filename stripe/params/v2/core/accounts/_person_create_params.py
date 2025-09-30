# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class PersonCreateParams(TypedDict):
    additional_addresses: NotRequired[
        List["PersonCreateParamsAdditionalAddress"]
    ]
    """
    Additional addresses associated with the person.
    """
    additional_names: NotRequired[List["PersonCreateParamsAdditionalName"]]
    """
    Additional names (e.g. aliases) associated with the person.
    """
    additional_terms_of_service: NotRequired[
        "PersonCreateParamsAdditionalTermsOfService"
    ]
    """
    Attestations of accepted terms of service agreements.
    """
    address: NotRequired["PersonCreateParamsAddress"]
    """
    The person's residential address.
    """
    date_of_birth: NotRequired["PersonCreateParamsDateOfBirth"]
    """
    The person's date of birth.
    """
    documents: NotRequired["PersonCreateParamsDocuments"]
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
    id_numbers: NotRequired[List["PersonCreateParamsIdNumber"]]
    """
    The identification numbers (e.g., SSN) associated with the person.
    """
    legal_gender: NotRequired[Literal["female", "male"]]
    """
    The person's gender (International regulations require either "male" or "female").
    """
    metadata: NotRequired[Dict[str, str]]
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
    political_exposure: NotRequired[Literal["existing", "none"]]
    """
    The person's political exposure.
    """
    relationship: NotRequired["PersonCreateParamsRelationship"]
    """
    The relationship that this person has with the Account's business or legal entity.
    """
    script_addresses: NotRequired["PersonCreateParamsScriptAddresses"]
    """
    The script addresses (e.g., non-Latin characters) associated with the person.
    """
    script_names: NotRequired["PersonCreateParamsScriptNames"]
    """
    The script names (e.g. non-Latin characters) associated with the person.
    """
    surname: NotRequired[str]
    """
    The person's last name.
    """


class PersonCreateParamsAdditionalAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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
    Town or cho-me.
    """


class PersonCreateParamsAdditionalName(TypedDict):
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


class PersonCreateParamsAdditionalTermsOfService(TypedDict):
    account: NotRequired["PersonCreateParamsAdditionalTermsOfServiceAccount"]
    """
    Stripe terms of service agreement.
    """


class PersonCreateParamsAdditionalTermsOfServiceAccount(TypedDict):
    date: str
    """
    The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    ip: str
    """
    The IP address from which the Account's representative accepted the terms of service.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the Account's representative accepted the terms of service.
    """


class PersonCreateParamsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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
    Town or cho-me.
    """


class PersonCreateParamsDateOfBirth(TypedDict):
    day: int
    """
    The day of birth.
    """
    month: int
    """
    The month of birth.
    """
    year: int
    """
    The year of birth.
    """


class PersonCreateParamsDocuments(TypedDict):
    company_authorization: NotRequired[
        "PersonCreateParamsDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired["PersonCreateParamsDocumentsPassport"]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    primary_verification: NotRequired[
        "PersonCreateParamsDocumentsPrimaryVerification"
    ]
    """
    An identifying document showing the person's name, either a passport or local ID card.
    """
    secondary_verification: NotRequired[
        "PersonCreateParamsDocumentsSecondaryVerification"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    visa: NotRequired["PersonCreateParamsDocumentsVisa"]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class PersonCreateParamsDocumentsCompanyAuthorization(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonCreateParamsDocumentsPassport(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonCreateParamsDocumentsPrimaryVerification(TypedDict):
    front_back: "PersonCreateParamsDocumentsPrimaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class PersonCreateParamsDocumentsPrimaryVerificationFrontBack(TypedDict):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: str
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class PersonCreateParamsDocumentsSecondaryVerification(TypedDict):
    front_back: "PersonCreateParamsDocumentsSecondaryVerificationFrontBack"
    """
    The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
    """
    type: Literal["front_back"]
    """
    The format of the verification document. Currently supports `front_back` only.
    """


class PersonCreateParamsDocumentsSecondaryVerificationFrontBack(TypedDict):
    back: NotRequired[str]
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: str
    """
    A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class PersonCreateParamsDocumentsVisa(TypedDict):
    files: List[str]
    """
    One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
    """
    type: Literal["files"]
    """
    The format of the document. Currently supports `files` only.
    """


class PersonCreateParamsIdNumber(TypedDict):
    type: Literal[
        "ae_eid",
        "ao_nif",
        "az_tin",
        "bd_brc",
        "bd_etin",
        "bd_nid",
        "br_cpf",
        "cr_cpf",
        "cr_dimex",
        "cr_nite",
        "de_stn",
        "do_rcn",
        "gt_nit",
        "hk_id",
        "kz_iin",
        "mx_rfc",
        "my_nric",
        "mz_nuit",
        "nl_bsn",
        "pe_dni",
        "pk_cnic",
        "pk_snic",
        "sa_tin",
        "sg_fin",
        "sg_nric",
        "th_lc",
        "th_pin",
        "us_itin",
        "us_itin_last_4",
        "us_ssn",
        "us_ssn_last_4",
    ]
    """
    The ID number type of an individual.
    """
    value: str
    """
    The value of the ID number.
    """


class PersonCreateParamsRelationship(TypedDict):
    authorizer: NotRequired[bool]
    """
    Whether the individual is an authorizer of the Account's legal entity.
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
    percent_ownership: NotRequired[str]
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


class PersonCreateParamsScriptAddresses(TypedDict):
    kana: NotRequired["PersonCreateParamsScriptAddressesKana"]
    """
    Kana Address.
    """
    kanji: NotRequired["PersonCreateParamsScriptAddressesKanji"]
    """
    Kanji Address.
    """


class PersonCreateParamsScriptAddressesKana(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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
    Town or cho-me.
    """


class PersonCreateParamsScriptAddressesKanji(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: str
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
    Town or cho-me.
    """


class PersonCreateParamsScriptNames(TypedDict):
    kana: NotRequired["PersonCreateParamsScriptNamesKana"]
    """
    Persons name in kana script.
    """
    kanji: NotRequired["PersonCreateParamsScriptNamesKanji"]
    """
    Persons name in kanji script.
    """


class PersonCreateParamsScriptNamesKana(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """


class PersonCreateParamsScriptNamesKanji(TypedDict):
    given_name: NotRequired[str]
    """
    The person's first or given name.
    """
    surname: NotRequired[str]
    """
    The person's last or family name.
    """
