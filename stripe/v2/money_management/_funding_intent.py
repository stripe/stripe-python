# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class FundingIntent(StripeObject):
    """
    A FundingIntent represents the lifecycle of adding funds to a FinancialAccount.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.funding_intent"]] = (
        "v2.money_management.funding_intent"
    )

    class Check(StripeObject):
        back_image: Optional[str]
        """
        The ID of a File containing the back image of the check.
        """
        front_image: Optional[str]
        """
        The ID of a File containing the front image of the check.
        """

    class LatestAttempt(StripeObject):
        inbound_funding: str
        """
        The ID of the InboundFunding created by the attempt.
        """
        type: Union[Literal["inbound_funding"], str]
        """
        The type of underlying money movement created by the attempt.
        """

    class NextAction(StripeObject):
        class HandleFailure(StripeObject):
            reason: Union[
                Literal[
                    "insufficient_funds", "not_authorized", "stripe_rejected"
                ],
                str,
            ]
            """
            The reason the attempt failed.
            """
            retryable: bool
            """
            Whether you can retry the FundingIntent.
            """

        class ProvideNewCheck(StripeObject):
            description: str
            """
            A human-readable description of the factor.
            """
            reason: Union[
                Literal[
                    "amount_variance_exceeds_threshold",
                    "amount_variance_nearing_threshold",
                    "back_image_not_processed",
                    "back_looks_like_front",
                    "back_signature_not_detected",
                    "bad_payee_name",
                    "date_invalid",
                    "date_in_future",
                    "date_older_than_one_year",
                    "date_older_than_six_months",
                    "duplicate_check",
                    "endorsement_missing",
                    "folded_or_torn_corners",
                    "front_image_dimension_mismatch",
                    "front_image_not_processed",
                    "front_image_too_dark",
                    "front_image_too_light",
                    "front_image_too_small",
                    "front_signature_not_detected",
                    "high_risk",
                    "image_cannot_be_processed",
                    "image_out_of_focus",
                    "invalid_check_type",
                    "invalid_routing_number",
                    "not_accepted_please_contact",
                    "no_routing_number_detected",
                    "safe_harbor_phrase_missing",
                    "savings_bond_detected",
                    "travelers_check",
                    "unable_to_read_account_info",
                ],
                str,
            ]
            """
            A machine-readable reason for the factor.
            """

        class ProvideNewImages(StripeObject):
            class AmountIssue(StripeObject):
                description: str
                """
                A human-readable description of the factor.
                """
                reason: Union[
                    Literal[
                        "amount_variance_exceeds_threshold",
                        "amount_variance_nearing_threshold",
                        "back_image_not_processed",
                        "back_looks_like_front",
                        "back_signature_not_detected",
                        "bad_payee_name",
                        "date_invalid",
                        "date_in_future",
                        "date_older_than_one_year",
                        "date_older_than_six_months",
                        "duplicate_check",
                        "endorsement_missing",
                        "folded_or_torn_corners",
                        "front_image_dimension_mismatch",
                        "front_image_not_processed",
                        "front_image_too_dark",
                        "front_image_too_light",
                        "front_image_too_small",
                        "front_signature_not_detected",
                        "high_risk",
                        "image_cannot_be_processed",
                        "image_out_of_focus",
                        "invalid_check_type",
                        "invalid_routing_number",
                        "not_accepted_please_contact",
                        "no_routing_number_detected",
                        "safe_harbor_phrase_missing",
                        "savings_bond_detected",
                        "travelers_check",
                        "unable_to_read_account_info",
                    ],
                    str,
                ]
                """
                A machine-readable reason for the factor.
                """

            class BackImage(StripeObject):
                description: str
                """
                A human-readable description of the factor.
                """
                reason: Union[
                    Literal[
                        "amount_variance_exceeds_threshold",
                        "amount_variance_nearing_threshold",
                        "back_image_not_processed",
                        "back_looks_like_front",
                        "back_signature_not_detected",
                        "bad_payee_name",
                        "date_invalid",
                        "date_in_future",
                        "date_older_than_one_year",
                        "date_older_than_six_months",
                        "duplicate_check",
                        "endorsement_missing",
                        "folded_or_torn_corners",
                        "front_image_dimension_mismatch",
                        "front_image_not_processed",
                        "front_image_too_dark",
                        "front_image_too_light",
                        "front_image_too_small",
                        "front_signature_not_detected",
                        "high_risk",
                        "image_cannot_be_processed",
                        "image_out_of_focus",
                        "invalid_check_type",
                        "invalid_routing_number",
                        "not_accepted_please_contact",
                        "no_routing_number_detected",
                        "safe_harbor_phrase_missing",
                        "savings_bond_detected",
                        "travelers_check",
                        "unable_to_read_account_info",
                    ],
                    str,
                ]
                """
                A machine-readable reason for the factor.
                """

            class FrontImage(StripeObject):
                description: str
                """
                A human-readable description of the factor.
                """
                reason: Union[
                    Literal[
                        "amount_variance_exceeds_threshold",
                        "amount_variance_nearing_threshold",
                        "back_image_not_processed",
                        "back_looks_like_front",
                        "back_signature_not_detected",
                        "bad_payee_name",
                        "date_invalid",
                        "date_in_future",
                        "date_older_than_one_year",
                        "date_older_than_six_months",
                        "duplicate_check",
                        "endorsement_missing",
                        "folded_or_torn_corners",
                        "front_image_dimension_mismatch",
                        "front_image_not_processed",
                        "front_image_too_dark",
                        "front_image_too_light",
                        "front_image_too_small",
                        "front_signature_not_detected",
                        "high_risk",
                        "image_cannot_be_processed",
                        "image_out_of_focus",
                        "invalid_check_type",
                        "invalid_routing_number",
                        "not_accepted_please_contact",
                        "no_routing_number_detected",
                        "safe_harbor_phrase_missing",
                        "savings_bond_detected",
                        "travelers_check",
                        "unable_to_read_account_info",
                    ],
                    str,
                ]
                """
                A machine-readable reason for the factor.
                """

            amount_issues: List[AmountIssue]
            """
            Issues detected in the check amount.
            """
            back_image: List[BackImage]
            """
            Issues detected in the back image of the check.
            """
            front_image: List[FrontImage]
            """
            Issues detected in the front image of the check.
            """
            _inner_class_types = {
                "amount_issues": AmountIssue,
                "back_image": BackImage,
                "front_image": FrontImage,
            }

        handle_failure: Optional[HandleFailure]
        """
        Details for handling a failed attempt.
        """
        provide_new_check: Optional[ProvideNewCheck]
        """
        The reason that you must provide a different check.
        """
        provide_new_images: Optional[ProvideNewImages]
        """
        Issues that require corrected check images or an updated amount.
        """
        type: Union[
            Literal[
                "handle_failure",
                "provide_new_check",
                "provide_new_images",
                "requires_check_images",
            ],
            str,
        ]
        """
        The type of action required.
        """
        _inner_class_types = {
            "handle_failure": HandleFailure,
            "provide_new_check": ProvideNewCheck,
            "provide_new_images": ProvideNewImages,
        }

    class NextConfirmation(StripeObject):
        class RequiresReview(StripeObject):
            class Factor(StripeObject):
                description: str
                """
                A human-readable description of the factor.
                """
                reason: Union[
                    Literal[
                        "amount_variance_exceeds_threshold",
                        "amount_variance_nearing_threshold",
                        "back_image_not_processed",
                        "back_looks_like_front",
                        "back_signature_not_detected",
                        "bad_payee_name",
                        "date_invalid",
                        "date_in_future",
                        "date_older_than_one_year",
                        "date_older_than_six_months",
                        "duplicate_check",
                        "endorsement_missing",
                        "folded_or_torn_corners",
                        "front_image_dimension_mismatch",
                        "front_image_not_processed",
                        "front_image_too_dark",
                        "front_image_too_light",
                        "front_image_too_small",
                        "front_signature_not_detected",
                        "high_risk",
                        "image_cannot_be_processed",
                        "image_out_of_focus",
                        "invalid_check_type",
                        "invalid_routing_number",
                        "not_accepted_please_contact",
                        "no_routing_number_detected",
                        "safe_harbor_phrase_missing",
                        "savings_bond_detected",
                        "travelers_check",
                        "unable_to_read_account_info",
                    ],
                    str,
                ]
                """
                A machine-readable reason for the factor.
                """

            factors: List[Factor]
            """
            Factors that require review.
            """
            _inner_class_types = {"factors": Factor}

        requires_review: Optional[RequiresReview]
        """
        Factors to review before confirming the FundingIntent.
        """
        type: Union[Literal["requires_review"], str]
        """
        The type of confirmation required.
        """
        _inner_class_types = {"requires_review": RequiresReview}

    class SettlementTiming(StripeObject):
        delay_days_override: Optional[int]
        """
        The number of days to delay the availability of funds after processing completes.
        """

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Union[Literal["canceled_by_user"], str]
            """
            The reason the FundingIntent was canceled.
            """

        canceled: Optional[Canceled]
        """
        Details present when the FundingIntent is canceled.
        """
        _inner_class_types = {"canceled": Canceled}

    class StatusTransitions(StripeObject):
        canceled_at: Optional[str]
        """
        Time at which the FundingIntent entered the `canceled` status.
        """
        processing_at: Optional[str]
        """
        Time at which the FundingIntent entered the `processing` status.
        """
        requires_action_at: Optional[str]
        """
        Time at which the FundingIntent entered the `requires_action` status.
        """
        requires_confirmation_at: Optional[str]
        """
        Time at which the FundingIntent entered the `requires_confirmation` status.
        """
        succeeded_at: Optional[str]
        """
        Time at which the FundingIntent entered the `succeeded` status.
        """
        validating_at: Optional[str]
        """
        Time at which the FundingIntent entered the `validating` status.
        """

    class To(StripeObject):
        currency: str
        """
        The currency of the destination FinancialAccount balance.
        """
        financial_account: str
        """
        The ID of the FinancialAccount that receives the funds.
        """

    amount: Amount
    """
    The amount to add to the destination.
    """
    cancelable: bool
    """
    Whether you can cancel the FundingIntent.
    """
    check: Optional[Check]
    """
    Details for a check FundingIntent.
    """
    confirmation_method: Union[Literal["automatic", "manual"], str]
    """
    How the FundingIntent is confirmed after validation.
    """
    created: str
    """
    Time at which the FundingIntent was created.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the FundingIntent.
    """
    id: str
    """
    Unique identifier for the FundingIntent.
    """
    latest_attempt: Optional[LatestAttempt]
    """
    Details about the latest underlying money movement attempt.
    """
    livemode: bool
    """
    Whether the FundingIntent exists in live mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs attached to the FundingIntent.
    """
    next_action: Optional[NextAction]
    """
    The action required to continue processing the FundingIntent.
    """
    next_confirmation: Optional[NextConfirmation]
    """
    The information to review before confirming the FundingIntent.
    """
    object: Literal["v2.money_management.funding_intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    settlement_timing: Optional[SettlementTiming]
    """
    Controls when the funds become available after processing.
    """
    status: Union[
        Literal[
            "canceled",
            "processing",
            "requires_action",
            "requires_confirmation",
            "succeeded",
            "validating",
        ],
        str,
    ]
    """
    The current status of the FundingIntent.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details about the current status.
    """
    status_transitions: StatusTransitions
    """
    Timestamps for the FundingIntent's status transitions.
    """
    to: To
    """
    The destination for the funds.
    """
    type: Union[Literal["check"], str]
    """
    The type of FundingIntent.
    """
    _inner_class_types = {
        "check": Check,
        "latest_attempt": LatestAttempt,
        "next_action": NextAction,
        "next_confirmation": NextConfirmation,
        "settlement_timing": SettlementTiming,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "to": To,
    }
