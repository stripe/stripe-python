# -*- coding: utf-8 -*-
"""
event_notification_handler_endpoint.py - receive and process event notifications (AKA thin events) like "v1.billing.meter.error_report_triggered" using EventNotificationHandler.

In this example, we:
    - write a fallback callback to handle unrecognized event notifications
    - create a StripeClient called client
    - Initialize an EventNotificationHandler with the client, webhook secret, and fallback callback
    - register a specific handler for the "v1.billing.meter.error_report_triggered" event notification type
    - use handler.handle() to process the received notification webhook body
"""

import os
from flask import Flask, request, jsonify

from stripe import StripeClient, UnhandledNotificationDetails
from stripe.v2.core import EventNotification
from stripe.events import V1BillingMeterErrorReportTriggeredEventNotification

app = Flask(__name__)
api_key = os.environ.get("STRIPE_API_KEY", "")
webhook_secret = os.environ.get("WEBHOOK_SECRET", "")


def fallback_callback(
    notif: EventNotification,
    client: StripeClient,
    details: UnhandledNotificationDetails,
):
    print(f"Got an unhandled event of type {notif.type}!")


client = StripeClient(api_key)
handler = client.notification_handler(webhook_secret, fallback_callback)

# Handles events delivered through a channel that has already authenticated them, such as
# AWS EventBridge or Azure Event Grid. Those payloads carry no Stripe-Signature header.
unverified_handler = client.notification_handler_without_verification(
    fallback_callback
)


# can be anywhere in your codebase; registering on both handlers means either
# endpoint below will route this event type
@handler.on_v1_billing_meter_error_report_triggered
@unverified_handler.on_v1_billing_meter_error_report_triggered
def handle_meter_error(
    notif: V1BillingMeterErrorReportTriggeredEventNotification,
    client: StripeClient,
):
    event = notif.fetch_event()
    print(f"Err! No meter found: {event.data.developer_message_summary}")


@app.route("/webhook", methods=["POST"])
def webhook():
    webhook_body = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        handler.handle(webhook_body, sig_header)
        return jsonify(success=True), 200
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route("/webhook-from-cloud-provider", methods=["POST"])
def webhook_from_cloud_provider():
    # no signature header to pass along; the channel already authenticated this event
    try:
        unverified_handler.handle(request.data)
        return jsonify(success=True), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
