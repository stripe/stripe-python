from __future__ import absolute_import, division, print_function


class VerifyMixin(object):
    def verify(self, idempotency_key=None, **params):
        url = self.instance_url() + "/verify"  # type: ignore
        return self._request(  # type: ignore
            "post", url, idempotency_key=idempotency_key, params=params
        )
