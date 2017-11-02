from __future__ import absolute_import, division, print_function

#
# This module doesn't serve much purpose anymore. It's only here to maintain
# backwards compatibility.
#
# TODO: get rid of this module in the next major version.
#

import warnings

from stripe import util
from stripe.util import (  # noqa
    convert_array_to_dict,
    convert_to_stripe_object,
)
from stripe.stripe_object import StripeObject  # noqa
from stripe.api_resources.abstract import (  # noqa
    APIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SingletonAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources import *  # noqa


class StripeObjectEncoder(util.json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        warnings.warn(
            '`StripeObjectEncoder` is deprecated and will be removed in '
            'version 2.0 of the Stripe bindings.  StripeObject is now a '
            'subclass of `dict` and is handled natively by the built-in '
            'json library.',
            DeprecationWarning)
        super(StripeObjectEncoder, self).__init__(*args, **kwargs)
