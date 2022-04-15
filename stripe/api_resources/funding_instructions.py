# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class FundingInstructions(CreateableAPIResource, ListableAPIResource):
    OBJECT_NAME = "funding_instructions"

    @classmethod
    def create(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't create a funding instruction without a customer ID. Use customer.create_funding_instruction(...)"
        )

    @classmethod
    def list(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't list funding instructions without a customer ID. Use customer.create_funding_instruction(...)"
        )
