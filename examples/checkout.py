"""
This is a thorough example using Stripe's Checkout Session API for customers paying with a credit card.
    Using checkouts, Stripe handles the collection and processing of sensitive customer data,
    meaning that you don't have to worry about PCI compliance, and customers don't have to trust you to secure their data.
Relevant docs: https://stripe.com/docs/api/checkout/sessions
Video tutorial: https://www.youtube.com/watch?v=8y9RNFc71DA

Get API keys: https://dashboard.stripe.com/apikeys
Credit card acceptance/blocking rules: https://dashboard.stripe.com/settings/radar/rules
"""
import time
# 3rd party
import stripe
# not required in server code
import webbrowser
import os
from contextlib import suppress


def load_dot_env():
    """ Helper funtion that parses and loads local .env file.
    STRIPE_SECRET_KEY=sk_...
    """
    with suppress(FileNotFoundError):
        with open('.env', encoding='utf-8') as dot_env_file:
            for line in iter(lambda: dot_env_file.readline().strip(), ''):
                if not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value


load_dot_env()
stripe.api_key = os.environ['STRIPE_SECRET_KEY']

base_url = 'http://[::1]:5000'      # use localhost (ipv4 is http://127.0.0.1) in development
# base_url = 'https://lenerva.com'  # use domain in production

# in the backend,
#  handle success and cancel redirects
#  ensure that the payment_status == 'paid' before processing the order
s = stripe.checkout.Session.create(
    success_url=f'{base_url}/order/order-id?good',  # success redirect does not imply paid!
    cancel_url=f'{base_url}/order/order-id?cancel',
    line_items=[
        {
            'price_data': {
                'currency': 'USD',  # can be any currency Stripe supports
                'product_data': {
                    'name': "Donation to Your's Truly",
                },
                # Lowest denomination is cents for USD/CAD
                #  If the currency was JPY, 2000 would be 2000 YEN not 20000 YEN
                'unit_amount': 2000  # $20.00
            },
            "quantity": 1,
        },
    ],
    mode='payment',
    customer_email='test@gmail.com',    # default is None
    expires_at=int(time.time()) + 3600  # 1 hour expiry
)
print(s)
# use these cards to test if the checkout session is working according to your expectations
print('''Get more cards from https://stripe.com/docs/testing#cards
4000000000000077 12/24 111 SUCCESS
4000000000000036 12/24 111 ZIP FAIL         [related rule: block on postal fail]
4000000000000101 12/24 111 CVC FAIL         [related rule: block on CVC fail]
4000000000000002 12/24 111 CARD DECLINED
4000000000000069 12/21 111 CARD EXPIRED
4000000000000119 12/24 111 PROCESSING ERROR
''')

input('Press Enter to go to checkout site...')
session_id = s['id']        # use Session['id'] to retrieve session later
webbrowser.open(s['url'])   # use Session['url'] to redirect customers
input('Press Enter to see status and payment status of checkout session...')

# Retrieve the session
checkout_sess = stripe.checkout.Session.retrieve(session_id)
print('status        :', checkout_sess['status'])           # open, complete, expired
print('payment_status:', checkout_sess['payment_status'])   # paid, unpaid, no_payment_required
