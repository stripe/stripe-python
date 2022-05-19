# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class CreditReversal(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "treasury.credit_reversal"
