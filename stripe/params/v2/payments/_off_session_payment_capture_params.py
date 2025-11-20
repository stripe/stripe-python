# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class OffSessionPaymentCaptureParams(TypedDict):
    amount_to_capture: NotRequired[int]
    """
    The amount to capture.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can
    attach to an object. This can be useful for storing additional information about
    the object in a structured format. Learn more about
    [storing information in metadata](https://docs.stripe.com/payments/payment-intents#storing-information-in-metadata).
    """
    statement_descriptor: NotRequired[str]
    """
    Text that appears on the customer's statement as the statement descriptor for a
    non-card charge. This value overrides the account's default statement descriptor.
    For information about requirements, including the 22-character limit, see the
    [Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    """
    statement_descriptor_suffix: NotRequired[str]
    """
    Provides information about a card charge. Concatenated to the account's
    [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static)
    to form the complete statement descriptor that appears on the customer's statement.
    """
    transfer_data: NotRequired["OffSessionPaymentCaptureParamsTransferData"]
    """
    The data that automatically creates a Transfer after the payment finalizes. Learn more about the use case for [connected accounts](https://docs.stripe.com/payments/connected-accounts).
    """


class OffSessionPaymentCaptureParamsTransferData(TypedDict):
    amount: NotRequired[int]
    """
    The amount transferred to the destination account. This transfer will occur
    automatically after the payment succeeds. If no amount is specified, by default
    the entire payment amount is transferred to the destination account. The amount
    must be less than or equal to the
    [amount_requested](https://docs.stripe.com/api/v2/off-session-payments/object?api-version=2025-05-28.preview#v2_off_session_payment_object-amount_requested),
    and must be a positive integer representing how much to transfer in the smallest
    currency unit (e.g., 100 cents to charge $1.00).
    """
