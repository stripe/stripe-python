# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


class CreditUnderwritingRecord(
    ListableAPIResource["CreditUnderwritingRecord"]
):
    """
    Every time an applicant submits an application for a Charge Card product your platform offers, or every time your platform takes a proactive credit decision on an existing account, you must record the decision by creating a new `CreditUnderwritingRecord` object on a connected account.

    [Follow the guide](https://stripe.com/docs/issuing/credit/report-credit-decisions-and-manage-aans) to learn about your requirements as a platform.
    """

    OBJECT_NAME: ClassVar[
        Literal["issuing.credit_underwriting_record"]
    ] = "issuing.credit_underwriting_record"

    class Application(StripeObject):
        application_method: Literal["in_person", "mail", "online", "phone"]
        """
        The channel through which the applicant has submitted their application.
        """
        purpose: Literal["credit_limit_increase", "credit_line_opening"]
        """
        Scope of demand made by the applicant.
        """
        submitted_at: int
        """
        Date when the applicant submitted their application.
        """

    class CreditUser(StripeObject):
        email: str
        """
        Email of the applicant or accountholder.
        """
        name: str
        """
        Full name of the company or person.
        """

    class Decision(StripeObject):
        class ApplicationRejected(StripeObject):
            reason_other_explanation: Optional[str]
            """
            Details about the `reasons.other` when present.
            """
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
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
            List of reasons why the application was rejected up to 4 reasons, in order of importance.
            """

        class CreditLimitApproved(StripeObject):
            amount: int
            """
            Credit amount approved. An approved credit limit is required before you can set a amount in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """

        class CreditLimitDecreased(StripeObject):
            amount: int
            """
            Credit amount approved after decrease. An approved credit limit is required before you can set a amount in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            reason_other_explanation: Optional[str]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the existing credit was decreased, up to 4 reasons, in order of importance.
            """

        class CreditLineClosed(StripeObject):
            reason_other_explanation: Optional[str]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the existing account was closed, up to 4 reasons, in order of importance.
            """

        application_rejected: Optional[ApplicationRejected]
        """
        Details about a decision application_rejected.
        """
        credit_limit_approved: Optional[CreditLimitApproved]
        """
        Details about a decision credit_limit_approved.
        """
        credit_limit_decreased: Optional[CreditLimitDecreased]
        """
        Details about a decision credit_limit_decreased.
        """
        credit_line_closed: Optional[CreditLineClosed]
        """
        Details about a decision credit_line_closed.
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
        _inner_class_types = {
            "application_rejected": ApplicationRejected,
            "credit_limit_approved": CreditLimitApproved,
            "credit_limit_decreased": CreditLimitDecreased,
            "credit_line_closed": CreditLineClosed,
        }

    class UnderwritingException(StripeObject):
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

    if TYPE_CHECKING:

        class CorrectParams(RequestOptions):
            application: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsApplication|None"
            ]
            """
            Details about the application submission.
            """
            credit_user: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsCreditUser|None"
            ]
            """
            Information about the company or person applying or holding the account.
            """
            decided_at: NotRequired["int|None"]
            """
            Date when a decision was made.
            """
            decision: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsDecision|None"
            ]
            """
            Details about the decision.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            underwriting_exception: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsUnderwritingException|None"
            ]
            """
            If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
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

        class CorrectParamsDecision(TypedDict):
            application_rejected: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsDecisionApplicationRejected|None"
            ]
            """
            Details about the application rejection.
            """
            credit_limit_approved: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsDecisionCreditLimitApproved|None"
            ]
            """
            Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy/)
            """
            credit_limit_decreased: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsDecisionCreditLimitDecreased|None"
            ]
            """
            Details about the credit limit decreased.
            """
            credit_line_closed: NotRequired[
                "CreditUnderwritingRecord.CorrectParamsDecisionCreditLineClosed|None"
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

        class CorrectParamsDecisionCreditLineClosed(TypedDict):
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the credit line was closed, up to 4 reasons, in order of importance.
            """

        class CorrectParamsDecisionCreditLimitDecreased(TypedDict):
            amount: int
            """
            The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: NotRequired["str|None"]
            """
            The currency of the credit approved, will default to the Account's Issuing currency.
            """
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the existing credit was decreased, up to 4 reasons, in order of importance.
            """

        class CorrectParamsDecisionCreditLimitApproved(TypedDict):
            amount: int
            """
            The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: NotRequired["str|None"]
            """
            The currency of the credit approved, will default to the Account's Issuing currency.
            """

        class CorrectParamsDecisionApplicationRejected(TypedDict):
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
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

        class CorrectParamsCreditUser(TypedDict):
            email: str
            """
            Email of the applicant or accountholder.
            """
            name: str
            """
            Full name of the company or person.
            """

        class CorrectParamsApplication(TypedDict):
            application_method: NotRequired[
                "Literal['in_person', 'mail', 'online', 'phone']|None"
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

        class CreateFromApplicationParams(RequestOptions):
            application: "CreditUnderwritingRecord.CreateFromApplicationParamsApplication"
            """
            Details about the application submission.
            """
            credit_user: "CreditUnderwritingRecord.CreateFromApplicationParamsCreditUser"
            """
            Information about the company or person applying or holding the account.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
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

        class CreateFromApplicationParamsApplication(TypedDict):
            application_method: NotRequired[
                "Literal['in_person', 'mail', 'online', 'phone']|None"
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

        class CreateFromProactiveReviewParams(RequestOptions):
            credit_user: "CreditUnderwritingRecord.CreateFromProactiveReviewParamsCreditUser"
            """
            Information about the company or person applying or holding the account.
            """
            decided_at: int
            """
            Date when a decision was made.
            """
            decision: "CreditUnderwritingRecord.CreateFromProactiveReviewParamsDecision"
            """
            Details about the decision.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            underwriting_exception: NotRequired[
                "CreditUnderwritingRecord.CreateFromProactiveReviewParamsUnderwritingException|None"
            ]
            """
            If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
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

        class CreateFromProactiveReviewParamsDecision(TypedDict):
            credit_limit_approved: NotRequired[
                "CreditUnderwritingRecord.CreateFromProactiveReviewParamsDecisionCreditLimitApproved|None"
            ]
            """
            Details about the credit limit approved. An approved credit limit is required before you can set a `credit_limit_amount` in the [CreditPolicy API](https://stripe.com/docs/api/issuing/credit_policy/)
            """
            credit_limit_decreased: NotRequired[
                "CreditUnderwritingRecord.CreateFromProactiveReviewParamsDecisionCreditLimitDecreased|None"
            ]
            """
            Details about the credit limit decreased.
            """
            credit_line_closed: NotRequired[
                "CreditUnderwritingRecord.CreateFromProactiveReviewParamsDecisionCreditLineClosed|None"
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

        class CreateFromProactiveReviewParamsDecisionCreditLineClosed(
            TypedDict,
        ):
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the credit line was closed, up to 4 reasons, in order of importance.
            """

        class CreateFromProactiveReviewParamsDecisionCreditLimitDecreased(
            TypedDict,
        ):
            amount: int
            """
            The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: NotRequired["str|None"]
            """
            The currency of the credit approved, will default to the Account's Issuing currency.
            """
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
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
            """
            List of reasons why the existing credit was decreased, up to 4 reasons, in order of importance.
            """

        class CreateFromProactiveReviewParamsDecisionCreditLimitApproved(
            TypedDict,
        ):
            amount: int
            """
            The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: NotRequired["str|None"]
            """
            The currency of the credit approved, will default to the Account's Issuing currency.
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

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ReportDecisionParams(RequestOptions):
            decided_at: int
            """
            Date when a decision was made.
            """
            decision: "CreditUnderwritingRecord.ReportDecisionParamsDecision"
            """
            Details about the decision.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            underwriting_exception: NotRequired[
                "CreditUnderwritingRecord.ReportDecisionParamsUnderwritingException|None"
            ]
            """
            If an exception to the usual underwriting criteria was made for this decision, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
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

        class ReportDecisionParamsDecision(TypedDict):
            application_rejected: NotRequired[
                "CreditUnderwritingRecord.ReportDecisionParamsDecisionApplicationRejected|None"
            ]
            """
            Details about the application rejection.
            """
            credit_limit_approved: NotRequired[
                "CreditUnderwritingRecord.ReportDecisionParamsDecisionCreditLimitApproved|None"
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

        class ReportDecisionParamsDecisionCreditLimitApproved(TypedDict):
            amount: int
            """
            The credit approved, in the currency of the account and [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
            """
            currency: NotRequired["str|None"]
            """
            The currency of the credit approved, will default to the Account's Issuing currency.
            """

        class ReportDecisionParamsDecisionApplicationRejected(TypedDict):
            reason_other_explanation: NotRequired["str|None"]
            """
            Details about the `reasons.other` when present.
            """
            reasons: List[
                Literal[
                    "applicant_too_young",
                    "application_is_not_beneficial_owner",
                    "bankruptcy",
                    "business_size_too_small",
                    "customer_already_exists",
                    "debt_to_cash_balance_ratio_too_high",
                    "debt_to_equity_ratio_too_high",
                    "delinquent_credit_obligations",
                    "duration_of_residence",
                    "excessive_income_or_revenue_obligations",
                    "expenses_to_cash_balance_ratio_too_high",
                    "foreclosure_or_repossession",
                    "frozen_file_at_credit_bureau",
                    "garnishment_or_attachment",
                    "government_loan_program_criteria",
                    "high_concentration_of_clients",
                    "incomplete_application",
                    "inconsistent_monthly_revenues",
                    "insufficient_bank_account_history",
                    "insufficient_cash_balance",
                    "insufficient_cash_flow",
                    "insufficient_collateral",
                    "insufficient_credit_experience",
                    "insufficient_deposits",
                    "insufficient_income",
                    "insufficient_period_in_operation",
                    "insufficient_revenue",
                    "insufficient_social_media_performance",
                    "insufficient_trade_credit_insurance",
                    "late_payment_history_reported_to_bureau",
                    "lien_collection_action_or_judgement",
                    "negative_public_information",
                    "no_credit_file",
                    "other",
                    "outside_supported_country",
                    "outside_supported_state",
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

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    application: Optional[Application]
    """
    For decisions triggered by an application, details about the submission.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    created_from: Literal["application", "proactive_review"]
    """
    The event that triggered the underwriting.
    """
    credit_user: CreditUser
    decided_at: Optional[int]
    """
    Date when a decision was made.
    """
    decision: Optional[Decision]
    """
    Details about the decision.
    """
    decision_deadline: Optional[int]
    """
    For underwriting initiated by an application, a decision must be taken 30 days after the submission.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["issuing.credit_underwriting_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    underwriting_exception: Optional[UnderwritingException]
    """
    If an exception to the usual underwriting criteria was made for this application, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
    """

    @classmethod
    def _cls_correct(
        cls,
        credit_underwriting_record: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.CorrectParams"]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
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
            ),
        )

    @overload
    @classmethod
    def correct(
        cls,
        credit_underwriting_record: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.CorrectParams"]
    ) -> "CreditUnderwritingRecord":
        ...

    @overload
    def correct(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.CorrectParams"]
    ) -> "CreditUnderwritingRecord":
        ...

    @class_method_variant("_cls_correct")
    def correct(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.CorrectParams"]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create_from_application(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "CreditUnderwritingRecord.CreateFromApplicationParams"
        ]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_from_proactive_review(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "CreditUnderwritingRecord.CreateFromProactiveReviewParams"
        ]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.ListParams"]
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
        **params: Unpack["CreditUnderwritingRecord.ReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
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
            ),
        )

    @overload
    @classmethod
    def report_decision(
        cls,
        credit_underwriting_record: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.ReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        ...

    @overload
    def report_decision(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.ReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        ...

    @class_method_variant("_cls_report_decision")
    def report_decision(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["CreditUnderwritingRecord.ReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["CreditUnderwritingRecord.RetrieveParams"]
    ) -> "CreditUnderwritingRecord":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "application": Application,
        "credit_user": CreditUser,
        "decision": Decision,
        "underwriting_exception": UnderwritingException,
    }
