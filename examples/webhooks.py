import os

from stripe import Webhook, SignatureVerificationError
from flask import Flask, request

# this is for handling v1-style Snapshot Events.
# To handle v2-style Events, see `event_notification_webhook_handler.py`

webhook_secret = os.environ.get("WEBHOOK_SECRET")

app = Flask(__name__)


@app.route("/webhooks", methods=["POST"])
def webhooks():
    payload = request.data.decode("utf-8")
    received_sig = request.headers.get("Stripe-Signature", None)

    try:
        event = Webhook.construct_event(
            payload, received_sig, webhook_secret, api_key="sk_test_..."
        )
    except ValueError:
        print("Error while decoding event!")
        return "Bad payload", 400
    except SignatureVerificationError:
        print("Invalid signature!")
        return "Bad signature", 400

    print(
        "Received event: id={id}, type={type}".format(
            id=event.id, type=event.type
        )
    )

    return "", 200


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
