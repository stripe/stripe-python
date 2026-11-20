# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
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

        class StripeAction(StripeObject):
            display_name: str
            """
            Public display name captured when the action occurs.
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
        stripe_action: Optional[StripeAction]
        """
        Set when a display name is available for an action performed by Stripe.
        """
        type: Literal["api_key", "stripe_action", "user"]
        """
        The type of actor.
        """
        user: Optional[User]
        """
        Set when the actor is a user.
        """
        _inner_class_types = {
            "api_key": ApiKey,
            "stripe_action": StripeAction,
            "user": User,
        }

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

        class Connect(StripeObject):
            class Application(StripeObject):
                id: str
                """
                Identifier of the application.
                """

            class NewExpressBrandingSettings(StripeObject):
                border_radius: Optional[str]
                """
                Border radius for the Express Dashboard.
                """
                primary_button_background_color: Optional[str]
                """
                Primary button background color for the Express Dashboard.
                """
                primary_color: Optional[str]
                """
                Primary color for the Express Dashboard.
                """
                secondary_button_background_color: Optional[str]
                """
                Secondary button background color for the Express Dashboard.
                """

            class NewSettings(StripeObject):
                business_name: Optional[str]
                """
                The display name shown on the onboarding experience and Dashboard. This is different from the business legal name.
                """
                copy_platform_branding_to_new_connected_accounts: Optional[
                    bool
                ]
                """
                Whether platform branding is copied to new connected accounts. These also appear on invoices, receipts, and other Stripe products.
                """
                hide_onboarding_support_email: Optional[bool]
                """
                Whether the support email is hidden on onboarding surfaces.
                """
                hide_onboarding_support_phone: Optional[bool]
                """
                Whether the support phone number is hidden on onboarding surfaces.
                """
                hide_onboarding_support_url: Optional[bool]
                """
                Whether the support URL is hidden on onboarding surfaces.
                """
                icon: Optional[str]
                """
                Identifier of the icon file (file_* ID).
                """
                logo: Optional[str]
                """
                Identifier of the logo file (file_* ID).
                """
                payout_statement_descriptor: Optional[str]
                """
                The platform's default payout statement descriptor. It appears on the bank statements of the platform's connected accounts for their payouts.
                """
                primary_color: Optional[str]
                """
                A CSS hex color value representing the primary branding color, applied to the onboarding experience and the Stripe Dashboard.
                """
                secondary_color: Optional[str]
                """
                A CSS hex color value representing the secondary branding color, applied to the onboarding experience and the Stripe Dashboard.
                """

            class OldExpressBrandingSettings(StripeObject):
                border_radius: Optional[str]
                """
                Border radius for the Express Dashboard.
                """
                primary_button_background_color: Optional[str]
                """
                Primary button background color for the Express Dashboard.
                """
                primary_color: Optional[str]
                """
                Primary color for the Express Dashboard.
                """
                secondary_button_background_color: Optional[str]
                """
                Secondary button background color for the Express Dashboard.
                """

            class OldSettings(StripeObject):
                business_name: Optional[str]
                """
                The display name shown on the onboarding experience and Dashboard. This is different from the business legal name.
                """
                copy_platform_branding_to_new_connected_accounts: Optional[
                    bool
                ]
                """
                Whether platform branding is copied to new connected accounts. These also appear on invoices, receipts, and other Stripe products.
                """
                hide_onboarding_support_email: Optional[bool]
                """
                Whether the support email is hidden on onboarding surfaces.
                """
                hide_onboarding_support_phone: Optional[bool]
                """
                Whether the support phone number is hidden on onboarding surfaces.
                """
                hide_onboarding_support_url: Optional[bool]
                """
                Whether the support URL is hidden on onboarding surfaces.
                """
                icon: Optional[str]
                """
                Identifier of the icon file (file_* ID).
                """
                logo: Optional[str]
                """
                Identifier of the logo file (file_* ID).
                """
                payout_statement_descriptor: Optional[str]
                """
                The platform's default payout statement descriptor. It appears on the bank statements of the platform's connected accounts for their payouts.
                """
                primary_color: Optional[str]
                """
                A CSS hex color value representing the primary branding color, applied to the onboarding experience and the Stripe Dashboard.
                """
                secondary_color: Optional[str]
                """
                A CSS hex color value representing the secondary branding color, applied to the onboarding experience and the Stripe Dashboard.
                """

            application: Optional[Application]
            """
            The Connect application.
            """
            new_express_branding_settings: Optional[NewExpressBrandingSettings]
            """
            Express Dashboard branding settings after the change. Set for the connect_express_branding_updated action.
            """
            new_settings: Optional[NewSettings]
            """
            Connect settings after the change. Set for the connect_settings_updated action.
            """
            old_express_branding_settings: Optional[OldExpressBrandingSettings]
            """
            Express Dashboard branding settings before the change. Set for the connect_express_branding_updated action.
            """
            old_settings: Optional[OldSettings]
            """
            Connect settings before the change. Set for the connect_settings_updated action.
            """
            site_link_route: Optional[
                Union[
                    Literal[
                        "account_management",
                        "balances",
                        "documents",
                        "financial_accounts",
                        "issuing_card_transactions",
                        "notification_banner",
                        "payments",
                        "payouts",
                    ],
                    str,
                ]
            ]
            """
            The site link route. Set for the connect_site_link_updated action.
            """
            _inner_class_types = {
                "application": Application,
                "new_express_branding_settings": NewExpressBrandingSettings,
                "new_settings": NewSettings,
                "old_express_branding_settings": OldExpressBrandingSettings,
                "old_settings": OldSettings,
            }

        class DataExport(StripeObject):
            type: str
            """
            Name of export type.
            """

        class EventDestination(StripeObject):
            class NewConfiguration(StripeObject):
                class AmazonEventbridge(StripeObject):
                    aws_account_id: str
                    """
                    AWS account ID configured for the event destination.
                    """
                    aws_event_source_arn: str
                    """
                    ARN of the AWS event source configured for the event destination.
                    """
                    aws_region: str
                    """
                    AWS region configured for the event destination.
                    """

                class AzureEventGrid(StripeObject):
                    azure_partner_topic_name: str
                    """
                    Azure partner topic name configured for the event destination.
                    """
                    azure_region: str
                    """
                    Azure region configured for the event destination.
                    """
                    azure_resource_group_name: str
                    """
                    Azure resource group name configured for the event destination.
                    """
                    azure_subscription_id: str
                    """
                    Azure subscription ID configured for the event destination.
                    """

                class WebhookEndpoint(StripeObject):
                    url: str
                    """
                    URL configured for the webhook endpoint.
                    """

                amazon_eventbridge: Optional[AmazonEventbridge]
                """
                Amazon EventBridge configuration.
                """
                azure_event_grid: Optional[AzureEventGrid]
                """
                Azure Event Grid configuration.
                """
                enabled_events: List[str]
                """
                Event types subscribed to by the destination. ["*"] subscribes to all V1 webhook events.
                """
                events_from: List[str]
                """
                Event source selectors: @self, @accounts, @organization_members, or @organization_members/@accounts.
                """
                status: Union[Literal["disabled", "enabled"], str]
                """
                Status of the event destination.
                """
                webhook_endpoint: Optional[WebhookEndpoint]
                """
                Webhook endpoint configuration.
                """
                _inner_class_types = {
                    "amazon_eventbridge": AmazonEventbridge,
                    "azure_event_grid": AzureEventGrid,
                    "webhook_endpoint": WebhookEndpoint,
                }

            class OldConfiguration(StripeObject):
                class AmazonEventbridge(StripeObject):
                    aws_account_id: str
                    """
                    AWS account ID configured for the event destination.
                    """
                    aws_event_source_arn: str
                    """
                    ARN of the AWS event source configured for the event destination.
                    """
                    aws_region: str
                    """
                    AWS region configured for the event destination.
                    """

                class AzureEventGrid(StripeObject):
                    azure_partner_topic_name: str
                    """
                    Azure partner topic name configured for the event destination.
                    """
                    azure_region: str
                    """
                    Azure region configured for the event destination.
                    """
                    azure_resource_group_name: str
                    """
                    Azure resource group name configured for the event destination.
                    """
                    azure_subscription_id: str
                    """
                    Azure subscription ID configured for the event destination.
                    """

                class WebhookEndpoint(StripeObject):
                    url: str
                    """
                    URL configured for the webhook endpoint.
                    """

                amazon_eventbridge: Optional[AmazonEventbridge]
                """
                Amazon EventBridge configuration.
                """
                azure_event_grid: Optional[AzureEventGrid]
                """
                Azure Event Grid configuration.
                """
                enabled_events: List[str]
                """
                Event types subscribed to by the destination. ["*"] subscribes to all V1 webhook events.
                """
                events_from: List[str]
                """
                Event source selectors: @self, @accounts, @organization_members, or @organization_members/@accounts.
                """
                status: Union[Literal["disabled", "enabled"], str]
                """
                Status of the event destination.
                """
                webhook_endpoint: Optional[WebhookEndpoint]
                """
                Webhook endpoint configuration.
                """
                _inner_class_types = {
                    "amazon_eventbridge": AmazonEventbridge,
                    "azure_event_grid": AzureEventGrid,
                    "webhook_endpoint": WebhookEndpoint,
                }

            new_configuration: Optional[NewConfiguration]
            """
            Configuration after the change. Set for added and updated actions, absent for removed actions.
            """
            old_configuration: Optional[OldConfiguration]
            """
            Configuration before the change. Set for updated and removed actions, absent for added actions.
            """
            type: Union[
                Literal[
                    "amazon_eventbridge",
                    "azure_event_grid",
                    "webhook_endpoint",
                ],
                str,
            ]
            """
            Type of the event destination.
            """
            _inner_class_types = {
                "new_configuration": NewConfiguration,
                "old_configuration": OldConfiguration,
            }

        class Radar(StripeObject):
            class NewRule(StripeObject):
                action: Union[
                    Literal[
                        "allow",
                        "block",
                        "block_fa_outbound",
                        "manual_review",
                        "payout_pause",
                        "raise_review",
                        "request_credentials",
                        "resolve_dispute",
                    ],
                    str,
                ]
                """
                Action performed when the rule matches.
                """
                enabled: Optional[bool]
                """
                Whether the rule is enabled.
                """
                id: str
                """
                Identifier of the rule.
                """
                objective: Optional[str]
                """
                Objective of the rule.
                """
                predicate: Optional[str]
                """
                Rule expression evaluated to determine whether the rule matches.
                """
                rollout_percentage: Optional[Decimal]
                """
                Percentage of matching traffic to which the rule applies, between 0 and 100, serialized as a decimal string.
                """
                type: Optional[Union[Literal["account", "payment"], str]]
                """
                Type of entity evaluated by the rule.
                """
                _field_encodings = {"rollout_percentage": "decimal_string"}

            class OldRule(StripeObject):
                action: Union[
                    Literal[
                        "allow",
                        "block",
                        "block_fa_outbound",
                        "manual_review",
                        "payout_pause",
                        "raise_review",
                        "request_credentials",
                        "resolve_dispute",
                    ],
                    str,
                ]
                """
                Action performed when the rule matches.
                """
                enabled: Optional[bool]
                """
                Whether the rule is enabled.
                """
                id: str
                """
                Identifier of the rule.
                """
                objective: Optional[str]
                """
                Objective of the rule.
                """
                predicate: Optional[str]
                """
                Rule expression evaluated to determine whether the rule matches.
                """
                rollout_percentage: Optional[Decimal]
                """
                Percentage of matching traffic to which the rule applies, between 0 and 100, serialized as a decimal string.
                """
                type: Optional[Union[Literal["account", "payment"], str]]
                """
                Type of entity evaluated by the rule.
                """
                _field_encodings = {"rollout_percentage": "decimal_string"}

            new_risk_preference: Optional[
                Union[
                    Literal["balanced", "custom", "high_growth", "low_risk"],
                    str,
                ]
            ]
            """
            Risk preference after a preference switch carried by a protection-toggle action.
            """
            new_rules: Optional[List[NewRule]]
            """
            Rules after the change. Set for add, update, enable, and disable actions; absent for remove actions.
            """
            old_risk_preference: Optional[
                Union[
                    Literal["balanced", "custom", "high_growth", "low_risk"],
                    str,
                ]
            ]
            """
            Risk preference before a preference switch carried by a protection-toggle action.
            """
            old_rules: Optional[List[OldRule]]
            """
            Rules before the change. Set for update, removal, enable, and disable actions; absent for add actions.
            """
            _inner_class_types = {"new_rules": NewRule, "old_rules": OldRule}

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

        class StripeAccess(StripeObject):
            class Reason(StripeObject):
                class AccessRequest(StripeObject):
                    id: str
                    """
                    Identifier of the access request.
                    """

                class SupportRelationship(StripeObject):
                    id: str
                    """
                    Identifier of the support relationship.
                    """
                    name: Optional[str]
                    """
                    Name of the support contact, when available.
                    """
                    role: Optional[str]
                    """
                    Role of the support contact, when available.
                    """

                class SupportTicket(StripeObject):
                    id: str
                    """
                    Identifier of the support ticket.
                    """

                access_request: Optional[AccessRequest]
                """
                Set when access is granted through an access request.
                """
                support_relationship: Optional[SupportRelationship]
                """
                Set when access is granted through a support relationship.
                """
                support_ticket: Optional[SupportTicket]
                """
                Set when access is granted through a support ticket.
                """
                type: Union[
                    Literal[
                        "access_request",
                        "support_relationship",
                        "support_ticket",
                    ],
                    str,
                ]
                """
                The type of reason for granting access.
                """
                _inner_class_types = {
                    "access_request": AccessRequest,
                    "support_relationship": SupportRelationship,
                    "support_ticket": SupportTicket,
                }

            access_type: Union[
                Literal["dashboard_read_only", "dashboard_read_write"], str
            ]
            """
            The level of Dashboard access granted.
            """
            reason: Reason
            """
            The reason for granting Stripe access.
            """
            _inner_class_types = {"reason": Reason}

        class UserAccess(StripeObject):
            class DashboardClient(StripeObject):
                user_agent: str
                """
                User-Agent header for the user access action.
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

                signals: List[Signal]
                """
                Risk signals for the user access action.
                """
                _inner_class_types = {"signals": Signal}

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
            surface: Union[Literal["dashboard", "embedded", "express"], str]
            """
            Surface where the user access action started.
            """
            _inner_class_types = {
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
        connect: Optional[Connect]
        """
        Details of a Connect action.
        """
        data_export: Optional[DataExport]
        """
        Details of a data export action.
        """
        event_destination: Optional[EventDestination]
        """
        Details of an event destination action.
        """
        radar: Optional[Radar]
        """
        Details of a Radar action.
        """
        scim: Optional[Scim]
        """
        Details of a SCIM action.
        """
        sso: Optional[Sso]
        """
        Details of an SSO action.
        """
        stripe_access: Optional[StripeAccess]
        """
        Details of a Stripe access action.
        """
        type: Union[
            Literal[
                "account_security",
                "api_key",
                "app",
                "authentication",
                "connect",
                "data_export",
                "event_destination",
                "issuing",
                "payout",
                "radar",
                "scim",
                "sso",
                "stripe_access",
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
            "connect": Connect,
            "data_export": DataExport,
            "event_destination": EventDestination,
            "radar": Radar,
            "scim": Scim,
            "sso": Sso,
            "stripe_access": StripeAccess,
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
                "apps.install",
                "balance_transfer",
                "bank_account",
                "blockchain_address",
                "card",
                "v2.core.event_destination",
                "issuing.card",
                "issuing.cardholder",
                "issuing.dispute",
                "webhook_endpoint",
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
            "application_authorized",
            "application_created",
            "application_deauthorized",
            "app_installed",
            "app_uninstalled",
            "connect_express_branding_updated",
            "connect_oauth_disabled",
            "connect_oauth_enabled",
            "connect_settings_updated",
            "connect_site_link_updated",
            "data_export_requested",
            "event_destination_added",
            "event_destination_removed",
            "event_destination_updated",
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
            "payout_schedule_updated",
            "radar_adaptive_3ds_disabled",
            "radar_dynamic_risk_thresholds_disabled",
            "radar_early_fraud_warning_disabled",
            "radar_for_setup_intents_disabled",
            "radar_fraud_dispute_protection_disabled",
            "radar_rule_added",
            "radar_rule_disabled",
            "radar_rule_enabled",
            "radar_rule_removed",
            "radar_rule_updated",
            "scim_group_deleted",
            "scim_group_member_added",
            "scim_group_member_removed",
            "scim_group_roles_updated",
            "scim_group_updated",
            "sso_domain_verified",
            "sso_settings_created",
            "sso_settings_deleted",
            "sso_settings_updated",
            "stripe_access_started",
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
