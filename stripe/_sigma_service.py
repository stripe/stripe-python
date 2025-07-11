# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.sigma._scheduled_query_run_service import ScheduledQueryRunService
from stripe.sigma._schema_service import SchemaService


class SigmaService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.scheduled_query_runs = ScheduledQueryRunService(self._requestor)
        self.schemas = SchemaService(self._requestor)
