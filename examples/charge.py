from __future__ import absolute_import, division, print_function

import os

import stripe


stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

print("Attempting charge...")

resp = stripe.Charge.create(
    amount=200,
    currency="usd",
    card="tok_visa",
    description="customer@gmail.com",
)

print("Success: %r" % (resp))
