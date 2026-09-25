# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class ActivityLog(StripeObject):
    """
    An activity log records a single action performed on an account.
    """

    OBJECT_NAME: ClassVar[Literal["v2.iam.activity_log"]] = (
        "v2.iam.activity_log"
    )

    class Actor(StripeObject):
        class ApiKey(StripeObject):
            id: str
            """
            Unique identifier of the API key.
            """

        class User(StripeObject):
            email: str
            """
            Email address of the user.
            """

        api_key: Optional[ApiKey]
        """
        Set when the actor is an API key.
        """
        type: Literal["api_key", "stripe_action", "user"]
        """
        The type of actor.
        """
        user: Optional[User]
        """
        Set when the actor is a user.
        """
        _inner_class_types = {"api_key": ApiKey, "user": User}

    class Details(StripeObject):
        class AccountSecurity(StripeObject):
            class NewAnomalySettings(StripeObject):
                dormant_api_key_protection_enabled: Optional[bool]
                """
                Whether dormant API key protection is enabled.
                """
                money_movement_anomaly_detection_enabled: Optional[bool]
                """
                Whether money movement anomaly detection is enabled.
                """
                request_level_anomaly_detection_enabled: Optional[bool]
                """
                Whether request-level anomaly detection is enabled.
                """

            class OldAnomalySettings(StripeObject):
                dormant_api_key_protection_enabled: Optional[bool]
                """
                Whether dormant API key protection is enabled.
                """
                money_movement_anomaly_detection_enabled: Optional[bool]
                """
                Whether money movement anomaly detection is enabled.
                """
                request_level_anomaly_detection_enabled: Optional[bool]
                """
                Whether request-level anomaly detection is enabled.
                """

            new_anomaly_settings: Optional[NewAnomalySettings]
            """
            Anomaly detection settings after the change.
            """
            old_anomaly_settings: Optional[OldAnomalySettings]
            """
            Anomaly detection settings before the change.
            """
            _inner_class_types = {
                "new_anomaly_settings": NewAnomalySettings,
                "old_anomaly_settings": OldAnomalySettings,
            }

        class ApiKey(StripeObject):
            class ManagedBy(StripeObject):
                class Application(StripeObject):
                    id: str
                    """
                    Identifier of the application.
                    """

                application: Optional[Application]
                """
                An application.
                """
                type: Union[Literal["application"], str]
                """
                The type of entity.
                """
                _inner_class_types = {"application": Application}

            created: str
            """
            Timestamp when the API key was created.
            """
            expires_at: Optional[str]
            """
            Timestamp when the API key expires.
            """
            id: str
            """
            Unique identifier of the API key.
            """
            ip_allowlist: List[str]
            """
            List of IP addresses allowed to use this API key.
            """
            managed_by: Optional[ManagedBy]
            """
            Information about the entity managing this API key.
            """
            name: Optional[str]
            """
            Name of the API key.
            """
            new_key: Optional[str]
            """
            Unique identifier of the new API key, set when this key was rotated.
            """
            note: Optional[str]
            """
            Note or description for the API key.
            """
            type: Literal["publishable_key", "secret_key"]
            """
            Type of the API key.
            """
            _inner_class_types = {"managed_by": ManagedBy}

        class Authentication(StripeObject):
            backup_email: Optional[str]
            """
            Backup email address involved in the authentication.
            """
            challenge_type: Optional[
                Union[
                    Literal[
                        "external_account_code",
                        "oauth",
                        "previous_account_number",
                        "reverse_sms",
                        "sms",
                        "stripe_identity",
                        "totp",
                        "webauthn",
                    ],
                    str,
                ]
            ]
            """
            Type of challenge used for the authentication.
            """
            surface: Optional[Union[Literal["dashboard", "express"], str]]
            """
            Surface where the authentication occurred.
            """
            target_email: Optional[str]
            """
            Target email address involved in the authentication.
            """

        class Scim(StripeObject):
            group_name: str
            """
            Name of the SCIM group.
            """
            new_roles: List[str]
            """
            Group roles after the change; only set for the group roles-updated action (scim_group_roles_updated).
            """
            old_roles: List[str]
            """
            Group roles before the change; only set for the group roles-updated action (scim_group_roles_updated).
            """
            role_assigned_context: Optional[str]
            """
            The context the roles were assigned in.
            """
            user_email: Optional[str]
            """
            Email address of the affected member.
            """

        class Sso(StripeObject):
            mandate: Optional[Literal["off", "optional", "required"]]
            """
            SSO enforcement level.
            """

        class UserAccess(StripeObject):
            class Authentication(StripeObject):
                class PrimaryFactor(StripeObject):
                    sso_provider: Optional[str]
                    """
                    SSO provider for the authentication factor.
                    """
                    type: Union[
                        Literal[
                            "backup_code",
                            "email_code",
                            "oauth",
                            "passkey",
                            "password",
                            "phone_code",
                            "saml",
                            "sms",
                            "totp",
                            "web_authn",
                        ],
                        str,
                    ]
                    """
                    Type of authentication factor.
                    """

                class SecondaryFactor(StripeObject):
                    sso_provider: Optional[str]
                    """
                    SSO provider for the authentication factor.
                    """
                    type: Union[
                        Literal[
                            "backup_code",
                            "email_code",
                            "oauth",
                            "passkey",
                            "password",
                            "phone_code",
                            "saml",
                            "sms",
                            "totp",
                            "web_authn",
                        ],
                        str,
                    ]
                    """
                    Type of authentication factor.
                    """

                primary_factor: PrimaryFactor
                """
                Primary authentication factor.
                """
                secondary_factors: List[SecondaryFactor]
                """
                Secondary authentication factors.
                """
                _inner_class_types = {
                    "primary_factor": PrimaryFactor,
                    "secondary_factors": SecondaryFactor,
                }

            class DashboardClient(StripeObject):
                browser: str
                """
                Browser used for the user access action.
                """
                browser_version: str
                """
                Browser version used for the user access action.
                """
                device_type: str
                """
                Device type used for the user access action.
                """
                os: str
                """
                Operating system used for the user access action.
                """

            class Network(StripeObject):
                city: str
                """
                City for the user access action.
                """
                country: str
                """
                Country for the user access action.
                """
                ip_address: str
                """
                IP address for the user access action.
                """
                region: str
                """
                Region for the user access action.
                """

            class Risk(StripeObject):
                class Signal(StripeObject):
                    class NovelDevice(StripeObject):
                        pass

                    novel_device: Optional[NovelDevice]
                    """
                    The user access action used a novel device.
                    """
                    type: Union[Literal["novel_device"], str]
                    """
                    Type of risk signal.
                    """
                    _inner_class_types = {"novel_device": NovelDevice}

                level: Union[Literal["high", "low", "medium"], str]
                """
                Risk level for the user access action.
                """
                signals: List[Signal]
                """
                Risk signals for the user access action.
                """
                _inner_class_types = {"signals": Signal}

            authentication: Authentication
            """
            Authentication details for the user access action.
            """
            dashboard_client: Optional[DashboardClient]
            """
            Dashboard client details for the user access action.
            """
            expires_at: str
            """
            Timestamp when the user access expires.
            """
            network: Network
            """
            Network details for the user access action.
            """
            risk: Risk
            """
            Risk details for the user access action.
            """
            roles: List[str]
            """
            Roles associated with the user access action.
            """
            session_fingerprint: str
            """
            Session fingerprint for the user access action.
            """
            surface: Union[Literal["dashboard", "express"], str]
            """
            Surface where the user access action started.
            """
            _inner_class_types = {
                "authentication": Authentication,
                "dashboard_client": DashboardClient,
                "network": Network,
                "risk": Risk,
            }

        class UserInvite(StripeObject):
            invited_user_email: str
            """
            Email address of the invited user.
            """
            roles: List[str]
            """
            Roles assigned to the invited user.
            """

        class UserProfile(StripeObject):
            new_email: Optional[str]
            """
            Email address after the change.
            """
            new_redacted_phone_number: Optional[str]
            """
            Redacted phone number after the change.
            """
            old_email: Optional[str]
            """
            Email address before the change.
            """
            old_redacted_phone_number: Optional[str]
            """
            Redacted phone number before the change.
            """

        class UserRoles(StripeObject):
            new_roles: List[str]
            """
            Roles the user has after the change.
            """
            old_roles: List[str]
            """
            Roles the user had before the change.
            """
            source: Union[Literal["dashboard", "scim", "sso"], str]
            """
            Source of the role change.
            """
            user_email: str
            """
            Email address of the user whose roles were changed.
            """

        account_security: Optional[AccountSecurity]
        """
        Details of an account security action.
        """
        api_key: Optional[ApiKey]
        """
        Details of an API key action.
        """
        authentication: Optional[Authentication]
        """
        Details of an authentication action.
        """
        scim: Optional[Scim]
        """
        Details of a SCIM action.
        """
        sso: Optional[Sso]
        """
        Details of an SSO action.
        """
        type: Union[
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
        """
        The action group type of the activity log entry.
        """
        user_access: Optional[UserAccess]
        """
        Details of a user access action.
        """
        user_invite: Optional[UserInvite]
        """
        Details of a user invite action.
        """
        user_profile: Optional[UserProfile]
        """
        Details of a user profile action.
        """
        user_roles: Optional[UserRoles]
        """
        Details of a user role change action.
        """
        _inner_class_types = {
            "account_security": AccountSecurity,
            "api_key": ApiKey,
            "authentication": Authentication,
            "scim": Scim,
            "sso": Sso,
            "user_access": UserAccess,
            "user_invite": UserInvite,
            "user_profile": UserProfile,
            "user_roles": UserRoles,
        }

    class RelatedObject(StripeObject):
        id: str
        """
        Unique identifier of the object.
        """
        type: Union[
            Literal[
                "balance_transfer",
                "bank_account",
                "blockchain_address",
                "card",
                "issuing.card",
                "issuing.cardholder",
                "issuing.dispute",
            ],
            str,
        ]
        """
        Type of the object.
        """

    class Request(StripeObject):
        id: str
        """
        ID of the API request.
        """

    actor: Actor
    """
    The actor that performed the action.
    """
    context: str
    """
    The account on which the action was performed.
    """
    created: str
    """
    Timestamp when the activity log entry was created.
    """
    details: Details
    """
    Action-specific details of the activity log entry.
    """
    id: str
    """
    Unique identifier of the activity log entry.
    """
    livemode: bool
    """
    Whether the action was performed in live mode.
    """
    object: Literal["v2.iam.activity_log"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    related_object: Optional[RelatedObject]
    """
    The object related to the activity log entry.
    """
    request: Optional[Request]
    """
    The API request that instigated the action.
    """
    type: Union[
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
    """
    The type of action that was performed.
    """
    _inner_class_types = {
        "actor": Actor,
        "details": Details,
        "related_object": RelatedObject,
        "request": Request,
    }
