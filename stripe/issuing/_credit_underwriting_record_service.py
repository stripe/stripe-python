# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.issuing._credit_underwriting_record import CreditUnderwritingRecord
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CreditUnderwritingRecordService(StripeService):
    class CorrectParams(TypedDict):
        application: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsApplication"
        ]
        """
        Details about the application submission.
        """
        credit_user: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsCreditUser"
        ]
        """
        Information about the company or person applying or holding the account.
        """
        decided_at: NotRequired["int"]
        """
        Date when a decision was made.
        """
        decision: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsDecision"
        ]
        """
        Details about the decision.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        underwriting_exception: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsUnderwritingException"
        ]
        """
        If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
        """

    class CorrectParamsApplication(TypedDict):
        application_method: NotRequired[
            "Literal['in_person', 'mail', 'online', 'phone']"
        ]
        """
        The channel through which the applicant has submitted their application. Defaults to `online`.
        """
        purpose: Literal["credit_limit_increase", "credit_line_opening"]
        """
        Scope of demand made by the applicant.
        """
        submitted_at: int
        """
        Date when the applicant submitted their application.
        """

    class CorrectParamsCreditUser(TypedDict):
        email: str
        """
        Email of the applicant or accountholder.
        """
        name: str
        """
        Full name of the company or person.
        """

    class CorrectParamsDecision(TypedDict):
        application_rejected: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsDecisionApplicationRejected"
        ]
        """
        Details about the application rejection.
        """
        credit_limit_approved: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsDecisionCreditLimitApproved"
        ]
        """
        Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy/)
        """
        credit_limit_decreased: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsDecisionCreditLimitDecreased"
        ]
        """
        Details about the credit limit decreased.
        """
        credit_line_closed: NotRequired[
            "CreditUnderwritingRecordService.CorrectParamsDecisionCreditLineClosed"
        ]
        """
        Details about the credit line closed.
        """
        type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]
        """
        Outcome of the decision.
        """

    class CorrectParamsDecisionApplicationRejected(TypedDict):
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
                "duration_of_residence",
                "excessive_income_or_revenue_obligations",
                "expenses_to_cash_balance_ratio_too_high",
                "foreclosure_or_repossession",
                "frozen_file_at_credit_bureau",
                "garnishment_or_attachment",
                "government_loan_program_criteria",
                "high_concentration_of_clients",
                "high_risk_industry",
                "incomplete_application",
                "inconsistent_monthly_revenues",
                "insufficient_account_history_with_platform",
                "insufficient_bank_account_history",
                "insufficient_cash_balance",
                "insufficient_cash_flow",
                "insufficient_collateral",
                "insufficient_credit_experience",
                "insufficient_deposits",
                "insufficient_income",
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the application was rejected, up to 4 reasons, in order of importance.
        """

    class CorrectParamsDecisionCreditLimitApproved(TypedDict):
        amount: int
        """
        The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        currency: NotRequired["str"]
        """
        The currency of the credit approved, will default to the Account's Issuing currency.
        """

    class CorrectParamsDecisionCreditLimitDecreased(TypedDict):
        amount: int
        """
        The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        currency: NotRequired["str"]
        """
        The currency of the credit approved, will default to the Account's Issuing currency.
        """
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "change_in_financial_state",
                "change_in_utilization_of_credit_line",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "decrease_in_income_to_expense_ratio",
                "decrease_in_social_media_performance",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
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
                "high_risk_industry",
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
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "insufficient_usage_as_qualified_expenses",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the existing credit was decreased, up to 4 reasons, in order of importance.
        """

    class CorrectParamsDecisionCreditLineClosed(TypedDict):
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "change_in_financial_state",
                "change_in_utilization_of_credit_line",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "decrease_in_income_to_expense_ratio",
                "decrease_in_social_media_performance",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
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
                "high_risk_industry",
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
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "insufficient_usage_as_qualified_expenses",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the credit line was closed, up to 4 reasons, in order of importance.
        """

    class CorrectParamsUnderwritingException(TypedDict):
        explanation: str
        """
        Written explanation for the exception.
        """
        original_decision_type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]
        """
        The decision before the exception was applied.
        """

    class CreateFromApplicationParams(TypedDict):
        application: "CreditUnderwritingRecordService.CreateFromApplicationParamsApplication"
        """
        Details about the application submission.
        """
        credit_user: "CreditUnderwritingRecordService.CreateFromApplicationParamsCreditUser"
        """
        Information about the company or person applying or holding the account.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class CreateFromApplicationParamsApplication(TypedDict):
        application_method: NotRequired[
            "Literal['in_person', 'mail', 'online', 'phone']"
        ]
        """
        The channel through which the applicant has submitted their application. Defaults to `online`.
        """
        purpose: Literal["credit_limit_increase", "credit_line_opening"]
        """
        Scope of demand made by the applicant.
        """
        submitted_at: int
        """
        Date when the applicant submitted their application.
        """

    class CreateFromApplicationParamsCreditUser(TypedDict):
        email: str
        """
        Email of the applicant or accountholder.
        """
        name: str
        """
        Full name of the company or person.
        """

    class CreateFromProactiveReviewParams(TypedDict):
        credit_user: "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsCreditUser"
        """
        Information about the company or person applying or holding the account.
        """
        decided_at: int
        """
        Date when a decision was made.
        """
        decision: "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsDecision"
        """
        Details about the decision.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        underwriting_exception: NotRequired[
            "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsUnderwritingException"
        ]
        """
        If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
        """

    class CreateFromProactiveReviewParamsCreditUser(TypedDict):
        email: str
        """
        Email of the applicant or accountholder.
        """
        name: str
        """
        Full name of the company or person.
        """

    class CreateFromProactiveReviewParamsDecision(TypedDict):
        credit_limit_approved: NotRequired[
            "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsDecisionCreditLimitApproved"
        ]
        """
        Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy/)
        """
        credit_limit_decreased: NotRequired[
            "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsDecisionCreditLimitDecreased"
        ]
        """
        Details about the credit limit decreased.
        """
        credit_line_closed: NotRequired[
            "CreditUnderwritingRecordService.CreateFromProactiveReviewParamsDecisionCreditLineClosed"
        ]
        """
        Details about the credit line closed.
        """
        type: Literal[
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
        ]
        """
        Outcome of the decision.
        """

    class CreateFromProactiveReviewParamsDecisionCreditLimitApproved(
        TypedDict
    ):
        amount: int
        """
        The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        currency: NotRequired["str"]
        """
        The currency of the credit approved, will default to the Account's Issuing currency.
        """

    class CreateFromProactiveReviewParamsDecisionCreditLimitDecreased(
        TypedDict,
    ):
        amount: int
        """
        The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        currency: NotRequired["str"]
        """
        The currency of the credit approved, will default to the Account's Issuing currency.
        """
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "change_in_financial_state",
                "change_in_utilization_of_credit_line",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "decrease_in_income_to_expense_ratio",
                "decrease_in_social_media_performance",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
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
                "high_risk_industry",
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
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "insufficient_usage_as_qualified_expenses",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the existing credit was decreased, up to 4 reasons, in order of importance.
        """

    class CreateFromProactiveReviewParamsDecisionCreditLineClosed(TypedDict):
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "change_in_financial_state",
                "change_in_utilization_of_credit_line",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "decrease_in_income_to_expense_ratio",
                "decrease_in_social_media_performance",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
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
                "high_risk_industry",
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
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "insufficient_usage_as_qualified_expenses",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the credit line was closed, up to 4 reasons, in order of importance.
        """

    class CreateFromProactiveReviewParamsUnderwritingException(TypedDict):
        explanation: str
        """
        Written explanation for the exception.
        """
        original_decision_type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]
        """
        The decision before the exception was applied.
        """

    class ListParams(TypedDict):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ReportDecisionParams(TypedDict):
        decided_at: int
        """
        Date when a decision was made.
        """
        decision: "CreditUnderwritingRecordService.ReportDecisionParamsDecision"
        """
        Details about the decision.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        underwriting_exception: NotRequired[
            "CreditUnderwritingRecordService.ReportDecisionParamsUnderwritingException"
        ]
        """
        If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
        """

    class ReportDecisionParamsDecision(TypedDict):
        application_rejected: NotRequired[
            "CreditUnderwritingRecordService.ReportDecisionParamsDecisionApplicationRejected"
        ]
        """
        Details about the application rejection.
        """
        credit_limit_approved: NotRequired[
            "CreditUnderwritingRecordService.ReportDecisionParamsDecisionCreditLimitApproved"
        ]
        """
        Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy/)
        """
        type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "withdrawn_by_applicant",
        ]
        """
        Outcome of the decision.
        """

    class ReportDecisionParamsDecisionApplicationRejected(TypedDict):
        reason_other_explanation: NotRequired["str"]
        """
        Details about the `reasons.other` when present.
        """
        reasons: List[
            Literal[
                "applicant_is_not_beneficial_owner",
                "applicant_too_young",
                "application_is_not_beneficial_owner",
                "bankruptcy",
                "business_size_too_small",
                "current_account_tier_ineligible",
                "customer_already_exists",
                "customer_requested_account_closure",
                "debt_to_cash_balance_ratio_too_high",
                "debt_to_equity_ratio_too_high",
                "delinquent_credit_obligations",
                "dispute_rate_too_high",
                "duration_of_residence",
                "excessive_income_or_revenue_obligations",
                "expenses_to_cash_balance_ratio_too_high",
                "foreclosure_or_repossession",
                "frozen_file_at_credit_bureau",
                "garnishment_or_attachment",
                "government_loan_program_criteria",
                "high_concentration_of_clients",
                "high_risk_industry",
                "incomplete_application",
                "inconsistent_monthly_revenues",
                "insufficient_account_history_with_platform",
                "insufficient_bank_account_history",
                "insufficient_cash_balance",
                "insufficient_cash_flow",
                "insufficient_collateral",
                "insufficient_credit_experience",
                "insufficient_deposits",
                "insufficient_income",
                "insufficient_margin_ratio",
                "insufficient_operating_profit",
                "insufficient_period_in_operation",
                "insufficient_reserves",
                "insufficient_revenue",
                "insufficient_social_media_performance",
                "insufficient_time_in_network",
                "insufficient_trade_credit_insurance",
                "invalid_business_license",
                "lacking_cash_account",
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
        """
        List of reasons why the application was rejected, up to 4 reasons, in order of importance.
        """

    class ReportDecisionParamsDecisionCreditLimitApproved(TypedDict):
        amount: int
        """
        The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
        """
        currency: NotRequired["str"]
        """
        The currency of the credit approved, will default to the Account's Issuing currency.
        """

    class ReportDecisionParamsUnderwritingException(TypedDict):
        explanation: str
        """
        Written explanation for the exception.
        """
        original_decision_type: Literal[
            "additional_information_requested",
            "application_rejected",
            "credit_limit_approved",
            "credit_limit_decreased",
            "credit_line_closed",
            "no_changes",
            "withdrawn_by_applicant",
        ]
        """
        The decision before the exception was applied.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "CreditUnderwritingRecordService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CreditUnderwritingRecord]:
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            ListObject[CreditUnderwritingRecord],
            self._request(
                "get",
                "/v1/issuing/credit_underwriting_records",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CreditUnderwritingRecordService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CreditUnderwritingRecord]:
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        return cast(
            ListObject[CreditUnderwritingRecord],
            await self._request_async(
                "get",
                "/v1/issuing/credit_underwriting_records",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        return cast(
            CreditUnderwritingRecord,
            self._request(
                "get",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        return cast(
            CreditUnderwritingRecord,
            await self._request_async(
                "get",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def correct(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.CorrectParams" = {},
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            CreditUnderwritingRecord,
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def correct_async(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.CorrectParams" = {},
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            CreditUnderwritingRecord,
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def report_decision(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.ReportDecisionParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            CreditUnderwritingRecord,
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def report_decision_async(
        self,
        credit_underwriting_record: str,
        params: "CreditUnderwritingRecordService.ReportDecisionParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            CreditUnderwritingRecord,
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    ),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_application(
        self,
        params: "CreditUnderwritingRecordService.CreateFromApplicationParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            CreditUnderwritingRecord,
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_application_async(
        self,
        params: "CreditUnderwritingRecordService.CreateFromApplicationParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            CreditUnderwritingRecord,
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_proactive_review(
        self,
        params: "CreditUnderwritingRecordService.CreateFromProactiveReviewParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            CreditUnderwritingRecord,
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_proactive_review_async(
        self,
        params: "CreditUnderwritingRecordService.CreateFromProactiveReviewParams",
        options: RequestOptions = {},
    ) -> CreditUnderwritingRecord:
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            CreditUnderwritingRecord,
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
