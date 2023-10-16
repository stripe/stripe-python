# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account as AccountResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional
from typing_extensions import Literal, TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.file import File


class Person(UpdateableAPIResource["Person"]):
    """
    This is an object representing a person associated with a Stripe account.

    A platform cannot access a Standard or Express account's persons after the account starts onboarding, such as after generating an account link for the account.
    See the [Standard onboarding](https://stripe.com/docs/connect/standard-accounts) or [Express onboarding documentation](https://stripe.com/docs/connect/express-accounts) for information about platform prefilling and account onboarding steps.

    Related guide: [Handling identity verification with the API](https://stripe.com/docs/connect/handling-api-verification#person-information)
    """

    OBJECT_NAME = "person"

    class AdditionalTosAcceptances(StripeObject):
        class Account(StripeObject):
            date: Optional[int]
            ip: Optional[str]
            user_agent: Optional[str]

        account: Account
        _inner_class_types = {"account": Account}

    class Address(StripeObject):
        city: Optional[str]
        country: Optional[str]
        line1: Optional[str]
        line2: Optional[str]
        postal_code: Optional[str]
        state: Optional[str]

    class AddressKana(StripeObject):
        city: Optional[str]
        country: Optional[str]
        line1: Optional[str]
        line2: Optional[str]
        postal_code: Optional[str]
        state: Optional[str]
        town: Optional[str]

    class AddressKanji(StripeObject):
        city: Optional[str]
        country: Optional[str]
        line1: Optional[str]
        line2: Optional[str]
        postal_code: Optional[str]
        state: Optional[str]
        town: Optional[str]

    class Dob(StripeObject):
        day: Optional[int]
        month: Optional[int]
        year: Optional[int]

    class FutureRequirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
            ]
            reason: str
            requirement: str

        alternatives: Optional[List[Alternative]]
        currently_due: List[str]
        errors: List[Error]
        eventually_due: List[str]
        past_due: List[str]
        pending_verification: List[str]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class RegisteredAddress(StripeObject):
        city: Optional[str]
        country: Optional[str]
        line1: Optional[str]
        line2: Optional[str]
        postal_code: Optional[str]
        state: Optional[str]

    class Relationship(StripeObject):
        director: Optional[bool]
        executive: Optional[bool]
        legal_guardian: Optional[bool]
        owner: Optional[bool]
        percent_ownership: Optional[float]
        representative: Optional[bool]
        title: Optional[str]

    class Requirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_address_highway_contract_box",
                "invalid_address_private_mailbox",
                "invalid_business_profile_name",
                "invalid_business_profile_name_denylisted",
                "invalid_company_name_denylisted",
                "invalid_dob_age_over_maximum",
                "invalid_dob_age_under_18",
                "invalid_product_description_length",
                "invalid_product_description_url_match",
                "invalid_representative_country",
                "invalid_statement_descriptor_business_mismatch",
                "invalid_statement_descriptor_denylisted",
                "invalid_statement_descriptor_length",
                "invalid_statement_descriptor_prefix_denylisted",
                "invalid_statement_descriptor_prefix_mismatch",
                "invalid_street_address",
                "invalid_tax_id",
                "invalid_tax_id_format",
                "invalid_tos_acceptance",
                "invalid_url_denylisted",
                "invalid_url_format",
                "invalid_url_length",
                "invalid_url_web_presence_detected",
                "invalid_url_website_business_information_mismatch",
                "invalid_url_website_empty",
                "invalid_url_website_inaccessible",
                "invalid_url_website_inaccessible_geoblocked",
                "invalid_url_website_inaccessible_password_protected",
                "invalid_url_website_incomplete",
                "invalid_url_website_incomplete_cancellation_policy",
                "invalid_url_website_incomplete_customer_service_details",
                "invalid_url_website_incomplete_legal_restrictions",
                "invalid_url_website_incomplete_refund_policy",
                "invalid_url_website_incomplete_return_policy",
                "invalid_url_website_incomplete_terms_and_conditions",
                "invalid_url_website_incomplete_under_construction",
                "invalid_url_website_other",
                "invalid_value_other",
                "verification_directors_mismatch",
                "verification_document_address_mismatch",
                "verification_document_address_missing",
                "verification_document_corrupt",
                "verification_document_country_not_supported",
                "verification_document_directors_mismatch",
                "verification_document_dob_mismatch",
                "verification_document_duplicate_type",
                "verification_document_expired",
                "verification_document_failed_copy",
                "verification_document_failed_greyscale",
                "verification_document_failed_other",
                "verification_document_failed_test_mode",
                "verification_document_fraudulent",
                "verification_document_id_number_mismatch",
                "verification_document_id_number_missing",
                "verification_document_incomplete",
                "verification_document_invalid",
                "verification_document_issue_or_expiry_date_missing",
                "verification_document_manipulated",
                "verification_document_missing_back",
                "verification_document_missing_front",
                "verification_document_name_mismatch",
                "verification_document_name_missing",
                "verification_document_nationality_mismatch",
                "verification_document_not_readable",
                "verification_document_not_signed",
                "verification_document_not_uploaded",
                "verification_document_photo_mismatch",
                "verification_document_too_large",
                "verification_document_type_not_supported",
                "verification_extraneous_directors",
                "verification_failed_address_match",
                "verification_failed_business_iec_number",
                "verification_failed_document_match",
                "verification_failed_id_number_match",
                "verification_failed_keyed_identity",
                "verification_failed_keyed_match",
                "verification_failed_name_match",
                "verification_failed_other",
                "verification_failed_residential_address",
                "verification_failed_tax_id_match",
                "verification_failed_tax_id_not_issued",
                "verification_missing_directors",
                "verification_missing_executives",
                "verification_missing_owners",
                "verification_requires_additional_memorandum_of_associations",
            ]
            reason: str
            requirement: str

        alternatives: Optional[List[Alternative]]
        currently_due: List[str]
        errors: List[Error]
        eventually_due: List[str]
        past_due: List[str]
        pending_verification: List[str]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Verification(StripeObject):
        class AdditionalDocument(StripeObject):
            back: Optional[ExpandableField["File"]]
            details: Optional[str]
            details_code: Optional[str]
            front: Optional[ExpandableField["File"]]

        class Document(StripeObject):
            back: Optional[ExpandableField["File"]]
            details: Optional[str]
            details_code: Optional[str]
            front: Optional[ExpandableField["File"]]

        additional_document: Optional[AdditionalDocument]
        details: Optional[str]
        details_code: Optional[str]
        document: Optional[Document]
        status: str
        _inner_class_types = {
            "additional_document": AdditionalDocument,
            "document": Document,
        }

    account: Optional[str]
    additional_tos_acceptances: Optional[AdditionalTosAcceptances]
    address: Optional[Address]
    address_kana: Optional[AddressKana]
    address_kanji: Optional[AddressKanji]
    created: int
    dob: Optional[Dob]
    email: Optional[str]
    first_name: Optional[str]
    first_name_kana: Optional[str]
    first_name_kanji: Optional[str]
    full_name_aliases: Optional[List[str]]
    future_requirements: Optional[FutureRequirements]
    gender: Optional[str]
    id: str
    id_number_provided: Optional[bool]
    id_number_secondary_provided: Optional[bool]
    last_name: Optional[str]
    last_name_kana: Optional[str]
    last_name_kanji: Optional[str]
    maiden_name: Optional[str]
    metadata: Optional[Dict[str, str]]
    nationality: Optional[str]
    object: Literal["person"]
    phone: Optional[str]
    political_exposure: Optional[Literal["existing", "none"]]
    registered_address: Optional[RegisteredAddress]
    relationship: Optional[Relationship]
    requirements: Optional[Requirements]
    ssn_last_4_provided: Optional[bool]
    verification: Optional[Verification]
    deleted: Optional[Literal[True]]

    def instance_url(self):
        token = self.id
        account = self.account
        base = AccountResource.class_url()
        assert account is not None
        acct_extn = quote_plus(account)
        extn = quote_plus(token)
        return "%s/%s/persons/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a person without an account ID. "
            "Use stripe.Account.modify_person('account_id', 'person_id', ...) "
            "(see https://stripe.com/docs/api/persons/update)."
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a person without an account ID. "
            "Use stripe.Account.retrieve_person('account_id', 'person_id') "
            "(see https://stripe.com/docs/api/persons/retrieve)."
        )

    _inner_class_types = {
        "additional_tos_acceptances": AdditionalTosAcceptances,
        "address": Address,
        "address_kana": AddressKana,
        "address_kanji": AddressKanji,
        "dob": Dob,
        "future_requirements": FutureRequirements,
        "registered_address": RegisteredAddress,
        "relationship": Relationship,
        "requirements": Requirements,
        "verification": Verification,
    }
