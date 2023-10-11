# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_resources, oauth, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
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

    class CreateParams(RequestOptions):
        account_token: NotRequired[Optional[str]]
        business_profile: NotRequired[
            Optional["Account.CreateBusinessProfileParams"]
        ]
        business_type: NotRequired[
            Optional[
                Literal[
                    "company", "government_entity", "individual", "non_profit"
                ]
            ]
        ]
        capabilities: NotRequired[Optional["Account.CreateCapabilitiesParams"]]
        company: NotRequired[Optional["Account.CreateCompanyParams"]]
        country: NotRequired[Optional[str]]
        default_currency: NotRequired[Optional[str]]
        documents: NotRequired[Optional["Account.CreateDocumentsParams"]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        external_account: NotRequired[Optional[str]]
        individual: NotRequired[Optional["Account.CreateIndividualParams"]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        settings: NotRequired[Optional["Account.CreateSettingsParams"]]
        tos_acceptance: NotRequired[
            Optional["Account.CreateTosAcceptanceParams"]
        ]
        type: NotRequired[Optional[Literal["custom", "express", "standard"]]]

    class CreateTosAcceptanceParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        service_agreement: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateSettingsParams(TypedDict):
        branding: NotRequired[Optional["Account.CreateSettingsBrandingParams"]]
        card_issuing: NotRequired[
            Optional["Account.CreateSettingsCardIssuingParams"]
        ]
        card_payments: NotRequired[
            Optional["Account.CreateSettingsCardPaymentsParams"]
        ]
        payments: NotRequired[Optional["Account.CreateSettingsPaymentsParams"]]
        payouts: NotRequired[Optional["Account.CreateSettingsPayoutsParams"]]
        treasury: NotRequired[Optional["Account.CreateSettingsTreasuryParams"]]

    class CreateSettingsTreasuryParams(TypedDict):
        tos_acceptance: NotRequired[
            Optional["Account.CreateSettingsTreasuryTosAcceptanceParams"]
        ]

    class CreateSettingsTreasuryTosAcceptanceParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateSettingsPayoutsParams(TypedDict):
        debit_negative_balances: NotRequired[Optional[bool]]
        schedule: NotRequired[
            Optional["Account.CreateSettingsPayoutsScheduleParams"]
        ]
        statement_descriptor: NotRequired[Optional[str]]

    class CreateSettingsPayoutsScheduleParams(TypedDict):
        delay_days: NotRequired[Optional[Union[Literal["minimum"], int]]]
        interval: NotRequired[
            Optional[Literal["daily", "manual", "monthly", "weekly"]]
        ]
        monthly_anchor: NotRequired[Optional[int]]
        weekly_anchor: NotRequired[
            Optional[
                Literal[
                    "friday",
                    "monday",
                    "saturday",
                    "sunday",
                    "thursday",
                    "tuesday",
                    "wednesday",
                ]
            ]
        ]

    class CreateSettingsPaymentsParams(TypedDict):
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_kana: NotRequired[Optional[str]]
        statement_descriptor_kanji: NotRequired[Optional[str]]

    class CreateSettingsCardPaymentsParams(TypedDict):
        decline_on: NotRequired[
            Optional["Account.CreateSettingsCardPaymentsDeclineOnParams"]
        ]
        statement_descriptor_prefix: NotRequired[Optional[str]]
        statement_descriptor_prefix_kana: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        statement_descriptor_prefix_kanji: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class CreateSettingsCardPaymentsDeclineOnParams(TypedDict):
        avs_failure: NotRequired[Optional[bool]]
        cvc_failure: NotRequired[Optional[bool]]

    class CreateSettingsCardIssuingParams(TypedDict):
        tos_acceptance: NotRequired[
            Optional["Account.CreateSettingsCardIssuingTosAcceptanceParams"]
        ]

    class CreateSettingsCardIssuingTosAcceptanceParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateSettingsBrandingParams(TypedDict):
        icon: NotRequired[Optional[str]]
        logo: NotRequired[Optional[str]]
        primary_color: NotRequired[Optional[str]]
        secondary_color: NotRequired[Optional[str]]

    class CreateIndividualParams(TypedDict):
        address: NotRequired[Optional["Account.CreateIndividualAddressParams"]]
        address_kana: NotRequired[
            Optional["Account.CreateIndividualAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreateIndividualAddressKanjiParams"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.CreateIndividualDobParams"]]
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
            Optional["Account.CreateIndividualRegisteredAddressParams"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.CreateIndividualVerificationParams"]
        ]

    class CreateIndividualVerificationParams(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.CreateIndividualVerificationAdditionalDocumentParams"
            ]
        ]
        document: NotRequired[
            Optional["Account.CreateIndividualVerificationDocumentParams"]
        ]

    class CreateIndividualVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateIndividualVerificationAdditionalDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateIndividualRegisteredAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateIndividualDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreateIndividualAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateIndividualAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateIndividualAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateDocumentsParams(TypedDict):
        bank_account_ownership_verification: NotRequired[
            Optional[
                "Account.CreateDocumentsBankAccountOwnershipVerificationParams"
            ]
        ]
        company_license: NotRequired[
            Optional["Account.CreateDocumentsCompanyLicenseParams"]
        ]
        company_memorandum_of_association: NotRequired[
            Optional[
                "Account.CreateDocumentsCompanyMemorandumOfAssociationParams"
            ]
        ]
        company_ministerial_decree: NotRequired[
            Optional["Account.CreateDocumentsCompanyMinisterialDecreeParams"]
        ]
        company_registration_verification: NotRequired[
            Optional[
                "Account.CreateDocumentsCompanyRegistrationVerificationParams"
            ]
        ]
        company_tax_id_verification: NotRequired[
            Optional["Account.CreateDocumentsCompanyTaxIdVerificationParams"]
        ]
        proof_of_registration: NotRequired[
            Optional["Account.CreateDocumentsProofOfRegistrationParams"]
        ]

    class CreateDocumentsProofOfRegistrationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsCompanyTaxIdVerificationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsCompanyRegistrationVerificationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsCompanyMinisterialDecreeParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsCompanyMemorandumOfAssociationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsCompanyLicenseParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateDocumentsBankAccountOwnershipVerificationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateCompanyParams(TypedDict):
        address: NotRequired[Optional["Account.CreateCompanyAddressParams"]]
        address_kana: NotRequired[
            Optional["Account.CreateCompanyAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreateCompanyAddressKanjiParams"]
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
            Optional["Account.CreateCompanyOwnershipDeclarationParams"]
        ]
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
            Optional["Account.CreateCompanyVerificationParams"]
        ]

    class CreateCompanyVerificationParams(TypedDict):
        document: NotRequired[
            Optional["Account.CreateCompanyVerificationDocumentParams"]
        ]

    class CreateCompanyVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateCompanyOwnershipDeclarationParams(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateCompanyAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateCompanyAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateCompanyAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateCapabilitiesParams(TypedDict):
        acss_debit_payments: NotRequired[
            Optional["Account.CreateCapabilitiesAcssDebitPaymentsParams"]
        ]
        affirm_payments: NotRequired[
            Optional["Account.CreateCapabilitiesAffirmPaymentsParams"]
        ]
        afterpay_clearpay_payments: NotRequired[
            Optional[
                "Account.CreateCapabilitiesAfterpayClearpayPaymentsParams"
            ]
        ]
        au_becs_debit_payments: NotRequired[
            Optional["Account.CreateCapabilitiesAuBecsDebitPaymentsParams"]
        ]
        bacs_debit_payments: NotRequired[
            Optional["Account.CreateCapabilitiesBacsDebitPaymentsParams"]
        ]
        bancontact_payments: NotRequired[
            Optional["Account.CreateCapabilitiesBancontactPaymentsParams"]
        ]
        bank_transfer_payments: NotRequired[
            Optional["Account.CreateCapabilitiesBankTransferPaymentsParams"]
        ]
        blik_payments: NotRequired[
            Optional["Account.CreateCapabilitiesBlikPaymentsParams"]
        ]
        boleto_payments: NotRequired[
            Optional["Account.CreateCapabilitiesBoletoPaymentsParams"]
        ]
        card_issuing: NotRequired[
            Optional["Account.CreateCapabilitiesCardIssuingParams"]
        ]
        card_payments: NotRequired[
            Optional["Account.CreateCapabilitiesCardPaymentsParams"]
        ]
        cartes_bancaires_payments: NotRequired[
            Optional["Account.CreateCapabilitiesCartesBancairesPaymentsParams"]
        ]
        cashapp_payments: NotRequired[
            Optional["Account.CreateCapabilitiesCashappPaymentsParams"]
        ]
        eps_payments: NotRequired[
            Optional["Account.CreateCapabilitiesEpsPaymentsParams"]
        ]
        fpx_payments: NotRequired[
            Optional["Account.CreateCapabilitiesFpxPaymentsParams"]
        ]
        giropay_payments: NotRequired[
            Optional["Account.CreateCapabilitiesGiropayPaymentsParams"]
        ]
        grabpay_payments: NotRequired[
            Optional["Account.CreateCapabilitiesGrabpayPaymentsParams"]
        ]
        ideal_payments: NotRequired[
            Optional["Account.CreateCapabilitiesIdealPaymentsParams"]
        ]
        india_international_payments: NotRequired[
            Optional[
                "Account.CreateCapabilitiesIndiaInternationalPaymentsParams"
            ]
        ]
        jcb_payments: NotRequired[
            Optional["Account.CreateCapabilitiesJcbPaymentsParams"]
        ]
        klarna_payments: NotRequired[
            Optional["Account.CreateCapabilitiesKlarnaPaymentsParams"]
        ]
        konbini_payments: NotRequired[
            Optional["Account.CreateCapabilitiesKonbiniPaymentsParams"]
        ]
        legacy_payments: NotRequired[
            Optional["Account.CreateCapabilitiesLegacyPaymentsParams"]
        ]
        link_payments: NotRequired[
            Optional["Account.CreateCapabilitiesLinkPaymentsParams"]
        ]
        oxxo_payments: NotRequired[
            Optional["Account.CreateCapabilitiesOxxoPaymentsParams"]
        ]
        p24_payments: NotRequired[
            Optional["Account.CreateCapabilitiesP24PaymentsParams"]
        ]
        paynow_payments: NotRequired[
            Optional["Account.CreateCapabilitiesPaynowPaymentsParams"]
        ]
        promptpay_payments: NotRequired[
            Optional["Account.CreateCapabilitiesPromptpayPaymentsParams"]
        ]
        sepa_debit_payments: NotRequired[
            Optional["Account.CreateCapabilitiesSepaDebitPaymentsParams"]
        ]
        sofort_payments: NotRequired[
            Optional["Account.CreateCapabilitiesSofortPaymentsParams"]
        ]
        tax_reporting_us_1099_k: NotRequired[
            Optional["Account.CreateCapabilitiesTaxReportingUs1099KParams"]
        ]
        tax_reporting_us_1099_misc: NotRequired[
            Optional["Account.CreateCapabilitiesTaxReportingUs1099MiscParams"]
        ]
        transfers: NotRequired[
            Optional["Account.CreateCapabilitiesTransfersParams"]
        ]
        treasury: NotRequired[
            Optional["Account.CreateCapabilitiesTreasuryParams"]
        ]
        us_bank_account_ach_payments: NotRequired[
            Optional[
                "Account.CreateCapabilitiesUsBankAccountAchPaymentsParams"
            ]
        ]
        zip_payments: NotRequired[
            Optional["Account.CreateCapabilitiesZipPaymentsParams"]
        ]

    class CreateCapabilitiesZipPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesUsBankAccountAchPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesTreasuryParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesTransfersParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesTaxReportingUs1099MiscParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesTaxReportingUs1099KParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesSofortPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesSepaDebitPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesPromptpayPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesPaynowPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesP24PaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesOxxoPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesLinkPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesLegacyPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesKonbiniPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesKlarnaPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesJcbPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesIndiaInternationalPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesIdealPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesGrabpayPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesGiropayPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesFpxPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesEpsPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesCashappPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesCartesBancairesPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesCardPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesCardIssuingParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesBoletoPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesBlikPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesBankTransferPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesBancontactPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesBacsDebitPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesAuBecsDebitPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesAfterpayClearpayPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesAffirmPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateCapabilitiesAcssDebitPaymentsParams(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateBusinessProfileParams(TypedDict):
        mcc: NotRequired[Optional[str]]
        monthly_estimated_revenue: NotRequired[
            Optional[
                "Account.CreateBusinessProfileMonthlyEstimatedRevenueParams"
            ]
        ]
        name: NotRequired[Optional[str]]
        product_description: NotRequired[Optional[str]]
        support_address: NotRequired[
            Optional["Account.CreateBusinessProfileSupportAddressParams"]
        ]
        support_email: NotRequired[Optional[str]]
        support_phone: NotRequired[Optional[str]]
        support_url: NotRequired[Optional[Union[Literal[""], str]]]
        url: NotRequired[Optional[str]]

    class CreateBusinessProfileSupportAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateBusinessProfileMonthlyEstimatedRevenueParams(TypedDict):
        amount: int
        currency: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        created: NotRequired[Optional[Union["Account.ListCreatedParams", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class PersonsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        relationship: NotRequired[
            Optional["Account.PersonsRelationshipParams"]
        ]
        starting_after: NotRequired[Optional[str]]

    class PersonsRelationshipParams(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        representative: NotRequired[Optional[bool]]

    class RejectParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        reason: str

    class RetrieveCapabilityParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyCapabilityParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        requested: NotRequired[Optional[bool]]

    class ListCapabilitiesParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateExternalAccountParams(RequestOptions):
        default_for_currency: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        external_account: str
        metadata: NotRequired[Optional[Dict[str, str]]]

    class RetrieveExternalAccountParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyExternalAccountParams(RequestOptions):
        account_holder_name: NotRequired[Optional[str]]
        account_holder_type: NotRequired[
            Optional[Union[Literal[""], Literal["company", "individual"]]]
        ]
        account_type: NotRequired[
            Optional[Literal["checking", "futsu", "savings", "toza"]]
        ]
        address_city: NotRequired[Optional[str]]
        address_country: NotRequired[Optional[str]]
        address_line1: NotRequired[Optional[str]]
        address_line2: NotRequired[Optional[str]]
        address_state: NotRequired[Optional[str]]
        address_zip: NotRequired[Optional[str]]
        default_for_currency: NotRequired[Optional[bool]]
        documents: NotRequired[
            Optional["Account.ModifyExternalAccountDocumentsParams"]
        ]
        exp_month: NotRequired[Optional[str]]
        exp_year: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]

    class ModifyExternalAccountDocumentsParams(TypedDict):
        bank_account_ownership_verification: NotRequired[
            Optional[
                "Account.ModifyExternalAccountDocumentsBankAccountOwnershipVerificationParams"
            ]
        ]

    class ModifyExternalAccountDocumentsBankAccountOwnershipVerificationParams(
        TypedDict,
    ):
        files: NotRequired[Optional[List[str]]]

    class DeleteExternalAccountParams(RequestOptions):
        pass

    class ListExternalAccountsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        object: NotRequired[Optional[Literal["bank_account", "card"]]]
        starting_after: NotRequired[Optional[str]]

    class CreateLoginLinkParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreatePersonParams(RequestOptions):
        address: NotRequired[Optional["Account.CreatePersonAddressParams"]]
        address_kana: NotRequired[
            Optional["Account.CreatePersonAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreatePersonAddressKanjiParams"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.CreatePersonDobParams"]]
        ]
        documents: NotRequired[Optional["Account.CreatePersonDocumentsParams"]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
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
        person_token: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        political_exposure: NotRequired[Optional[str]]
        registered_address: NotRequired[
            Optional["Account.CreatePersonRegisteredAddressParams"]
        ]
        relationship: NotRequired[
            Optional["Account.CreatePersonRelationshipParams"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.CreatePersonVerificationParams"]
        ]

    class CreatePersonVerificationParams(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.CreatePersonVerificationAdditionalDocumentParams"
            ]
        ]
        document: NotRequired[
            Optional["Account.CreatePersonVerificationDocumentParams"]
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
            Optional["Account.CreatePersonDocumentsCompanyAuthorizationParams"]
        ]
        passport: NotRequired[
            Optional["Account.CreatePersonDocumentsPassportParams"]
        ]
        visa: NotRequired[Optional["Account.CreatePersonDocumentsVisaParams"]]

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

    class RetrievePersonParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyPersonParams(RequestOptions):
        address: NotRequired[Optional["Account.ModifyPersonAddressParams"]]
        address_kana: NotRequired[
            Optional["Account.ModifyPersonAddressKanaParams"]
        ]
        address_kanji: NotRequired[
            Optional["Account.ModifyPersonAddressKanjiParams"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.ModifyPersonDobParams"]]
        ]
        documents: NotRequired[Optional["Account.ModifyPersonDocumentsParams"]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
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
        person_token: NotRequired[Optional[str]]
        phone: NotRequired[Optional[str]]
        political_exposure: NotRequired[Optional[str]]
        registered_address: NotRequired[
            Optional["Account.ModifyPersonRegisteredAddressParams"]
        ]
        relationship: NotRequired[
            Optional["Account.ModifyPersonRelationshipParams"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.ModifyPersonVerificationParams"]
        ]

    class ModifyPersonVerificationParams(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.ModifyPersonVerificationAdditionalDocumentParams"
            ]
        ]
        document: NotRequired[
            Optional["Account.ModifyPersonVerificationDocumentParams"]
        ]

    class ModifyPersonVerificationDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class ModifyPersonVerificationAdditionalDocumentParams(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class ModifyPersonRelationshipParams(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        percent_ownership: NotRequired[Optional[Union[Literal[""], float]]]
        representative: NotRequired[Optional[bool]]
        title: NotRequired[Optional[str]]

    class ModifyPersonRegisteredAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyPersonDocumentsParams(TypedDict):
        company_authorization: NotRequired[
            Optional["Account.ModifyPersonDocumentsCompanyAuthorizationParams"]
        ]
        passport: NotRequired[
            Optional["Account.ModifyPersonDocumentsPassportParams"]
        ]
        visa: NotRequired[Optional["Account.ModifyPersonDocumentsVisaParams"]]

    class ModifyPersonDocumentsVisaParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonDocumentsPassportParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonDocumentsCompanyAuthorizationParams(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonDobParams(TypedDict):
        day: int
        month: int
        year: int

    class ModifyPersonAddressKanjiParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class ModifyPersonAddressKanaParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class ModifyPersonAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class DeletePersonParams(RequestOptions):
        pass

    class ListPersonsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        relationship: NotRequired[
            Optional["Account.ListPersonsRelationshipParams"]
        ]
        starting_after: NotRequired[Optional[str]]

    class ListPersonsRelationshipParams(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        representative: NotRequired[Optional[bool]]

    business_profile: Optional[StripeObject]
    business_type: Optional[
        Literal["company", "government_entity", "individual", "non_profit"]
    ]
    capabilities: Optional[StripeObject]
    charges_enabled: Optional[bool]
    company: Optional[StripeObject]
    controller: Optional[StripeObject]
    country: Optional[str]
    created: Optional[int]
    default_currency: Optional[str]
    details_submitted: Optional[bool]
    email: Optional[str]
    external_accounts: Optional[ListObject[Any]]
    future_requirements: Optional[StripeObject]
    id: str
    individual: Optional["Person"]
    metadata: Optional[Dict[str, str]]
    object: Literal["account"]
    payouts_enabled: Optional[bool]
    requirements: Optional[StripeObject]
    settings: Optional[StripeObject]
    tos_acceptance: Optional[StripeObject]
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
