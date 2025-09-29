import os

from stripe import StripeClient, Webhook, SignatureVerificationError

from flask import Flask, request


client = StripeClient(
    api_key=os.environ["STRIPE_SECRET_KEY"],
    client_id=os.environ.get("STRIPE_CLIENT_ID"),
)

webhook_secret = os.environ.get("WEBHOOK_SECRET")

app = Flask(__name__)


@app.route("/webhooks", methods=["POST"])
def webhooks():
    payload = request.data.decode("utf-8")
    received_sig = request.headers.get("Stripe-Signature", None)

    try:
        event = Webhook.construct_event(payload, received_sig, webhook_secret)
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
