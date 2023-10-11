# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.account import Account
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class Capability(UpdateableAPIResource["Capability"]):
    """
    This is an object representing a capability for a Stripe account.

    Related guide: [Account capabilities](https://stripe.com/docs/connect/account-capabilities)
    """

    OBJECT_NAME = "capability"

    class FutureRequirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_dob_age_under_18",
                "invalid_representative_country",
                "invalid_street_address",
                "invalid_tos_acceptance",
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
        current_deadline: Optional[int]
        currently_due: List[str]
        disabled_reason: Optional[str]
        errors: List[Error]
        eventually_due: List[str]
        past_due: List[str]
        pending_verification: List[str]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    class Requirements(StripeObject):
        class Alternative(StripeObject):
            alternative_fields_due: List[str]
            original_fields_due: List[str]

        class Error(StripeObject):
            code: Literal[
                "invalid_address_city_state_postal_code",
                "invalid_dob_age_under_18",
                "invalid_representative_country",
                "invalid_street_address",
                "invalid_tos_acceptance",
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
        current_deadline: Optional[int]
        currently_due: List[str]
        disabled_reason: Optional[str]
        errors: List[Error]
        eventually_due: List[str]
        past_due: List[str]
        pending_verification: List[str]
        _inner_class_types = {"alternatives": Alternative, "errors": Error}

    account: ExpandableField["Account"]
    future_requirements: Optional[FutureRequirements]
    id: str
    object: Literal["capability"]
    requested: bool
    requested_at: Optional[int]
    requirements: Optional[Requirements]
    status: Literal["active", "disabled", "inactive", "pending", "unrequested"]

    def instance_url(self):
        token = self.id
        account = self.account
        base = Account.class_url()
        if isinstance(account, Account):
            account = account.id
        acct_extn = quote_plus(account)
        extn = quote_plus(token)
        return "%s/%s/capabilities/%s" % (base, acct_extn, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't update a capability without an account ID. Update a capability using "
            "account.modify_capability('acct_123', 'acap_123', params)"
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a capability without an account ID. Retrieve a capability using "
            "account.retrieve_capability('acct_123', 'acap_123')"
        )

    _inner_class_types = {
        "future_requirements": FutureRequirements,
        "requirements": Requirements,
    }
