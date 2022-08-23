# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource


class CountrySpec(ListableAPIResource):
    """
    Stripe needs to collect certain pieces of information about each account
    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](https://stripe.com/docs/connect/required-verification-information).
    """

    OBJECT_NAME = "country_spec"
