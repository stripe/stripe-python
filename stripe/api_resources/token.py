# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

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

    class CreateParams(RequestOptions):
        account: NotRequired[Optional["Token.CreateAccountParams"]]
        bank_account: NotRequired[Optional["Token.CreateBankAccountParams"]]
        card: NotRequired[Optional[Union["Token.CreateCardParams", str]]]
        customer: NotRequired[Optional[str]]
        cvc_update: NotRequired[Optional["Token.CreateCvcUpdateParams"]]
        expand: NotRequired[Optional[List[str]]]
        person: NotRequired[Optional["Token.CreatePersonParams"]]
        pii: NotRequired[Optional["Token.CreatePiiParams"]]

    class CreatePiiParams(TypedDict):
        id_number: NotRequired[Optional[str]]

    class CreatePersonParams(TypedDict):
        address: NotRequired[Optional["Token.CreatePersonAddressParams"]]
        address_kana: NotRequired[
            Optional["Token.CreatePersonAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Token.CreatePersonAddressKanjiParams"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Token.CreatePersonDobParams"]]
        ]
        documents: NotRequired[Optional["Token.CreatePersonDocumentsParams"]]
        email: NotRequired[Optional[str]]
        first_name: NotRequired[Optional[str]]
        first_name_kana: NotRequired[Optional[str]]
        first_name_kanji: NotRequired[Optional[str]]
        full_name_aliases: NotRequired[Optional[Union[Literal[""], List[str]]]]
        gender: NotRequired[Optional[str]]
        id_number: NotRequired[Optional[str]]
        id_number_secondary: NotRequired[Optional[str]]
        last_name: NotRequired[Optional[str]]
        last_name_kana: NotRequired[Optional[str]]
        last_name_kanji: NotRequired[Optional[str]]
        maiden_name: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        nationality: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        political_exposure: NotRequired[Optional[str]]
        registered_address: NotRequired[
            Optional["Token.CreatePersonRegisteredAddressParams"]
        ]
        relationship: NotRequired[
            Optional["Token.CreatePersonRelationshipParams"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Token.CreatePersonVerificationParams"]
        ]

    class CreatePersonVerificationParams(TypedDict):
        additional_document: NotRequired[
            Optional["Token.CreatePersonVerificationAdditionalDocumentParams"]
        ]
        document: NotRequired[
            Optional["Token.CreatePersonVerificationDocumentParams"]
        ]

    class CreatePersonVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreatePersonVerificationAdditionalDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreatePersonRelationshipParams(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        percent_ownership: NotRequired[Optional[Union[Literal[""], float]]]
        representative: NotRequired[Optional[bool]]
        title: NotRequired[Optional[str]]

    class CreatePersonRegisteredAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreatePersonDocumentsParams(TypedDict):
        company_authorization: NotRequired[
            Optional["Token.CreatePersonDocumentsCompanyAuthorizationParams"]
        ]
        passport: NotRequired[
            Optional["Token.CreatePersonDocumentsPassportParams"]
        ]
        visa: NotRequired[Optional["Token.CreatePersonDocumentsVisaParams"]]

    class CreatePersonDocumentsVisaParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonDocumentsPassportParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonDocumentsCompanyAuthorizationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreatePersonAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreatePersonAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreatePersonAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateCvcUpdateParams(TypedDict):
        cvc: str

    class CreateCardParams(TypedDict):
        address_city: NotRequired[Optional[str]]
        address_country: NotRequired[Optional[str]]
        address_line1: NotRequired[Optional[str]]
        address_line2: NotRequired[Optional[str]]
        address_state: NotRequired[Optional[str]]
        address_zip: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        cvc: NotRequired[Optional[str]]
        exp_month: str
        exp_year: str
        name: NotRequired[Optional[str]]
        number: str

    class CreateBankAccountParams(TypedDict):
        account_holder_name: NotRequired[Optional[str]]
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: str
        account_type: NotRequired[
            Optional[Literal["checking", "futsu", "savings", "toza"]]
        ]
        country: str
        currency: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreateAccountParams(TypedDict):
        business_type: NotRequired[
            Optional[
                Literal[
                    "company", "government_entity", "individual", "non_profit"
                ]
            ]
        ]
        company: NotRequired[Optional["Token.CreateAccountCompanyParams"]]
        individual: NotRequired[
            Optional["Token.CreateAccountIndividualParams"]
        ]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class CreateAccountIndividualParams(TypedDict):
        address: NotRequired[
            Optional["Token.CreateAccountIndividualAddressParams"]
        ]
        address_kana: NotRequired[
            Optional["Token.CreateAccountIndividualAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Token.CreateAccountIndividualAddressKanjiParams"]
        ]
        dob: NotRequired[
            Optional[
                Union[Literal[""], "Token.CreateAccountIndividualDobParams"]
            ]
        ]
        email: NotRequired[Optional[str]]
        first_name: NotRequired[Optional[str]]
        first_name_kana: NotRequired[Optional[str]]
        first_name_kanji: NotRequired[Optional[str]]
        full_name_aliases: NotRequired[Optional[Union[Literal[""], List[str]]]]
        gender: NotRequired[Optional[str]]
        id_number: NotRequired[Optional[str]]
        id_number_secondary: NotRequired[Optional[str]]
        last_name: NotRequired[Optional[str]]
        last_name_kana: NotRequired[Optional[str]]
        last_name_kanji: NotRequired[Optional[str]]
        maiden_name: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        phone: NotRequired[Optional[str]]
        political_exposure: NotRequired[Optional[Literal["existing", "none"]]]
        registered_address: NotRequired[
            Optional["Token.CreateAccountIndividualRegisteredAddressParams"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Token.CreateAccountIndividualVerificationParams"]
        ]

    class CreateAccountIndividualVerificationParams(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Token.CreateAccountIndividualVerificationAdditionalDocumentParams"
            ]
        ]
        document: NotRequired[
            Optional["Token.CreateAccountIndividualVerificationDocumentParams"]
        ]

    class CreateAccountIndividualVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateAccountIndividualVerificationAdditionalDocumentParams(
        TypedDict,
    ):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateAccountIndividualRegisteredAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateAccountIndividualDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreateAccountIndividualAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateAccountIndividualAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateAccountIndividualAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateAccountCompanyParams(TypedDict):
        address: NotRequired[
            Optional["Token.CreateAccountCompanyAddressParams"]
        ]
        address_kana: NotRequired[
            Optional["Token.CreateAccountCompanyAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Token.CreateAccountCompanyAddressKanjiParams"]
        ]
        directors_provided: NotRequired[Optional[bool]]
        executives_provided: NotRequired[Optional[bool]]
        export_license_id: NotRequired[Optional[str]]
        export_purpose_code: NotRequired[Optional[str]]
        name: NotRequired[Optional[str]]
        name_kana: NotRequired[Optional[str]]
        name_kanji: NotRequired[Optional[str]]
        owners_provided: NotRequired[Optional[bool]]
        ownership_declaration: NotRequired[
            Optional["Token.CreateAccountCompanyOwnershipDeclarationParams"]
        ]
        ownership_declaration_shown_and_signed: NotRequired[Optional[bool]]
        phone: NotRequired[Optional[str]]
        registration_number: NotRequired[Optional[str]]
        structure: NotRequired[
            Optional[
                Union[
                    Literal[""],
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
                    ],
                ]
            ]
        ]
        tax_id: NotRequired[Optional[str]]
        tax_id_registrar: NotRequired[Optional[str]]
        vat_id: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Token.CreateAccountCompanyVerificationParams"]
        ]

    class CreateAccountCompanyVerificationParams(TypedDict):
        document: NotRequired[
            Optional["Token.CreateAccountCompanyVerificationDocumentParams"]
        ]

    class CreateAccountCompanyVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateAccountCompanyOwnershipDeclarationParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateAccountCompanyAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateAccountCompanyAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateAccountCompanyAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
