# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
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
        type: Literal["api_key", "user"]
        """
        The type of actor.
        """
        user: Optional[User]
        """
        Set when the actor is a user.
        """
        _inner_class_types = {"api_key": ApiKey, "user": User}

    class Details(StripeObject):
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
                type: Literal["application"]
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

        class UserInvite(StripeObject):
            invited_user_email: str
            """
            Email address of the invited user.
            """
            roles: List[str]
            """
            Roles assigned to the invited user.
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
            user_email: str
            """
            Email address of the user whose roles were changed.
            """

        api_key: Optional[ApiKey]
        """
        Details of an API key action.
        """
        type: Literal["api_key", "user_invite", "user_roles"]
        """
        The action group type of the activity log entry.
        """
        user_invite: Optional[UserInvite]
        """
        Details of a user invite action.
        """
        user_roles: Optional[UserRoles]
        """
        Details of a user role change action.
        """
        _inner_class_types = {
            "api_key": ApiKey,
            "user_invite": UserInvite,
            "user_roles": UserRoles,
        }

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
    type: Literal[
        "api_key_created",
        "api_key_deleted",
        "api_key_updated",
        "api_key_viewed",
        "user_invite_accepted",
        "user_invite_created",
        "user_invite_deleted",
        "user_roles_deleted",
        "user_roles_updated",
    ]
    """
    The type of action that was performed.
    """
    _inner_class_types = {"actor": Actor, "details": Details}
