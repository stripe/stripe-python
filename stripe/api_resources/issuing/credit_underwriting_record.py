# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
from typing_extensions import Literal


class CreditUnderwritingRecord(
    ListableAPIResource["CreditUnderwritingRecord"]
):
    """
    Every time an applicant submits an application for a Charge Card product your Platform offers, or every time your Platform takes a proactive credit decision on an existing account, you must record the decision by creating a new CreditUnderwritingRecord object on a Connected account.

    [Follow the guide](https://stripe.com/docs/issuing/coming_soon) to learn about your requirements as a Platform.
    """

    OBJECT_NAME = "issuing.credit_underwriting_record"

    class Application(StripeObject):
        application_method: Literal["in_person", "mail", "online", "phone"]
        purpose: Literal["credit_limit_increase", "credit_line_opening"]
        submitted_at: int

    class CreditUser(StripeObject):
        email: str
        name: str

    class Decision(StripeObject):
        class ApplicationRejected(StripeObject):
            reason_other_explanation: Optional[str]
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "change_in_financial_state",
                    "change_in_utilization_of_credit_line",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "decrease_in_income_to_expense_ratio",
                    "decrease_in_social_media_performance",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "exceeds_acceptable_platform_exposure",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "has_recent_credit_limit_increase",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_account_history_with_platform",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_credit_utilization",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "insufficient_usage_as_qualified_expenses",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
                    "poor_payment_history_with_platform",
                    "prior_or_current_legal_action",
                    "prohibited_industry",
                    "rate_of_cash_balance_fluctuation_too_high",
                    "recent_inquiries_on_business_credit_report",
                    "removal_of_bank_account_connection",
                    "revenue_discrepancy",
                    "runway_too_short",
                    "suspected_fraud",
                    "too_many_non_sufficient_funds_or_overdrafts",
                    "unable_to_verify_address",
                    "unable_to_verify_identity",
                    "unable_to_verify_income_or_revenue",
                    "unprofitable",
                    "unsupportable_business_type",
                ]
            ]

        class CreditLimitApproved(StripeObject):
            amount: int
            currency: str

        class CreditLimitDecreased(StripeObject):
            amount: int
            currency: str
            reason_other_explanation: Optional[str]
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "change_in_financial_state",
                    "change_in_utilization_of_credit_line",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "decrease_in_income_to_expense_ratio",
                    "decrease_in_social_media_performance",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "exceeds_acceptable_platform_exposure",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "has_recent_credit_limit_increase",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_account_history_with_platform",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_credit_utilization",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "insufficient_usage_as_qualified_expenses",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
                    "poor_payment_history_with_platform",
                    "prior_or_current_legal_action",
                    "prohibited_industry",
                    "rate_of_cash_balance_fluctuation_too_high",
                    "recent_inquiries_on_business_credit_report",
                    "removal_of_bank_account_connection",
                    "revenue_discrepancy",
                    "runway_too_short",
                    "suspected_fraud",
                    "too_many_non_sufficient_funds_or_overdrafts",
                    "unable_to_verify_address",
                    "unable_to_verify_identity",
                    "unable_to_verify_income_or_revenue",
                    "unprofitable",
                    "unsupportable_business_type",
                ]
            ]

        class CreditLineClosed(StripeObject):
            reason_other_explanation: Optional[str]
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "change_in_financial_state",
                    "change_in_utilization_of_credit_line",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "decrease_in_income_to_expense_ratio",
                    "decrease_in_social_media_performance",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "exceeds_acceptable_platform_exposure",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "has_recent_credit_limit_increase",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_account_history_with_platform",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_credit_utilization",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "insufficient_usage_as_qualified_expenses",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
                    "poor_payment_history_with_platform",
                    "prior_or_current_legal_action",
                    "prohibited_industry",
                    "rate_of_cash_balance_fluctuation_too_high",
                    "recent_inquiries_on_business_credit_report",
                    "removal_of_bank_account_connection",
                    "revenue_discrepancy",
                    "runway_too_short",
                    "suspected_fraud",
                    "too_many_non_sufficient_funds_or_overdrafts",
                    "unable_to_verify_address",
                    "unable_to_verify_identity",
                    "unable_to_verify_income_or_revenue",
                    "unprofitable",
                    "unsupportable_business_type",
                ]
            ]

        application_rejected: Optional[ApplicationRejected]
        credit_limit_approved: Optional[CreditLimitApproved]
        credit_limit_decreased: Optional[CreditLimitDecreased]
        credit_line_closed: Optional[CreditLineClosed]
        type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]
        _inner_class_types = {
            "application_rejected": ApplicationRejected,
            "credit_limit_approved": CreditLimitApproved,
            "credit_limit_decreased": CreditLimitDecreased,
            "credit_line_closed": CreditLineClosed,
        }

    class UnderwritingException(StripeObject):
        explanation: str
        original_decision_type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]

    application: Optional[Application]
    created: int
    created_from: Literal["application", "proactive_review"]
    credit_user: CreditUser
    decided_at: Optional[int]
    decision: Optional[Decision]
    decision_deadline: Optional[int]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["issuing.credit_underwriting_record"]
    underwriting_exception: Optional[UnderwritingException]

    @classmethod
    def _cls_correct(
        cls,
        credit_underwriting_record: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                credit_underwriting_record=util.sanitize_id(
                    credit_underwriting_record
                )
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_correct")
    def correct(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                credit_underwriting_record=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create_from_application(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/credit_underwriting_records/create_from_application",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_from_proactive_review(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["CreditUnderwritingRecord"]:
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
    def _cls_report_decision(
        cls,
        credit_underwriting_record: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                credit_underwriting_record=util.sanitize_id(
                    credit_underwriting_record
                )
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_report_decision")
    def report_decision(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                credit_underwriting_record=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "CreditUnderwritingRecord":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "application": Application,
        "credit_user": CreditUser,
        "decision": Decision,
        "underwriting_exception": UnderwritingException,
    }
