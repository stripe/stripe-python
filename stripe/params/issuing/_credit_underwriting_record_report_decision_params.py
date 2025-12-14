# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class CreditUnderwritingRecordReportDecisionParams(RequestOptions):
    decided_at: int
    """
    Date when a decision was made.
    """
    decision: "CreditUnderwritingRecordReportDecisionParamsDecision"
    """
    Details about the decision.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    regulatory_reporting_file: NotRequired[str]
    """
    File containing regulatory reporting data for the decision. Required if you are subject to this [reporting requirement](https://docs.stripe.com/issuing/credit/report-required-regulatory-data-for-credit-decisions).
    """
    underwriting_exception: NotRequired[
        "CreditUnderwritingRecordReportDecisionParamsUnderwritingException"
    ]
    """
    If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
    """


class CreditUnderwritingRecordReportDecisionParamsDecision(TypedDict):
    application_rejected: NotRequired[
        "CreditUnderwritingRecordReportDecisionParamsDecisionApplicationRejected"
    ]
    """
    Details about the application rejection.
    """
    credit_limit_approved: NotRequired[
        "CreditUnderwritingRecordReportDecisionParamsDecisionCreditLimitApproved"
    ]
    """
    Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://docs.stripe.com/api/issuing/credit_policy/)
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


class CreditUnderwritingRecordReportDecisionParamsDecisionApplicationRejected(
    TypedDict,
):
    reason_other_explanation: NotRequired[str]
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


class CreditUnderwritingRecordReportDecisionParamsDecisionCreditLimitApproved(
    TypedDict,
):
    amount: int
    """
    The credit approved, in the currency of the account and [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
    """
    currency: NotRequired[str]
    """
    The currency of the credit approved, will default to the Account's Issuing currency.
    """


class CreditUnderwritingRecordReportDecisionParamsUnderwritingException(
    TypedDict,
):
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
