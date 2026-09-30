# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ActivityLogListParams(TypedDict):
    action_groups: NotRequired[
        List[
            Union[
                Literal[
                    "account_security",
                    "api_key",
                    "authentication",
                    "issuing",
                    "payout",
                    "scim",
                    "sso",
                    "user_access",
                    "user_invite",
                    "user_profile",
                    "user_roles",
                ],
                str,
            ]
        ]
    ]
    """
    Filter results to only include activity logs for the specified action group types.
    """
    actions: NotRequired[
        List[
            Union[
                Literal[
                    "anomaly_detection_settings_updated",
                    "api_key_created",
                    "api_key_deleted",
                    "api_key_updated",
                    "api_key_viewed",
                    "issuing_activated",
                    "issuing_balance_transfer_created",
                    "issuing_cardholder_created",
                    "issuing_cardholder_updated",
                    "issuing_card_created",
                    "issuing_card_sensitive_details_viewed",
                    "issuing_card_updated",
                    "issuing_dispute_created",
                    "issuing_dispute_submitted",
                    "issuing_dispute_updated",
                    "manual_payouts_disabled",
                    "manual_payouts_enabled",
                    "payout_destination_added",
                    "payout_destination_removed",
                    "payout_destination_updated",
                    "payout_schedule_edits_disabled",
                    "payout_schedule_edits_enabled",
                    "scim_group_deleted",
                    "scim_group_member_added",
                    "scim_group_member_removed",
                    "scim_group_roles_updated",
                    "scim_group_updated",
                    "sso_domain_verified",
                    "sso_settings_created",
                    "sso_settings_deleted",
                    "sso_settings_updated",
                    "two_step_authentication_mandate_disabled",
                    "two_step_authentication_mandate_enabled",
                    "user_access_started",
                    "user_auth_challenge_failed",
                    "user_email_changed",
                    "user_email_verified",
                    "user_express_phone_number_changed",
                    "user_google_account_connected",
                    "user_google_account_disconnected",
                    "user_invite_accepted",
                    "user_invite_created",
                    "user_invite_deleted",
                    "user_passkey_added",
                    "user_passkey_removed",
                    "user_passkey_updated",
                    "user_passkey_upgraded",
                    "user_password_changed",
                    "user_password_initialized",
                    "user_password_reset_failed",
                    "user_password_reset_requested",
                    "user_password_reset_succeeded",
                    "user_roles_deleted",
                    "user_roles_updated",
                    "user_two_step_authentication_backup_code_used",
                    "user_two_step_authentication_method_added",
                    "user_two_step_authentication_method_removed",
                    "user_two_step_authentication_method_reset",
                    "user_two_step_authentication_method_updated",
                    "user_two_step_authentication_reset_requested",
                ],
                str,
            ]
        ]
    ]
    """
    Filter results to only include activity logs for the specified action types.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page.
    """
