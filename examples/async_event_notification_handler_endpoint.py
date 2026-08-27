"""
async_event_notification_handler_endpoint.py - receive and process event notifications (AKA thin events) like "v1.billing.meter.error_report_triggered" using AsyncEventNotificationHandler.

The async equivalent of event_notification_handler_endpoint.py. In this example, we:
    - write an async fallback callback to handle unrecognized event notifications
    - create a StripeClient called client
    - Initialize an AsyncStripeEventNotificationHandler with the client, webhook secret, and fallback callback
    - register a pre_handle hook that deduplicates events by id before any callback runs
    - register a specific handler for the "v1.billing.meter.error_report_triggered" event notification type
    - await handler.handle_async() to process the received notification webhook body

Note that only your callbacks are awaited. Verifying the signature and parsing the
payload are pure CPU work, so they stay synchronous even here.
"""

import os
from fastapi import FastAPI, Request, Response

from stripe import StripeClient, UnhandledNotificationDetails
from stripe.v2.core import EventNotification
from stripe.events import V1BillingMeterErrorReportTriggeredEventNotification

app = FastAPI()
api_key = os.environ.get("STRIPE_API_KEY", "")
webhook_secret = os.environ.get("WEBHOOK_SECRET", "")

# Webhooks can be delivered more than once, so we track ids we've already
# processed. In production, back this with something durable and shared
# across processes (e.g. Redis or a database table) instead of an in-memory set.
processed_event_ids: set[str] = set()


async def fallback_callback(
    notif: EventNotification,
    client: StripeClient,
    details: UnhandledNotificationDetails,
):
    print(f"Got an unhandled event of type {notif.type}!")


client = StripeClient(api_key)
handler = client.async_notification_handler(webhook_secret, fallback_callback)

# Handles events delivered through a channel that has already authenticated them, such as
# AWS EventBridge or Azure Event Grid. Those payloads carry no Stripe-Signature header.
unverified_handler = client.async_notification_handler_without_verification(
    fallback_callback
)


@handler.pre_handle
@unverified_handler.pre_handle
async def deduplicate_events(
    notif: EventNotification, client: StripeClient
) -> bool:
    """
    Runs before any registered callback. Returning False
    here skips handling entirely for this delivery, which is useful for
    deduplicating webhooks.
    """
    if notif.id in processed_event_ids:
        print(f"Already processed {notif.id}, skipping.")
        return False

    processed_event_ids.add(notif.id)
    return True


# can be anywhere in your codebase; registering on both handlers means either
# endpoint below will route this event type
@handler.on_v1_billing_meter_error_report_triggered
@unverified_handler.on_v1_billing_meter_error_report_triggered
async def handle_meter_error(
    notif: V1BillingMeterErrorReportTriggeredEventNotification,
    client: StripeClient,
):
    # the async variants of the fetch methods keep the whole callback non-blocking
    event = await notif.fetch_event_async()
    print(f"Err! No meter found: {event.data.developer_message_summary}")


@app.post("/webhook")
async def webhook(request: Request):
    webhook_body = await request.body()
    sig_header = request.headers.get("Stripe-Signature", "")

    try:
        await handler.handle_async(webhook_body.decode(), sig_header)
        return Response(status_code=200)
    except Exception as e:
        return Response(content=str(e), status_code=500)


@app.post("/webhook-from-cloud-provider")
async def webhook_from_cloud_provider(request: Request):
    # no signature header to pass along; the channel already authenticated this event
    try:
        body = await request.body()
        await unverified_handler.handle_async(body)
        return Response(status_code=200)
    except Exception as e:
        return Response(content=str(e), status_code=500)
