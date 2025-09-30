# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class SubscriptionAttachCadenceParams(RequestOptions):
    billing_cadence: str
    """
    The Billing Cadence which controls the timing of recurring invoice generation for this subscription. If unset, the subscription will bill according to its own configured schedule and create its own invoices. If set, this subscription will be billed by the cadence instead, potentially sharing invoices with the other subscriptions linked to that Cadence.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
