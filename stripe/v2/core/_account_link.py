# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class AccountLink(StripeObject):
    """
    AccountLinks are the means by which a Merchant grants an Account permission to access Stripe-hosted applications, such as Recipient Onboarding. This API is only available for users enrolled in the public preview for Global Payouts.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.account_link"]] = (
        "v2.core.account_link"
    )

    class UseCase(StripeObject):
        class AccountOnboarding(StripeObject):
            configurations: List[Literal["recipient"]]
            """
            Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
            """
            refresh_url: str
            """
            The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
            """
            return_url: Optional[str]
            """
            The URL that the user will be redirected to upon completing the linked flow.
            """

        class AccountUpdate(StripeObject):
            configurations: List[Literal["recipient"]]
            """
            Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
            """
            refresh_url: str
            """
            The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
            """
            return_url: Optional[str]
            """
            The URL that the user will be redirected to upon completing the linked flow.
            """

        account_onboarding: Optional[AccountOnboarding]
        """
        Indicates that the AccountLink provided should onboard an account.
        """
        account_update: Optional[AccountUpdate]
        """
        Indicates that the AccountLink provided should update a previously onboarded account.
        """
        type: Literal["account_onboarding", "account_update"]
        """
        Open Enum. The type of AccountLink the user is requesting.
        """
        _inner_class_types = {
            "account_onboarding": AccountOnboarding,
            "account_update": AccountUpdate,
        }

    account: str
    """
    The ID of the Account the link was created for.
    """
    created: str
    """
    The timestamp at which this AccountLink was created.
    """
    expires_at: str
    """
    The timestamp at which this AccountLink will expire.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.account_link"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    url: str
    """
    The URL for the AccountLink.
    """
    use_case: UseCase
    """
    The use case of AccountLink the user is requesting.
    """
    _inner_class_types = {"use_case": UseCase}
