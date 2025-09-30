"""
event_notification_webhook_handler.py - receive and process thin events like the
v1.billing.meter.error_report_triggered event.

In this example, we:
    - create a StripeClient called client
    - use client.parse_event_notification() to parse the received notification webhook body
    - if its type is "v1.billing.meter.error_report_triggered":
        - call event_notification.fetch_event() to retrieve the full event object
        - call event_notification.fetch_related_object() to retrieve the Meter that failed
        - log info about the failure
"""

import os
from stripe import StripeClient
from stripe import Event
from stripe.v2.core import Event as V2Event, EventNotification
from stripe.events import (
    V2CoreEventDestinationPingEventNotification,
    V1BillingMeterErrorReportTriggeredEvent,
    UnknownEventNotification,
    ALL_EVENT_NOTIFICATIONS,
)

from flask import Flask, request, jsonify

app = Flask(__name__)
api_key = os.environ.get("STRIPE_API_KEY", "")
webhook_secret = os.environ.get("WEBHOOK_SECRET", "")

client = StripeClient(api_key)


@app.route("/webhook", methods=["POST"])
def webhook():
    webhook_body = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event_notification = client.parse_event_notification(
            webhook_body, sig_header, webhook_secret
        )

        # Fetch the event data to understand the failure
        if (
            event_notification.type
            == "v1.billing.meter.error_report_triggered"
        ):
            meter = event_notification.fetch_related_object()
            event = event_notification.fetch_event()
            print(
                f"Err! Meter {meter.id} had a problem (more info: {event.data.developer_message_summary})"
            )
            # Record the failures and alert your team
            # Add your logic here

        return jsonify(success=True), 200
    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(port=4242)
