# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import NotRequired, TypedDict


class PaymentIntentIncrementAuthorizationParams(RequestOptions):
    amount: int
    """
    The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
    """
    application_fee_amount: NotRequired[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    statement_descriptor: NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """
    transfer_data: NotRequired[
        "PaymentIntentIncrementAuthorizationParamsTransferData"
    ]
    """
    The parameters used to automatically create a transfer after the payment is captured.
    Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    """


class PaymentIntentIncrementAuthorizationParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount that will be transferred automatically when a charge succeeds.
    """
