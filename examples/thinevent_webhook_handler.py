"""
thinevent_webhook_handler.py - receive and process thin events like the
v1.billing.meter.error_report_triggered event.

In this example, we:
    - create a StripeClient called client
    - use client.parse_thin_event to parse the received thin event webhook body
    - call client.v2.core.events.retrieve to retrieve the full event object
    - if it is a V1BillingMeterErrorReportTriggeredEvent event type, call
      event.fetchRelatedObject to retrieve the Billing Meter object associated
      with the event.
"""

import os
from stripe import StripeClient
from stripe.events import V1BillingMeterErrorReportTriggeredEvent

from flask import Flask, request, jsonify

app = Flask(__name__)
api_key = os.environ.get("STRIPE_API_KEY")
webhook_secret = os.environ.get("WEBHOOK_SECRET")

client = StripeClient(api_key)


@app.route("/webhook", methods=["POST"])
def webhook():
    webhook_body = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        thin_event = client.parse_thin_event(
            webhook_body, sig_header, webhook_secret
        )

        # Fetch the event data to understand the failure
        event = client.v2.core.events.retrieve(thin_event.id)
        if isinstance(event, V1BillingMeterErrorReportTriggeredEvent):
            meter = event.fetch_related_object()
            meter_id = meter.id
            print("Success! " + str(meter_id))

            # Record the failures and alert your team
            # Add your logic here

        return jsonify(success=True), 200
    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(port=4242)
