# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.issuing._credit_underwriting_record_correct_params import (
        CreditUnderwritingRecordCorrectParams,
    )
    from stripe.params.issuing._credit_underwriting_record_create_from_application_params import (
        CreditUnderwritingRecordCreateFromApplicationParams,
    )
    from stripe.params.issuing._credit_underwriting_record_create_from_proactive_review_params import (
        CreditUnderwritingRecordCreateFromProactiveReviewParams,
    )
    from stripe.params.issuing._credit_underwriting_record_list_params import (
        CreditUnderwritingRecordListParams,
    )
    from stripe.params.issuing._credit_underwriting_record_report_decision_params import (
        CreditUnderwritingRecordReportDecisionParams,
    )
    from stripe.params.issuing._credit_underwriting_record_retrieve_params import (
        CreditUnderwritingRecordRetrieveParams,
    )


class CreditUnderwritingRecord(
    ListableAPIResource["CreditUnderwritingRecord"]
):
    """
    Every time an applicant submits an application for a Charge Card product your platform offers, or every time your platform takes a proactive credit decision on an existing account, you must record the decision by creating a new `CreditUnderwritingRecord` object on a connected account.

    [Follow the guide](https://docs.stripe.com/issuing/credit/report-credit-decisions-and-manage-aans) to learn about your requirements as a platform.
    """

    OBJECT_NAME: ClassVar[Literal["issuing.credit_underwriting_record"]] = (
        "issuing.credit_underwriting_record"
    )

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
            List of reasons why the application was rejected up to 4 reasons, in order of importance.
            """

        class CreditLimitApproved(StripeObject):
            amount: int
            """
            Credit amount approved. An approved credit limit is required before you can set a amount in the [CreditPolicy API](https://docs.stripe.com/api/issuing/credit_policy).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """

        class CreditLimitDecreased(StripeObject):
            amount: int
            """
            Credit amount approved after decrease. An approved credit limit is required before you can set a amount in the [CreditPolicy API](https://docs.stripe.com/api/issuing/credit_policy).
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

        class CreditLineClosed(StripeObject):
            reason_other_explanation: Optional[str]
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
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["issuing.credit_underwriting_record"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    regulatory_reporting_file: Optional[str]
    """
    File containing regulatory reporting data for the decision. Required if you are subject to this [reporting requirement](https://docs.stripe.com/issuing/credit/report-required-regulatory-data-for-credit-decisions).
    """
    underwriting_exception: Optional[UnderwritingException]
    """
    If an exception to the usual underwriting criteria was made for this application, details about the exception must be provided. Exceptions should only be granted in rare circumstances, in consultation with Stripe Compliance.
    """

    @classmethod
    def _cls_correct(
        cls,
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordCorrectParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def correct(
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordCorrectParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        ...

    @overload
    def correct(
        self, **params: Unpack["CreditUnderwritingRecordCorrectParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        ...

    @class_method_variant("_cls_correct")
    def correct(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditUnderwritingRecordCorrectParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_correct_async(
        cls,
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordCorrectParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            await cls._static_request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def correct_async(
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordCorrectParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        ...

    @overload
    async def correct_async(
        self, **params: Unpack["CreditUnderwritingRecordCorrectParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        ...

    @class_method_variant("_cls_correct_async")
    async def correct_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditUnderwritingRecordCorrectParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object to correct mistakes.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/correct".format(
                    credit_underwriting_record=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create_from_application(
        cls,
        **params: Unpack[
            "CreditUnderwritingRecordCreateFromApplicationParams"
        ],
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                params=params,
            ),
        )

    @classmethod
    async def create_from_application_async(
        cls,
        **params: Unpack[
            "CreditUnderwritingRecordCreateFromApplicationParams"
        ],
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object with information about a credit application submission.
        """
        return cast(
            "CreditUnderwritingRecord",
            await cls._static_request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_application",
                params=params,
            ),
        )

    @classmethod
    def create_from_proactive_review(
        cls,
        **params: Unpack[
            "CreditUnderwritingRecordCreateFromProactiveReviewParams"
        ],
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                params=params,
            ),
        )

    @classmethod
    async def create_from_proactive_review_async(
        cls,
        **params: Unpack[
            "CreditUnderwritingRecordCreateFromProactiveReviewParams"
        ],
    ) -> "CreditUnderwritingRecord":
        """
        Creates a CreditUnderwritingRecord object from an underwriting decision coming from a proactive review of an existing accountholder.
        """
        return cast(
            "CreditUnderwritingRecord",
            await cls._static_request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/create_from_proactive_review",
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["CreditUnderwritingRecordListParams"]
    ) -> ListObject["CreditUnderwritingRecord"]:
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["CreditUnderwritingRecordListParams"]
    ) -> ListObject["CreditUnderwritingRecord"]:
        """
        Retrieves a list of CreditUnderwritingRecord objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
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
        **params: Unpack["CreditUnderwritingRecordReportDecisionParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            cls._static_request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def report_decision(
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordReportDecisionParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        ...

    @overload
    def report_decision(
        self, **params: Unpack["CreditUnderwritingRecordReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        ...

    @class_method_variant("_cls_report_decision")
    def report_decision(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditUnderwritingRecordReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            self._request(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_report_decision_async(
        cls,
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordReportDecisionParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            await cls._static_request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(
                        credit_underwriting_record
                    )
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def report_decision_async(
        credit_underwriting_record: str,
        **params: Unpack["CreditUnderwritingRecordReportDecisionParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        ...

    @overload
    async def report_decision_async(
        self, **params: Unpack["CreditUnderwritingRecordReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        ...

    @class_method_variant("_cls_report_decision_async")
    async def report_decision_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["CreditUnderwritingRecordReportDecisionParams"]
    ) -> "CreditUnderwritingRecord":
        """
        Update a CreditUnderwritingRecord object from a decision made on a credit application.
        """
        return cast(
            "CreditUnderwritingRecord",
            await self._request_async(
                "post",
                "/v1/issuing/credit_underwriting_records/{credit_underwriting_record}/report_decision".format(
                    credit_underwriting_record=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["CreditUnderwritingRecordRetrieveParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["CreditUnderwritingRecordRetrieveParams"],
    ) -> "CreditUnderwritingRecord":
        """
        Retrieves a CreditUnderwritingRecord object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "application": Application,
        "credit_user": CreditUser,
        "decision": Decision,
        "underwriting_exception": UnderwritingException,
    }
