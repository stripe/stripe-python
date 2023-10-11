# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources.abstract import (
    DeletableAPIResource,
    UpdateableAPIResource,
    VerifyMixin,
)
from stripe.api_resources.account import Account
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class BankAccount(
    DeletableAPIResource["BankAccount"],
    UpdateableAPIResource["BankAccount"],
    VerifyMixin,
):
    """
    These bank accounts are payment methods on `Customer` objects.

    On the other hand [External Accounts](https://stripe.com/docs/api#external_accounts) are transfer
    destinations on `Account` objects for [Custom accounts](https://stripe.com/docs/connect/custom-accounts).
    They can be bank accounts or debit cards as well, and are documented in the links above.

    Related guide: [Bank debits and transfers](https://stripe.com/docs/payments/bank-debits-transfers)
    """

    OBJECT_NAME = "bank_account"

    class FutureRequirements(StripeObject):
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

        currently_due: Optional[List[str]]
        errors: Optional[List[Error]]
        past_due: Optional[List[str]]
        pending_verification: Optional[List[str]]
        _inner_class_types = {"errors": Error}

    class Requirements(StripeObject):
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

        currently_due: Optional[List[str]]
        errors: Optional[List[Error]]
        past_due: Optional[List[str]]
        pending_verification: Optional[List[str]]
        _inner_class_types = {"errors": Error}

    account: Optional[ExpandableField["Account"]]
    account_holder_name: Optional[str]
    account_holder_type: Optional[str]
    account_type: Optional[str]
    available_payout_methods: Optional[List[Literal["instant", "standard"]]]
    bank_name: Optional[str]
    country: str
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    default_for_currency: Optional[bool]
    fingerprint: Optional[str]
    future_requirements: Optional[FutureRequirements]
    id: str
    last4: str
    metadata: Optional[Dict[str, str]]
    object: Literal["bank_account"]
    requirements: Optional[Requirements]
    routing_number: Optional[str]
    status: str
    deleted: Optional[Literal[True]]

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> Any:
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            Any,
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> Any:
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    def instance_url(self):
        token = self.id
        extn = quote_plus(token)
        if hasattr(self, "customer"):
            customer = self.customer

            base = Customer.class_url()
            assert customer is not None
            if isinstance(customer, Customer):
                customer = customer.id
            owner_extn = quote_plus(customer)
            class_base = "sources"

        elif hasattr(self, "account"):
            account = self.account

            base = Account.class_url()
            assert account is not None
            if isinstance(account, Account):
                account = account.id
            owner_extn = quote_plus(account)
            class_base = "external_accounts"

        else:
            raise error.InvalidRequestError(
                "Could not determine whether bank_account_id %s is "
                "attached to a customer or an account." % token,
                "id",
            )

        return "%s/%s/%s/%s" % (base, owner_extn, class_base, extn)

    @classmethod
    def modify(cls, sid, **params):
        raise NotImplementedError(
            "Can't modify a bank account without a customer or account ID. "
            "Use stripe.Customer.modify_source('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/customer_bank_accounts/update) or "
            "stripe.Account.modify_external_account('customer_id', 'bank_account_id', ...) "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/update)."
        )

    @classmethod
    def retrieve(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        raise NotImplementedError(
            "Can't retrieve a bank account without a customer or account ID. "
            "Use stripe.customer.retrieve_source('customer_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/customer_bank_accounts/retrieve) or "
            "stripe.Account.retrieve_external_account('account_id', 'bank_account_id') "
            "(see https://stripe.com/docs/api/external_account_bank_accounts/retrieve)."
        )

    _inner_class_types = {
        "future_requirements": FutureRequirements,
        "requirements": Requirements,
    }
