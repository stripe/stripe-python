# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class BatchJobCreateParams(TypedDict):
    endpoint: "BatchJobCreateParamsEndpoint"
    """
    The endpoint configuration for the batch job.
    """
    maximum_rps: NotRequired[int]
    """
    Optional field that allows the user to control how fast they want this batch job to run.
    Gives them a control over the number of webhooks they receive.
    """
    metadata: "Dict[str, str]|UntypedStripeObject[str]"
    """
    The metadata of the `batch_job`.
    """
    notification_suppression: NotRequired[
        "BatchJobCreateParamsNotificationSuppression"
    ]
    """
    Notification suppression settings for the batch job.
    """
    skip_validation: bool
    """
    Allows the user to skip validation.
    """


class BatchJobCreateParamsEndpoint(TypedDict):
    http_method: Literal["delete", "post"]
    """
    The HTTP method to use when calling the endpoint.
    """
    path: Literal[
        "/v1/accounts/:account",
        "/v1/accounts",
        "/v1/accounts/:account",
        "/v1/coupons",
        "/v1/coupons/:coupon",
        "/v1/coupons/:coupon",
        "/v1/credit_notes",
        "/v1/customers/:customer",
        "/v1/customers/:customer",
        "/v1/customers",
        "/v1/customers/:customer/discount",
        "/v1/customers/:customer/funding_instructions",
        "/v1/customers/:customer/subscriptions",
        "/v1/customers/:customer/subscriptions",
        "/v1/customers/:customer/subscriptions/:subscription_exposed_id",
        "/v1/customers/:customer/subscriptions/:subscription_exposed_id/discount",
        "/v1/customers/:customer/bank_accounts",
        "/v1/customers/:customer/bank_accounts/:id",
        "/v1/customers/:customer/bank_accounts/:id",
        "/v1/customers/:customer/bank_accounts/:id/verify",
        "/v1/customers/:customer/cards",
        "/v1/customers/:customer/cards/:id",
        "/v1/customers/:customer/cards/:id",
        "/v1/customers/:customer/tax_ids",
        "/v1/customers/:customer/sources",
        "/v1/customers/:customer/sources/:id",
        "/v1/customers/:customer/sources/:id",
        "/v1/customers/:customer/sources/:id/verify",
        "/v1/customers/:customer/balance_transactions",
        "/v1/customers/:customer/balance_transactions/:transaction",
        "/v1/customers/:customer/cash_balance",
        "/v1/customer_sessions",
        "/v1/disputes/:dispute/close",
        "/v1/invoices",
        "/v1/invoices/:invoice",
        "/v1/invoices/:invoice",
        "/v1/invoices/:invoice/pay",
        "/v1/invoices/:invoice/send",
        "/v1/invoices/:invoice/void",
        "/v1/invoices/:invoice/finalize",
        "/v1/invoices/:invoice/mark_uncollectible",
        "/v1/invoices/:invoice/update_lines",
        "/v1/invoices/:invoice/add_lines",
        "/v1/invoices/:invoice/remove_lines",
        "/v1/invoices/create_preview",
        "/v1/invoices/:invoice/lines/:line_item_id",
        "/v1/invoiceitems",
        "/v1/invoiceitems/:invoiceitem",
        "/v1/invoiceitems/:invoiceitem",
        "/v1/invoice_rendering_templates/:template/archive",
        "/v1/invoice_rendering_templates/:template/unarchive",
        "/v1/payment_methods/:payment_method/attach",
        "/v1/prices",
        "/v1/prices/:price",
        "/v1/products",
        "/v1/products/:id",
        "/v1/products/:id",
        "/v1/products/:product/features",
        "/v1/products/:product/features/:id",
        "/v1/promotion_codes",
        "/v1/promotion_codes/:promotion_code",
        "/v1/radar/value_list_items",
        "/v1/refunds",
        "/v1/refunds/:refund/cancel",
        "/v1/subscriptions/:subscription_exposed_id",
        "/v1/subscriptions/:subscription_exposed_id",
        "/v1/subscriptions/:subscription/migrate",
        "/v1/subscriptions",
        "/v1/subscriptions/:subscription/resume",
        "/v1/subscriptions/:subscription/pause",
        "/v1/subscription_items",
        "/v1/subscription_items/:item",
        "/v1/subscription_items/:item",
        "/v1/subscription_schedules",
        "/v1/subscription_schedules/:schedule",
        "/v1/subscription_schedules/:schedule/cancel",
        "/v1/subscription_schedules/:schedule/release",
        "/v1/tax/registrations",
        "/v1/tax/registrations/:id",
        "/v1/tax/settings",
        "/v1/tax/transactions/create_reversal",
        "/v1/tax_ids",
        "/v1/tax_ids/:id",
        "/v1/customers/:customer/tax_ids",
        "/v1/customers/:customer/tax_ids/:id",
        "/v1/tax_rates",
        "/v1/tax_rates/:tax_rate",
    ]
    """
    The path of the endpoint to run this batch job against.
    In the form used in the documentation. For instance, for
    subscription migration this would be `/v1/subscriptions/:id/migrate`.
    """


class BatchJobCreateParamsNotificationSuppression(TypedDict):
    scope: Literal["all", "none"]
    """
    The scope of notification suppression.
    """
