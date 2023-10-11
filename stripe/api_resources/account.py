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
            Optional["Account.CreateParamsBusinessProfile"]
        ]
        business_type: NotRequired[
            Optional[
                Literal[
                    "company", "government_entity", "individual", "non_profit"
                ]
            ]
        ]
        capabilities: NotRequired[Optional["Account.CreateParamsCapabilities"]]
        company: NotRequired[Optional["Account.CreateParamsCompany"]]
        country: NotRequired[Optional[str]]
        default_currency: NotRequired[Optional[str]]
        documents: NotRequired[Optional["Account.CreateParamsDocuments"]]
        email: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        external_account: NotRequired[Optional[str]]
        individual: NotRequired[Optional["Account.CreateParamsIndividual"]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        settings: NotRequired[Optional["Account.CreateParamsSettings"]]
        tos_acceptance: NotRequired[
            Optional["Account.CreateParamsTosAcceptance"]
        ]
        type: NotRequired[Optional[Literal["custom", "express", "standard"]]]

    class CreateParamsTosAcceptance(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        service_agreement: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParamsSettings(TypedDict):
        branding: NotRequired[Optional["Account.CreateParamsSettingsBranding"]]
        card_issuing: NotRequired[
            Optional["Account.CreateParamsSettingsCardIssuing"]
        ]
        card_payments: NotRequired[
            Optional["Account.CreateParamsSettingsCardPayments"]
        ]
        payments: NotRequired[Optional["Account.CreateParamsSettingsPayments"]]
        payouts: NotRequired[Optional["Account.CreateParamsSettingsPayouts"]]
        treasury: NotRequired[Optional["Account.CreateParamsSettingsTreasury"]]

    class CreateParamsSettingsTreasury(TypedDict):
        tos_acceptance: NotRequired[
            Optional["Account.CreateParamsSettingsTreasuryTosAcceptance"]
        ]

    class CreateParamsSettingsTreasuryTosAcceptance(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsSettingsPayouts(TypedDict):
        debit_negative_balances: NotRequired[Optional[bool]]
        schedule: NotRequired[
            Optional["Account.CreateParamsSettingsPayoutsSchedule"]
        ]
        statement_descriptor: NotRequired[Optional[str]]

    class CreateParamsSettingsPayoutsSchedule(TypedDict):
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

    class CreateParamsSettingsPayments(TypedDict):
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_kana: NotRequired[Optional[str]]
        statement_descriptor_kanji: NotRequired[Optional[str]]

    class CreateParamsSettingsCardPayments(TypedDict):
        decline_on: NotRequired[
            Optional["Account.CreateParamsSettingsCardPaymentsDeclineOn"]
        ]
        statement_descriptor_prefix: NotRequired[Optional[str]]
        statement_descriptor_prefix_kana: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        statement_descriptor_prefix_kanji: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class CreateParamsSettingsCardPaymentsDeclineOn(TypedDict):
        avs_failure: NotRequired[Optional[bool]]
        cvc_failure: NotRequired[Optional[bool]]

    class CreateParamsSettingsCardIssuing(TypedDict):
        tos_acceptance: NotRequired[
            Optional["Account.CreateParamsSettingsCardIssuingTosAcceptance"]
        ]

    class CreateParamsSettingsCardIssuingTosAcceptance(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsSettingsBranding(TypedDict):
        icon: NotRequired[Optional[str]]
        logo: NotRequired[Optional[str]]
        primary_color: NotRequired[Optional[str]]
        secondary_color: NotRequired[Optional[str]]

    class CreateParamsIndividual(TypedDict):
        address: NotRequired[Optional["Account.CreateParamsIndividualAddress"]]
        address_kana: NotRequired[
            Optional["Account.CreateParamsIndividualAddressKana"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreateParamsIndividualAddressKanji"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.CreateParamsIndividualDob"]]
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
            Optional["Account.CreateParamsIndividualRegisteredAddress"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.CreateParamsIndividualVerification"]
        ]

    class CreateParamsIndividualVerification(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.CreateParamsIndividualVerificationAdditionalDocument"
            ]
        ]
        document: NotRequired[
            Optional["Account.CreateParamsIndividualVerificationDocument"]
        ]

    class CreateParamsIndividualVerificationDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateParamsIndividualVerificationAdditionalDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateParamsIndividualRegisteredAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsIndividualDob(TypedDict):
        day: int
        month: int
        year: int

    class CreateParamsIndividualAddressKanji(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateParamsIndividualAddressKana(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateParamsIndividualAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsDocuments(TypedDict):
        bank_account_ownership_verification: NotRequired[
            Optional[
                "Account.CreateParamsDocumentsBankAccountOwnershipVerification"
            ]
        ]
        company_license: NotRequired[
            Optional["Account.CreateParamsDocumentsCompanyLicense"]
        ]
        company_memorandum_of_association: NotRequired[
            Optional[
                "Account.CreateParamsDocumentsCompanyMemorandumOfAssociation"
            ]
        ]
        company_ministerial_decree: NotRequired[
            Optional["Account.CreateParamsDocumentsCompanyMinisterialDecree"]
        ]
        company_registration_verification: NotRequired[
            Optional[
                "Account.CreateParamsDocumentsCompanyRegistrationVerification"
            ]
        ]
        company_tax_id_verification: NotRequired[
            Optional["Account.CreateParamsDocumentsCompanyTaxIdVerification"]
        ]
        proof_of_registration: NotRequired[
            Optional["Account.CreateParamsDocumentsProofOfRegistration"]
        ]

    class CreateParamsDocumentsProofOfRegistration(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsCompanyTaxIdVerification(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsCompanyRegistrationVerification(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsCompanyMinisterialDecree(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsCompanyMemorandumOfAssociation(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsCompanyLicense(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsDocumentsBankAccountOwnershipVerification(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreateParamsCompany(TypedDict):
        address: NotRequired[Optional["Account.CreateParamsCompanyAddress"]]
        address_kana: NotRequired[
            Optional["Account.CreateParamsCompanyAddressKana"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreateParamsCompanyAddressKanji"]
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
            Optional["Account.CreateParamsCompanyOwnershipDeclaration"]
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
            Optional["Account.CreateParamsCompanyVerification"]
        ]

    class CreateParamsCompanyVerification(TypedDict):
        document: NotRequired[
            Optional["Account.CreateParamsCompanyVerificationDocument"]
        ]

    class CreateParamsCompanyVerificationDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreateParamsCompanyOwnershipDeclaration(TypedDict):
        date: NotRequired[Optional[int]]
        ip: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParamsCompanyAddressKanji(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateParamsCompanyAddressKana(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreateParamsCompanyAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsCapabilities(TypedDict):
        acss_debit_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesAcssDebitPayments"]
        ]
        affirm_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesAffirmPayments"]
        ]
        afterpay_clearpay_payments: NotRequired[
            Optional[
                "Account.CreateParamsCapabilitiesAfterpayClearpayPayments"
            ]
        ]
        au_becs_debit_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesAuBecsDebitPayments"]
        ]
        bacs_debit_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesBacsDebitPayments"]
        ]
        bancontact_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesBancontactPayments"]
        ]
        bank_transfer_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesBankTransferPayments"]
        ]
        blik_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesBlikPayments"]
        ]
        boleto_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesBoletoPayments"]
        ]
        card_issuing: NotRequired[
            Optional["Account.CreateParamsCapabilitiesCardIssuing"]
        ]
        card_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesCardPayments"]
        ]
        cartes_bancaires_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesCartesBancairesPayments"]
        ]
        cashapp_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesCashappPayments"]
        ]
        eps_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesEpsPayments"]
        ]
        fpx_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesFpxPayments"]
        ]
        giropay_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesGiropayPayments"]
        ]
        grabpay_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesGrabpayPayments"]
        ]
        ideal_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesIdealPayments"]
        ]
        india_international_payments: NotRequired[
            Optional[
                "Account.CreateParamsCapabilitiesIndiaInternationalPayments"
            ]
        ]
        jcb_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesJcbPayments"]
        ]
        klarna_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesKlarnaPayments"]
        ]
        konbini_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesKonbiniPayments"]
        ]
        legacy_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesLegacyPayments"]
        ]
        link_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesLinkPayments"]
        ]
        oxxo_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesOxxoPayments"]
        ]
        p24_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesP24Payments"]
        ]
        paynow_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesPaynowPayments"]
        ]
        promptpay_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesPromptpayPayments"]
        ]
        sepa_debit_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesSepaDebitPayments"]
        ]
        sofort_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesSofortPayments"]
        ]
        tax_reporting_us_1099_k: NotRequired[
            Optional["Account.CreateParamsCapabilitiesTaxReportingUs1099K"]
        ]
        tax_reporting_us_1099_misc: NotRequired[
            Optional["Account.CreateParamsCapabilitiesTaxReportingUs1099Misc"]
        ]
        transfers: NotRequired[
            Optional["Account.CreateParamsCapabilitiesTransfers"]
        ]
        treasury: NotRequired[
            Optional["Account.CreateParamsCapabilitiesTreasury"]
        ]
        us_bank_account_ach_payments: NotRequired[
            Optional[
                "Account.CreateParamsCapabilitiesUsBankAccountAchPayments"
            ]
        ]
        zip_payments: NotRequired[
            Optional["Account.CreateParamsCapabilitiesZipPayments"]
        ]

    class CreateParamsCapabilitiesZipPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesUsBankAccountAchPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesTreasury(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesTransfers(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesTaxReportingUs1099Misc(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesTaxReportingUs1099K(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesSofortPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesSepaDebitPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesPromptpayPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesPaynowPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesP24Payments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesOxxoPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesLinkPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesLegacyPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesKonbiniPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesKlarnaPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesJcbPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesIndiaInternationalPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesIdealPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesGrabpayPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesGiropayPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesFpxPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesEpsPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesCashappPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesCartesBancairesPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesCardPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesCardIssuing(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesBoletoPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesBlikPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesBankTransferPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesBancontactPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesBacsDebitPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesAuBecsDebitPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesAfterpayClearpayPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesAffirmPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsCapabilitiesAcssDebitPayments(TypedDict):
        requested: NotRequired[Optional[bool]]

    class CreateParamsBusinessProfile(TypedDict):
        mcc: NotRequired[Optional[str]]
        monthly_estimated_revenue: NotRequired[
            Optional[
                "Account.CreateParamsBusinessProfileMonthlyEstimatedRevenue"
            ]
        ]
        name: NotRequired[Optional[str]]
        product_description: NotRequired[Optional[str]]
        support_address: NotRequired[
            Optional["Account.CreateParamsBusinessProfileSupportAddress"]
        ]
        support_email: NotRequired[Optional[str]]
        support_phone: NotRequired[Optional[str]]
        support_url: NotRequired[Optional[Union[Literal[""], str]]]
        url: NotRequired[Optional[str]]

    class CreateParamsBusinessProfileSupportAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsBusinessProfileMonthlyEstimatedRevenue(TypedDict):
        amount: int
        currency: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        created: NotRequired[Optional[Union["Account.ListParamsCreated", int]]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class PersonsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        relationship: NotRequired[
            Optional["Account.PersonsParamsRelationship"]
        ]
        starting_after: NotRequired[Optional[str]]

    class PersonsParamsRelationship(TypedDict):
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
            Optional["Account.ModifyExternalAccountParamsDocuments"]
        ]
        exp_month: NotRequired[Optional[str]]
        exp_year: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        name: NotRequired[Optional[str]]

    class ModifyExternalAccountParamsDocuments(TypedDict):
        bank_account_ownership_verification: NotRequired[
            Optional[
                "Account.ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification"
            ]
        ]

    class ModifyExternalAccountParamsDocumentsBankAccountOwnershipVerification(
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
        address: NotRequired[Optional["Account.CreatePersonParamsAddress"]]
        address_kana: NotRequired[
            Optional["Account.CreatePersonParamsAddressKana"]
        ]
        address_kanji: NotRequired[
            Optional["Account.CreatePersonParamsAddressKanji"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.CreatePersonParamsDob"]]
        ]
        documents: NotRequired[Optional["Account.CreatePersonParamsDocuments"]]
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
            Optional["Account.CreatePersonParamsRegisteredAddress"]
        ]
        relationship: NotRequired[
            Optional["Account.CreatePersonParamsRelationship"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.CreatePersonParamsVerification"]
        ]

    class CreatePersonParamsVerification(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.CreatePersonParamsVerificationAdditionalDocument"
            ]
        ]
        document: NotRequired[
            Optional["Account.CreatePersonParamsVerificationDocument"]
        ]

    class CreatePersonParamsVerificationDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreatePersonParamsVerificationAdditionalDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class CreatePersonParamsRelationship(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        percent_ownership: NotRequired[Optional[Union[Literal[""], float]]]
        representative: NotRequired[Optional[bool]]
        title: NotRequired[Optional[str]]

    class CreatePersonParamsRegisteredAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreatePersonParamsDocuments(TypedDict):
        company_authorization: NotRequired[
            Optional["Account.CreatePersonParamsDocumentsCompanyAuthorization"]
        ]
        passport: NotRequired[
            Optional["Account.CreatePersonParamsDocumentsPassport"]
        ]
        visa: NotRequired[Optional["Account.CreatePersonParamsDocumentsVisa"]]

    class CreatePersonParamsDocumentsVisa(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonParamsDocumentsPassport(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonParamsDocumentsCompanyAuthorization(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class CreatePersonParamsDob(TypedDict):
        day: int
        month: int
        year: int

    class CreatePersonParamsAddressKanji(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreatePersonParamsAddressKana(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class CreatePersonParamsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class RetrievePersonParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ModifyPersonParams(RequestOptions):
        address: NotRequired[Optional["Account.ModifyPersonParamsAddress"]]
        address_kana: NotRequired[
            Optional["Account.ModifyPersonParamsAddressKana"]
        ]
        address_kanji: NotRequired[
            Optional["Account.ModifyPersonParamsAddressKanji"]
        ]
        dob: NotRequired[
            Optional[Union[Literal[""], "Account.ModifyPersonParamsDob"]]
        ]
        documents: NotRequired[Optional["Account.ModifyPersonParamsDocuments"]]
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
            Optional["Account.ModifyPersonParamsRegisteredAddress"]
        ]
        relationship: NotRequired[
            Optional["Account.ModifyPersonParamsRelationship"]
        ]
        ssn_last_4: NotRequired[Optional[str]]
        verification: NotRequired[
            Optional["Account.ModifyPersonParamsVerification"]
        ]

    class ModifyPersonParamsVerification(TypedDict):
        additional_document: NotRequired[
            Optional[
                "Account.ModifyPersonParamsVerificationAdditionalDocument"
            ]
        ]
        document: NotRequired[
            Optional["Account.ModifyPersonParamsVerificationDocument"]
        ]

    class ModifyPersonParamsVerificationDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class ModifyPersonParamsVerificationAdditionalDocument(TypedDict):
        back: NotRequired[Optional[str]]
        front: NotRequired[Optional[str]]

    class ModifyPersonParamsRelationship(TypedDict):
        director: NotRequired[Optional[bool]]
        executive: NotRequired[Optional[bool]]
        owner: NotRequired[Optional[bool]]
        percent_ownership: NotRequired[Optional[Union[Literal[""], float]]]
        representative: NotRequired[Optional[bool]]
        title: NotRequired[Optional[str]]

    class ModifyPersonParamsRegisteredAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyPersonParamsDocuments(TypedDict):
        company_authorization: NotRequired[
            Optional["Account.ModifyPersonParamsDocumentsCompanyAuthorization"]
        ]
        passport: NotRequired[
            Optional["Account.ModifyPersonParamsDocumentsPassport"]
        ]
        visa: NotRequired[Optional["Account.ModifyPersonParamsDocumentsVisa"]]

    class ModifyPersonParamsDocumentsVisa(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonParamsDocumentsPassport(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonParamsDocumentsCompanyAuthorization(TypedDict):
        files: NotRequired[Optional[List[str]]]

    class ModifyPersonParamsDob(TypedDict):
        day: int
        month: int
        year: int

    class ModifyPersonParamsAddressKanji(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class ModifyPersonParamsAddressKana(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]
        town: NotRequired[Optional[str]]

    class ModifyPersonParamsAddress(TypedDict):
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
            Optional["Account.ListPersonsParamsRelationship"]
        ]
        starting_after: NotRequired[Optional[str]]

    class ListPersonsParamsRelationship(TypedDict):
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
