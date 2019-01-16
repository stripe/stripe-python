from __future__ import absolute_import, division, print_function

import os

import stripe
from flask import Flask, request, redirect


stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
stripe.client_id = os.environ.get("STRIPE_CLIENT_ID")

app = Flask(__name__)


@app.route("/")
def index():
    return '<a href="/authorize">Connect with Stripe</a>'


@app.route("/authorize")
def authorize():
    url = stripe.OAuth.authorize_url(scope="read_only")
    return redirect(url)


@app.route("/oauth/callback")
def callback():
    code = request.args.get("code")
    try:
        resp = stripe.OAuth.token(grant_type="authorization_code", code=code)
    except stripe.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{stripe_user_id}</code> is connected.</p>
<p>Click <a href="/deauthorize?stripe_user_id={stripe_user_id}">here</a> to
disconnect the account.</p>
""".format(
        stripe_user_id=resp["stripe_user_id"]
    )


@app.route("/deauthorize")
def deauthorize():
    stripe_user_id = request.args.get("stripe_user_id")
    try:
        stripe.OAuth.deauthorize(stripe_user_id=stripe_user_id)
    except stripe.oauth_error.OAuthError as e:
        return "Error: " + str(e)

    return """
<p>Success! Account <code>{stripe_user_id}</code> is disconnected.</p>
<p>Click <a href="/">here</a> to restart the OAuth flow.</p>
""".format(
        stripe_user_id=stripe_user_id
    )


if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
