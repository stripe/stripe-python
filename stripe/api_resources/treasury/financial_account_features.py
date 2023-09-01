# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class FinancialAccountFeatures(StripeObject):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """

    OBJECT_NAME = "treasury.financial_account_features"
    card_issuing: StripeObject
    deposit_insurance: StripeObject
    financial_addresses: StripeObject
    inbound_transfers: StripeObject
    intra_stripe_flows: StripeObject
    object: Literal["treasury.financial_account_features"]
    outbound_payments: StripeObject
    outbound_transfers: StripeObject
