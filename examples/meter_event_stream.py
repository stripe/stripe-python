"""
meter_event_stream.py - use the high-throughput meter event stream to report create billing meter events.

In this example, we:
  - create a meter event session and store the session's authentication token
  - define an event with a payload
  - use the meter_event_stream service accessor in StripeClient to create an event stream that reports this event

This example expects a billing meter with an event_name of 'alpaca_ai_tokens'.  If you have
a different meter event name, you can change it before running this example.
"""

from datetime import datetime, timezone
import stripe

# Global variable for the meter event session
meter_event_session = None


def refresh_meter_event_session(api_key):
    global meter_event_session

    # Check if the session is None or expired
    if meter_event_session is None or datetime.fromisoformat(
        meter_event_session["expires_at"]
    ) <= datetime.now(timezone.utc):
        # Create a new meter event session if the existing session has expired
        client = stripe.StripeClient(api_key)
        meter_event_session = client.v2.billing.meter_event_session.create()


def send_meter_event(meter_event, api_key):
    # Refresh the meter event session if necessary
    refresh_meter_event_session(api_key)
    if not meter_event_session:
        raise RuntimeError("Unable to refresh meter event session")

    # Create a meter event with the current session's authentication token
    client = stripe.StripeClient(meter_event_session["authentication_token"])
    client.v2.billing.meter_event_stream.create(
        params={"events": [meter_event]}
    )


# Set your API key here
api_key = "{{API_KEY}}"
customer_id = "{{CUSTOMER_ID}}"

# Send meter event
send_meter_event(
    {
        "event_name": "alpaca_ai_tokens",
        "payload": {"stripe_customer_id": customer_id, "value": "25"},
    },
    api_key,
)
