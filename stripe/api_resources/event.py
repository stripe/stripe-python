# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)


class Event(ListableAPIResource["Event"]):
    """
    Events are our way of letting you know when something interesting happens in
    your account. When an interesting event occurs, we create a new `Event`
    object. For example, when a charge succeeds, we create a `charge.succeeded`
    event, and when an invoice payment attempt fails, we create an
    `invoice.payment_failed` event. Certain API requests might create multiple
    events. For example, if you create a new subscription for a
    customer, you receive both a `customer.subscription.created` event and a
    `charge.succeeded` event.

    Events occur when the state of another API resource changes. The event's data
    field embeds the resource's state at the time of the change. For
    example, a `charge.succeeded` event contains a charge, and an
    `invoice.payment_failed` event contains an invoice.

    As with other API resources, you can use endpoints to retrieve an
    [individual event](https://stripe.com/docs/api#retrieve_event) or a [list of events](https://stripe.com/docs/api#list_events)
    from the API. We also have a separate
    [webhooks](http://en.wikipedia.org/wiki/Webhook) system for sending the
    `Event` objects directly to an endpoint on your server. You can manage
    webhooks in your
    [account settings](https://dashboard.stripe.com/account/webhooks). Learn how
    to [listen for events]
    (/docs/webhooks) so that your integration can automatically trigger reactions.

    When using [Connect](https://stripe.com/docs/connect), you can also receive event notifications
    that occur in connected accounts. For these events, there's an
    additional `account` attribute in the received `Event` object.

    We only guarantee access to events through the [Retrieve Event API](https://stripe.com/docs/api#retrieve_event)
    for 30 days.
    """

    OBJECT_NAME = "event"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired["Event.ListParamsCreated|int|None"]
            delivery_success: NotRequired["bool|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired["str|None"]
            types: NotRequired["List[str]|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    account: Optional[str]
    api_version: Optional[str]
    created: int
    data: StripeObject
    id: str
    livemode: bool
    object: Literal["event"]
    pending_webhooks: int
    request: Optional[StripeObject]
    type: Literal[
        "account.application.authorized",
        "account.application.deauthorized",
        "account.external_account.created",
        "account.external_account.deleted",
        "account.external_account.updated",
        "account.updated",
        "application_fee.created",
        "application_fee.refund.updated",
        "application_fee.refunded",
        "balance.available",
        "billing_portal.configuration.created",
        "billing_portal.configuration.updated",
        "billing_portal.session.created",
        "capability.updated",
        "cash_balance.funds_available",
        "charge.captured",
        "charge.dispute.closed",
        "charge.dispute.created",
        "charge.dispute.funds_reinstated",
        "charge.dispute.funds_withdrawn",
        "charge.dispute.updated",
        "charge.expired",
        "charge.failed",
        "charge.pending",
        "charge.refund.updated",
        "charge.refunded",
        "charge.succeeded",
        "charge.updated",
        "checkout.session.async_payment_failed",
        "checkout.session.async_payment_succeeded",
        "checkout.session.completed",
        "checkout.session.expired",
        "coupon.created",
        "coupon.deleted",
        "coupon.updated",
        "credit_note.created",
        "credit_note.updated",
        "credit_note.voided",
        "customer.created",
        "customer.deleted",
        "customer.discount.created",
        "customer.discount.deleted",
        "customer.discount.updated",
        "customer.source.created",
        "customer.source.deleted",
        "customer.source.expiring",
        "customer.source.updated",
        "customer.subscription.created",
        "customer.subscription.deleted",
        "customer.subscription.paused",
        "customer.subscription.pending_update_applied",
        "customer.subscription.pending_update_expired",
        "customer.subscription.resumed",
        "customer.subscription.trial_will_end",
        "customer.subscription.updated",
        "customer.tax_id.created",
        "customer.tax_id.deleted",
        "customer.tax_id.updated",
        "customer.updated",
        "customer_cash_balance_transaction.created",
        "file.created",
        "financial_connections.account.created",
        "financial_connections.account.deactivated",
        "financial_connections.account.disconnected",
        "financial_connections.account.reactivated",
        "financial_connections.account.refreshed_balance",
        "identity.verification_session.canceled",
        "identity.verification_session.created",
        "identity.verification_session.processing",
        "identity.verification_session.redacted",
        "identity.verification_session.requires_input",
        "identity.verification_session.verified",
        "invoice.created",
        "invoice.deleted",
        "invoice.finalization_failed",
        "invoice.finalized",
        "invoice.marked_uncollectible",
        "invoice.paid",
        "invoice.payment_action_required",
        "invoice.payment_failed",
        "invoice.payment_succeeded",
        "invoice.sent",
        "invoice.upcoming",
        "invoice.updated",
        "invoice.voided",
        "invoiceitem.created",
        "invoiceitem.deleted",
        "issuing_authorization.created",
        "issuing_authorization.request",
        "issuing_authorization.updated",
        "issuing_card.created",
        "issuing_card.updated",
        "issuing_cardholder.created",
        "issuing_cardholder.updated",
        "issuing_dispute.closed",
        "issuing_dispute.created",
        "issuing_dispute.funds_reinstated",
        "issuing_dispute.submitted",
        "issuing_dispute.updated",
        "issuing_token.created",
        "issuing_token.updated",
        "issuing_transaction.created",
        "issuing_transaction.updated",
        "mandate.updated",
        "payment_intent.amount_capturable_updated",
        "payment_intent.canceled",
        "payment_intent.created",
        "payment_intent.partially_funded",
        "payment_intent.payment_failed",
        "payment_intent.processing",
        "payment_intent.requires_action",
        "payment_intent.succeeded",
        "payment_link.created",
        "payment_link.updated",
        "payment_method.attached",
        "payment_method.automatically_updated",
        "payment_method.detached",
        "payment_method.updated",
        "payout.canceled",
        "payout.created",
        "payout.failed",
        "payout.paid",
        "payout.reconciliation_completed",
        "payout.updated",
        "person.created",
        "person.deleted",
        "person.updated",
        "plan.created",
        "plan.deleted",
        "plan.updated",
        "price.created",
        "price.deleted",
        "price.updated",
        "product.created",
        "product.deleted",
        "product.updated",
        "promotion_code.created",
        "promotion_code.updated",
        "quote.accepted",
        "quote.canceled",
        "quote.created",
        "quote.finalized",
        "radar.early_fraud_warning.created",
        "radar.early_fraud_warning.updated",
        "refund.created",
        "refund.updated",
        "reporting.report_run.failed",
        "reporting.report_run.succeeded",
        "reporting.report_type.updated",
        "review.closed",
        "review.opened",
        "setup_intent.canceled",
        "setup_intent.created",
        "setup_intent.requires_action",
        "setup_intent.setup_failed",
        "setup_intent.succeeded",
        "sigma.scheduled_query_run.created",
        "source.canceled",
        "source.chargeable",
        "source.failed",
        "source.mandate_notification",
        "source.refund_attributes_required",
        "source.transaction.created",
        "source.transaction.updated",
        "subscription_schedule.aborted",
        "subscription_schedule.canceled",
        "subscription_schedule.completed",
        "subscription_schedule.created",
        "subscription_schedule.expiring",
        "subscription_schedule.released",
        "subscription_schedule.updated",
        "tax.settings.updated",
        "tax_rate.created",
        "tax_rate.updated",
        "terminal.reader.action_failed",
        "terminal.reader.action_succeeded",
        "test_helpers.test_clock.advancing",
        "test_helpers.test_clock.created",
        "test_helpers.test_clock.deleted",
        "test_helpers.test_clock.internal_failure",
        "test_helpers.test_clock.ready",
        "topup.canceled",
        "topup.created",
        "topup.failed",
        "topup.reversed",
        "topup.succeeded",
        "transfer.created",
        "transfer.reversed",
        "transfer.updated",
        "treasury.credit_reversal.created",
        "treasury.credit_reversal.posted",
        "treasury.debit_reversal.completed",
        "treasury.debit_reversal.created",
        "treasury.debit_reversal.initial_credit_granted",
        "treasury.financial_account.closed",
        "treasury.financial_account.created",
        "treasury.financial_account.features_status_updated",
        "treasury.inbound_transfer.canceled",
        "treasury.inbound_transfer.created",
        "treasury.inbound_transfer.failed",
        "treasury.inbound_transfer.succeeded",
        "treasury.outbound_payment.canceled",
        "treasury.outbound_payment.created",
        "treasury.outbound_payment.expected_arrival_date_updated",
        "treasury.outbound_payment.failed",
        "treasury.outbound_payment.posted",
        "treasury.outbound_payment.returned",
        "treasury.outbound_transfer.canceled",
        "treasury.outbound_transfer.created",
        "treasury.outbound_transfer.expected_arrival_date_updated",
        "treasury.outbound_transfer.failed",
        "treasury.outbound_transfer.posted",
        "treasury.outbound_transfer.returned",
        "treasury.received_credit.created",
        "treasury.received_credit.failed",
        "treasury.received_credit.succeeded",
        "treasury.received_debit.created",
        "invoiceitem.updated",
        "order.created",
        "recipient.created",
        "recipient.deleted",
        "recipient.updated",
        "sku.created",
        "sku.deleted",
        "sku.updated",
    ]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Event.ListParams"]
    ) -> ListObject["Event"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Event.RetrieveParams"]
    ) -> "Event":
        instance = cls(id, **params)
        instance.refresh()
        return instance
