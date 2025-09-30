# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountCreatePersonParams(RequestOptions):
    additional_tos_acceptances: NotRequired[
        "AccountCreatePersonParamsAdditionalTosAcceptances"
    ]
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """
    address: NotRequired["AccountCreatePersonParamsAddress"]
    """
    The person's address.
    """
    address_kana: NotRequired["AccountCreatePersonParamsAddressKana"]
    """
    The Kana variation of the person's address (Japan only).
    """
    address_kanji: NotRequired["AccountCreatePersonParamsAddressKanji"]
    """
    The Kanji variation of the person's address (Japan only).
    """
    dob: NotRequired["Literal['']|AccountCreatePersonParamsDob"]
    """
    The person's date of birth.
    """
    documents: NotRequired["AccountCreatePersonParamsDocuments"]
    """
    Documents that may be submitted to satisfy various informational requests.
    """
    email: NotRequired[str]
    """
    The person's email address.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    first_name: NotRequired[str]
    """
    The person's first name.
    """
    first_name_kana: NotRequired[str]
    """
    The Kana variation of the person's first name (Japan only).
    """
    first_name_kanji: NotRequired[str]
    """
    The Kanji variation of the person's first name (Japan only).
    """
    full_name_aliases: NotRequired["Literal['']|List[str]"]
    """
    A list of alternate names or aliases that the person is known by.
    """
    gender: NotRequired[str]
    """
    The person's gender (International regulations require either "male" or "female").
    """
    id_number: NotRequired[str]
    """
    The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    """
    id_number_secondary: NotRequired[str]
    """
    The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    """
    last_name: NotRequired[str]
    """
    The person's last name.
    """
    last_name_kana: NotRequired[str]
    """
    The Kana variation of the person's last name (Japan only).
    """
    last_name_kanji: NotRequired[str]
    """
    The Kanji variation of the person's last name (Japan only).
    """
    maiden_name: NotRequired[str]
    """
    The person's maiden name.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    nationality: NotRequired[str]
    """
    The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    """
    person_token: NotRequired[str]
    """
    A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    """
    phone: NotRequired[str]
    """
    The person's phone number.
    """
    political_exposure: NotRequired[Literal["existing", "none"]]
    """
    Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    """
    registered_address: NotRequired[
        "AccountCreatePersonParamsRegisteredAddress"
    ]
    """
    The person's registered address.
    """
    relationship: NotRequired["AccountCreatePersonParamsRelationship"]
    """
    The relationship that this person has with the account's legal entity.
    """
    ssn_last_4: NotRequired[str]
    """
    The last four digits of the person's Social Security number (U.S. only).
    """
    us_cfpb_data: NotRequired["AccountCreatePersonParamsUsCfpbData"]
    """
    Demographic data related to the person.
    """
    verification: NotRequired["AccountCreatePersonParamsVerification"]
    """
    The person's verification status.
    """


class AccountCreatePersonParamsAdditionalTosAcceptances(TypedDict):
    account: NotRequired[
        "AccountCreatePersonParamsAdditionalTosAcceptancesAccount"
    ]
    """
    Details on the legal guardian's acceptance of the main Stripe service agreement.
    """


class AccountCreatePersonParamsAdditionalTosAcceptancesAccount(TypedDict):
    date: NotRequired[int]
    """
    The Unix timestamp marking when the account representative accepted the service agreement.
    """
    ip: NotRequired[str]
    """
    The IP address from which the account representative accepted the service agreement.
    """
    user_agent: NotRequired["Literal['']|str"]
    """
    The user agent of the browser from which the account representative accepted the service agreement.
    """


class AccountCreatePersonParamsAddress(TypedDict):
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
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """


class AccountCreatePersonParamsAddressKana(TypedDict):
    city: NotRequired[str]
    """
    City or ward.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Block or building number.
    """
    line2: NotRequired[str]
    """
    Building details.
    """
    postal_code: NotRequired[str]
    """
    Postal code.
    """
    state: NotRequired[str]
    """
    Prefecture.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountCreatePersonParamsAddressKanji(TypedDict):
    city: NotRequired[str]
    """
    City or ward.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Block or building number.
    """
    line2: NotRequired[str]
    """
    Building details.
    """
    postal_code: NotRequired[str]
    """
    Postal code.
    """
    state: NotRequired[str]
    """
    Prefecture.
    """
    town: NotRequired[str]
    """
    Town or cho-me.
    """


class AccountCreatePersonParamsDob(TypedDict):
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


class AccountCreatePersonParamsDocuments(TypedDict):
    company_authorization: NotRequired[
        "AccountCreatePersonParamsDocumentsCompanyAuthorization"
    ]
    """
    One or more documents that demonstrate proof that this person is authorized to represent the company.
    """
    passport: NotRequired["AccountCreatePersonParamsDocumentsPassport"]
    """
    One or more documents showing the person's passport page with photo and personal data.
    """
    visa: NotRequired["AccountCreatePersonParamsDocumentsVisa"]
    """
    One or more documents showing the person's visa required for living in the country where they are residing.
    """


class AccountCreatePersonParamsDocumentsCompanyAuthorization(TypedDict):
    files: NotRequired[List[str]]
    """
    One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
    """


class AccountCreatePersonParamsDocumentsPassport(TypedDict):
    files: NotRequired[List[str]]
    """
    One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
    """


class AccountCreatePersonParamsDocumentsVisa(TypedDict):
    files: NotRequired[List[str]]
    """
    One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
    """


class AccountCreatePersonParamsRegisteredAddress(TypedDict):
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
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """


class AccountCreatePersonParamsRelationship(TypedDict):
    authorizer: NotRequired[bool]
    """
    Whether the person is the authorizer of the account's representative.
    """
    director: NotRequired[bool]
    """
    Whether the person is a director of the account's legal entity. Directors are typically members of the governing board of the company, or responsible for ensuring the company meets its regulatory obligations.
    """
    executive: NotRequired[bool]
    """
    Whether the person has significant responsibility to control, manage, or direct the organization.
    """
    legal_guardian: NotRequired[bool]
    """
    Whether the person is the legal guardian of the account's representative.
    """
    owner: NotRequired[bool]
    """
    Whether the person is an owner of the account's legal entity.
    """
    percent_ownership: NotRequired["Literal['']|float"]
    """
    The percent owned by the person of the account's legal entity.
    """
    representative: NotRequired[bool]
    """
    Whether the person is authorized as the primary representative of the account. This is the person nominated by the business to provide information about themselves, and general information about the account. There can only be one representative at any given time. At the time the account is created, this person should be set to the person responsible for opening the account.
    """
    title: NotRequired[str]
    """
    The person's title (e.g., CEO, Support Engineer).
    """


class AccountCreatePersonParamsUsCfpbData(TypedDict):
    ethnicity_details: NotRequired[
        "AccountCreatePersonParamsUsCfpbDataEthnicityDetails"
    ]
    """
    The persons ethnicity details
    """
    race_details: NotRequired["AccountCreatePersonParamsUsCfpbDataRaceDetails"]
    """
    The persons race details
    """
    self_identified_gender: NotRequired[str]
    """
    The persons self-identified gender
    """


class AccountCreatePersonParamsUsCfpbDataEthnicityDetails(TypedDict):
    ethnicity: NotRequired[
        List[
            Literal[
                "cuban",
                "hispanic_or_latino",
                "mexican",
                "not_hispanic_or_latino",
                "other_hispanic_or_latino",
                "prefer_not_to_answer",
                "puerto_rican",
            ]
        ]
    ]
    """
    The persons ethnicity
    """
    ethnicity_other: NotRequired[str]
    """
    Please specify your origin, when other is selected.
    """


class AccountCreatePersonParamsUsCfpbDataRaceDetails(TypedDict):
    race: NotRequired[
        List[
            Literal[
                "african_american",
                "american_indian_or_alaska_native",
                "asian",
                "asian_indian",
                "black_or_african_american",
                "chinese",
                "ethiopian",
                "filipino",
                "guamanian_or_chamorro",
                "haitian",
                "jamaican",
                "japanese",
                "korean",
                "native_hawaiian",
                "native_hawaiian_or_other_pacific_islander",
                "nigerian",
                "other_asian",
                "other_black_or_african_american",
                "other_pacific_islander",
                "prefer_not_to_answer",
                "samoan",
                "somali",
                "vietnamese",
                "white",
            ]
        ]
    ]
    """
    The persons race.
    """
    race_other: NotRequired[str]
    """
    Please specify your race, when other is selected.
    """


class AccountCreatePersonParamsVerification(TypedDict):
    additional_document: NotRequired[
        "AccountCreatePersonParamsVerificationAdditionalDocument"
    ]
    """
    A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
    """
    document: NotRequired["AccountCreatePersonParamsVerificationDocument"]
    """
    An identifying document, either a passport or local ID card.
    """


class AccountCreatePersonParamsVerificationAdditionalDocument(TypedDict):
    back: NotRequired[str]
    """
    The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """


class AccountCreatePersonParamsVerificationDocument(TypedDict):
    back: NotRequired[str]
    """
    The back of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
    front: NotRequired[str]
    """
    The front of an ID returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
    """
