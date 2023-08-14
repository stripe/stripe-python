# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import ListableAPIResource


class ReceivedCredit(ListableAPIResource):
    """
    ReceivedCredits represent funds sent to a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) (for example, via ACH or wire). These money movements are not initiated from the FinancialAccount.
    """

    OBJECT_NAME = "treasury.received_credit"

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def create(
            cls,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/received_credits",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


ReceivedCredit.TestHelpers._resource_cls = ReceivedCredit
