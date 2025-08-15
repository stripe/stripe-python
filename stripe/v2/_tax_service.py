# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.tax._automatic_rule_service import AutomaticRuleService


class TaxService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.automatic_rules = AutomaticRuleService(self._requestor)
