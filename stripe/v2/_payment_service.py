# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.v2.payments._off_session_payment_service import (
    OffSessionPaymentService,
)


class PaymentService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.off_session_payments = OffSessionPaymentService(self._requestor)
