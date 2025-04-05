# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.privacy._redaction_job_service import RedactionJobService


class PrivacyService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.redaction_jobs = RedactionJobService(self._requestor)
