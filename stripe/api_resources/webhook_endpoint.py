# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus


class WebhookEndpoint(
    CreateableAPIResource["WebhookEndpoint"],
    DeletableAPIResource["WebhookEndpoint"],
    ListableAPIResource["WebhookEndpoint"],
    UpdateableAPIResource["WebhookEndpoint"],
):
    """
    You can configure [webhook endpoints](https://stripe.com/docs/webhooks/) via the API to be
    notified about events that happen in your Stripe account or connected
    accounts.

    Most users configure webhooks from [the dashboard](https://dashboard.stripe.com/webhooks), which provides a user interface for registering and testing your webhook endpoints.

    Related guide: [Setting up webhooks](https://stripe.com/docs/webhooks/configure)
    """

    OBJECT_NAME = "webhook_endpoint"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            api_version: NotRequired[
                "Literal['2011-01-01', '2011-06-21', '2011-06-28', '2011-08-01', '2011-09-15', '2011-11-17', '2012-02-23', '2012-03-25', '2012-06-18', '2012-06-28', '2012-07-09', '2012-09-24', '2012-10-26', '2012-11-07', '2013-02-11', '2013-02-13', '2013-07-05', '2013-08-12', '2013-08-13', '2013-10-29', '2013-12-03', '2014-01-31', '2014-03-13', '2014-03-28', '2014-05-19', '2014-06-13', '2014-06-17', '2014-07-22', '2014-07-26', '2014-08-04', '2014-08-20', '2014-09-08', '2014-10-07', '2014-11-05', '2014-11-20', '2014-12-08', '2014-12-17', '2014-12-22', '2015-01-11', '2015-01-26', '2015-02-10', '2015-02-16', '2015-02-18', '2015-03-24', '2015-04-07', '2015-06-15', '2015-07-07', '2015-07-13', '2015-07-28', '2015-08-07', '2015-08-19', '2015-09-03', '2015-09-08', '2015-09-23', '2015-10-01', '2015-10-12', '2015-10-16', '2016-02-03', '2016-02-19', '2016-02-22', '2016-02-23', '2016-02-29', '2016-03-07', '2016-06-15', '2016-07-06', '2016-10-19', '2017-01-27', '2017-02-14', '2017-04-06', '2017-05-25', '2017-06-05', '2017-08-15', '2017-12-14', '2018-01-23', '2018-02-05', '2018-02-06', '2018-02-28', '2018-05-21', '2018-07-27', '2018-08-23', '2018-09-06', '2018-09-24', '2018-10-31', '2018-11-08', '2019-02-11', '2019-02-19', '2019-03-14', '2019-05-16', '2019-08-14', '2019-09-09', '2019-10-08', '2019-10-17', '2019-11-05', '2019-12-03', '2020-03-02', '2020-08-27', '2022-08-01', '2022-11-15', '2023-08-16']|None"
            ]
            connect: NotRequired["bool|None"]
            description: NotRequired["Literal['']|str|None"]
            enabled_events: List[
                Literal[
                    "*",
                    "account.application.authorized",
                    "account.application.deauthorized",
                    "account.external_account.created",
                    "account.external_account.deleted",
                    "account.external_account.updated",
                    "account.updated",
                    "account_notice.created",
                    "account_notice.updated",
                    "application_fee.created",
                    "application_fee.refund.updated",
                    "application_fee.refunded",
                    "balance.available",
                    "billing_portal.configuration.created",
                    "billing_portal.configuration.updated",
                    "billing_portal.session.created",
                    "capability.updated",
                    "capital.financing_offer.accepted",
                    "capital.financing_offer.canceled",
                    "capital.financing_offer.created",
                    "capital.financing_offer.expired",
                    "capital.financing_offer.fully_repaid",
                    "capital.financing_offer.paid_out",
                    "capital.financing_offer.rejected",
                    "capital.financing_offer.replacement_created",
                    "capital.financing_transaction.created",
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
                    "customer.subscription.collection_paused",
                    "customer.subscription.collection_resumed",
                    "customer.subscription.created",
                    "customer.subscription.custom_event",
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
                    "financial_connections.account.refreshed_inferred_balances",
                    "financial_connections.account.refreshed_ownership",
                    "financial_connections.account.refreshed_transactions",
                    "financial_connections.session.updated",
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
                    "issuing_personalization_design.activated",
                    "issuing_personalization_design.deactivated",
                    "issuing_personalization_design.rejected",
                    "issuing_personalization_design.updated",
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
                    "quote.accept_failed",
                    "quote.accepted",
                    "quote.accepting",
                    "quote.canceled",
                    "quote.created",
                    "quote.draft",
                    "quote.finalized",
                    "quote.reestimated",
                    "quote.stale",
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
                    "tax.form.updated",
                    "tax.settings.updated",
                    "tax_rate.created",
                    "tax_rate.updated",
                    "terminal.reader.action_failed",
                    "terminal.reader.action_succeeded",
                    "terminal.reader.action_updated",
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
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            url: str

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            description: NotRequired["Literal['']|str|None"]
            disabled: NotRequired["bool|None"]
            enabled_events: NotRequired[
                "List[Literal['*', 'account.application.authorized', 'account.application.deauthorized', 'account.external_account.created', 'account.external_account.deleted', 'account.external_account.updated', 'account.updated', 'account_notice.created', 'account_notice.updated', 'application_fee.created', 'application_fee.refund.updated', 'application_fee.refunded', 'balance.available', 'billing_portal.configuration.created', 'billing_portal.configuration.updated', 'billing_portal.session.created', 'capability.updated', 'capital.financing_offer.accepted', 'capital.financing_offer.canceled', 'capital.financing_offer.created', 'capital.financing_offer.expired', 'capital.financing_offer.fully_repaid', 'capital.financing_offer.paid_out', 'capital.financing_offer.rejected', 'capital.financing_offer.replacement_created', 'capital.financing_transaction.created', 'cash_balance.funds_available', 'charge.captured', 'charge.dispute.closed', 'charge.dispute.created', 'charge.dispute.funds_reinstated', 'charge.dispute.funds_withdrawn', 'charge.dispute.updated', 'charge.expired', 'charge.failed', 'charge.pending', 'charge.refund.updated', 'charge.refunded', 'charge.succeeded', 'charge.updated', 'checkout.session.async_payment_failed', 'checkout.session.async_payment_succeeded', 'checkout.session.completed', 'checkout.session.expired', 'coupon.created', 'coupon.deleted', 'coupon.updated', 'credit_note.created', 'credit_note.updated', 'credit_note.voided', 'customer.created', 'customer.deleted', 'customer.discount.created', 'customer.discount.deleted', 'customer.discount.updated', 'customer.source.created', 'customer.source.deleted', 'customer.source.expiring', 'customer.source.updated', 'customer.subscription.collection_paused', 'customer.subscription.collection_resumed', 'customer.subscription.created', 'customer.subscription.custom_event', 'customer.subscription.deleted', 'customer.subscription.paused', 'customer.subscription.pending_update_applied', 'customer.subscription.pending_update_expired', 'customer.subscription.resumed', 'customer.subscription.trial_will_end', 'customer.subscription.updated', 'customer.tax_id.created', 'customer.tax_id.deleted', 'customer.tax_id.updated', 'customer.updated', 'customer_cash_balance_transaction.created', 'file.created', 'financial_connections.account.created', 'financial_connections.account.deactivated', 'financial_connections.account.disconnected', 'financial_connections.account.reactivated', 'financial_connections.account.refreshed_balance', 'financial_connections.account.refreshed_inferred_balances', 'financial_connections.account.refreshed_ownership', 'financial_connections.account.refreshed_transactions', 'financial_connections.session.updated', 'identity.verification_session.canceled', 'identity.verification_session.created', 'identity.verification_session.processing', 'identity.verification_session.redacted', 'identity.verification_session.requires_input', 'identity.verification_session.verified', 'invoice.created', 'invoice.deleted', 'invoice.finalization_failed', 'invoice.finalized', 'invoice.marked_uncollectible', 'invoice.paid', 'invoice.payment_action_required', 'invoice.payment_failed', 'invoice.payment_succeeded', 'invoice.sent', 'invoice.upcoming', 'invoice.updated', 'invoice.voided', 'invoiceitem.created', 'invoiceitem.deleted', 'issuing_authorization.created', 'issuing_authorization.request', 'issuing_authorization.updated', 'issuing_card.created', 'issuing_card.updated', 'issuing_cardholder.created', 'issuing_cardholder.updated', 'issuing_dispute.closed', 'issuing_dispute.created', 'issuing_dispute.funds_reinstated', 'issuing_dispute.submitted', 'issuing_dispute.updated', 'issuing_personalization_design.activated', 'issuing_personalization_design.deactivated', 'issuing_personalization_design.rejected', 'issuing_personalization_design.updated', 'issuing_transaction.created', 'issuing_transaction.updated', 'mandate.updated', 'payment_intent.amount_capturable_updated', 'payment_intent.canceled', 'payment_intent.created', 'payment_intent.partially_funded', 'payment_intent.payment_failed', 'payment_intent.processing', 'payment_intent.requires_action', 'payment_intent.succeeded', 'payment_link.created', 'payment_link.updated', 'payment_method.attached', 'payment_method.automatically_updated', 'payment_method.detached', 'payment_method.updated', 'payout.canceled', 'payout.created', 'payout.failed', 'payout.paid', 'payout.reconciliation_completed', 'payout.updated', 'person.created', 'person.deleted', 'person.updated', 'plan.created', 'plan.deleted', 'plan.updated', 'price.created', 'price.deleted', 'price.updated', 'product.created', 'product.deleted', 'product.updated', 'promotion_code.created', 'promotion_code.updated', 'quote.accept_failed', 'quote.accepted', 'quote.accepting', 'quote.canceled', 'quote.created', 'quote.draft', 'quote.finalized', 'quote.reestimated', 'quote.stale', 'radar.early_fraud_warning.created', 'radar.early_fraud_warning.updated', 'refund.created', 'refund.updated', 'reporting.report_run.failed', 'reporting.report_run.succeeded', 'reporting.report_type.updated', 'review.closed', 'review.opened', 'setup_intent.canceled', 'setup_intent.created', 'setup_intent.requires_action', 'setup_intent.setup_failed', 'setup_intent.succeeded', 'sigma.scheduled_query_run.created', 'source.canceled', 'source.chargeable', 'source.failed', 'source.mandate_notification', 'source.refund_attributes_required', 'source.transaction.created', 'source.transaction.updated', 'subscription_schedule.aborted', 'subscription_schedule.canceled', 'subscription_schedule.completed', 'subscription_schedule.created', 'subscription_schedule.expiring', 'subscription_schedule.released', 'subscription_schedule.updated', 'tax.form.updated', 'tax.settings.updated', 'tax_rate.created', 'tax_rate.updated', 'terminal.reader.action_failed', 'terminal.reader.action_succeeded', 'terminal.reader.action_updated', 'test_helpers.test_clock.advancing', 'test_helpers.test_clock.created', 'test_helpers.test_clock.deleted', 'test_helpers.test_clock.internal_failure', 'test_helpers.test_clock.ready', 'topup.canceled', 'topup.created', 'topup.failed', 'topup.reversed', 'topup.succeeded', 'transfer.created', 'transfer.reversed', 'transfer.updated', 'treasury.credit_reversal.created', 'treasury.credit_reversal.posted', 'treasury.debit_reversal.completed', 'treasury.debit_reversal.created', 'treasury.debit_reversal.initial_credit_granted', 'treasury.financial_account.closed', 'treasury.financial_account.created', 'treasury.financial_account.features_status_updated', 'treasury.inbound_transfer.canceled', 'treasury.inbound_transfer.created', 'treasury.inbound_transfer.failed', 'treasury.inbound_transfer.succeeded', 'treasury.outbound_payment.canceled', 'treasury.outbound_payment.created', 'treasury.outbound_payment.expected_arrival_date_updated', 'treasury.outbound_payment.failed', 'treasury.outbound_payment.posted', 'treasury.outbound_payment.returned', 'treasury.outbound_transfer.canceled', 'treasury.outbound_transfer.created', 'treasury.outbound_transfer.expected_arrival_date_updated', 'treasury.outbound_transfer.failed', 'treasury.outbound_transfer.posted', 'treasury.outbound_transfer.returned', 'treasury.received_credit.created', 'treasury.received_credit.failed', 'treasury.received_credit.succeeded', 'treasury.received_debit.created', 'invoiceitem.updated', 'order.created', 'recipient.created', 'recipient.deleted', 'recipient.updated', 'sku.created', 'sku.deleted', 'sku.updated']]|None"
            ]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            url: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    api_version: Optional[str]
    application: Optional[str]
    created: int
    description: Optional[str]
    enabled_events: List[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["webhook_endpoint"]
    secret: Optional[str]
    status: str
    url: str
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["WebhookEndpoint.CreateParams"]
    ) -> "WebhookEndpoint":
        return cast(
            "WebhookEndpoint",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["WebhookEndpoint.DeleteParams"]
    ) -> "WebhookEndpoint":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "WebhookEndpoint",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["WebhookEndpoint.DeleteParams"]
    ) -> "WebhookEndpoint":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["WebhookEndpoint.ListParams"]
    ) -> ListObject["WebhookEndpoint"]:
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
    def modify(
        cls, id, **params: Unpack["WebhookEndpoint.ModifyParams"]
    ) -> "WebhookEndpoint":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "WebhookEndpoint",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["WebhookEndpoint.RetrieveParams"]
    ) -> "WebhookEndpoint":
        instance = cls(id, **params)
        instance.refresh()
        return instance
