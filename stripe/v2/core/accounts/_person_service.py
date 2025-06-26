# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.core._person import Person
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class PersonService(StripeService):
    class CreateParams(TypedDict):
        additional_addresses: NotRequired[
            List["PersonService.CreateParamsAdditionalAddress"]
        ]
        """
        Additional addresses associated with the person.
        """
        additional_names: NotRequired[
            List["PersonService.CreateParamsAdditionalName"]
        ]
        """
        Additional names (e.g. aliases) associated with the person.
        """
        additional_terms_of_service: NotRequired[
            "PersonService.CreateParamsAdditionalTermsOfService"
        ]
        """
        Attestations of accepted terms of service agreements.
        """
        address: NotRequired["PersonService.CreateParamsAddress"]
        """
        The person's residential address.
        """
        date_of_birth: NotRequired["PersonService.CreateParamsDateOfBirth"]
        """
        The person's date of birth.
        """
        documents: NotRequired["PersonService.CreateParamsDocuments"]
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
        id_numbers: NotRequired[List["PersonService.CreateParamsIdNumber"]]
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
        nationalities: NotRequired[
            List[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
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
        relationship: NotRequired["PersonService.CreateParamsRelationship"]
        """
        The relationship that this person has with the Account's business or legal entity.
        """
        script_addresses: NotRequired[
            "PersonService.CreateParamsScriptAddresses"
        ]
        """
        The script addresses (e.g., non-Latin characters) associated with the person.
        """
        script_names: NotRequired["PersonService.CreateParamsScriptNames"]
        """
        The script names (e.g. non-Latin characters) associated with the person.
        """
        surname: NotRequired[str]
        """
        The person's last name.
        """

    class CreateParamsAdditionalAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsAdditionalName(TypedDict):
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

    class CreateParamsAdditionalTermsOfService(TypedDict):
        account: NotRequired[
            "PersonService.CreateParamsAdditionalTermsOfServiceAccount"
        ]
        """
        Stripe terms of service agreement.
        """

    class CreateParamsAdditionalTermsOfServiceAccount(TypedDict):
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

    class CreateParamsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsDateOfBirth(TypedDict):
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

    class CreateParamsDocuments(TypedDict):
        company_authorization: NotRequired[
            "PersonService.CreateParamsDocumentsCompanyAuthorization"
        ]
        """
        One or more documents that demonstrate proof that this person is authorized to represent the company.
        """
        passport: NotRequired["PersonService.CreateParamsDocumentsPassport"]
        """
        One or more documents showing the person's passport page with photo and personal data.
        """
        primary_verification: NotRequired[
            "PersonService.CreateParamsDocumentsPrimaryVerification"
        ]
        """
        An identifying document showing the person's name, either a passport or local ID card.
        """
        secondary_verification: NotRequired[
            "PersonService.CreateParamsDocumentsSecondaryVerification"
        ]
        """
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
        """
        visa: NotRequired["PersonService.CreateParamsDocumentsVisa"]
        """
        One or more documents showing the person's visa required for living in the country where they are residing.
        """

    class CreateParamsDocumentsCompanyAuthorization(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsDocumentsPassport(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsDocumentsPrimaryVerification(TypedDict):
        front_back: (
            "PersonService.CreateParamsDocumentsPrimaryVerificationFrontBack"
        )
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class CreateParamsDocumentsPrimaryVerificationFrontBack(TypedDict):
        back: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: str
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class CreateParamsDocumentsSecondaryVerification(TypedDict):
        front_back: (
            "PersonService.CreateParamsDocumentsSecondaryVerificationFrontBack"
        )
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class CreateParamsDocumentsSecondaryVerificationFrontBack(TypedDict):
        back: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: str
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class CreateParamsDocumentsVisa(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class CreateParamsIdNumber(TypedDict):
        type: Literal[
            "ae_eid",
            "br_cpf",
            "de_stn",
            "hk_id",
            "mx_rfc",
            "my_nric",
            "nl_bsn",
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

    class CreateParamsRelationship(TypedDict):
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

    class CreateParamsScriptAddresses(TypedDict):
        kana: NotRequired["PersonService.CreateParamsScriptAddressesKana"]
        """
        Kana Address.
        """
        kanji: NotRequired["PersonService.CreateParamsScriptAddressesKanji"]
        """
        Kanji Address.
        """

    class CreateParamsScriptAddressesKana(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsScriptAddressesKanji(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "ax",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bl",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cw",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "qz",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "xx",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
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

    class CreateParamsScriptNames(TypedDict):
        kana: NotRequired["PersonService.CreateParamsScriptNamesKana"]
        """
        Persons name in kana script.
        """
        kanji: NotRequired["PersonService.CreateParamsScriptNamesKanji"]
        """
        Persons name in kanji script.
        """

    class CreateParamsScriptNamesKana(TypedDict):
        given_name: NotRequired[str]
        """
        The person's first or given name.
        """
        surname: NotRequired[str]
        """
        The person's last or family name.
        """

    class CreateParamsScriptNamesKanji(TypedDict):
        given_name: NotRequired[str]
        """
        The person's first or given name.
        """
        surname: NotRequired[str]
        """
        The person's last or family name.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        The upper limit on the number of accounts returned by the List Account request.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        additional_addresses: NotRequired[
            List["PersonService.UpdateParamsAdditionalAddress"]
        ]
        """
        Additional addresses associated with the person.
        """
        additional_names: NotRequired[
            List["PersonService.UpdateParamsAdditionalName"]
        ]
        """
        Additional names (e.g. aliases) associated with the person.
        """
        additional_terms_of_service: NotRequired[
            "PersonService.UpdateParamsAdditionalTermsOfService"
        ]
        """
        Attestations of accepted terms of service agreements.
        """
        address: NotRequired["PersonService.UpdateParamsAddress"]
        """
        The primary address associated with the person.
        """
        date_of_birth: NotRequired["PersonService.UpdateParamsDateOfBirth"]
        """
        The person's date of birth.
        """
        documents: NotRequired["PersonService.UpdateParamsDocuments"]
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
        id_numbers: NotRequired[List["PersonService.UpdateParamsIdNumber"]]
        """
        The identification numbers (e.g., SSN) associated with the person.
        """
        legal_gender: NotRequired[Literal["female", "male"]]
        """
        The person's gender (International regulations require either "male" or "female").
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        nationalities: NotRequired[
            List[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
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
        relationship: NotRequired["PersonService.UpdateParamsRelationship"]
        """
        The relationship that this person has with the Account's business or legal entity.
        """
        script_addresses: NotRequired[
            Optional["PersonService.UpdateParamsScriptAddresses"]
        ]
        """
        The script addresses (e.g., non-Latin characters) associated with the person.
        """
        script_names: NotRequired[
            Optional["PersonService.UpdateParamsScriptNames"]
        ]
        """
        The script names (e.g. non-Latin characters) associated with the person.
        """
        surname: NotRequired[str]
        """
        The person's last name.
        """

    class UpdateParamsAdditionalAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        purpose: Literal["registered"]
        """
        Purpose of additional address.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsAdditionalName(TypedDict):
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

    class UpdateParamsAdditionalTermsOfService(TypedDict):
        account: NotRequired[
            "PersonService.UpdateParamsAdditionalTermsOfServiceAccount"
        ]
        """
        Stripe terms of service agreement.
        """

    class UpdateParamsAdditionalTermsOfServiceAccount(TypedDict):
        date: NotRequired[str]
        """
        The time when the Account's representative accepted the terms of service. Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        ip: NotRequired[str]
        """
        The IP address from which the Account's representative accepted the terms of service.
        """
        user_agent: NotRequired[str]
        """
        The user agent of the browser from which the Account's representative accepted the terms of service.
        """

    class UpdateParamsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsDateOfBirth(TypedDict):
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

    class UpdateParamsDocuments(TypedDict):
        company_authorization: NotRequired[
            "PersonService.UpdateParamsDocumentsCompanyAuthorization"
        ]
        """
        One or more documents that demonstrate proof that this person is authorized to represent the company.
        """
        passport: NotRequired["PersonService.UpdateParamsDocumentsPassport"]
        """
        One or more documents showing the person's passport page with photo and personal data.
        """
        primary_verification: NotRequired[
            Optional["PersonService.UpdateParamsDocumentsPrimaryVerification"]
        ]
        """
        An identifying document showing the person's name, either a passport or local ID card.
        """
        secondary_verification: NotRequired[
            Optional[
                "PersonService.UpdateParamsDocumentsSecondaryVerification"
            ]
        ]
        """
        A document showing address, either a passport, local ID card, or utility bill from a well-known utility company.
        """
        visa: NotRequired["PersonService.UpdateParamsDocumentsVisa"]
        """
        One or more documents showing the person's visa required for living in the country where they are residing.
        """

    class UpdateParamsDocumentsCompanyAuthorization(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsDocumentsPassport(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsDocumentsPrimaryVerification(TypedDict):
        front_back: (
            "PersonService.UpdateParamsDocumentsPrimaryVerificationFrontBack"
        )
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class UpdateParamsDocumentsPrimaryVerificationFrontBack(TypedDict):
        back: NotRequired[Optional[str]]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class UpdateParamsDocumentsSecondaryVerification(TypedDict):
        front_back: (
            "PersonService.UpdateParamsDocumentsSecondaryVerificationFrontBack"
        )
        """
        The [file upload](https://docs.stripe.com/api/persons/update#create_file) tokens referring to each side of the document.
        """
        type: Literal["front_back"]
        """
        The format of the verification document. Currently supports `front_back` only.
        """

    class UpdateParamsDocumentsSecondaryVerificationFrontBack(TypedDict):
        back: NotRequired[Optional[str]]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the back of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """
        front: NotRequired[str]
        """
        A [file upload](https://docs.stripe.com/api/persons/update#create_file) token representing the front of the verification document. The purpose of the uploaded file should be 'identity_document'. The uploaded file needs to be a color image (smaller than 8,000px by 8,000px), in JPG, PNG, or PDF format, and less than 10 MB in size.
        """

    class UpdateParamsDocumentsVisa(TypedDict):
        files: List[str]
        """
        One or more document IDs returned by a [file upload](https://docs.stripe.com/api/persons/update#create_file) with a purpose value of `account_requirement`.
        """
        type: Literal["files"]
        """
        The format of the document. Currently supports `files` only.
        """

    class UpdateParamsIdNumber(TypedDict):
        type: Literal[
            "ae_eid",
            "br_cpf",
            "de_stn",
            "hk_id",
            "mx_rfc",
            "my_nric",
            "nl_bsn",
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

    class UpdateParamsRelationship(TypedDict):
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

    class UpdateParamsScriptAddresses(TypedDict):
        kana: NotRequired[
            Optional["PersonService.UpdateParamsScriptAddressesKana"]
        ]
        """
        Kana Address.
        """
        kanji: NotRequired[
            Optional["PersonService.UpdateParamsScriptAddressesKanji"]
        ]
        """
        Kanji Address.
        """

    class UpdateParamsScriptAddressesKana(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsScriptAddressesKanji(TypedDict):
        city: NotRequired[Optional[str]]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[
            Optional[
                Literal[
                    "ad",
                    "ae",
                    "af",
                    "ag",
                    "ai",
                    "al",
                    "am",
                    "ao",
                    "aq",
                    "ar",
                    "as",
                    "at",
                    "au",
                    "aw",
                    "ax",
                    "az",
                    "ba",
                    "bb",
                    "bd",
                    "be",
                    "bf",
                    "bg",
                    "bh",
                    "bi",
                    "bj",
                    "bl",
                    "bm",
                    "bn",
                    "bo",
                    "bq",
                    "br",
                    "bs",
                    "bt",
                    "bv",
                    "bw",
                    "by",
                    "bz",
                    "ca",
                    "cc",
                    "cd",
                    "cf",
                    "cg",
                    "ch",
                    "ci",
                    "ck",
                    "cl",
                    "cm",
                    "cn",
                    "co",
                    "cr",
                    "cu",
                    "cv",
                    "cw",
                    "cx",
                    "cy",
                    "cz",
                    "de",
                    "dj",
                    "dk",
                    "dm",
                    "do",
                    "dz",
                    "ec",
                    "ee",
                    "eg",
                    "eh",
                    "er",
                    "es",
                    "et",
                    "fi",
                    "fj",
                    "fk",
                    "fm",
                    "fo",
                    "fr",
                    "ga",
                    "gb",
                    "gd",
                    "ge",
                    "gf",
                    "gg",
                    "gh",
                    "gi",
                    "gl",
                    "gm",
                    "gn",
                    "gp",
                    "gq",
                    "gr",
                    "gs",
                    "gt",
                    "gu",
                    "gw",
                    "gy",
                    "hk",
                    "hm",
                    "hn",
                    "hr",
                    "ht",
                    "hu",
                    "id",
                    "ie",
                    "il",
                    "im",
                    "in",
                    "io",
                    "iq",
                    "ir",
                    "is",
                    "it",
                    "je",
                    "jm",
                    "jo",
                    "jp",
                    "ke",
                    "kg",
                    "kh",
                    "ki",
                    "km",
                    "kn",
                    "kp",
                    "kr",
                    "kw",
                    "ky",
                    "kz",
                    "la",
                    "lb",
                    "lc",
                    "li",
                    "lk",
                    "lr",
                    "ls",
                    "lt",
                    "lu",
                    "lv",
                    "ly",
                    "ma",
                    "mc",
                    "md",
                    "me",
                    "mf",
                    "mg",
                    "mh",
                    "mk",
                    "ml",
                    "mm",
                    "mn",
                    "mo",
                    "mp",
                    "mq",
                    "mr",
                    "ms",
                    "mt",
                    "mu",
                    "mv",
                    "mw",
                    "mx",
                    "my",
                    "mz",
                    "na",
                    "nc",
                    "ne",
                    "nf",
                    "ng",
                    "ni",
                    "nl",
                    "no",
                    "np",
                    "nr",
                    "nu",
                    "nz",
                    "om",
                    "pa",
                    "pe",
                    "pf",
                    "pg",
                    "ph",
                    "pk",
                    "pl",
                    "pm",
                    "pn",
                    "pr",
                    "ps",
                    "pt",
                    "pw",
                    "py",
                    "qa",
                    "qz",
                    "re",
                    "ro",
                    "rs",
                    "ru",
                    "rw",
                    "sa",
                    "sb",
                    "sc",
                    "sd",
                    "se",
                    "sg",
                    "sh",
                    "si",
                    "sj",
                    "sk",
                    "sl",
                    "sm",
                    "sn",
                    "so",
                    "sr",
                    "ss",
                    "st",
                    "sv",
                    "sx",
                    "sy",
                    "sz",
                    "tc",
                    "td",
                    "tf",
                    "tg",
                    "th",
                    "tj",
                    "tk",
                    "tl",
                    "tm",
                    "tn",
                    "to",
                    "tr",
                    "tt",
                    "tv",
                    "tw",
                    "tz",
                    "ua",
                    "ug",
                    "um",
                    "us",
                    "uy",
                    "uz",
                    "va",
                    "vc",
                    "ve",
                    "vg",
                    "vi",
                    "vn",
                    "vu",
                    "wf",
                    "ws",
                    "xx",
                    "ye",
                    "yt",
                    "za",
                    "zm",
                    "zw",
                ]
            ]
        ]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[Optional[str]]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[Optional[str]]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[Optional[str]]
        """
        ZIP or postal code.
        """
        state: NotRequired[Optional[str]]
        """
        State, county, province, or region.
        """
        town: NotRequired[Optional[str]]
        """
        Town or cho-me.
        """

    class UpdateParamsScriptNames(TypedDict):
        kana: NotRequired[
            Optional["PersonService.UpdateParamsScriptNamesKana"]
        ]
        """
        Persons name in kana script.
        """
        kanji: NotRequired[
            Optional["PersonService.UpdateParamsScriptNamesKanji"]
        ]
        """
        Persons name in kanji script.
        """

    class UpdateParamsScriptNamesKana(TypedDict):
        given_name: NotRequired[Optional[str]]
        """
        The person's first or given name.
        """
        surname: NotRequired[Optional[str]]
        """
        The person's last or family name.
        """

    class UpdateParamsScriptNamesKanji(TypedDict):
        given_name: NotRequired[Optional[str]]
        """
        The person's first or given name.
        """
        surname: NotRequired[Optional[str]]
        """
        The person's last or family name.
        """

    def list(
        self,
        account_id: str,
        params: "PersonService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Person]:
        """
        Returns a list of Persons associated with an Account.
        """
        return cast(
            ListObject[Person],
            self._request(
                "get",
                "/v2/core/accounts/{account_id}/persons".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        account_id: str,
        params: "PersonService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Person]:
        """
        Returns a list of Persons associated with an Account.
        """
        return cast(
            ListObject[Person],
            await self._request_async(
                "get",
                "/v2/core/accounts/{account_id}/persons".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        account_id: str,
        params: "PersonService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Create a Person associated with an Account.
        """
        return cast(
            Person,
            self._request(
                "post",
                "/v2/core/accounts/{account_id}/persons".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        account_id: str,
        params: "PersonService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Create a Person associated with an Account.
        """
        return cast(
            Person,
            await self._request_async(
                "post",
                "/v2/core/accounts/{account_id}/persons".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def delete(
        self,
        account_id: str,
        id: str,
        params: "PersonService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Delete a Person associated with an Account.
        """
        return cast(
            Person,
            self._request(
                "delete",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        account_id: str,
        id: str,
        params: "PersonService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Delete a Person associated with an Account.
        """
        return cast(
            Person,
            await self._request_async(
                "delete",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        account_id: str,
        id: str,
        params: "PersonService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Retrieves a Person associated with an Account.
        """
        return cast(
            Person,
            self._request(
                "get",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_id: str,
        id: str,
        params: "PersonService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Retrieves a Person associated with an Account.
        """
        return cast(
            Person,
            await self._request_async(
                "get",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        account_id: str,
        id: str,
        params: "PersonService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Updates a Person associated with an Account.
        """
        return cast(
            Person,
            self._request(
                "post",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        account_id: str,
        id: str,
        params: "PersonService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Person:
        """
        Updates a Person associated with an Account.
        """
        return cast(
            Person,
            await self._request_async(
                "post",
                "/v2/core/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
