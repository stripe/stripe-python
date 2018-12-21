from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource


class CheckoutSession(CreateableAPIResource):
    OBJECT_NAME = 'checkout_session'
