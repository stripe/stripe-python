# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card


class Token(CreateableAPIResource["Token"]):
    """
    Tokenization is the process Stripe uses to collect sensitive card or bank
    account details, or personally identifiable information (PII), directly from
    your customers in a secure manner. A token representing this information is
    returned to your server to use. Use our
    [recommended payments integrations](https://stripe.com/docs/payments) to perform this process
    on the client-side. This guarantees that no sensitive card data touches your server,
    and allows your integration to operate in a PCI-compliant way.

    If you can't use client-side tokenization, you can also create tokens using
    the API with either your publishable or secret API key. If
    your integration uses this method, you're responsible for any PCI compliance
    that it might require, and you must keep your secret API key safe. Unlike with
    client-side tokenization, your customer's information isn't sent directly to
    Stripe, so we can't determine how it's handled or stored.

    You can't store or use tokens more than once. To store card or bank account
    information for later use, create [Customer](https://stripe.com/docs/api#customers)
    objects or [Custom accounts](https://stripe.com/docs/api#external_accounts).
    [Radar](https://stripe.com/docs/radar), our integrated solution for automatic fraud protection,
    performs best with integrations that use client-side tokenization.
    """

    OBJECT_NAME = "token"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account: NotRequired["Token.CreateParamsAccount|None"]
            bank_account: NotRequired["Token.CreateParamsBankAccount|None"]
            card: NotRequired["Token.CreateParamsCard|str|None"]
            customer: NotRequired["str|None"]
            cvc_update: NotRequired["Token.CreateParamsCvcUpdate|None"]
            expand: NotRequired["List[str]|None"]
            person: NotRequired["Token.CreateParamsPerson|None"]
            pii: NotRequired["Token.CreateParamsPii|None"]

        class CreateParamsPii(TypedDict):
            id_number: NotRequired["str|None"]

        class CreateParamsPerson(TypedDict):
            additional_tos_acceptances: NotRequired[
                "Token.CreateParamsPersonAdditionalTosAcceptances|None"
            ]
            address: NotRequired["Token.CreateParamsPersonAddress|None"]
            address_kana: NotRequired[
                "Token.CreateParamsPersonAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Token.CreateParamsPersonAddressKanji|None"
            ]
            dob: NotRequired["Literal['']|Token.CreateParamsPersonDob|None"]
            documents: NotRequired["Token.CreateParamsPersonDocuments|None"]
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
            nationality: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            political_exposure: NotRequired["str|None"]
            registered_address: NotRequired[
                "Token.CreateParamsPersonRegisteredAddress|None"
            ]
            relationship: NotRequired[
                "Token.CreateParamsPersonRelationship|None"
            ]
            ssn_last_4: NotRequired["str|None"]
            verification: NotRequired[
                "Token.CreateParamsPersonVerification|None"
            ]

        class CreateParamsPersonVerification(TypedDict):
            additional_document: NotRequired[
                "Token.CreateParamsPersonVerificationAdditionalDocument|None"
            ]
            document: NotRequired[
                "Token.CreateParamsPersonVerificationDocument|None"
            ]

        class CreateParamsPersonVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsPersonVerificationAdditionalDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsPersonRelationship(TypedDict):
            director: NotRequired["bool|None"]
            executive: NotRequired["bool|None"]
            legal_guardian: NotRequired["bool|None"]
            owner: NotRequired["bool|None"]
            percent_ownership: NotRequired["Literal['']|float|None"]
            representative: NotRequired["bool|None"]
            title: NotRequired["str|None"]

        class CreateParamsPersonRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsPersonDocuments(TypedDict):
            company_authorization: NotRequired[
                "Token.CreateParamsPersonDocumentsCompanyAuthorization|None"
            ]
            passport: NotRequired[
                "Token.CreateParamsPersonDocumentsPassport|None"
            ]
            visa: NotRequired["Token.CreateParamsPersonDocumentsVisa|None"]

        class CreateParamsPersonDocumentsVisa(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsPersonDocumentsPassport(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsPersonDocumentsCompanyAuthorization(TypedDict):
            files: NotRequired["List[str]|None"]

        class CreateParamsPersonDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsPersonAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsPersonAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsPersonAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsPersonAdditionalTosAcceptances(TypedDict):
            account: NotRequired[
                "Token.CreateParamsPersonAdditionalTosAcceptancesAccount|None"
            ]

        class CreateParamsPersonAdditionalTosAcceptancesAccount(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["Literal['']|str|None"]

        class CreateParamsCvcUpdate(TypedDict):
            cvc: str

        class CreateParamsCard(TypedDict):
            address_city: NotRequired["str|None"]
            address_country: NotRequired["str|None"]
            address_line1: NotRequired["str|None"]
            address_line2: NotRequired["str|None"]
            address_state: NotRequired["str|None"]
            address_zip: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            cvc: NotRequired["str|None"]
            exp_month: str
            exp_year: str
            name: NotRequired["str|None"]
            number: str

        class CreateParamsBankAccount(TypedDict):
            account_holder_name: NotRequired["str|None"]
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: str
            account_type: NotRequired[
                "Literal['checking', 'futsu', 'savings', 'toza']|None"
            ]
            country: str
            currency: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class CreateParamsAccount(TypedDict):
            business_type: NotRequired[
                "Literal['company', 'government_entity', 'individual', 'non_profit']|None"
            ]
            company: NotRequired["Token.CreateParamsAccountCompany|None"]
            individual: NotRequired["Token.CreateParamsAccountIndividual|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class CreateParamsAccountIndividual(TypedDict):
            address: NotRequired[
                "Token.CreateParamsAccountIndividualAddress|None"
            ]
            address_kana: NotRequired[
                "Token.CreateParamsAccountIndividualAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Token.CreateParamsAccountIndividualAddressKanji|None"
            ]
            dob: NotRequired[
                "Literal['']|Token.CreateParamsAccountIndividualDob|None"
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
                "Token.CreateParamsAccountIndividualRegisteredAddress|None"
            ]
            ssn_last_4: NotRequired["str|None"]
            verification: NotRequired[
                "Token.CreateParamsAccountIndividualVerification|None"
            ]

        class CreateParamsAccountIndividualVerification(TypedDict):
            additional_document: NotRequired[
                "Token.CreateParamsAccountIndividualVerificationAdditionalDocument|None"
            ]
            document: NotRequired[
                "Token.CreateParamsAccountIndividualVerificationDocument|None"
            ]

        class CreateParamsAccountIndividualVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsAccountIndividualVerificationAdditionalDocument(
            TypedDict,
        ):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsAccountIndividualRegisteredAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsAccountIndividualDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsAccountIndividualAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsAccountIndividualAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsAccountIndividualAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsAccountCompany(TypedDict):
            address: NotRequired[
                "Token.CreateParamsAccountCompanyAddress|None"
            ]
            address_kana: NotRequired[
                "Token.CreateParamsAccountCompanyAddressKana|None"
            ]
            address_kanji: NotRequired[
                "Token.CreateParamsAccountCompanyAddressKanji|None"
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
                "Token.CreateParamsAccountCompanyOwnershipDeclaration|None"
            ]
            ownership_declaration_shown_and_signed: NotRequired["bool|None"]
            phone: NotRequired["str|None"]
            registration_number: NotRequired["str|None"]
            structure: NotRequired[
                "Literal['']|Literal['free_zone_establishment', 'free_zone_llc', 'government_instrumentality', 'governmental_unit', 'incorporated_non_profit', 'incorporated_partnership', 'limited_liability_partnership', 'llc', 'multi_member_llc', 'private_company', 'private_corporation', 'private_partnership', 'public_company', 'public_corporation', 'public_partnership', 'single_member_llc', 'sole_establishment', 'sole_proprietorship', 'tax_exempt_government_instrumentality', 'unincorporated_association', 'unincorporated_non_profit', 'unincorporated_partnership']|None"
            ]
            tax_id: NotRequired["str|None"]
            tax_id_registrar: NotRequired["str|None"]
            vat_id: NotRequired["str|None"]
            verification: NotRequired[
                "Token.CreateParamsAccountCompanyVerification|None"
            ]

        class CreateParamsAccountCompanyVerification(TypedDict):
            document: NotRequired[
                "Token.CreateParamsAccountCompanyVerificationDocument|None"
            ]

        class CreateParamsAccountCompanyVerificationDocument(TypedDict):
            back: NotRequired["str|None"]
            front: NotRequired["str|None"]

        class CreateParamsAccountCompanyOwnershipDeclaration(TypedDict):
            date: NotRequired["int|None"]
            ip: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class CreateParamsAccountCompanyAddressKanji(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsAccountCompanyAddressKana(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]
            town: NotRequired["str|None"]

        class CreateParamsAccountCompanyAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    bank_account: Optional["BankAccount"]
    card: Optional["Card"]
    client_ip: Optional[str]
    created: int
    id: str
    livemode: bool
    object: Literal["token"]
    type: str
    used: bool

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Token.CreateParams"]
    ) -> "Token":
        return cast(
            "Token",
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
    def retrieve(
        cls, id: str, **params: Unpack["Token.RetrieveParams"]
    ) -> "Token":
        instance = cls(id, **params)
        instance.refresh()
        return instance
