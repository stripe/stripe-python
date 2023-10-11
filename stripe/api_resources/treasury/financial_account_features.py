# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class FinancialAccountFeatures(StripeObject):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """

    OBJECT_NAME = "treasury.financial_account_features"
    card_issuing: Optional[StripeObject]
    deposit_insurance: Optional[StripeObject]
    financial_addresses: Optional[StripeObject]
    inbound_transfers: Optional[StripeObject]
    intra_stripe_flows: Optional[StripeObject]
    object: Literal["treasury.financial_account_features"]
    outbound_payments: Optional[StripeObject]
    outbound_transfers: Optional[StripeObject]
