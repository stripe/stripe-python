# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class RateCardSubscriptionListParams(TypedDict):
    billing_cadence: NotRequired[str]
    """
    Optionally filter by a BillingCadence. Mutually exclusive with `payers`, `rate_card`, and `rate_card_version`.
    """
    limit: NotRequired[int]
    """
    The page size limit, if not provided the default is 20.
    """
    payer: NotRequired["RateCardSubscriptionListParamsPayer"]
    """
    Optionally filter by the payer associated with Billing Cadences which the Rate Card Subscriptions are subscribed to.
    Mutually exclusive with `billing_cadence`, `rate_card`, and `rate_card_version`.
    """
    rate_card: NotRequired[str]
    """
    Optionally filter by a RateCard. Mutually exclusive with `billing_cadence`, `payers`, and `rate_card_version`.
    """
    rate_card_version: NotRequired[str]
    """
    Optionally filter by a RateCard version. Mutually exclusive with `billing_cadence`, `payers`, and `rate_card`.
    """
    servicing_status: NotRequired[
        Literal["active", "canceled", "paused", "pending"]
    ]
    """
    Optionally filter by servicing status.
    """


class RateCardSubscriptionListParamsPayer(TypedDict):
    customer: NotRequired[str]
    """
    The ID of the Customer object. If provided, only the Rate Card Subscriptions that are subscribed on the Billing Cadences with the specified payer will be returned.
    """
    type: Literal["customer"]
    """
    A string identifying the type of the payer. Currently the only supported value is `customer`.
    """
