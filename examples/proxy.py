from __future__ import absolute_import, division, print_function

import os

import stripe


stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

clients = (
    stripe.http_client.RequestsClient(
        verify_ssl_certs=stripe.verify_ssl_certs, proxy=proxy
    ),
    stripe.http_client.PycurlClient(
        verify_ssl_certs=stripe.verify_ssl_certs, proxy=proxy
    ),
    stripe.http_client.Urllib2Client(
        verify_ssl_certs=stripe.verify_ssl_certs, proxy=proxy
    ),
)

for c in clients:
    stripe.default_http_client = c
    resp = stripe.Charge.create(
        amount=200,
        currency="usd",
        card="tok_visa",
        description="customer@gmail.com",
    )
    print("Success: %s, %r" % (c.name, resp))
