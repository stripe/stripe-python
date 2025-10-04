"""
event_notification_webhook_handler.py - receive and process event notifications (AKA thin events) like the v1.billing.meter.error_report_triggered and v1.billing.meter.no_meter_found events.

In this example, we:
    - create a StripeClient called client
    - use client.parse_event_notification() to parse the received notification webhook body
    - if its type is "v1.billing.meter.error_report_triggered":
        - call event_notification.fetch_related_object() to retrieve the Meter that failed
        - call event_notification.fetch_event() to retrieve the full event object
        - log info about the failure
    - if its type is "v1.billing.meter.no_meter_found":
        - call event_notification.fetch_event() to retrieve the full event object
        - log info about the failure
    - if the SDK doesn't have types for it, it will be an UnknownEventNotification:
        - optionally cast it to UnknownEventNotification to get more accurate typing
        - match on the type property to handle specific unknown event types
"""

import os
from stripe import StripeClient
from stripe.events import UnknownEventNotification

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
        event_notif = client.parse_event_notification(
            webhook_body, sig_header, webhook_secret
        )

        # type checkers will narrow the type based on the `type` property
        if event_notif.type == "v1.billing.meter.error_report_triggered":
            # in this block, event_notification is typed as a V1BillingMeterErrorReportTriggeredEventNotification

            # there's basic info about the related object in the notification
            print(f"Meter w/ id {event_notif.related_object.id} had a problem")

            # or you can fetch the full object form the API for more details
            meter = event_notif.fetch_related_object()
            print(f"Meter {meter.display_name} ({meter.id}) had a problem")

            # And you can always fetch the full event:
            event = event_notif.fetch_event()
            print(f"More info: {event.data.developer_message_summary}")

        elif event_notif.type == "v1.billing.meter.no_meter_found":
            # in this block, event_notification is typed as a V1BillingMeterNoMeterFoundEventNotification

            # that class doesn't define `fetch_related_object` because the event has no related object
            # so this line would correctly give a type error:
            # meter = event_notif.fetch_related_object()

            # but fetching the event always works:
            event = event_notif.fetch_event()
            print(
                f"Err! No meter found: {event.data.developer_message_summary}"
            )

        # the above approach works for all event types that predate the SDK you're using
        # but, you also may need to handle event types that the SDK doesn't know about
        elif isinstance(event_notif, UnknownEventNotification):
            # these lines are optional, but will give you more accurate typing in this block
            from typing import cast

            event_notif = cast(UnknownEventNotification, event_notif)

            # continue matching on the type property
            # from this point on, the `related_object` property _may_ be None (depending on the event type)
            if event_notif.type == "some.new.event":
                # if this event type has a related object, you can fetch it
                obj = event_notif.fetch_related_object()
                # otherwise, `obj` will just be `None`
                print(f"Related object: {obj}")

                # you can still fetch the full event, but it will be untyped
                event = event_notif.fetch_event()
                print(f"New event: {event.data}")  # type: ignore

        return jsonify(success=True), 200
    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == "__main__":
    app.run(port=4242)
