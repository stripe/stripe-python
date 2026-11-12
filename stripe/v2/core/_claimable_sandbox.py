# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class ClaimableSandbox(StripeObject):
    """
    A claimable sandbox is a Stripe sandbox that a user can claim into a new or existing Stripe account
    through an onboarding link. You can prefill it with an email address, sandbox name, and country.
    Claimable sandboxes have 60 days to be claimed. After this expiration time has passed,
    if the sandbox is not claimed, it will be deleted.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.claimable_sandbox"]] = (
        "v2.core.claimable_sandbox"
    )

    class OnboardingLinkDetails(StripeObject):
        expires_at: str
        """
        Time at which the onboarding link expires. Represented as an RFC 3339 timestamp in UTC
        with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
        """
        refresh_url: str
        """
        The URL the user will be redirected to if the onboarding link is expired or invalid.
        The URL specified should attempt to generate a new onboarding link,
        and re-direct the user to this new onboarding link so that they can proceed with the onboarding flow.
        """
        return_url: Optional[str]
        """
        The URL offered to the user as a way back to your app after they claim the sandbox.
        """
        url: str
        """
        The URL that lets a user claim the sandbox or continue onboarding their Stripe account,
        depending on the sandbox's status.
        """

    class OwnerDetails(StripeObject):
        account: Optional[str]
        """
        The ID of the live mode Stripe account that owns the sandbox.
        This field is only set when `owner_details.app_install_status` is `installed`.
        """
        app_install_status: Optional[
            Literal["installed", "pending_install", "pending_onboarding"]
        ]
        """
        Indicates whether the platform app is installed on the sandbox's live mode owner account.
        """

    class Prefill(StripeObject):
        country: str
        """
        Country in which the account holder resides, or in which the business is legally established.
        Use two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        email: str
        """
        Email address of the user who will claim the sandbox.
        Stripe sends this address an invitation to claim the sandbox and a reminder before the unclaimed sandbox expires.
        """
        name: str
        """
        Name for the sandbox.
        """

    class SandboxDetails(StripeObject):
        class ApiKeys(StripeObject):
            class Mcp(StripeObject):
                class SecretKey(StripeObject):
                    token: Optional[str]
                    """
                    The plaintext token for the API key.
                    """

                created: str
                """
                Time at which the API key was created. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                expires_at: Optional[str]
                """
                Time at which the API key expires. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                id: str
                """
                Unique identifier of the API key.
                """
                secret_key: Optional[SecretKey]
                """
                Token for the secret key. Present only in the create response;
                null in subsequent retrieve responses.
                """
                status: Union[Literal["active", "expired"], str]
                """
                Current status of the API key.
                """
                type: Union[Literal["secret_key"], str]
                """
                Type of the API key.
                """
                _inner_class_types = {"secret_key": SecretKey}

            class Publishable(StripeObject):
                class PublishableKey(StripeObject):
                    token: Optional[str]
                    """
                    The plaintext token for the API key.
                    """

                created: str
                """
                Time at which the API key was created. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                expires_at: Optional[str]
                """
                Time at which the API key expires. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                id: str
                """
                Unique identifier of the API key.
                """
                publishable_key: Optional[PublishableKey]
                """
                Token for the publishable key. Present only in the create response;
                null in subsequent retrieve responses.
                """
                status: Union[Literal["active", "expired"], str]
                """
                Current status of the API key.
                """
                type: Union[Literal["publishable_key"], str]
                """
                Type of the API key.
                """
                _inner_class_types = {"publishable_key": PublishableKey}

            class Secret(StripeObject):
                class SecretKey(StripeObject):
                    token: Optional[str]
                    """
                    The plaintext token for the API key.
                    """

                created: str
                """
                Time at which the API key was created. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                expires_at: Optional[str]
                """
                Time at which the API key expires. Represented as an RFC 3339 timestamp in UTC
                with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
                """
                id: str
                """
                Unique identifier of the API key.
                """
                secret_key: Optional[SecretKey]
                """
                Token for the secret key. Present only in the create response;
                null in subsequent retrieve responses.
                """
                status: Union[Literal["active", "expired"], str]
                """
                Current status of the API key.
                """
                type: Union[Literal["secret_key"], str]
                """
                Type of the API key.
                """
                _inner_class_types = {"secret_key": SecretKey}

            mcp: Optional[Mcp]
            """
            Object hash for the sandbox's MCP key.
            Null unless `enable_mcp_access: true` was passed in the creation request.
            """
            publishable: Publishable
            """
            Object hash for the sandbox's publishable key.
            """
            secret: Secret
            """
            Object hash for the sandbox's secret key.
            """
            _inner_class_types = {
                "mcp": Mcp,
                "publishable": Publishable,
                "secret": Secret,
            }

        account: str
        """
        The sandbox's Stripe account ID.
        """
        api_keys: Optional[ApiKeys]
        """
        Keys that can be used to set up an integration for this sandbox and operate on the account.
        Present in the create response. To fetch this field in the retrieve response,
        pass `sandbox_details.api_keys` in the `include` parameter.
        """
        _inner_class_types = {"api_keys": ApiKeys}

    channel: Literal["public", "testing"]
    """
    The distribution channel used to pre-install your Stripe App on the claimable sandbox.
    Use `testing` to install your app's external test version or `public` to install its published version.
    """
    claimed_at: Optional[str]
    """
    Time at which the sandbox was claimed. Set when the status is `claimed` or `live`.
    Represented as an RFC 3339 timestamp in UTC with millisecond precision,
    for example `2022-09-18T13:22:18.123Z`.
    """
    created: str
    """
    Time at which the sandbox was created. Represented as an RFC 3339 timestamp in UTC
    with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
    """
    expires_at: Optional[str]
    """
    Time at which the unclaimed sandbox expires. Null when the status is `claimed` or `live`.
    Represented as an RFC 3339 timestamp in UTC with millisecond precision,
    for example `2022-09-18T13:22:18.123Z`.
    """
    id: str
    """
    Unique identifier for the claimable sandbox.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.claimable_sandbox"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    onboarding_link_details: Optional[OnboardingLinkDetails]
    """
    Details about the onboarding link.
    Null when the sandbox status is `live` or `expired`.
    """
    owner_details: Optional[OwnerDetails]
    """
    Details about the live mode owner account of the sandbox.
    This will be null until the sandbox is claimed.
    """
    prefill: Prefill
    """
    Values prefilled during the creation of the sandbox. When a user claims the sandbox, they will be able to update these values.
    """
    sandbox_details: SandboxDetails
    """
    Data about the Stripe sandbox object.
    """
    status: Literal["claimed", "expired", "live", "unclaimed"]
    """
    Status of the sandbox.
    """
    _inner_class_types = {
        "onboarding_link_details": OnboardingLinkDetails,
        "owner_details": OwnerDetails,
        "prefill": Prefill,
        "sandbox_details": SandboxDetails,
    }
