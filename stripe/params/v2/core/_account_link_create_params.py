# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountLinkCreateParams(TypedDict):
    account: str
    """
    The ID of the Account to create link for.
    """
    use_case: "AccountLinkCreateParamsUseCase"
    """
    The use case of the AccountLink.
    """


class AccountLinkCreateParamsUseCase(TypedDict):
    type: Literal["account_onboarding", "account_update"]
    """
    Open Enum. The type of AccountLink the user is requesting.
    """
    account_onboarding: NotRequired[
        "AccountLinkCreateParamsUseCaseAccountOnboarding"
    ]
    """
    Indicates that the AccountLink provided should onboard an account.
    """
    account_update: NotRequired["AccountLinkCreateParamsUseCaseAccountUpdate"]
    """
    Indicates that the AccountLink provided should update a previously onboarded account.
    """


class AccountLinkCreateParamsUseCaseAccountOnboarding(TypedDict):
    collection_options: NotRequired[
        "AccountLinkCreateParamsUseCaseAccountOnboardingCollectionOptions"
    ]
    """
    Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.
    """
    configurations: List[
        Literal["customer", "merchant", "recipient", "storer"]
    ]
    """
    Open Enum. A v2/core/account can be configured to enable certain functionality. The configuration param targets the v2/core/account_link to collect information for the specified v2/core/account configuration/s.
    """
    refresh_url: str
    """
    The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
    """
    return_url: NotRequired[str]
    """
    The URL that the user will be redirected to upon completing the linked flow.
    """


class AccountLinkCreateParamsUseCaseAccountOnboardingCollectionOptions(
    TypedDict,
):
    fields: NotRequired[Literal["currently_due", "eventually_due"]]
    """
    Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). If you don't specify collection_options, the default value is currently_due.
    """
    future_requirements: NotRequired[Literal["include", "omit"]]
    """
    Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
    """


class AccountLinkCreateParamsUseCaseAccountUpdate(TypedDict):
    collection_options: NotRequired[
        "AccountLinkCreateParamsUseCaseAccountUpdateCollectionOptions"
    ]
    """
    Specifies the requirements that Stripe collects from v2/core/accounts in the Onboarding flow.
    """
    configurations: List[
        Literal["customer", "merchant", "recipient", "storer"]
    ]
    """
    Open Enum. A v2/account can be configured to enable certain functionality. The configuration param targets the v2/account_link to collect information for the specified v2/account configuration/s.
    """
    refresh_url: str
    """
    The URL the user will be redirected to if the AccountLink is expired, has been used, or is otherwise invalid. The URL you specify should attempt to generate a new AccountLink with the same parameters used to create the original AccountLink, then redirect the user to the new AccountLink's URL so they can continue the flow. If a new AccountLink cannot be generated or the redirect fails you should display a useful error to the user. Please make sure to implement authentication before redirecting the user in case this URL is leaked to a third party.
    """
    return_url: NotRequired[str]
    """
    The URL that the user will be redirected to upon completing the linked flow.
    """


class AccountLinkCreateParamsUseCaseAccountUpdateCollectionOptions(TypedDict):
    fields: NotRequired[Literal["currently_due", "eventually_due"]]
    """
    Specifies whether the platform collects only currently_due requirements (`currently_due`) or both currently_due and eventually_due requirements (`eventually_due`). If you don't specify collection_options, the default value is currently_due.
    """
    future_requirements: NotRequired[Literal["include", "omit"]]
    """
    Specifies whether the platform collects future_requirements in addition to requirements in Connect Onboarding. The default value is `omit`.
    """
