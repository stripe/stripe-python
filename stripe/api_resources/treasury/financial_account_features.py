# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class FinancialAccountFeatures(StripeObject):
    """
    Encodes whether a FinancialAccount has access to a particular Feature, with a `status` enum and associated `status_details`.
    Stripe or the platform can control Features via the requested field.
    """

    OBJECT_NAME: ClassVar[
        Literal["treasury.financial_account_features"]
    ] = "treasury.financial_account_features"
    card_issuing: Optional[StripeObject]
    """
    Toggle settings for enabling/disabling a feature
    """
    deposit_insurance: Optional[StripeObject]
    """
    Toggle settings for enabling/disabling a feature
    """
    financial_addresses: Optional[StripeObject]
    """
    Settings related to Financial Addresses features on a Financial Account
    """
    inbound_transfers: Optional[StripeObject]
    """
    InboundTransfers contains inbound transfers features for a FinancialAccount.
    """
    intra_stripe_flows: Optional[StripeObject]
    """
    Toggle settings for enabling/disabling a feature
    """
    object: Literal["treasury.financial_account_features"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    outbound_payments: Optional[StripeObject]
    """
    Settings related to Outbound Payments features on a Financial Account
    """
    outbound_transfers: Optional[StripeObject]
    """
    OutboundTransfers contains outbound transfers features for a FinancialAccount.
    """
