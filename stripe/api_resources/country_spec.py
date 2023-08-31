# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import List
from typing_extensions import Literal


class CountrySpec(ListableAPIResource["CountrySpec"]):
    """
    Stripe needs to collect certain pieces of information about each account
    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](https://stripe.com/docs/connect/required-verification-information).
    """

    OBJECT_NAME = "country_spec"
    default_currency: str
    id: str
    object: Literal["country_spec"]
    supported_bank_account_currencies: Dict[str, List[str]]
    supported_payment_currencies: List[str]
    supported_payment_methods: List[str]
    supported_transfer_countries: List[str]
    verification_fields: StripeObject
