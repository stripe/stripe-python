from __future__ import absolute_import, division, print_function

from typing import Optional
from typing_extensions import Protocol

from stripe.stripe_object import StripeObject


class _Verifiable(Protocol):
    def instance_url(self) -> str:
        ...

    def _request(
        self,
        method: str,
        url: str,
        idempotency_key: Optional[str],
        params: dict,
    ) -> StripeObject:
        ...


class VerifyMixin(object):
    def verify(self: _Verifiable, idempotency_key=None, **params):
        url = self.instance_url() + "/verify"
        return self._request(
            "post", url, idempotency_key=idempotency_key, params=params
        )
